from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.endpoints import analyse

app = FastAPI(**settings.api_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyse.router, prefix="/v1")

if __name__ == "__main__":
    import uvicorn
    import torch
    print("GPU:", torch.cuda.get_device_name(0))
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)