
import streamlit as st
import spacy

nlp = spacy.load("en_core_web_sm")

st.title("📄 Contract Risk Analyzer")

file = st.file_uploader("Upload contract", type=["txt"])

if file:
    text = file.read().decode()

    st.subheader("Summary")
    st.write(text[:300])

    doc = nlp(text)

    st.subheader("Entities Found")
    for ent in doc.ents:
        st.write(ent.text, ent.label_)

    risk = 0
    if "penalty" in text.lower():
        risk += 2
    if "terminate" in text.lower():
        risk += 2

    st.subheader("Risk Score")
    st.write(risk)
