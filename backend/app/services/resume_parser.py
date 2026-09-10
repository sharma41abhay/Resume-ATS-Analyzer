import re


# ============================================================
# 1. SKILLS DATABASE
# ============================================================

SKILLS_DATABASE = [

    # Programming Languages
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",

    # Frameworks / Libraries
    "react",
    "node.js",
    "fastapi",
    "django",
    "flask",
    "raylib",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",

    # Databases
    "sql",
    "mysql",
    "sqlite",
    "postgresql",
    "mongodb",

    # Tools
    "git",
    "github",
    "docker",
    "postman",
    "vs code",

    # Cloud
    "aws",

    # Concepts
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data structures & algorithms",
    "object oriented programming",
    "oop",
    "dbms",
    "operating systems",
    "os",
    "computer networks",
    "software engineering",

    # Other
    "stockfish",
]


# ============================================================
# 2. KNOWN SECTION NAMES
# ============================================================

SECTION_NAMES = {

    "summary": [
        "summary",
        "professional summary",
        "profile",
        "profile summary",
        "career objective",
        "objective",
        "career profile",
    ],

    "education": [
        "education",
        "academic background",
        "educational qualification",
        "academic qualifications",
    ],

    "skills": [
        "skills",
        "technical skills",
        "technical skill",
        "core skills",
        "key skills",
        "technical profile",
        "technologies",
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "major projects",
        "project experience",
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "employment history",
        "work history",
        "internship",
        "internships",
    ],

    "certifications": [
        "certifications",
        "certificates",
        "certification",
        "professional certifications",
    ],

    "achievements": [
        "achievements",
        "accomplishments",
        "awards",
        "honors",
        "honours",
    ],

    "strengths": [
        "strengths",
        "key strengths",
        "core strengths",
    ],

    "languages": [
        "languages",
        "language proficiency",
        "known languages",
    ],

    "interests": [
        "interests",
        "hobbies",
        "hobbies and interests",
    ],

    "references": [
        "references",
        "referees",
    ],

    "declaration": [
        "declaration",
        "declarations",
    ],
}


# ============================================================
# 3. NORMALIZE TEXT
# ============================================================

def normalize_text(text: str):

    text = text.lower().strip()

    text = text.replace(
        "&",
        " and "
    )

    text = re.sub(
        r"[:\-/_,]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# 4. CLASSIFY SECTION
# ============================================================

def classify_known_section(section_name: str):

    normalized = normalize_text(
        section_name
    )

    for category, names in SECTION_NAMES.items():

        for name in names:

            if normalize_text(name) == normalized:

                return category

    # Combined section
    if (
        "certification" in normalized
        and "achievement" in normalized
    ):
        return "certifications_and_achievements"

    return None


# ============================================================
# 5. CHECK KNOWN SKILL
# ============================================================

def is_known_skill(line: str):

    normalized_line = normalize_text(
        line
    )

    for skill in SKILLS_DATABASE:

        if normalize_text(skill) == normalized_line:

            return True

    return False


# ============================================================
# 6. CLEAN TEXT
# ============================================================

def clean_text(text: str):

    text = text.replace(
        "\r",
        ""
    )

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


# ============================================================
# 7. EXTRACT EMAIL
# ============================================================

def extract_email(text: str):

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(
        pattern,
        text
    )

    if match:
        return match.group()

    return None


# ============================================================
# 8. EXTRACT PHONE
# ============================================================

def extract_phone(text: str):

    pattern = r'(?<!\d)\+?\d[\d\s\-]{8,14}\d'

    match = re.search(
        pattern,
        text
    )

    if not match:
        return None

    phone = match.group().strip()

    digits = re.sub(
        r"\D",
        "",
        phone
    )

    if 10 <= len(digits) <= 15:

        return phone

    return None


# ============================================================
# 9. EXTRACT NAME
# ============================================================

def extract_name(lines):

    if not lines:
        return None

    for line in lines:

        text = line["text"].strip()

        if text:

            return text

    return None


# ============================================================
# 10. EXTRACT SKILLS
# ============================================================

def extract_skills(text: str):

    lower_text = text.lower()

    found_skills = []

    # Search longer skills first.
    sorted_skills = sorted(
        SKILLS_DATABASE,
        key=len,
        reverse=True
    )

    for skill in sorted_skills:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )

        if not re.search(
            pattern,
            lower_text
        ):
            continue

        overlapping = False

        for existing in found_skills:

            if (
                skill.lower()
                in existing.lower()
            ):

                overlapping = True
                break

        if not overlapping:

            found_skills.append(
                skill
            )

    # Return in database order
    final_skills = []

    for skill in SKILLS_DATABASE:

        if skill in found_skills:

            final_skills.append(
                skill
            )

    return final_skills


