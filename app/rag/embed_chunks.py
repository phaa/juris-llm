import os
import shutil
from uuid import uuid4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_chroma import Chroma

from rag.constants import DATA_PATH, CHROMA_PATH, EMBEDDING_MODEL_NAME
from logging_config import logger


def clean_text(text: str) -> str:
    text = text.replace("\uf24e", "")
    text = text.replace(" \xa0", "")
    return text


def load_documents() -> list[Document]:
    """
    Load PDF documents from the specified directory using PyPDFDirectoryLoader.
    Returns:
    List of Document objects: Loaded PDF documents represented as Langchain Document objects.
    """
    try:
        # Initialize PDF loader with specified directory
        document_loader = PyPDFDirectoryLoader(DATA_PATH)
        # Load PDF documents and return them as a list of Document objects
        return document_loader.load()
    except Exception as e:
        logger.error(f"There was an error while loading documents: {e}")


def split_text(documents: list[Document]) -> list[Document]:
    """
    Split the text content of the given list of Document objects into smaller chunks.
    Args:
      documents (list[Document]): List of Document objects containing text content to split.
    Returns:
      list[Document]: List of Document objects representing the split text chunks.
    """
    # Initialize text splitter with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )

    # Split documents into smaller chunks using text splitter
    chunks = text_splitter.split_documents(documents)
    logger.info(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks  # Return the list of split text chunks


def save_to_chroma(chunks: list[Document]):
    """
    Save the given list of Document objects to a Chroma database.
    Args:
    chunks (list[Document]): List of Document objects representing text chunks to save.
    Returns:
    None
    """
    try:
        # Clear out the existing database directory if it exists
        if os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)

        # Create a new Chroma database from the documents using OpenAI embeddings
        embedding_function = VertexAIEmbeddings(model_name=EMBEDDING_MODEL_NAME)
        vector_store = Chroma(
            collection_name="constitucional",
            embedding_function=embedding_function,
            persist_directory=CHROMA_PATH,  # Where to save data locally, remove if not necessary
        )
        uuids = [str(uuid4()) for _ in range(len(chunks))]
        vector_store.add_documents(documents=chunks, ids=uuids)
    except Exception as e:
        logger.error(f"There was an error while saving embeddings to ChromaDB: {e}")


def generate_data_store():
    """
    Function to generate vector database in chroma from documents.
    """
    documents = load_documents()  # Load documents from a source
    chunks = split_text(documents)  # Split documents into manageable chunks
    save_to_chroma(chunks)  # Save the processed data to a data store

