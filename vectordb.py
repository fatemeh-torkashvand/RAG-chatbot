# Libraries
import hashlib
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import config

# Connect to Qdrant vector Database,create the collection
# Store vectors and search the collection by vector similarity



def get_client():
    """ create a Qdrant client """
    try:
        client = QdrantClient(
            url=config.QDRANT_URL,
            api_key=config.QDRANT_API_KEY or None
        )
        client.get_collections()  #connection test
        return client
    except Exception as e:
        raise RuntimeError(
            f"connection failed"
            f"URL: {config.QDRANT_URL}\n"
            f"error: {e}"
        )


_client = get_client()



def create_collection():
    """create the collection in Qdrant if collection doesn't exist"""
    if not _client.collection_exists(config.COLLECTION_NAME):
        _client.create_collection(
            collection_name=config.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=config.EMBED_DIM,
                distance=Distance.COSINE
            )
        )
        print(f"---Collection '{config.COLLECTION_NAME}'created")
    else:
        print(f"---Collection '{config.COLLECTION_NAME}' exists")


 
def chunk_text(text, size=None, overlap=None):
    """
    split text to small chunks
    """
    size = size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    
    return chunks


# create ID 
def make_id(source, chunk_id):
    raw = f"{source}::{chunk_id}"
    return hashlib.md5(raw.encode()).hexdigest()


def upsert(chunks, vectors, source):
    #store chunks and their vectors in qdrant
    points = []
    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
        points.append(
            PointStruct(
                id=make_id(source, i),
                vector=vector,
                payload={
                    "text": chunk,
                    "source": source,
                    "chunk_id": i
                }
            )
        )
    
    _client.upsert(
        collection_name=config.COLLECTION_NAME,
        points=points
    )
    print(f"---{len(points)} chunk from«{source}» stored.")

def search(vector, top_k=None):
    #return the nearest chunks to the given vector 
    top_k = top_k or config.TOP_K
    
    results = _client.query_points(
        collection_name=config.COLLECTION_NAME,
        query=vector,
        limit=top_k
    )
    
    docs = []
    for point in results.points:
        if point.score >= config.SCORE_THRESHOLD:
            docs.append({
                "text": point.payload["text"],
                "source": point.payload["source"],
                "score": point.score
            })
    
    return docs

### Test
if __name__ == "__main__":
    create_collection()

    text = "This is a test text. " * 30
    chunks = chunk_text(text)
    print(f"Chunks: {len(chunks)}")
    print(f"First chunk length: {len(chunks[0])}")

    id1 = make_id("test.txt", 0)
    id2 = make_id("test.txt", 0)
    id3 = make_id("test.txt", 1)
    print(f"id1 == id2: {id1 == id2}")
    print(f"id1 == id3: {id1 == id3}")