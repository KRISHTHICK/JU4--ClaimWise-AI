# app.py – ClaimWise AI: Smart Claim Analyzer

import streamlit as st
from PyPDF2 import PdfReader
import re
import ollama

# --- Step 1: Extract text from PDF ---
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

# --- Step 2: Basic rule-based validation ---
def validate_fields(text):
    issues = []
    if "policy number" not in text.lower():
        issues.append("Missing: Policy Number")
    if not re.search(r"\b[A-Z]{2}\d{4}\b", text):
        issues.append("Invalid or Missing: Policy Number Format (e.g., AB1234)")
    if "claim amount" not in text.lower():
        issues.append("Missing: Claim Amount")
    if not re.search(r"\d{2}-\d{2}-\d{4}", text):
        issues.append("Missing or Invalid Date Format (dd-mm-yyyy)")
    return issues

# --- Step 3: Generate LLM Prompt ---
def generate_prompt(text):
    prompt = f"""
You are a smart claim validation assistant for insurance companies. 
Given the following claim document content, extract key information in JSON format with the following keys:

- Name
- Policy Number
- Claim Amount
- Date of Incident
- Hospital Name
- Treatment Summary

Also flag any anomalies or missing sections in a separate list.

Content:
{text[:4000]}
"""
    return prompt

# --- Step 4: LLM-based extraction and anomaly detection ---
def analyze_with_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="ClaimWise AI", layout="wide")
st.title("🧾 ClaimWise AI – Smart Claim Analyzer")

uploaded_file = st.file_uploader("Upload Claim Form (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting and validating..."):
        text = extract_text_from_pdf(uploaded_file)
        issues = validate_fields(text)
        st.success("Text extracted and basic validation complete.")

    st.subheader("🔍 Validation Report")
    if issues:
        for i in issues:
            st.warning(i)
    else:
        st.success("✅ No basic issues found.")

    if st.button("🧠 Analyze with AI Agent"):
        with st.spinner("Analyzing with LLM..."):
            prompt = generate_prompt(text)
            result = analyze_with_llm(prompt)
            st.markdown("### 📋 Extracted Claim Summary")
            st.code(result, language='json')
else:
    st.info("Please upload a PDF claim form to begin.")
