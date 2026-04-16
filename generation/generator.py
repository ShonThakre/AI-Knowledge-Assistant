from config import LLM_PROVIDER
from generation.ollama_client import generate_with_ollama
from generation.openai_client import generate_with_openai


def generate_answer(query: str, context: str):
    prompt = f"""
You are a helpful assistant.

Use ONLY the provided context to answer.
Do NOT make up information.
If the answer is not in the context, say "I don't know".

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