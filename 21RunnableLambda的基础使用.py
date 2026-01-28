from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda

model = ChatOllama(model="qwen2.5:0.5b-instruct")
str_parser = StrOutputParser()

first_prompt = PromptTemplate.from_template("我邻居姓：{lastname},刚生了{gender}，请帮忙起名字，仅告知我名字，不要额外信息")

second_prompt = PromptTemplate.from_template("姓名{name}，请帮我解析含义")

my_func = RunnableLambda(lambda ai_msg:{"name": ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"lastname":"张","gender":"女孩"}):
    print(chunk,end="",flush=True)

