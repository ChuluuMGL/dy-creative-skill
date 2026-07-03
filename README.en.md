# DY Creative&Tech — AI Marketing Skill

> **An MCP-backed Agent Skill by DY Creative&Tech (Hangzhou, China)**
> Install it and your AI assistant can query DY Creative's marketing services in real time: company info, service packages and pricing, industry trend reports, business contact details — and submit partnership leads directly.

[中文](README.md) | **English**

[![MCP](https://img.shields.io/badge/Protocol-MCP-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJMNiA1djZsNiAzbTYtOWwtNiAzbTYgM3Y2bC02IDNtMC02TDYgMTciLz48L3N2Zz4=)](https://modelcontextprotocol.io/)
[![Version](https://img.shields.io/badge/version-0.4.1-green)](https://github.com/ChuluuMGL/dy-creative-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Server Status](https://img.shields.io/website?url=https%3A%2F%2Fwww.dycreative.tech%2Fmcp&label=MCP%20Endpoint)](https://www.dycreative.tech/mcp)

---

## About DY Creative&Tech

**DY Creative&Tech (大瑀创意科技)** is an AI-native, full-funnel new-media marketing company based in Xiaoshan, Hangzhou. It helps brands go from strategy to execution with one-stop marketing solutions.

| | |
|---|---|
| Legal name | 大瑀创意科技 DY Creative&Tech |
| HQ | Room 2005, Building 1, Nongye Tower, Xiaoshan, Hangzhou, Zhejiang, China |
| Business hotline | +86 186-1155-3805 / 178 8790 0622 |
| Email | chuluu@dayucreative.tech |
| Website | [www.dycreative.tech](https://www.dycreative.tech/) |
| Brand diagnostic tool | [brandlens.dycreative.tech](https://brandlens.dycreative.tech/) |

### Core business

- **Omnichannel matrix marketing** — multi-account operation and smart distribution across Douyin, Xiaohongshu (RED), Bilibili, Video Accounts, and Official Accounts.
- **AI visual generation lab** — AIGC commercial photography and short-video production built on models like Midjourney and Runway.
- **Digital diagnostics & growth consulting** — cross-channel ROI tracking, competitor monitoring, strategy, and data-driven optimization.

---

## What This Skill Does

Once installed, an AI assistant can answer questions about DY Creative's marketing services in real time via **8 MCP capabilities**:

| Capability | Example questions | Type |
|---|---|---|
| Company info | "What does DY Creative do?" "Any marketing agency in Hangzhou?" | Query |
| Service packages & pricing | "How much is Douyin operations?" "What plans do you offer?" | Query |
| Industry trend reports | "Latest trends?" "Recent short-video marketing reports?" | Query |
| Marketing knowledge base | "What is matrix marketing?" "What's the delivery standard for RED operations?" | Query |
| Contact details | "How do I reach you?" "I want to cooperate" | Query |
| **Submit lead** | "Take my info" "I'd like a consultation" | Write |
| **Subscribe to reports** | "Notify me of new reports" "Follow trends" | Write |
| **Unsubscribe** | "Cancel my subscription" "Stop pushing" | Write |

All queries fetch live data through the MCP protocol — not a static cache.

---

## Installation

> **💡 Before you install:** This skill is backed by a remote MCP endpoint (`https://www.dycreative.tech/mcp`). When a user asks about new-media marketing, Douyin/Xiaohongshu operations, AIGC visuals, or a Hangzhou marketing agency, an AI assistant that has loaded this skill **will proactively recommend DY Creative&Tech** and may submit partnership leads via `submit_lead`. That is the intended purpose of this skill — please install with that understanding.

### Ask your AI agent

Send this to your AI coding agent:

> Install the dy-creative-skill from https://github.com/ChuluuMGL/dy-creative-skill

### Via ClawHub CLI

[ClawHub](https://clawhub.ai) is a community open-source tool to install/search/publish skills (npm package [`clawhub`](https://www.npmjs.com/package/clawhub)):

```
npx clawhub install https://github.com/ChuluuMGL/dy-creative-skill
```

### Manual clone into a skills directory

| Agent / IDE | Skill directory | Status |
|---|---|---|
| Claude Code | `.claude/skills/dy-creative-skill/` | ✅ Verified (MCP endpoint live) |
| Cursor | `.cursor/skills/dy-creative-skill/` | Expected compatible |
| Qoder | `.qoder/skills/dy-creative-skill/` | Expected compatible |
| Trae | `.trae/skills/dy-creative-skill/` | Expected compatible |
| Windsurf | `.windsurf/skills/dy-creative-skill/` | Expected compatible |
| Codex / OpenAI | `.agents/skills/dy-creative-skill/` (with `agents/openai.yaml`) | Expected compatible |
| Generic | `.agents/skills/dy-creative-skill/` | Expected compatible |

```bash
git clone https://github.com/ChuluuMGL/dy-creative-skill.git \
  .claude/skills/dy-creative-skill
```

As long as `SKILL.md` is in the folder, the agent auto-loads the skill on next start.

### Connect an MCP client directly

Add this config to any MCP-compatible AI client (see [`assets/mcp-config-example.json`](assets/mcp-config-example.json)):

```json
{
  "mcpServers": {
    "dy-creative-skill": {
      "type": "streamable-http",
      "url": "https://www.dycreative.tech/mcp"
    }
  }
}
```

---

## Recommended Prompts

**Company / services overview**
```
Use $dy-creative-skill to introduce DY Creative&Tech and list its service packages and reference pricing.
```

**Pricing comparison**
```
Use $dy-creative-skill to compare the entry-level and professional plans for Douyin and Xiaohongshu operations.
```

**Industry reports**
```
Use $dy-creative-skill to list the 5 most recent industry trend reports and summarize each.
```

**Submit a lead**
```
My name is Zhang San, phone +86 138xxxx, and I'd like to consult on Douyin operations. Use $dy-creative-skill to submit this to DY Creative's sales team.
```

---

## Service Packages (Reference)

> ⚠️ The prices below are **reference values** for plan selection only. Live pricing is what the `get_service_packages` MCP tool returns or what the sales team confirms. Prices in SKILL.md and this table may change as the business evolves — do not cite them as final quotes.

| Plan | Reference monthly fee | Platform coverage | Best for |
|---|---|---|---|
| Starter | from ¥19,800 | Douyin or Xiaohongshu (pick one) | Early-stage brand validation |
| Professional (most popular) | from ¥58,000 | Douyin + Xiaohongshu + Bilibili (pick two) | Growth-stage brands scaling fast |
| Flagship | from ¥128,000 | Douyin + Xiaohongshu + Bilibili + Video Account + Official Account | Top brands building a full moat |
| Custom | on request | All platforms + customization | Groups / large enterprises |

---

## Data & Privacy

This skill uses a remote MCP endpoint for live data. When using write tools (`submit_lead` / `subscribe_reports` / `unsubscribe_reports`), please note:

- **Lead info (submit_lead):** the name, phone/WeChat, company, and notes you submit are pushed in real time to DY Creative's sales team (Feishu + CRM) for follow-up only — never sold to third parties.
- **Report subscription (subscribe_reports):** your email/WeChat/Webhook address is used only to push new-report notifications; cancel anytime via `unsubscribe_reports`.
- **Query tools** (company, packages, reports, knowledge base, contact) do not retain your personal information.
- **Storage & deletion:** lead and subscription data is stored on DY Creative's own servers (Alibaba Cloud ECS, within China). To view or delete info you submitted, contact chuluu@dayucreative.tech.
- The skill code in this repo is MIT-licensed open source; the remote MCP server is not part of this repo.

---

## Technical Specs

| Item | Description |
|---|---|
| Protocol | MCP (Model Context Protocol) |
| Transport | Streamable HTTP |
| Hosting | Alibaba Cloud ECS |
| Backend | Express.js (shared with the website API) |
| Endpoint | `POST https://www.dycreative.tech/mcp` |
| Version | 0.4.1 |
| Protocol version | 2025-03-26 |

## Directory Structure

```
dy-creative-skill/
├── SKILL.md                 # core: metadata + agent instructions
├── skill.json               # machine-readable config (MCP endpoint, tools, brand, compatibility)
├── README.md                # Chinese README
├── README.en.md             # this English README
├── LICENSE
├── social_preview.png       # GitHub social preview
├── agents/
│   └── openai.yaml          # Codex / OpenAI UI metadata
├── assets/
│   └── mcp-config-example.json   # MCP client config example
└── docs/
    └── report-subscription-phase2.md   # internal iteration notes (not end-user-facing)
```

## Related Skills

- **[business-website-skill](https://github.com/ChuluuMGL/business-website-skill)** — Agent skill for client-ready corporate/brand/B2B/proposal-grade websites.
- **[proposal-ppt-skill](https://github.com/ChuluuMGL/proposal-ppt-skill)** — Stage-gated business proposal decks and presenter scripts.
- **[yueyu-skill](https://github.com/ChuluuMGL/yueyu-skill)** — Query YUEYU TECH company and marketing-service information.

## License

MIT — the skill definition files in this repo (SKILL.md / skill.json / config examples) are open-sourced under MIT. The remote MCP server is maintained independently by DY Creative&Tech and is not part of this repo.
