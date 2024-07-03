from scapy.all import Ether, IP, ICMP, sendp

# Define the source MAC address (replace with desired MAC address)
source_mac = "AA:BB:CC:DD:EE:FF"

# Define the destination MAC address (replace with smartphone's MAC address)
destination_mac = "12:34:56:78:90:AB"

# Define the destination IP address
destination_ip = '192.168.1.1'

# Create an ICMP echo request packet with source and destination MAC addresses, and destination IP address
icmp_packet = Ether(src=source_mac, dst=destination_mac) / IP(dst=destination_ip) / ICMP()

# Send the ICMP echo request packet
sendp(icmp_packet)
