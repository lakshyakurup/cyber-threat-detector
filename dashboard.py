# Minimal Streamlit dashboard to show fake/live predictions
import streamlit as st
import numpy as np
import requests
st.title('Cyber Threat Detector - Demo Dashboard')

st.write('This dashboard demonstrates using the /predict API.')

col1, col2 = st.columns(2)
with col1:
    pkt_size = st.slider('Packet size mean (normalized)', 0.0, 1.0, 0.3)
    pkt_count = st.slider('Packet count (normalized)', 0.0, 1.0, 0.1)
    uniq_ips = st.slider('Unique src IPs (normalized)', 0.0, 1.0, 0.2)
    tcp_ratio = st.slider('TCP flag ratio', 0.0, 1.0, 0.1)
    avg_int = st.slider('Avg interval (normalized)', 0.0, 1.0, 0.1)
    if st.button('Send to API'):
        payload = {'features':[pkt_size, pkt_count, uniq_ips, tcp_ratio, avg_int]}
        try:
            res = requests.post('http://127.0.0.1:8000/predict', json=payload, timeout=5)
            st.json(res.json())
        except Exception as e:
            st.error('API request failed: ' + str(e))
with col2:
    st.write('Instructions:')
    st.write('1. Run the API: `uvicorn app.api:app --reload`')
    st.write('2. Run this dashboard: `streamlit run ui/dashboard.py`')
