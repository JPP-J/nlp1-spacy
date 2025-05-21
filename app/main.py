from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="NLP API",
    description="API for Natural Language Processing tasks using spaCy",
    version="1.0.0"
)

app.include_router(router) 