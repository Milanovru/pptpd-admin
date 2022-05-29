from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import chap_secrets


app = FastAPI(
    prefix='/api/v1/'
)

app.include_router(chap_secrets.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
