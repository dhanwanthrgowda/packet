import tkinter as tk
from tkinter import simpledialog, messagebox
from scapy.all import sniff, IP, ICMP
import threading
import time
import requests
from area import get_areas_by_postal_code
from disableWifi import (disable_wifi,enable_wifi)
from pro1 import (send_telegram_message,send_telegram_otp,send_telegram_video,get_last_message,send_folder)
import time
from capture import (capture_photos,create_video)

API_URL = "http://ipinfo.io/{}/json?token=cfd1532f7a5833"
INTERFACE = "Wi-Fi"  # Replace with your actual Wi-Fi interface name

class ICMPDetector:
    def __init__(self, duration):
        self.duration = duration
        self.icmp_count = 0
        self.lock = threading.Lock()
        self.running = True
        self.packet_counts = {}

    def packet_callback(self, packet):
        if IP in packet and ICMP in packet:
            with self.lock:
                self.icmp_count += 1
                src_ip = packet[IP].src
                if src_ip in self.packet_counts:
                    self.packet_counts[src_ip] += 1
                else:
                    self.packet_counts[src_ip] = 1
                print(f"ICMP packet from {src_ip}")  # Debugging output

    def start_sniffing(self):
        sniff(prn=self.packet_callback, stop_filter=self.should_stop_sniffing, store=0, iface=INTERFACE)

    def should_stop_sniffing(self, packet):
        return not self.running

    def get_ip_info(self, ip):
        try:
            response = requests.get(API_URL.format(ip))
            response.raise_for_status()
            data = response.json()
            print(f"API Response for IP {ip}: {data}")  # Debugging output
            city = data.get('city', 'Unknown city')
            country = data.get('region', 'Unknown country')
            location = data.get('loc', 'Unknown location')
            postal = data.get('postal', 'Unknown postal code')
            area = get_areas_by_postal_code(postal)
            return f"{city}, {country},{location},{postal},{area}".format(city=city, country=country, location=location)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching IP info: {e}")  # Debugging output
            return "Location information not available"

    def start_detection(self):
        sniff_thread = threading.Thread(target=self.start_sniffing)
        sniff_thread.start()

        start_time = time.time()
        while time.time() - start_time < self.duration:
            time.sleep(1)
            with self.lock:
                if self.icmp_count > 10:
                    self.running = False
                    attacker_ip = max(self.packet_counts, key=self.packet_counts.get)
                    location = self.get_ip_info(attacker_ip)
                    messagebox.showwarning("ICMP Attack Detected", 
                                           f"More than 10 ICMP packets detected in 10 seconds!\nAttacker IP: {attacker_ip}\nLocation: {location}")
                    otp = send_telegram_otp()
                    send_telegram_message(message="System Under Icmp Attack")
                    send_telegram_message(message="Do You want location , Ip to verify press Yes")
                    send_telegram_message(message="if you want photos to verify press Photos")
                    time.sleep(10)
                    request=get_last_message()
                    if(request=="Yes"):
                        send_telegram_message(message=location)
                    elif(request=="Photos"):
                            folder_path = "photos"
                            num_photos = 10
                            output_video_path = "output_video1.mp4"

                            # Capture photos
                            capture_photos(folder_path, num_photos)
                            print("Video created successfully!")
                            send_folder()
                    
                    else:
                        send_telegram_message(message="entered wrong bot message")

                    disable_wifi()
                    psw = simpledialog.askinteger("psw", "Enter otp:")
                    if(psw==otp):
                        enable_wifi()
                        raise KeyboardInterrupt("ARP attack detected")
                    else:
                        raise KeyboardInterrupt("ARP attack detected")
                    break
        self.icmp_count = 0
        self.packet_counts.clear()

        self.running = False
        sniff_thread.join()

def get_duration():
    root = tk.Tk()
    root.withdraw()
    duration = simpledialog.askinteger("Input", "Enter the duration to run the process (in seconds):", minvalue=1)
    return duration

def main():
    duration = get_duration()
    if duration:
        detector = ICMPDetector(duration)
        detector.start_detection()

if __name__ == "__main__":
    main()
