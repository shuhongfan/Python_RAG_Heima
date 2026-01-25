import os

from openai import OpenAI

# 1. 获取client对象
client = OpenAI(
    base_url="http://localhost:11434/v1",
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen2.5:0.5b-instruct",
    messages=[
        {"role": "system", "content": "你是一个Python编程传家，并且不说废话简单回答"},
        {"role": "assistant", "content": "好的，我是变成专家，并且话不多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，使用pythn代码"},
    ]
)

# 3.处理结果
print(response.choices[0].message.content)