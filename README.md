# JU4--ClaimWise-AI
GenAI

🧳 ClaimWise AI – Smart Claim Assistant for BFSI
🔍 What It Does
ClaimWise AI is an intelligent agent that:

Helps customers and internal teams analyze insurance or financial claim forms

Detects missing fields, inconsistent data, and invalid entries

Suggests next steps or auto-generates missing sections using LLMs

Supports both structured (form) and unstructured (email, PDF) inputs

🛠️ Key Features
Feature	Description
📄 Upload Claim Form	Supports PDF, DOCX, or scanned image
🧠 AI-Based Entity Extraction	Extracts Name, Policy No., Dates, Amount Claimed, etc.
🧾 Form Validator	Detects missing or inconsistent data entries
🔍 Suggest Fixes	Auto-suggests missing fields using LLM inference
📌 Flag Suspicious Claims	Uses basic rule/ML logic to flag anomalies
🗂️ Export Summary	Generates a filled + cleaned version of the form

🧱 Tech Stack
Frontend: Streamlit

Backend: Python

Document Parsing: PyMuPDF / pdfplumber / python-docx

OCR (for scans): Azure Vision AI / Tesseract

LLM: Ollama or Azure OpenAI (GPT-4)

Validation Rules: Custom logic or fine-tuned BERT

Optional DB: MongoDB for storing user claims

 README.md
markdown
Copy
Edit
# 📘 PolicyPal AI – Insurance Policy Summarizer and Checker

PolicyPal AI helps users understand their insurance policies by summarizing uploaded PDFs and extracting key clauses like sum insured, waiting period, exclusions, etc.

## 🚀 Features

- Upload policy documents in PDF
- AI summarizes coverage, exclusions, conditions
- Warns about missing clauses
- Outputs structured summary with highlights

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/policypal-ai.git
cd policypal-ai
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Pull the LLaMA model using Ollama:

bash
Copy
Edit
ollama pull llama3
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
🧪 Sample Test
Use the sample_docs/sample_policy.pdf to test the summarization.

🔐 LLM Options
Uses llama3 via Ollama (local)

You can switch to Azure OpenAI or GPT-4 via API by editing query_llm() function
