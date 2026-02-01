from langchain_ollama import OllamaEmbeddings


model = OllamaEmbeddings(model="qwen3-embedding:4b")

# 不用invoke stream
# embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
