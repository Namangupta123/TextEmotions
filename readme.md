# Text Emotion Prediction API

This project is a machine learning application that predicts emotions from text input. It consists of a trained model that can classify text into different emotion categories and a FastAPI-based REST API for serving predictions.

## Project Overview

The system can identify 8 different emotions from text:
- Joy
- Sadness
- Fear
- Anger
- Surprise
- Neutral
- Disgust
- Shame

## Project Structure

```
├── api/
│   └── main.py          # FastAPI application
├── data/
│   └── emotion_dataset_raw.csv  # Dataset used for training
├── model/
│   └── Text_emotions_model.pkl  # Trained model file
├── notebook/
│   └── Model_training.ipynb     # Jupyter notebook with model training process
├── python-version               # Python version specification
├── readme.md                    # This file
└── requirements.txt             # Project dependencies
```

## Dataset

The model was trained on a dataset containing text samples labeled with emotions. The dataset includes 34,792 entries across 8 emotion categories with the following distribution:
- Joy: 11,045 samples
- Sadness: 6,722 samples
- Fear: 5,410 samples
- Anger: 4,297 samples
- Surprise: 4,062 samples
- Neutral: 2,254 samples
- Disgust: 856 samples
- Shame: 146 samples

## Model Training

The model training process is documented in the Jupyter notebook `notebook/Model_training.ipynb`. The notebook includes:
- Data loading and exploration
- Data preprocessing
- Model training
- Model evaluation
- Model serialization

## API

The API is built using FastAPI and provides endpoints for emotion prediction.

### Endpoints

- `GET /`: Health check endpoint
- `POST /predict`: Endpoint for emotion prediction

### Request Format for Prediction

```json
{
  "text": "Your text here"
}
```

### Response Format

```json
{
  "Emotion": "The predicted emotion"
}
```

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:
   ```bash
   cd api
   python main.py
   ```
   The API will be available at http://localhost:8000

## Dependencies

- seaborn
- neattext
- joblib
- pandas
- scikit-learn
- numpy
- fastapi
- uvicorn
- pydantic

## Usage Examples

### Using curl

```bash
CURL -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text":"I am so happy today!"}'
```

### Using Python requests

```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={"text": "I am so happy today!"}
)

print(response.json())
```

### Social Handles

- [GitHub](https://github.com/NamanGupta)
- [LinkedIn](https://github.com/RohanGupta)
- [Twitter](https://github.com/NamanGupta)
- [Email](mailto:namanguptacse0330@gmail.com)
