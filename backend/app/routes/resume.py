from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException,
)

from app.services.pdf_parser import extract_pdf_data
from app.services.resume_parser import parse_resume_with_layout
from app.services.ats_analyzer import analyze_ats


router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


# ============================================================
# RESUME UPLOAD / PARSING
# ============================================================

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
):
    """
    Upload a resume PDF and return the
    structured resume data.
    """

    # --------------------------------------------------------
    # 1. Validate file type
    # --------------------------------------------------------

    if file.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported",
        )

    # --------------------------------------------------------
    # 2. Read uploaded file
    # --------------------------------------------------------

    contents = await file.read()

    if not contents:

        raise HTTPException(
            status_code=400,
            detail="Uploaded PDF is empty",
        )

    # --------------------------------------------------------
    # 3. Extract PDF data
    # --------------------------------------------------------

    try:

        pdf_lines = extract_pdf_data(
            contents
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=f"Unable to read PDF: {str(e)}",
        )

    # --------------------------------------------------------
    # 4. Create plain text
    # --------------------------------------------------------

    text = "\n".join(
        line["text"]
        for line in pdf_lines
    )

    # --------------------------------------------------------
    # 5. Parse resume
    # --------------------------------------------------------

    try:

        resume_data = parse_resume_with_layout(
            text,
            pdf_lines,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to parse resume: {str(e)}",
        )

    # --------------------------------------------------------
    # 6. Return parsed resume
    # --------------------------------------------------------

    return {
        "filename": file.filename,
        "resume": resume_data,
    }


# ============================================================
# RESUME + JOB DESCRIPTION ATS ANALYSIS
# ============================================================

@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(""),
):
    """
    Upload a resume PDF and analyze it
    against a job description.
    """

    # --------------------------------------------------------
    # 1. Validate file type
    # --------------------------------------------------------

    if file.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported",
        )

    # --------------------------------------------------------
    # 2. Validate job description
    # --------------------------------------------------------

    if (
        not job_description
        or not job_description.strip()
    ):

        raise HTTPException(
            status_code=400,
            detail="Job description is required",
        )

    # --------------------------------------------------------
    # 3. Read uploaded PDF
    # --------------------------------------------------------

    contents = await file.read()

    if not contents:

        raise HTTPException(
            status_code=400,
            detail="Uploaded PDF is empty",
        )

    # --------------------------------------------------------
    # 4. Extract PDF data
    # --------------------------------------------------------

    try:

        pdf_lines = extract_pdf_data(
            contents
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=f"Unable to read PDF: {str(e)}",
        )

    # --------------------------------------------------------
    # 5. Create plain text
    # --------------------------------------------------------

    text = "\n".join(
        line["text"]
        for line in pdf_lines
    )

    # --------------------------------------------------------
    # 6. Parse resume
    # --------------------------------------------------------

    try:

        resume_data = parse_resume_with_layout(
            text,
            pdf_lines,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to parse resume: {str(e)}",
        )

    # --------------------------------------------------------
    # 7. Run ATS analysis
    # --------------------------------------------------------

    try:

        ats_result = analyze_ats(
            resume_data,
            job_description,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to analyze resume: {str(e)}",
        )

    # --------------------------------------------------------
    # 8. Return complete result
    # --------------------------------------------------------

    return {
        "filename": file.filename,

        "resume": resume_data,

        "ats": ats_result,
    }