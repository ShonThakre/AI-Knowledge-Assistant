from dotenv import load_dotenv
import os
from pinecone import Pinecone

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "developer-quickstart-py"

index = pc.Index(index_name)

# index.upsert_records(
#     namespace="__default__",
#     records=[
#         {
#             "_id": "1",
#             "chunk_text": "This is the first chunk of text."
#         },
#         {
#             "_id": "2",
#             "chunk_text": "This is the second chunk of text."
#         },
#         {
#             "_id": "3",
#             "chunk_text": "This is the third chunk of text."
#         }
#     ]
# )

# response = index.fetch(
#     ids=["1", "2"],
#     namespace="__default__"
# )

# print(response)

results = index.search(
    namespace="__default__",
    query={
        "inputs": {"text": "This is the first chunk of text"},
        "top_k": 3
    }
)

#print(results)

if results and results.result and results.result.hits:
    for hit in results.result.hits:
        print(hit._score)
        print(hit.fields["chunk_text"])
        print("------")
else:
    print("No results found ❌")