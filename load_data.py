# Placeholder data loader - in real use replace with parsers for CIC-IDS, netflow, pcap using scapy.
import pandas as pd
import numpy as np

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

if __name__ == '__main__':
    df = load_dummy(200)
    print(df.head())
