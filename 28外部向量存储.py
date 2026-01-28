from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

embeddings = OllamaEmbeddings(model="qwen2.5:0.5b-instruct")

vector_store = Chroma(
    # 当前向量存储起名字，类似于数据库的名词
    collection_name="test",

    # 嵌入模型
    embedding_function=embeddings,

    # 指定数据库存放的文件夹
    persist_directory="./chroma_db"
)

# vector_store = InMemoryVectorStore(
#     # embedding=DashScopeEmbeddings()
#     embedding=embeddings
# )


loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source"
)

documents=loader.load()

# 向量存储的新增、删除、检索
vector_store.add_documents(
    documents=documents,
    ids=["id"+str(i) for i in range(1,len(documents)+1)]
)

# 删除 传入id
vector_store.delete(["id1","id2"])

# 检索
res=vector_store.similarity_search(
    "Python是不是简单易学呀",
    # 检索的结果要几个
    3,
    filter={"score":"黑马程序员"}
)
print(res)