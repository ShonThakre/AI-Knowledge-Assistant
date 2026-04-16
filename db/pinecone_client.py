from pinecone import Pinecone, ServerlessSpec
from config import INDEX_NAME, PINECONE_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
DIMENSION = 768  

def create_index_if_not_exists():
    existing_indexes = [i["name"] for i in pc.list_indexes()]

    if INDEX_NAME not in existing_indexes:
        print(f"[Pinecone] Creating index: {INDEX_NAME}")

        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    else:
        print(f"[Pinecone] Index already exists: {INDEX_NAME}")


create_index_if_not_exists()

index = pc.Index(INDEX_NAME)