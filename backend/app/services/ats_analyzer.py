import re

from app.services.semantic_matcher import (
    analyze_requirement_semantically
)

# ============================================================
# NORMALIZATION
# ============================================================

def normalize_text(text):
    """
    Normalize text for comparison.
    """

    if text is None:
        return ""

    text = str(text).lower().strip()

    # Normalize common symbols

    text = text.replace(
        "&",
        " and "
    )

    text = text.replace(
        "/",
        " "
    )

    text = text.replace(
        "-",
        " "
    )

    # Normalize whitespace

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# SKILL ALIASES
# ============================================================

SKILL_ALIASES = {

    "python": [
        "python"
    ],

    "java": [
        "java"
    ],

    "c": [
        "c"
    ],

    "c++": [
        "c++",
        "cpp"
    ],

    "javascript": [
        "javascript",
        "js"
    ],

    "html": [
        "html"
    ],

    "css": [
        "css"
    ],

    "react": [
        "react",
        "reactjs"
    ],

    "fastapi": [
        "fastapi"
    ],

    "django": [
        "django"
    ],

    "flask": [
        "flask"
    ],

    "raylib": [
        "raylib"
    ],

    "pandas": [
        "pandas"
    ],

    "numpy": [
        "numpy"
    ],

    "scikit-learn": [
        "scikit-learn",
        "sklearn"
    ],

    "mysql": [
        "mysql"
    ],

    "sqlite": [
        "sqlite"
    ],

    "postgresql": [
        "postgresql",
        "postgres"
    ],

    "sql": [
        "sql"
    ],

    "git": [
        "git"
    ],

    "github": [
        "github",
        "github.com"
    ],

    "docker": [
        "docker"
    ],

    "aws": [
        "aws",
        "amazon web services"
    ],

    "postman": [
        "postman"
    ],

    "vs code": [
        "vs code",
        "visual studio code"
    ],

    "stockfish": [
        "stockfish"
    ],

    "data structures": [
        "data structures",
        "data structure"
    ],

    "algorithms": [
        "algorithms",
        "algorithm"
    ],

    "dsa": [
        "dsa",
        "data structures and algorithms",
        "data structures & algorithms",
        "data structures algorithms"
    ],

    "oop": [
        "oop",
        "object oriented programming",
        "object-oriented programming"
    ],

    "dbms": [
        "dbms",
        "database management system"
    ],

    "os": [
        "os",
        "operating systems",
        "operating system"
    ],

    "computer networks": [
        "computer networks",
        "computer network"
    ],

    "software engineering": [
        "software engineering"
    ],

    "rest api": [
        "rest api",
        "rest apis",
        "restful api",
        "restful apis",
        "rest based api",
        "rest based apis",
        "rest-based api",
        "rest-based apis",
        "rest-based",
    ],

    "backend development": [
        "backend development",
        "backend developer",
        "backend applications",
        "server side development",
        "server-side development"
    ],

    "version control": [
        "version control",
        "version-control"
    ]
}


# ============================================================
# RELATED SKILLS
# ============================================================

RELATED_SKILLS = {

    "django": [
        "fastapi",
        "flask"
    ],

    "fastapi": [
        "django",
        "flask"
    ],

    "postgresql": [
        "mysql",
        "sqlite",
        "sql"
    ],

    "mysql": [
        "postgresql",
        "sqlite",
        "sql"
    ],

    "sqlite": [
        "postgresql",
        "mysql",
        "sql"
    ],

    "sql": [
        "postgresql",
        "mysql",
        "sqlite"
    ],

    "rest api": [
        "fastapi",
        "django",
        "flask"
    ],

    "backend development": [
        "fastapi",
        "django",
        "flask",
        "rest api"
    ],

    "version control": [
        "git",
        "github"
    ],

    "data structures": [
        "dsa",
        "data structures & algorithms"
    ],

    "algorithms": [
        "dsa",
        "data structures & algorithms"
    ]
}


# ============================================================
# REQUIREMENT GROUPS
# ============================================================

REQUIREMENT_GROUPS = {

    "python": {
        "name": "Python",
        "required_skills": [
            "python"
        ]
    },

    "backend_framework": {
        "name": "Backend Framework",
        "required_skills": [
            "fastapi",
            "django",
            "flask"
        ]
    },

    "database_sql": {
        "name": "SQL / Database",
        "required_skills": [
            "postgresql",
            "sql"
        ]
    },

    "containerization": {
        "name": "Containerization",
        "required_skills": [
            "docker"
        ]
    },

    "cloud": {
        "name": "Cloud Platform",
        "required_skills": [
            "aws"
        ]
    },

    "version_control": {
        "name": "Version Control",
        "required_skills": [
            "git",
            "github",
            "version control"
        ]
    },

    "data_structures": {
        "name": "Data Structures",
        "required_skills": [
            "data structures"
        ]
    },

    "algorithms": {
        "name": "Algorithms",
        "required_skills": [
            "algorithms"
        ]
    },

    "rest_api": {
        "name": "REST API",
        "required_skills": [
            "rest api"
        ]
    },

    "skill_backend_development": {
        "name": "Backend Development",
        "required_skills": [
            "backend development"
        ]
    }
}


# ============================================================
# CATEGORY MAP
# ============================================================

CATEGORY_MAP = {

    "programming_languages": [
        "python",
        "java",
        "c",
        "c++",
        "javascript"
    ],

    "backend": [
        "fastapi",
        "django",
        "flask",
        "backend development",
        "rest api"
    ],

    "frontend": [
        "html",
        "css",
        "javascript",
        "react"
    ],

    "databases": [
        "sql",
        "mysql",
        "sqlite",
        "postgresql"
    ],

    "data_science": [
        "numpy",
        "pandas",
        "scikit-learn"
    ],

    "devops_cloud": [
        "docker",
        "aws"
    ],

    "tools": [
        "git",
        "github",
        "postman",
        "vs code"
    ],

    "concepts": [
        "data structures",
        "algorithms",
        "dsa",
        "oop",
        "dbms",
        "os",
        "computer networks",
        "software engineering",
        "version control",
        "rest api",
        "backend development"
    ]
}


