from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.utils.text_tools import clean_text


def test_chunking():
    sample_text = (
        "Art. 1º Todos são iguais perante a lei.\n\n"
        "Art. 2º Ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei.\n\n"
        "Art. 3º É livre a manifestação do pensamento."
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 100,
        chunk_overlap=20,
        separators=["\n\n", "\n", "."]
    )

    chunks = splitter.split_text(sample_text)
    chunks = [clean_text(c) for c in chunks]

    assert isinstance(chunks, list)
    assert len(chunks) >= 2 # Must split the text
    for chunk in chunks:
        assert len(chunk) > 20
        assert "\n\n" not in chunk # Original separator removed
