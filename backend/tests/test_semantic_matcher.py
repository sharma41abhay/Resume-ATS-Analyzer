from app.services.semantic_matcher import (
    semantic_similarity,
    classify_similarity,
    find_best_match,
)


def test_empty_text_similarity():
    score = semantic_similarity("", "Python")

    assert score == 0.0


def test_exact_semantic_match():
    score = semantic_similarity(
        "Python programming",
        "Developed applications using Python."
    )

    assert score >= 0.60


def test_unrelated_semantic_match():
    score = semantic_similarity(
        "AWS cloud deployment",
        "Created a responsive HTML and CSS website."
    )

    assert score < 0.25


def test_strong_classification():
    assert classify_similarity(0.70) == "strong"


def test_related_classification():
    assert classify_similarity(0.50) == "related"


def test_weak_classification():
    assert classify_similarity(0.30) == "weak"


def test_unrelated_classification():
    assert classify_similarity(0.10) == "unrelated"


def test_find_best_match():

    result = find_best_match(
        "Build REST APIs",
        [
            "Designed a chess game using C++.",
            "Created REST APIs using FastAPI.",
            "Built a responsive website using HTML and CSS."
        ]
    )

    assert result is not None

    assert result["resume_match"] == (
        "Created REST APIs using FastAPI."
    )

    assert result["similarity"] >= 0.60

    assert result["classification"] == "strong"