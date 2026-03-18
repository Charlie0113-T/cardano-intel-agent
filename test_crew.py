import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

# --- 配置区 ---
GMAIL_USER = "charlestao0113@gmail.com"
GMAIL_PASSWORD = "iejzzaaztlkxawfq"
MODEL_NAME = "ollama/llama3"
os.environ["OPENAI_API_KEY"] = "NA"
TARGET_DIR = os.path.expanduser("~/Desktop/4TB Photos+CODE/Charles")

# --- 邮件发送函数 ---
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = GMAIL_USER # 发给自己
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("📧 邮件已成功发送至您的邮箱！")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
def run_automated_report():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    # 将文件名拼接到目标路径
    filename = os.path.join(TARGET_DIR, f"Cardano_Report_{timestamp}.md")

# --- 原有 Agent 与工具定义 ---
lc_search_tool = DuckDuckGoSearchRun()

@tool("cardano_search_tool")
def search_tool(query: str):
    """用于 Cardano 生态研究的搜索工具。"""
    return lc_search_tool.run(query)

news_collector = Agent(
    role='Cardano 情报员',
    goal='搜集 ADA 最新动态',
    backstory='你是一名研究员，专注于 eUTXO 模型、Hydra 扩容和 Cardano 治理。',
    tools=[search_tool],
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)

strategist = Agent(
    role='首席分析师',
    goal='撰写中文分析简报',
    backstory='你是一个资深的区块链分析师，擅长从复杂的数据中提炼核心观点，并能用流畅的中文进行表达。',
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)

# --- 自动化主逻辑 ---
def run_automated_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    filename = f"Cardano_Report_{timestamp.replace(' ', '_').replace(':', '-')}.md"

    task1 = Task(
        description='搜索今日 Cardano 核心新闻和恐惧贪婪指数。',
        expected_output='新闻摘要。',
        agent=news_collector
    )

    task2 = Task(
        description='撰写中文报告。',
        expected_output='Markdown 格式报告。',
        agent=strategist,
        output_file=filename
    )

    crew = Crew(
        agents=[news_collector, strategist],
        tasks=[task1, task2],
        process=Process.sequential
    )

    print(f"\n--- 🛰️ 正在生成报告 ({timestamp}) ---")
    result = crew.kickoff()
    
    # 执行发送邮件
    email_subject = f"Cardano 每日快报 - {timestamp}"
    send_email(email_subject, str(result))

if __name__ == "__main__":
    # 每 4 小时运行一次
    while True:
        run_automated_report()
        print("😴 进入待机状态...")
        time.sleep(4 * 60 * 60)
