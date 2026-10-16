from vectordb import create_collection, chunk_text, upsert
from embedder import encode
from rag import query


def load_file(filepath, source_name):
    """Load a text file and store it in Qdrant."""
    
    # 1. Read file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"text length: {len(text)} characters")
    
    # 2. Chunk
    chunks = chunk_text(text)
    print(f"chunks number: {len(chunks)}")
    
    # 3. Encode
    print("vectorizing..")
    vectors = encode(chunks)
    print(f"vectors number: {len(vectors)}")
    
    # 4. Store
    upsert(chunks, vectors, source=source_name)
    print(f" «{source_name}» saved")


def main():
    create_collection()
    load_file("faq.txt", "faq.txt")


if __name__ == "__main__":
    main()
    

    result = query("ساعت کاری فروشگاه چنده؟")
    print("پاسخ:", result["answer"])
    print()

    result = query("چند روز طول می‌کشه تا سفارشم برسه؟")
    print("پاسخ:", result["answer"])
    print()

    result = query("چطور محصولم رو مرجوع کنم؟")
    print("پاسخ:", result["answer"])