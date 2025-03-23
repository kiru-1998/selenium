import paramiko
import os
import logging

# Setup logging
logging.basicConfig(
    filename='device_log_collection.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# List of ThinOS devices with their IP addresses and credentials
devices = [
    {'hostname': '100.106.117.138', 'username': 'root', 'password': 'p@ssw0rd'},
    # Add more devices as needed
]

# Directory to save logs
log_Devicelog = r"C:\Users\Kiran\Desktop\Device log"

# Ensure the log directory exists
os.makedirs(log_Devicelog, exist_ok=True)

def collect_logs(device):
    hostname = device['hostname']
    username = device['username']
    password = device['password']
    ssh = None

    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        ssh.connect(hostname, username=username, password=password, timeout=100)

        # Command to list all log files in the directory
        list_command = 'ls -p /compat/linux/var/log | grep -v /'
        stdin, stdout, stderr = ssh.exec_command(list_command)

        # Read the output and errors
        log_files = stdout.read().decode('utf-8', errors='ignore').splitlines()
        error_output = stderr.read().decode('utf-8', errors='ignore')

        if error_output:
            logging.error(f"Error listing logs on {hostname}: {error_output}")
            print(f"Error listing logs on {hostname}: {error_output}")
            return

        if not log_files:
            logging.warning(f"No log files found on {hostname}.")
            print(f"No log files found on {hostname}.")
            return

        # Download each log file
        for log_file_name in log_files:
            command = f'cat /compat/linux/var/log/{log_file_name}'

            # Execute the command to read the log file
            stdin, stdout, stderr = ssh.exec_command(command)

            # Check for errors in the stderr output
            error_output = stderr.read().decode('utf-8', errors='ignore')
            if error_output:
                logging.error(f"Error retrieving {log_file_name} from {hostname}: {error_output}")
                print(f"Error retrieving {log_file_name} from {hostname}: {error_output}")
                continue

            # Read the log data
            log_data = stdout.read().decode('utf-8', errors='ignore')

            if log_data:
                # Save the log data to a file
                log_file_path = os.path.join(log_Devicelog, f"{hostname}_{log_file_name}")
                with open(log_file_path, 'w', encoding='utf-8', errors='ignore') as log_file:
                    log_file.write(log_data)
                print(f"Log {log_file_name} collected for device: {hostname}")
                logging.info(f"Log {log_file_name} successfully collected for device: {hostname}")
            else:
                logging.warning(f"Log file {log_file_name} is empty for device: {hostname}.")
                print(f"Log file {log_file_name} is empty for device: {hostname}.")

    except Exception as e:
        logging.error(f"Failed to collect logs from {hostname}, Error: {str(e)}")
        print(f"Failed to collect logs from {hostname}, Error: {str(e)}")

    finally:
        if ssh is not None:
            ssh.close()

# Loop through each device and collect logs
for device in devices:
    collect_logs(device)
