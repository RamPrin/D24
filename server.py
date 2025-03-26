from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Query(BaseModel):
    description: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/modelize")
def modelize(description: Query):
    requests.post(
        "", json={
            
        }
    )
    return {"response": description.description}

