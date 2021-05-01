from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import text_similarity, model_multiling

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextIn(BaseModel):
    first_text: str
    second_text: str


@app.get('/')
def pong():
    return {'Status': 'Up'}


@app.post('/api/ml')
def get_score(texts: TextIn):
    score = text_similarity(texts.first_text, texts.second_text, model_multiling)
    return {'score': score}


@app.get('/')
def get_service_status():
    return {'status': 'up'}
