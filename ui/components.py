"""
UI组件模块
提供可复用的现代化UI组件
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Optional, Callable
from .themes import AppTheme


class ModernButton(tk.Button):
    """现代化按钮组件"""
    
    def __init__(self, parent, text: str, command: Optional[Callable] = None,
                 style: str = 'primary', width: int = 15, **kwargs):
        """
        初始化现代化按钮
        
        Args:
            parent: 父组件
            text: 按钮文字
            command: 点击回调函数
            style: 样式类型 (primary, success, warning, danger, secondary)
            width: 按钮宽度
        """
        # 获取样式
        button_style = AppTheme.get_button_style(style)
        
        # 默认配置
        config = {
            'text': text,
            'command': command,
            'font': AppTheme.get_font('button'),
            'bg': button_style['bg'],
            'fg': button_style['fg'],
            'activebackground': button_style['active_bg'],
            'activeforeground': AppTheme.get_color('text_white'),
            'relief': tk.FLAT,
            'bd': 0,
            'padx': 20,
            'pady': 10,
            'cursor': 'hand2',
            'width': width,
        }
        config.update(kwargs)
        
        super().__init__(parent, **config)
        
        # 保存样式信息
        self.style_type = style
        self.button_style = button_style
        self.is_disabled = False
        
        # 绑定悬停效果
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
    
    def _on_enter(self, event):
        """鼠标进入"""
        if not self.is_disabled:
            self.config(bg=self.button_style['hover_bg'])
    
    def _on_leave(self, event):
        """鼠标离开"""
        if not self.is_disabled:
            self.config(bg=self.button_style['bg'])
    
    def set_loading(self, loading: bool = True):
        """设置加载状态"""
        if loading:
            self.is_disabled = True
            self.config(
                state=tk.DISABLED,
                bg=AppTheme.get_color('border_medium'),
                cursor='wait'
            )
        else:
            self.is_disabled = False
            self.config(
                state=tk.NORMAL,
                bg=self.button_style['bg'],
                cursor='hand2'
            )


class ModernEntry(tk.Entry):
    """现代化输入框组件"""
    
    def __init__(self, parent, placeholder: str = '', **kwargs):
        """
        初始化现代化输入框
        
        Args:
            parent: 父组件
            placeholder: 占位符文字
        """
        # 默认配置
        config = {
            'font': AppTheme.get_font('body'),
            'bg': AppTheme.get_color('bg_primary'),
            'fg': AppTheme.get_color('text_primary'),
            'relief': tk.SOLID,
            'bd': 1,
            'highlightthickness': 2,
            'highlightbackground': AppTheme.get_color('border_light'),
            'highlightcolor': AppTheme.get_color('primary'),
            'insertbackground': AppTheme.get_color('text_primary'),
        }
        config.update(kwargs)
        
        super().__init__(parent, **config)
        
        # 占位符
        self.placeholder = placeholder
        self.placeholder_active = False
        
        if placeholder:
            self._show_placeholder()
            self.bind('<FocusIn>', self._on_focus_in)
            self.bind('<FocusOut>', self._on_focus_out)
    
    def _show_placeholder(self):
        """显示占位符"""
        if not self.get():
            self.placeholder_active = True
            self.insert(0, self.placeholder)
            self.config(fg=AppTheme.get_color('text_tertiary'))
    
    def _hide_placeholder(self):
        """隐藏占位符"""
        if self.placeholder_active:
            self.placeholder_active = False
            self.delete(0, tk.END)
            self.config(fg=AppTheme.get_color('text_primary'))
    
    def _on_focus_in(self, event):
        """获得焦点"""
        self._hide_placeholder()
    
    def _on_focus_out(self, event):
        """失去焦点"""
        if not self.get():
            self._show_placeholder()
    
    def get_value(self) -> str:
        """获取实际值（排除占位符）"""
        if self.placeholder_active:
            return ''
        return self.get()


class ModernTextArea(scrolledtext.ScrolledText):
    """现代化文本区域组件"""
    
    def __init__(self, parent, placeholder: str = '', **kwargs):
        """
        初始化现代化文本区域
        
        Args:
            parent: 父组件
            placeholder: 占位符文字
        """
        # 默认配置
        config = {
            'font': AppTheme.get_font('body_en'),
            'bg': AppTheme.get_color('bg_primary'),
            'fg': AppTheme.get_color('text_primary'),
            'relief': tk.SOLID,
            'bd': 1,
            'wrap': tk.WORD,
            'padx': 10,
            'pady': 10,
        }
        config.update(kwargs)
        
        super().__init__(parent, **config)

