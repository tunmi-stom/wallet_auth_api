from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from services.custom_docs_service import CustomDocsService

router = APIRouter()
@router.get("/docs", response_class=HTMLResponse, tags=["Documentation"])
def custom_docs():
    html_content = CustomDocsService.read_html_custom_docs("utils\\documentation_frontend\\docs.html")
    return HTMLResponse(content=html_content)