# ============================================================
# GET RESUME TEXT
# ============================================================

def get_resume_text(resume):
    """
    Convert the structured resume into one searchable string.
    """

    parts = []

    # --------------------------------------------------------
    # Basic fields
    # --------------------------------------------------------

    for key in [
        "name",
        "email",
        "phone"
    ]:

        value = resume.get(
            key
        )

        if value:

            parts.append(
                str(value)
            )


    # --------------------------------------------------------
    # Main resume arrays
    # --------------------------------------------------------

    for key in [
        "skills",
        "education",
        "experience",
        "projects"
    ]:

        values = resume.get(
            key,
            []
        )

        if isinstance(
            values,
            list
        ):

            parts.extend(
                str(value)
                for value in values
                if value
            )

        elif values:

            parts.append(
                str(values)
            )


    # --------------------------------------------------------
    # Structured sections
    # --------------------------------------------------------

    for section in resume.get(
        "sections",
        []
    ):

        if not isinstance(
            section,
            dict
        ):
            continue


        if section.get(
            "name"
        ):

            parts.append(
                str(
                    section["name"]
                )
            )


        # Section content

        for value in section.get(
            "content",
            []
        ):

            if value:

                parts.append(
                    str(value)
                )


        # Subsections

        for subsection in section.get(
            "subsections",
            []
        ):

            if not isinstance(
                subsection,
                dict
            ):
                continue


            if subsection.get(
                "name"
            ):

                parts.append(
                    str(
                        subsection["name"]
                    )
                )


            for value in subsection.get(
                "content",
                []
            ):

                if value:

                    parts.append(
                        str(value)
                    )


        # Entries

        for entry in section.get(
            "entries",
            []
        ):

            if not isinstance(
                entry,
                dict
            ):
                continue


            if entry.get(
                "title"
            ):

                parts.append(
                    str(
                        entry["title"]
                    )
                )


            for value in entry.get(
                "content",
                []
            ):

                if value:

                    parts.append(
                        str(value)
                    )


    return normalize_text(
        " ".join(parts)
    )


# ============================================================
# TARGETED RESUME EVIDENCE FOR NLP
# ============================================================

def _flatten_resume_chunks(resume):
    """
    Build small, meaningful resume evidence chunks.

    Each chunk keeps its source so the NLP layer can later identify
    where the evidence came from.
    """

    chunks = []

    def add_chunk(text, source):
        if not text:
            return

        text = str(text).strip()

        if not text:
            return

        chunks.append({
            "text": text,
            "source": source
        })

    # --------------------------------------------------------
    # Explicit skills
    # --------------------------------------------------------

    skills = resume.get("skills", [])

    if isinstance(skills, list):
        for skill in skills:
            add_chunk(skill, "skills")

    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    education = resume.get("education", [])

    if isinstance(education, list):
        for item in education:
            add_chunk(item, "education")
    elif education:
        add_chunk(education, "education")

    # --------------------------------------------------------
    # Experience
    # --------------------------------------------------------

    experience = resume.get("experience", [])

    if isinstance(experience, list):
        for item in experience:
            add_chunk(item, "experience")
    elif experience:
        add_chunk(experience, "experience")

    # --------------------------------------------------------
    # Projects
    # --------------------------------------------------------

    projects = resume.get("projects", [])

    if isinstance(projects, list):
        for item in projects:
            add_chunk(item, "projects")
    elif projects:
        add_chunk(projects, "projects")

    # --------------------------------------------------------
    # Structured sections
    # --------------------------------------------------------

    for section in resume.get("sections", []):

        if not isinstance(section, dict):
            continue

        section_name = section.get("name", "")
        section_type = section.get("type", "")

        source = normalize_text(
            section_type or section_name or "section"
        )

        for value in section.get("content", []):

            add_chunk(
                value,
                source
            )

        for subsection in section.get("subsections", []):

            if not isinstance(subsection, dict):
                continue

            subsection_name = subsection.get(
                "name",
                ""
            )

            subsection_source = normalize_text(
                subsection_name or source
            )

            for value in subsection.get(
                "content",
                []
            ):

                add_chunk(
                    value,
                    subsection_source
                )

        for entry in section.get("entries", []):

            if not isinstance(entry, dict):
                continue

            title = entry.get("title")

            if title:
                add_chunk(
                    title,
                    source
                )

            for value in entry.get(
                "content",
                []
            ):

                add_chunk(
                    value,
                    source
                )

    return chunks


def _requirement_terms(requirement_name):
    """
    Convert a requirement name into canonical skill terms and aliases.
    """

    requirement = normalize_text(
        requirement_name
    )

    terms = set()

    # Direct requirement name
    if requirement:
        terms.add(requirement)

    # Requirement group
    for group in REQUIREMENT_GROUPS.values():

        group_name = normalize_text(
            group.get("name", "")
        )

        if group_name == requirement:

            for skill in group.get(
                "required_skills",
                []
            ):

                terms.add(
                    normalize_text(skill)
                )

                for alias in SKILL_ALIASES.get(
                    skill,
                    []
                ):

                    terms.add(
                        normalize_text(alias)
                    )

    # Canonical skill names / aliases
    for canonical, aliases in SKILL_ALIASES.items():

        canonical_normalized = normalize_text(
            canonical
        )

        if (
            canonical_normalized == requirement
            or requirement in [
                normalize_text(alias)
                for alias in aliases
            ]
        ):

            terms.add(
                canonical_normalized
            )

            for alias in aliases:
                terms.add(
                    normalize_text(alias)
                )

    # Known requirement concepts
    requirement_expansions = {

        "backend framework": [
            "fastapi",
            "django",
            "flask",
            "backend",
            "web api"
        ],

        "backend development": [
            "backend",
            "server side",
            "server-side",
            "api",
            "fastapi",
            "django",
            "flask"
        ],

        "rest api": [
            "rest api",
            "rest apis",
            "restful api",
            "restful apis",
            "api"
        ],

        "sql database": [
            "sql",
            "postgresql",
            "postgres",
            "mysql",
            "sqlite",
            "database",
            "databases"
        ],

        "version control": [
            "git",
            "github",
            "version control"
        ],

        "containerization": [
            "docker",
            "container",
            "containers"
        ],

        "cloud platform": [
            "aws",
            "amazon web services",
            "cloud",
            "cloud deployment"
        ],

        "data structures": [
            "data structures",
            "data structure",
            "dsa"
        ],

        "algorithms": [
            "algorithm",
            "algorithms",
            "dsa"
        ]
    }

    for term in requirement_expansions.get(
        requirement,
        []
    ):

        terms.add(
            normalize_text(term)
        )

    return {
        term
        for term in terms
        if term
    }


