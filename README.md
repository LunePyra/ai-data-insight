# 🤖AI数据洞察助手
利用大语言模型自动分析 CSV 文件，生成数据概况、质量问题和清洗建议。

## ✨项目能力
### 📊 CSV 数据智能分析（阶段一）
- 读取 CSV，自动提取行数、列类型、缺失值统计
- 调用大模型生成**数据概况总结、质量问题、清洗建议**

### 🧠 Prompt 工程实战（阶段二）
- **结构化信息提取** —— 从非结构化文本中提取情感、特征、紧急程度，稳定输出 JSON
- **Few-shot 分类** —— 用少量示例教会模型按自定义标准分类（如岗位级别）
- **链式调用** —— AI 生成清洗代码 → 本地执行 → AI 解释结果，实现分析流程自动化

## 🛠技术栈

|组件|说明|
|-|-|
|Python 3.8+|解释器|
|pandas|数据处理|
|openai|大模型通用调用库|
|python-dotenv|安全加载环境变量|
|支持模型|Qwen-plus、DeepSeek-Chat、GLM 等（通过修改 .env 切换）|


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
# 第一阶段：CSV 分析
python data_insight.py

# 第二阶段：结构化提取
python prompt_json.py

# 第二阶段：Few-shot 分类
python prompt_fewshot.py

# 第二阶段：链式调用（生成代码→执行→解读）
python prompt_chain.py
```



## 📂项目结构

```

ai-data-insight/
├── data_insight.py          # 阶段一：CSV 数据智能分析
├── prompt_json.py           # 阶段二：JSON 结构化信息提取
├── prompt_fewshot.py        # 阶段二：Few-shot 自定义分类
├── prompt_chain.py          # 阶段二：链式调用（生成代码→执行→解读）
├── requirements.txt         # Python 依赖
├── .gitignore               # Git 忽略规则
├── env.example              # 环境变量示例（可公开）
└── README.md                # 项目文档

```



## 📈效果展示

第一阶段：CSV 分析

```
正在分析 test_data.csv ...
==================================================
1. 数据概况总结：该数据集包含5条记录，4个字段，涉及用户基本信息和消费数据...
2. 发现的数据质量问题：姓名和年龄列各缺失1个值...
3. 清洗建议：对缺失值较少的列可考虑删除缺失行；年龄缺失可根据均值填充...
==================================================
```

第二阶段：结构化提取

```
输入："物流太慢了，三天还没发货，但是客服态度还行。"
输出：{"sentiment": "负面", "features": ["物流", "客服"], "urgency": "高"}
```

第二阶段：链式调用

```
1. AI 根据数据特征自动生成清洗代码（处理重复值、缺失值、离群值）
2. 本地执行清洗代码
3. AI 解释清洗前后数据的变化及影响
```

---


## 🌱学习路径与后续规划

· 阶段一：API 调用基础
· 阶段二：Prompt 工程（JSON/ Few-shot / 链式调用）
· 阶段三：RAG 知识库问答（向量数据库、文档切片、检索链）
· 阶段四：AI Agent 工具调用
· 增加 Web 界面（Gradio / Streamlit）



## 📧贡献与反馈

如有问题或建议，欢迎通过 GitHub Issues 联系。

如果你觉得这个项目有用，请点亮 🌟 Star 支持一下



## 📄许可
本项目采用 MIT License 开源。





