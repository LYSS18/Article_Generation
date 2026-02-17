# 英文文章生成器 - Article Generator

基于AI模型的CET-6级别英文文章生成器

## 📖 项目简介

这是一个使用AI模型自动生成CET-6（大学英语六级）标准英文文章的工具。文章符合六级写作要求，包含标题和3个段落，适合英语学习和写作参考。

## ✨ 功能特点

- ✅ 按CET-6标准生成文章
- ✅ 自动生成标题和3段式结构
- ✅ 使用六级词汇和句式
- ✅ 支持自定义关键词
- ✅ 文章长度约200词
- ✅ 自动保存到文件
- ✅ **现代化GUI界面**（新增）
- ✅ **命令行界面**（原有）

## 📋 环境要求

- Python 3.10+
- conda（推荐使用py10虚拟环境）
- 网络连接

## 🚀 快速开始

### 第一步：获取API密钥

#### 方案1：硅基流动 SiliconFlow（推荐，国内服务）

**优点：**
- ✅ 国内可直接访问，无需VPN
- ✅ 新用户有免费额度
- ✅ 注册简单，只需手机号
- ✅ 质量好，速度快

**注册步骤：**

1. 访问：https://siliconflow.cn/
2. 点击"注册"，使用手机号注册
3. 登录后，点击"API密钥"
4. 创建密钥并复制（格式：`sk-...`）

#### 方案2：DeepSeek（国内服务，质量最高）

**优点：**
- ✅ 国内可直接访问
- ✅ 质量接近GPT-4
- ✅ 价格极低（约$0.01生成16篇）

**注册步骤：**

1. 访问：https://platform.deepseek.com/
2. 使用手机号注册
3. 充值$5（可用很久）
4. 获取API密钥

#### 方案3：OpenAI官方（需要VPN）

**注册步骤：**

1. 访问：https://platform.openai.com/api-keys
2. 注册并登录
3. 创建API密钥
4. 复制密钥（格式：`sk-proj-...`）

### 第二步：安装依赖

#### Windows用户（推荐）

双击运行 `scripts\setup.bat`

#### 手动安装

```bash
# 激活conda环境
conda activate py10

# 安装依赖
pip install -r requirements.txt
```

### 第三步：配置API密钥

**方法1：手动创建配置文件**

1. 复制 `config\.env.example` 为 `config\.env`
2. 编辑 `config\.env` 文件，填入你的API密钥

**方法2：运行setup.bat自动创建**

双击 `scripts\setup.bat`，会自动创建 `config\.env` 文件

**配置示例：**

#### 使用硅基流动（推荐）

```env
API_KEY=sk-你的硅基流动密钥
API_BASE_URL=https://api.siliconflow.cn/v1
MODEL_NAME=Qwen/Qwen2.5-7B-Instruct
```

**可选模型：**
- `Qwen/Qwen2.5-7B-Instruct` - 速度快，质量好（推荐）
- `Qwen/Qwen2.5-32B-Instruct` - 质量更高
- `Qwen/Qwen2.5-72B-Instruct` - 质量最高

#### 使用DeepSeek

```env
API_KEY=sk-你的DeepSeek密钥
API_BASE_URL=https://api.deepseek.com/v1
MODEL_NAME=deepseek-chat
```

#### 使用OpenAI

```env
API_KEY=sk-proj-你的OpenAI密钥
API_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini
```

### 第四步：运行程序

本项目提供两种界面：**GUI图形界面**（推荐）和**命令行界面**

#### 🎨 GUI图形界面（推荐，默认模式）

**方式1：Windows批处理启动**
```
双击 "scripts\run.bat"
```

**方式2：命令行运行**
```bash
conda activate py10
python main.py
```

#### 💻 命令行界面

**命令行运行**
```bash
conda activate py10
python main.py --cli
```

## 💡 使用说明

### 🎨 GUI界面使用（推荐）

**启动程序：**
- Windows: 双击 `scripts\run.bat`
- 命令行: `python main.py`

**操作步骤：**

1. **等待初始化** - 程序启动后会自动初始化生成器
2. **输入关键词** - 在"主题关键词"输入框中输入主题（如：cultural shock）
3. **添加描述**（可选）- 在"主题描述"输入框中添加详细描述
4. **生成文章** - 点击"🚀 生成文章"按钮
5. **查看结果** - 文章将显示在下方的输出区域
6. **保存文章** - 点击"💾 保存文章"按钮，选择保存位置
7. **清空输出** - 点击"🗑️ 清空"按钮清空输出区域

**界面特性：**
- ✅ 实时状态显示
- ✅ 加载动画提示
- ✅ 字数统计
- ✅ 自动保存对话框
- ✅ 错误提示
- ✅ 现代化设计

### 💻 命令行界面使用

**启动程序：** `python main.py --cli`

**操作步骤：**

运行程序后，会看到以下菜单：

```text
============================================================
Please select an option:
============================================================
1. Generate an article by keyword
0. Exit
============================================================
```

**生成文章：**

1. 输入 `1` 选择生成文章
2. 输入主题关键词（例如：`cultural shock`、`hospitality`、`friendship`等）
3. 等待生成（通常5-10秒）
4. 文章自动保存到 `output/` 文件夹

