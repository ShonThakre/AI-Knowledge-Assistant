from idlelib import query

from retrieval.retriever import retrieve_chunks
from generation.generator import generate_answer


def run_rag_pipeline(query: str):
    chunks = retrieve_chunks(query)
    print(f"Retrieved {len(chunks)} chunks for query: '{query}'")
    context = "\n".join(chunks)

    answer = generate_answer(query, context)

    return answer