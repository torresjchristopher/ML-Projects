import streamlit as st
from src.parser import extract_text_from_pdf, load_job_description
from src.embedder import embed_text
from src.matcher import compute_similarity

st.title("🧠 Resume Matcher")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_choice = st.selectbox("Choose Job Role", ["software_engineer.txt"])

if uploaded_resume and job_choice:
    resume_text = extract_text_from_pdf(uploaded_resume)
    jd_text = load_job_description(f"data/job_descriptions/{job_choice}")

    res_embed = embed_text(resume_text)
    jd_embed = embed_text(jd_text)

    score = compute_similarity(res_embed, jd_embed)
    st.success(f"Similarity Score: {score:.4f}")
