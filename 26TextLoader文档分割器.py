from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./data/Python基础语法.txt",encoding="utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    # 分段的最大字符数
    chunk_size=500,

    # 分段之间允许重叠的字符数
    chunk_overlap=50,

    # 文本自然段落分隔的依据分号
    separators=["\n\n","\n","。","！","？",".","?"," ",""],

    # 获取文本长度的函数
    length_function=len
)

split_docs = splitter.split_documents(docs)

print(len(split_docs))

for doc in split_docs:
    print("="*20)
    print(doc)
    print("="*20)

