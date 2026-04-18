from db.upsert_manager import upsert_chunks
from fastapi import APIRouter, UploadFile, File, HTTPException
from ingestion.fixed_size_chunking import chunk_text, load_file, clean_text

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        print(f"Received file: {file.filename}")
        content = await file.read()

        text = load_file(content, file.filename)

        cleaned_text = clean_text(text)

        chunks = chunk_text(cleaned_text)

        upsert_chunks(chunks, source=file.filename)

        return {
            "message": "Document uploaded successfully",
            "chunks": len(chunks)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))