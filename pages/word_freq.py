import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📗 Top Frequent Words in Ham Messages")

# Sample Top Ham Words & Frequencies (you can update the real data)
top_ham_words = [
    'ok', 'go', 'come', 'got', 'know', 'love', 'good', 'time', 'day', 'going',
    'home', 'now', 'will', 'later', 'see', 'yeah', 'need', 'night', 'much', 'wait'
]
top_ham_counts = [
    290, 275, 260, 240, 230, 225, 220, 210, 200, 195,
    190, 185, 180, 170, 165, 160, 155, 150, 145, 140
]

# Create DataFrame
df_ham = pd.DataFrame({
    "Word": top_ham_words,
    "Count": top_ham_counts
})

# Plot
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
bars = sns.barplot(x="Word", y="Count", data=df_ham, hue="Word", palette="Greens_d", legend=False)


# Add value labels
for bar in bars.patches:
    bars.annotate(
        str(bar.get_height()),
        (bar.get_x() + bar.get_width() / 2, bar.get_height() + 5),
        ha='center', va='center', fontsize=8, color='black'
    )

plt.xticks(rotation=45, ha='right')
plt.title("Top 20 Frequent Words in Ham Messages", fontsize=16)
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()


st.pyplot(plt)
