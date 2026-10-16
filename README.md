markdown
# Floriashop Chatbot

A retrieval-augmented chatbot for Floriashop's customer support. It answers questions about orders,
shipping, returns, payment, and store policies by searching a FAQ knowledge base and passing the relevant chunks to an LLM.

Everything runs locally except the LLM call, which goes through GapGPT's OpenAI-compatible endpoint.
