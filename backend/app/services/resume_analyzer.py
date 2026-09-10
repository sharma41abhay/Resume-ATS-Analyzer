# ============================================================
# RESUME ANALYZER
# ============================================================
#
# Pipeline:
#
# PDF
#   ↓
# pdf_parser.py
#   ↓
# resume_parser.py
#   ↓
# resume_analyzer.py
#   ↓
# Resume Score + Warnings + Suggestions
#
# Scoring:
#
# Contact Information   10%
# Completeness           20%
# Content Quality        25%
# Skills Quality         15%
# Projects Quality       15%
# Experience Quality     15%
#
# Total                  100%
# ============================================================


import re


# ============================================================
# 1. SCORING WEIGHTS
# ============================================================

SCORING_WEIGHTS = {

    "contact": 10,

    "completeness": 20,

    "content_quality": 25,

    "skills_quality": 15,

    "projects_quality": 15,

    "experience_quality": 15
}


# ============================================================
# 2. GENERIC / WEAK PHRASES
# ============================================================

GENERIC_PHRASES = [

    "hardworking",
    "dedicated",
    "motivated",
    "passionate",
    "quick learner",
    "team player",
    "responsible",
    "self motivated",
    "self-motivated",
    "excellent communication skills",
    "good communication skills",
    "seeking an opportunity",
    "looking for an opportunity",
    "willing to learn",
    "ability to work",
]


# ============================================================
# 3. ACTION VERBS
# ============================================================

ACTION_VERBS = [

    "built",
    "developed",
    "created",
    "designed",
    "implemented",
    "developed",
    "managed",
    "led",
    "supervised",
    "coordinated",
    "optimized",
    "improved",
    "analyzed",
    "automated",
    "integrated",
    "tested",
    "deployed",
    "maintained",
    "engineered",
    "configured",
    "implemented",
    "solved",
    "reduced",
    "increased",
    "delivered",
    "organized",
    "handled",
    "supported",
    "developed",
]


# ============================================================
# 4. TECHNOLOGY KEYWORDS
# ============================================================

TECHNOLOGY_KEYWORDS = [

    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",

    "react",
    "node.js",
    "fastapi",
    "django",
    "flask",

    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",

    "mysql",
    "sqlite",
    "postgresql",
    "mongodb",
    "sql",

    "git",
    "github",
    "docker",
    "postman",

    "aws",

    "machine learning",
    "deep learning",
    "artificial intelligence",

    "raylib",
    "stockfish"
]


# ============================================================
# 5. HELPER FUNCTIONS
# ============================================================

def has_content(value):
    """
    Check whether a value contains meaningful content.
    """

    if value is None:
        return False

    if isinstance(value, list):

        return len(value) > 0

    if isinstance(value, str):

        return bool(
            value.strip()
        )

    if isinstance(value, dict):

        return len(value) > 0

    return bool(value)


# ============================================================
# GET SECTION
# ============================================================

def get_section(
    resume,
    section_type
):

    sections = resume.get(
        "sections",
        []
    )

    for section in sections:

        if section.get("type") == section_type:

            return section

    return None


# ============================================================
# GET SECTION CONTENT
# ============================================================

def get_section_content(
    section
):

    if not section:

        return []

    content = []

    # Direct content
    content.extend(
        section.get(
            "content",
            []
        )
    )

    # Subsections
    for subsection in section.get(
        "subsections",
        []
    ):

        content.extend(
            subsection.get(
                "content",
                []
            )
        )

    # Entries
    for entry in section.get(
        "entries",
        []
    ):

        if entry.get("title"):

            content.append(
                entry["title"]
            )

        content.extend(
            entry.get(
                "content",
                []
            )
        )

    return [
        str(item)
        for item in content
        if has_content(item)
    ]


# ============================================================
# GET ALL TEXT
# ============================================================

