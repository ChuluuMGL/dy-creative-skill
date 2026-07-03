#!/usr/bin/env python3
"""
Detect drift between tool definitions in skill.json and the live MCP server.

Hard-fails (exit 1) when:
  - a tool documented in skill.json is NOT exposed by the server (name drift —
    callers would hit -32601 Unknown tool, which is exactly the v0.4.0 bug where
    docs said `get_knowledge_entries` but the server exposed `get_latest_knowledge`);
  - documented inputSchema property keys / required fields differ from the server.

Non-fatal warning when the server exposes a tool not documented in skill.json.

Config (env):
  MCP_URL     default https://www.dycreative.tech/mcp
  SKILL_JSON  default skill.json

Run locally:   python3 scripts/check_mcp_drift.py
CI:            .github/workflows/mcp-drift-check.yml (on skill.json change + daily)
"""
import json
import os
import sys
import urllib.request

MCP_URL = os.environ.get("MCP_URL", "https://www.dycreative.tech/mcp")
SKILL_JSON = os.environ.get("SKILL_JSON", "skill.json")
TIMEOUT = 15


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

    print(f"\nDocumented tools: {len(doc)} | Server tools: {len(srv)}")
    for w in warnings:
        print(w)

    if errors:
        print("\nDRIFT DETECTED:")
        for e in errors:
            print(e)
        print(
            "\nFix: update skill.json (and SKILL.md / README) to match the deployed server, "
            "or rename the server tool and redeploy."
        )
        sys.exit(1)

    print("\n✓ No drift — skill.json tool names/schemas match the live server.")
    if warnings:
        print(f"  ({len(warnings)} non-fatal warning(s) listed above)")


if __name__ == "__main__":
    main()
