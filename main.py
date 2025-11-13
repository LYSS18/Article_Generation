"""
英文文章生成器 - 主程序入口
Author: Article Generator
Description: 基于AI模型生成跨文化交流主题的英文文章
"""

import os
import sys
from src.generator import ArticleGenerator


def print_banner():
    """打印程序横幅"""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║         英文文章生成器 - Article Generator              ║
    ║              Cross-Cultural Communication                ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_env_file():
    """检查config/.env文件是否存在"""
    env_path = os.path.join('config', '.env')
    if not os.path.exists(env_path):
        print("⚠️  Warning: config/.env file not found!")
        print("Please create a config/.env file based on config/.env.example")
        print("\nSteps:")
        print("1. Copy config/.env.example to config/.env")
        print("2. Edit config/.env and add your API key")
        print("3. Run this program again")
        return False
    return True


def main():
    """主函数"""
    print_banner()
    
    # 检查环境配置
    if not check_env_file():
        sys.exit(1)
    
    try:
        # 初始化生成器
        print("🔧 Initializing Article Generator...")
        generator = ArticleGenerator()
        print(f"✓ Using model: {generator.model_name}")
        print(f"✓ Target article length: {generator.article_length} words")
        
        # 显示菜单
        print("\n" + "="*60)
        print("Please select an option:")
        print("="*60)
        print("1. Generate an article by keyword")
        print("0. Exit")
        print("="*60)

        choice = input("\nEnter your choice (0-1): ").strip()

        # 转换全角数字为半角数字
        full_to_half = str.maketrans('０１', '01')
        choice = choice.translate(full_to_half)

        if choice == '0':
            print("👋 Goodbye!")
            sys.exit(0)

        elif choice == '1':
            keyword = input("\nEnter the keyword/topic: ").strip()
            if keyword:
                print(f"\n🚀 Generating CET-6 level article for: {keyword}")
                article = generator.generate_article(keyword, f"An essay about {keyword}")

                os.makedirs("output", exist_ok=True)
                filename = f"{keyword.replace('/', '_').replace(' ', '_')}.txt"
                filepath = os.path.join("output", filename)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Topic: {keyword}\n")
                    f.write(f"{'='*60}\n\n")
                    f.write(article)

                print(f"✓ Article saved to: {filepath}")
            else:
                print("❌ No keyword provided!")

        else:
            print("❌ Invalid choice!")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

