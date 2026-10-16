# Embedding 
EMBED_MODEL = "Snowflake/snowflake-arctic-embed-l-v2.0"
EMBED_DIM = 1024

#  Qdrant 
QDRANT_URL = "http://localhost:6333"
QDRANT_API_KEY = ""
COLLECTION_NAME = "shop_faq"

#  Chunking 
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50

# Retrieval 
TOP_K = 5
SCORE_THRESHOLD = 0.35



# LLM GapGPT
OPENAI_API_KEY = "" 
OPENAI_MODEL = "gpt-4o-mini"
OPENAI_BASE_URL = "https://api.gapgpt.app/v1"
MAX_NEW_TOKENS = 500
TEMPERATURE = 0.0