from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen2.5:0.5b-instruct")

res  = model.stream(input="你是谁")

for chunk in res:
    print(chunk,end="",flush=True)