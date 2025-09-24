from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os
from pathlib import Path

app = FastAPI(title="Cyber Threat Detector - Minimal API")

MODEL_PATH = Path(__file__).parents[1] / "models" / "model.pkl"
SCALER_PATH = Path(__file__).parents[1] / "models" / "scaler.pkl"

class Features(BaseModel):
    features: list

# Try to load model if exists
model = None
scaler = None
try:
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
    if SCALER_PATH.exists():
        scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print("Warning: couldn't load model:", e)

@app.get("/")
def root():
    return {"status":"ok", "info":"Send POST /predict with JSON {features: [...]}"}

@app.post("/predict")
def predict(payload: Features):
    x = np.array(payload.features, dtype=float).reshape(1, -1)
    if scaler is not None:
        try:
            x = scaler.transform(x)
        except Exception:
            pass
    if model is not None:
        score = float(model.predict_proba(x)[0][1])
        label = int(score > 0.5)
        return {"threat": bool(label), "score": score}
    # fallback dummy logic: threat if mean(feature) > 0.5
    score = float(x.mean())
    return {"threat": bool(score > 0.5), "score": score}
