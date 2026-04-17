from db.pinecone_client import index
from generation.embedding import get_embedding


def retrieve_chunks(query, k=10, source=None):
    query_embedding = get_embedding(query)

    query_params = {
        "vector": query_embedding,
        "top_k": k,
        "include_metadata": True
    }

    if source:
        query_params["filter"] = {"source": source}

    results = index.query(**query_params)

    matches = results["matches"]

    # 🔥 return full metadata
    return [
        {
            "text": m["metadata"]["text"],
            "source": m["metadata"]["source"]
        }
        for m in matches
    ]