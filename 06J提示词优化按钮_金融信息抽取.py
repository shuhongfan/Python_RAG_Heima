from dotenv import load_dotenv
import openai
import json
import re
import os

from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="http://localhost:11434/v1",
)

schema = ['日期', '股票名称', '开盘价', '收盘价', '成交量']

examples_data = [
    {
        "content": "2025-06-16，股市收。股票传智教育A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
        "answers": {
            "股票名称": "传智教育",
            "日期": "2025-06-16",
            "开盘价": 66.0,
            "最高价": 70.0,
            "最低价": 65.0,
            "收盘价": 68.0,
            "成交量": 123000
        }
    },
    {
        "content": "2025-06-06，股市利好。股票黑马程序员A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。",
        "answers": {
            "股票名称": "黑马程序员",
            "日期": "2025-06-06",
            "开盘价": 200.0,
            "最高价": 211.0,
            "最低价": 201.0,
            "收盘价": 206.0,
            "成交量": None  # 原问题未提及成交量，用None表示缺失
        }
    }
]


messages = [
    {"role": "system", "content": f"现在你需要帮助我完成信息抽取任务，当我给你一个句子时，你需要帮我抽取出句子中{schema}信息，并按照JSON的格式输出，上述句子中没有的信息用['原文中未提及']来表示，多个值之间用','分隔。"}
]

for example in examples_data:
    messages.append({'role': 'user', 'content': example["content"]})
    messages.append({'role': 'assistant', 'content': json.dumps(example['answers'],ensure_ascii=False)})

questions = [
    "2023-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。",
    "2023-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。",
]

messages = [
    {'role': 'system', 'content': "现在你需要帮助我完成信息抽取任务，当我给你一个句子时，你需要帮我抽取出句子中实体信息，并按照JSON的格式输出，上述句子中没有的信息用['原文中未提及']来表示，多个值之间用','分隔。"},
]

for question in questions:
    completion = client.chat.completions.create(
        model="qwen2.5:0.5b-instruct",
        messages=messages + [{'role': 'user', 'content': f"按照上述的是咧,现在抽取这个句子的信息:{question}"}]
    )
    print(completion.choices[0].message.content)


