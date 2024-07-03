from scapy.all import sniff, IP, Ether
# Function to handle packet sniffing
def packet_callback(packet):
    if IP in packet:
        # Your packet processing logic here
        return packet.summary()

# Start sniffing Wi-Fi packets, capture only IP packets
#sniff(iface="Wi-Fi", prn=packet_callback, filter="ip",count=30)

sniff(iface="Wi-Fi", prn=packet_callback, filter="ether", count=30)