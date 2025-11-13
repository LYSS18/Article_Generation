"""
文章生成器核心模块
调用AI模型API生成文章
"""

import os
import json
import time
import re
from typing import Dict, List, Optional
from openai import OpenAI
from dotenv import load_dotenv
from .prompts import generate_prompt, generate_subtopic_prompt


class ArticleGenerator:
    """文章生成器类"""

    def __init__(self):
        """初始化生成器，加载配置"""
        # 从 config/.env 文件加载环境变量
        env_path = os.path.join('config', '.env')
        load_dotenv(dotenv_path=env_path)

        self.api_key = os.getenv('API_KEY')
        self.api_base_url = os.getenv('API_BASE_URL', 'https://api.openai.com/v1')
        self.model_name = os.getenv('MODEL_NAME', 'gpt-4o-mini')
        self.article_length = int(os.getenv('ARTICLE_LENGTH', '200'))
        self.temperature = float(os.getenv('TEMPERATURE', '0.7'))
        self.max_tokens = int(os.getenv('MAX_TOKENS', '400'))

        if not self.api_key:
            raise ValueError("API_KEY not found in config/.env file")

        # 初始化OpenAI客户端
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.api_base_url,
            timeout=60.0,  # 设置60秒超时
            max_retries=2  # 最多重试2次
        )

    
    def generate_article(self, keyword: str, description: str = "", is_subtopic: bool = False, 
                        main_keyword: str = "") -> str:
        """
        生成单篇文章
        
        Args:
            keyword: 主题关键词
            description: 主题描述
            is_subtopic: 是否为子主题
            main_keyword: 主主题关键词（仅当is_subtopic=True时使用）
        
        Returns:
            生成的文章内容
        """
        try:
            # 生成提示词
            if is_subtopic and main_keyword:
                prompt = generate_subtopic_prompt(main_keyword, keyword, self.article_length)
            else:
                prompt = generate_prompt(keyword, description, self.article_length)

            print(f"  → Calling API: {self.model_name}")

            # 调用API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )

            article = response.choices[0].message.content.strip()
            return article

        except Exception as e:
            error_msg = f"Error generating article: {type(e).__name__}: {str(e)}"
            print(f"  ❌ {error_msg}")

            # 提供更详细的错误信息
            if "Connection" in str(e) or "timeout" in str(e).lower():
                error_msg += "\n\n可能的原因：\n"
                error_msg += "1. 网络连接问题 - 请检查网络连接\n"
                error_msg += "2. API服务器无法访问 - 可能需要VPN\n"
                error_msg += "3. 防火墙阻止 - 检查防火墙设置\n"
                error_msg += "\n建议：尝试使用国内可访问的API服务（如OpenRouter）"
            elif "API key" in str(e) or "Unauthorized" in str(e):
                error_msg += "\n\nAPI密钥错误，请检查.env文件中的API_KEY是否正确"
            elif "model" in str(e).lower():
                error_msg += f"\n\n模型名称可能不正确，当前使用: {self.model_name}"

            return error_msg
    
    def load_topics(self, config_path: str = "config/topics.json") -> Dict:
        """
        加载主题配置
        
        Args:
            config_path: 配置文件路径
        
        Returns:
            主题配置字典
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def generate_all_articles(self, output_dir: str = "output") -> Dict[str, List[str]]:
        """
        生成所有主题的文章
        
        Args:
            output_dir: 输出目录
        
        Returns:
            生成结果字典
        """
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 加载主题
        topics = self.load_topics()
        results = {}
        
        # 遍历所有组
        for group_key, group_data in topics.items():
            group_name = group_data['name']
            print(f"\n{'='*60}")
            print(f"Processing {group_name}")
            print(f"{'='*60}")
            
            group_results = []
            
            # 遍历该组的所有主题
            for topic in group_data['topics']:
                keyword = topic['keyword']
                description = topic.get('description', '')
                
                print(f"\nGenerating article for: {keyword}")
                article = self.generate_article(keyword, description)
                
                # 保存文章
                filename = f"{group_key}_{keyword.replace('/', '_').replace(' ', '_')}.txt"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Topic: {keyword}\n")
                    f.write(f"{'='*60}\n\n")
                    f.write(article)

                group_results.append(filename)
                print(f"✓ Saved to: {filepath}")
                
                # 处理子主题
                if 'subtopics' in topic:
                    for subtopic in topic['subtopics']:
                        sub_keyword = subtopic['keyword']
                        print(f"  Generating subtopic article for: {sub_keyword}")
                        
                        sub_article = self.generate_article(
                            sub_keyword, 
                            subtopic.get('description', ''),
                            is_subtopic=True,
                            main_keyword=keyword
                        )
                        
                        # 保存子主题文章
                        sub_filename = f"{group_key}_{keyword.replace('/', '_').replace(' ', '_')}_{sub_keyword.replace(' ', '_')}.txt"
                        sub_filepath = os.path.join(output_dir, sub_filename)

                        with open(sub_filepath, 'w', encoding='utf-8') as f:
                            f.write(f"Topic: {sub_keyword}\n")
                            f.write(f"{'='*60}\n\n")
                            f.write(sub_article)

                        group_results.append(sub_filename)
                        print(f"  ✓ Saved to: {sub_filepath}")
                        
                        # 避免API限流
                        time.sleep(1)
                
                # 避免API限流
                time.sleep(1)
            
            results[group_key] = group_results
        
        return results

