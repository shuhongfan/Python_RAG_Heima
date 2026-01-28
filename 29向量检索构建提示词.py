from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama,OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="qwen2.5:0.5b-instruct")

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','以我提供的已知参考资料为主，简介和专业的回答用户问题，参考资料：{context}'),
        ('user','用户提问:{input}'),
    ]
)

embeddings = OllamaEmbeddings(model="qwen2.5:0.5b-instruct")
vector_store = InMemoryVectorStore(embeddings)


vector_store.add_texts(["减肥就是要少吃多练","在减脂期间吃东西很重要，清单少油控制卡路里摄入并运动起来","跑步是很好的运动喔"])

input_text="怎样减肥"


result = resource=vector_store.similarity_search(input_text,2)
reference_text="["

for doc in result:
    reference_text+=doc.page_content
reference_text+="]"

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

chain = prompt | print_prompt|model|StrOutputParser()

res =chain.invoke({"input":input_text,"context":reference_text})
print(res)