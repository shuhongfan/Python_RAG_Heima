from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "我的邻居姓：{lastname},刚生了{gender},你帮我起个名字，简单回答"
)

prompt_text = prompt_template.format_prompt(lastname='张',gender="女儿")

model = OllamaLLM(model="qwen2.5:0.5b-instruct")

# res = model.invoke(input=prompt_text)
# print(res)

chain =prompt_template | model
res = chain.invoke(input={"lastname":'张',"gender":"女儿"})
print(res)