from fastapi import APIRouter, Query
from app.services.document_retriever import search_policy

router = APIRouter(prefix="/policy")

@router.get("/search")
def search_docs(query: str = Query(...)):
    results = search_policy(query)
    return {"results": results}
