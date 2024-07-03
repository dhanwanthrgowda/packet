import subprocess

def disable_wifi():
    try:
        # Run netsh command to disable Wi-Fi adapter
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "disabled"], check=True)
        print("Wi-Fi adapter disabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def enable_wifi():
    try:
        # Run netsh command to disable Wi-Fi adapter
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "enabled"], check=True)
        print("Wi-Fi adapter enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

enable_wifi()
