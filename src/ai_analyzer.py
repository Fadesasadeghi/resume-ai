import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume_with_ai(resume_text, job_description):
    prompt = f"""
You are a careful and evidence-based professional resume reviewer.

Your task is to compare the candidate's resume with the provided job
description and give useful feedback based ONLY on the supplied text.

RESUME:
--- BEGIN RESUME ---
{resume_text}
--- END RESUME ---

JOB DESCRIPTION:
--- BEGIN JOB DESCRIPTION ---
{job_description}
--- END JOB DESCRIPTION ---

Provide the analysis using exactly these sections:

## Overall Assessment
Give a short assessment of how well the resume aligns with the job description.

## Strengths
List relevant skills, education, experience, projects, or achievements that are
explicitly supported by the resume and relevant to the job description.

## Gaps
Identify requirements from the job description that are not mentioned or not
clearly demonstrated in the resume.

## Missing Skills
List job-related skills that appear in the job description but are not mentioned
in the resume.

## Suggestions for Improvement
Give practical suggestions for improving the resume for this specific job.

IMPORTANT RULES:

1. Use only information explicitly present in the resume and job description.
2. Never invent skills, work experience, projects, education, certifications,
   achievements, or personal information.
3. If something is not mentioned in the resume, say:
   "not mentioned in the resume"
   or
   "not demonstrated in the resume."
   Do NOT claim that the candidate does not have that skill or experience.
4. Do not treat missing certifications as a weakness unless the job description
   explicitly requires or prefers them.
5. Do not treat missing work experience, projects, or technologies as a weakness
   unless they are relevant to the supplied job description.
6. Distinguish between:
   - a requirement that is missing from the resume
   - a skill that the candidate definitely does not have
   You can identify the first, but you cannot infer the second.
7. If PDF text extraction appears fragmented or out of order, do not assume that
   information is absent solely because formatting is imperfect.
8. Focus primarily on job-relevant information.
9. Suggestions must be specific and actionable.
10. Do not recommend adding a skill, experience, project, or achievement unless
    it is true. Instead, say that if the candidate has that experience, they
    should make it explicit in the resume.
11. The resume may contain Persian text. Understand Persian content normally and
    do not treat Persian wording as missing information simply because it is not
    written in English.
12. Keep the response concise, professional, and evidence-based.
13. Never assign or suggest a proficiency level (such as Beginner,
    Intermediate, Advanced, or Expert) unless that level is explicitly
    supported by the resume.

14. Never suggest that the candidate add a missing skill to the resume simply
    to match the job description. If a job-required skill is not mentioned,
    recommend adding it only if the candidate genuinely has that skill or
    experience. Otherwise, describe it as a potential learning area.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content