def _chunk_contains_term(
    chunk_text,
    term
):
    """
    Check whether a chunk contains a meaningful requirement term.
    """

    text = normalize_text(
        chunk_text
    )

    term = normalize_text(
        term
    )

    if not text or not term:
        return False

    # For short terms such as C, use word boundaries.
    pattern = (
        r"(?<!\w)"
        + re.escape(term)
        + r"(?!\w)"
    )

    return re.search(
        pattern,
        text
    ) is not None


def get_targeted_resume_evidence(
    resume,
    requirement_name,
    max_chunks=8
):
    """
    Extract only resume evidence relevant to a requirement.

    Unlike the old implementation, this function does NOT append
    the entire education/projects/experience sections.

    It returns focused chunks that explicitly mention the requirement
    or a known technical relationship.
    """

    chunks = _flatten_resume_chunks(
        resume
    )

    terms = _requirement_terms(
        requirement_name
    )

    requirement = normalize_text(
        requirement_name
    )

    scored = []

    for chunk in chunks:

        chunk_text = chunk["text"]
        normalized_chunk = normalize_text(
            chunk_text
        )

        score = 0

        # ----------------------------------------------------
        # Direct term match
        # ----------------------------------------------------

        for term in terms:

            if _chunk_contains_term(
                normalized_chunk,
                term
            ):

                # Longer/more specific phrases receive more weight.
                score += max(
                    2,
                    len(term.split())
                )


        # ----------------------------------------------------
        # Requirement-specific section preference
        # ----------------------------------------------------

        source = normalize_text(
            chunk["source"]
        )

        if requirement in [
            "backend framework",
            "backend development",
            "rest api"
        ]:

            if source in [
                "projects",
                "experience"
            ]:

                score += 2

        elif requirement in [
            "sql / database"
        ]:

            if source in [
                "projects",
                "experience",
                "databases"
            ]:

                score += 2

        elif requirement in [
            "version control",
            "containerization",
            "cloud platform"
        ]:

            if source in [
                "projects",
                "experience",
                "tools"
            ]:

                score += 2

        elif requirement in [
            "data structures",
            "algorithms",
            "python"
        ]:

            if source in [
                "projects",
                "experience",
                "skills",
                "languages"
            ]:

                score += 1


        # ----------------------------------------------------
        # Keep only evidence with actual relevance.
        # ----------------------------------------------------

        if score > 0:

            scored.append(
                (
                    score,
                    chunk
                )
            )


    # --------------------------------------------------------
    # Sort strongest evidence first.
    # --------------------------------------------------------

    scored.sort(
        key=lambda item: (
            -item[0],
            len(item[1]["text"])
        )
    )


    # --------------------------------------------------------
    # Remove duplicate text.
    # --------------------------------------------------------

    selected = []
    seen = set()

    for score, chunk in scored:

        normalized = normalize_text(
            chunk["text"]
        )

        if normalized in seen:
            continue

        seen.add(
            normalized
        )

        selected.append(
            chunk
        )

        if len(selected) >= max_chunks:
            break


    return selected


def get_targeted_resume_evidence(
    resume,
    requirement_name,
    max_chunks=8
):
    """
    Extract only resume evidence that is actually relevant
    to the requested requirement.

    Evidence must first contain a requirement-related term.
    Section/source preference is applied only AFTER relevance
    has been established.
    """

    chunks = _flatten_resume_chunks(resume)

    terms = _requirement_terms(
        requirement_name
    )

    requirement = normalize_text(
        requirement_name
    )

    scored = []

    for chunk in chunks:

        chunk_text = chunk["text"]

        normalized_chunk = normalize_text(
            chunk_text
        )

        # ----------------------------------------------------
        # 1. Find actual matching terms
        # ----------------------------------------------------

        matched_terms = []

        for term in terms:

            if _chunk_contains_term(
                normalized_chunk,
                term
            ):

                matched_terms.append(
                    term
                )

        # ----------------------------------------------------
        # IMPORTANT:
        # If the chunk contains no relevant term,
        # completely ignore it.
        # ----------------------------------------------------

        if not matched_terms:
            continue

        score = 0

        # ----------------------------------------------------
        # 2. Direct term score
        # ----------------------------------------------------

        for term in matched_terms:

            # Longer phrases are more specific.
            score += max(
                2,
                len(term.split())
            )

        # ----------------------------------------------------
        # 3. Source preference
        #
        # Only applied because the chunk already matched.
        # ----------------------------------------------------

        source = normalize_text(
            chunk["source"]
        )

        if requirement in [
            "backend framework",
            "backend development",
            "rest api"
        ]:

            if source in [
                "projects",
                "experience"
            ]:

                score += 2

        elif requirement in [
            "sql / database"
        ]:

            if source in [
                "projects",
                "experience",
                "databases"
            ]:

                score += 2

        elif requirement in [
            "version control",
            "containerization",
            "cloud platform"
        ]:

            if source in [
                "projects",
                "experience",
                "tools"
            ]:

                score += 2

        elif requirement in [
            "data structures",
            "algorithms",
            "python"
        ]:

            if source in [
                "projects",
                "experience",
                "skills",
                "languages"
            ]:

                score += 1

        # ----------------------------------------------------
        # 4. Store matched evidence
        # ----------------------------------------------------

        scored.append(
            (
                score,
                chunk
            )
        )

    # --------------------------------------------------------
    # Sort strongest evidence first.
    # --------------------------------------------------------

    scored.sort(
        key=lambda item: (
            -item[0],
            len(item[1]["text"])
        )
    )

    # --------------------------------------------------------
    # Remove duplicate text.
    # --------------------------------------------------------

    selected = []

    seen = set()

    for score, chunk in scored:

        normalized = normalize_text(
            chunk["text"]
        )

        if normalized in seen:
            continue

        seen.add(
            normalized
        )

        selected.append(
            chunk
        )

        if len(selected) >= max_chunks:
            break

    return selected