def get_all_resume_text(
    resume
):

    parts = []

    if resume.get("name"):

        parts.append(
            str(resume["name"])
        )

    if resume.get("email"):

        parts.append(
            str(resume["email"])
        )

    if resume.get("phone"):

        parts.append(
            str(resume["phone"])
        )

    for skill in resume.get(
        "skills",
        []
    ):

        parts.append(
            str(skill)
        )

    for section in resume.get(
        "sections",
        []
    ):

        parts.extend(
            get_section_content(
                section
            )
        )

    return " ".join(
        parts
    )


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(
    text
):

    text = str(
        text
    ).lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# COUNT ACTION VERBS
# ============================================================

def count_action_verbs(
    text
):

    text = normalize_text(
        text
    )

    count = 0

    for verb in ACTION_VERBS:

        if re.search(
            r"\b"
            + re.escape(verb)
            + r"\b",
            text
        ):

            count += 1

    return count


# ============================================================
# COUNT GENERIC PHRASES
# ============================================================

def count_generic_phrases(
    text
):

    text = normalize_text(
        text
    )

    count = 0

    for phrase in GENERIC_PHRASES:

        if phrase in text:

            count += 1

    return count


# ============================================================
# COUNT TECHNOLOGIES
# ============================================================

def count_technologies(
    text
):

    text = normalize_text(
        text
    )

    count = 0

    found = set()

    for technology in TECHNOLOGY_KEYWORDS:

        if re.search(
            r"(?<!\w)"
            + re.escape(
                technology
            )
            + r"(?!\w)",
            text
        ):

            found.add(
                technology
            )

    count = len(
        found
    )

    return count


# ============================================================
# CONTACT ANALYSIS
# ============================================================

def analyze_contact(
    resume
):

    score = 0

    warnings = []

    suggestions = []

    # --------------------------------------------------------
    # Name
    # --------------------------------------------------------

    if has_content(
        resume.get("name")
    ):

        score += 30

    else:

        warnings.append(
            "Candidate name is missing."
        )

        suggestions.append(
            "Add your full name at the top of the resume."
        )

    # --------------------------------------------------------
    # Email
    # --------------------------------------------------------

    if has_content(
        resume.get("email")
    ):

        score += 35

    else:

        warnings.append(
            "Email address is missing."
        )

        suggestions.append(
            "Add a professional email address."
        )

    # --------------------------------------------------------
    # Phone
    # --------------------------------------------------------

    if has_content(
        resume.get("phone")
    ):

        score += 35

    else:

        warnings.append(
            "Phone number is missing."
        )

        suggestions.append(
            "Add a reachable phone number."
        )

    return {

        "score": score,

        "warnings": warnings,

        "suggestions": suggestions
    }


# ============================================================
# COMPLETENESS ANALYSIS
# ============================================================

def analyze_completeness(
    resume
):

    # Each section contributes to completeness.
    #
    # These aren't necessarily mandatory for every resume.
    # They measure whether the resume is reasonably complete.

    section_weights = {

        "summary": 10,

        "education": 20,

        "skills": 20,

        "projects": 20,

        "experience": 15,

        "certifications_and_achievements": 10,

        "strengths": 5
    }

    score = 0

    warnings = []

    suggestions = []

    for section_type, weight in section_weights.items():

        section = get_section(
            resume,
            section_type
        )

        if section:

            content = get_section_content(
                section
            )

            if content:

                score += weight

        else:

            # Only warn about important sections.
            if section_type in [
                "education",
                "skills",
                "projects"
            ]:

                section_name = (
                    section_type
                    .replace(
                        "_",
                        " "
                    )
                    .title()
                )

                warnings.append(
                    f"{section_name} section is missing."
                )

                suggestions.append(
                    f"Add a {section_name} section."
                )

    return {

        "score": score,

        "warnings": warnings,

        "suggestions": suggestions
    }


# ============================================================
# CONTENT QUALITY
# ============================================================

