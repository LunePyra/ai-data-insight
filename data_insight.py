import os
import pandas as pd
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

def analyze_csv_with_ai(file_path,large_mode=None):

    #读取数据基本信息
    try:
        df = pd.read_csv(file_path,encoding='utf-8')
    except FileNotFoundError:
        return "错误：找不到指定文件，请检查路径。"
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file_path, encoding='gbk')
        except Exception as e:
            return f"错误：读取文件时编码错误。{e}"
    except Exception as e:
        return f"错误：读取文件失败。{e}"

    #自动判断大文件模式
    if large_mode is None:
        large_mode = len(df) > 1000

    desc = df.describe(include='all').to_string()
    missing_info = df.isnull().sum().to_string()
    columns_info = df.dtypes.to_string()

    #如果开启大文件模式，就不发样本数据
    if large_mode:
        sample_text = "（大文件模式，已省略样本数据，仅用统计摘要）"
    else:
        sample_text = df.head(5).to_string()

    #构建给AI的提示词
    prompt = f'''
你是一位资深数据分析师。现在有一个 CSV 文件，请根据以下信息给出分析：

【文件基本信息】
- 总行数：{len(df)}
- 总列数：{len(df.columns)}

【列名及数据类型】
{columns_info}

【每列缺失值数量】
{missing_info}

【数据统计摘要】
{desc}

【前5行数据样本】
{sample_text}

请按以下格式输出（用中文）：
1. 数据概况总结（2-3句话）
2. 发现的数据质量问题（列出具体问题，没有则写“无明显问题”）
3. 清洗建议（给出3条具体的处理建议）
4. 请单独生成一段可直接运行的 Python pandas 清洗代码，要求：
   - 代码用 ```python ...``` 包裹
   - 包含缺失值处理、重复值检查、数据类型转换（如有必要）
   - 假设数据文件为 'input.csv'，清洗后保存为 'cleaned.csv'
   - 代码中要加上必要的注释
'''
    #调用大模型
    try:
        response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role":"system","content":"你是一个专业的数据分析师，回答要实用、具体。"
            },
            {
                "role":"user","content":prompt
            }
        ],
            temperature=0.3#降低随机性，让输出更稳定
        )
        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg:
            return "API密钥无效，请检查.env文件中的API_KEY。"
        elif "404" in error_msg:
            return ("模型名称错误或服务不可用，请检查MODEL_NAME。")
        elif "timeout" in error_msg.lower():
            return "请求超时，请稍后重试。"
        else:
            return f"API调用失败：{error_msg}"

if __name__ == "__main__":
    test_file = "test_data.csv"
    print("正在分析...\n")
    result = analyze_csv_with_ai(test_file)
    print("=" * 50)
    print(result)
    print("=" * 50)

