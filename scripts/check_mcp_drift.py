#!/usr/bin/env python3
"""
Detect drift between tool definitions in skill.json and the live MCP server,
plus consistency checks across the repo's hardcoded business data.

Hard-fails (exit 1) when:
  - a tool documented in skill.json is NOT exposed by the server (name drift —
    callers would hit -32601 Unknown tool, which is exactly the v0.4.0 bug where
    docs said `get_knowledge_entries` but the server exposed `get_latest_knowledge`);
  - documented inputSchema property keys / required fields differ from the server;
  - get_service_packages floors differ from EXPECTED_PRICES (price drift — business
    data is the most drift-prone content and was not covered by the tool-name check);
  - get_contact_info phone/email/address differ from EXPECTED_CONTACT, OR the
    README files' hardcoded contact strings fall out of sync (server-side change OR
    a README edit both caught);
  - README package tables (CN + EN) no longer show the EXPECTED_PRICES floors;
  - the version string differs across skill.json / SKILL.md / README badges /
    JSON-LD (manual version bumps historically missed files).

Non-fatal warning when the server exposes a tool not documented in skill.json.

Config (env):
  MCP_URL     default https://www.dycreative.tech/mcp
  SKILL_JSON  default skill.json

Run locally:   python3 scripts/check_mcp_drift.py
CI:            .github/workflows/mcp-drift-check.yml (on skill.json change + daily)
"""
import json
import os
import re
import sys
import urllib.request

MCP_URL = os.environ.get("MCP_URL", "https://www.dycreative.tech/mcp")
SKILL_JSON = os.environ.get("SKILL_JSON", "skill.json")
TIMEOUT = 15

# Reference package floors documented in README ("参考价"). The price spot-check
# verifies the server's get_service_packages still matches these, so a server-side
# price change forces a README update instead of silently drifting. Business data
# (pricing) is the most drift-prone content and is NOT covered by the tool-name check.
# KEEP IN SYNC with the 套餐概览 / Service Packages table in README.md / README.en.md
# AND with the formatted reference floors appearing elsewhere in those READMEs.
# (定制版 / Custom is 面议 / on-request, so not numerically checked.)
EXPECTED_PRICES = {
    "入门版": 19800,
    "专业版": 58000,
    "旗舰版": 128000,
}

# AI vision (short-video) package floors — same drift risk as the content
# packages above. Names must match the server's aiVisionPackages[].name.
# KEEP IN SYNC with the "AI 视觉服务报价单 / AI Vision Services Price Sheet"
# table in README.md / README.en.md.
EXPECTED_VISION_PRICES = {
    "AI 营销短视频": 2980,
    "AI 电商主图视频": 5800,
    "AI TVC 级定制视频": 19800,
}

# Canonical contact values — the single source of truth. Both the live server
# (get_contact_info) AND the hardcoded contact strings in the READMEs must match.
# Catches drift in either direction: a server-side change OR a README edit.
# phone + email are language-invariant (identical in CN + EN READMEs); the address
# substring is checked against the Chinese README only (the EN README translates it).
# KEEP IN SYNC with the "关于大瑀创意科技 / About" table in README.md / README.en.md.
EXPECTED_CONTACT = {
    "phone": "+86 186-1155-3805",
    "email": "chuluu@dayucreative.tech",
    "address_contains": "萧山区农业大厦1座2005室",
}

# Files checked for contact-info + version consistency.
README_FILES = ["README.md", "README.en.md"]

# Files that must display the reference price floors (content + AI vision).
# READMEs are consumer-facing; references/sales-consultation.md also cites them.
PRICE_FILES = ["README.md", "README.en.md", "references/sales-consultation.md"]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def rpc(method, params=None, rid=1):
    payload = {"jsonrpc": "2.0", "id": rid, "method": method}
    if params is not None:
        payload["params"] = params
    req = urllib.request.Request(
        MCP_URL,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        },
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        body = r.read().decode()
    # server may answer with SSE 'data:' lines
    if "data:" in body:
        for line in body.splitlines():
            if line.startswith("data:"):
                body = line[5:].strip()
                break
    return json.loads(body)


def server_tools():
    rpc("initialize", {
        "protocolVersion": "2025-03-26",
        "capabilities": {},
        "clientInfo": {"name": "drift-check", "version": "0"},
    }, 1)
    data = rpc("tools/list", {}, 2)
    if "error" in data:
        sys.exit(f"FATAL: tools/list returned an error: {data['error']}")
    return {t["name"]: t for t in data["result"]["tools"]}


