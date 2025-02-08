from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.example import router as example_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example_router, prefix="/api/v1/example", tags=["example"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}