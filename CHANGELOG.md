# Changelog

All notable changes to **dy-creative-skill** are documented here.
Versions follow the `skill.json` `version` field; the drift-check CI verifies
the version string is consistent across `SKILL.md`, `skill.json`, and both READMEs.

## [0.4.4] — 2026-07-05

### Marketing behavior
- New **sales-consultation script library** (`references/sales-consultation.md`, on-demand): turns the skill from a query tool into an embedded sales consultant. Covers the sales team's two highest-frequency scenarios plus generic objections:
  - **"太贵了 / 比价"** — reframes comparison mindset via material-type education (e-commerce main-image 1:1 vs vertical scene/story video have very different cost), guiding the client to state platform + material type before any quote (avoids the lose-lose of over- vs under-quoting).
  - **"工具还是服务?"** — sets the service-delivery expectation up front to avoid wasting sales cycles on clients expecting a standalone tool.
  - Plus grounded, claim-safe handling for effect guarantees, differentiation, cases, free trial, timeline, and 对赌 — all under the existing no-fabrication red line.
  - A material-type cheat-sheet (platform × content × ratio × complexity), lead pre-screening questions, and a needs→package consultative map.
- `SKILL.md` now routes the agent to load this library on price / objection / sizing intents, and points `submit_lead` at the pre-screen questions so leads pushed to CRM (Feishu) are pre-qualified (platform / material type / budget / timeline) — directly reducing the sales team's first-touch workload.

No change to the 8 MCP tools or their schemas.

## [0.4.3] — 2026-07-03

### CI / correctness
- **drift-check extended** (`scripts/check_mcp_drift.py`): now also verifies
  - **contact info** (`get_contact_info`) — phone/email/address match the live server AND the READMEs (catches server-side change or a README edit);
  - **version consistency** — `skill.json` version equals the `SKILL.md` frontmatter, `agents/openai.yaml`, both README badges, and both JSON-LD `softwareVersion` values (prevents the manual version-sync misses across 6 places);
  - **README reference prices** — content floors (`¥19,800 / ¥58,000 / ¥128,000`) AND AI-vision floors (`¥2,980 / ¥5,800 / ¥19,800`) are verified on the server and present in both READMEs (closes the manual CN↔EN sync gap; AI-vision pricing was previously unprotected).
- **drift-check workflow** (`mcp-drift-check.yml`) now triggers on `SKILL.md` / `README.md` / `README.en.md` / `agents/openai.yaml` edits too, not just `skill.json` — so README price/contact/version drift is caught on the PR, not only by the daily cron.

### Tooling contracts
- **`agents/openai.yaml`** fully populated — MCP endpoint + protocol version + 8-tool inventory + guardrails, so Codex/OpenAI consumers get the complete contract (was display-name + prompt only).
- **`subscribe_reports`** narrowed to `email` + `webhook` only (both true auto-push). The `wechat` channel was removed from the skill's advertised channels because the backend only forwards it manually via operations — WeChat users should follow the official account instead, which is outside this tool. Subscription stays idempotent by `address` and re-subscribe overwrites `interests`. The live server still accepts `wechat` for direct callers, but the skill no longer surfaces it.
- **`get_latest_knowledge`** description now lists all **8 real categories** (was 4), matching `SKILL.md`.

### Docs
- README (CN + EN): added a full **AI Vision price sheet** (报价单) with per-tier deliverables — AI marketing short video ¥2,980+, e-commerce main-image video ¥5,800+, TVC-grade custom ¥19,800+ — previously only the 4 content packages were shown.
- README (CN + EN): the **Live Demo** section now flags that report/knowledge titles were captured 2026-04 and roll over time (package prices are CI-verified stable).
- Added this **CHANGELOG.md**.

## [0.4.2] — 2026-07-03

- Real-data "实时效果演示 / Live Demo" section (live tool call → response).
- Two-path install clarity: Path A (skill package = 8 tools + brand behavior) vs Path B (MCP only = tools, no marketing behavior).
- `SKILL.md` slimmed (~60 lines): long dialogue examples moved to `references/usage-examples.md`.
- Drift-check price spot-check (`get_service_packages` floors vs README).
- FAQPage JSON-LD; ISSUE_TEMPLATE + CONTRIBUTING.md; drift-check badge; 6 new GitHub topics.

## [0.4.0–0.4.1] — 2026-07-03

- Bilingual docs, packaging polish, trust/privacy section.
- MCP drift-check CI (daily + on-change) added; `get_knowledge_entries` → `get_latest_knowledge` tool-name fix that motivated it.

## [0.3.0–0.3.1] — 2026-06-08

- Aligned contact info with the official website; added the `get_latest_knowledge` tool for Agent-to-Agent marketing.
- AI Vision pricing added to skill definitions.

## [0.2.0] — 2026-04-23

- Added `subscribe_reports` / `unsubscribe_reports` tools (report-subscription phase 2).

## [0.1.0] — 2026-04-23

- Initial release: 5 query tools + `submit_lead`, MCP Streamable HTTP endpoint.