# ============================================================


def extract_resume_skills(resume):

    skills = set()

    # --------------------------------------------------------
    # Explicit skills
    # --------------------------------------------------------

    resume_skills = resume.get(
        "skills",
        []
    )

    if isinstance(
        resume_skills,
        list
    ):

        for skill in resume_skills:

            normalized = normalize_text(
                skill
            )

            if normalized:

                skills.add(
                    normalized
                )


    # --------------------------------------------------------
    # Search complete resume text
    # --------------------------------------------------------

    resume_text = get_resume_text(
        resume
    )


    for canonical, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            alias_normalized = normalize_text(
                alias
            )

            if not alias_normalized:
                continue


            pattern = r"(?<!\w)" + re.escape(
                alias_normalized
            ) + r"(?!\w)"


            if re.search(
                pattern,
                resume_text
            ):

                skills.add(
                    canonical
                )

                break


    return sorted(
        skills
    )

# ============================================================
# EXTRACT RESUME SKILLS
# ============================================================

def extract_resume_skills(resume):
    """Extract resume skills and return canonical, deduplicated skills."""

    skills = set()

    def add_canonical(skill):
        normalized = normalize_text(skill)
        if not normalized:
            return

        for canonical, aliases in SKILL_ALIASES.items():
            terms = {normalize_text(canonical)}
            terms.update(normalize_text(alias) for alias in aliases)

            if normalized in terms:
                if canonical == "dsa":
                    skills.add("data structures")
                    skills.add("algorithms")
                else:
                    skills.add(canonical)
                return

        skills.add(normalized)

    # Explicit skills
    resume_skills = resume.get("skills", [])

    if isinstance(resume_skills, list):
        for skill in resume_skills:
            add_canonical(skill)
    elif resume_skills:
        add_canonical(resume_skills)

    # Search the complete resume for skills that were not explicitly listed.
    resume_text = get_resume_text(resume)

    for canonical, aliases in SKILL_ALIASES.items():
        for alias in [canonical, *aliases]:
            alias_normalized = normalize_text(alias)

            if not alias_normalized:
                continue

            pattern = (
                r"(?<!\w)"
                + re.escape(alias_normalized)
                + r"(?!\w)"
            )

            if re.search(pattern, resume_text):
                if canonical == "dsa":
                    skills.add("data structures")
                    skills.add("algorithms")
                else:
                    skills.add(canonical)
                break

    return sorted(skills)


# ============================================================
# EXTRACT JOB SKILLS
# ============================================================

def extract_job_skills(job_description):

    job_text = normalize_text(
        job_description
    )

    detected = set()


    for canonical, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            alias_normalized = normalize_text(
                alias
            )

            if not alias_normalized:
                continue


            pattern = r"(?<!\w)" + re.escape(
                alias_normalized
            ) + r"(?!\w)"


            if re.search(
                pattern,
                job_text
            ):

                detected.add(
                    canonical
                )

                break


    # --------------------------------------------------------
    # Normalize DSA as a combined concept.
    # DSA should not become a separate independent requirement
    # when Data Structures / Algorithms are already detected.
    # --------------------------------------------------------

    if "dsa" in detected:

        detected.discard("dsa")

        detected.add("data structures")
        detected.add("algorithms")

    return sorted(
        detected
    )


# ============================================================
# FIND EXACT MATCHES
# ============================================================

def find_exact_matches(
    job_skills,
    resume_skills
):

    resume_set = set(
        resume_skills
    )

    return sorted(
        skill
        for skill in job_skills
        if skill in resume_set
    )


# ============================================================
# FIND RELATED MATCHES
# ============================================================

def find_related_matches(
    job_skills,
    resume_skills
):

    matches = []

    resume_set = set(
        resume_skills
    )

    for job_skill in job_skills:

        if job_skill in resume_set:
            continue


        related = RELATED_SKILLS.get(
            job_skill,
            []
        )


        for resume_skill in related:

            if resume_skill in resume_set:

                matches.append(
                    {
                        "job_skill": job_skill,
                        "resume_skill": resume_skill
                    }
                )


    return matches


# ============================================================
# FIND MISSING SKILLS
# ============================================================

def find_missing_skills(
    job_skills,
    resume_skills
):

    resume_set = set(
        resume_skills
    )

    missing = []

    for skill in job_skills:

        if skill in resume_set:
            continue


        related = RELATED_SKILLS.get(
            skill,
            []
        )


        if any(
            related_skill in resume_set
            for related_skill in related
        ):

            continue


        missing.append(
            skill
        )


    return sorted(
        missing
    )


# ============================================================
# RESUME-ONLY SKILLS
# ============================================================

def find_resume_only_skills(
    job_skills,
    resume_skills
):

    job_set = set(
        job_skills
    )

    return sorted(
        skill
        for skill in resume_skills
        if skill not in job_set
    )


# ============================================================
# ANALYZE REQUIREMENT GROUP
# ============================================================

