from google import genai
from google.genai.types import HttpOptions
from app.chroma_loader import get_chroma_collection
from app.logging_config import logger

client = genai.Client(http_options=HttpOptions(api_version="v1"))

def answer_question(question: str) -> str:
    try:
        logger.info(f"Receiving question {question}")
        collection = get_chroma_collection()
        results = collection.query(query_texts=[question], n_results=3)
        context = "\n\n".join(results["documents"][0])
        print(context)
        prompt = f"""
        Responda à pergunta com base no seguinte contexto da Constituição:

        {context}

        Pergunta: {question}
        Resposta:
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=prompt,
        )

        logger.info(f"Response generated successfully")
        return response.text

    except Exception as e:
        logger.error(f"Error when generating response: {e}")
        print(f"[Erro inesperado] {e}")
        return "Erro inesperado ao gerar a resposta."
