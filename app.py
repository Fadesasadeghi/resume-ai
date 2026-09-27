import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.analyzer import analyze_resume
from src.ai_analyzer import analyze_resume_with_ai


st.set_page_config(
    page_title="ResumeAI",
    page_icon="📄",
    layout="wide",
)


# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero {
            text-align: center;
            padding: 2rem 1rem 2.5rem 1rem;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 0.4rem;
        }

        .hero p {
            font-size: 1.1rem;
            opacity: 0.75;
            max-width: 720px;
            margin: 0 auto;
        }

        .section-title {
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(128, 128, 128, 0.25);
            border-radius: 14px;
            padding: 1rem;
        }

        div[data-testid="stFileUploader"] {
            border-radius: 14px;
        }

        .footer {
            text-align: center;
            opacity: 0.6;
            padding-top: 2rem;
            font-size: 0.9rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Header ----------
st.markdown(
    """
    <div class="hero">
        <h1>📄 ResumeAI</h1>
        <p>
            Compare your resume with a job description, discover missing skills,
            calculate your match score, and receive AI-powered feedback.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- Input ----------
st.subheader("📥 Resume & Job Details")

input_col1, input_col2 = st.columns(2, gap="large")

with input_col1:
    resume_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="Upload your resume as a PDF file.",
    )

with input_col2:
    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the job description here...",
        height=220,
    )

analyze_clicked = st.button(
    "✨ Analyze Resume",
    type="primary",
    use_container_width=True,
)


# ---------- Analysis ----------
if analyze_clicked:

    if resume_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            with st.spinner("Reading and analyzing your resume..."):
                resume_text = extract_text_from_pdf(resume_file)

            if not resume_text:
                st.error("No readable text was found in the PDF.")

            else:
                result = analyze_resume(
                    resume_text,
                    job_description,
                )

                st.success("Resume analyzed successfully!")

                st.divider()

                # ---------- Overview ----------
                st.subheader("📊 Match Overview")

                metric1, metric2, metric3 = st.columns(3)

                with metric1:
                    st.metric(
                        "Match Score",
                        f'{result["score"]}%',
                    )

                with metric2:
                    st.metric(
                        "Matched Skills",
                        len(result["matched_skills"]),
                    )

                with metric3:
                    st.metric(
                        "Missing Skills",
                        len(result["missing_skills"]),
                    )

                st.progress(result["score"] / 100)

                # ---------- Skills ----------
                st.subheader("🎯 Skill Comparison")

                matched_col, missing_col = st.columns(2, gap="large")

                with matched_col:
                    st.markdown("### ✅ Matched Skills")

                    if result["matched_skills"]:
                        for skill in result["matched_skills"]:
                            st.success(skill)
                    else:
                        st.info("No matching skills found.")

                with missing_col:
                    st.markdown("### ❌ Missing Skills")

                    if result["missing_skills"]:
                        for skill in result["missing_skills"]:
                            st.error(skill)
                    else:
                        st.success("No missing skills found.")

                # ---------- AI ----------
                st.divider()
                st.subheader("🤖 AI Resume Analysis")

                try:
                    with st.spinner(
                        "AI is reviewing your resume against the job description..."
                    ):
                        ai_analysis = analyze_resume_with_ai(
                            resume_text,
                            job_description,
                        )

                    st.markdown(ai_analysis)

                except Exception as ai_error:
                    st.warning(
                        "The skill analysis was completed, but the AI review "
                        f"could not be generated: {ai_error}"
                    )

                # ---------- Details ----------
                st.divider()
                st.subheader("🔎 Analysis Details")

                with st.expander("Skills Found in Resume"):
                    if result["resume_skills"]:
                        for skill in result["resume_skills"]:
                            st.write(f"• {skill}")
                    else:
                        st.write("No known skills detected.")

                with st.expander("Skills Found in Job Description"):
                    if result["job_skills"]:
                        for skill in result["job_skills"]:
                            st.write(f"• {skill}")
                    else:
                        st.write("No known skills detected.")

                with st.expander("Extracted Resume Text"):
                    st.text(resume_text)

        except Exception as error:
            st.error(f"Could not analyze the resume: {error}")


# ---------- Footer ----------
st.markdown(
    """
    <div class="footer">
        ResumeAI • Built with Python, Streamlit & Groq
    </div>
    """,
    unsafe_allow_html=True,
)
