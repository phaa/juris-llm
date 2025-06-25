from google import genai
from google.genai.types import HttpOptions
from langchain_chroma import Chroma
from langchain_google_vertexai import VertexAIEmbeddings

from logging_config import logger
from rag.constants import EMBEDDING_MODEL_NAME, MODEL_NAME, CHROMA_PATH

client = genai.Client(http_options=HttpOptions(api_version="v1"))


def answer_question(query_text: str) -> str:
    try:
        logger.info(f"Generating response")

        embedding_function = VertexAIEmbeddings(model_name=EMBEDDING_MODEL_NAME)
        vector_store = Chroma(
            collection_name="constitucional",
            embedding_function=embedding_function,
            persist_directory=CHROMA_PATH,  # Where to save data locally, remove if not necessary
        )

        # Retrieving the context from the DB using similarity search
        results = vector_store.similarity_search(query_text, k=3)

        # Check if there are any matching results or if the relevance score is too low
        if len(results) == 0:
            return "Não foi possível encontrar resultados para sua pesquisa."

        # Combine context from matching documents
        context_text = "\n\n - -\n\n".join([doc.page_content for doc in results])

        prompt = f"""
        Responda à pergunta com base no seguinte contexto da Constituição:

        {context_text}

        Pergunta: {query_text}
        Responda com texto plano, sem quaisquer formatações.
        """

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        logger.info(f"Response generated successfully")
        return response.text

    except Exception as e:
        logger.error(f"Error when generating response: {e}")
        return "Erro inesperado ao gerar a resposta."
