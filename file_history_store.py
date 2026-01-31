import  os,json
from typing import Sequence
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory



class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path

        # 完整文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)

        # 确保文件夹存在
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # sequence序列，类似list、tuple

        # 已有的消息列表
        all_messages = list(self.messages)

        # 新的和已有的融合成一个list
        all_messages.extend(messages)

        # 将数据同步写入到本地文件中
        new_messages = []
        for message in all_messages:
            d = message_to_dict(message)
            new_messages.append(d)

        new_messages = [message_to_dict( message) for message in all_messages]

        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)

    # property装饰器将messages方法变成成员属性使用
    @property
    def messages(self)->list[BaseMessage]:
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                message_data = json.load(f)
                return messages_from_dict(message_data)
        except FileNotFoundError:
            return  []

    def clear(self)->None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)

def get_history(session_id: str):
    return FileChatMessageHistory(session_id,"./chat_history")

