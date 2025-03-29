from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import requests

app = FastAPI()
client = OpenAI()

class Query(BaseModel):
    description: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/modelize")
def modelize(description: Query):
    response = client.responses.create(
        model="gpt-4o",
        input=description.description
    )
    return {"response": response.output_text}

