import json
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

def extract_review_info(review_text):
    """
    从用户评论中提取结构化信息。
    返回字典，包含情感、特征、紧急程度。
    """
    prompt = f"""
    你是一个数据标注专家。请从以下用户评论中提取信息，并严格按 JSON 格式输出。

    评论：{review_text}

    你需要提取的字段：
    - sentiment: 情感倾向，只能从 ["正面", "负面", "中性"] 中选择
    - features: 提到的产品特征列表，数组
    - urgency: 紧急程度，只能从 ["高", "中", "低"] 中选择

    输出示例：
    {{"sentiment": "负面", "features": ["物流", "客服"], "urgency": "高"}}

    请直接输出 JSON，不要包含任何其他文字、代码块标记或解释。
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system", "content": "你是一个严格遵循指令的数据处理助手。"
            },
            {
                "role": "user", "content": prompt
            }
        ],
        temperature=0.1  # 极低温度，确保输出稳定
    )
    result_text = response.choices[0].message.content.strip()

    # 容错：如果模型偶尔包了 ```json 标记，自动去除
    if result_text.startswith("```"):
        result_text = result_text.split("\n", 1)[1]
        if result_text.endswith("```"):
            result_text = result_text[:-3]

    try:
        return json.loads(result_text)
    except json.JSONDecodeError:
        # 解析失败时返回错误信息，便于后续处理
        return {"error": "JSON解析失败", "raw_output": result_text}

# 测试
if __name__ == "__main__":
    with open("reviews.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]   # 去掉空行
    for review in lines:
        result = extract_review_info(review)
        print(result)

