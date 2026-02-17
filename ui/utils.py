"""
UI工具模块
提供UI相关的辅助函数
"""

import tkinter as tk
from tkinter import messagebox
from typing import Optional


def center_window(window: tk.Tk, width: int, height: int):
    """
    将窗口居中显示
    
    Args:
        window: Tkinter窗口对象
        width: 窗口宽度
        height: 窗口高度
    """
    # 获取屏幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 计算居中位置
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # 设置窗口位置和大小
    window.geometry(f'{width}x{height}+{x}+{y}')


def show_error(title: str, message: str, parent: Optional[tk.Tk] = None):
    """
    显示错误消息框
    
    Args:
        title: 标题
        message: 消息内容
        parent: 父窗口
    """
    messagebox.showerror(title, message, parent=parent)


def show_success(title: str, message: str, parent: Optional[tk.Tk] = None):
    """
    显示成功消息框
    
    Args:
        title: 标题
        message: 消息内容
        parent: 父窗口
    """
    messagebox.showinfo(title, message, parent=parent)


def show_info(title: str, message: str, parent: Optional[tk.Tk] = None):
    """
    显示信息消息框
    
    Args:
        title: 标题
        message: 消息内容
        parent: 父窗口
    """
    messagebox.showinfo(title, message, parent=parent)


def show_warning(title: str, message: str, parent: Optional[tk.Tk] = None):
    """
    显示警告消息框
    
    Args:
        title: 标题
        message: 消息内容
        parent: 父窗口
    """
    messagebox.showwarning(title, message, parent=parent)


def ask_yes_no(title: str, message: str, parent: Optional[tk.Tk] = None) -> bool:
    """
    显示是/否确认框
    
    Args:
        title: 标题
        message: 消息内容
        parent: 父窗口
    
    Returns:
        用户选择（True=是，False=否）
    """
    return messagebox.askyesno(title, message, parent=parent)


def truncate_text(text: str, max_length: int = 50, suffix: str = '...') -> str:
    """
    截断文本
    
    Args:
        text: 原始文本
        max_length: 最大长度
        suffix: 后缀
    
    Returns:
        截断后的文本
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小
    
    Args:
        size_bytes: 字节数
    
    Returns:
        格式化后的大小字符串
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def validate_keyword(keyword: str) -> tuple[bool, str]:
    """
    验证关键词输入
    
    Args:
        keyword: 关键词
    
    Returns:
        (是否有效, 错误消息)
    """
    if not keyword or not keyword.strip():
        return False, "关键词不能为空"
    
    if len(keyword.strip()) < 2:
        return False, "关键词至少需要2个字符"
    
    if len(keyword.strip()) > 100:
        return False, "关键词不能超过100个字符"
    
    return True, ""


def safe_filename(filename: str) -> str:
    """
    生成安全的文件名
    
    Args:
        filename: 原始文件名
    
    Returns:
        安全的文件名
    """
    # 替换不安全的字符
    unsafe_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    safe_name = filename
    for char in unsafe_chars:
        safe_name = safe_name.replace(char, '_')
    return safe_name

