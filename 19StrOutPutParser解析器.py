from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import AIMessage

parser = StrOutputParser()
model = ChatOllama(model="qwen2.5:0.5b-instruct")
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname},刚生了{gender}，请起名，仅告诉我姓名无需其它内容"
)

chain = prompt | model | parser | model | parser
res = chain.invoke(input={"lastname": '张', "gender": "女儿"})
print(res)
