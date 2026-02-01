

from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi


prompt = PromptTemplate.from_template("你是一个AI助手")
model = Tongyi(model="qwen3-max")

chain = prompt | model | prompt | model
chain.invoke()
chain.stream()
print(type(chain))