def analyze_requirement_group(
    group,
    resume_skills
):

    required = group.get(
        "required_skills",
        []
    )

    resume_set = set(
        resume_skills
    )


    exact = [
        skill
        for skill in required
        if skill in resume_set
    ]


    related = []

    # Exact evidence is authoritative. Do not also report related
    # alternatives when the requirement group is already exact.
    if not exact:
        for required_skill in required:

            related_skills = RELATED_SKILLS.get(
                required_skill,
                []
            )

            for resume_skill in related_skills:

                if resume_skill in resume_set:

                    related.append(
                        {
                            "job_skill": required_skill,
                            "resume_skill": resume_skill
                        }
                    )

    if exact:

        status = "exact"
        score = 1.0

    elif related:

        status = "related"
        score = 0.5

    else:

        status = "missing"
        score = 0.0


    return {
        "name": group.get(
            "name"
        ),
        "required_skills": required,
        "status": status,
        "matched": exact,
        "related": related,
        "score": score
    }


# ============================================================
# ANALYZE REQUIREMENTS
# ============================================================

def analyze_requirements(
    resume_skills,
    job_skills=None
):
    """
    Analyze only requirement groups that are actually represented
    in the job description.

    This prevents the ATS from scoring a requirement as missing when
    that requirement was never mentioned by the employer.
    """

    requirements = {}

    job_skill_set = set(job_skills or [])

    for key, group in REQUIREMENT_GROUPS.items():

        required_skills = set(
            group.get("required_skills", [])
        )

        # A requirement group is active only when at least one of its
        # canonical required skills was detected in the job description.
        if job_skills is not None and not (
            required_skills & job_skill_set
        ):
            continue

        requirements[key] = analyze_requirement_group(
            group,
            resume_skills
        )

    return requirements


# ============================================================
# JOB / RESUME RESPONSE SUMMARIES
# ============================================================

def extract_preferred_skills(job_description):
    """
    Extract skills from an explicitly labelled Preferred Skills /
    Preferred Qualifications section.

    If the job description does not contain such a section, return [].
    This intentionally does not guess that every non-core skill is
    preferred.
    """

    text = str(job_description or "")

    section_pattern = re.compile(
        r"(?is)"
        r"(?:preferred skills|preferred qualifications|nice to have|"
        r"nice-to-have|bonus skills|preferred)"
        r"\s*:?\s*"
        r"(.*?)"
        r"(?=\\s*(?:required skills|required qualifications|"
        r"requirements|responsibilities|qualifications|"
        r"what we(?:\'re| are) looking for|education|experience)\\s*:?|$)"
    )

    match = section_pattern.search(text)

    if not match:
        return []

    section_text = match.group(1)
    normalized_section = normalize_text(section_text)

    detected = set()

    for canonical, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            alias_normalized = normalize_text(alias)

            if not alias_normalized:
                continue

            pattern = (
                r"(?<!\w)"
                + re.escape(alias_normalized)
                + r"(?!\w)"
            )

            if re.search(
                pattern,
                normalized_section
            ):
                detected.add(canonical)
                break

    return sorted(detected)


def build_job_summary(
    job_description,
    job_skills,
    requirements
):
    """
    Build a clean, frontend-friendly job summary.

    Core requirements are the requirement groups actually detected
    in the job description. Additional detected skills are kept
    separately so they do not silently become scored requirements.
    """

    core_requirements = []

    for requirement_key, requirement in requirements.items():

        core_requirements.append({
            "key": requirement_key,
            "name": requirement.get("name"),
            "required_skills": requirement.get(
                "required_skills",
                []
            )
        })

    # `core_skill_count` represents the number of active scored
    # requirement groups, NOT the number of alternative keywords
    # inside those groups. For example, FastAPI/Django/Flask is
    # one Backend Framework requirement.
    core_skill_count = len(core_requirements)

    core_skill_set = set()

    for requirement in core_requirements:
        core_skill_set.update(
            requirement["required_skills"]
        )

    preferred_skills = extract_preferred_skills(
        job_description
    )

    additional_detected_skills = sorted(
        set(job_skills)
        - core_skill_set
    )

    return {
        "skill_count": len(job_skills),
        "core_skill_count": core_skill_count,
        "core_requirements": core_requirements,
        "preferred_skills": preferred_skills,
        "additional_detected_skills":
            additional_detected_skills
    }


def build_resume_summary(
    resume_skills,
    exact_matches,
    related_matches,
    missing_skills,
    resume_only_skills
):
    """
    Build a clean, frontend-friendly resume summary while retaining
    the existing detailed fields elsewhere in the API response.
    """

    matched_skills = sorted(
        set(
            exact_matches
        )
    )

    related_resume_skills = sorted(
        {
            item.get("resume_skill")
            for item in related_matches
            if item.get("resume_skill")
        }
    )

    return {
        "skill_count": len(resume_skills),
        "skills": resume_skills,
        "matched_skills": matched_skills,
        "related_skills": related_resume_skills,
        "missing_skills": missing_skills,
        "resume_only_skills": resume_only_skills
    }


# ============================================================
# REMOVE RELATED MATCHES WHEN A REQUIREMENT GROUP IS EXACT
# ============================================================

def filter_related_matches_by_requirements(
    related_matches,
    requirements
):
    """
    Remove related matches belonging to a requirement group that is
    already satisfied exactly.

    Example:
        Backend Framework = exact via FastAPI
        Django -> FastAPI must not be reported as related.

        Version Control = exact via Git/GitHub
        version control -> Git/GitHub must not be reported as related.
    """

    exact_group_skills = set()

    for requirement in requirements.values():

        if requirement.get("status") != "exact":
            continue

        exact_group_skills.update(
            normalize_text(skill)
            for skill in requirement.get("required_skills", [])
            if skill
        )

    return [
        item
        for item in related_matches
        if normalize_text(item.get("job_skill", ""))
        not in exact_group_skills
    ]


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

