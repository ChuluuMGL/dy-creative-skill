# Contributing

感谢你关注大瑀创意科技 AI Skill！本仓库包含**Skill 定义文件**（开源，MIT）与配套文档/脚本；远程 MCP 服务端由大瑀创意科技独立维护，**不在本仓库贡献范围内**。

## 我可以贡献什么

- ✅ **文档改进**：README / README.en / SKILL.md 的措辞、示例、排版。
- ✅ **工具契约对齐**：如果发现 `skill.json` 里的工具名/参数与 server 实际不一致，欢迎提 PR 修正（对齐到已部署的 server 真实 schema）。
- ✅ **兼容性补充**：在更多 IDE / agent 上的实测结果、安装路径修正。
- ✅ **脚本 / CI**：`scripts/check_mcp_drift.py` 与 workflow 的增强。

## 提交前请确认

1. **改动工具定义时**——CI（[mcp-drift-check](.github/workflows/mcp-drift-check.yml)）会在 PR 上自动跑，校验 `skill.json` 与 server `tools/list` 一致；价格改动需同时更新 README 套餐表与 `scripts/check_mcp_drift.py` 里的 `EXPECTED_PRICES`。
2. **中英文同步**——README.md 与 README.en.md 描述同一事实，改了中文请同步英文。
3. **本地先跑校验**：

   ```bash
   python3 scripts/check_mcp_drift.py     # 应输出 ✓ No drift
   python3 -c "import json; json.load(open('skill.json'))"   # JSON 合法
   ```

## 不接受的范围

- ❌ 远程 MCP 服务端代码（不在此仓库）。
- ❌ 编造案例 / 效果 / 合同细节 / 虚假报价（违反 Skill 红线）。
- ❌ 商务咨询类 issue（请走官网或 `submit_lead`，见 issue 模板里的入口）。

## 流程

1. Fork → 分支 → 改 → 本地校验 → 提 PR（描述清楚动机与测试）。
2. CI 绿 + 维护者 review → 合并。
3. 改动纳入下一个 release（版本号由维护者 bump）。

## 行为准则

保持专业、对事不对人。营销类项目尤其注意：不夸大、不误导、报价以实时数据为准。
