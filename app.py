import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.analyzer import analyze_resume
from src.ai_analyzer import analyze_resume_with_ai


st.set_page_config(
    page_title="ResumeAI",
    page_icon="📄",
    layout="wide",
)

st.title("📄 ResumeAI")
st.subheader("AI-Powered Resume Analyzer")

st.write(
    "Upload your resume and compare it with a job description "
    "to discover your strengths, missing skills, and opportunities for improvement."
)

st.divider()

resume_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
)

job_description = st.text_area(
    "Job Description",
    placeholder="Paste the job description here...",
    height=250,
)

if st.button("Analyze Resume", type="primary"):

    if resume_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            resume_text = extract_text_from_pdf(resume_file)

            if not resume_text:
                st.error("No readable text was found in the PDF.")

            else:
                # Rule-based analysis
                result = analyze_resume(
                    resume_text,
                    job_description
                )

                st.success("Resume analyzed successfully!")

                st.subheader("Match Score")
                st.progress(result["score"] / 100)
                st.metric(
                    "Resume Match",
                    f'{result["score"]}%'
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("✅ Matched Skills")

                    if result["matched_skills"]:
                        for skill in result["matched_skills"]:
                            st.write(f"• {skill}")
                    else:
                        st.write("No matching skills found.")

                with col2:
                    st.subheader("❌ Missing Skills")

                    if result["missing_skills"]:
                        for skill in result["missing_skills"]:
                            st.write(f"• {skill}")
                    else:
                        st.write("No missing skills found.")

                # AI analysis
                st.divider()
                st.subheader("🤖 AI Resume Analysis")

                with st.spinner("AI is analyzing your resume..."):
                    ai_analysis = analyze_resume_with_ai(
                        resume_text,
                        job_description
                    )

                st.markdown(ai_analysis)

                with st.expander("Skills Found in Resume"):
                    if result["resume_skills"]:
                        for skill in result["resume_skills"]:
                            st.write(f"• {skill}")
                    else:
                        st.write("No known skills detected.")

                with st.expander("Extracted Resume Text"):
                    st.text(resume_text)

        except Exception as error:
            st.error(f"Could not analyze the resume: {error}")
