from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(model="qwen2.5:0.5b-instruct")

print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你",'我稀饭你','晚上吃啥']))