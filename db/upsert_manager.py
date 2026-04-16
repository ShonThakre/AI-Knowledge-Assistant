from db.pinecone_client import index
import uuid

from generation.embedding import get_embedding


def upsert_chunks(chunks, source: str):
    vectors = []

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)

        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embedding,
            "metadata": {
                "text": chunk,
                "source": source,
                "chunk_id": i
            }
        })

    index.upsert(vectors=vectors)