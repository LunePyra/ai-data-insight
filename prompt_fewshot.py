import os
from openai import OpenAI
from dotenv import load_dotenv

#加载.env文件中的环境变量
load_dotenv()

#从环境变量读取配置
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

#检查读取
if not API_KEY:
    raise ValueError("请在.env文件中设置API_KEY")

client = OpenAI(api_key=API_KEY,base_url=BASE_URL)

def classify_job_level(jd_text):
    prompt = f"""
你是一个 HR 数据分析师。请将以下数据岗位 JD 分类为：初级、中级、高级。

分类标准示例：
- "熟悉Excel、SQL，协助数据报表制作" -> 初级
- "负责数据仓库建设、ETL开发、数据建模" -> 中级
- "主导数据架构设计、带领数据团队、制定数据战略" -> 高级

现在请分类以下 JD（仅回复"初级"、"中级"或"高级"三个字，不要解释）：
{jd_text}
"""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# 测试
if __name__ == "__main__":
    # 从文件读取所有行，每行作为一个 JD
    with open("job_descriptions.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]  # 忽略空行

    for idx, jd in enumerate(lines, 1):
        result = classify_job_level(jd)
        print(f"{idx}. {result} → {jd}")
