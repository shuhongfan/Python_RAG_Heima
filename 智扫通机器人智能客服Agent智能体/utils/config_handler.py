import yaml
from yaml import Loader
from utils.path_tool import get_abs_path


def load_rag_config(config_path=get_abs_path("config/rag.yml"),encoding="utf-8"):
    with open(config_path, 'r',encoding=encoding) as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
    return config

def load_chroma_config(config_path=get_abs_path("config/chroma.yml"),encoding="utf-8"):
    with open(config_path, 'r',encoding=encoding) as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
    return config

def load_prompts_config(config_path=get_abs_path("config/prompts.yml"),encoding="utf-8"):
    with open(config_path, 'r',encoding=encoding) as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
    return config

def load_agent_config(config_path=get_abs_path("config/agent.yml"),encoding="utf-8"):
    with open(config_path, 'r',encoding=encoding) as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
    return config

rag_conf = load_rag_config()
chroma_conf = load_chroma_config()
prompts_conf = load_prompts_config()
agent_conf = load_agent_config()


if __name__ == '__main__':
    print(rag_conf["chat_model_name"])