def analyze_categories(
    job_skills,
    resume_skills,
    requirements
):

    result = {}


    for category, category_skills in CATEGORY_MAP.items():

        job_category_skills = [
            skill
            for skill in job_skills
            if skill in category_skills
        ]


        resume_category_skills = [
            skill
            for skill in resume_skills
            if skill in category_skills
        ]


        exact = [
            skill
            for skill in job_category_skills
            if skill in resume_category_skills
        ]

        # Version control is a concept represented by Git/GitHub.
        # Treat Git or GitHub as an exact category-level match for
        # a job requirement that explicitly asks for version control.
        if "version control" in job_category_skills:

            if (
                "version control" not in exact
                and (
                    "git" in resume_skills
                    or "github" in resume_skills
                )
            ):
                exact.append("version control")


        # If a requirement group is exact, every skill in that group
        # is considered satisfied for category-level reporting.
        exact_group_skills = set()

        for requirement in requirements.values():

            if requirement.get("status") == "exact":

                exact_group_skills.update(
                    normalize_text(skill)
                    for skill in requirement.get("required_skills", [])
                    if skill
                )

        related = []


        for job_skill in job_category_skills:

            if normalize_text(job_skill) in exact_group_skills:
                continue

            if job_skill in exact:
                continue


            related_skills = RELATED_SKILLS.get(
                job_skill,
                []
            )


            for resume_skill in related_skills:

                if resume_skill in resume_category_skills:

                    related.append(
                        {
                            "job_skill": job_skill,
                            "resume_skill": resume_skill
                        }
                    )


        missing = [
            skill
            for skill in job_category_skills
            if (
                skill not in exact
                and not any(
                    item["job_skill"] == skill
                    for item in related
                )
            )
        ]


        result[category] = {

            "job_skills": job_category_skills,

            "resume_skills": resume_category_skills,

            "exact_matches": exact,

            "related_matches": related,

            "missing_skills": missing
        }


    return result



# ============================================================
# HYBRID SEMANTIC SCORE
# ============================================================

def calculate_hybrid_score(
    ats_status,
    semantic_classification,
    semantic_score,
    requirement_name="",
    required_skills=None
):
    """
    Combine deterministic ATS matching with semantic similarity.

    Rules:
    - Exact skill evidence is authoritative: 1.00
    - Related matches receive partial credit.
    - Semantic similarity can strengthen a related match,
      but cannot make a different technology equivalent.
    - Missing requirements only receive partial semantic credit
      when actual resume evidence exists.
    """

    required_skills = required_skills or []

    # --------------------------------------------------------
    # Exact match
    # --------------------------------------------------------

    if ats_status == "exact":
        return 1.0

    # --------------------------------------------------------
    # Related match
    # --------------------------------------------------------

    if ats_status == "related":

        # Technology-specific requirements should be conservative.
        # Example:
        # PostgreSQL != MySQL
        # Django != FastAPI
        # AWS != Docker
        technology_specific = any(
            skill in {
                "postgresql",
                "mysql",
                "sqlite",
                "django",
                "fastapi",
                "flask",
                "aws",
                "docker"
            }
            for skill in required_skills
        )

        if technology_specific:

            if semantic_classification == "strong":
                return 0.60

            if semantic_classification == "related":
                return 0.50

            if semantic_classification == "weak":
                return 0.35

            return 0.25

        # General requirements can receive more benefit from
        # semantic similarity.
        if semantic_classification == "strong":
            return 0.85

        if semantic_classification == "related":
            return 0.65

        if semantic_classification == "weak":
            return 0.45

        return 0.25

    # --------------------------------------------------------
    # Missing requirement
    # --------------------------------------------------------

    if ats_status == "missing":

        # No evidence means no credit.
        if semantic_score <= 0:
            return 0.0

        if semantic_classification == "strong":
            return 0.35

        if semantic_classification == "related":
            return 0.20

        if semantic_classification == "weak":
            return 0.10

        return 0.0

    return 0.0


def calculate_hybrid_ats_score(
    semantic_targets
):
    """
    Calculate the final ATS score using the hybrid scores
    generated for each requirement.
    """

    if not semantic_targets:
        return 0

    total = 0.0

    for target in semantic_targets.values():

        total += target.get(
            "hybrid_score",
            0.0
        )

    score = (
        total /
        len(semantic_targets)
    ) * 100

    return round(score)


# ============================================================
# ATS SCORE
# ============================================================

def calculate_ats_score(
    requirements
):

    if not requirements:

        return 0


    total = 0.0

    for requirement in requirements.values():

        total += requirement.get(
            "score",
            0.0
        )


    score = (
        total
        /
        len(requirements)
    ) * 100


    return round(
        score
    )


# ============================================================
# RECOMMENDATIONS
# ============================================================

def generate_recommendations(
    ats_score,
    requirements,
    resume_only_skills
):

    recommendations = []


    if ats_score >= 80:

        recommendations.append(
            "Your resume has a strong match with the detected job requirements."
        )

    elif ats_score >= 60:

        recommendations.append(
            "Your resume has a moderate-to-strong match with the detected job requirements."
        )

    elif ats_score >= 40:

        recommendations.append(
            "Your resume has a limited technical match with this job description."
        )

    else:

        recommendations.append(
            "Your resume currently has a low technical match with this job description."
        )


    missing_names = []

    for requirement in requirements.values():

        if requirement.get(
            "status"
        ) == "missing":

            missing_names.append(
                requirement.get(
                    "name"
                )
            )


    if missing_names:

        recommendations.append(
            "Missing requirements: "
            + ", ".join(
                missing_names
            )
            + ". Add them only if you genuinely have experience with them."
        )


    for requirement in requirements.values():

        if requirement.get(
            "status"
        ) == "related":

            name = requirement.get(
                "name"
            )

            related = requirement.get(
                "related",
                []
            )


            for item in related:

                recommendations.append(
                    f"{name} is not an exact match, but your resume contains related experience with "
                    f"{item['resume_skill'].title()}."
                )


    if resume_only_skills:

        recommendations.append(
            "Your resume contains many skills not directly detected in this job description. "
            "Prioritize the most relevant skills."
        )


    # Remove duplicate recommendations while preserving order
    recommendations = list(
        dict.fromkeys(recommendations)
    )

    return recommendations


# ============================================================
# TARGETED NLP TEST
# ============================================================

