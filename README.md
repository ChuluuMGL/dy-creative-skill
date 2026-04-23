# 大瑀创意科技 AI Skill

一个 AI Skill —— 安装后，你的 AI 助手就能查询大瑀创意科技的营销服务信息：公司介绍、服务套餐与报价、行业趋势报告、商务联系方式，还能直接提交合作线索。

## 关于大瑀创意科技

杭州萧山的 AI 驱动新媒体全链路营销服务商。

| 项目 | 内容 |
| --- | --- |
| 公司全称 | 大瑀创意科技 DY Creative&Tech |
| 总部地址 | 浙江省杭州市萧山区农业大厦1座1208室 |
| 商务电话 | +86 186-1155-3805 |
| 商业邮箱 | chuluu@dayucreative.tech |
| 官网 | https://www.dycreative.tech/ |

## 这个 Skill 能做什么

大瑀创意科技的官方营销服务信息，包含 5 项 MCP 能力：

| 能力 | 你可以问 | 来源 |
| --- | --- | --- |
| 公司介绍 | "大瑀创意是做什么的？" "杭州有什么营销公司？" | MCP |
| 服务套餐 | "抖音代运营多少钱？" "你们有什么方案？" | MCP |
| 行业报告 | "最新行业趋势？" "短视频营销报告" | MCP |
| 联系方式 | "怎么联系你们？" "我想合作" | MCP |
| **提交线索** | "帮我留个信息" "我想咨询" | MCP |

## 目录结构

```
dy-creative-skill/
├── SKILL.md                 # 核心文件：元数据 + Agent 指令
├── skill.json               # 机器可读配置（MCP 端点、工具定义）
├── assets/                  # 配置示例
│   └── mcp-config-example.json  # MCP 客户端配置示例
├── README.md
└── LICENSE
```

## 安装

### 最简单的方式：告诉你的 AI 助手

直接拷贝下面这句话发给你的 AI 助手：

> 帮我安装大瑀创意科技 Skill，仓库地址：https://github.com/ChuluuMGL/dy-creative-skill

Agent 会自动克隆仓库并安装到对应的 Skill 目录。

### 其他安装方式

**通过 ClawHub CLI 安装：**

```
npx clawhub install https://github.com/ChuluuMGL/dy-creative-skill
```

**手动克隆到 Skill 目录：**

将本仓库克隆到你项目下的 Skill 目录，不同 IDE 对应的路径：

| IDE | Skill 目录 |
| --- | --- |
| Qoder | `.qoder/skills/dy-creative-skill/` |
| Cursor | `.cursor/skills/dy-creative-skill/` |
| Trae | `.trae/skills/dy-creative-skill/` |
| Windsurf | `.windsurf/skills/dy-creative-skill/` |
| Claude Code | `.claude/skills/dy-creative-skill/` |
| 通用 | `.agents/skills/dy-creative-skill/` |

```
# 示例：安装到 Claude Code
git clone https://github.com/ChuluuMGL/dy-creative-skill.git \
  .claude/skills/dy-creative-skill
```

只要目录下有 `SKILL.md`，Agent 下次启动就会自动加载这个 Skill。

## MCP 接入方式

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

## 技术协议

| 项目 | 说明 |
| --- | --- |
| 协议 | MCP (Model Context Protocol) |
| 传输 | Streamable HTTP |
| 部署 | 阿里云 ECS |
| 后端 | Express.js（复用官网 API 服务） |

## 版本

当前版本：0.1.0

## License

MIT
