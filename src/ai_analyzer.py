import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume_with_ai(resume_text, job_description):
    prompt = f"""
You are a professional resume reviewer.

Analyze the following resume against the provided job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide your response with these sections:

1. Overall Assessment
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions for Improvement

Important rules:
- Base the analysis only on the resume and job description.
- Do not invent experience, skills, education, or achievements.
- Clearly distinguish missing skills from existing skills.
- Give practical and specific improvement suggestions.
- Keep the response concise and professional.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
