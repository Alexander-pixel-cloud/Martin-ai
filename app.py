import streamlit as st
from utils import analyze_text, sentence_analysis
import base64

# Load custom CSS
with open("custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧠 AI Text Detector")
st.markdown("Deteksi apakah teks ditulis oleh AI atau manusia. Powered by lightweight AI heuristics.")

text_input = st.text_area("📄 Masukkan teks kamu di sini:", height=250)

if st.button("🚀 Deteksi Sekarang"):
    if len(text_input.strip()) == 0:
        st.warning("⚠️ Masukkan teks dulu dong.")
    else:
        ai_score, readability, perplexity, burstiness = analyze_text(text_input)
        st.subheader(f"🎯 Skor Kemungkinan AI: {ai_score:.2f}%")
        st.markdown(f"- **Readability**: {readability:.2f}")
        st.markdown(f"- **Perplexity**: {perplexity:.2f}")
        st.markdown(f"- **Burstiness**: {burstiness:.2f}")

        if ai_score > 75:
            st.error("⚠️ Teks ini kemungkinan besar ditulis oleh AI.")
        elif ai_score > 50:
            st.warning("⚠️ Teks ini mungkin campuran AI dan manusia.")
        else:
            st.success("✅ Teks ini kemungkinan besar ditulis oleh manusia.")

        st.markdown("---")
        st.subheader("🔎 Analisis per Kalimat:")
        results = sentence_analysis(text_input)
        for sent, is_ai in results:
            if is_ai:
                st.markdown(f'<div class="ai-sent">🧠 {sent}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="human-sent">👤 {sent}</div>', unsafe_allow_html=True)
