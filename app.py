import streamlit as st
import tempfile
from summarizer.extract import extract_text_from_pdf
from summarizer.summarize import summarize_pipeline

st.set_page_config(page_title="Document Summarizer", layout="wide")
st.title("📑 AI Document Summarizer")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("Extracting text from PDF...")
    text = extract_text_from_pdf(tmp_path)

    if text.strip():
        st.success("Text extracted. Running summarization...")
        summary, chunk_summaries = summarize_pipeline(text)

        st.subheader("📌 Executive Summary")
        st.write(summary)

        with st.expander("🔎 Chunk-level Summaries"):
            for i, cs in enumerate(chunk_summaries, 1):
                st.markdown(f"**Chunk {i}:** {cs}")
    else:
        st.error("No text could be extracted from this PDF.")
