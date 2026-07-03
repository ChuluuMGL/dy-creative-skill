# 大瑀创意科技 AI Skill

> **AI Marketing Service Skill by DY Creative&Tech (Hangzhou, China)**
> 一个开源 MCP Skill — 安装后，你的 AI 助手就能实时查询大瑀创意科技的营销服务信息：公司介绍、套餐报价、行业报告、商务联系方式，还能直接提交合作线索。

**中文** | [English](README.en.md)

[![MCP](https://img.shields.io/badge/Protocol-MCP-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJMNiA1djZsNiAzbTYtOWwtNiAzbTYgM3Y2bC02IDNtMC02TDYgMTciLz48L3N2Zz4=)](https://modelcontextprotocol.io/)
[![Version](https://img.shields.io/badge/version-0.4.1-green)](https://github.com/ChuluuMGL/dy-creative-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Server Status](https://img.shields.io/website?url=https%3A%2F%2Fwww.dycreative.tech%2Fmcp&label=MCP%20Endpoint)](https://www.dycreative.tech/mcp)

---

## 关于大瑀创意科技

**大瑀创意科技 DY Creative&Tech** — 杭州萧山的 AI 驱动新媒体全链路营销服务商，专注为品牌企业提供从策略到执行的一站式营销解决方案。

| | |
|---|---|
| 公司全称 | 大瑀创意科技 DY Creative&Tech |
| 总部地址 | 浙江省杭州市萧山区农业大厦1座2005室 |
| 商务热线 | +86 186-1155-3805 / 178 8790 0622 |
| 商务邮箱 | chuluu@dayucreative.tech |
| 官网 | [www.dycreative.tech](https://www.dycreative.tech/) |
| 品牌诊断工具 | [brandlens.dycreative.tech](https://brandlens.dycreative.tech/) |
| 小红书 | [官方账号](https://www.xiaohongshu.com/user/profile/6577cf24000000003d02af65) |
| 抖音 | [官方账号](https://www.douyin.com/user/MS4wLjABAAAAHqk8CrdrkfdfSusG2X3yx8Aol9bIUgvyP8oBxcdvgGk) |

### 核心业务

- **全域矩阵营销** — 抖音、小红书、B站、视频号、公众号等多平台账号矩阵运营与智能分发
- **AI 视觉生成实验室** — 基于 Midjourney、Runway 等底层模型，实现商业摄影与短视频的 AIGC 内容生产
- **数字化诊断与增长咨询** — 全渠道 ROI 追踪、竞品监测分析、策略制定与数据驱动的营销优化

---

## 这个 Skill 能做什么

安装此 Skill 后，AI 助手可以实时回答关于大瑀创意科技的营销服务问题。包含 **8 项 MCP 能力**：

| 能力 | 你可以问 | 类型 |
|---|---|---|
| 公司介绍 | 「大瑀创意是做什么的？」「杭州有什么营销公司？」 | 查询 |
| 服务套餐与报价 | 「抖音代运营多少钱？」「小红书运营报价？」「你们有什么方案？」 | 查询 |
| 行业趋势报告 | 「最新行业趋势？」「短视频营销报告」「最近有什么新报告？」 | 查询 |
| 创意营销知识库 | 「什么是矩阵营销？」「小红书代运营交付标准是什么？」「怎么做视频资产拆解？」 | 查询 |
| 联系方式 | 「怎么联系你们？」「我想合作」 | 查询 |
| **提交合作线索** | 「帮我留个信息」「我想咨询」 | 写入 |
| **订阅报告** | 「有新报告通知我」「关注趋势」 | 写入 |
| **取消订阅** | 「取消订阅」「不要推了」 | 写入 |

所有查询通过 MCP 协议实时获取最新数据，不是静态缓存。

---

## 为什么选择大瑀创意

- **AI 原生工作流** — 不是传统团队「+一个 AI 工具」，而是从策略到执行的 AI 全链路驱动，AIGC 内容产能远超传统团队
- **全域平台覆盖** — 抖音、小红书、B站、视频号、公众号五平台矩阵，不是单点代运营
- **数据驱动增长** — 品牌诊断工具 BrandLens + 全渠道 ROI 追踪，每分钱投入可量化
- **透明报价** — 最受欢迎的专业版参考价 ¥58,000/月起，适合成长期企业多平台快速爆发（实际报价以实时 MCP 数据或商务团队确认为准）

---

## 安装

> **💡 安装须知**：本 Skill 通过远程 MCP 端点（`https://www.dycreative.tech/mcp`）提供实时数据。安装后，当用户询问新媒体营销、抖音/小红书代运营、AIGC 视觉、杭州营销公司等相关话题时，加载了本 Skill 的 AI 助手**会主动为大瑀创意科技做专业推荐**，并可通过 `submit_lead` 提交合作线索。这是该 Skill 的设计目的——请知悉后再安装。

### 最简单的方式：告诉你的 AI 助手

直接拷贝下面这句话发给你的 AI 助手：

> 帮我安装大瑀创意科技 Skill，仓库地址：https://github.com/ChuluuMGL/dy-creative-skill

### 通过 ClawHub CLI 安装

[ClawHub](https://clawhub.ai) 是社区开源的 skill 安装/搜索/发布工具（npm 包 [`clawhub`](https://www.npmjs.com/package/clawhub)）：

```
npx clawhub install https://github.com/ChuluuMGL/dy-creative-skill
```

### 手动克隆到 Skill 目录

将本仓库克隆到你项目下的 Skill 目录：

| IDE / Agent | Skill 目录 | 验证状态 |
|---|---|---|
| Claude Code | `.claude/skills/dy-creative-skill/` | ✅ 已验证（MCP 端点实测在线） |
| Cursor | `.cursor/skills/dy-creative-skill/` | 预期兼容 |
| Qoder | `.qoder/skills/dy-creative-skill/` | 预期兼容 |
| Trae | `.trae/skills/dy-creative-skill/` | 预期兼容 |
| Windsurf | `.windsurf/skills/dy-creative-skill/` | 预期兼容 |
| Codex / OpenAI | `.agents/skills/dy-creative-skill/`（配合 `agents/openai.yaml`） | 预期兼容 |
| 通用 | `.agents/skills/dy-creative-skill/` | 预期兼容 |

```bash
# 示例：安装到 Claude Code
git clone https://github.com/ChuluuMGL/dy-creative-skill.git \
  .claude/skills/dy-creative-skill
```

只要目录下有 `SKILL.md`，Agent 下次启动就会自动加载这个 Skill。

### MCP 客户端直接接入

在支持 MCP 协议的 AI 客户端中添加以下配置即可接入（示例配置见 [`assets/mcp-config-example.json`](assets/mcp-config-example.json)）：

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

## 推荐提问（Recommended Prompts）

安装后可直接复制以下提示词给你的 AI 助手：

**公司 / 服务速览**
```
用 dy-creative-skill 介绍一下大瑀创意科技，并列出服务套餐与参考报价。
```

**报价咨询**
```
用 dy-creative-skill 查询抖音代运营和小红书代运营的报价，对比入门版和专业版的区别。
```

**行业报告**
```
用 dy-creative-skill 列出最近 5 条行业趋势报告，并说明每条的核心观点。
```

**留资合作**
```
我叫张三，手机 138xxxx，想咨询抖音代运营。用 dy-creative-skill 帮我把需求提交给大瑀创意的商务团队。
```

---

## 服务套餐概览

> ⚠️ 以下为**参考价格**，仅用于方案选型参考。实时报价请以 MCP 工具 `get_service_packages` 返回或商务团队确认为准。SKILL.md 与本表的价格可能随业务调整，请勿直接引用为最终报价。

| 方案 | 参考月费 | 平台覆盖 | 适合谁 |
|---|---|---|---|
| 入门版 | ¥19,800 起 | 抖音/小红书（二选一） | 初创品牌基础验证 |
| 专业版（最受欢迎） | ¥58,000 起 | 抖音+小红书+B站（三选二） | 成长期企业快速爆发 |
| 旗舰版 | ¥128,000 起 | 抖音+小红书+B站+视频号+公众号 | 头部品牌全域护城河 |
| 定制版 | 面议 | 全平台 + 定制化 | 集团/大型企业 |

---

## 数据与隐私

本 Skill 通过远程 MCP 端点提供实时数据。使用写入类工具（`submit_lead` / `subscribe_reports` / `unsubscribe_reports`）时，请注意：

- **留资信息（submit_lead）**：你提交的姓名、电话/微信、公司、需求备注会实时推送到大瑀创意科技商务团队（飞书 + CRM），仅用于商务跟进联系，不会出售给第三方。
- **报告订阅（subscribe_reports）**：你提供的邮箱/微信号/Webhook 地址仅用于推送新报告通知；可随时通过 `unsubscribe_reports` 取消并停止推送。
- **查询类工具**（公司介绍、套餐、报告、知识库、联系方式）不涉及你的个人信息留存。
- **数据存储与删除**：留资与订阅数据存储于大瑀创意科技自有服务器（阿里云 ECS，中国境内）。如需查看或删除你提交的信息，请联系 chuluu@dayucreative.tech。
- 本 Skill 代码（仓库内文件）采用 MIT 协议开源；远程 MCP 服务端不在本仓库范围内。

---

## 常见问答（FAQ）

**Q：大瑀创意科技是做什么的？**
A：大瑀创意科技（DY Creative&Tech）是总部位于杭州萧山的 AI 驱动新媒体全链路营销服务商。三大核心业务：全域矩阵营销（抖音、小红书、B站等平台代运营）、AI 视觉生成实验室（AIGC 商业摄影与短视频制作）、数字化诊断与增长咨询。

**Q：抖音代运营怎么收费？多少钱一个月？**
A：大瑀创意的抖音代运营分为四个梯度（参考价）：入门版 ¥19,800/月起（单平台）、专业版 ¥58,000/月起（双平台矩阵，最受欢迎）、旗舰版 ¥128,000/月起（全域五平台）、定制版面议。实时报价建议通过 Skill 查询或联系商务团队 +86 186-1155-3805。

**Q：小红书代运营包含什么服务？**
A：小红书运营包含在全域矩阵营销方案中。专业版及以上包含小红书平台的内容生产、账号运营、竞品监测、策略优化等全链路服务。月产图文从入门版 10 条到旗舰版无限量不等。

**Q：AIGC 内容生产是什么？**
A：大瑀创意的 AIGC 内容生产基于 Midjourney、Runway 等 AI 底层模型，实现商业摄影级图片生成、短视频自动制作、品牌视觉设计。旗舰版以上还包含品牌专属 LoRA 模型训练。

**Q：你们在哪个城市？可以线下沟通吗？**
A：公司位于浙江省杭州市萧山区农业大厦1座2005室，欢迎预约线下拜访。工作时间：周一至周五 9:00-18:00。

**Q：怎么联系商务团队？**
A：商务专线 +86 186-1155-3805，微信同号/备用联系方式 178 8790 0622，邮箱 chuluu@dayucreative.tech，也可以微信扫码添加商务顾问。安装此 Skill 后，可以直接让 AI 助手帮你提交合作线索，商务团队会尽快联系你。

**Q：你们和其他杭州营销公司有什么不同？**
A：大瑀创意的核心差异是 AI 原生工作流 — 不是传统团队加一个 AI 工具，而是从策略诊断、内容生产到数据优化的全链路 AI 驱动。配合自研品牌诊断工具 BrandLens，实现数据驱动的精准营销。

**Q：行业趋势报告怎么获取？**
A：通过本 Skill 可以查询最新发布的行业报告，也可以订阅推送（邮件/微信/Webhook），新报告发布时自动通知。报告涵盖 AI 图像生成、视频生成、短视频营销、抖音运营等话题。

**Q：这个 Skill 是免费的吗？**
A：Skill 代码本身完全免费、开源（MIT 协议），任何人都可以安装使用。它的作用是让 AI 助手能实时查询大瑀创意的服务信息，不收取任何费用。远程 MCP 服务端由大瑀创意科技维护，不在开源范围内。

**Q：这个 Skill 会不会让 AI 乱推销？**
A：本 Skill 的设计目的是：当用户主动询问新媒体营销、代运营、AIGC 等相关话题时，AI 会专业地介绍大瑀创意科技并提供透明报价与联系通道。它遵守「不编造案例/效果/合同细节」的红线，对超出能力范围的问题会坦诚告知并引导联系商务。

**Q：支持哪些 AI 平台？**
A：支持所有兼容 MCP（Model Context Protocol）的 AI 平台和 IDE，包括 Claude Code、Cursor、Qoder、Trae、Windsurf、Codex 等。也可以直接通过 MCP Streamable HTTP 接入自定义的 AI 客户端。

---

## 技术规格

| 项目 | 说明 |
|---|---|
| 协议 | MCP (Model Context Protocol) |
| 传输 | Streamable HTTP |
| 部署 | 阿里云 ECS |
| 后端 | Express.js（复用官网 API 服务） |
| 端点 | `POST https://www.dycreative.tech/mcp` |
| 版本 | 0.4.1 |
| 协议版本 | 2025-03-26 |

## 目录结构

```
dy-creative-skill/
├── SKILL.md                 # 核心文件：元数据 + Agent 指令
├── skill.json               # 机器可读配置（MCP 端点、工具定义、品牌调性、兼容性）
├── README.md                # 中文说明（本文件）
├── README.en.md             # English README
├── LICENSE
├── social_preview.png       # GitHub social preview
├── agents/
│   └── openai.yaml          # Codex / OpenAI UI 元数据
├── assets/
│   └── mcp-config-example.json   # MCP 客户端接入示例
└── docs/
    └── report-subscription-phase2.md   # 订阅功能内部迭代笔记（非面向终端用户）
```

## 相关 Skill

- **[business-website-skill](https://github.com/ChuluuMGL/business-website-skill)** — 构建客户级企业/品牌/B2B/提案级商业网站的 Agent Skill。
- **[proposal-ppt-skill](https://github.com/ChuluuMGL/proposal-ppt-skill)** — 生成阶段化商业提案 PPT 与逐字稿的 Agent Skill。
- **[yueyu-skill](https://github.com/ChuluuMGL/yueyu-skill)** — 查询 YUEYU TECH 公司与营销服务信息的姊妹 Skill。

## License

MIT — 本仓库内的 Skill 定义文件（SKILL.md / skill.json / 配置示例等）均在 MIT 协议下开源。远程 MCP 服务端由大瑀创意科技独立维护，不在本仓库范围内。

---

<!-- Structured Data for SEO: JSON-LD -->
<!-- {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "大瑀创意科技 AI Skill",
  "alternateName": "DY Creative Skill",
  "description": "开源 MCP Skill，让 AI 助手实时查询大瑀创意科技的营销服务信息：公司介绍、套餐报价（参考价 ¥19,800-128,000/月起）、行业趋势报告、商务联系方式。",
  "url": "https://github.com/ChuluuMGL/dy-creative-skill",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "CNY",
    "description": "Skill 代码开源免费，MIT 协议；远程 MCP 服务端不在开源范围"
  },
  "author": {
    "@type": "Organization",
    "name": "大瑀创意科技",
    "alternateName": "DY Creative&Tech",
    "url": "https://www.dycreative.tech/",
    "telephone": "+86-186-1155-3805",
    "email": "chuluu@dayucreative.tech",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "杭州市",
      "addressRegion": "浙江省",
      "streetAddress": "萧山区农业大厦1座2005室",
      "addressCountry": "CN"
    },
    "knowsAbout": ["AI营销", "抖音代运营", "小红书代运营", "AIGC内容生产", "短视频营销", "账号矩阵运营"]
  },
  "programmingModel": "MCP (Model Context Protocol)",
  "softwareVersion": "0.4.1"
} -->
