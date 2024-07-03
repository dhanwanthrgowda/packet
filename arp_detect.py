from scapy.all import sniff, ARP
from tkinter import messagebox, simpledialog
import tkinter as tk
from disableWifi import (disable_wifi,enable_wifi)
from pro1 import (send_telegram_message,send_telegram_otp,send_telegram_video,get_last_message,send_folder)
import time
from capture import (capture_photos,create_video)

# Global counter to track the number of ARP packets captured
arp_packet_count = 0

# Function to handle packet sniffing
def packet_callback(packet):
    global arp_packet_count
    
    # Check if the packet is an ARP packet
    if packet.haslayer(ARP):
        # Increment the ARP packet count
        arp_packet_count += 1
        
        # Check if more than 10 ARP packets are received within the specified time
        if arp_packet_count >= 10:
            # Display ARP attack message
            messagebox.showwarning("ARP Attack Detected","Arp Spoof attack on wifi interface")
            otp = send_telegram_otp()
            send_telegram_message()
            time.sleep(10)
            request=get_last_message()
            if(request=="Yes"):
                    folder_path = "photos"
                    num_photos = 10
                    output_video_path = "output_video1.mp4"

                    # Capture photos
                    capture_photos(folder_path, num_photos)

                    # Create video from photos
                    create_video(folder_path, output_video_path)


                    print("Video created successfully!")
                    send_telegram_video()
                    send_folder()

            elif(request=="No"):
                send_telegram_message(message="accepted")
            else:
                send_telegram_message(message="enter proper message")
            disable_wifi()
            psw = simpledialog.askinteger("psw", "Enter otp:")
            if(psw==otp):
                enable_wifi()
                raise KeyboardInterrupt("ARP attack detected")
            else:
                raise KeyboardInterrupt("ARP attack detected")

# Function to prompt the user for input using Tkinter
def get_timeout():
    root = tk.Tk()
    root.withdraw()
    timeout = simpledialog.askinteger("Timeout", "Enter the timeout in seconds:")
    return timeout

# Get timeout from the user
timeout = get_timeout()

# Start sniffing ARP packets
try:
    sniff(timeout=timeout, prn=packet_callback)
except KeyboardInterrupt:
    print("Packet sniffing stopped.")
