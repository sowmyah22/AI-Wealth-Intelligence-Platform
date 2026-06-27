from app.rag.embedding_service import generate_embedding
from app.rag.chroma_service import collection


def retrieve_similar_context(query: str, top_k=3):
    query_embedding = generate_embedding(query)

    results=collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]
