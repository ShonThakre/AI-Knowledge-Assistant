from db.pinecone_client import index
from generation.embedding import get_embedding


def retrieve_chunks(query: str, k: int = 3):
    query_embedding = get_embedding(query)

    results = index.query(
        vector=query_embedding,
        top_k=k,
        include_metadata=True
    )

    chunks = [
        match["metadata"]["text"]
        for match in results["matches"]
    ]

    return chunks