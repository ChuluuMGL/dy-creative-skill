# 大瑀创意科技 AI Skill

> **AI Marketing Service Skill by DY Creative&Tech (Hangzhou, China)**
> 一个开源 MCP Skill — 安装后，你的 AI 助手就能实时查询大瑀创意科技的营销服务信息：公司介绍、套餐报价、行业报告、商务联系方式，还能直接提交合作线索。

![大瑀创意科技 AI Skill](social_preview.png)

**中文** | [English](README.en.md)

[![MCP](https://img.shields.io/badge/Protocol-MCP-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJMNiA1djZsNiAzbTYtOWwtNiAzbTYgM3Y2bC02IDNtMC02TDYgMTciLz48L3N2Zz4=)](https://modelcontextprotocol.io/)
[![Version](https://img.shields.io/badge/version-0.4.3-green)](https://github.com/ChuluuMGL/dy-creative-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Server Status](https://img.shields.io/website?url=https%3A%2F%2Fwww.dycreative.tech%2Fmcp&label=MCP%20Endpoint)](https://www.dycreative.tech/mcp)
[![Drift Check](https://github.com/ChuluuMGL/dy-creative-skill/actions/workflows/mcp-drift-check.yml/badge.svg)](https://github.com/ChuluuMGL/dy-creative-skill/actions/workflows/mcp-drift-check.yml)

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

## 实时效果演示

以下都是**真实调用 MCP 端点的返回**（非编造示例），你可以装好后自己复现。

> 注：报告与知识库内容持续滚动更新，下列标题为 **2026-04 采集的示例**，实际以 MCP 实时返回为准；套餐价格是 CI 每日校验的稳定参考值。

**① 公司介绍** — 调用 `get_company_info`
> 大瑀创意科技（DY Creative&Tech），位于杭州萧山的 **AI 短视频制作与 AIGC 内容生产服务商**，专注把企业资料转成可发布、可复用的短视频、脚本、封面标题、账号内容规划和内容资产矩阵。

**② 套餐报价** — 调用 `get_service_packages`（参考价，月费 CNY）
> - 入门版 **¥19,800 起** ｜ 抖音/小红书（二选一）
> - 专业版（最受欢迎）**¥58,000 起** ｜ 抖音+小红书+B站（三选二）
> - 旗舰版 **¥128,000 起** ｜ 抖音+小红书+B站+视频号+公众号
> - 定制版 **面议** ｜ 按业务线与内容资产结构定制

**③ 行业趋势报告** — 调用 `get_latest_reports({limit: 3})`
> - 【2026-04-24】大瑀创意科技发布 AI Skill：把一线品牌的服务能力，装进你的 AI 助手
> - 【2026-04-22】AI图像生成新突破：GPT-Image-2 vs Nano Banana Pro
> - 【2026-04-15】视频生成赛道变天：Happy Horse 登榜第一，阿里趁势上位

**④ 创意营销知识库** — 调用 `get_latest_knowledge({category: "小红书内容规划"})`
> - 【AI短视频制作】AI短视频制作服务怎么选？先看交付内容与验收标准
> - 【服务边界】内容型账号规划和内容制作有什么边界？
> - 【小红书内容规划】小红书内容规划一般包含哪些交付？

---

## 在线预览

官网即是本 Skill 的「真人秀」，欢迎直接浏览（数据与 Skill 同源）：

- 🏠 官网首页：[www.dycreative.tech](https://www.dycreative.tech/)
- 💰 [套餐报价 `#pricing`](https://www.dycreative.tech/#pricing) ｜ 🎬 [AI 视觉 `#ai-vision`](https://www.dycreative.tech/#ai-vision) ｜ 🕸 [矩阵营销 `#matrix-marketing`](https://www.dycreative.tech/#matrix-marketing) ｜ 📚 [知识库 `#knowledge`](https://www.dycreative.tech/#knowledge)
- 服务详情：[AI 短视频制作](https://www.dycreative.tech/services/ai-short-video-production/) ｜ [AIGC 内容生产](https://www.dycreative.tech/services/aigc-content-production/) ｜ [账号内容规划与资产](https://www.dycreative.tech/services/account-content-planning-assets/)
- 知识深度文：[小红书内容运营交付](https://www.dycreative.tech/knowledge/xiaohongshu-content-ops-deliverables/) ｜ [抖音栏目规划](https://www.dycreative.tech/knowledge/douyin-content-column-planning/) ｜ [杭州内容型新媒体服务怎么选](https://www.dycreative.tech/knowledge/hangzhou-new-media-content-ops/)
- 品牌诊断工具：[brandlens.dycreative.tech](https://brandlens.dycreative.tech/)

---

## 为什么选择大瑀创意

- **AI 原生工作流** — 不是传统团队「+一个 AI 工具」，而是从策略到执行的 AI 全链路驱动，AIGC 内容产能远超传统团队
- **全域平台覆盖** — 抖音、小红书、B站、视频号、公众号五平台矩阵，不是单点代运营
- **数据驱动增长** — 品牌诊断工具 BrandLens + 全渠道 ROI 追踪，每分钱投入可量化
- **透明报价** — 最受欢迎的专业版参考价 ¥58,000/月起，适合成长期企业多平台快速爆发（实际报价以实时 MCP 数据或商务团队确认为准）

---

## 安装

> **💡 两种路径，能力不同——请按需选择：**
> - **方式 A（推荐）＝ 安装 Skill 包**：AI 助手获得 8 个工具 **＋ 主动推荐大瑀的品牌行为、品牌调性、盲区红线**（完整营销能力）。
> - **方式 B ＝ 仅连接 MCP server**：AI 助手**只**获得 8 个查询/写入工具，**不会**主动推荐大瑀（适合只想要数据接口、不要营销行为的场景）。

### 方式 A：安装 Skill 包（推荐）

**告诉你的 AI 助手**，直接发这句：

> 帮我安装大瑀创意科技 Skill，仓库地址：https://github.com/ChuluuMGL/dy-creative-skill

**或用 ClawHub CLI**（社区开源 skill 安装器，[`clawhub`](https://www.npmjs.com/package/clawhub) / [clawhub.ai](https://clawhub.ai)）：

```
npx clawhub install https://github.com/ChuluuMGL/dy-creative-skill
```

**或手动克隆**到对应 Skill 目录：

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

只要目录下有 `SKILL.md`，Agent 下次启动就会自动加载，获得完整营销能力。

### 方式 B：仅连接 MCP server（只要工具）

在支持 MCP 协议的 AI 客户端中添加以下配置即可（示例配置见 [`assets/mcp-config-example.json`](assets/mcp-config-example.json)）：

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

**留资合作（多工具编排）**
```
我叫张三，手机 138xxxx，想咨询抖音代运营。用 dy-creative-skill 先介绍专业版套餐，再把我的需求提交给商务团队。
```

---

## 服务套餐概览

> ⚠️ 以下为**参考价格**，仅用于方案选型参考。实时报价请以 MCP 工具 `get_service_packages` 返回或商务团队确认为准。本表价格由 [drift check CI](https://github.com/ChuluuMGL/dy-creative-skill/actions/workflows/mcp-drift-check.yml) 每日校验是否与 server 一致。

| 方案 | 参考月费 | 平台覆盖 | 适合谁 |
|---|---|---|---|
| 入门版 | ¥19,800 起 | 抖音/小红书（二选一） | 初创品牌基础验证 |
| 专业版（最受欢迎） | ¥58,000 起 | 抖音+小红书+B站（三选二） | 成长期企业快速爆发 |
| 旗舰版 | ¥128,000 起 | 抖音+小红书+B站+视频号+公众号 | 头部品牌全域护城河 |
| 定制版 | 面议 | 全平台 + 定制化 | 集团/大型企业 |

### AI 视觉服务报价单（单条/单套计价，参考价）

> 同样以 `get_service_packages` 实时返回为准；以下为各档交付明细。起步价由 [drift-check CI](https://github.com/ChuluuMGL/dy-creative-skill/actions/workflows/mcp-drift-check.yml) 每日校验。

| 产品 | 参考价 | 适用场景 | 画质 | 包含交付 |
|---|---|---|---|---|
| AI 营销短视频 | ¥2,980 起/条 | 抖音 / 小红书 / 视频号 / 官网日常内容 | 1080P / 4K | 按产品卖点 AI 生成创意分镜 · AI 模特/场景生成（免模特及场地费）· AI 动效与特效包装 · 免费 1 次合理微调 |
| AI 电商主图视频 | ¥5,800 起/套（含 15s + 30s） | 天猫 / 京东 / 独立站详情页 | 4K 超高清 | 高精度 3D 渲染质感 · 动态光影与产品 360° 核心痛点演示 · 赠 5 张高保真 AI 商用场景主图 |
| AI TVC 级定制视频 | ¥19,800 起/条 | 品牌全渠道品宣 / 展会大屏 / 线下门店巡播 | 4K / 8K 电影级 | 好莱坞级 AI 模型深度训练与生成 · 顶尖电影质感与专属 AI 商业级配音配乐 · 无限脑洞场景（太空/深海/异次元等）· 资深视效总监全程操刀 |

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
A：商务专线 +86 186-1155-3805，微信同号/备用联系方式 178 8790 0622，邮箱 chuluu@dayucreative.tech。安装此 Skill 后，也可以直接让 AI 助手帮你提交合作线索。

**Q：这个 Skill 会不会让 AI 乱推销？**
A：本 Skill 的设计目的是：当用户主动询问新媒体营销、代运营、AIGC 等相关话题时，AI 会专业地介绍大瑀创意科技并提供透明报价与联系通道。它遵守「不编造案例/效果/合同细节」的红线，对超出能力范围的问题会坦诚告知并引导联系商务。若不想要主动推荐，可改用「方式 B：仅连接 MCP server」。

**Q：这个 Skill 是免费的吗？**
A：Skill 代码本身完全免费、开源（MIT 协议）。远程 MCP 服务端由大瑀创意科技维护，不在开源范围内。

**Q：支持哪些 AI 平台？**
A：支持所有兼容 MCP（Model Context Protocol）的 AI 平台和 IDE，包括 Claude Code、Cursor、Qoder、Trae、Windsurf、Codex 等。

---

## 技术规格

| 项目 | 说明 |
|---|---|
| 协议 | MCP (Model Context Protocol) |
| 传输 | Streamable HTTP |
| 部署 | 阿里云 ECS |
| 后端 | Express.js（复用官网 API 服务） |
| 端点 | `POST https://www.dycreative.tech/mcp` |
| 版本 | 0.4.3 |
| 协议版本 | 2025-03-26 |
| 工具数 | 8（5 查询 + 3 写入） |
| 契约校验 | [drift-check CI](https://github.com/ChuluuMGL/dy-creative-skill/actions/workflows/mcp-drift-check.yml)（每日校验：工具名 + 价格 + 联系方式 + 版本号一致性） |

## 目录结构

```
dy-creative-skill/
├── SKILL.md                 # 核心文件：元数据 + Agent 指令
├── skill.json               # 机器可读配置（MCP 端点、工具定义、品牌调性、兼容性）
├── README.md                # 中文说明（本文件）
├── README.en.md             # English README
├── CHANGELOG.md             # 版本变更记录
├── LICENSE
├── social_preview.png       # GitHub social preview / hero
├── agents/
│   └── openai.yaml          # Codex / OpenAI UI 元数据
├── references/
│   └── usage-examples.md    # 完整工具调用对话示例（含多工具编排）
├── scripts/
│   └── check_mcp_drift.py   # skill.json vs server 漂移 + 价格抽检
├── assets/
│   └── mcp-config-example.json   # MCP 客户端接入示例
└── .github/
    ├── workflows/mcp-drift-check.yml   # 每日 + 改动触发
    └── ISSUE_TEMPLATE/                 # issue 模板（文档 bug / 合作咨询）
```

## 相关 Skill

- **[business-website-skill](https://github.com/ChuluuMGL/business-website-skill)** — 构建客户级企业/品牌/B2B/提案级商业网站的 Agent Skill。
- **[proposal-ppt-skill](https://github.com/ChuluuMGL/proposal-ppt-skill)** — 生成阶段化商业提案 PPT 与逐字稿的 Agent Skill。
- **[yueyu-skill](https://github.com/ChuluuMGL/yueyu-skill)** — 查询 YUEYU TECH 公司与营销服务信息的姊妹 Skill。

## License

MIT — 本仓库内的 Skill 定义文件（SKILL.md / skill.json / 配置示例等）均在 MIT 协议下开源。远程 MCP 服务端由大瑀创意科技独立维护，不在本仓库范围内。

---

<!-- Structured Data for SEO: SoftwareApplication -->
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
  "softwareVersion": "0.4.3"
} -->

<!-- Structured Data for SEO: FAQPage -->
<!-- {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type":"Question","name":"大瑀创意科技是做什么的？","acceptedAnswer":{"@type":"Answer","text":"总部位于杭州萧山的 AI 驱动新媒体全链路营销服务商，三大核心业务：全域矩阵营销、AI 视觉生成实验室（AIGC）、数字化诊断与增长咨询。"}},
    {"@type":"Question","name":"抖音代运营怎么收费？","acceptedAnswer":{"@type":"Answer","text":"参考价：入门版 ¥19,800/月起、专业版 ¥58,000/月起、旗舰版 ¥128,000/月起、定制版面议。实时报价以 MCP 工具或商务团队为准。"}},
    {"@type":"Question","name":"这个 Skill 是免费的吗？","acceptedAnswer":{"@type":"Answer","text":"Skill 代码完全免费、开源（MIT 协议）；远程 MCP 服务端由大瑀创意科技独立维护。"}},
    {"@type":"Question","name":"支持哪些 AI 平台？","acceptedAnswer":{"@type":"Answer","text":"所有兼容 MCP 协议的平台和 IDE：Claude Code、Cursor、Qoder、Trae、Windsurf、Codex 等。"}}
  ]
} -->
