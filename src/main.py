from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.api import settings

app = FastAPI()

print(settings)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE"),
    allow_headers=[settings.CORS_HEADERS],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