# ============================================================
# 11. EDUCATION DETAIL DETECTION
# ============================================================

def is_education_detail(text):

    text = text.strip().lower()

    # --------------------------------------------------------
    # Year range
    #
    # 2023 - 2027
    # 2023 – 2027
    # 2023 — 2027
    # 2023 to 2027
    # --------------------------------------------------------

    if re.fullmatch(
        r"\d{4}\s*(?:-|–|—|to)\s*\d{4}",
        text
    ):

        return True

    # --------------------------------------------------------
    # Single year
    # --------------------------------------------------------

    if re.fullmatch(
        r"\d{4}",
        text
    ):

        return True

    # --------------------------------------------------------
    # CGPA / GPA
    # --------------------------------------------------------

    if re.search(
        r"\b(?:cgpa|gpa)\b",
        text
    ):

        return True

    # --------------------------------------------------------
    # Percentage
    # --------------------------------------------------------

    if (
        "percentage" in text
        or "%" in text
        or "percent" in text
    ):

        return True

    # --------------------------------------------------------
    # Marks
    # --------------------------------------------------------

    if "marks" in text:

        return True

    return False


# ============================================================
# 12. MAIN SECTION DETECTION
# ============================================================

def is_main_section(line):

    text = line["text"].strip()

    if not text:
        return False

    if is_known_skill(text):

        return False

    if not line.get(
        "is_bold",
        False
    ):

        return False

    font_size = line["font_size"]

    # Main headings in the sample are 11.5 pt.
    if font_size >= 10.5:

        return True

    return False


# ============================================================
# 13. SUBSECTION DETECTION
# ============================================================

def is_subsection(line):

    text = line["text"].strip()

    if not text:
        return False

    if is_known_skill(text):

        return False

    if not line.get(
        "is_bold",
        False
    ):

        return False

    font_size = line["font_size"]

    # Technical-skill subsections are around 8.5 pt.
    #
    # 9.2 pt education entries must NOT be classified
    # as subsections.
    if 7.5 <= font_size < 9.0:

        return True

    return False


# ============================================================
# 14. ENTRY / TITLE DETECTION
# ============================================================

def is_entry_title(line):

    text = line["text"].strip()

    if not text:
        return False

    if is_main_section(line):

        return False

    if is_subsection(line):

        return False

    if not line.get(
        "is_bold",
        False
    ):

        return False

    # --------------------------------------------------------
    # Education details are NOT new entries
    # --------------------------------------------------------

    if is_education_detail(text):

        return False

    font_size = line["font_size"]

    # Project / experience / education titles
    if 9.0 <= font_size < 10.5:

        return True

    return False


# ============================================================
# 15. EXTRACT HIERARCHICAL RESUME STRUCTURE
# ============================================================

