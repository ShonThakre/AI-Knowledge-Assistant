from retrieval.retriever import retrieve_chunks
from generation.generator import generate_answer

def run_rag_pipeline(query, source=None):
    results = retrieve_chunks(query, source=source)

    chunks = [r["text"] for r in results]

    sources = list(set([r["source"] for r in results]))

    context = "\n".join(chunks[:10])

    answer = generate_answer(query, context)

    return {
        "answer": answer,
        "sources": sources,
        "chunks": chunks[:3] 
    }