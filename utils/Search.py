from db.pinecone_client import index

def search(query,top_k):
    results = index.search(
        namespace="__default__",
        query={
            "inputs": {"text": query},
            "top_k": top_k
        }
    )

    if results and results.result and results.result.hits:
        return results.result.hits
    else:
        return None