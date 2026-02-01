from abc import ABC,abstractmethod
from typing import Optional
from langchain_ollama import ChatOllama

from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel

from utils.config_handler import rag_conf


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self)->Optional[Embeddings|BaseChatModel]:
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self) ->Optional[Embeddings|BaseChatModel]:
        return ChatOllama(model=rag_conf["chat_model_name"])

class EmbeddingsModelFactory(BaseModelFactory):
    def generator(self) ->Optional[Embeddings|BaseChatModel]:
        return ChatOllama(model=rag_conf["embedding_model_name"])

chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsModelFactory().generator()