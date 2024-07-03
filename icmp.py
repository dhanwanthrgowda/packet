from scapy.all import IP, ICMP, send

# Define the destination IP address
destination_ip = '92.168.0.104'
# Define the spoofed source IP address
source_ip = '106.51.174.9'  # Replace with the desired spoofed source IP

# Create an ICMP echo request packet with the spoofed source IP
icmp_packet = IP(dst=destination_ip, src=source_ip) / ICMP()

# Send the ICMP echo request packet
for i in range(20):
    send(icmp_packet)
