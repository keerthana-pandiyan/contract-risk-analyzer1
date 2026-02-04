import streamlit as st
import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

# -------- CSS ----------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#667eea,#764ba2);
}

h1 {
    text-align:center;
    color:#6C63FF;
}

.upload-text {
    text-align:center;
    font-size:20px;
    color:#333;
    font-weight:bold;
}

.summary-box {
    background:#f0f2ff;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #6C63FF;
}

.entities-box {
    background:#fff4f4;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #ff4b4b;
}

</style>
""", unsafe_allow_html=True)

# -------- Layout ----------
col1, col2 = st.columns([1,2])

with col1:
    # Animated man GIF
    st.image(
        "https://img.freepik.com/premium-vector/boy-pointing-right-with-yellow-background_723224-1521.jpg",
        width=200
    )

with col2:
    st.title("📄 Contract Risk Analyzer")

st.markdown(
    "<div class='upload-text'>👇 Upload your contract here</div>",
    unsafe_allow_html=True
)

# -------- Upload ----------
file = st.file_uploader("📂 Upload contract", type=["txt"])

if file:
    text = file.read().decode()

    st.subheader("Summary")
    st.markdown(
        f"<div class='summary-box'>{text[:300]}</div>",
        unsafe_allow_html=True
    )

    doc = nlp(text)

    st.subheader("Entities Found")
    st.markdown("<div class='entities-box'>", unsafe_allow_html=True)

    for ent in doc.ents:
        st.write(f"**{ent.text}** → {ent.label_}")

    st.markdown("</div>", unsafe_allow_html=True)
