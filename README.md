# 🛡️ Cardano Intel Agent (Llama 3 Powered)

这是一个运行在本地 Mac Mini 上的自动化区块链情报系统。它利用 **CrewAI** 编排多个 AI Agent，实时监控 Cardano (ADA) 的技术动态与市场情绪。

## 🌟 核心功能
- **全本地运行**：基于 Ollama + Llama 3，保护隐私，无 API 成本。
- **多维度分析**：
  - **情报员 (News Collector)**：追踪 GitHub 提交 (Hydra, Mithril) 与生态新闻。
  - **分析师 (Market Analyst)**：抓取加密货币“恐惧与贪婪指数”。
- **自动化交付**：
  - 自动生成带时间戳的 Markdown 报告。
  - 自动发送研报至 Gmail 邮箱。

## 🛠️ 技术栈
- **Language**: Python 3.12
- **Orchestration**: CrewAI
- **LLM**: Ollama / Llama 3
- **Storage**: Local Markdown Archive (Synced to 4TB Data Vault)

## 📂 项目结构
- `test_crew.py`: 主程序逻辑。
- `.env`: 环境配置文件（包含 Gmail 应用密码）。
- `archive/`: 历史情报简报存放处。

## ✍️ 关于作者
**Charles Tao** - Stonepark Intermediate 8年级学生，Cardano 开发者，正在构建 **EchoForge**。
