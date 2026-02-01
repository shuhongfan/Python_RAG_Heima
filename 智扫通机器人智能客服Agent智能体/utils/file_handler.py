import os
import hashlib

from langchain_community.document_loaders import PyPDFLoader, TextLoader

from utils.logger_handler import logger


# 获取文件的md5的十六进制字符串
def get_file_md5_hex(filePath):
    if not os.path.exists(filePath):
        logger.error(f'[md5计算]文件{filePath}不存在')
        return

    if not os.path.isfile(filePath):
        logger.error(f'[md5计算]路径{filePath}不是文件')
        return

    md5_obj = hashlib.md5()

    chunk_size = 4096

    try:
        with open(filePath, 'rb') as f:
            while chunk:=f.read(chunk_size):
                md5_obj.update(chunk)
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f'[md5计算]文件{filePath}读取失败，错误信息：{str(e)}')


    # 返回文件夹内的文件列表
def listdir_with_allowed_type(filePath,allowed_type):
    files = []

    if not os.path.isdir(filePath):
        logger.error(f'[listdir_with_allowed_type]{filePath}不是文件夹')
        return allowed_type

    for f in os.listdir(filePath):
        if f.endswith(allowed_type):
            files.append(os.path.join(filePath,f))
    return tuple(files)



def paf_loader(file_path,password=None):
    return PyPDFLoader(file_path,password).load()

def txt_loader(file_path):
    return TextLoader(file_path,encoding="utf-8").load()