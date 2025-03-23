import subprocess

def get_available_wifi_networks():
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        result = result.decode('utf-8')
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"


if __name__ == "__main__":
    print("Scanning for available Wi-Fi networks...\n")

    wifi_networks_info = get_available_wifi_networks()

    print(wifi_networks_info)

