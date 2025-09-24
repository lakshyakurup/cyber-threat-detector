# Cybersecurity Threat Detector (Starter + Prototype)

This repository contains two levels of starter content:

1. **Minimal & Runnable** - a tiny FastAPI app that accepts feature JSON and returns a dummy prediction.
2. **Semi-working Prototype** - a simple scikit-learn model training script that creates synthetic network-like features, trains a RandomForest, and saves the model + scaler.

## Structure
```
cyber-threat-detector/
├── app/
│   ├── api.py
│   └── stream_listener.py
├── models/
│   ├── train.py
│   └── load_model.py
├── scripts/
│   ├── load_data.py
│   └── eval.py
├── ui/
│   └── dashboard.py
├── data/               # add real datasets here
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Quick start (minimal app)
1. Create and activate a virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run the API:
   ```bash
   uvicorn app.api:app --reload --port 8000
   ```
3. Test:
   ```bash
   curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"features":[0.1,0.2,0.3,0.4]}'
   ```

## Prototype training
Train a small RandomForest on synthetic data and produce `models/model.pkl` and `models/scaler.pkl`:
```bash
python models/train.py
```
Then run the API; it will automatically use the saved model if present.

## Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - cyber threat starter"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cyber-threat-detector.git
git push -u origin main
```
