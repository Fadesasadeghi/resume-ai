# 📄 ResumeAI

ResumeAI is an AI-powered resume analysis application built with Python and Streamlit.

It compares a PDF resume with a job description, identifies matching and missing skills, calculates a match score, and provides AI-powered feedback using Groq.

## ✨ Features

- Upload and extract text from PDF resumes
- Detect technical skills automatically
- Compare resume skills with job requirements
- Calculate a resume-job match score
- Identify matched and missing skills
- Generate detailed AI-powered resume feedback
- Provide strengths, weaknesses, and improvement suggestions
- Simple interactive interface built with Streamlit

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- pypdf
- python-dotenv
- Git & GitHub

## 📁 Project Structure

    resume-ai/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    └── src/
        ├── __init__.py
        ├── resume_parser.py
        ├── analyzer.py
        └── ai_analyzer.py

## 🚀 How It Works

1. Upload a PDF resume.
2. Paste a job description.
3. ResumeAI extracts the text from the resume.
4. Technical skills are detected automatically.
5. Resume skills are compared with the job requirements.
6. A match score is calculated.
7. Groq generates detailed AI-powered feedback.

## ⚙️ Installation

Clone the repository and enter the project directory:

    git clone YOUR_REPOSITORY_URL
    cd resume-ai

Create a virtual environment:

    python -m venv .venv

Activate it on Linux or WSL:

    source .venv/bin/activate

Install the dependencies:

    pip install -r requirements.txt

Create a `.env` file and add your Groq API key:

    GROQ_API_KEY=your_groq_api_key

Run the application:

    streamlit run app.py

## 🔐 Security

API keys are stored locally in the `.env` file.

The `.env` file is excluded from Git using `.gitignore`, so API keys are not committed to the repository.

## 📌 Current Status

ResumeAI currently supports:

- PDF resume parsing
- Technical skill detection
- Resume-job skill comparison
- Match score calculation
- Matched and missing skill detection
- AI-powered resume analysis using Groq

## 👩‍💻 Author

Developed by Fadesa Sadeghi.
