import subprocess


def list_wifi_networks():
    try:

        result = subprocess.run(
            ["netsh", "wlan", "show", "networks"],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse the command output
        output = result.stdout
        networks = []

        for line in output.split('\n'):
            if "SSID" in line:
                ssid = line.split(':')[1].strip()
                networks.append(ssid)

        return networks

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print(f"Command output: {e.output}")
        return []


# Example usage
wifi_networks = list_wifi_networks()
print("Available Wi-Fi Networks:")
for network in wifi_networks:
    print(network)