def analyze_content_quality(
    resume
):

    score_parts = []

    warnings = []

    suggestions = []

    # ========================================================
    # CAREER OBJECTIVE / SUMMARY
    # ========================================================

    summary = get_section(
        resume,
        "summary"
    )

    summary_score = 0

    if summary:

        content = get_section_content(
            summary
        )

        summary_text = " ".join(
            content
        )

        word_count = len(
            summary_text.split()
        )

        if word_count >= 25:

            summary_score += 40

        elif word_count >= 15:

            summary_score += 30

        elif word_count >= 8:

            summary_score += 20

        else:

            warnings.append(
                "Career objective or summary is very short."
            )

            suggestions.append(
                "Write a concise summary that highlights your role, skills, and career direction."
            )

        generic_count = count_generic_phrases(
            summary_text
        )

        if generic_count == 0:

            summary_score += 30

        elif generic_count <= 2:

            summary_score += 15

            warnings.append(
                "Career objective contains generic wording."
            )

            suggestions.append(
                "Replace generic phrases with specific skills, goals, or achievements."
            )

        else:

            warnings.append(
                "Career objective contains several generic phrases."
            )

            suggestions.append(
                "Make the career objective more specific to your target role."
            )

        technology_count = count_technologies(
            summary_text
        )

        if technology_count >= 2:

            summary_score += 30

        elif technology_count == 1:

            summary_score += 15

        else:

            suggestions.append(
                "Consider mentioning relevant technical skills in the summary."
            )

    else:

        warnings.append(
            "Career objective or professional summary is missing."
        )

        suggestions.append(
            "Add a short professional summary tailored to your target role."
        )

    score_parts.append(
        summary_score
    )

    # ========================================================
    # GENERAL CONTENT
    # ========================================================

    all_text = get_all_resume_text(
        resume
    )

    action_verbs = count_action_verbs(
        all_text
    )

    generic_phrases = count_generic_phrases(
        all_text
    )

    # Action verbs
    if action_verbs >= 6:

        score_parts.append(
            100
        )

    elif action_verbs >= 3:

        score_parts.append(
            70
        )

        suggestions.append(
            "Use stronger action verbs such as developed, implemented, designed, optimized, or automated."
        )

    elif action_verbs >= 1:

        score_parts.append(
            40
        )

        warnings.append(
            "Resume uses relatively few action verbs."
        )

        suggestions.append(
            "Use action-oriented language to describe your work."
        )

    else:

        score_parts.append(
            20
        )

        warnings.append(
            "Resume contains very few action verbs."
        )

    # Generic phrases
    if generic_phrases == 0:

        score_parts.append(
            100
        )

    elif generic_phrases <= 2:

        score_parts.append(
            70
        )

        warnings.append(
            "Some generic phrases were detected."
        )

    else:

        score_parts.append(
            40
        )

        warnings.append(
            "Several generic phrases were detected."
        )

        suggestions.append(
            "Replace generic statements with specific evidence of your skills."
        )

    # --------------------------------------------------------
    # Final content score
    # --------------------------------------------------------

    if score_parts:

        score = round(
            sum(score_parts)
            / len(score_parts)
        )

    else:

        score = 0

    return {

        "score": min(
            score,
            100
        ),

        "warnings": warnings,

        "suggestions": suggestions
    }


# ============================================================
# SKILLS QUALITY
# ============================================================

