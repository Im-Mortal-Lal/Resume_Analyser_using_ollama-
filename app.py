import streamlit as st
from pdf_reader import extract_text
from analyzer import analyze_resume

st.set_page_config(page_title="Resume Analyzer by LALIT KOTURU", layout="wide")
st.title("Resume Analyzer by LALIT KOTURU")
st.markdown("Upload a PDF resume to analyze it using AI.")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading resume..."):
        resume = extract_text(uploaded_file)
    st.success("Resume analysis completed!")

    if st.button("Analyze Resume"):
            with st.spinner("Analyzing resume text..."):
                result = analyze_resume(resume)

            st.markdown("### Resume Text")

            st.download_button( "Download Resume Text", result, file_name="resume_text.txt")
