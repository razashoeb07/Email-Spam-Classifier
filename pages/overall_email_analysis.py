import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Email Spam Classifier Dashboard")
st.markdown("### 🔍 Analyze and classify emails as Spam or Ham")

# Updated stats
total_emails = 5572
spam_percentage = 12.63 / 100
spam_emails = int(total_emails * spam_percentage)
ham_emails = total_emails - spam_emails
unique_words = 8271

# Summary stats dictionary
stats = {
    "Total Emails": total_emails,
    "Spam Emails": f"{spam_emails} ({spam_percentage*100:.2f}%)",
    "Ham Emails": f"{ham_emails} ({(1 - spam_percentage)*100:.2f}%)",
    "Unique Words": unique_words,
    "Most Common Spam Word": "free",
    "Most Common Ham Word": "meeting"
}

# Convert and force string type to prevent Arrow conversion error
df_stats = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
df_stats["Value"] = df_stats["Value"].astype(str)
st.dataframe(df_stats,use_container_width=True)

# Pie Chart
st.subheader("🧁 Spam vs Ham Distribution")
fig1, ax1 = plt.subplots()
ax1.pie([spam_emails, ham_emails], labels=['Spam', 'Ham'], autopct='%1.1f%%',
        colors=['#ff9999', '#66b3ff'], startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

