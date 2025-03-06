import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff, IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6, _ICMPv6  # Import IPv6 and ICMPv6 separately
import threading

def packet_callback(packet):
    if packet.haslayer(IP) or packet.haslayer(IPv6):  # Check for both IPv4 and IPv6
        protocol = "Other"

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP) or packet.haslayer(_ICMPv6):  # Check for ICMP and ICMPv6
            protocol = "ICMP"

        # Extract IP addresses based on packet type
        if packet.haslayer(IP):  # IPv4 Packet
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
        elif packet.haslayer(IPv6):  # IPv6 Packet
            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst

        display_text = f"{protocol} Packet: {src_ip} -> {dst_ip}\n"
        display_text1 = f"{packet}\n"
        text_area.insert(tk.END, display_text)
        text_area.see(tk.END)
        text_area1.insert(tk.END, display_text1)
        text_area1.see(tk.END)
def start_sniffing():
    global sniffing
    sniffing = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    thread = threading.Thread(target=sniffer, daemon=True)  # Daemon thread to run in background
    thread.start()

def sniffer():
    sniff(prn=packet_callback, store=False, stop_filter=lambda x: not sniffing)

def stop_sniffing():
    global sniffing
    sniffing = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Network Sniffer")
root.geometry("1000x750")

start_button = tk.Button(root, text="Start Sniffing", command=start_sniffing)
start_button.grid(row=0, column=0)

stop_button = tk.Button(root, text="Stop Sniffing", command=stop_sniffing, state=tk.DISABLED)
stop_button.grid(row=0, column=1)

text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.grid(row=1, column=0, sticky="N,E,NS")

text_area1 = scrolledtext.ScrolledText(root, width=60, height=20)
text_area1.grid(row=1, column=1, sticky="N,W,NS")

text_area2 = scrolledtext.ScrolledText(root, width=60, height=20)
text_area2.grid(row=2, column=0, sticky="S,E,NS")

text_area3 = scrolledtext.ScrolledText(root, width=60, height=20)
text_area3.grid(row=2, column=1, sticky="S,W,NS")

root.mainloop()
