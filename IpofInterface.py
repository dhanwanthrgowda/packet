import netifaces

def get_ip_address(interface_name):
    try:
        # Get all the addresses for the specified interface
        addresses = netifaces.ifaddresses(interface_name)
        
        # Extract and return the IPv4 address (if available)
        if netifaces.AF_INET in addresses:
            return addresses[netifaces.AF_INET][0]['addr']
        else:
            return None
    except ValueError:
        return None

# Specify the interface name (e.g., "Wi-Fi")
interface_name = input("interface Name is:")

# Get the IP address of the specified interface
ip_address = get_ip_address(interface_name)

if ip_address:
    print(f"IP address of {interface_name}: {ip_address}")
else:
    print(f"No IP address found for {interface_name}")
