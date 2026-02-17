# 快速入门指南 - Quick Start Guide

## 🚀 5分钟快速开始

### 步骤1：安装依赖（首次使用）

**Windows用户：**
```
双击 "scripts\setup.bat"
```

**或手动安装：**
```bash
conda activate py10
pip install -r requirements.txt
```

### 步骤2：配置API密钥

1. 打开 `config` 文件夹
2. 复制 `.env.example` 为 `.env`
3. 编辑 `.env` 文件，填入你的API密钥

**推荐配置（硅基流动）：**
```env
API_KEY=sk-你的密钥
API_BASE_URL=https://api.siliconflow.cn/v1
MODEL_NAME=Qwen/Qwen2.5-7B-Instruct
```

### 步骤3：启动程序

#### 🎨 GUI界面（推荐）
```
双击 "快速启动GUI.bat"
```

#### 💻 命令行界面
```
双击 "快速启动.bat"
```

---

## 📖 详细使用说明

### GUI界面使用

1. **启动程序** - 双击 `快速启动GUI.bat`
2. **等待初始化** - 看到"就绪"状态后可以开始使用
3. **输入主题** - 在"主题关键词"框输入关键词
4. **生成文章** - 点击"🚀 生成文章"按钮
5. **保存文章** - 点击"💾 保存文章"按钮

**示例关键词：**
- cultural shock
- friendship
- hospitality
- intercultural communication

### 命令行界面使用

1. **启动程序** - 双击 `快速启动.bat`
2. **选择选项** - 输入 `1` 生成文章
3. **输入关键词** - 例如：`cultural shock`
4. **等待生成** - 文章自动保存到 `output/` 文件夹

---

## 🔧 常见问题

### Q1: 如何获取API密钥？

**硅基流动（推荐）：**
1. 访问 https://siliconflow.cn/
2. 注册账号（手机号即可）
3. 进入控制台 → API密钥
4. 创建并复制密钥

**DeepSeek：**
1. 访问 https://platform.deepseek.com/
2. 注册账号
3. 充值$5（可用很久）
4. 获取API密钥

### Q2: 程序无法启动？

**检查清单：**
- ✅ 已安装Python 3.10+
- ✅ 已激活conda环境（py10）
- ✅ 已安装依赖（运行setup.bat）
- ✅ 已配置.env文件

### Q3: 生成失败？

**可能原因：**
1. API密钥错误 - 检查.env文件
2. 网络问题 - 使用国内可访问的API
3. 余额不足 - 检查账户余额

### Q4: GUI界面无法显示？

**解决方案：**
- Windows: tkinter通常已安装
- Linux: `sudo apt-get install python3-tk`
- macOS: `brew install python-tk`

---

## 💡 使用技巧

### 1. 提高文章质量

- 使用更具体的关键词
- 添加详细的主题描述
- 尝试更大参数的模型

### 2. 批量生成

编辑 `config/topics.json` 添加主题，然后使用批量生成功能

### 3. 自定义参数

编辑 `.env` 文件调整：
- `ARTICLE_LENGTH` - 文章长度
- `TEMPERATURE` - 创造性（0.5-0.9）
- `MAX_TOKENS` - 最大生成长度

---

## 📞 获取帮助

- 查看完整文档：`README.md`
- UI模块说明：`ui/README.md`
- 测试连接：运行 `python test_connection.py`

---

**祝使用愉快！🎉**

