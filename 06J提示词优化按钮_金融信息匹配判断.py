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

examples_data = {
    '是': [
        ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
    ],
    '不是': [
        ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
        ('央行降息，刺激经济增长。', '新能源技术的创新。')
    ]
}

messages = [
    {"role": "system", "content": f"判断2个句子语义是否相似，相似句子返回是，不相似句子返回不是，不要其他回答"}
]

for key, value in examples_data.items():
    for t in value:
        messages.append({'role': 'user', 'content': f"句子1:[{t[0]}], 句子2:[{t[1]}]"})
        messages.append({'role': 'assistant', 'content': key})


questions = [
    ("利率上传,影响房地产市场.","高利率对房地产有一定的冲击"),
    ("油价大幅下跌,能源公司面临挑战.","维持智能城市的建设趋势越加明显"),
    ("股票市场今日大涨,投资者乐观.","持续上涨的市场让投资者感到满意"),

]

messages = [
    {'role': 'system',
     'content': "判断2个句子语义是否相似，相似句子返回是，不相似句子返回不是，不要其他回答"},
]

for question in questions:
    completion = client.chat.completions.create(
        model="qwen2.5:0.5b-instruct",
        messages=messages + [{'role': 'user', 'content': f"按照上述的是咧,现在抽取这个句子的信息:{question}"}]
    )
    print(completion.choices[0].message.content)
