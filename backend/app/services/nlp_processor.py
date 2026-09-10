import re
import spacy


# ============================================================
# LOAD NLP MODEL
# ============================================================

nlp = spacy.load("en_core_web_sm")


# ============================================================
# TECHNICAL TERM NORMALIZATION
# ============================================================

NORMALIZATION_MAP = {

    # APIs
    "restful api": "rest api",
    "restful apis": "rest api",
    "rest apis": "rest api",
    "rest-based api": "rest api",

    # Data structures
    "data structures and algorithms": "data structures & algorithms",
    "data structures & algorithms": "data structures & algorithms",

    # Version control
    "version-control": "version control",

    # JavaScript
    "js": "javascript",

    # C++
    "cpp": "c++",

    # Machine learning
    "machine-learning": "machine learning",

    # Deep learning
    "deep-learning": "deep learning",

}


# ============================================================
# CLEAN TEXT
# ============================================================

def clean_text(text: str) -> str:

    if not text:
        return ""

    # Normalize whitespace

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Normalize common separators

    text = text.replace(
        "–",
        "-"
    )

    text = text.replace(
        "—",
        "-"
    )

    return text.strip()


# ============================================================
# NORMALIZE TECHNICAL TERMS
# ============================================================

def normalize_technical_terms(text: str) -> str:

    text = clean_text(text)

    lower_text = text.lower()

    # Longer phrases first

    for original, replacement in sorted(
        NORMALIZATION_MAP.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):

        lower_text = lower_text.replace(
            original,
            replacement
        )

    return lower_text


# ============================================================
# NLP DOCUMENT
# ============================================================

def process_text(text: str):

    text = normalize_technical_terms(
        text
    )

    doc = nlp(
        text
    )

    return doc


# ============================================================
# TOKENIZATION
# ============================================================

def tokenize(text: str):

    doc = process_text(
        text
    )

    return [
        token.text
        for token in doc
        if not token.is_space
    ]


# ============================================================
# STOP WORD REMOVAL
# ============================================================

def get_content_tokens(text: str):

    doc = process_text(
        text
    )

    return [
        token.lemma_.lower()
        for token in doc
        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
        )
    ]


# ============================================================
# SENTENCE EXTRACTION
# ============================================================

def extract_sentences(text: str):

    doc = process_text(
        text
    )

    return [
        sentence.text.strip()
        for sentence in doc.sents
        if sentence.text.strip()
    ]


# ============================================================
# NOUN PHRASES
# ============================================================

def extract_phrases(text: str):

    doc = process_text(
        text
    )

    return [
        phrase.text.strip()
        for phrase in doc.noun_chunks
        if phrase.text.strip()
    ]


# ============================================================
# LEMMATIZATION
# ============================================================

def lemmatize_text(text: str):

    doc = process_text(
        text
    )

    return [
        token.lemma_.lower()
        for token in doc
        if not token.is_space
    ]


# ============================================================
# NLP SUMMARY
# ============================================================

def analyze_text(text: str):

    doc = process_text(
        text
    )

    return {

        "cleaned_text": normalize_technical_terms(
            text
        ),

        "tokens": tokenize(
            text
        ),

        "content_tokens": get_content_tokens(
            text
        ),

        "sentences": extract_sentences(
            text
        ),

        "phrases": extract_phrases(
            text
        ),

        "lemmas": lemmatize_text(
            text
        )
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    sample = """
    Developed RESTful APIs using Python and FastAPI.
    Worked with PostgreSQL databases and Git version control.
    """

    result = analyze_text(
        sample
    )

    print("\nCLEANED TEXT:")
    print(result["cleaned_text"])

    print("\nTOKENS:")
    print(result["tokens"])

    print("\nCONTENT TOKENS:")
    print(result["content_tokens"])

    print("\nSENTENCES:")
    print(result["sentences"])

    print("\nPHRASES:")
    print(result["phrases"])

    print("\nLEMMAS:")
    print(result["lemmas"])