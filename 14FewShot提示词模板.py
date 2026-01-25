from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_ollama import OllamaLLM

example_template = PromptTemplate(
    input_variables=["word", "antonym"],
    template="单词：{word},反义词：{antonym}"
)

examples_data = [
    {
        "word": "大",
        "antonym": "小"
    },
    {
        "word": "上",
        "antonym": "下"
    }
]

few_shot_template = FewShotPromptTemplate(
    # 示例数据的模板
    example_prompt=example_template,

    # 示例的数据（用来注入动态数据的），list内套字典
    examples=examples_data,

    # 示例之前的提示词
    prefix="告知我单词的反义词，我提供如下的示例",

    # 示例之后的提示词
    suffix="基于前面的示例告知我，{input_word}的反义词是？",

    # 声明再前缀或后缀中需要注入的变量名
    input_variables=['input_word']
)

prompt_text = few_shot_template.invoke(input={"input_word":"左"}).to_string()
print(prompt_text)


model = OllamaLLM(model="qwen2.5:0.5b-instruct")
print(model.invoke(input=prompt_text))