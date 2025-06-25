from unittest.mock import patch, MagicMock
from app.rag.main import answer_question
from app.logging_config import logger

@patch("app.rag.get_chroma_collection")
@patch("app.rag.requests.post")
def test_answer_question_success(mock_post, mock_chroma):
    logger.info("Testing answer_question() with simulated input")
    # Simulate chromadb return
    mock_chroma.return_value.query.return_value = {
        "documents": [["Texto do contexto simulado."]]
    }

    # Emulate model response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"text": "Resposta simulada"}
    mock_post.return_value = mock_response

    question = "O que a constituição fala sobre liberdade de expressão?"
    response = answer_question(question)

    assert "Resposta simulada" in response


@patch("app.rag.requests.post", side_effect=Exception("Erro Simulado"))
@patch("app.rag.get_chroma_collection")
def test_answer_question_fail(mock_chroma, mock_post):
    logger.info("Testing answer_question() with inference exception")

    # Simulate chromadb return
    mock_chroma.return_value.query.return_value = {
        "documents": [["Texto do contexto simulado."]]
    }
    response = answer_question("Qualquer pergunta")
    assert "problema" in response.lower()