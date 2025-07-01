import streamlit as st
import pandas as pd

st.title("📈 Top Spam Words")

top_spam_words = ["free", "win", "offer", "urgent", "money"]
top_word_counts = [320, 270, 250, 180, 160]

df = pd.DataFrame({
    "Word": top_spam_words,
    "Count": top_word_counts
})

st.bar_chart(df.set_index("Word"))
