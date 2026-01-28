from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./data/pdf1.pdf",

    # single模式，不管有多少页，只返回1个Document文档
    # 默认Page模式，每一个页面生成一个Document文档
    mode="single",
)

i=0
for doc in loader.lazy_load():
    i+=1
    print(doc)
    print("="*20,i)
