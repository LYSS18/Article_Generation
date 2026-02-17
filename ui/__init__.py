"""
UI模块 - 图形用户界面
提供基于Tkinter的现代化GUI界面
"""

from .main_window import ArticleGeneratorApp
from .themes import AppTheme
from .components import ModernButton, ModernEntry, ModernTextArea
from .utils import center_window, show_error, show_success, show_info

__all__ = [
    'ArticleGeneratorApp',
    'AppTheme',
    'ModernButton',
    'ModernEntry',
    'ModernTextArea',
    'center_window',
    'show_error',
    'show_success',
    'show_info'
]

__version__ = '1.0.0'

