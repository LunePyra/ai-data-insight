\# 🤖AI数据洞察助手

利用大语言模型自动分析 CSV 文件，生成数据概况、质量问题和清洗建议。



\## ✨功能

1\.输入 CSV 文件路径，自动读取并提取摘要信息

2\.调用云端大模型（支持阿里百炼、DeepSeek 等）

3\.输出结构化中文分析报告：数据概况、质量问题、清洗建议

4\.可作为数据工程日常工作的效率工具



\## 🛠技术栈

=======
# 🤖AI数据洞察助手
利用大语言模型自动分析 CSV 文件，生成数据概况、质量问题和清洗建议。

## ✨功能
1.输入 CSV 文件路径，自动读取并提取摘要信息
2.调用云端大模型（支持阿里百炼、DeepSeek 等）
3.输出结构化中文分析报告：数据概况、质量问题、清洗建议
4.可作为数据工程日常工作的效率工具

## 🛠技术栈
>>>>>>> b8cbc30b1ddf214d187893eba38962faf3460803
|组件|说明|
|-|-|
|Python 3.8+|解释器|
|pandas|数据处理|
|openai|大模型通用调用库|
|python-dotenv|安全加载环境变量|
|支持模型|Qwen-plus、DeepSeek-Chat、GLM 等（通过修改 .env 切换）|

<<<<<<< HEAD


\## 🚀快速开始



\### 1. 克隆仓库

```bash

git clone https://github.com/你的用户名/ai-data-insight.git

cd ai-data-insight

```



\### 2. 安装依赖

```bash

pip install -r requirements.txt

```



\### 3.配置API密钥

```bash

\# 复制示例配置

cp env.example .env

\# 编辑 .env，填入你的真实 Key（支持阿里百炼、DeepSeek、硅基流动等）

```



\### 4.运行实例

```bash

python data\_insight.py

```

程序会自动生成示例数据并调用 AI 分析，结果打印在终端。



\## 🔧使用你自己的数据

```python

from data\_insight import analyze\_csv\_with\_ai



\# 本地任何 CSV 文件都可以

result = analyze\_csv\_with\_ai(test\_file)

print(result)

```



\## 📂项目结构

```

ai-data-insight/

├── data\_insight.py        # 核心脚本：包含数据读取、提示词构建和 API 调用

├── requirements.txt       # Python 依赖清单

├── .gitignore             # Git 忽略规则（保护密钥）

├── env.example            # 环境变量示例文件

└── README.md              # 你正在看这份文档

```



\## 📈效果展示

运行后终端输出示例：



```

正在分析...

==================================================

1\. 数据概况总结

这份数据集共有5行记录和4个字段，包含用户的基本信息和消费数据。数据中存在少量缺失值（姓名、年龄、消费金额各缺失1个），年龄和消费金额的均值分别为29.5岁和114元，数据覆盖北京、上海、广州三个城市。



2\. 发现的数据质量问题

\- 缺失值问题：姓名、年龄、消费金额字段各存在1个缺失值

\- 数据类型问题：年龄字段为浮点数类型，实际应转换为整数类型

\- 潜在异常值：消费金额最小值为55.5，最大值为200，标准差较大（63.29），可能存在离散分布



3\. 清洗建议

\- 对年龄缺失值使用均值29.5填充，并转换为整数类型

\- 对消费金额缺失值使用中位数100.25填充，保持数据分布稳定性

\- 删除姓名字段的缺失记录（因姓名为主标识字段，难以合理填补）



4\. 数据清洗代码

```python

import pandas as pd

import numpy as np



\# 读取原始数据

df = pd.read\_csv('input.csv')

……

```

==================================================

```



\## 🌱未来规划

1\.支持 Excel 文件

2\.生成 Markdown / PDF 报告

3\.加入网页界面（Gradio / Streamlit）

4\.集成 RAG 知识库，辅助专业领域分析



\## 📧贡献与反馈

如有问题或建议，欢迎通过 GitHub Issues 联系。

如果你觉得这个项目有用，请点亮 🌟 Star 支持一下

=======
## 🚀快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/你的用户名/ai-data-insight.git
cd ai-data-insight
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3.配置API密钥
```bash
# 复制示例配置
cp env.example .env
# 编辑 .env，填入你的真实 Key（支持阿里百炼、DeepSeek、硅基流动等）
```

### 4.运行实例
```bash
python data_insight.py
```
程序会自动生成示例数据并调用 AI 分析，结果打印在终端。

## 🔧使用你自己的数据
```python
from data_insight import analyze_csv_with_ai
# 本地任何 CSV 文件都可以
result = analyze_csv_with_ai(test_file)
print(result)
```

## 📂项目结构
```
ai-data-insight/
├── data_insight.py        # 核心脚本：包含数据读取、提示词构建和 API 调用
├── requirements.txt       # Python 依赖清单
├── .gitignore             # Git 忽略规则（保护密钥）
├── env.example            # 环境变量示例文件
└── README.md              # 你正在看这份文档
```

## 📈效果展示
运行后终端输出示例：
```
正在分析...

==================================================
1. 数据概况总结
这份数据集共有5行记录和4个字段，包含用户的基本信息和消费数据。数据中存在少量缺失值（姓名、年龄、消费金额各缺失1个），年龄和消费金额的均值分别为29.5岁和114元，数据覆盖北京、上海、广州三个城市。

2. 发现的数据质量问题
- 缺失值问题：姓名、年龄、消费金额字段各存在1个缺失值
- 数据类型问题：年龄字段为浮点数类型，实际应转换为整数类型
- 潜在异常值：消费金额最小值为55.5，最大值为200，标准差较大（63.29），可能存在离散分布

3. 清洗建议
- 对年龄缺失值使用均值29.5填充，并转换为整数类型
- 对消费金额缺失值使用中位数100.25填充，保持数据分布稳定性
- 删除姓名字段的缺失记录（因姓名为主标识字段，难以合理填补）

4. 数据清洗代码
```python
import pandas as pd
import numpy as np
# 读取原始数据
df = pd.read_csv('input.csv')
……
```

## 🌱未来规划
1.支持 Excel 文件
2.生成 Markdown / PDF 报告
3.加入网页界面（Gradio / Streamlit）
4.集成 RAG 知识库，辅助专业领域分析

## 📧贡献与反馈
如有问题或建议，欢迎通过 GitHub Issues 联系。
如果你觉得这个项目有用，请点亮 🌟 Star 支持一下

## 📄许可
本项目采用 MIT License 开源。