def extract_resume_structure(lines):

    sections = []

    current_section = None
    current_subsection = None
    current_entry = None

    meaningful_index = 0

    for line in lines:

        text = line["text"].strip()

        if not text:
            continue

        # ----------------------------------------------------
        # First meaningful line is usually the candidate name.
        # ----------------------------------------------------

        if meaningful_index == 0:

            meaningful_index += 1

            continue

        meaningful_index += 1

        # ====================================================
        # MAIN SECTION
        # ====================================================

        if is_main_section(line):

            section_name = normalize_text(
                text
            )

            section_type = classify_known_section(
                section_name
            )

            current_section = {

                "name": section_name,

                "type": section_type,

                "subsections": [],

                "entries": [],

                "content": []
            }

            sections.append(
                current_section
            )

            current_subsection = None
            current_entry = None

            continue

        # ----------------------------------------------------
        # Ignore text before first main section
        # ----------------------------------------------------

        if current_section is None:

            continue

        # ====================================================
        # SUBSECTION
        # ====================================================

        if is_subsection(line):

            subsection = {

                "name": normalize_text(
                    text
                ),

                "content": []
            }

            current_section[
                "subsections"
            ].append(
                subsection
            )

            current_subsection = subsection

            current_entry = None

            continue

        # ====================================================
        # ENTRY / TITLE
        # ====================================================

        if is_entry_title(line):

            entry = {

                "title": text,

                "content": []
            }

            current_section[
                "entries"
            ].append(
                entry
            )

            current_entry = entry

            current_subsection = None

            continue

        # ====================================================
        # NORMAL CONTENT
        # ====================================================

        if current_subsection is not None:

            current_subsection[
                "content"
            ].append(
                text
            )

        elif current_entry is not None:

            current_entry[
                "content"
            ].append(
                text
            )

        else:

            current_section[
                "content"
            ].append(
                text
            )

    return sections


# ============================================================
# 16. EXTRACT EDUCATION
# ============================================================

def extract_education_from_structure(
    sections
):

    education = []

    for section in sections:

        if section["type"] != "education":

            continue

        for entry in section[
            "entries"
        ]:

            education.append(
                entry["title"]
            )

            education.extend(
                entry["content"]
            )

        education.extend(
            section["content"]
        )

    return education


# ============================================================
# 17. EXTRACT EXPERIENCE
# ============================================================

def extract_experience_from_structure(
    sections
):

    experience = []

    for section in sections:

        if section["type"] != "experience":

            continue

        for entry in section[
            "entries"
        ]:

            experience.append(
                entry["title"]
            )

            experience.extend(
                entry["content"]
            )

        experience.extend(
            section["content"]
        )

    return experience


# ============================================================
# 18. EXTRACT PROJECTS
# ============================================================

def extract_projects_from_structure(
    sections
):

    projects = []

    for section in sections:

        if section["type"] != "projects":

            continue

        for entry in section[
            "entries"
        ]:

            projects.append(
                entry["title"]
            )

            projects.extend(
                entry["content"]
            )

        projects.extend(
            section["content"]
        )

    return projects


# ============================================================
# 19. EXTRACT SKILLS
# ============================================================

def extract_skills_from_structure(
    sections
):

    skill_text = []

    for section in sections:

        if section["type"] != "skills":

            continue

        # Direct section content
        skill_text.extend(
            section["content"]
        )

        # Subsections
        for subsection in section[
            "subsections"
        ]:

            skill_text.extend(
                subsection["content"]
            )

        # Entries
        for entry in section[
            "entries"
        ]:

            skill_text.append(
                entry["title"]
            )

            skill_text.extend(
                entry["content"]
            )

    combined_text = "\n".join(
        skill_text
    )

    return extract_skills(
        combined_text
    )


# ============================================================
# 20. MAIN RESUME PARSER
# ============================================================

def parse_resume_with_layout(
    text,
    pdf_lines
):

    # --------------------------------------------------------
    # Clean extracted text
    # --------------------------------------------------------

    text = clean_text(
        text
    )

    # --------------------------------------------------------
    # Candidate name
    # --------------------------------------------------------

    name = extract_name(
        pdf_lines
    )

    # --------------------------------------------------------
    # Build hierarchical structure
    # --------------------------------------------------------

    sections = extract_resume_structure(
        pdf_lines
    )

    # --------------------------------------------------------
    # Extract standard fields
    # --------------------------------------------------------

    education = (
        extract_education_from_structure(
            sections
        )
    )

    experience = (
        extract_experience_from_structure(
            sections
        )
    )

    projects = (
        extract_projects_from_structure(
            sections
        )
    )

    skills = (
        extract_skills_from_structure(
            sections
        )
    )

    # --------------------------------------------------------
    # Skill fallback
    # --------------------------------------------------------

    if not skills:

        skills = extract_skills(
            text
        )

    # --------------------------------------------------------
    # Final resume object
    # --------------------------------------------------------

    resume = {

        "name": name,

        "email": extract_email(
            text
        ),

        "phone": extract_phone(
            text
        ),

        "skills": skills,

        "education": education,

        "experience": experience,

        "projects": projects,

        "sections": sections
    }

    return resume


