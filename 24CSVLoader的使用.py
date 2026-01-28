from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        # 指定分隔符
        "delimiter": ",",

        # 指定带有分隔符文本的引号包围的是单引号还是双引号
        "quotechar": '"',
        # 列名
        "fieldnames": ['name', 'age', 'gender', 'hobby'],
        "doublequote": True,
        "skipinitialspace": True,
        "lineterminator": "\n",
        "quoting": 0,
    },
    encoding="utf-8",
)


documents = loader.load()

# print(documents)

# 批量加载
# for document in documents:
#     print(type(document),document)

# 懒加载
for document in loader.lazy_load():
    print(type(document), document)