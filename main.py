from fastapi import FastAPI, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from routes import auth
from core.config import settings
from database.db_config import Base, engine

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=None,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return {"detail": settings.PROJECT_NAME}