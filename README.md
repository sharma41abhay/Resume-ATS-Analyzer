# AI Resume ATS Analyzer

An AI-powered full-stack Resume ATS Analyzer that parses PDF resumes, extracts structured information, compares resumes against job descriptions, and generates an ATS compatibility score with actionable feedback.

## Overview

Recruiters and Applicant Tracking Systems (ATS) often evaluate resumes against job requirements before a candidate reaches the interview stage. This project helps candidates understand how well their resume matches a specific job description.

The application combines PDF parsing, NLP-based skill extraction, rule-based requirement analysis, and semantic similarity using Sentence Transformers to produce a practical ATS analysis.

## Features

- Upload a resume in PDF format
- Extract resume text and structured information
- Detect skills and normalize common skill aliases
- Analyze a job description against the resume
- Identify exact matches, related skills, missing skills, and resume-only skills
- Group job requirements into meaningful categories
- Semantic matching using `all-MiniLM-L6-v2`
- Hybrid ATS scoring combining exact matching and semantic similarity
- Targeted resume evidence for requirements
- REST API built with FastAPI
- React + Vite frontend
- Responsive dashboard-style interface
- Automated backend tests with pytest

## Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- PyMuPDF
- NLP processing
- Sentence Transformers
- PyTorch
- pytest

### Frontend

- React
- Vite
- JavaScript
- Axios
- CSS

## Architecture

```text
Resume PDF
    │
    ▼
PDF Parser
    │
    ▼
Resume Parser + NLP Processing
    │
    ▼
ATS Analyzer
 ┌──────────────────────────────┐
 │ Exact Skill Matching         │
 │ Requirement Analysis         │
 │ Semantic Matching            │
 │ Hybrid ATS Scoring           │
 │ Resume Evidence              │
 └──────────────┬───────────────┘
                │
                ▼
       ATS Score + Results
       + Recommendations
```

## Project Structure

```text
AI-Resume-ATS-Analyzer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   └── resume.py
│   │   └── services/
│   │       ├── ats_analyzer.py
│   │       ├── nlp_processor.py
│   │       ├── pdf_parser.py
│   │       ├── resume_analyzer.py
│   │       ├── resume_parser.py
│   │       └── semantic_matcher.py
│   │
│   ├── tests/
│   │   ├── fixtures/
│   │   │   └── sample_resume.pdf
│   │   ├── test_ats_analyzer.py
│   │   ├── test_resume_api.py
│   │   └── test_semantic_matcher.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   │   └── hero.png
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── .gitignore
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/sharma41abhay/Resume-ATS-Analyzer.git
cd Resume-ATS-Analyzer
```

### 2. Start the backend

From the project root:

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Start the frontend

Open a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Vite will display the local frontend URL. The application commonly runs on:

```text
http://localhost:5173
```

If that port is occupied, Vite may select another available port.

## API Endpoints

### Upload Resume

```http
POST /resume/upload
```

Accepts a PDF resume and returns parsed resume information.

### Analyze Resume

```http
POST /resume/analyze
```

Accepts:

- `file` — Resume PDF
- `job_description` — Job description text

Returns:

- Parsed resume data
- ATS score
- Job skill analysis
- Exact matches
- Related matches
- Missing skills
- Recommendations
- Semantic matching information

## ATS Analysis

The analyzer uses a hybrid approach instead of relying only on keyword counting.

### Exact Matching

Direct matches between resume skills and job requirements receive the strongest match signal.

### Semantic Matching

Sentence Transformers compare resume evidence with job requirements. This helps identify related concepts even when the wording differs.

Model:

```text
all-MiniLM-L6-v2
```

### Technology-Aware Matching

Technology-specific relationships are handled separately from general semantic relationships. For example, related technologies can receive partial credit without being incorrectly treated as exact matches.

### Hybrid Scoring

The final ATS score combines requirement matching and semantic evidence to provide a more useful estimate of resume-job compatibility.

## Example

For a backend developer position, the analyzer can distinguish between:

| Requirement | Example result |
|---|---|
| Python | Exact match |
| FastAPI / Django | Exact or related match |
| REST API | Exact/semantic match |
| PostgreSQL | Related when another SQL database is present |
| Git / GitHub | Exact match |
| Docker | Missing when not present |
| AWS / Cloud | Missing or semantically related |

This allows the application to highlight genuine skill gaps rather than simply counting keywords.

## Testing

From the `backend` directory:

```powershell
.\venv\Scripts\Activate.ps1
pytest -q
```

The test suite covers:

- ATS analyzer logic
- Resume API endpoints
- Semantic matching

## Future Improvements

- Resume improvement suggestions based on missing requirements
- Resume formatting and ATS readability checks
- Job-description keyword weighting
- Skill-gap visualizations
- User accounts and saved analyses
- Production database integration
- Cloud deployment
- More robust section-aware resume parsing

## Project Status

**Working full-stack prototype**

The backend API, resume parsing pipeline, ATS analysis, semantic matching, automated tests, and React frontend are implemented and integrated.

## Author

**Abhay Sharma**

GitHub: https://github.com/sharma41abhay