def analyze_skills_quality(
    resume
):

    skills = resume.get(
        "skills",
        []
    )

    score = 0

    warnings = []

    suggestions = []

    skill_count = len(
        skills
    )

    # --------------------------------------------------------
    # Number of skills
    # --------------------------------------------------------

    if skill_count >= 15:

        score += 40

    elif skill_count >= 10:

        score += 35

    elif skill_count >= 6:

        score += 25

    elif skill_count >= 3:

        score += 15

    else:

        score += 5

        warnings.append(
            "Very few technical skills were detected."
        )

        suggestions.append(
            "Add relevant technical skills that you actually know."
        )

    # --------------------------------------------------------
    # Programming languages
    # --------------------------------------------------------

    programming_languages = {

        "python",
        "java",
        "c++",
        "c#",
        "javascript",
        "typescript"
    }

    if any(
        skill in programming_languages
        for skill in skills
    ):

        score += 20

    else:

        suggestions.append(
            "Include relevant programming languages."
        )

    # --------------------------------------------------------
    # Frameworks / libraries
    # --------------------------------------------------------

    frameworks = {

        "react",
        "node.js",
        "fastapi",
        "django",
        "flask",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch"
    }

    if any(
        skill in frameworks
        for skill in skills
    ):

        score += 15

    else:

        suggestions.append(
            "Include frameworks or libraries relevant to your target role."
        )

    # --------------------------------------------------------
    # Database
    # --------------------------------------------------------

    databases = {

        "sql",
        "mysql",
        "sqlite",
        "postgresql",
        "mongodb"
    }

    if any(
        skill in databases
        for skill in skills
    ):

        score += 10

    else:

        suggestions.append(
            "Consider listing database technologies you have used."
        )

    # --------------------------------------------------------
    # Tools
    # --------------------------------------------------------

    tools = {

        "git",
        "github",
        "docker",
        "postman"
    }

    if any(
        skill in tools
        for skill in skills
    ):

        score += 15

    else:

        suggestions.append(
            "Consider including development tools such as Git or relevant alternatives."
        )

    return {

        "score": min(
            score,
            100
        ),

        "skill_count": skill_count,

        "warnings": warnings,

        "suggestions": suggestions
    }


# ============================================================
# PROJECT QUALITY
# ============================================================

def analyze_projects_quality(
    resume
):

    projects = resume.get(
        "projects",
        []
    )

    score = 0

    warnings = []

    suggestions = []

    if not projects:

        return {

            "score": 0,

            "project_count": 0,

            "warnings": [
                "No projects were detected."
            ],

            "suggestions": [
                "Add academic or personal projects relevant to your target role."
            ]
        }

    # --------------------------------------------------------
    # Count project titles
    # --------------------------------------------------------

    project_titles = []

    for item in projects:

        text = str(
            item
        ).strip()

        if (
            "—" in text
            or " – " in text
            or " - " in text
        ):

            project_titles.append(
                text
            )

    project_count = len(
        project_titles
    )

    # --------------------------------------------------------
    # Project quantity
    # --------------------------------------------------------

    if project_count >= 3:

        score += 30

    elif project_count == 2:

        score += 25

    elif project_count == 1:

        score += 15

    else:

        score += 5

        warnings.append(
            "Project titles could not be reliably detected."
        )

    # --------------------------------------------------------
    # Descriptions
    # --------------------------------------------------------

    descriptions = [

        str(item)
        for item in projects
        if str(item).strip().startswith("•")
    ]

    if len(descriptions) >= project_count:

        score += 25

    elif descriptions:

        score += 15

        warnings.append(
            "Some projects do not appear to have descriptions."
        )

    else:

        warnings.append(
            "Project descriptions are missing."
        )

        suggestions.append(
            "Explain what you built, how you built it, and what the result was."
        )

    # --------------------------------------------------------
    # Technologies
    # --------------------------------------------------------

    project_text = " ".join(
        str(item)
        for item in projects
    )

    technology_count = count_technologies(
        project_text
    )

    if technology_count >= 5:

        score += 25

    elif technology_count >= 3:

        score += 20

    elif technology_count >= 1:

        score += 10

    else:

        suggestions.append(
            "Mention the technologies used in your projects."
        )

    # --------------------------------------------------------
    # Action verbs
    # --------------------------------------------------------

    project_description_text = " ".join(
        descriptions
    )

    action_count = count_action_verbs(
        project_description_text
    )

    if action_count >= 3:

        score += 20

    elif action_count >= 1:

        score += 10

        suggestions.append(
            "Use stronger action verbs and describe your contribution."
        )

    else:

        warnings.append(
            "Project descriptions contain few action verbs."
        )

        suggestions.append(
            "Describe what you built or implemented using action-oriented language."
        )

    return {

        "score": min(
            score,
            100
        ),

        "project_count": project_count,

        "warnings": warnings,

        "suggestions": suggestions
    }


