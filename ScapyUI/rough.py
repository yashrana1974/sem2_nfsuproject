import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff, IP, TCP, UDP, ICMP
import threading

def packet_callback(packet):
    if packet.haslayer(IP):
        protocol = "Other"
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        display_text = f"{protocol} Packet: {src_ip} -> {dst_ip}\n"
        text_area.insert(tk.END, display_text)
        text_area.see(tk.END)

def start_sniffing():
    global sniffing
    sniffing = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    thread = threading.Thread(target=sniffer)
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
root.geometry("500x400")

start_button = tk.Button(root, text="Start Sniffing", command=start_sniffing)
start_button.pack()

stop_button = tk.Button(root, text="Stop Sniffing", command=stop_sniffing, state=tk.DISABLED)
stop_button.pack()

text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.pack()

root.mainloop()