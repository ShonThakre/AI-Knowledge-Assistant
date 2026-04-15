from pinecone import Pinecone 
from config import INDEX_NAME, PINECONE_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)