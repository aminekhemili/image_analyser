import base64
import time
import anthropic
import streamlit as st
from PyPDF2 import PdfReader
import os
from anthropic import Anthropic
from io import BytesIO



client = anthropic.Anthropic(

)

def ask_claude(prompt, model="claude-3-opus-20240229"):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        system="ff",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def analyze_pdf(file_param):
    pdf_reader = PdfReader(file_param)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    },
                    {
                        "type": "text",
                        "text": "Please summarize the content of this PDF."
                    },
                ]
            }
        ]
    )

    return message.content[0].text

st.set_page_config(page_title="Analyser un PDF")
st.title("Analyser un PDF")
uploaded_file = st.file_uploader("Choisissez un fichier PDF.", type=["pdf"])

if uploaded_file is not None:
    pdf_file = BytesIO(uploaded_file.getvalue())

    if st.button("Analyser le PDF"):
        with st.spinner("Analyse en cours..."):
            analysis = analyze_pdf(pdf_file)
            st.subheader("Résultats de l'analyse:")
            st.write(analysis)