from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


str_parser  = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatOllama(model="qwen2.5:0.5b-instruct")

first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname},刚生了{gender}，请帮忙起名字。\n"
    "必须严格按照JSON格式返回：{{\"name\": \"姓名\"}}\n"
    "不要返回任何其他内容，只要JSON格式的数据。"
)


second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)

# 构建链
chain = first_prompt|model|json_parser|second_prompt|model|str_parser

for chunk in chain.invoke({"lastname": "张", "gender": "女儿"}):
    print(chunk,end="",flush=True)