from fastapi import APIRouter
from pydantic import BaseModel
from pipeline.rag_pipeline import run_rag_pipeline

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: ChatRequest):
    answer = run_rag_pipeline(request.query)
    return {"answer": answer}