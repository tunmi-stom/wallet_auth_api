from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import auth, docs
from core.config import settings
from database.db_config import Base, engine

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # to be changed in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
# app.include_router(docs.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return {"detail": settings.PROJECT_NAME}