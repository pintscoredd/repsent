from utils.formatting import print_header, print_table
from engines.polymarket_signal import detect_anomalies

def execute_poly(topic: str):
    print_header(f"POLYMARKET ANOMALY DETECTION{': ' + topic.upper() if topic else ''}")
    anomalies = detect_anomalies()
    if not anomalies:
        return
        
    rows = [[a["Market"], a["Volume"], a["Signal"]] for a in anomalies]
    print_table("Detected Signals", ["Market", "Volume", "Signal"], rows)
