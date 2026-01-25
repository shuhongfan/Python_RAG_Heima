from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import ChatOllama


chat_Prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system','你是一个边塞诗人，可以作诗',),
        MessagesPlaceholder('history'),
        ('human','请再来一首唐诗',)
    ]
)


history_data=[
    ('human','你来写一首唐诗'),
    ('ai','锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦'),
    ('human','请继续写一首唐诗'),
    ('ai','行行高歌，歌歌高行，行行高歌，歌歌高行'),
]

model = ChatOllama(model="qwen2.5:0.5b-instruct")

# 组成链，要求每一个组件都是Runnable的子类
chain = chat_Prompt_template | model

res = chain.invoke({"history":history_data})
print(res.content)

for chunk in chain.stream({"history": history_data}):
    print(chunk.content,end="",flush=True)