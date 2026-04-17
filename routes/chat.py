from fastapi import APIRouter
from pydantic import BaseModel
from pipeline.rag_pipeline import run_rag_pipeline
from utils.logger import log_chat

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    source: str | None = None

@router.post("/chat")
def chat(request: ChatRequest):
    result = run_rag_pipeline(request.query, request.source)
    log_chat(request.query, result)
    return result