import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# ✅ Load dataset correctly
df = pd.read_csv("C:\\Users\\shoeb\\Desktop\\spam.csv", encoding="latin1")

# ✅ Fix column names
df = df.rename(columns={"v1": "label", "v2": "message"})

# ✅ Convert labels to binary
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# ✅ Text Data
X = df["message"]
y = df["label"]

# ✅ TF-IDF Vectorization with bigrams
tfidf = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
X_tfidf = tfidf.fit_transform(X)

# ✅ Balance Data Using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_tfidf, y)

# ✅ Train Model
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# ✅ Save Model & Vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model retrained and saved successfully!")
