from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./data/stus.json",
    jq_schema=".[].name",
    text_content=False
)

document  = loader.load()
print(document)