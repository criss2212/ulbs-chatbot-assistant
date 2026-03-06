from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="ULBS Chatbot API")

class Question(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Bine ai venit la Code4ULBS Chatbot!"}

@app.post("/ask")
async def ask_question(question: Question):
    return {
        "answer": f"Ai întrebat: '{question.text}'. Momentan sunt în curs de configurare a bazei de date cu regulamentele ULBS."
    }