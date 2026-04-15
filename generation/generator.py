from config import LLM_PROVIDER
from generation.ollama_client import generate_with_ollama

# optional OpenAI
from generation.openai_client import client as openai_client


def generate_answer(query, context):
    prompt = f"""
    You are a helpful assistant.

    Answer ONLY using the context below.
    If not found, say "I don't know".

    Context:
    {context}

    Question:
    {query}
    """

    if LLM_PROVIDER == "ollama":
        return generate_with_ollama(prompt)

    elif LLM_PROVIDER == "openai":
        response = openai_client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    else:
        return "Invalid LLM provider"