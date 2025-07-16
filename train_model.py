import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load CSV dataset
url = "https://raw.githubusercontent.com/Kamalsharma0/Python-/refs/heads/main/Data%20Sets/UpdatedResumeDataSet.csv"
df = pd.read_csv(url)

# Extract relevant columns
df = df[['Category', 'Resume']]

# Vectorize resume text
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Resume'])
y = df['Category']

# Split for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "resume_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and Vectorizer saved successfully!")
