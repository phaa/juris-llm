from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.rag.embed_chunks import load_documents, split_text


def test_chunking():
    documents = load_documents()  # Load documents from a source
    chunks = split_text(documents)  # Split documents into manageable chunks

    assert isinstance(chunks, list)
    assert len(chunks) >= 2 # Must split the text
    for chunk in chunks:
        assert len(chunk) > 20
        assert "\n\n" not in chunk # Original separator removed
