import streamlit as st
import requests

st.title("Spam Detection App")

text = st.text_area("Enter message")

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"text": text}
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
        st.info(f"Confidence: {result['confidence']}")
    else:
        st.error("API error")
