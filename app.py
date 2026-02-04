import streamlit as st
import re

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
.risk-box {
    background:#fff4f4;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #ff4b4b;
}
.entity-box {
    background:#f4fff6;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #28a745;
}
</style>
""", unsafe_allow_html=True)

# -------- Layout ----------
col1, col2 = st.columns([1,2])

with col1:
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

    # -------- Summary ----------
    st.subheader("Summary")
    st.markdown(
        f"<div class='summary-box'>{text[:300]}</div>",
        unsafe_allow_html=True
    )

    # -------- Fake Entity Detection ----------
    st.subheader("Entities Found")

    names = re.findall(r'[A-Z][a-z]+', text)
    dates = re.findall(r'\d{1,2}/\d{1,2}/\d{2,4}', text)

    st.markdown("<div class='entity-box'>", unsafe_allow_html=True)

    if names:
        st.write("👤 Names detected:")
        for n in set(names[:5]):
            st.write("-", n)

    if dates:
        st.write("📅 Dates detected:")
        for d in dates:
            st.write("-", d)

    st.markdown("</div>", unsafe_allow_html=True)

    # -------- Risk Detection ----------
    risk_words = [
        "penalty","terminate","liability","breach",
        "damages","lawsuit","fine","legal action"
    ]

    found_risks = [w for w in risk_words if w in text.lower()]

    st.subheader("⚠️ Risks Found")
    st.markdown("<div class='risk-box'>", unsafe_allow_html=True)

    if found_risks:
        for word in found_risks:
            st.write(f"⚠️ Risk keyword: **{word}**")
    else:
        st.write("✅ No major risks detected")

    st.markdown("</div>", unsafe_allow_html=True)
