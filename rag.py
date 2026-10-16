import time
from embedder import encode_query
from vectordb import search
from llm import generate, SYSTEM_PROMPT, RAG_TEMPLATE, NO_CONTEXT_RESPONSE

def query(question):
    """Answer a question using RAG."""
    start = time.perf_counter()
    
    # Embed the question
    query_vector = encode_query(question)
    
    # Search in Qdrant
    docs = search(query_vector)
    
    # If nothing found
    if not docs:
        return {
            "answer": NO_CONTEXT_RESPONSE,
            "sources": [],
            "latency": round(time.perf_counter() - start, 2)
        }
    
    # Build context
    context = "\n\n".join(d["text"] for d in docs)
    
    # Build prompt
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": RAG_TEMPLATE.format(context=context, query=question)}
    ]
    
    # Generate answer
    answer = generate(messages)
    
    return {
        "answer": answer,
        "sources": docs,
        "latency": round(time.perf_counter() - start, 2)
    }


#Test
if __name__ == "__main__":
    q = input("سوال: ")
    result = query(q)
    print("\nپاسخ:", result["answer"])
    print("\nمنابع:")
    for doc in result["sources"]:
        print(f"  - {doc['source']} (score: {doc['score']:.3f})")
    print(f"\n زمان: {result['latency']} ثانیه")
    