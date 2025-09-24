# Simple training script: generates synthetic 'network' data, trains a RandomForest, and saves model+scaler.
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

OUT = Path(__file__).parents[0]
MODEL_FILE = OUT / "model.pkl"
SCALER_FILE = OUT / "scaler.pkl"

def gen_synthetic(n=2000, seed=42):
    rng = np.random.RandomState(seed)
    # features: pkt_size_mean, pkt_count, unique_src_ips, tcp_flag_ratio, avg_interval
    X = np.zeros((n,5))
    X[:,0] = rng.normal(500, 200, size=n) / 1500  # normalized pkt size
    X[:,1] = rng.poisson(5, size=n) / 50          # pkt count normalized
    X[:,2] = rng.randint(1,10,size=n) / 10
    X[:,3] = rng.beta(2,5,size=n)
    X[:,4] = rng.exponential(1.0, size=n) / 10
    # label: attacks have higher pkt_count and tcp_flag_ratio
    y = ((X[:,1] > 0.1) & (X[:,3] > 0.2)).astype(int)
    return X, y

if __name__ == '__main__':
    X,y = gen_synthetic(3000)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=7)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    clf = RandomForestClassifier(n_estimators=100, random_state=0)
    clf.fit(X_train_s, y_train)
    preds = clf.predict(X_test_s)
    print(classification_report(y_test, preds))
    joblib.dump(clf, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    print("Saved model to", MODEL_FILE)