def test_targeted_resume_text(
    resume
):

    print("\n")
    print("=" * 70)
    print("TARGETED RESUME TEXT TEST")
    print("=" * 70)


    test_requirements = [

        "Python",

        "Backend Framework",

        "REST API",

        "SQL / Database",

        "Data Structures",

        "Version Control",

        "Cloud Platform"

    ]


    for requirement in test_requirements:

        evidence = get_targeted_resume_evidence(
            resume,
            requirement
        )

        targeted_text = normalize_text(
            " ".join(
                item["text"]
                for item in evidence
            )
        )

        print("\nRequirement:")
        print(
            requirement
        )

        print("\nEvidence:")

        if evidence:

            for item in evidence:

                print(
                    f"[{item['source']}] {item['text']}"
                )

        else:

            print(
                "No relevant resume evidence found."
            )

        print("\nTargeted Resume Text:")

        print(
            targeted_text
        )

        print("-" * 70)


# ============================================================
# MAIN ATS ANALYZER
# ============================================================

def analyze_ats(
    resume,
    job_description
):

    # --------------------------------------------------------
    # Extract skills
    # --------------------------------------------------------

    resume_skills = extract_resume_skills(
        resume
    )


    job_skills = extract_job_skills(
        job_description
    )


    # --------------------------------------------------------
    # Matches
    # --------------------------------------------------------

    exact_matches = find_exact_matches(
        job_skills,
        resume_skills
    )


    related_matches = find_related_matches(
        job_skills,
        resume_skills
    )


    missing_skills = find_missing_skills(
        job_skills,
        resume_skills
    )


    resume_only_skills = find_resume_only_skills(
        job_skills,
        resume_skills
    )


    # --------------------------------------------------------
    # Requirement groups
    # --------------------------------------------------------

    requirements = analyze_requirements(
        resume_skills,
        job_skills
    )


    # Remove related matches that belong to an already-exact
    # requirement group.
    related_matches = filter_related_matches_by_requirements(
        related_matches,
        requirements
    )


    # --------------------------------------------------------
    # Categories
    # --------------------------------------------------------

    categories = analyze_categories(
        job_skills,
        resume_skills,
        requirements
    )


    # --------------------------------------------------------
    # TARGETED NLP + SEMANTIC MATCHING
    # --------------------------------------------------------

    semantic_targets = {}

    for requirement_key, requirement in requirements.items():

        requirement_name = requirement.get(
            "name"
        )

        # ----------------------------------------------------
        # Find targeted resume evidence
        # ----------------------------------------------------

        evidence = get_targeted_resume_evidence(
            resume,
            requirement_name
        )

        # ----------------------------------------------------
        # For exact ATS matches, prioritize evidence that contains
        # the actual matched skill. This keeps semantic explanations
        # focused instead of embedding unrelated technologies from
        # the same project/framework list.
        # ----------------------------------------------------

        if requirement.get("status") == "exact":

            matched_exact_skills = [
                normalize_text(skill)
                for skill in requirement.get("matched", [])
                if skill
            ]

            exact_evidence = [
                item
                for item in evidence
                if any(
                    _chunk_contains_term(
                        normalize_text(item.get("text", "")),
                        skill
                    )
                    for skill in matched_exact_skills
                )
            ]

            if exact_evidence:
                # Prefer direct skill evidence over broad project/library
                # lists. This keeps semantic explanations focused.
                source_priority = {
                    "skills": 0,
                    "tools": 1,
                    "languages": 2,
                    "frameworks libraries": 3,
                    "databases": 3,
                    "projects": 4,
                    "experience": 4
                }

                exact_evidence.sort(
                    key=lambda item: (
                        source_priority.get(
                            normalize_text(item.get("source", "")),
                            5
                        ),
                        len(item.get("text", ""))
                    )
                )

                # One or two direct pieces of evidence are normally
                # sufficient for an exact technical match.
                evidence = exact_evidence[:2]

        # ----------------------------------------------------
        # Build a technology-aware semantic query
        # ----------------------------------------------------
        # A generic requirement-group name such as 'Backend Framework'
        # is not a good embedding query when the actual technology is
        # FastAPI, Django, or Flask. Prefer the concrete requirement.

        semantic_query = requirement_name

        matched_skills = [
            normalize_text(skill)
            for skill in requirement.get("matched", [])
            if skill
        ]

        if matched_skills:
            semantic_query = matched_skills[0]

        elif requirement.get("status") == "related":
            related_items = requirement.get("related", [])

            if related_items:
                semantic_query = normalize_text(
                    related_items[0].get(
                        "job_skill",
                        requirement_name
                    )
                )

        elif requirement.get("status") == "missing":
            required_skills = [
                normalize_text(skill)
                for skill in requirement.get(
                    "required_skills",
                    []
                )
                if skill
            ]

            if required_skills:
                semantic_query = required_skills[0]

        # ----------------------------------------------------
        # Run semantic matching
        # ----------------------------------------------------

        semantic_result = analyze_requirement_semantically(
            semantic_query,
            evidence
        )

        # ----------------------------------------------------
        # Combine ATS matching + semantic matching
        # ----------------------------------------------------

        ats_status = requirement.get(
            "status",
            "missing"
        )

        semantic_classification = semantic_result[
            "classification"
        ]

        semantic_score = semantic_result[
            "similarity"
        ]

        hybrid_score = calculate_hybrid_score(
            ats_status,
            semantic_classification,
            semantic_score,
            requirement_name,
            requirement.get(
                "required_skills",
                []
            )
        )


        # Exact ATS match always has strong evidence
        if ats_status == "exact":

            final_classification = "strong"


        # Related ATS match uses semantic evidence
        elif ats_status == "related":

            if semantic_classification == "strong":

                final_classification = "strong"

            elif semantic_classification == "related":

                final_classification = "related"

            else:

                final_classification = "weak"


        # Missing requirement
        else:

            if evidence and semantic_score >= 0.60:

                final_classification = "related"

            else:

                final_classification = "unrelated"

        # ----------------------------------------------------
        # Store complete NLP result
        # ----------------------------------------------------

        semantic_targets[requirement_key] = {

            "requirement":
                requirement_name,

            "semantic_query":
                semantic_query,

            "targeted_resume_text":
                normalize_text(
                    " ".join(
                        item["text"]
                        for item in evidence
                    )
                ),

            "evidence":
                evidence,

            "similarity":
                semantic_result["similarity"],

            "classification":
                semantic_result["classification"],

            "best_match":
                semantic_result["best_match"],

            "resume_evidence":
                semantic_result["resume_evidence"],

            "ats_status":
                ats_status,

            "semantic_classification":
                semantic_classification,

            "final_classification":
                final_classification,

            "hybrid_score":
                hybrid_score
        }


    # --------------------------------------------------------
    # FINAL HYBRID ATS SCORE
    # --------------------------------------------------------

    ats_score = calculate_hybrid_ats_score(
        semantic_targets
    )


    # --------------------------------------------------------
    # Recommendations
    # --------------------------------------------------------

    recommendations = generate_recommendations(
        ats_score,
        requirements,
        resume_only_skills
    )


    # --------------------------------------------------------
    # Clean frontend-friendly summaries
    # --------------------------------------------------------

    job_summary = build_job_summary(
        job_description,
        job_skills,
        requirements
    )

    resume_summary = build_resume_summary(
        resume_skills,
        exact_matches,
        related_matches,
        missing_skills,
        resume_only_skills
    )


    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {

        "ats_score": ats_score,

        # ----------------------------------------------------
        # New clean summary structure
        # ----------------------------------------------------

        "job": job_summary,

        "resume": resume_summary,

        # ----------------------------------------------------
        # Backward-compatible fields
        # ----------------------------------------------------

        "job_skill_count":
            len(job_skills),

        "resume_skill_count":
            len(resume_skills),

        "detected_job_skills":
            job_skills,

        "requirements":
            requirements,

        "exact_matches": [

            {
                "requirement":
                    skill.title(),

                "matched": [
                    skill
                ]
            }

            for skill in exact_matches
        ],

        "related_matches":
            related_matches,

        "missing_requirements": [

            {
                "requirement":
                    skill.title(),

                "expected": [
                    skill
                ]
            }

            for skill in missing_skills
        ],

        "resume_only_skills":
            resume_only_skills,

        "semantic_targets":
            semantic_targets,

        "categories":
            categories,

        "recommendations":
            recommendations
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    sample_resume = {

        "name":
            "ABHAY SHARMA",

        "email":
            "abhay@example.com",

        "phone":
            "+91 XXXXX XXXXX",

        "skills": [

            "Python",

            "C++",

            "Java",

            "JavaScript",

            "HTML",

            "CSS",

            "React",

            "FastAPI",

            "Pandas",

            "NumPy",

            "scikit-learn",

            "MySQL",

            "SQLite",

            "Git",

            "GitHub",

            "Postman",

            "VS Code",

            "Data Structures",

            "Algorithms",

            "OOP",

            "DBMS",

            "Computer Networks",

            "Software Engineering"
        ],

        "education": [

            "B.Tech / B.E. in Computer Science & Engineering",

            "ABC Institute of Technology, India",

            "2023 – 2027",

            "CGPA: 8.2/10"
        ],

        "experience": [

            "Supervisor | Dream Beauty Fashion Volmo | 6 months",

            "• Supervised daily operations, coordinated staff activities, maintained records, and supported customer service.",

            "Sales Executive | Utkarsh Small Finance Bank | 9 months",

            "• Handled customer interactions, explained banking products, supported sales activities."
        ],

        "projects": [

            "Smart Task Management System — Python, FastAPI, SQLite, HTML/CSS/JS",

            "• Built a REST-based task management application with user authentication, task CRUD operations, filtering, and a responsive frontend.",

            "Chess Game with AI — C++, Raylib, Stockfish",

            "• Developed a desktop chess game with graphical UI and Stockfish-based computer opponent integration."
        ],

        "sections": [

            {
                "name":
                    "technical skills",

                "type":
                    "skills",

                "subsections": [

                    {
                        "name":
                            "languages",

                        "content": [
                            "C++, Java, Python, JavaScript, HTML, CSS"
                        ]
                    },

                    {
                        "name":
                            "frameworks libraries",

                        "content": [
                            "FastAPI, React, Raylib, Pandas, NumPy, scikit-learn"
                        ]
                    },

                    {
                        "name":
                            "databases",

                        "content": [
                            "MySQL, SQLite"
                        ]
                    },

                    {
                        "name":
                            "tools",

                        "content": [
                            "Git, GitHub, VS Code, Postman"
                        ]
                    }
                ],

                "entries": [],

                "content": []
            },

            {
                "name":
                    "projects",

                "type":
                    "projects",

                "subsections": [],

                "entries": [

                    {
                        "title":
                            "Smart Task Management System — Python, FastAPI, SQLite",

                        "content": [

                            "• Built a REST-based task management application."
                        ]
                    }
                ],

                "content": []
            },

            {
                "name":
                    "experience",

                "type":
                    "experience",

                "subsections": [],

                "entries": [

                    {
                        "title":
                            "Supervisor | Dream Beauty Fashion Volmo | 6 months",

                        "content": [

                            "• Supervised daily operations."
                        ]
                    }
                ],

                "content": []
            }
        ]
    }


    sample_job_description = """
    Python Backend Developer

    Requirements:

    Strong Python programming skills.
    Experience with FastAPI or Django.
    REST API development.
    SQL and PostgreSQL.
    Git and GitHub.
    Docker.
    AWS.
    Knowledge of data structures and algorithms.
    Backend development.
    Version control.
    """


    # --------------------------------------------------------
    # Run ATS analysis
    # --------------------------------------------------------

    result = analyze_ats(
        sample_resume,
        sample_job_description
    )


    # --------------------------------------------------------
    # Print ATS result
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("ATS RESULT")
    print("=" * 70)

    print(
        result
    )


    # --------------------------------------------------------
    # Test targeted NLP text
    # --------------------------------------------------------

    test_targeted_resume_text(
        sample_resume
    )
