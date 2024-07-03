import netifaces

# Get a list of all network interface names
interface_names = netifaces.interfaces()

# Print the list of interface names
print(interface_names)
