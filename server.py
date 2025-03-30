from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import requests

app = FastAPI()
client = OpenAI()

class Query(BaseModel):
    description: str

class TM(BaseModel):
    model: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/modelize")
def modelize(description: Query):
    response = client.responses.create(
        model="gpt-4o",
        input=description.description,
        instructions="Use the last PyTM library version. Provide only model code snippet"
    )
    return {"response": response.output_text}

@app.post("/analyze")
def analyze(model: TM):
    response = client.responses.create(
        model="gpt-4o",
        input=model.model,
        instructions="Analyze the following threat model and retrieve threats. "
        "Use STRIDE methodology. Give only list of threats categorized by STRIDE with threat title and brief description."
        "Evaluate these threats with DREAD approach"
    )
    return {"response": response.output_text}