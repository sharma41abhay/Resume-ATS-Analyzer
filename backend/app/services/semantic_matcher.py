from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================================
# CREATE EMBEDDING
# ============================================================

def create_embedding(text: str):

    if not text or not text.strip():
        return None

    return model.encode(
        text,
        convert_to_numpy=True
    )


# ============================================================
# CALCULATE SEMANTIC SIMILARITY
# ============================================================

def semantic_similarity(
    text1: str,
    text2: str
):

    embedding1 = create_embedding(
        text1
    )

    embedding2 = create_embedding(
        text2
    )

    if embedding1 is None or embedding2 is None:
        return 0.0

    score = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return float(score)


# ============================================================
# CLASSIFY SEMANTIC SIMILARITY
# ============================================================

def classify_similarity(
    score: float
):

    if score >= 0.60:

        return "strong"

    elif score >= 0.40:

        return "related"

    elif score >= 0.25:

        return "weak"

    else:

        return "unrelated"


# ============================================================
# FIND BEST SEMANTIC MATCH
# ============================================================

def find_best_match(
    job_requirement: str,
    resume_texts: list[str]
):

    if not job_requirement:
        return None

    if not resume_texts:
        return None

    best_match = None
    best_score = 0.0

    for resume_text in resume_texts:

        score = semantic_similarity(
            job_requirement,
            resume_text
        )

        if score > best_score:

            best_score = score

            best_match = resume_text

    return {
        "job_requirement": job_requirement,

        "resume_match": best_match,

        "similarity": round(
            best_score,
            4
        ),

        "classification": classify_similarity(
            best_score
        )
    }


# ============================================================
# ANALYZE TARGETED RESUME EVIDENCE
# ============================================================

def analyze_requirement_semantically(
    requirement: str,
    evidence: list
):
    """
    Analyze only the targeted resume evidence associated with
    a specific job requirement.

    Expected evidence format:

    [
        {
            "text": "...",
            "source": "projects",
            "matched_terms": ["rest-based"]
        }
    ]
    """

    if not requirement:

        return {
            "requirement": requirement,
            "resume_evidence": [],
            "best_match": None,
            "similarity": 0.0,
            "classification": "unrelated"
        }

    if not evidence:

        return {
            "requirement": requirement,
            "resume_evidence": [],
            "best_match": None,
            "similarity": 0.0,
            "classification": "unrelated"
        }

    # --------------------------------------------------------
    # Extract text from evidence objects
    # --------------------------------------------------------

    evidence_texts = []

    for item in evidence:

        # Normal structured evidence
        if isinstance(
            item,
            dict
        ):

            text = item.get(
                "text",
                ""
            )

        # Also support plain strings
        elif isinstance(
            item,
            str
        ):

            text = item

        else:

            continue

        if text and text.strip():

            evidence_texts.append(
                text.strip()
            )

    if not evidence_texts:

        return {
            "requirement": requirement,
            "resume_evidence": [],
            "best_match": None,
            "similarity": 0.0,
            "classification": "unrelated"
        }

    # --------------------------------------------------------
    # Find strongest semantic match
    # --------------------------------------------------------

    result = find_best_match(
        requirement,
        evidence_texts
    )

    if result is None:

        return {
            "requirement": requirement,
            "resume_evidence": evidence_texts,
            "best_match": None,
            "similarity": 0.0,
            "classification": "unrelated"
        }

    return {
        "requirement": requirement,

        "resume_evidence": evidence_texts,

        "best_match":
            result["resume_match"],

        "similarity":
            result["similarity"],

        "classification":
            result["classification"]
    }


# ============================================================
# ANALYZE MULTIPLE REQUIREMENTS
# ============================================================

def analyze_requirements_semantically(
    requirements: list,
    semantic_targets: dict
):
    """
    Analyze multiple ATS requirements using the targeted evidence
    generated by ats_analyzer.py.

    semantic_targets is expected to look like:

    {
        "python": {
            "requirement": "Python",
            "targeted_resume_text": "...",
            "evidence": [...]
        }
    }
    """

    results = []

    for requirement in requirements:

        requirement_key = (
            str(requirement)
            .strip()
            .lower()
        )

        target = semantic_targets.get(
            requirement_key
        )

        if not target:

            results.append({

                "requirement":
                    requirement,

                "resume_evidence":
                    [],

                "best_match":
                    None,

                "similarity":
                    0.0,

                "classification":
                    "unrelated"
            })

            continue

        evidence = target.get(
            "evidence",
            []
        )

        result = analyze_requirement_semantically(
            requirement,
            evidence
        )

        results.append(
            result
        )

    return results


# ============================================================
# TEST SEMANTIC MATCHING
# ============================================================

if __name__ == "__main__":

    test_cases = [

        (
            "Build REST APIs",
            "Created REST APIs for a task management system."
        ),

        (
            "Python programming",
            "Developed applications using Python."
        ),

        (
            "Git version control",
            "Used Git and GitHub to manage source code."
        ),

        (
            "Develop backend applications",
            "Built backend services using FastAPI."
        ),

        (
            "Use Django for backend development",
            "Developed web APIs using FastAPI."
        ),

        (
            "Work with PostgreSQL",
            "Worked with MySQL and SQLite databases."
        ),

        (
            "Cloud deployment",
            "Deployed applications on AWS."
        ),

        (
            "Develop backend applications",
            "Created an interactive typing speed test using JavaScript."
        ),

        (
            "Work with databases",
            "Designed a chess game using C++ and Raylib."
        ),

        (
            "AWS cloud deployment",
            "Created a responsive HTML and CSS website."
        ),
    ]


    print("=" * 70)
    print("SEMANTIC MATCHING TEST")
    print("=" * 70)


    for job_text, resume_text in test_cases:

        score = semantic_similarity(
            job_text,
            resume_text
        )

        classification = classify_similarity(
            score
        )

        print("\nJob:")
        print(job_text)

        print("\nResume:")
        print(resume_text)

        print("\nSimilarity:")
        print(
            round(
                score,
                4
            )
        )

        print("\nClassification:")
        print(
            classification
        )

        print("-" * 70)