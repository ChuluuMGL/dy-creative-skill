# 行业报告订阅功能 — 需求文档（阶段二）

## 概述

为大瑀创意科技 MCP Skill 增加**报告订阅推送**能力。用户通过 AI Agent 留下邮箱或微信后，当大瑀发布新的行业趋势报告时，自动向订阅者推送通知。

## 当前状态（阶段一）

阶段一已实现 `get_latest_reports` 工具，支持：
- 查询最新报告列表（`limit` 参数控制数量）
- 增量查询（`since` 参数过滤指定日期后的报告）

**阶段一的局限**：依赖用户主动查询，Agent 无法自动感知新报告发布。

## 阶段二目标

实现**推送式订阅**，核心链路：

```
用户通过 Agent 订阅 → 订阅信息存入飞书多维表格 → 发布新报告时 → 自动推送通知
```

## 需要新增的 MCP 工具

### `subscribe_reports`

```json
{
  "name": "subscribe_reports",
  "description": "订阅大瑀创意科技的行业趋势报告。新报告发布时，会通过用户选择的渠道推送通知。",
  "inputSchema": {
    "type": "object",
    "properties": {
      "channel": {
        "type": "string",
        "enum": ["email", "wechat", "webhook"],
        "description": "订阅渠道：email=邮件推送, wechat=微信推送, webhook=webhook回调"
      },
      "address": {
        "type": "string",
        "description": "订阅地址：邮箱地址 / 微信号 / webhook URL"
      },
      "interests": {
        "type": "array",
        "items": { "type": "string" },
        "description": "感兴趣的话题标签（可选），如 ['短视频', 'AIGC', '抖音运营']"
      }
    },
    "required": ["channel", "address"]
  }
}
```

### `unsubscribe_reports`

```json
{
  "name": "unsubscribe_reports",
  "description": "取消订阅大瑀创意科技的趋势报告推送。",
  "inputSchema": {
    "type": "object",
    "properties": {
      "address": {
        "type": "string",
        "description": "订阅时使用的地址"
      }
    },
    "required": ["address"]
  }
}
```

## 后端实现方案

### 1. 订阅数据存储

在飞书多维表格中新建一个 **"报告订阅者" 表**，字段：

| 字段名 | 类型 | 说明 |
|---|---|---|
| channel | 文本 | email / wechat / webhook |
| address | 文本 | 订阅地址 |
| interests | 文本 | 感兴趣的话题（逗号分隔） |
| status | 文本 | active / unsubscribed |
| subscribedAt | 日期 | 订阅时间 |
| unsubscribedAt | 日期 | 取消订阅时间 |

同时保留一份本地 JSON 备份（`server/data.json` 中新增 `subscribers` 数组）。

### 2. 推送触发机制

**方案 A：定时轮询（推荐，简单可靠）**

在 Express server 中加入定时任务：

```javascript
const cron = require('node-cron');

// 每小时检查一次是否有新报告
cron.schedule('0 * * * *', async () => {
  await checkAndNotifyNewReports();
});
```

**方案 B：发布时触发**

在 `POST /api/posts` 创建报告时，同步触发推送通知。

推荐 **方案 B**，因为推送时机更精确，且不需要额外依赖。

### 3. 推送渠道实现

#### 邮件推送
- 使用 Nodemailer 发送邮件
- 邮件模板包含：报告标题、摘要、发布日期、阅读链接
- SMTP 配置通过环境变量注入

#### 微信推送
- 通过飞书机器人发送给指定运营人员
- 运营人员在企业微信/飞书中转发给订阅用户
- 或者使用微信模板消息 API（需要微信服务号）

#### Webhook 推送
- POST 请求到用户提供的 webhook URL
- 请求体包含报告信息 JSON
- 处理失败重试（最多 3 次，间隔 1h/6h/24h）

### 4. 推送内容格式

```json
{
  "event": "new_report",
  "data": {
    "id": 1713123456789,
    "title": "2026 Q1 抖音电商趋势白皮书",
    "summary": "...",
    "publishedAt": "2026-04-15T10:00:00.000Z",
    "url": "https://www.dycreative.tech/#report-1713123456789",
    "unsubscribeUrl": "mailto:<your-email>?subject=取消订阅"
  }
}
```

### 5. 防骚扰机制

- 每个地址每天最多推送 1 次
- 如果一天内有多篇报告，合并为一条汇总通知
- 推送时附带退订说明

## 需要新增的依赖

```json
{
  "nodemailer": "^7.0.0",
  "node-cron": "^3.0.0"
}
```

## 环境变量

```env
# 邮件推送（如使用）
SMTP_HOST=<your-smtp-host>
SMTP_PORT=465
SMTP_USER=<your-smtp-user>
SMTP_PASS=<your-smtp-password>
SMTP_FROM="大瑀创意科技 <<your-smtp-user>>"

# 飞书订阅者表格（新增）
FEISHU_SUBSCRIBER_TABLE_ID=tblXXXXXXXXXXXX
```

## SKILL.md 更新

在触发场景表格中新增：

```
| "我想订阅你们的报告" / "有新报告通知我" | `subscribe_reports` |
| "取消报告订阅" | `unsubscribe_reports` |
```

## skill.json 更新

在 `tools` 数组中新增 `subscribe_reports` 和 `unsubscribe_reports` 两个工具定义。

## 实现步骤

1. [ ] 在飞书多维表格中创建"报告订阅者"表
2. [ ] 后端新增 `subscribe_reports` 和 `unsubscribe_reports` 工具 handler
3. [ ] 后端在 `POST /api/posts` 中加入推送触发逻辑
4. [ ] 实现邮件推送渠道（Nodemailer）
5. [ ] 实现微信推送渠道（飞书消息卡片 → 运营转发）
6. [ ] 更新 SKILL.md 和 skill.json
7. [ ] 测试完整流程
