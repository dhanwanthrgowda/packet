from scapy.all import ARP, Ether, sendp

def send_arp_packet(interface, target_ip, target_mac):
    # Craft the ARP packet
    arp_packet = Ether(dst=target_mac)/ARP(op=1, pdst=target_ip)

    # Send the ARP packet
    sendp(arp_packet, iface=interface, verbose=False)

# Example usage
interface = "Wi-Fi"  # Replace "wlan0" with your WiFi interface name
target_ip = "192.168.1.1"  # Replace with the IP address you want to send the ARP packet to
target_mac = "00:11:22:33:44:55"  # Replace with the MAC address of the target device
for i in range(50):
 send_arp_packet(interface, target_ip, target_mac)
