import textstat
import streamlit as st

st.set_page_config(page_title="AI Text Detector", layout="centered")
st.title("🧠 AI Text Detector")
st.markdown("Masukkan teks, lalu klik 'Deteksi' untuk melihat apakah teks kemungkinan buatan AI.")

text_input = st.text_area("📄 Teks", height=250)

def analyze_text(text):
    try:
        readability = textstat.flesch_reading_ease(text)
    except:
        readability = 0
    unique_words = len(set(text.split())) / (len(text.split()) + 1) * 100
    length_penalty = max(0, (len(text) - 1000) / 1000 * 10)
    ai_score = (100 - readability + (100 - unique_words) + length_penalty) / 3
    ai_score = max(0, min(ai_score, 100))
    return ai_score

if st.button("🚀 Deteksi"):
    if len(text_input.strip()) == 0:
        st.warning("Masukkan teks terlebih dahulu.")
    else:
        score = analyze_text(text_input)
        st.subheader(f"🔍 Skor Kemungkinan AI: {round(score, 2)}%")
        if score > 75:
            st.error("⚠️ Teks ini kemungkinan besar ditulis oleh AI.")
        elif score > 50:
            st.warning("⚠️ Teks ini mungkin campuran AI dan manusia.")
        else:
            st.success("✅ Teks ini kemungkinan besar ditulis oleh manusia.")
