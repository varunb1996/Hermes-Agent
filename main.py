from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

class TaskRequest(BaseModel):
    task: str

@app.get("/")
def home():
    return {"message": "HermesForge-X running"}

@app.post("/generate")
def generate(request: TaskRequest):

    response = client.chat.completions.create(
        model="openrouter/owl-alpha",
        messages=[
            {
                "role": "system",
                "content": "You are HermesForge-X, an advanced autonomous engineering agent."
            },
            {
                "role": "user",
                "content": request.task
            }
        ],
        temperature=0.2,
        max_tokens=2000
    )

    return {
        "response": response.choices[0].message.content
    }