# ============================================================
# 21. LOCAL TEST
# ============================================================

if __name__ == "__main__":

    sample_lines = [

        # ====================================================
        # NAME
        # ====================================================

        {
            "text": "ABHAY SHARMA",
            "font_size": 22.0,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        # ====================================================
        # SUBTITLE
        # ====================================================

        {
            "text": "Computer Science & Engineering Student",
            "font_size": 10.0,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # CONTACT
        # ====================================================

        {
            "text": "Phone: +91 9876543210 | Email: abhay@example.com",
            "font_size": 9.0,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # CAREER OBJECTIVE
        # ====================================================

        {
            "text": "CAREER OBJECTIVE",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Motivated Computer Science undergraduate seeking an internship.",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # EDUCATION
        # ====================================================

        {
            "text": "EDUCATION",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "B.Tech / B.E. in Computer Science & Engineering",
            "font_size": 9.2,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "ABC Institute of Technology, India",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "2023 – 2027",
            "font_size": 9.2,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "CGPA: 8.2/10",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "Higher Secondary (12th)",
            "font_size": 9.2,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "XYZ Senior Secondary School",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "2023",
            "font_size": 9.2,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Percentage: 82%",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # TECHNICAL SKILLS
        # ====================================================

        {
            "text": "TECHNICAL SKILLS",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Languages",
            "font_size": 8.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "C++, Java, Python, JavaScript, HTML, CSS",
            "font_size": 8.5,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "Frameworks / Libraries",
            "font_size": 8.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "FastAPI, React, Raylib, Pandas, NumPy, scikit-learn",
            "font_size": 8.5,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "Databases",
            "font_size": 8.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "MySQL, SQLite",
            "font_size": 8.5,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "Tools",
            "font_size": 8.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Git, GitHub, VS Code, Postman",
            "font_size": 8.5,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        {
            "text": "Core Concepts",
            "font_size": 8.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Data Structures & Algorithms, OOP, DBMS, OS, Computer Networks, Software Engineering",
            "font_size": 8.5,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # PROJECTS
        # ====================================================

        {
            "text": "PROJECTS",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Smart Task Management System — Python, FastAPI, SQLite",
            "font_size": 9.5,
            "fonts": [
                "Helvetica-Bold",
                "Helvetica",
                "Helvetica-Oblique"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "• Built a REST-based task management application.",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # EXPERIENCE
        # ====================================================

        {
            "text": "EXPERIENCE",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Software Developer Intern | ABC Company",
            "font_size": 9.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "• Developed backend applications.",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # CERTIFICATIONS
        # ====================================================

        {
            "text": "CERTIFICATIONS & ACHIEVEMENTS",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "• Completed Python coursework.",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        },

        # ====================================================
        # STRENGTHS
        # ====================================================

        {
            "text": "STRENGTHS",
            "font_size": 11.5,
            "fonts": [
                "Helvetica-Bold"
            ],
            "is_bold": True,
            "page": 0
        },

        {
            "text": "Problem Solving • Teamwork • Communication",
            "font_size": 9.2,
            "fonts": [
                "Helvetica"
            ],
            "is_bold": False,
            "page": 0
        }
    ]


    # ========================================================
    # RUN TEST
    # ========================================================

    sample_text = "\n".join(
        line["text"]
        for line in sample_lines
    )

    result = parse_resume_with_layout(
        sample_text,
        sample_lines
    )

    import pprint

    pprint.pprint(
        result,
        sort_dicts=False
    )