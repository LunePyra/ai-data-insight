import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv
import sys

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


def ai_generate_cleaning_code(df):
    """让AI根据数据特征生成pandas清洗代码"""

    # 构造数据摘要，不发送原始数据
    col_info = df.dtypes.to_dict()
    missing = df.isnull().sum().to_dict()
    sample = df.head(2).to_string()

    prompt = f"""
你是一个数据清洗专家。现在有一个 DataFrame，请生成一段完整的 Python 代码来清洗它。
代码必须包含以下步骤：
1. 删除重复行
2. 处理缺失值（数值列用中位数填充，分类列用"未知"填充）
3. 删除明显异常的离群值（可根据数值列 IQR 判断）

数据信息：
- 列名及类型：
{col_info}
- 每列缺失值数量：
{missing}
- 前2行样本：
{sample}

请**只输出可直接运行的 Python 代码**，不要包含任何解释或 markdown 标记。
代码中假设 df 变量已存在，直接对 df 进行修改，最后不需要 return。
"""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    code = response.choices[0].message.content.strip()
    # 清理可能的代码块标记
    if code.startswith("```python"):
        code = code[9:]
    if code.endswith("```"):
        code = code[:-3]
    return code


def ai_interpret_cleaning_result(df_before, df_after):
    """让AI解读清洗前后的变化"""
    summary = f"""
    清洗前：{df_before.shape[0]}行, 缺失值总数{df_before.isnull().sum().sum()}
    清洗后：{df_after.shape[0]}行, 缺失值总数{df_after.isnull().sum().sum()}
    各列均值变化：{(df_after.mean(numeric_only=True) - df_before.mean(numeric_only=True)).to_dict()}
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
            "role": "user", "content": f"作为数据分析师，用通俗语言解释清洗前后的变化和潜在影响：\n{summary}"
        }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content


# ---- 演示流程 ----
if __name__ == "__main__":
    # 1. 读取外部 CSV（通过命令行参数或默认值）
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        csv_path = "test_data.csv"
        # 如果不存在默认测试文件，可以自动创建一个示例
        if not os.path.exists(csv_path):
            print(f"未找到 {csv_path}，正在生成示例数据...")
            pd.DataFrame({
                "年龄": [25, 30, None, 28, 35, 100],
                "城市": ["北京", "上海", "北京", None, "上海", "广州"],
                "消费": [120, 80, 200, 150, None, 9999]
            }).to_csv(csv_path, index=False)

    print(f"读取数据：{csv_path}")
    df = pd.read_csv(csv_path)
    df_original = df.copy()
    print("原始数据预览：\n", df.head())

    # 1. AI生成清洗代码
    cleaning_code = ai_generate_cleaning_code(df)
    print("\n===== AI生成的清洗代码 =====\n")
    print(cleaning_code)

    # 2. 在安全环境中执行代码
    # 重要：仅在自己可控的环境下使用 exec，或改用更安全的 eval 方式
    try:
        exec(cleaning_code)
    except Exception as e:
        print(f"执行清洗代码时出错：{e}")
        exit()

    print("\n清洗后数据：\n", df)

    # 3. AI解读结果
    interpretation = ai_interpret_cleaning_result(df, df)
    print("\n===== AI解读 =====\n")
    print(interpretation)
    
