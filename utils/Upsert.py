
from db.pinecone_client import index 
import time

def upsert_data(records):
    if not records:
        print("No records to upsert")
        return
    
    index.upsert_records(
        namespace="__default__",
        records=records
    )

def create_record(chunks, source="doc"):
    records = []
    timestamp = int(time.time())

    for i, chunk in enumerate(chunks):
        record = {
            "_id": f"{source}_{timestamp}_{i}",
            "chunk_text": chunk
        }
        records.append(record)
        upsert_data(records)
    print(f"Created {len(records)} records successfully")
    return records