def documented_tools():
    with open(SKILL_JSON, encoding="utf-8") as f:
        doc = json.load(f)
    out = {}
    for t in doc.get("tools", []):
        schema = t.get("inputSchema", {}) or {}
        out[t["name"]] = {
            "props": set((schema.get("properties") or {}).keys()),
            "required": set(schema.get("required") or []),
        }
    return out


def call_tool(name, arguments=None):
    data = rpc("tools/call", {"name": name, "arguments": arguments or {}}, 3)
    if "error" in data:
        return None, data["error"]
    text = data["result"]["content"][0].get("text", "")
    try:
        return json.loads(text), None
    except Exception:
        return None, "non-JSON response"


def _check_pkg_floors(packages, expected, label, errors, warnings):
    """Compare a server package list's floors against an expected {name: floor} dict."""
    by_name = {}
    for pk in packages:
        nm = pk.get("name") or pk.get("planName")
        if nm:
            by_name[nm] = pk.get("price") or pk.get("monthlyFee") or ""
    for plan, expected_floor in expected.items():
        actual_str = by_name.get(plan)
        if actual_str is None:
            warnings.append(f"  ⚠ {label} price spot-check: '{plan}' not found in server packages")
            continue
        nums = re.findall(r"\d[\d,]*", str(actual_str))
        if not nums:
            warnings.append(f"  ⚠ {label} price spot-check: could not parse number from '{plan}' price '{actual_str}'")
            continue
        actual = int(nums[0].replace(",", ""))
        if actual != expected_floor:
            errors.append(
                f"  ✗ {label} price drift: '{plan}' server floor ¥{actual:,} ≠ documented ¥{expected_floor:,} "
                f"(update README reference price AND the EXPECTED_*_PRICES constant here)"
            )


def check_prices():
    """Spot-check content + AI-vision package floors against the README reference prices."""
    errors, warnings = [], []
    payload, err = call_tool("get_service_packages")
    if err is not None:
        warnings.append(f"  ⚠ price spot-check skipped: get_service_packages unusable ({err})")
        return errors, warnings
    content = payload.get("contentPackages") or payload.get("packages") or []
    vision = payload.get("aiVisionPackages") or []
    if content:
        _check_pkg_floors(content, EXPECTED_PRICES, "content", errors, warnings)
    else:
        warnings.append("  ⚠ content price spot-check skipped: no contentPackages in server response")
    if vision:
        _check_pkg_floors(vision, EXPECTED_VISION_PRICES, "vision", errors, warnings)
    else:
        warnings.append("  ⚠ vision price spot-check skipped: no aiVisionPackages in server response")
    return errors, warnings


def check_contact():
    """Live server contact info AND README hardcoded contacts must match EXPECTED_CONTACT."""
    errors, warnings = [], []
    payload, err = call_tool("get_contact_info")
    if err is not None:
        warnings.append(f"  ⚠ contact spot-check skipped: get_contact_info unusable ({err})")
        return errors, warnings
    s_phone = (payload.get("phone") or "").strip()
    s_email = (payload.get("email") or "").strip()
    s_addr = (payload.get("address") or "").strip()
    if s_phone != EXPECTED_CONTACT["phone"]:
        errors.append(f"  ✗ contact drift: server phone '{s_phone}' ≠ documented '{EXPECTED_CONTACT['phone']}'")
    if s_email != EXPECTED_CONTACT["email"]:
        errors.append(f"  ✗ contact drift: server email '{s_email}' ≠ documented '{EXPECTED_CONTACT['email']}'")
    if EXPECTED_CONTACT["address_contains"] not in s_addr:
        errors.append(
            f"  ✗ contact drift: server address '{s_addr}' missing '{EXPECTED_CONTACT['address_contains']}' "
            f"(update EXPECTED_CONTACT or fix the server)"
        )

    # README hardcoded strings — phone + email are language-invariant.
    for path in README_FILES:
        text = read(path)
        if EXPECTED_CONTACT["phone"] not in text:
            errors.append(f"  ✗ contact drift: {path} missing phone '{EXPECTED_CONTACT['phone']}'")
        if EXPECTED_CONTACT["email"] not in text:
            errors.append(f"  ✗ contact drift: {path} missing email '{EXPECTED_CONTACT['email']}'")
    # Full address substring only in the Chinese README (EN translates it).
    if EXPECTED_CONTACT["address_contains"] not in read("README.md"):
        errors.append(f"  ✗ contact drift: README.md missing address '{EXPECTED_CONTACT['address_contains']}'")
    return errors, warnings


