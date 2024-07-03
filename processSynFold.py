from scapy.all import *
from collections import defaultdict
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from pro1 import (send_telegram_message, send_telegram_otp, send_telegram_video, get_last_message, send_folder)
#from ipofpackets import getip
from capture import (capture_photos, create_video)
from disableWifi import (disable_wifi, enable_wifi)

# Define a dictionary to keep track of SYN packet counts
syn_counts = defaultdict(int)
# Define a dictionary to keep track of the last seen time for each source IP
last_seen = defaultdict(float)
# Define the threshold for SYN packet count to consider it as a potential attack
SYN_THRESHOLD = 1

# Define the time window in seconds
TIME_WINDOW = 10

def syn_flood_detection(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):  # Check if the packet has IP and TCP layers
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
            
            current_time = time.time()
            
            # Remove entries that are outside the time window
            for ip in list(last_seen.keys()):
                if current_time - last_seen[ip] > TIME_WINDOW:
                    del syn_counts[ip]
                    del last_seen[ip]
            
            # Update the last seen time for the source IP
            last_seen[src_ip] = current_time
            
            # Increment the SYN count for the source IP
            syn_counts[src_ip] += 1
            
            # Check if the SYN count exceeds the threshold within the time window
            if syn_counts[src_ip] > SYN_THRESHOLD:
                messagebox.showwarning(f"Possible SYN flood detected from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
                messagebox.showwarning(f"SYN count for {src_ip}: 192.168.1.7")
                send_telegram_message(message=f"SYN count for {src_ip}: {syn_counts[src_ip]}")
                send_telegram_message(message="Do you want all the IP details?")
                otp = send_telegram_otp()
                time.sleep(20)
                request = get_last_message()
                if request == "Ip":
                    iplist = "{src_ip}: {syn_counts[src_ip]}"
                    send_telegram_message(message=iplist)
                    folder_path = "photos"
                    num_photos = 1
                    output_video_path = "output_video1.mp4"

                    # Capture photos
                    capture_photos(folder_path, num_photos)

                    # Create video from photos
                    #create_video(folder_path, output_video_path)

                    print("Video created successfully!")
                    send_telegram_video() 
                    disable_wifi()
                    psw = simpledialog.askinteger("psw", "Enter OTP:")
                    if psw == otp:
                        enable_wifi()
                        raise KeyboardInterrupt("SYN flood detected")
                else:
                    otp = send_telegram_otp()
                    disable_wifi()   
                    psw = simpledialog.askinteger("psw", "Enter OTP:")
                    if psw == otp:
                        enable_wifi()
                        raise KeyboardInterrupt("SYN flood detected")

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt user to enter timeout value using a message box
timeout = simpledialog.askinteger("Timeout", "Enter the timeout duration in seconds:")

# Capture packets from WiFi interface for the specified duration
sniff(timeout=timeout, prn=syn_flood_detection)
