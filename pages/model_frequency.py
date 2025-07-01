import streamlit as st
import pandas as pd

st.subheader("Algorithm Frequency")

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

df = pd.DataFrame(data)  # directly convert dictionary to dataframe
st.table(df)



