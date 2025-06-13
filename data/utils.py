import unidecode

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    return unidecode.unidecode(text).strip().lower()
