import paramiko
import os

# List of ThinOS devices with their IP addresses and credentials
devices = [
    {'hostname': '100.106.126.111', 'username': 'root', 'password': 'p@ssw0rd'},
    # Add more devices as needed
]

# Directory to save logs
log_Devicelog = r'"C:\Users\Kiran\Desktop\Device log"'

# Ensure the log directory exists
os.makedirs(log_Devicelog, exist_ok=True)

def collect_logs(device):
    # Correctly access the dictionary keys
    hostname = device['100.106.126.111']
    username = device['root']
    password = device['p@ssw0rd']

    ssh = None  # Initialize ssh variable to ensure it exists in the finally block

    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device using dictionary values
        ssh.connect('100.106.126.111', username='root', password='p@ssw0rd')

        # Command to retrieve logs (replace with actual command for ThinOS)
        command = 'cat/compat/linux/var/log/messages'
        # Example command, modify as per your ThinOS device

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the log data
        log_data = stdout.read().decode('utf-8')

        # Save the log data to a file
        with open(f"{log_Devicelog}/{'100.106.126.111'}_log.txt", 'w') as log_file:
            log_file.write(log_data)

        print(f"Logs collected for device: {'100.106.126.111'}")

    except Exception as e:
        print(f"Failed to collect logs for device: {'100.106.126.111'}, Error: {str(e)}")

    finally:
        if ssh is not None:
            ssh.close()

# Loop through each device and collect logs
for device in devices:
    collect_logs(device)



