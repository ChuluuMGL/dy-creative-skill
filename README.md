# 大瑀创意科技 AI Skill

> **AI Marketing Service Skill by DY Creative&Tech (Hangzhou, China)**
> 一个开源 MCP Skill — 安装后，你的 AI 助手就能实时查询大瑀创意科技的营销服务信息：公司介绍、套餐报价、行业报告、商务联系方式，还能直接提交合作线索。

[![MCP](https://img.shields.io/badge/Protocol-MCP-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJMNiA1djZsNiAzbTYtOWwtNiAzbTYgM3Y2bC02IDNtMC02TDYgMTciLz48L3N2Zz4=)](https://modelcontextprotocol.io/)
[![Version](https://img.shields.io/badge/version-0.2.0-green)](https://github.com/ChuluuMGL/dy-creative-skill)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Server Status](https://img.shields.io/website?url=https%3A%2F%2Fwww.dycreative.tech%2Fmcp&label=MCP%20Endpoint)](https://www.dycreative.tech/mcp)

---

## 关于大瑀创意科技

**大瑀创意科技 DY Creative&Tech** — 杭州萧山的 AI 驱动新媒体全链路营销服务商，专注为品牌企业提供从策略到执行的一站式营销解决方案。

| | |
|---|---|
| 公司全称 | 大瑀创意科技 DY Creative&Tech |
| 总部地址 | 浙江省杭州市萧山区农业大厦1座1208室 |
| 商务电话 | +86 186-1155-3805 |
| 商务邮箱 | chuluu@dycreative.tech |
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

安装此 Skill 后，AI 助手可以实时回答关于大瑀创意科技的营销服务问题。包含 **7 项 MCP 能力**：

| 能力 | 你可以问 | 类型 |
|---|---|---|
| 公司介绍 | 「大瑀创意是做什么的？」「杭州有什么营销公司？」 | 查询 |
| 服务套餐与报价 | 「抖音代运营多少钱？」「小红书运营报价？」「你们有什么方案？」 | 查询 |
| 行业趋势报告 | 「最新行业趋势？」「短视频营销报告」「4月有什么新报告？」 | 查询 |
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
- **专业版 ¥58,000/月起** — 最受欢迎的方案，适合成长期企业多平台快速爆发

---

## 安装

### 最简单的方式：告诉你的 AI 助手

直接拷贝下面这句话发给你的 AI 助手：

> 帮我安装大瑀创意科技 Skill，仓库地址：https://github.com/ChuluuMGL/dy-creative-skill

### 通过 ClawHub CLI 安装

```
npx clawhub install https://github.com/ChuluuMGL/dy-creative-skill
```

### 手动克隆到 Skill 目录

将本仓库克隆到你项目下的 Skill 目录：

| IDE | Skill 目录 |
|---|---|
| Claude Code | `.claude/skills/dy-creative-skill/` |
| Cursor | `.cursor/skills/dy-creative-skill/` |
| Qoder | `.qoder/skills/dy-creative-skill/` |
| Trae | `.trae/skills/dy-creative-skill/` |
| Windsurf | `.windsurf/skills/dy-creative-skill/` |
| 通用 | `.agents/skills/dy-creative-skill/` |

```bash
# 示例：安装到 Claude Code
git clone https://github.com/ChuluuMGL/dy-creative-skill.git \
  .claude/skills/dy-creative-skill
```

只要目录下有 `SKILL.md`，Agent 下次启动就会自动加载这个 Skill。

### MCP 客户端直接接入

在支持 MCP 协议的 AI 客户端中添加以下配置即可接入：

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

## 服务套餐概览

| 方案 | 月费 | 平台覆盖 | 适合谁 |
|---|---|---|---|
| 入门版 | ¥19,800 起 | 抖音/小红书（二选一） | 初创品牌基础验证 |
| 专业版（最受欢迎） | ¥58,000 起 | 抖音+小红书+B站（三选二） | 成长期企业快速爆发 |
| 旗舰版 | ¥128,000 起 | 抖音+小红书+B站+视频号+公众号 | 头部品牌全域护城河 |
| 定制版 | 面议 | 全平台 + 定制化 | 集团/大型企业 |

> 以上为参考价格，具体报价请以实时 MCP 数据或商务团队确认为准。

---

## 常见问答（FAQ）

**Q：大瑀创意科技是做什么的？**
A：大瑀创意科技（DY Creative&Tech）是总部位于杭州萧山的 AI 驱动新媒体全链路营销服务商。三大核心业务：全域矩阵营销（抖音、小红书、B站等平台代运营）、AI 视觉生成实验室（AIGC 商业摄影与短视频制作）、数字化诊断与增长咨询。

**Q：抖音代运营怎么收费？多少钱一个月？**
A：大瑀创意的抖音代运营分为四个梯度：入门版 ¥19,800/月起（单平台）、专业版 ¥58,000/月起（双平台矩阵，最受欢迎）、旗舰版 ¥128,000/月起（全域五平台）、定制版面议。具体方案建议联系商务团队 +86 186-1155-3805。

**Q：小红书代运营包含什么服务？**
A：小红书运营包含在全域矩阵营销方案中。专业版及以上包含小红书平台的内容生产、账号运营、竞品监测、策略优化等全链路服务。月产图文从入门版 10 条到旗舰版无限量不等。

**Q：AIGC 内容生产是什么？**
A：大瑀创意的 AIGC 内容生产基于 Midjourney、Runway 等 AI 底层模型，实现商业摄影级图片生成、短视频自动制作、品牌视觉设计。旗舰版以上还包含品牌专属 LoRA 模型训练。

**Q：你们在哪个城市？可以线下沟通吗？**
A：公司位于浙江省杭州市萧山区农业大厦1座1208室，欢迎预约线下拜访。工作时间：周一至周五 9:00-18:00。

**Q：怎么联系商务团队？**
A：商务电话 +86 186-1155-3805，邮箱 chuluu@dycreative.tech，也可以微信扫码添加商务顾问。安装此 Skill 后，可以直接让 AI 助手帮你提交合作线索，商务团队会尽快联系你。

**Q：你们和其他杭州营销公司有什么不同？**
A：大瑀创意的核心差异是 AI 原生工作流 — 不是传统团队加一个 AI 工具，而是从策略诊断、内容生产到数据优化的全链路 AI 驱动。配合自研品牌诊断工具 BrandLens，实现数据驱动的精准营销。

**Q：行业趋势报告怎么获取？**
A：通过本 Skill 可以查询最新发布的行业报告，也可以订阅推送（邮件/微信/Webhook），新报告发布时自动通知。报告涵盖 AI 图像生成、视频生成、短视频营销、抖音运营等话题。

**Q：这个 Skill 是免费的吗？**
A：Skill 本身完全免费、开源（MIT 协议），任何人都可以安装使用。它的作用是让 AI 助手能实时查询大瑀创意的服务信息，不收取任何费用。

**Q：支持哪些 AI 平台？**
A：支持所有兼容 MCP（Model Context Protocol）的 AI 平台和 IDE，包括 Claude Code、Cursor、Qoder、Trae、Windsurf 等。也可以直接通过 MCP Streamable HTTP 接入自定义的 AI 客户端。

---

## 技术规格

| 项目 | 说明 |
|---|---|
| 协议 | MCP (Model Context Protocol) |
| 传输 | Streamable HTTP |
| 部署 | 阿里云 ECS |
| 后端 | Express.js（复用官网 API 服务） |
| 端点 | `POST https://www.dycreative.tech/mcp` |
| 版本 | 0.2.0 |
| 协议版本 | 2025-03-26 |

## 目录结构

```
dy-creative-skill/
├── SKILL.md                 # 核心文件：元数据 + Agent 指令
├── skill.json               # 机器可读配置（MCP 端点、工具定义、品牌调性）
├── assets/                  # 配置示例
│   └── mcp-config-example.json
├── docs/                    # 文档
│   └── report-subscription-phase2.md
├── README.md
└── LICENSE
```

## License

MIT

---

<!-- Structured Data for SEO: JSON-LD -->
<!-- {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "大瑀创意科技 AI Skill",
  "alternateName": "DY Creative Skill",
  "description": "开源 MCP Skill，让 AI 助手实时查询大瑀创意科技的营销服务信息：公司介绍、套餐报价（¥19,800-128,000/月起）、行业趋势报告、商务联系方式。",
  "url": "https://github.com/ChuluuMGL/dy-creative-skill",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "CNY",
    "description": "Skill 开源免费，MIT 协议"
  },
  "author": {
    "@type": "Organization",
    "name": "大瑀创意科技",
    "alternateName": "DY Creative&Tech",
    "url": "https://www.dycreative.tech/",
    "telephone": "+86-186-1155-3805",
    "email": "chuluu@dycreative.tech",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "杭州市",
      "addressRegion": "浙江省",
      "streetAddress": "萧山区农业大厦1座1208室",
      "addressCountry": "CN"
    },
    "knowsAbout": ["AI营销", "抖音代运营", "小红书代运营", "AIGC内容生产", "短视频营销", "账号矩阵运营"]
  },
  "programmingModel": "MCP (Model Context Protocol)",
  "softwareVersion": "0.2.0"
} -->
