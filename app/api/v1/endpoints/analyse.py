from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi import status
from typing import List, Optional, Union
from uuid import UUID
from pydantic import BaseModel

from app.services.extractor import extract_text_from_pdf, extract_text_from_image
from app.services.qa import answer_query
from app.services.summarizer import summarize_text
from app.db.mongo import logs_collection
from app.models.log_model import build_log_entry

router = APIRouter()

class SummaryItem(BaseModel):
    name_file: str
    summary: str

class SummaryResponse(BaseModel):
    summaries: List[SummaryItem]

class QueryResponse(BaseModel):
    query: str
    responses: List[str]

@router.post(
    "/analyse",
    status_code=status.HTTP_200_OK,
    response_model=Union[SummaryResponse, QueryResponse],
    summary="Analisar CV",
    description="Aceita arquivos PDF ou imagem, e responde com resumo ou respostas baseadas na query"
)
async def analyse_cv(
    files: List[UploadFile] = File(..., description="Arquivos de CV (PDF ou imagem)"),
    query: Optional[str] = Form(None, description="Pergunta para responder com base nos arquivos"),
    request_id: UUID = Form(..., description="UUID para identificar a requisição"),
    user_id: str = Form(..., description="ID do usuário que está fazendo a análise")
):
    texts, names = [], []
    for file in files:
        content = await file.read()
        ext = file.filename.lower()
        text = extract_text_from_pdf(content) if ext.endswith(".pdf") else extract_text_from_image(content)
        texts.append(text)
        names.append(file.filename)

    result = (
        {"query": query, "responses": answer_query(texts, query)} if query
        else {"summaries": [{"name_file": names[i], "summary": summarize_text(texts[i])} for i in range(len(texts))]}
    )

    logs_collection.insert_one(build_log_entry(str(request_id), user_id, query, result))
    return JSONResponse(content=result)