import time
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from difflib import get_close_matches

# --------------------------
# FAQ dictionary with special triggers
# --------------------------
project_faq = {
    "name": "The project is called **Email Spam Classifier**.",
    "describe": "This project uses NLP techniques to classify emails as spam or not spam.",
    "technologies": "Technologies used include Python, Scikit-learn, Pandas, NumPy, NLTK or SpaCy, and Streamlit.",
    "goal": "The goal is to detect and filter spam emails using machine learning models.",
    "deployment": "Yes, it’s deployed using Streamlit for real-time email input and classification.",

    # Triggers for spam words chart
    "top spam words": "Here's a visual of the most common spam words found in emails.",
    "common spam words": "Here's a visual of the most common spam words found in emails.",
    "spam keywords": "Here's a visual of the most common spam words found in emails.",

    # Triggers for spam vs ham trend chart
    "spam vs ham trend": "__show_spam_ham_chart__",
    "spam vs ham over time": "__show_spam_ham_chart__",
    "spam and ham comparison": "__show_spam_ham_chart__",
    "emails trend": "__show_spam_ham_chart__",
    "email trends": "__show_spam_ham_chart__",

    # Triggers for ham words chart
    "top ham words": "__show_top_ham_words_chart__",
    "common ham words": "__show_top_ham_words_chart__",
    "ham keywords": "__show_top_ham_words_chart__",
    "ham words": "__show_top_ham_words_chart__",

    # Triggers for algorithm frequency table
    "algorithm frequency": "__show_algorithm_freq_table__",
    "algorithm performance": "__show_algorithm_freq_table__",
    "model accuracy": "__show_algorithm_freq_table__",
    "model precision": "__show_algorithm_freq_table__",
    "algorithm table": "__show_algorithm_freq_table__",
}

# --------------------------
# Typing animation generator
# --------------------------
def response_generator(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.03)

# --------------------------
# Show Top Spam Words Bar Chart
# --------------------------
def show_spam_words_chart():
    top_spam_words = ["free", "win", "offer", "urgent", "money"]
    top_word_counts = [320, 270, 250, 180, 160]
    df = pd.DataFrame({
        "Word": top_spam_words,
        "Count": top_word_counts
    })
    st.bar_chart(df.set_index("Word"))

# --------------------------
# Show Spam vs Ham Trend Line Chart
# --------------------------
def show_spam_vs_ham_chart():
    years = list(range(2015, 2025))
    spam = [100 + i*10 for i in range(len(years))]
    ham = [300 + i*15 for i in range(len(years))]

    df = pd.DataFrame({
        "Year": years * 2,
        "Count": spam + ham,
        "Type": ["Spam"] * len(years) + ["Ham"] * len(years)
    })

    chart = alt.Chart(df).mark_line(point=True).encode(
        x="Year:O",
        y="Count:Q",
        color="Type:N",
        tooltip=["Year", "Type", "Count"]
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

# --------------------------
# Show Top Ham Words Bar Chart (matplotlib + seaborn)
# --------------------------
def show_top_ham_words_chart():
    top_ham_words = [
        'ok', 'go', 'come', 'got', 'know', 'love', 'good', 'time', 'day', 'going',
        'home', 'now', 'will', 'later', 'see', 'yeah', 'need', 'night', 'much', 'wait'
    ]
    top_ham_counts = [
        290, 275, 260, 240, 230, 225, 220, 210, 200, 195,
        190, 185, 180, 170, 165, 160, 155, 150, 145, 140
    ]

    df_ham = pd.DataFrame({
        "Word": top_ham_words,
        "Count": top_ham_counts
    })

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    bars = sns.barplot(x="Word", y="Count", data=df_ham, palette="Greens_d")

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
    plt.clf()  # Clear the plot after displaying to avoid overlaps

# --------------------------
# Show Algorithm Frequency Table
# --------------------------
def show_algorithm_frequency():
    data = {
        "Model": [
            "SVC", "KNN", "Naive Bayes", "Decision Tree", "Logistic Regression",
            "Random Forest", "AdaBoost", "Bagging Classifier",
            "Extra Trees Classifier", "Gradient Boosting", "XGBoost"
        ],
        "Accuracy": [
            0.8665, 0.9342, 0.9410, 0.9449, 0.9613,
            0.9691, 0.9642, 0.9662, 0.9787, 0.9516, 0.9691
        ],
        "Precision": [
            0.0, 0.8182, 1.0, 0.8857, 0.9623,
            0.9818, 0.9316, 0.8992, 0.9754, 0.9314, 0.9417
        ]
    }
    df = pd.DataFrame(data)
    st.subheader("Algorithm Frequency and Performance")
    st.dataframe(df)

# --------------------------
# Main Chatbot App
# --------------------------
st.title("📬 Email Spam Classifier Q&A Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past messages & charts if any
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("show_chart") == "spam_words":
            show_spam_words_chart()
        elif message.get("show_chart") == "spam_vs_ham":
            show_spam_vs_ham_chart()
        elif message.get("show_chart") == "ham_words":
            show_top_ham_words_chart()
        elif message.get("show_chart") == "algorithm_freq":
            show_algorithm_frequency()

# Chat input
if prompt := st.chat_input("Ask me about the Email Spam Classifier project..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower()
    matches = get_close_matches(prompt_lower, project_faq.keys(), n=1, cutoff=0.4)

    if matches:
        response = project_faq[matches[0]]

        with st.chat_message("assistant"):

            # Handle special triggers to show charts/tables
            if response == "__show_spam_ham_chart__":
                message_placeholder = st.empty()
                full_response = "Here's the trend of spam vs ham emails over the years."
                for chunk in response_generator(full_response):
                    message_placeholder.markdown(chunk)
                    time.sleep(0.03)
                show_spam_vs_ham_chart()
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response,
                    "show_chart": "spam_vs_ham"
                })

            elif response == "Here's a visual of the most common spam words found in emails.":
                message_placeholder = st.empty()
                full_response = ""
                for chunk in response_generator(response):
                    full_response += chunk
                    message_placeholder.markdown(full_response)
                show_spam_words_chart()
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response,
                    "show_chart": "spam_words"
                })

            elif response == "__show_top_ham_words_chart__":
                message_placeholder = st.empty()
                full_response = "Here are the top frequent words found in ham messages."
                for chunk in response_generator(full_response):
                    message_placeholder.markdown(chunk)
                    time.sleep(0.03)
                show_top_ham_words_chart()
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response,
                    "show_chart": "ham_words"
                })

            elif response == "__show_algorithm_freq_table__":
                message_placeholder = st.empty()
                full_response = "Here is the algorithm frequency table with accuracy and precision scores."
                for chunk in response_generator(full_response):
                    message_placeholder.markdown(chunk)
                    time.sleep(0.03)
                show_algorithm_frequency()
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response,
                    "show_chart": "algorithm_freq"
                })

            else:
                # Normal text response with typing effect
                message_placeholder = st.empty()
                full_response = ""
                for chunk in response_generator(response):
                    full_response += chunk
                    message_placeholder.markdown(full_response)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })

    else:
        with st.chat_message("assistant"):
            st.markdown("Sorry, I don’t have an answer for that. Please try asking something else.")

