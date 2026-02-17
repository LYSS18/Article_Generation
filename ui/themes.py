"""
主题配置模块
定义应用程序的颜色主题和样式
"""

from typing import Dict


class AppTheme:
    """应用程序主题类"""
    
    # 颜色配置
    COLORS = {
        # 主色调
        'primary': '#2563eb',           # 蓝色
        'primary_hover': '#1d4ed8',     # 蓝色悬停
        'primary_dark': '#1e40af',      # 深蓝色
        'primary_light': '#3b82f6',     # 浅蓝色
        
        # 功能色
        'success': '#10b981',           # 绿色
        'success_hover': '#059669',     # 绿色悬停
        'warning': '#f59e0b',           # 橙色
        'warning_hover': '#d97706',     # 橙色悬停
        'danger': '#ef4444',            # 红色
        'danger_hover': '#dc2626',      # 红色悬停
        'info': '#3b82f6',              # 信息蓝
        
        # 背景色
        'bg_primary': '#ffffff',        # 主背景（白色）
        'bg_secondary': '#f8fafc',      # 次背景（浅灰）
        'bg_tertiary': '#f1f5f9',       # 三级背景
        'bg_dark': '#1e293b',           # 深色背景
        
        # 文字色
        'text_primary': '#1e293b',      # 主文字（深灰）
        'text_secondary': '#64748b',    # 次文字（灰色）
        'text_tertiary': '#94a3b8',     # 三级文字（浅灰）
        'text_white': '#ffffff',        # 白色文字
        'text_muted': '#cbd5e1',        # 弱化文字
        
        # 边框色
        'border_light': '#e2e8f0',      # 浅边框
        'border_medium': '#cbd5e1',     # 中边框
        'border_dark': '#94a3b8',       # 深边框
        
        # 状态色
        'status_ready': '#10b981',      # 就绪（绿色）
        'status_busy': '#f59e0b',       # 忙碌（橙色）
        'status_error': '#ef4444',      # 错误（红色）
        'status_idle': '#94a3b8',       # 空闲（灰色）
    }
    
    # 字体配置
    FONTS = {
        'title': ('Microsoft YaHei UI', 24, 'bold'),
        'subtitle': ('Microsoft YaHei UI', 14, 'bold'),
        'heading': ('Microsoft YaHei UI', 12, 'bold'),
        'body': ('Microsoft YaHei UI', 10),
        'body_en': ('Arial', 10),
        'small': ('Microsoft YaHei UI', 9),
        'code': ('Consolas', 10),
        'button': ('Microsoft YaHei UI', 10, 'bold'),
    }
    
    # 尺寸配置
    SIZES = {
        'window_width': 1000,
        'window_height': 750,
        'window_min_width': 800,
        'window_min_height': 600,
        
        'padding_large': 20,
        'padding_medium': 15,
        'padding_small': 10,
        'padding_tiny': 5,
        
        'button_height': 40,
        'button_width': 120,
        'input_height': 35,
        
        'border_radius': 8,
        'border_width': 1,
    }
    
    # 动画配置
    ANIMATION = {
        'duration_fast': 150,       # 毫秒
        'duration_normal': 300,
        'duration_slow': 500,
    }
    
    @classmethod
    def get_color(cls, key: str) -> str:
        """获取颜色值"""
        return cls.COLORS.get(key, '#000000')
    
    @classmethod
    def get_font(cls, key: str) -> tuple:
        """获取字体配置"""
        return cls.FONTS.get(key, ('Microsoft YaHei UI', 10))
    
    @classmethod
    def get_size(cls, key: str) -> int:
        """获取尺寸值"""
        return cls.SIZES.get(key, 0)
    
    @classmethod
    def get_button_style(cls, style_type: str = 'primary') -> Dict:
        """获取按钮样式"""
        styles = {
            'primary': {
                'bg': cls.COLORS['primary'],
                'fg': cls.COLORS['text_white'],
                'hover_bg': cls.COLORS['primary_hover'],
                'active_bg': cls.COLORS['primary_dark'],
            },
            'success': {
                'bg': cls.COLORS['success'],
                'fg': cls.COLORS['text_white'],
                'hover_bg': cls.COLORS['success_hover'],
                'active_bg': '#047857',
            },
            'warning': {
                'bg': cls.COLORS['warning'],
                'fg': cls.COLORS['text_white'],
                'hover_bg': cls.COLORS['warning_hover'],
                'active_bg': '#b45309',
            },
            'danger': {
                'bg': cls.COLORS['danger'],
                'fg': cls.COLORS['text_white'],
                'hover_bg': cls.COLORS['danger_hover'],
                'active_bg': '#b91c1c',
            },
            'secondary': {
                'bg': cls.COLORS['bg_tertiary'],
                'fg': cls.COLORS['text_primary'],
                'hover_bg': cls.COLORS['border_medium'],
                'active_bg': cls.COLORS['border_dark'],
            },
        }
        return styles.get(style_type, styles['primary'])

