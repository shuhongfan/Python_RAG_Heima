import os

from datetime import datetime
from langchain_chroma import Chroma

import config_data as config
import hashlib
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 检查传入的md5字符串是否以及被处理过了
def check_md5(md5_str: str):
    if not os.path.exists(config.md5_path):
        open(config.md5_path, "w",encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path,'r',encoding="utf-8").readline():
            line=line.strip()
            if line==md5_str:
                return True
        return False


# 将传入的md5字符串，记录到文件内保存
def save_md5(m5d_str: str,encoding="utf-8"):
    with open(config.md5_path, "a",encoding="utf-8") as f:
        f.write(m5d_str+"\n")
    pass


# 将传入的字符串转换为md5字符串
def get_string_md5(input_str: str,encoding="utf-8"):
    # 将字符串转换为bytes字节数组
    str_bytes=input_str.encode(encoding)

    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()

    return md5_hex

class KnowledgeBaseService(object):
    def __init__(self):
        # 如果文件夹不存在则创建，如果存在则跳过
        os.makedirs(config.persist_directory,exist_ok=True)

        # 向量存储的示例Chroma向量库对象
        self.chroma=Chroma(
            collection_name=config.collection_name,
            embedding_function= OllamaEmbeddings(model="qwen2.5:0.5b-instruct"),
            persist_directory=config.persist_directory
        )
        # 文本分割器的对象
        self.spliter=RecursiveCharacterTextSplitter(
            # 分割后的文本段最大长度
            chunk_size=config.chunk_size,

            # 连续文本段之间的字符重叠数量
            chunk_overlap=config.chunk_overlap,

            # 自然段落划分的符号
            separators =config.separators,

            # 使用python自带的len函数做长度统计
            length_function= len
        )

    def upload_by_str(self,data,filename):
        md5_hex = get_string_md5(data)
        if check_md5(md5_hex):
            return "[跳过]内容已经存在知识库中"

        if len(data)>config.max_split_char_number:
            knowledge_chunks: list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "小曹"
        }

        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks],
        )

        save_md5(md5_hex)

        return "[成功]内容已经成功载入向量库"

if __name__ == '__main__':
    service = KnowledgeBaseService()
    service.upload_by_str("周杰伦","testfile")