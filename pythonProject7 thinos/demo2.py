import paramiko
import os

# List of ThinOS devices with their IP addresses and credentials
devices = [
    {'hostname': '100.106.117.119', 'username': 'administrator', 'password': 'ThinOS@123'},
    # Add more devices as needed
]

# Directory to save logs
log_directory = './logs'

# Ensure the log directory exists
os.makedirs(log_directory, exist_ok=True)

def collect_logs(device):
    hostname = device['hostname']
    username = device['username']
    password = device['password']

    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        ssh.connect(hostname, username=username, password=password)

        # Command to retrieve logs (replace with actual command for ThinOS)
        command = 'cat /wnos/troubleshoot/logs/system.log'  # Example command, modify as per your ThinOS device

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the log data
        log_data = stdout.read().decode('utf-8')

        # Save the log data to a file
        with open(f"{log_directory}/{hostname}_log.txt", 'w') as log_file:
            log_file.write(log_data)

        print(f"Logs collected for device: {hostname}")

    except Exception as e:
        print(f"Failed to collect logs for device: {hostname}, Error: {str(e)}")

    finally:
        ssh.close()

# Loop through each device and collect logs
for device in devices:
    collect_logs(device)
