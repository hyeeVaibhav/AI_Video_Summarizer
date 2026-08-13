import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summary_pipeline(model_name):
    # Load the pipeline once and keep it in memory
    return pipeline("summarization", model=model_name)

def summarize_text(text: str, model_name: str = "Falconsai/text_summarization", max_length: int = 150, min_length: int = 30) -> str:
    summarizer = load_summary_pipeline(model_name)
    
    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']