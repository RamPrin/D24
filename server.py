from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import requests

app = FastAPI()
client = OpenAI()
template="""
# Model:
<!---
Insert PyTM threat model as a codeblock
-->
# Threats
<!---
Write list of threats in the following format:
- [Threat title]: [Short threat description]
[Threat Evaluation by DREAD]  
-->
"""

class Query(BaseModel):
    model: str = 'gpt-4o'
    description: str

class TM(BaseModel):
    agent: str = 'gpt-4o'
    model: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/modelize")
def modelize(description: Query):
    response = client.responses.create(
        model=description.model,
        input=description.description,
        instructions="Compose a threat model from description using PyTM library."
        "Use the last PyTM library version. Provide only model code snippet"
    )
    return {"response": response.output_text}

@app.post("/analyze")
def analyze(model: TM):
    response = client.responses.create(
        model=model.agent,
        input=model.model,
        instructions="Analyze the following threat model and retrieve threats. "
        "Use STRIDE methodology. Give only list of threats categorized by STRIDE with threat title and brief description."
        "Find as many threats as you can."
        "Evaluate these threats with DREAD approach."
    )
    return {"response": response.output_text}

@app.post("/one_agent")
def analyze(description: Query):
    response = client.responses.create(
        model="gpt-4o",
        input=description.model,
        instructions="Compose the model using PyTM and analyze it to retrieve threats by STRIDE methodology."
        "Use the latest PyTM library version. Find as many threats as you can"
        f"Give the output by template:\n{template}"
    )
    return {"response": response.output_text}