from fastapi import FastAPI
from app.schema import SpamRequest, SpamResponse
from app.model import predict_spam   # ✅ CORRECT IMPORT

app = FastAPI(title="Spam Detection API")

@app.get("/")
def home():
    return {"message": "Welcome to the Spam Detection API"}

@app.post("/predict", response_model=SpamResponse)
def predict(request: SpamRequest):
    label, confidence = predict_spam(request.text)
    return {
        "prediction": label,
        "confidence": confidence
    }
