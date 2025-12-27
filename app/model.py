import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "spam_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "artifacts", "vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

def predict_spam(text: str):
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    pred = model.predict(X)[0]

    label = "spam" if pred == 1 else "ham"
    confidence = float(max(probs))

    return label, confidence
