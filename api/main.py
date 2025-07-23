import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app= FastAPI(title="Text Prediction API")

class PredictionRequest(BaseModel):
    text: str

with open("model/Text_emotions_model.pkl", "rb") as f:
    model = joblib.load(f)

@app.post("/predict")
async def predict(request: PredictionRequest):
    input_text = request.text
    prediction = model.predict([input_text])
    return {"Emotion": prediction[0]}

@app.get("/")
def health_check():
    return {"status": "Emotion Prediction API is running"}

if __name__ == "__main__":
    print("Starting the Emotion Prediction API...")
    uvicorn.run(app, host="0.0.0.0", port=8000)