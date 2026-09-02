<p align="center">
  <img src="assets/logo.svg" width="96" height="96" alt="Cardano Intel Agent Logo" />
</p>

<h1 align="center">Cardano Intel Agent</h1>

<p align="center">一个跑在本地 Mac Mini 上的自动化区块链情报系统 — 由 Llama 3 驱动，零 API 成本，数据不出本机。</p>

<p align="center">
  <a href="README.en.md"><b>English</b></a> ·
  <span>简体中文</span>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-000000.svg?style=flat-square&labelColor=0a0a0a" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-000000.svg?style=flat-square&labelColor=0a0a0a&logo=python&logoColor=white" />
  <img alt="CrewAI" src="https://img.shields.io/badge/CrewAI-multi--agent-000000.svg?style=flat-square&labelColor=0a0a0a" />
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-Llama%203-000000.svg?style=flat-square&labelColor=0a0a0a&logo=ollama&logoColor=white" />
  <img alt="Local First" src="https://img.shields.io/badge/LLM-100%25%20local-000000.svg?style=flat-square&labelColor=0a0a0a" />
  <img alt="Cardano" src="https://img.shields.io/badge/chain-Cardano-000000.svg?style=flat-square&labelColor=0a0a0a" />
</p>

---

这是一个运行在本地 Mac Mini 上的自动化区块链情报系统。它利用 **CrewAI** 编排多个 AI Agent，实时监控 Cardano (ADA) 的技术动态与市场情绪，并把结论以 Markdown 简报和邮件的形式送到你手上。

## 🌟 核心功能

- 🔒 **全本地运行** — 基于 Ollama + Llama 3，模型推理不出本机，保护隐私、无 API 成本
- 🛰️ **情报员 (News Collector)** — 追踪 GitHub 提交（Hydra、Mithril）与生态新闻
- 📊 **分析师 (Market Analyst)** — 抓取加密货币「恐惧与贪婪指数」等市场情绪指标
- 📝 **自动生成简报** — 输出带时间戳的 Markdown 报告，自动归档
- 📧 **自动投递** — 研报生成后自动发送至 Gmail 邮箱
- ⏰ **无人值守** — 每 4 小时自动跑一轮，常驻后台

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| Python 3.12 | 运行环境 |
| CrewAI | 多 Agent 编排框架 |
| Ollama / Llama 3 | 本地大模型推理 |
| LangChain Community | DuckDuckGo 搜索工具 |
| smtplib | Gmail 邮件投递 |
| Local Markdown Archive | 报告归档（同步至 4TB 数据仓库） |

## 🚀 快速开始

### 环境要求

- Python 3.12
- [Ollama](https://ollama.com)，并已拉取 `llama3` 模型
- 一个 Gmail 账号及其[应用专用密码](https://myaccount.google.com/apppasswords)

### 安装与运行

```bash
# 1. 拉取本地模型
ollama pull llama3

# 2. 安装依赖
pip install crewai crewai-tools langchain-community duckduckgo-search python-dotenv

# 3. 配置环境变量（见下方「配置」一节）
cp .env.example .env   # 然后填入你自己的凭据

# 4. 启动
python test_crew.py
```

启动后程序会立即生成第一份报告，随后每 4 小时自动运行一次。

### 配置

在项目根目录创建 `.env` 文件：

```bash
GMAIL_USER=your_address@gmail.com
GMAIL_PASSWORD=your_16_char_app_password
TARGET_DIR=~/Desktop/YourArchiveFolder
```

> ⚠️ `.env` 已被 `.gitignore` 忽略。**切勿**把 Gmail 应用密码硬编码进源码后提交 — 公开仓库里的密码等同于已泄露。

## 📂 项目结构

```
cardano-intel-agent/
├── test_crew.py      # 主程序：Agent 定义、任务编排、邮件投递
├── assets/
│   └── logo.svg      # 项目标识
├── .env              # 环境配置（不入库）
└── archive/          # 历史情报简报存放处（不入库）
```

## 🤖 Agent 编排

| Agent | 角色 | 职责 |
|------|------|------|
| **情报员** | Cardano 研究员 | 搜集 ADA 最新动态，专注 eUTXO 模型、Hydra 扩容与链上治理 |
| **首席分析师** | 资深区块链分析师 | 从原始情报中提炼核心观点，输出中文 Markdown 简报 |

两个 Agent 以 `Process.sequential` 串行执行：情报员先产出摘要，分析师再据此成稿。

## 📄 开源协议

本项目基于 Apache License 2.0 开源。

## ✍️ 关于作者

**Charles Tao** — Stonepark Intermediate 8 年级学生，Cardano 开发者，正在构建 **EchoForge**。
