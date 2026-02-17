"""
主窗口模块
定义应用程序的主窗口界面
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import threading
import os
from typing import Optional
from datetime import datetime

from .themes import AppTheme
from .components import ModernButton, ModernEntry, ModernTextArea
from .utils import center_window, show_error, show_success, show_info, validate_keyword, safe_filename

# 导入生成器（使用相对导入）
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.generator import ArticleGenerator


class ArticleGeneratorApp:
    """文章生成器主应用程序"""
    
    def __init__(self, root: tk.Tk):
        """
        初始化应用程序
        
        Args:
            root: Tkinter根窗口
        """
        self.root = root
        self.root.title("英文文章生成器 - Article Generator")
        
        # 设置窗口大小和位置
        width = AppTheme.get_size('window_width')
        height = AppTheme.get_size('window_height')
        center_window(self.root, width, height)
        
        # 设置最小窗口大小
        self.root.minsize(
            AppTheme.get_size('window_min_width'),
            AppTheme.get_size('window_min_height')
        )
        
        # 设置窗口图标（如果有）
        # self.root.iconbitmap('icon.ico')
        
        # 设置背景色
        self.root.configure(bg=AppTheme.get_color('bg_secondary'))
        
        # 初始化变量
        self.generator: Optional[ArticleGenerator] = None
        self.is_generating = False
        self.current_article = ""
        
        # 创建UI
        self.create_ui()
        
        # 初始化生成器
        self.initialize_generator()
        
        # 绑定关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_ui(self):
        """创建用户界面"""
        # 创建主容器
        main_container = tk.Frame(
            self.root,
            bg=AppTheme.get_color('bg_secondary')
        )
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 创建各个区域
        self.create_header(main_container)
        self.create_status_section(main_container)
        self.create_input_section(main_container)
        self.create_button_section(main_container)
        self.create_output_section(main_container)
        self.create_footer(main_container)
    
    def create_header(self, parent):
        """创建标题区域"""
        header_frame = tk.Frame(parent, bg=AppTheme.get_color('bg_secondary'))
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # 主标题
        title_label = tk.Label(
            header_frame,
            text="📝 英文文章生成器",
            font=AppTheme.get_font('title'),
            bg=AppTheme.get_color('bg_secondary'),
            fg=AppTheme.get_color('text_primary')
        )
        title_label.pack()
        
        # 副标题
        subtitle_label = tk.Label(
            header_frame,
            text="CET-6 Level Article Generator",
            font=AppTheme.get_font('body_en'),
            bg=AppTheme.get_color('bg_secondary'),
            fg=AppTheme.get_color('text_secondary')
        )
        subtitle_label.pack(pady=(5, 0))
    
    def create_status_section(self, parent):
        """创建状态指示区域"""
        status_frame = tk.Frame(
            parent,
            bg=AppTheme.get_color('bg_primary'),
            relief=tk.FLAT,
            bd=0
        )
        status_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 内部容器
        status_container = tk.Frame(status_frame, bg=AppTheme.get_color('bg_primary'))
        status_container.pack(pady=12, padx=15)
        
        # 状态指示器
        self.status_indicator = tk.Label(
            status_container,
            text="●",
            font=('Arial', 14),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('status_idle')
        )
        self.status_indicator.pack(side=tk.LEFT, padx=(0, 8))
        
        # 状态文字
        self.status_label = tk.Label(
            status_container,
            text="正在初始化...",
            font=AppTheme.get_font('body'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_secondary')
        )
        self.status_label.pack(side=tk.LEFT)
        
        # 模型信息（右侧）
        self.model_label = tk.Label(
            status_container,
            text="",
            font=AppTheme.get_font('small'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_tertiary')
        )
        self.model_label.pack(side=tk.RIGHT, padx=(15, 0))
    
    def create_input_section(self, parent):
        """创建输入区域"""
        input_frame = tk.LabelFrame(
            parent,
            text="  输入主题  ",
            font=AppTheme.get_font('heading'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_primary'),
            relief=tk.FLAT,
            bd=1,
            padx=15,
            pady=15
        )
        input_frame.pack(fill=tk.X, pady=(0, 15))

        # 关键词标签
        keyword_label = tk.Label(
            input_frame,
            text="主题关键词:",
            font=AppTheme.get_font('body'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_primary')
        )
        keyword_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

        # 关键词输入框
        self.keyword_entry = ModernEntry(
            input_frame,
            placeholder="例如: cultural shock, friendship, hospitality",
            width=60
        )
        self.keyword_entry.grid(row=1, column=0, sticky=tk.EW, pady=(0, 10))

        # 描述标签（可选）
        desc_label = tk.Label(
            input_frame,
            text="主题描述（可选）:",
            font=AppTheme.get_font('body'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_primary')
        )
        desc_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

        # 描述输入框
        self.description_entry = ModernEntry(
            input_frame,
            placeholder="例如: An essay about cultural differences",
            width=60
        )
        self.description_entry.grid(row=3, column=0, sticky=tk.EW)

        # 配置列权重
        input_frame.columnconfigure(0, weight=1)

    def create_button_section(self, parent):
        """创建按钮区域"""
        button_frame = tk.Frame(parent, bg=AppTheme.get_color('bg_secondary'))
        button_frame.pack(fill=tk.X, pady=(0, 15))

        # 按钮容器（居中）
        button_container = tk.Frame(button_frame, bg=AppTheme.get_color('bg_secondary'))
        button_container.pack()

        # 生成按钮
        self.generate_btn = ModernButton(
            button_container,
            text="🚀 生成文章",
            command=self.generate_article,
            style='primary',
            width=18
        )
        self.generate_btn.pack(side=tk.LEFT, padx=5)

        # 保存按钮
        self.save_btn = ModernButton(
            button_container,
            text="💾 保存文章",
            command=self.save_article,
            style='success',
            width=18
        )
        self.save_btn.pack(side=tk.LEFT, padx=5)
        self.save_btn.config(state=tk.DISABLED)

        # 清空按钮
        self.clear_btn = ModernButton(
            button_container,
            text="🗑️ 清空",
            command=self.clear_output,
            style='secondary',
            width=12
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)

    def create_output_section(self, parent):
        """创建输出区域"""
        output_frame = tk.LabelFrame(
            parent,
            text="  生成的文章  ",
            font=AppTheme.get_font('heading'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_primary'),
            relief=tk.FLAT,
            bd=1,
            padx=15,
            pady=15
        )
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # 文本区域
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            font=AppTheme.get_font('body_en'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_primary'),
            relief=tk.FLAT,
            bd=0,
            wrap=tk.WORD,
            padx=10,
            pady=10,
            height=15
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # 设置为只读
        self.output_text.config(state=tk.DISABLED)

    def create_footer(self, parent):
        """创建底部状态栏"""
        footer_frame = tk.Frame(
            parent,
            bg=AppTheme.get_color('bg_primary'),
            height=35
        )
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)

        # 左侧信息
        self.footer_label = tk.Label(
            footer_frame,
            text="就绪",
            font=AppTheme.get_font('small'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_secondary'),
            anchor=tk.W
        )
        self.footer_label.pack(side=tk.LEFT, padx=15, fill=tk.X, expand=True)

        # 右侧版本信息
        version_label = tk.Label(
            footer_frame,
            text="v1.0.0",
            font=AppTheme.get_font('small'),
            bg=AppTheme.get_color('bg_primary'),
            fg=AppTheme.get_color('text_tertiary'),
            anchor=tk.E
        )
        version_label.pack(side=tk.RIGHT, padx=15)

    def initialize_generator(self):
        """初始化文章生成器"""
        def init_task():
            try:
                self.update_status("正在初始化生成器...", 'busy')
                self.generator = ArticleGenerator()

                # 更新UI
                self.root.after(0, lambda: self.on_generator_ready())

            except Exception as e:
                error_msg = str(e)
                self.root.after(0, lambda: self.on_generator_error(error_msg))

        # 在后台线程初始化
        thread = threading.Thread(target=init_task, daemon=True)
        thread.start()

    def on_generator_ready(self):
        """生成器就绪回调"""
        model_info = f"模型: {self.generator.model_name}"
        self.model_label.config(text=model_info)
        self.update_status("就绪 - 可以开始生成文章", 'ready')
        self.footer_label.config(text=f"就绪 | 目标字数: {self.generator.article_length} 词")

    def on_generator_error(self, error_msg: str):
        """生成器错误回调"""
        self.update_status("初始化失败", 'error')
        show_error(
            "初始化失败",
            f"无法初始化文章生成器:\n\n{error_msg}\n\n请检查 config/.env 文件配置。",
            self.root
        )

    def update_status(self, message: str, status_type: str = 'idle'):
        """
        更新状态显示

        Args:
            message: 状态消息
            status_type: 状态类型 (ready, busy, error, idle)
        """
        status_colors = {
            'ready': AppTheme.get_color('status_ready'),
            'busy': AppTheme.get_color('status_busy'),
            'error': AppTheme.get_color('status_error'),
            'idle': AppTheme.get_color('status_idle'),
        }

        color = status_colors.get(status_type, status_colors['idle'])
        self.status_indicator.config(fg=color)
        self.status_label.config(text=message)

    def generate_article(self):
        """生成文章"""
        # 检查生成器是否就绪
        if not self.generator:
            show_error("错误", "生成器未初始化，请稍后再试。", self.root)
            return

        # 检查是否正在生成
        if self.is_generating:
            show_info("提示", "正在生成文章，请稍候...", self.root)
            return

        # 获取关键词
        keyword = self.keyword_entry.get_value().strip()

        # 验证关键词
        is_valid, error_msg = validate_keyword(keyword)
        if not is_valid:
            show_error("输入错误", error_msg, self.root)
            return

        # 获取描述
        description = self.description_entry.get_value().strip()
        if not description:
            description = f"An essay about {keyword}"

        # 开始生成
        self.is_generating = True
        self.generate_btn.set_loading(True)
        self.save_btn.config(state=tk.DISABLED)
        self.update_status(f"正在生成文章: {keyword}...", 'busy')
        self.footer_label.config(text=f"生成中... | 主题: {keyword}")

        # 清空输出
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

        # 在后台线程生成
        def generate_task():
            try:
                article = self.generator.generate_article(keyword, description)
                self.root.after(0, lambda: self.on_article_generated(keyword, article))
            except Exception as e:
                error_msg = str(e)
                self.root.after(0, lambda: self.on_generation_error(error_msg))

        thread = threading.Thread(target=generate_task, daemon=True)
        thread.start()

    def on_article_generated(self, keyword: str, article: str):
        """文章生成完成回调"""
        self.is_generating = False
        self.generate_btn.set_loading(False)
        self.save_btn.config(state=tk.NORMAL)

        # 保存当前文章
        self.current_article = article
        self.current_keyword = keyword

        # 显示文章
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, article)
        self.output_text.config(state=tk.DISABLED)

        # 更新状态
        word_count = len(article.split())
        self.update_status("生成完成", 'ready')
        self.footer_label.config(text=f"生成完成 | 字数: {word_count} 词 | 主题: {keyword}")

        # 显示成功消息
        show_success("成功", f"文章生成完成！\n\n字数: {word_count} 词", self.root)

    def on_generation_error(self, error_msg: str):
        """生成错误回调"""
        self.is_generating = False
        self.generate_btn.set_loading(False)
        self.update_status("生成失败", 'error')
        self.footer_label.config(text="生成失败")

        show_error("生成失败", f"生成文章时出错:\n\n{error_msg}", self.root)

    def save_article(self):
        """保存文章到文件"""
        if not self.current_article:
            show_error("错误", "没有可保存的文章", self.root)
            return

        # 生成默认文件名
        keyword = getattr(self, 'current_keyword', 'article')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"{safe_filename(keyword)}_{timestamp}.txt"

        # 打开保存对话框
        filepath = filedialog.asksaveasfilename(
            parent=self.root,
            title="保存文章",
            defaultextension=".txt",
            initialfile=default_filename,
            initialdir="output",
            filetypes=[
                ("文本文件", "*.txt"),
                ("所有文件", "*.*")
            ]
        )

        if not filepath:
            return

        try:
            # 确保输出目录存在
            os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else "output", exist_ok=True)

            # 保存文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Topic: {self.current_keyword}\n")
                f.write(f"{'='*60}\n\n")
                f.write(self.current_article)

            self.footer_label.config(text=f"已保存: {os.path.basename(filepath)}")
            show_success("保存成功", f"文章已保存到:\n{filepath}", self.root)

        except Exception as e:
            show_error("保存失败", f"保存文章时出错:\n\n{str(e)}", self.root)

    def clear_output(self):
        """清空输出区域"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

        self.current_article = ""
        self.save_btn.config(state=tk.DISABLED)
        self.footer_label.config(text="已清空")

    def on_closing(self):
        """窗口关闭事件"""
        if self.is_generating:
            from .utils import ask_yes_no
            if not ask_yes_no(
                "确认退出",
                "正在生成文章，确定要退出吗？",
                self.root
            ):
                return

        self.root.destroy()

    def run(self):
        """运行应用程序"""
        self.root.mainloop()


def main():
    """主函数"""
    root = tk.Tk()
    app = ArticleGeneratorApp(root)
    app.run()


if __name__ == '__main__':
    main()

