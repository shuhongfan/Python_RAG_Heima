from nltk.metrics.aline import similarity_matrix

md5_path = "./md5.text"

collection_name="rag"
persist_directory="./chroma_db"
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n","\n",".","?","!","。","！","？"," ",""]

# 文本分隔的阈值
max_split_char_number = 1000

# 检索返回匹配的文档数量
similarity_threshold = 1

embedding_mode_name="qwen2.5:0.5b-instruct"
chat_model_name="qwen2.5:0.5b-instruct"

session_config= {"configurable":{"session_id":"user_001"}}