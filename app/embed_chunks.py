import os
import chromadb
from chromadb.config import Settings
from tqdm import tqdm

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from sentence_transformers import SentenceTransformer


raw_folder = "data/raw"
doc_filename = "constituicao_federal_1988.pdf"
doc_path = os.path.join(raw_folder, doc_filename)


def clean_text(text: str) -> str:
    text = text.replace("\uf24e", "")
    text = text.replace(" \xa0", "")
    return text


def generate_chunks():
    print("Iniciando")
    loader = PyMuPDFLoader(doc_path)

    raw_text = ""
    for page in loader.lazy_load():
        raw_text += page.page_content

    print("Splitting")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", "."],
    )

    chunks = text_splitter.split_text(raw_text)
    chunks = [clean_text(chunk) for chunk in chunks]

    # Model for embedding extraction
    model = SentenceTransformer("all-MiniLM-L6-v2")  # Default model
    embeddings = model.encode(chunks, show_progress_bar=True)

    # ChromaDB client instance
    client = chromadb.Client(Settings(persist_directory="chroma_db"))
    collection = client.get_or_create_collection(name="constitucional")

    # If a chunk is relevant, add it to chromadb
    print("Armazenando")
    for i, chunk in tqdm(enumerate(chunks), total=len(chunks)):
        if len(chunk.strip()) > 50:
            collection.add(
                documents=[chunk],
                embeddings=embeddings[i],
                ids=[f"chunk_{i}"],
                metadatas=[{"source": "constituição", "index": i}],
            )


""" results = collection.query(
    query_texts=["O que a constituição diz sobre liberdade religiosa?"],
    n_results=3
)

print(results["documents"][0]) """
