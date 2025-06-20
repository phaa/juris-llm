from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


def test_ask_success():
    mock_response = {"text": "Aqui está a resposta gerada"}

    with patch("app.main.answer_question", return_value="Aqui está a resposta gerada"):
        response = client.get("/ask", params={"question": "O que é liberdade religiosa"})
        assert response.status_code == 200
        assert response.json() == mock_response


def test_ask_missing_param():
    response = client.get("/ask")  # No param
    assert response.status_code == 422  # # Unprocessable Entity (missing question)


def test_ask_empty_query():
    response = client.get("/ask?question=")
    body = response.json()
    assert response.status_code == 200
    assert isinstance(body["text"], str)
    assert len(body["text"]) >= 0


def test_ask_none_like_value():
    response = client.get("/ask?q=null")
    assert response.status_code == 200
