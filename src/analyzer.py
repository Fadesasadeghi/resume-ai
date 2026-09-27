import re


SKILLS = {
    "Python": ["python", "پایتون"],
    "C": ["c"],
    "C++": ["c++"],
    "Django": ["django"],
    "Flask": ["flask"],
    "FastAPI": ["fastapi"],
    "Streamlit": ["streamlit"],
    "Git": ["git"],
    "GitHub": ["github"],
    "Linux": ["linux", "لینوکس"],
    "SQL": ["sql"],
    "PostgreSQL": ["postgresql"],
    "MySQL": ["mysql"],
    "MongoDB": ["mongodb"],
    "Docker": ["docker"],
    "REST API": ["rest api", "restful api"],
    "Machine Learning": [
        "machine learning",
        "ماشین لرنینگ",
        "یادگیری ماشین",
    ],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "JavaScript": ["javascript"],
    "HTML": ["html"],
    "CSS": ["css"],
}


def contains_skill(text, alias):
    if alias == "c":
        return bool(
            re.search(r"(?<![A-Za-z0-9+#])c(?![A-Za-z0-9+#])", text)
        )

    if alias == "c++":
        return bool(
            re.search(r"(?<![A-Za-z0-9+])c\+\+(?![A-Za-z0-9+])", text)
        )

    return alias in text


def find_skills(text):
    text = text.lower()

    found_skills = []

    for skill, aliases in SKILLS.items():
        for alias in aliases:
            if contains_skill(text, alias.lower()):
                found_skills.append(skill)
                break

    return found_skills


def analyze_resume(resume_text, job_description):
    resume_skills = set(find_skills(resume_text))
    job_skills = set(find_skills(job_description))

    matched_skills = resume_skills & job_skills
    missing_skills = job_skills - resume_skills

    if job_skills:
        match_score = round(
            len(matched_skills) / len(job_skills) * 100
        )
    else:
        match_score = 0

    return {
        "score": match_score,
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
    }
