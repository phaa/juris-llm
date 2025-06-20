from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.models import Question, Answer
from app.rag import answer_question

app = FastAPI()

# Prometheus middleware endpoint /metrics
Instrumentator.instrument(app).expose(app)

@app.get("/ask", response_model=Answer)
def ask(question: str): # change to Question
    response = answer_question(question)
    return Answer(text=response)
