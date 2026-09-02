<p align="center">
  <img src="assets/logo.svg" width="96" height="96" alt="Cardano Intel Agent Logo" />
</p>

<h1 align="center">Cardano Intel Agent</h1>

<p align="center">An automated blockchain intelligence system running on a local Mac Mini — powered by Llama 3, zero API cost, nothing leaves the machine.</p>

<p align="center">
  <span>English</span> ·
  <a href="README.md"><b>简体中文</b></a>
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

An automated blockchain intelligence system that runs on a local Mac Mini. It uses **CrewAI** to orchestrate multiple AI agents that track Cardano (ADA) development activity and market sentiment, then delivers the findings as a Markdown briefing and an email.

## 🌟 Features

- 🔒 **Fully local** — runs on Ollama + Llama 3, so inference never leaves the machine: private by design, zero API cost
- 🛰️ **News Collector agent** — tracks GitHub activity (Hydra, Mithril) and ecosystem news
- 📊 **Market Analyst agent** — pulls market sentiment signals such as the crypto Fear & Greed Index
- 📝 **Automated briefings** — generates timestamped Markdown reports and archives them
- 📧 **Automated delivery** — emails each finished report to your Gmail inbox
- ⏰ **Unattended** — runs a fresh cycle every 4 hours as a background process

## 🛠️ Tech Stack

| Technology | Purpose |
|------|------|
| Python 3.12 | Runtime |
| CrewAI | Multi-agent orchestration |
| Ollama / Llama 3 | Local LLM inference |
| LangChain Community | DuckDuckGo search tool |
| smtplib | Gmail delivery |
| Local Markdown archive | Report storage (synced to a 4TB data vault) |

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- [Ollama](https://ollama.com) with the `llama3` model pulled
- A Gmail account and an [app password](https://myaccount.google.com/apppasswords)

### Install & Run

```bash
# 1. Pull the local model
ollama pull llama3

# 2. Install dependencies
pip install crewai crewai-tools langchain-community duckduckgo-search python-dotenv

# 3. Configure your environment (see "Configuration" below)
cp .env.example .env   # then fill in your own credentials

# 4. Start it
python test_crew.py
```

The first report is generated immediately on start, and a new one follows every 4 hours.

### Configuration

Create a `.env` file in the project root:

```bash
GMAIL_USER=your_address@gmail.com
GMAIL_PASSWORD=your_16_char_app_password
TARGET_DIR=~/Desktop/YourArchiveFolder
```

> ⚠️ `.env` is already covered by `.gitignore`. **Never** hard-code a Gmail app password into the source and commit it — a password in a public repository should be considered leaked.

## 📂 Project Structure

```
cardano-intel-agent/
├── test_crew.py      # Main program: agent definitions, task orchestration, email delivery
├── assets/
│   └── logo.svg      # Project mark
├── .env              # Environment config (not committed)
└── archive/          # Generated briefings (not committed)
```

## 🤖 Agent Crew

| Agent | Role | Responsibility |
|------|------|------|
| **News Collector** | Cardano researcher | Gathers the latest ADA developments, focused on the eUTXO model, Hydra scaling, and on-chain governance |
| **Chief Analyst** | Senior blockchain analyst | Distills the raw intel into key takeaways and writes the Markdown briefing |

The two agents run under `Process.sequential`: the collector produces the summary first, and the analyst writes the report from it.

## 📄 License

This project is open source under the Apache License 2.0.

## ✍️ About the Author

**Charles Tao** — 8th grader at Stonepark Intermediate, Cardano developer, currently building **EchoForge**.
