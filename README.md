# Floriashop Chatbot

A retrieval-augmented chatbot for Floriashop's customer support. It answers questions about orders,
shipping, returns, payment, and store policies by searching a FAQ knowledge base and passing the relevant chunks to an LLM.

Everything runs locally except the LLM call, which goes through GapGPT's OpenAI-compatible endpoint.

## How it works

1. The FAQ file is split into overlapping chunks.
2. Each chunk is embedded with `Snowflake/snowflake-arctic-embed-l-v2.0`.
3. Vectors are stored in a Qdrant collection.
4. At query time, the question is embedded, the closest chunks are retrieved, and they are sent to `gpt-4o-mini` as context.
5. If nothing passes the similarity threshold, the bot replies with a fixed fallback message instead of guessing.

## Project layout



.
├── streamlit.py     # Streamlit UI
├── rag.py           # Retrieval and generation pipeline
├── vectordb.py      # Qdrant client, chunking, upsert, search
├── embedder.py      # Sentence-transformer wrapper
├── llm.py           # LLM client and prompts
├── config.py        # Settings
├── load_data.py     # Loads faq.txt into Qdrant
└── faq.txt          # Knowledge base



## Requirements

- Python 3.10+
- A running Qdrant instance (local or cloud)
- An API key for GapGPT, or any OpenAI-compatible endpoint


bash
pip install -r requirements.txt


Setup

Fill in your keys in config.py:

· OPENAI_API_KEY — API key for the LLM provider
· QDRANT_URL — Qdrant endpoint (defaults to http://localhost:6333)
· QDRANT_API_KEY — only needed for Qdrant Cloud

Running it

Start Qdrant:


bash
docker run -p 6333:6333 qdrant/qdrant


Load the FAQ into the vector database:


bash
python load_data.py


Launch the UI:


bash
streamlit run streamlit.py
اً