def check_versions():
    """Every version string in the repo must equal skill.json's version."""
    errors = []
    with open(SKILL_JSON, encoding="utf-8") as f:
        skill_version = json.load(f).get("version")
    if not skill_version:
        return ["  ✗ no 'version' field in skill.json (cannot verify version consistency)"]

    # Plain-text occurrences (frontmatter + badges + agent metadata).
    text_checks = [
        ("SKILL.md", r"(?m)^version:\s*([^\s]+)\s*$"),
        ("agents/openai.yaml", r"(?m)^version:\s*([^\s]+)\s*$"),
        ("README.md", r"version-([^\s)-]+)-green"),
        ("README.en.md", r"version-([^\s)-]+)-green"),
    ]
    for path, pat in text_checks:
        m = re.search(pat, read(path))
        found = m.group(1) if m else None
        if found != skill_version:
            errors.append(f"  ✗ version mismatch: {path} has '{found}' but skill.json has '{skill_version}'")

    # JSON-LD softwareVersion in both READMEs.
    for path in README_FILES:
        m = re.search(r'"softwareVersion":\s*"([^"]+)"', read(path))
        found = m.group(1) if m else None
        if found != skill_version:
            errors.append(f"  ✗ version mismatch: {path} JSON-LD softwareVersion has '{found}' but skill.json has '{skill_version}'")
    return errors


def check_readme_prices():
    """Both READMEs must display the content + vision reference floors (¥N,NNN)."""
    errors = []
    for label, expected in [("content", EXPECTED_PRICES), ("vision", EXPECTED_VISION_PRICES)]:
        for plan, val in expected.items():
            formatted = f"¥{val:,}"  # e.g. ¥19,800
            for path in PRICE_FILES:
                if formatted not in read(path):
                    errors.append(
                        f"  ✗ {label} price drift: {path} missing reference floor '{formatted}' for '{plan}' "
                        f"(update the file or the EXPECTED_*_PRICES constant here)"
                    )
    return errors, []


def main():
    print(f"Comparing {SKILL_JSON}  against  {MCP_URL} ...")
    try:
        srv = server_tools()
    except Exception as e:
        sys.exit(f"FATAL: cannot reach MCP server: {e}")
    doc = documented_tools()

    errors, warnings = [], []

    for name, d in doc.items():
        if name not in srv:
            errors.append(
                f"  ✗ '{name}' is documented in skill.json but NOT exposed by the server "
                f"(callers will get -32601 Unknown tool)"
            )
            continue
        s = srv[name]
        sschema = s.get("inputSchema", {}) or {}
        sprops = set((sschema.get("properties") or {}).keys())
        sreq = set(sschema.get("required") or [])

        if d["props"] != sprops:
            missing = d["props"] - sprops
            extra = sprops - d["props"]
            if missing:
                errors.append(f"  ✗ '{name}': documented params missing on server: {sorted(missing)}")
            if extra:
                errors.append(f"  ✗ '{name}': server params not documented in skill.json: {sorted(extra)}")
        if d["required"] != sreq:
            errors.append(
                f"  ✗ '{name}': required mismatch — doc={sorted(d['required'])} server={sorted(sreq)}"
            )

    for name in srv:
        if name not in doc:
            warnings.append(f"  ⚠ '{name}' is exposed by the server but not documented in skill.json")

    p_errors, p_warnings = check_prices()
    errors += p_errors
    warnings += p_warnings

    c_errors, c_warnings = check_contact()
    errors += c_errors
    warnings += c_warnings

    r_errors, r_warnings = check_readme_prices()
    errors += r_errors
    warnings += r_warnings

    errors += check_versions()

    print(f"\nDocumented tools: {len(doc)} | Server tools: {len(srv)}")
    for w in warnings:
        print(w)

    if errors:
        print("\nDRIFT DETECTED:")
        for e in errors:
            print(e)
        print(
            "\nFix: update skill.json (and SKILL.md / README) to match the deployed server, "
            "or rename the server tool and redeploy. For price/contact/version drift, update "
            "the README AND the EXPECTED_* constants in this script."
        )
        sys.exit(1)

    print("\n✓ No drift — tool schemas, prices, contact info, and versions all consistent.")
    if warnings:
        print(f"  ({len(warnings)} non-fatal warning(s) listed above)")


if __name__ == "__main__":
    main()
