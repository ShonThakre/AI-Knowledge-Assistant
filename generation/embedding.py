from config import EMBEDDING_PROVIDER
from generation.ollama_client import get_embedding_ollama
from generation.openai_client import get_embedding_openai


def get_embedding(text: str):
    if EMBEDDING_PROVIDER == "ollama":
        return get_embedding_ollama(text)

    elif EMBEDDING_PROVIDER == "openai":
        return get_embedding_openai(text)

    else:
        raise ValueError("Invalid embedding provider")