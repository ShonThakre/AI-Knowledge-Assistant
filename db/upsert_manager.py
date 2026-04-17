import uuid
from generation.embedding import get_embedding
from db.pinecone_client import index

BATCH_SIZE = 50 


def upsert_chunks(chunks, source: str):
    batch = []

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)

        batch.append({
            "id": str(uuid.uuid4()),
            "values": embedding,
            "metadata": {
                "text": chunk,
                "source": source,
                "chunk_id": i
            }
        })

        if len(batch) >= BATCH_SIZE:
            index.upsert(vectors=batch)
            batch = []

    if batch:
        index.upsert(vectors=batch)