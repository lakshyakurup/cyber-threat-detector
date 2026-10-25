# Cybersecurity Threat Detector Engine - Ingestion Module
import pandas as pd
import numpy as np
from pathlib import Path

FEATURE_COLUMNS = ["pkt_size_mean", "pkt_count", "unique_src_ips", "tcp_flag_ratio", "avg_interval"]

def load_dummy(n=1000):
    rng = np.random.RandomState(0)
    df = pd.DataFrame({
        'pkt_size_mean': rng.normal(500,100,size=n),
        'pkt_count': rng.poisson(5,size=n),
        'unique_src_ips': rng.randint(1,5,size=n),
        'tcp_flag_ratio': rng.rand(n),
        'avg_interval': rng.exponential(1.0,size=n),
    })
    # create a label similar to train.py
    df['label'] = ((df['pkt_count']>6) & (df['tcp_flag_ratio']>0.4)).astype(int)
    return df


def load_csv(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = set(FEATURE_COLUMNS) - set(frame.columns)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")
    return frame


def prepare_features(frame: pd.DataFrame) -> tuple[np.ndarray, np.ndarray | None]:
    features = frame[FEATURE_COLUMNS].to_numpy(dtype=float)
    labels = frame["label"].to_numpy(dtype=int) if "label" in frame else None
    return features, labels

if __name__ == '__main__':
    df = load_dummy(200)
    print(df.head())
