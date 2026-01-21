# -*- coding: utf-8 -*-
"""
LMDeploy API 调用脚本
使用 OpenAI 兼容接口调用本地模型
"""

import httpx
from openai import OpenAI

# 创建客户端，连接本地服务，增加超时时间
client = OpenAI(
    api_key="not-needed",
    base_url="http://localhost:23333/v1",
    timeout=httpx.Timeout(60.0, connect=10.0)  # 60秒超时
)


def test_connection():
    """测试服务连接"""
    import requests
    try:
        resp = requests.get("http://localhost:23333/v1/models", timeout=5)
        print(f"✓ 服务连接正常，状态码: {resp.status_code}")
        print(f"  模型列表: {resp.json()}")
        return True
    except requests.exceptions.ConnectionError:
        print("✗ 无法连接到服务，请确保已启动 API 服务")
        print("  启动命令: $env:TORCH_COMPILE_DISABLE='1'; lmdeploy serve api_server F:\\my_model --backend pytorch --eager-mode --server-port 23333")
        return False
    except Exception as e:
        print(f"✗ 连接错误: {e}")
        return False


def chat(message: str, history: list = None) -> str:
    """发送消息并获取回复"""
    messages = history or []
    messages.append({"role": "user", "content": message})
    
    try:
        response = client.chat.completions.create(
            model="F:\\my_model",
            messages=messages,
            temperature=0.7,
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[错误] {e}"


def chat_stream(message: str, history: list = None):
    """流式输出模式"""
    messages = history or []
    messages.append({"role": "user", "content": message})
    
    try:
        response = client.chat.completions.create(
            model="F:\\my_model",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            stream=True
        )
        
        for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print()
    except Exception as e:
        print(f"[错误] {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("LMDeploy API 测试")
    print("=" * 50)
    
    # 先测试连接
    if not test_connection():
        exit(1)
    
    # 简单测试
    question = "你好，请用一句话介绍你自己"
    print(f"\n问题: {question}")
    print(f"回答: ", end="", flush=True)
    
    # 使用流式输出
    chat_stream(question)
    
    print("\n" + "=" * 50)
    print("交互模式 (输入 'quit' 退出)")
    print("=" * 50)
    
    history = []
    while True:
        try:
            user_input = input("\n你: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
            
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        if not user_input:
            continue
        
        print("AI: ", end="", flush=True)
        reply = chat(user_input, history.copy())
        print(reply)
        
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})