### 使用示例

```text
Enter your choice (0-1): 1

Enter the keyword/topic: cultural shock

🚀 Generating CET-6 level article for: cultural shock
✓ Article saved to: output\cultural_shock.txt
```

## 📝 文章格式

生成的文章格式如下：

```
Topic: cultural shock
============================================================

Understanding Cultural Shock in Cross-Cultural Transitions

Cultural shock is a phenomenon experienced by individuals who find
themselves in a new and unfamiliar cultural environment. This process
often involves an initial period of disorientation and confusion...

For instance, expatriates moving to a foreign country often report
experiencing a sudden loss of familiarity and control. As the individual
begins to understand and integrate the new cultural norms...

Research has indicated that cultural competence significantly mitigates
the severity of cultural shock. Overall, cultural shock is a complex
experience that requires nuanced understanding...
```

**文章特点：**

- ✅ 有清晰的标题
- ✅ 分为2-4个段落（结构灵活，逻辑清晰）
- ✅ 段落间有空行
- ✅ 使用CET-6级别词汇
- ✅ 包含过渡词和多样句式
- ✅ 约200词
- ✅ 符合CET-6写作标准

## 📂 输出文件

生成的文章保存在 `output/` 文件夹中：

- 文件名格式：`关键词.txt`
- 例如：`cultural_shock.txt`、`hospitality.txt`

## 🔧 故障排除

### 问题1：ModuleNotFoundError

**解决方案：**
```bash
conda activate py10
pip install -r requirements.txt
```

### 问题2：Connection error

**可能原因：**
- OpenAI API在国内无法访问（需要VPN）
- 网络连接问题

**解决方案：**
- 改用硅基流动或DeepSeek（国内可访问）
- 或使用VPN

### 问题3：API密钥错误

**解决方案：**

- 检查 `config\.env` 文件中的API密钥是否正确
- 确认密钥没有多余的空格
- 确认使用了正确的API_BASE_URL

### 问题4：找不到config/.env文件

**错误提示：**
```
⚠️  Warning: config/.env file not found!
```

**解决方案：**

1. 确认 `config\.env` 文件存在
2. 如果不存在，复制 `config\.env.example` 为 `config\.env`
3. 或者运行 `scripts\setup.bat` 自动创建

### 问题5：生成的文章质量不理想

**解决方案：**

- 尝试更换模型（如使用更大参数的模型）
- 调整 `TEMPERATURE` 参数（0.5-0.9之间）
- 提供更具体的主题词

### 问题6：GUI界面无法启动

**可能原因：**
- tkinter模块未安装（通常随Python一起安装）

**解决方案：**

**Windows:**
```bash
# tkinter通常已包含在Python中，如果缺失：
# 重新安装Python，确保勾选"tcl/tk and IDLE"选项
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

**macOS:**
```bash
# tkinter通常已包含在Python中
# 如果缺失，重新安装Python
brew install python-tk
```

## 💰 费用说明

### 硅基流动
- 新用户有免费额度
- 免费额度足够生成几百篇文章

### DeepSeek
- 价格：约$0.14/百万tokens
- 生成一篇文章：约$0.0001（几乎免费）

### OpenAI
- 价格：约$0.15/百万tokens
- 生成一篇文章：约$0.0001

## 📁 项目结构

```
Article_Generation/
├── config/                 # 配置文件夹
│   ├── .env                # 环境变量（需自己配置）
│   ├── .env.example        # 环境变量示例
│   └── topics.json         # 主题配置（预设主题）
├── scripts/                # 脚本文件夹
│   ├── setup.bat           # 环境配置脚本（Windows）
│   ├── run.bat             # 命令行运行脚本
│   └── run_gui.bat         # GUI运行脚本
├── src/                    # 源代码文件夹
│   ├── __init__.py
│   ├── generator.py        # 核心生成器
│   └── prompts.py          # CET-6提示词模板
├── ui/                     # UI界面文件夹
│   ├── __init__.py         # UI模块初始化
│   ├── main_window.py      # 主窗口类
│   ├── components.py       # UI组件
│   ├── themes.py           # 主题配置
│   ├── utils.py            # UI工具函数
│   └── README.md           # UI模块说明
├── output/                 # 输出文件夹
├── requirements.txt        # Python依赖
├── main.py                 # 统一启动入口（默认GUI，支持--cli参数）
├── test_connection.py      # 连接测试工具
└── README.md               # 本文档
```

## 🛠️ 技术栈

- **Python 3.10+**
- **OpenAI SDK** - 兼容多种API
- **python-dotenv** - 环境变量管理
- **Tkinter** - GUI界面（Python内置）

## 📚 推荐主题词

以下是一些适合生成的主题词：

**跨文化交流类：**
- cultural shock
- cultural values
- intercultural communication
- cross-cultural understanding
- cultural diversity

**社交类：**
- friendship
- hospitality
- social media
- friend circle
- communication skills

**文化概念类：**
- individualism
- collectivism
- stereotype
- cultural identity
- tradition

**语言类：**
- body language
- non-verbal communication
- language barrier
- cultural-loaded words


**祝使用愉快！🎉**
