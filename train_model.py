import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("cyber_threats.csv")

# Convert textual descriptions into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Description"])
y = df["Category"]

# Train Naïve Bayes model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, "threat_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model training complete. Saved as threat_model.pkl")
