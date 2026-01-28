from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatOllama(model="qwen2.5:0.5b-instruct")
# prompt = PromptTemplate.from_template("你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问:{input}，请回答")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应用户问题.对话历史:"),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题:{input}")
    ]
)

str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt


base_chain = prompt|print_prompt | model | str_parser

store = {}
# 通过会话ID获取InMemoryChatMessageHistory类对象
def get_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 创建一个新的链，对原有链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    # 被增强的原有chain
    base_chain,

    # 通过会话ID获取InMemoryChatMessageHistory类对象
    get_history,

    # 表示用户输入在模板中的占位符
    input_messages_key="input",

    # 表示用户输入在模板中的占位符
    history_messages_key="chat_history"
)


if __name__ == '__main__':
    session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }
    res = conversation_chain.invoke({"input":"小米有2个猫"},session_config)
    print("第一次执行:",res)

    res = conversation_chain.invoke({"input": "小强有5个猫"}, session_config)
    print("第二次执行:", res)

    res = conversation_chain.invoke({"input": "总共有几个宠物"}, session_config)
    print("第三次执行:", res)