import streamlit as st
import pickle
import time


# ✅ Load Model & Vectorizer
with open("vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 📩 Title Section
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>📩 Email/SMS Spam Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Enter a message to check if it is Spam or Ham</p>", unsafe_allow_html=True)

# 📑 Message Input
message = st.text_area("Enter the message here 👇", height=100)

# 🎚️ Spam Probability Threshold
threshold = st.slider("⚙️ Adjust Spam Probability Threshold", 0.1, 0.9, 0.4, 0.05)

# ✅ Maintain button state
if "prediction_made" not in st.session_state:
    st.session_state.prediction_made = False

# 🛠️ Prediction Button
predict_btn = st.button("🔍 Predict")

if predict_btn:
    if message.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        st.session_state.prediction_made = True  # Mark prediction as made

if st.session_state.prediction_made:
    vector_input = tfidf.transform([message])
    prob = model.predict_proba(vector_input)[0]
    spam_prob = prob[1]

    result = "🚨 Spam Message!" if spam_prob > threshold else "✅ Safe (Ham) Message"

    with st.spinner("Analyzing message..."):
        time.sleep(1)

    st.markdown(f"""
    <div style='background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); text-align: center;'>
        <h2 style='color: {"#ff4b4b" if spam_prob > threshold else "#2ecc71"};'>{result}</h2>
        <p style='font-size: 18px;'><b>Spam Probability:</b> {spam_prob:.4f}</p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(spam_prob)

st.markdown("<p style='text-align: center; font-size: 16px;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