# ============================================================
# EXPERIENCE QUALITY
# ============================================================

def analyze_experience_quality(
    resume
):

    experience = resume.get(
        "experience",
        []
    )

    score = 0

    warnings = []

    suggestions = []

    if not experience:

        return {

            "score": 50,

            "experience_count": 0,

            "warnings": [],

            "suggestions": [
                "If you have internships, freelance work, part-time work, or relevant experience, consider adding them."
            ]
        }

    # --------------------------------------------------------
    # Count entries
    # --------------------------------------------------------

    entries = [

        str(item)
        for item in experience
        if "|" in str(item)
    ]

    experience_count = len(
        entries
    )

    if experience_count >= 2:

        score += 25

    elif experience_count == 1:

        score += 15

    else:

        score += 5

        warnings.append(
            "Experience entries could not be reliably detected."
        )

    # --------------------------------------------------------
    # Descriptions
    # --------------------------------------------------------

    descriptions = [

        str(item)
        for item in experience
        if str(item).strip().startswith("•")
    ]

    if descriptions:

        score += 25

    else:

        warnings.append(
            "Experience descriptions are missing."
        )

        suggestions.append(
            "Describe responsibilities, contributions, and results for each position."
        )

    # --------------------------------------------------------
    # Action verbs
    # --------------------------------------------------------

    description_text = " ".join(
        descriptions
    )

    action_count = count_action_verbs(
        description_text
    )

    if action_count >= 3:

        score += 20

    elif action_count >= 1:

        score += 10

    else:

        suggestions.append(
            "Use stronger action verbs to describe your responsibilities."
        )

    # --------------------------------------------------------
    # Dates / duration
    # --------------------------------------------------------

    experience_text = " ".join(
        experience
    ).lower()

    has_duration = (

        "month" in experience_text

        or

        "year" in experience_text

        or

        bool(
            re.search(
                r"\b20\d{2}\b",
                experience_text
            )
        )
    )

    if has_duration:

        score += 15

    else:

        warnings.append(
            "Experience dates or durations were not detected."
        )

        suggestions.append(
            "Include the dates or duration for each position."
        )

    # --------------------------------------------------------
    # Measurable results
    # --------------------------------------------------------

    measurable = bool(
        re.search(
            r"\b\d+(?:\.\d+)?\s*(?:%|percent|users|projects|hours|days|months|years|x)\b",
            description_text.lower()
        )
    )

    if measurable:

        score += 15

    else:

        suggestions.append(
            "Add measurable results where possible, such as percentages, time saved, users served, or performance improvements."
        )

    return {

        "score": min(
            score,
            100
        ),

        "experience_count": experience_count,

        "warnings": warnings,

        "suggestions": suggestions
    }


# ============================================================
# CALCULATE OVERALL SCORE
# ============================================================

def calculate_overall_score(
    analyses
):

    total = 0

    for category, weight in SCORING_WEIGHTS.items():

        category_score = analyses[
            category
        ]["score"]

        total += (
            category_score
            * weight
            / 100
        )

    return round(
        total
    )


# ============================================================
# COLLECT WARNINGS
# ============================================================

def collect_warnings(
    analyses
):

    warnings = []

    for analysis in analyses.values():

        warnings.extend(
            analysis.get(
                "warnings",
                []
            )
        )

    # Remove duplicates
    return list(
        dict.fromkeys(
            warnings
        )
    )


# ============================================================
# COLLECT SUGGESTIONS
# ============================================================

def collect_suggestions(
    analyses
):

    suggestions = []

    for analysis in analyses.values():

        suggestions.extend(
            analysis.get(
                "suggestions",
                []
            )
        )

    # Remove duplicates
    return list(
        dict.fromkeys(
            suggestions
        )
    )


