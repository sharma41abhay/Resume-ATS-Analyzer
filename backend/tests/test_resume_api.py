from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# ============================================================
# TEST JOB DESCRIPTION
# ============================================================

JOB_DESCRIPTION = """
We are looking for a motivated Backend Developer.

Requirements:

- Python
- FastAPI or Django
- REST API development
- PostgreSQL
- Git
- GitHub
- Data Structures
- Algorithms
- Docker
- AWS
"""


# ============================================================
# SAMPLE PDF HELPER
# ============================================================

def get_sample_pdf():

    return (
        Path(__file__).parent
        / "fixtures"
        / "sample_resume.pdf"
    )


# ============================================================
# RESUME UPLOAD TESTS
# ============================================================

def test_resume_upload_rejects_non_pdf():

    response = client.post(
        "/resume/upload",
        files={
            "file": (
                "resume.txt",
                b"This is not a PDF",
                "text/plain"
            )
        }
    )

    assert response.status_code == 400

    assert response.json()["detail"] == (
        "Only PDF files are supported"
    )


def test_resume_upload_pdf():

    pdf_path = get_sample_pdf()

    with pdf_path.open("rb") as pdf_file:

        response = client.post(
            "/resume/upload",
            files={
                "file": (
                    "sample_resume.pdf",
                    pdf_file,
                    "application/pdf"
                )
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "filename" in data
    assert "resume" in data

    resume = data["resume"]

    assert "name" in resume
    assert "skills" in resume
    assert "education" in resume
    assert "projects" in resume


# ============================================================
# ATS ANALYZE TESTS
# ============================================================

def test_analyze_requires_job_description():

    pdf_path = get_sample_pdf()

    with pdf_path.open("rb") as pdf_file:

        response = client.post(
            "/resume/analyze",
            files={
                "file": (
                    "sample_resume.pdf",
                    pdf_file,
                    "application/pdf"
                )
            }
        )

    # Missing or empty job description is handled
    # by our endpoint validation.

    assert response.status_code == 400

    assert response.json()["detail"] == (
        "Job description is required"
    )


def test_analyze_rejects_empty_job_description():

    pdf_path = get_sample_pdf()

    with pdf_path.open("rb") as pdf_file:

        response = client.post(
            "/resume/analyze",
            files={
                "file": (
                    "sample_resume.pdf",
                    pdf_file,
                    "application/pdf"
                )
            },
            data={
                "job_description": ""
            }
        )

    assert response.status_code == 400

    assert response.json()["detail"] == (
        "Job description is required"
    )


def test_analyze_resume_with_job_description():

    pdf_path = get_sample_pdf()

    with pdf_path.open("rb") as pdf_file:

        response = client.post(
            "/resume/analyze",
            files={
                "file": (
                    "sample_resume.pdf",
                    pdf_file,
                    "application/pdf"
                )
            },
            data={
                "job_description": JOB_DESCRIPTION
            }
        )

    assert response.status_code == 200

    data = response.json()

    # --------------------------------------------------------
    # Top-level response
    # --------------------------------------------------------

    assert "filename" in data
    assert "resume" in data
    assert "ats" in data

    # --------------------------------------------------------
    # ATS result
    # --------------------------------------------------------

    ats = data["ats"]

    assert "ats_score" in ats
    assert "requirements" in ats
    assert "semantic_targets" in ats
    assert "recommendations" in ats

    # --------------------------------------------------------
    # Score validation
    # --------------------------------------------------------

    assert isinstance(
        ats["ats_score"],
        (int, float)
    )

    assert 0 <= ats["ats_score"] <= 100


def test_analyze_returns_expected_requirements():

    pdf_path = get_sample_pdf()

    with pdf_path.open("rb") as pdf_file:

        response = client.post(
            "/resume/analyze",
            files={
                "file": (
                    "sample_resume.pdf",
                    pdf_file,
                    "application/pdf"
                )
            },
            data={
                "job_description": JOB_DESCRIPTION
            }
        )

    assert response.status_code == 200

    data = response.json()

    ats = data["ats"]

    requirements = ats["requirements"]

    # --------------------------------------------------------
    # Required requirement groups
    # --------------------------------------------------------

    assert "python" in requirements

    assert (
        "backend_framework"
        in requirements
    )

    assert (
        "database_sql"
        in requirements
    )

    assert (
        "containerization"
        in requirements
    )

    assert "cloud" in requirements

    # --------------------------------------------------------
    # Python
    # --------------------------------------------------------

    assert (
        requirements["python"]["status"]
        == "exact"
    )

    # --------------------------------------------------------
    # Backend framework
    # --------------------------------------------------------

    assert (
        requirements["backend_framework"]["status"]
        == "exact"
    )

    # --------------------------------------------------------
    # Database
    # --------------------------------------------------------

    assert (
        requirements["database_sql"]["status"]
        == "related"
    )

    # --------------------------------------------------------
    # Docker
    # --------------------------------------------------------

    assert (
        requirements["containerization"]["status"]
        == "missing"
    )

    # --------------------------------------------------------
    # AWS
    # --------------------------------------------------------

    assert (
        requirements["cloud"]["status"]
        == "missing"
    )