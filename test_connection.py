"""
API连接测试脚本
用于诊断API连接问题
"""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

def test_connection():
    """测试API连接"""
    print("="*60)
    print("API连接测试")
    print("="*60)
    
    # 从 config/.env 文件加载环境变量
    env_path = os.path.join('config', '.env')
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv('API_KEY')
    api_base_url = os.getenv('API_BASE_URL', 'https://api.openai.com/v1')
    model_name = os.getenv('MODEL_NAME', 'gpt-4o-mini')

    print(f"\n配置信息：")
    print(f"  API Base URL: {api_base_url}")
    print(f"  Model Name: {model_name}")
    print(f"  API Key: {api_key[:20]}...{api_key[-10:] if api_key else 'NOT FOUND'}")

    if not api_key:
        print("\n❌ 错误：未找到API_KEY")
        print("请检查 config/.env 文件是否存在并包含 API_KEY")
        print("请检查.env文件是否存在且包含API_KEY")
        return False
    
    print("\n正在测试连接...")
    
    try:
        # 初始化客户端
        client = OpenAI(
            api_key=api_key,
            base_url=api_base_url,
            timeout=30.0
        )
        
        # 发送测试请求
        print("  → 发送测试请求...")
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": "Say 'Hello, API connection successful!' in one sentence."}
            ],
            max_tokens=50
        )
        
        result = response.choices[0].message.content.strip()
        
        print("\n✅ 连接成功！")
        print(f"  API响应: {result}")
        print(f"  使用的模型: {response.model}")
        print(f"  消耗tokens: {response.usage.total_tokens}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 连接失败！")
        print(f"  错误类型: {type(e).__name__}")
        print(f"  错误信息: {str(e)}")
        
        # 提供诊断建议
        print("\n诊断建议：")
        
        if "Connection" in str(e) or "timeout" in str(e).lower():
            print("  ⚠️  网络连接问题")
            print("     1. 检查网络连接是否正常")
            print("     2. OpenAI API在中国大陆可能需要VPN")
            print("     3. 建议使用国内可访问的API服务（如OpenRouter）")
            print("\n  解决方案：")
            print("     编辑.env文件，改用OpenRouter：")
            print("     API_BASE_URL=https://openrouter.ai/api/v1")
            print("     MODEL_NAME=openai/gpt-4o-mini")
            print("     API_KEY=你的OpenRouter密钥")
            
        elif "API key" in str(e) or "Unauthorized" in str(e) or "401" in str(e):
            print("  ⚠️  API密钥问题")
            print("     1. 检查API_KEY是否正确")
            print("     2. 确认密钥未过期")
            print("     3. 确认账户有足够余额")
            
        elif "model" in str(e).lower() or "404" in str(e):
            print("  ⚠️  模型名称问题")
            print(f"     当前模型: {model_name}")
            print("     1. 检查模型名称是否正确")
            print("     2. 确认账户有权限使用该模型")
            
        else:
            print("  ⚠️  未知错误")
            print("     请检查错误信息并搜索解决方案")
        
        return False

if __name__ == "__main__":
    success = test_connection()
    
    if success:
        print("\n" + "="*60)
        print("✅ 测试通过！可以开始使用文章生成器了")
        print("   运行: python main.py")
        print("="*60)
        sys.exit(0)
    else:
        print("\n" + "="*60)
        print("❌ 测试失败！请根据上述建议修复问题后重试")
        print("   重新测试: python test_connection.py")
        print("="*60)
        sys.exit(1)

