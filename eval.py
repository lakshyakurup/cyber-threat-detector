# Simple evaluator that loads model from models/ and evaluates on synthetic test data
from models.load_model import load
import numpy as np
from sklearn.metrics import classification_report
from models.train import gen_synthetic

if __name__ == '__main__':
    model, scaler = load()
    X,y = gen_synthetic(500, seed=99)
    if scaler is not None:
        X = scaler.transform(X)
    if model is None:
        print('No trained model found. Run python models/train.py first.')
    else:
        preds = model.predict(X)
        print(classification_report(y,preds))
