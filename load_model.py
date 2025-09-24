import joblib
from pathlib import Path
MODEL_FILE = Path(__file__).parents[0] / "model.pkl"
SCALER_FILE = Path(__file__).parents[0] / "scaler.pkl"

def load():
    model = None
    scaler = None
    try:
        model = joblib.load(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
    except Exception as e:
        print("No model found:", e)
    return model, scaler

if __name__ == '__main__':
    m,s = load()
    print("Model loaded?", m is not None)
