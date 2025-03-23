import paramiko
import os

# List of ThinOS devices with their IP addresses and credentials
devices = [
    {'hostname': '100.106.126.111', 'username': 'root', 'password': 'p@ssw0rd'},
    # Add more devices as needed
]

# Directory to save logs
log_directory = "C:/Users/Kiran/PycharmProjects/pythonProject7 thinos"  # Directory path, not a file path

# Ensure the log directory exists
os.makedirs(log_directory, exist_ok=True)


def collect_logs(device):
    hostname = device['hostname']
    username = device['username']
    password = device['password']

    ssh = None

    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device using dictionary values
        ssh.connect(hostname, username=username, password=password, timeout=60)  # Increased timeout

        # Command to retrieve logs (replace with actual command for ThinOS)
        command = 'cat /compat/linux/var/log/messages.log'

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the log data
        log_data = stdout.read().decode('utf-8')

        # Save the log data to a file
        log_file_path = os.path.join(log_directory, f"{hostname}_log.txt")
        with open(log_file_path, 'w') as log_file:
            log_file.write(log_data)

        print(f"Logs collected for device: {hostname}")

    except Exception as e:
        print(f"Failed to collect logs for device: {hostname}, Error: {str(e)}")

    finally:
        if ssh is not None:
            ssh.close()


# Loop through each device and collect logs
for device in devices:
    collect_logs(device)
