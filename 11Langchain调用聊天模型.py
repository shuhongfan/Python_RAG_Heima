from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from pyexpat.errors import messages

model = ChatOllama(model="qwen2.5:0.5b-instruct")

messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    HumanMessage(content="按照上一个回复的格式，写一首唐诗。"),
]

res = model.stream(messages)

for chunk in res:
    print(chunk.content,end="",flush=True)
