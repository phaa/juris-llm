def clean_text(text: str) -> str:
    text = text.replace("\uf24e", "")
    text = text.replace(" \xa0", "")
    return text