from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
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
            
        if bsniffing == True:
            display_text1 = f"{protocol} Packet: {src_ip} -> {dst_ip}\n"
            text_area1.insert(END, display_text1)
            text_area1.see(END)
            text_area2.insert(END, display_text1)
            text_area2.see(END)
            text_area3.insert(END, display_text1)
            text_area3.see(END)
            text_area4.insert(END, display_text1)
            text_area4.see(END) 
        
        display_text = f"{packet}\n"
        text_area.insert(END, display_text)
        text_area.see(END)
        
def start_sniffing():
    global sniffing
    sniffing = True
    text_area.config(state=NORMAL)
    start_button.config(state=DISABLED)
    stop_button.config(state=NORMAL)
    thread = threading.Thread(target=sniffer, daemon=True)  # Daemon thread to run in background
    thread.start()

def sniffer():
    sniff(prn=packet_callback, store=False, stop_filter=lambda x: not sniffing)

def stop_sniffing():
    global sniffing
    sniffing = False
    text_area.config(state=DISABLED)
    start_button.config(state=NORMAL)
    stop_button.config(state=DISABLED)
    
def aboutwindow():
    about = Tk()
    about.title("ScapyUI - About Tool")
    about.geometry("500x360")
    
    #Image icon for tool icon
    root.iconbitmap("C:\\Users\\ranay\\OneDrive\\Documents\\GitHub\\sem2_nfsuproject\\ScapyUI\\res\\logo.ico")
    
    info_area = scrolledtext.ScrolledText(about, width=60, height=20)
    info_area.grid(row=0, column=0, sticky="W,E,N,S")
    
    #creating a quit button
    buttonQuit = Button(about, text="Exit Program", command=about.destroy)
    buttonQuit.grid(row=1, column=0, sticky="W,E,N,S")

    
    about.mainloop()
    
def bstart_sniffing():
    global bsniffing
    bsniffing = True
    text_area1.config(state=NORMAL)
    text_area2.config(state=NORMAL)
    text_area3.config(state=NORMAL)
    text_area4.config(state=NORMAL)
    start_button.config(state=DISABLED)
    stop_button.config(state=NORMAL)
    thread = threading.Thread(target=sniffer, daemon=True)  # Daemon thread to run in background
    thread.start()

def bsniffer():
    sniff(prn=packet_callback, store=False, stop_filter=lambda x: not bsniffing)

def bstop_sniffing():
    global bsniffing
    bsniffing = False
    text_area1.config(state=DISABLED)
    text_area2.config(state=DISABLED)
    text_area3.config(state=DISABLED)
    text_area4.config(state=DISABLED)
    start_button.config(state=NORMAL)
    stop_button.config(state=DISABLED)
    
def bifurcation():
    analysis = Tk()
    analysis.title("ScapyUI - Bifurcation")
    analysis.geometry("1000x800") 
    
    #Image icon for tool icon
    analysis.iconbitmap("C:\\Users\\ranay\\OneDrive\\Documents\\GitHub\\sem2_nfsuproject\\ScapyUI\\res\\logo.ico")
    
    global text_area1, text_area2, text_area3, text_area4
    
    bstart_button = Button(analysis, text="Start Sniffing", command=bstart_sniffing)
    bstart_button.grid(row=0, column=0)

    bstop_button = Button(analysis, text="Stop Sniffing", command=bstop_sniffing, state=DISABLED)
    bstop_button.grid(row=0, column=1)
    
    text_area1 = scrolledtext.ScrolledText(analysis, width=60, height=20, state=DISABLED)
    text_area1.grid(row=1, column=1, sticky="N,W,NS")

    text_area2 = scrolledtext.ScrolledText(analysis, width=60, height=20, state=DISABLED)
    text_area2.grid(row=2, column=0, sticky="S,E,NS")

    text_area3 = scrolledtext.ScrolledText(analysis, width=60, height=20, state=DISABLED)
    text_area3.grid(row=2, column=1, sticky="S,W,NS")
    
    text_area4 = scrolledtext.ScrolledText(analysis, width=60, height=20, state=DISABLED)
    text_area4.grid(row=1, column=0, sticky="N,E,NS")
    
    analysis.mainloop()
    
def showpcap():
    pass
    

# GUI Setup
root = Tk()
#Title for the window
root.title("ScapyUI")

#Image icon for tool icon
root.iconbitmap("C:\\Users\\ranay\\OneDrive\\Documents\\GitHub\\sem2_nfsuproject\\ScapyUI\\res\\logo.ico")

# Geometry of the window
root.geometry("500x380")


myMenu = Menu(root)
root.config(menu=myMenu)

# Create a menu time
navigate = Menu(myMenu)
myMenu.add_cascade(label="Navigate", menu=navigate)
navigate.add_command(label="Open Bifurcation Panel", command=bifurcation)
navigate.add_command(label="Open pcap file", command=showpcap)
navigate.add_command(label="Exit", command=root.quit)
# naivgate.add_separator()

more = Menu(myMenu)
myMenu.add_cascade(label="More", menu=more)
more.add_command(label="About", command=aboutwindow)

start_button = Button(root, text="Start Sniffing", command=start_sniffing)
start_button.grid(row=0, column=0)

stop_button = Button(root, text="Stop Sniffing", command=stop_sniffing, state=DISABLED)
stop_button.grid(row=0, column=1)

text_area = scrolledtext.ScrolledText(root, width=60, height=20, wrap=WORD, state=DISABLED)
text_area.grid(row=1, column=0, columnspan=2, sticky="W,N,E,S")

#creating loop to continuosly execute the app
root.mainloop()
