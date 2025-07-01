import streamlit as st

st.set_page_config(page_title="Email Spam Classifier", page_icon="📩", layout="centered")

# Pages
from pathlib import Path
Page = st.Page

overall_email_analysis_page = Page("pages/overall_email_analysis.py", title="📊 Spam Overview", icon="📬",default=True)
stats_page = Page("pages/spam_stats.py", title="Spam Statistics", icon=":material/insights:")
check_page = Page("pages/email_spam_classifire.py", title="Check an Email", icon=":material/mark_email_read:")
chat_bot_page = Page("pages/chat_bot.py", title="Chat Bot", icon=":material/smart_toy:")

freq_page = Page("pages/word_freq.py", title="Word Frequencies", icon=":material/bar_chart:")
trend_page = Page("pages/spam_trends.py", title="Overall Spam Trends", icon=":material/trending_up:")
model_frequency_page = Page("pages/model_frequency.py", title="Algorithm Accuracy", icon=":material/check_circle:")
about_page = Page("pages/about_me.py", title="About Me", icon=":material/account_circle:")

sections = {
    "Info": [about_page, overall_email_analysis_page],
    "Analysis": [stats_page, freq_page, trend_page,model_frequency_page],
    "Tools": [check_page,chat_bot_page],
}

pg = st.navigation(sections, position="sidebar")

st.logo("assets/codingisfun_logo.png")

st.sidebar.markdown("Made with ❤️ by Shoeb Raza")

pg.run()
