import streamlit as st
import pandas as pd
import altair as alt

# Title
st.title("📊 Spam vs Ham Emails (2015–2024)")

# Data
years = list(range(2015, 2025))
spam = [100 + i*10 for i in range(len(years))]
ham = [300 + i*15 for i in range(len(years))]

df = pd.DataFrame({
    "Year": years * 2,
    "Count": spam + ham,
    "Type": ["Spam"] * len(years) + ["Ham"] * len(years)
})

# Altair line chart
chart = alt.Chart(df).mark_line(point=True).encode(
    x="Year:O",
    y="Count:Q",
    color="Type:N",
    tooltip=["Year", "Type", "Count"]
).interactive()

st.altair_chart(chart, use_container_width=True)

# Year selector
selected_year = st.selectbox("📅 Select a year to see data:", years)

# Filter and display data
filtered = df[df["Year"] == selected_year]
st.write(f"### 📌 Email Data for Year: {selected_year}")
st.table(filtered)
