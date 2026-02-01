from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.runtime import Runtime


@tool(description="查询天气,传入城市名称字符串，返回字符串天气信息")
def get_weather(city:str)->str:
    return f'{city}天气晴天'

@before_agent
def log_before_agent(state:AgentState,runtime:Runtime):
    print(f'[before_agent] agent启动，并附带 {len(state["messages"])}消息')

@after_agent
def log_after_agent(state:AgentState,runtime:Runtime):
    print(f'[after_agent] agent结束，并附带 {len(state["messages"])}消息')


@before_model
def log_before_model(state: AgentState, runtime: Runtime):
    print(f'[before_model] model启动，并附带 {len(state["messages"])}消息')


@after_model
def log_after_model(state: AgentState, runtime: Runtime):
    print(f'[after_model] model结束，并附带 {len(state["messages"])}消息')

@wrap_model_call
def log_wrap_model_call(request, handler):
    print("模型调用")
    return handler(request)


@wrap_tool_call
def log_wrap_tool_call(request, handler):
    print(f'工具执行：{request.tool_call["name"]}')
    print(f'工具执行传入参数：{request.tool_call["args"]}')
    return handler(request)

agent = create_agent(
    model=ChatOllama(model="qwen2.5:0.5b-instruct"),
    tools=[get_weather],
    system_prompt="你是一个聊天助手，可以回答用户问题",
    middleware=[log_before_agent,log_after_agent,log_before_model,log_after_model,log_wrap_model_call,log_wrap_tool_call]
)

res = agent.invoke({"messages":[{"role":"user","content":"深圳天气如何"}]})
print(res)