# ============================================================
# MAIN ANALYZER
# ============================================================

def analyze_resume(
    resume
):

    # --------------------------------------------------------
    # Individual analyses
    # --------------------------------------------------------

    contact = analyze_contact(
        resume
    )

    completeness = analyze_completeness(
        resume
    )

    content_quality = analyze_content_quality(
        resume
    )

    skills_quality = analyze_skills_quality(
        resume
    )

    projects_quality = analyze_projects_quality(
        resume
    )

    experience_quality = analyze_experience_quality(
        resume
    )

    # --------------------------------------------------------
    # Analysis collection
    # --------------------------------------------------------

    analyses = {

        "contact": contact,

        "completeness": completeness,

        "content_quality": content_quality,

        "skills_quality": skills_quality,

        "projects_quality": projects_quality,

        "experience_quality": experience_quality
    }

    # --------------------------------------------------------
    # Overall score
    # --------------------------------------------------------

    overall_score = calculate_overall_score(
        analyses
    )

    # --------------------------------------------------------
    # Warnings
    # --------------------------------------------------------

    warnings = collect_warnings(
        analyses
    )

    # --------------------------------------------------------
    # Suggestions
    # --------------------------------------------------------

    suggestions = collect_suggestions(
        analyses
    )

    # --------------------------------------------------------
    # Final response
    # --------------------------------------------------------

    return {

        "overall_score": overall_score,

        "weights": SCORING_WEIGHTS,

        "category_scores": {

            "contact": contact["score"],

            "completeness": completeness["score"],

            "content_quality": content_quality["score"],

            "skills_quality": skills_quality["score"],

            "projects_quality": projects_quality["score"],

            "experience_quality": experience_quality["score"]
        },

        "warnings": warnings,

        "suggestions": suggestions,

        "details": analyses
    }


# ============================================================
# LOCAL TEST
# ============================================================

