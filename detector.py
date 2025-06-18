# detector.py
from scapy.all import sniff, IP, TCP
import threading

alerts = []

def detect(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            if dport == 22 or dport == 23:  # Example: suspicious ports
                alert = f"⚠️ Suspicious TCP connection from {ip_src} to {ip_dst}:{dport}"
                alerts.append(alert)
                print(alert)

def start_sniffing():
    sniff(filter="ip", prn=detect, store=0)

def get_alerts():
    return alerts[-10:]  # Show last 10 alerts
