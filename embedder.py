from sentence_transformers import SentenceTransformer
import config
_model = SentenceTransformer(config.EMBED_MODEL)
def encode(texts):
    """encode chunks"""
    if isinstance(texts, str):
        texts = [texts]
    vectors = _model.encode(texts, batch_size=32)
    return vectors.tolist()

def encode_query(text):
    """for user queries"""
    vector = _model.encode(text, prompt_name="query")
    return vector.tolist()
#Test
if __name__ == "__main__":
    vecs = encode(["سلام", "خداحافظ", "مرجوعی"])
    print(len(vecs))
    print( len(vecs[0]))
    print( type(vecs))


    vec = encode_query("چطور محصولم رو مرجوع کنم؟")
    print( type(vec))
    print(len(vec))
