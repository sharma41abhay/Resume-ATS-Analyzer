from app.services.ats_analyzer import analyze_ats


SAMPLE_RESUME = {
    "name": "Test User",

    "skills": [
        "Python",
        "FastAPI",
        "REST API",
        "Git",
        "GitHub",
        "MySQL",
        "SQLite",
        "Data Structures",
        "Algorithms",
    ],

    "education": [
        "B.Tech Computer Science"
    ],

    "experience": [],

    "projects": [
        "Task Management System — Python, FastAPI, SQLite",
        "Built REST APIs for task management."
    ],

    "sections": []
}


SAMPLE_JOB = """
We are looking for a backend developer.

Requirements:
- Python
- FastAPI
- REST API development
- PostgreSQL
- Git
- Docker
- AWS
- Data Structures
- Algorithms
"""


def test_ats_returns_score():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    assert "ats_score" in result

    assert isinstance(
        result["ats_score"],
        (int, float)
    )


def test_ats_score_range():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    assert 0 <= result["ats_score"] <= 100


def test_requirements_exist():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    assert "requirements" in result

    assert isinstance(
        result["requirements"],
        dict
    )


def test_python_exact_match():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    python_requirement = result["requirements"]["python"]

    assert python_requirement["status"] == "exact"

    assert "python" in python_requirement["matched"]


def test_fastapi_exact_match():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    framework = result["requirements"]["backend_framework"]

    assert framework["status"] == "exact"

    assert "fastapi" in framework["matched"]


def test_database_is_related():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    database = result["requirements"]["database_sql"]

    assert database["status"] == "related"

    assert database["matched"] == []


def test_missing_docker():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    docker = result["requirements"]["containerization"]

    assert docker["status"] == "missing"


def test_missing_aws():

    result = analyze_ats(
        SAMPLE_RESUME,
        SAMPLE_JOB
    )

    cloud = result["requirements"]["cloud"]

    assert cloud["status"] == "missing"