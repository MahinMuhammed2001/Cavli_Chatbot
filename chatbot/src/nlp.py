import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Synonym mapping for better understanding
SYNONYM_MAP = {
    "companies": ["businesses", "corporations"],
    "semiconductors": ["chipmakers", "integrated circuits"],
    "microcontrollers": ["mcu", "controllers"],
    "germany": ["deutschland"]
}
def resolve_synonyms(word):
    """
    Resolves a word to its synonym key if it exists in the synonym map.
    """
    for key, synonyms in SYNONYM_MAP.items():
        if word in synonyms or word == key:
            return key
    return word
def extract_keywords(query):
    """
    Extracts keywords from the user query and resolves synonyms.
    """
    doc = nlp(query.lower())

    # Extract tokens that are nouns, proper nouns, or adjectives
    keywords = [
        resolve_synonyms(token.text) 
        for token in doc 
        if token.pos_ in {"NOUN", "PROPN", "ADJ"} and not token.is_stop and not token.is_punct
    ]
    return keywords
