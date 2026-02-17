# UI模块说明文档

## 📁 文件结构

```
ui/
├── __init__.py          # 模块初始化文件
├── main_window.py       # 主窗口类（核心UI逻辑）
├── components.py        # 可复用UI组件
├── themes.py            # 主题配置（颜色、字体、尺寸）
├── utils.py             # UI工具函数
└── README.md            # 本文档
```

## 🎨 模块说明

### 1. `themes.py` - 主题配置

定义了应用程序的视觉风格：

- **颜色配置**：主色调、功能色、背景色、文字色、边框色、状态色
- **字体配置**：标题、副标题、正文、按钮等字体
- **尺寸配置**：窗口大小、内边距、按钮尺寸等
- **动画配置**：动画持续时间

**使用示例：**
```python
from ui.themes import AppTheme

# 获取颜色
primary_color = AppTheme.get_color('primary')

# 获取字体
title_font = AppTheme.get_font('title')

# 获取尺寸
window_width = AppTheme.get_size('window_width')

# 获取按钮样式
button_style = AppTheme.get_button_style('primary')
```

### 2. `components.py` - UI组件

提供可复用的现代化UI组件：

#### ModernButton - 现代化按钮
```python
from ui.components import ModernButton

button = ModernButton(
    parent,
    text="生成文章",
    command=callback_function,
    style='primary',  # primary, success, warning, danger, secondary
    width=15
)

# 设置加载状态
button.set_loading(True)  # 显示加载中
button.set_loading(False) # 恢复正常
```

#### ModernEntry - 现代化输入框
```python
from ui.components import ModernEntry

entry = ModernEntry(
    parent,
    placeholder="请输入关键词",
    width=50
)

# 获取值（自动排除占位符）
value = entry.get_value()
```

#### ModernTextArea - 现代化文本区域
```python
from ui.components import ModernTextArea

text_area = ModernTextArea(
    parent,
    placeholder="文章内容将显示在这里",
    height=15
)
```

### 3. `utils.py` - 工具函数

提供UI相关的辅助函数：

```python
from ui.utils import (
    center_window,      # 窗口居中
    show_error,         # 显示错误消息
    show_success,       # 显示成功消息
    show_info,          # 显示信息消息
    show_warning,       # 显示警告消息
    ask_yes_no,         # 显示确认对话框
    validate_keyword,   # 验证关键词
    safe_filename,      # 生成安全文件名
)

# 窗口居中
center_window(root, 800, 600)

# 显示消息
show_success("成功", "文章生成完成！")

# 验证输入
is_valid, error_msg = validate_keyword(keyword)
```

### 4. `main_window.py` - 主窗口

应用程序的主窗口类，包含完整的UI布局和业务逻辑。

**主要功能：**
- 文章生成
- 文章保存
- 状态管理
- 错误处理

## 🚀 使用方法

### 启动GUI界面

**方式1：双击批处理文件（推荐）**
```
双击 "快速启动GUI.bat"
```

**方式2：命令行启动**
```bash
conda activate py10
python main_gui.py
```

**方式3：使用scripts文件夹**
```
双击 "scripts\run_gui.bat"
```

### 使用流程

1. **启动程序** - 等待生成器初始化完成
2. **输入主题** - 在"主题关键词"框中输入关键词
3. **添加描述**（可选）- 在"主题描述"框中输入详细描述
4. **生成文章** - 点击"🚀 生成文章"按钮
5. **查看结果** - 文章将显示在输出区域
6. **保存文章** - 点击"💾 保存文章"按钮保存到文件

## 🎨 界面特性

### 现代化设计
- ✅ 清晰的视觉层次
- ✅ 舒适的配色方案
- ✅ 响应式布局
- ✅ 悬停效果
- ✅ 状态指示器

### 用户体验
- ✅ 实时状态反馈
- ✅ 加载动画
- ✅ 错误提示
- ✅ 输入验证
- ✅ 快捷操作

### 功能完善
- ✅ 异步生成（不阻塞UI）
- ✅ 自动保存对话框
- ✅ 文件名安全处理
- ✅ 字数统计
- ✅ 清空功能

## 🔧 自定义主题

如需自定义界面样式，编辑 `themes.py` 文件：

```python
# 修改颜色
COLORS = {
    'primary': '#your_color',  # 修改主色调
    # ...
}

# 修改字体
FONTS = {
    'title': ('Your Font', 24, 'bold'),
    # ...
}

# 修改尺寸
SIZES = {
    'window_width': 1200,  # 修改窗口宽度
    # ...
}
```

## 📝 开发说明

### 添加新组件

1. 在 `components.py` 中定义新组件类
2. 继承自Tkinter基础组件
3. 应用AppTheme样式
4. 在 `__init__.py` 中导出

### 添加新功能

1. 在 `main_window.py` 中添加方法
2. 创建对应的UI元素
3. 绑定事件处理函数
4. 更新状态显示

## ⚠️ 注意事项

1. **线程安全**：UI更新必须在主线程中进行，使用 `root.after()` 方法
2. **异常处理**：所有用户操作都应有异常处理
3. **状态管理**：及时更新状态指示器和底部状态栏
4. **资源清理**：窗口关闭时检查是否有正在进行的任务

## 🐛 常见问题

**Q: 窗口无法显示？**
A: 确保已安装Python的tkinter模块（通常随Python一起安装）

**Q: 中文显示乱码？**
A: 检查字体设置，确保使用支持中文的字体（如Microsoft YaHei UI）

**Q: 按钮点击无响应？**
A: 检查是否在生成过程中，查看状态指示器

**Q: 保存文件失败？**
A: 检查output文件夹权限，确保有写入权限

