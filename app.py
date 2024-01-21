import streamlit as st
from transformers import pipeline

# Load pretrained model
summarizer = pipeline('summarization')

# Get input from user
text = st.text_area("Enter text here")

if text:
    # Summarize text
    summary = summarizer(text)[0]['summary_text']

    # Display summary
    st.write(summary)
