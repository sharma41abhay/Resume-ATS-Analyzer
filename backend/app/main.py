from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.resume import router as resume_router


app = FastAPI(
    title="AI Resume Analyzer",
    description="Resume parsing and ATS analysis API",
    version="1.0.0"
)


# ========================================================
# CORS
# ========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ========================================================
# ROUTES
# ========================================================

app.include_router(
    resume_router
)


# ========================================================
# ROOT
# ========================================================

@app.get("/")
def root():

    return {
        "message": "AI Resume Analyzer API is running"
    }