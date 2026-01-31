from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import win32ui
import config_data as config


class VectorStoreService(object):
    def __init__(self,embeddings):
        self.embedding = embeddings
        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory
        )

    # 返回向量检索其，方便加入chain
    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshold})


if __name__ == '__main__':
    retriever = VectorStoreService(OllamaEmbeddings(model="qwen2.5:0.5b-instruct")).get_retriever()
    res = retriever.invoke("我的体重180斤，尺码推荐")
    print(res)