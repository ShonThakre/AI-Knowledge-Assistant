from config import LLM_PROVIDER
from generation.ollama_client import generate_with_ollama
from generation.openai_client import generate_with_openai


def generate_answer(query: str, context: str):
    prompt = f"""
You are an AI assistant.

Rules:
- Answer ONLY from context
- If partial info exists, answer using best available info
- If question has typo, still try to answer
- Be helpful, not overly strict
- If nothing found, say "Not found in document"

Context:
{context}

Question:
{query}

Answer:
"""

    if LLM_PROVIDER == "ollama":
        return generate_with_ollama(prompt)

    elif LLM_PROVIDER == "openai":
        return generate_with_openai(prompt)

    else:
        raise ValueError("Invalid LLM provider")