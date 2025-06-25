from fastapi import APIRouter
from api.models import Answer
from rag.main import answer_question

router = APIRouter()

@router.get("/ask", response_model=Answer)
def ask(question: str): # change to Question
    response = answer_question(question)
    return Answer(text=response)


""" @router.get("/generate", response_model=Answer)
def ask(): # change to Question
    response = generate_chunks()
    return Answer(text="OK") """