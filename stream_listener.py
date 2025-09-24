# Minimal placeholder for a stream listener that would parse pcap/netflow.
# For now it simulates reading packets and printing feature vectors.
import time, random

def simulate_stream(n=10, delay=1.0):
    for i in range(n):
        # fake features: [pkt_size_mean, pkt_count, unique_src_ips, tcp_flag_ratio]
        features = [random.random(), random.randint(1,10), random.randint(1,5), random.random()]
        print("FRAME", i, "->", features)
        time.sleep(delay)

if __name__ == '__main__':
    simulate_stream(20, 0.5)
