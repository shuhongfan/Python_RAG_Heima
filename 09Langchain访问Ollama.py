from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen2.5:0.5b-instruct")

res = model.invoke(input="你是谁")

print(res)