if __name__ == "__main__":

    sample_resume = {

        "name": "ABHAY SHARMA",

        "email": "abhay@example.com",

        "phone": None,

        "skills": [
            "python",
            "c++",
            "javascript",
            "html",
            "css",
            "react",
            "fastapi",
            "raylib",
            "pandas",
            "numpy",
            "scikit-learn",
            "mysql",
            "sqlite",
            "github",
            "postman",
            "vs code",
            "data structures & algorithms",
            "oop",
            "dbms",
            "computer networks",
            "software engineering"
        ],

        "education": [
            "B.Tech / B.E. in Computer Science & Engineering",
            "ABC Institute of Technology, India",
            "2023 – 2027",
            "CGPA: 8.2/10",
            "Higher Secondary (12th)",
            "XYZ Senior Secondary School",
            "2023",
            "Percentage: 82%"
        ],

        "experience": [
            "Supervisor | Dream Beauty Fashion Volmo | 6 months",
            "• Supervised daily operations, coordinated staff activities, maintained records, and supported customer service.",
            "Sales Executive | Utkarsh Small Finance Bank | 9 months",
            "• Handled customer interactions, explained banking products, supported sales activities, and maintained customer records."
        ],

        "projects": [
            "Smart Task Management System — Python, FastAPI, SQLite, HTML/CSS/JS",
            "• Built a REST-based task management application with user authentication, task CRUD operations, filtering, and a responsive frontend.",
            "Chess Game with AI — C++, Raylib, Stockfish",
            "• Developed a desktop chess game with graphical UI, legal move handling, board rendering, and Stockfish-based computer opponent integration.",
            "Typing Speed Test — HTML, CSS, JavaScript",
            "• Created an interactive typing test that calculates WPM and accuracy, supports timed sessions, and provides performance feedback."
        ],

        "sections": [

            {
                "name": "career objective",
                "type": "summary",
                "subsections": [],
                "entries": [],
                "content": [
                    "Motivated Computer Science undergraduate seeking an internship or entry-level opportunity to apply programming, web development, software engineering, and problem-solving skills while contributing to real-world projects and continuing to learn."
                ]
            },

            {
                "name": "education",
                "type": "education",
                "subsections": [],
                "entries": [
                    {
                        "title": "B.Tech / B.E. in Computer Science & Engineering",
                        "content": [
                            "ABC Institute of Technology, India",
                            "2023 – 2027",
                            "CGPA: 8.2/10"
                        ]
                    },
                    {
                        "title": "Higher Secondary (12th)",
                        "content": [
                            "XYZ Senior Secondary School",
                            "2023",
                            "Percentage: 82%"
                        ]
                    }
                ],
                "content": []
            },

            {
                "name": "technical skills",
                "type": "skills",
                "subsections": [
                    {
                        "name": "languages",
                        "content": [
                            "C++, Java, Python, JavaScript, HTML, CSS"
                        ]
                    },
                    {
                        "name": "frameworks libraries",
                        "content": [
                            "FastAPI, React, Raylib, Pandas, NumPy, scikit-learn"
                        ]
                    },
                    {
                        "name": "databases",
                        "content": [
                            "MySQL, SQLite"
                        ]
                    },
                    {
                        "name": "tools",
                        "content": [
                            "Git, GitHub, VS Code, Postman"
                        ]
                    },
                    {
                        "name": "core concepts",
                        "content": [
                            "Data Structures & Algorithms, OOP, DBMS, OS, Computer Networks, Software Engineering"
                        ]
                    }
                ],
                "entries": [],
                "content": []
            },

            {
                "name": "projects",
                "type": "projects",
                "subsections": [],
                "entries": [
                    {
                        "title": "Smart Task Management System — Python, FastAPI, SQLite, HTML/CSS/JS",
                        "content": [
                            "• Built a REST-based task management application with user authentication, task CRUD operations, filtering, and a responsive frontend."
                        ]
                    },
                    {
                        "title": "Chess Game with AI — C++, Raylib, Stockfish",
                        "content": [
                            "• Developed a desktop chess game with graphical UI, legal move handling, board rendering, and Stockfish-based computer opponent integration."
                        ]
                    },
                    {
                        "title": "Typing Speed Test — HTML, CSS, JavaScript",
                        "content": [
                            "• Created an interactive typing test that calculates WPM and accuracy, supports timed sessions, and provides performance feedback."
                        ]
                    }
                ],
                "content": []
            },

            {
                "name": "experience",
                "type": "experience",
                "subsections": [],
                "entries": [
                    {
                        "title": "Supervisor | Dream Beauty Fashion Volmo | 6 months",
                        "content": [
                            "• Supervised daily operations, coordinated staff activities, maintained records, and supported customer service."
                        ]
                    },
                    {
                        "title": "Sales Executive | Utkarsh Small Finance Bank | 9 months",
                        "content": [
                            "• Handled customer interactions, explained banking products, supported sales activities, and maintained customer records."
                        ]
                    }
                ],
                "content": []
            },

            {
                "name": "certifications and achievements",
                "type": "certifications_and_achievements",
                "subsections": [],
                "entries": [],
                "content": [
                    "• Completed online coursework in Python, Machine Learning, and Web Development.",
                    "• Built multiple academic and personal software projects.",
                    "• Participated in programming and technical learning activities."
                ]
            },

            {
                "name": "strengths",
                "type": "strengths",
                "subsections": [],
                "entries": [],
                "content": [
                    "Problem Solving • Quick Learner • Teamwork • Communication • Adaptability"
                ]
            }
        ]
    }

    # --------------------------------------------------------
    # Run analyzer
    # --------------------------------------------------------

    result = analyze_resume(
        sample_resume
    )

    # --------------------------------------------------------
    # Print result
    # --------------------------------------------------------

    import pprint

    pprint.pprint(
        result,
        sort_dicts=False
    )