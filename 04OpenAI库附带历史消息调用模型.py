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
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物？"},
    ],
    stream=True
)

# 3.处理结果
for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ",  # 每一行之间以空格分隔
          flush=True   #立刻刷新缓冲区
          )