from tkinter import *
from PIL import ImageTk, Image
from tkinter import scrolledtext
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, DNS
from scapy.layers.inet6 import IPv6, _ICMPv6  # Corrected import
import threading
# For pcap file read
from scapy.utils import rdpcap
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
# For report and pdf storing
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from datetime import datetime
from tkinter import filedialog



def save_log_as_pdf(text_widget):
    """ Saves the content of a text widget to a properly formatted PDF file """
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF Files", "*.pdf")],
                                             title="Save Log as PDF")
    if not file_path:
        return  # User canceled the save dialog

    content = text_widget.get("1.0", END).strip()  # Extract text

    if not content:
        print("No data to save.")
        return

    # Create a PDF document
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 10)

    # Title & Timestamp
    c.drawString(100, 750, "ScapyUI - Network Traffic Log")
    c.drawString(100, 735, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.line(100, 730, 500, 730)  # Horizontal line

    # Writing text with proper word wrapping
    y_position = 710
    max_width = 400  # Maximum width for text before wrapping
    line_height = 15  # Line spacing

    for line in content.split("\n"):
        wrapped_lines = simpleSplit(line, "Helvetica", 10, max_width)  # Automatically split long lines
        for wrapped_line in wrapped_lines:
            if y_position < 50:  # Create a new page if space is insufficient
                c.showPage()
                c.setFont("Helvetica", 10)
                y_position = 750  # Reset y_position for the new page
            c.drawString(100, y_position, wrapped_line)
            y_position -= line_height  # Move down for the next line

    c.save()
    print(f"Log saved as PDF: {file_path}")

def packet_callback(packet):
    try:
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

            # Insert protocol and IP data
            display_text1 = f"{protocol} Packet: {src_ip} -> {dst_ip}\n"
            text_area1.insert(END, display_text1)
            text_area1.see(END)

            # Insert full packet details
            display_text2 = f"{packet}\n"
            text_area2.insert(END, display_text2)
            text_area2.see(END)

            # Extract HTTP Data from Raw Layer
            if packet.haslayer(TCP) and packet.haslayer(Raw):  # Ensure TCP and Raw layer exists
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                raw_data = packet[Raw].load.decode(errors="ignore")  # Decode safely

                # Check if packet is HTTP (port 80) or HTTPS (port 443)
                if sport == 80 or dport == 80 or sport == 443 or dport == 443:
                    display_text3 = f"HTTP Data ({sport} -> {dport}):\n{raw_data}\n\n"
                    text_area3.insert(END, display_text3)
                    text_area3.see(END)

            # Extract DNS Query/Response Data
            if packet.haslayer(DNS):
                dns_layer = packet[DNS]
                
                # Check if it's a DNS query
                if dns_layer.qdcount > 0:  # There's at least one query in the DNS packet
                    dns_query_name = dns_layer.qd[0].qname.decode()  # Extract the query domain name
                    display_text4 = f"DNS Query: {dns_query_name} from {src_ip}\n"
                
                # Check if it's a DNS response
                elif dns_layer.ancount > 0:  # There's at least one answer in the DNS response
                    dns_response = dns_layer.an[0]  # Get the first DNS answer
                    if isinstance(dns_response.rdata, bytes):  # Check if rdata is a valid bytes object
                        dns_response_data = dns_response.rdata.decode()  # Extract the response data (usually an IP address)
                        query_name = dns_layer.qd[0].qname.decode()  # Extract the original queried domain name
                        display_text4 = f"DNS Response: {dns_response_data} for {query_name}\n"
                    else:
                        display_text4 = f"DNS Response (non-IP response) for {dns_layer.qd[0].qname.decode()}\n"
                
                # Insert the DNS output into the text area
                text_area4.insert(END, display_text4)
                text_area4.see(END)
    except IndexError:
        print("Warning: Malformed packet encountered (IndexError). Skipping.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def start_sniffing():
    global sniffing
    sniffing = True
    start_button.config(state=DISABLED)
    stop_button.config(state=NORMAL)
    
    text_area1.config(state=NORMAL)
    text_area2.config(state=NORMAL)
    text_area3.config(state=NORMAL)
    text_area4.config(state=NORMAL)

    thread = threading.Thread(target=sniffer, daemon=True)  # Run in background
    thread.start()

def sniffer():
    sniff(prn=packet_callback, store=False, stop_filter=lambda x: not sniffing)

def stop_sniffing():
    global sniffing
    sniffing = False
    start_button.config(state=NORMAL)
    stop_button.config(state=DISABLED)
    
    text_area1.config(state=DISABLED)
    text_area2.config(state=DISABLED)
    text_area3.config(state=DISABLED)
    text_area4.config(state=DISABLED)

def aboutwindow():
    """ Displays an 'About' window with information about the tool. """
    about = Toplevel(root)  # Create a new window
    about.title("ScapyUI - About Tool")
    about.geometry("500x360")
    about.iconbitmap(r'C:\Users\ranay\OneDrive\Documents\GitHub\sem2_nfsuproject\ScapyUI\res\logo.ico') #Path to icon image
    about.configure(background='#82643C')

    # Creating a text area with information
    info_area = scrolledtext.ScrolledText(about, width=60, height=15, wrap=WORD, state=NORMAL, bg="#EDE8D0")
    info_area.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Tool Information Content
    about_text = """ScapyUI - Network Packet Sniffer

Version: 1.0
Developed by: Yash Rana

Description:
ScapyUI is a powerful GUI-based network sniffer built using Scapy and Tkinter.
It allows users to:
- Capture live network traffic
- Distributed panels to monitor traffic and raw data
- Open and analyze .pcap files in a new window
- Extract and display HTTP and DNS traffic
- Support both IPv4 and IPv6

This tool is useful for network forensics, penetration testing, and debugging.

License: Open Source

For any issues or contributions, feel free to contact the developer.
"""

    # Insert text and disable editing
    info_area.insert(END, about_text)
    info_area.config(state=DISABLED)

    # Exit Button
    buttonQuit = Button(about, text="Close", bg="#ff5a5a", fg="#ffffff", command=about.destroy)
    buttonQuit.grid(row=1, column=0, pady=10, sticky="nsew")

    # Adjust column/row behavior
    about.grid_rowconfigure(0, weight=1)
    about.grid_columnconfigure(0, weight=1)


def read_pcap():
    """ Opens a file dialog to select a pcap file and displays packets in a new Tkinter window """
    file_path = filedialog.askopenfilename(title="Select a PCAP file", filetypes=[("PCAP Files", "*.pcap")])
    
    if file_path:
        packets = rdpcap(file_path)  # Read the .pcap file

        # Create a new window to display the PCAP file
        pcap_window = Toplevel(root)
        pcap_window.title(f"PCAP Viewer - {file_path.split('/')[-1]}")
        pcap_window.geometry("800x600")
        pcap_window.iconbitmap(r'C:\Users\ranay\OneDrive\Documents\GitHub\sem2_nfsuproject\ScapyUI\res\logo.ico') #Path to icon image
        pcap_window.configure(background='#82643C')

        # Create a ScrolledText widget to display packet contents
        pcap_text_area = scrolledtext.ScrolledText(pcap_window, width=100, height=30, state=NORMAL, bg="#EDE8D0")
        pcap_text_area.pack(padx=10, pady=10, fill="both", expand=True)

        # Insert packets into the text area
        for i, packet in enumerate(packets, 1):
            pcap_text_area.insert(END, f"Packet {i}:\n{packet}\n\n")

        pcap_text_area.config(state=DISABLED)  # Make text read-only

        # Save Log Button
        save_pcap_button = Button(pcap_window, bg="#0173e6", fg="#ffffff", text="Save Log as PDF", command=lambda: save_log_as_pdf(pcap_text_area))
        save_pcap_button.pack(pady=5)

        # Exit Button
        exit_button = Button(pcap_window, text="Close", bg="#ff5a5a", fg="#ffffff",command=pcap_window.destroy)
        exit_button.pack(pady=5)

# GUI Setup
root = Tk()
root.title("ScapyUI - Network Sniffer")
root.geometry("1000x800")
root.iconbitmap(r'C:\Users\ranay\OneDrive\Documents\GitHub\sem2_nfsuproject\ScapyUI\res\logo.ico') #Path to icon image

#Color for the body of tool
root.configure(background='#82643C') #'#D1BF95'

# Adding a Menu
myMenu = Menu(root, background="#D1BF95")
# myMenu.configure(bg="#D1BF95")
root.config(menu=myMenu)

navigate = Menu(myMenu, tearoff=0, bg="#D1BF95")
myMenu.add_cascade(label="Navigate", menu=navigate)
navigate.add_command(label="Open PCAP File", command=read_pcap)
navigate.add_command(label="Exit", command=root.quit)

more = Menu(myMenu, tearoff=0, bg="#D1BF95")
myMenu.add_cascade(label="More", menu=more)
more.add_command(label="About", command=aboutwindow)

# Start/Stop Buttons
start_button = Button(root, text="Start Sniffing",command=start_sniffing, bg="#25b31c")
start_button.grid(row=0, column=0, padx=10, pady=10)

stop_button = Button(root, text="Stop Sniffing", command=stop_sniffing, state=DISABLED, bg="#ff5a5a", fg="#ffffff")
stop_button.grid(row=0, column=1, padx=10, pady=10)

# Text Areas with Scrollbars
text_area1 = scrolledtext.ScrolledText(root, width=60, height=20, state=DISABLED, bg="#EDE8D0") ##FFFF82
text_area1.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

text_area2 = scrolledtext.ScrolledText(root, width=60, height=20, state=DISABLED, bg="#EDE8D0")
text_area2.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

text_area3 = scrolledtext.ScrolledText(root, width=60, height=20, state=DISABLED, bg="#EDE8D0")
text_area3.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

text_area4 = scrolledtext.ScrolledText(root, width=60, height=20, state=DISABLED, bg="#EDE8D0")
text_area4.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

save_button = Button(root, text="Save Log as PDF", bg="#0173e6", fg="#ffffff",command=lambda: save_log_as_pdf(text_area2))
save_button.grid(row=5, column=0, columnspan=2, pady=10)

# Grid Layout Expansion
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run Application
root.mainloop()
