import paramiko
import os
import logging
import tkinter as tk
from tkinter import simpledialog

# Setup logging
logging.basicConfig(
    filename='device_log_collection.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Setup tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt user for device information
hostname = simpledialog.askstring("Device Info", "Enter the hostname/IP address:", parent=root)
username = simpledialog.askstring("Device Info", "Enter the username:", parent=root)
password = simpledialog.askstring("Device Info", "Enter the password:", show='*', parent=root)

devices = [
    {'hostname': hostname, 'username': username, 'password': password},
]

log_Devicelog = r"C:\Users\Kiran\Desktop\Device log"
os.makedirs(log_Devicelog, exist_ok=True)

def collect_logs(device):
    hostname = device['hostname']
    username = device['username']
    password = device['password']
    ssh = None

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password, timeout=100)

        list_command = 'ls -p /compat/linux/var/log | grep -v /'
        stdin, stdout, stderr = ssh.exec_command(list_command)

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

        for log_file_name in log_files:
            command = f'cat /compat/linux/var/log/{log_file_name}'

            stdin, stdout, stderr = ssh.exec_command(command)

            error_output = stderr.read().decode('utf-8', errors='ignore')
            if error_output:
                logging.error(f"Error retrieving {log_file_name} from {hostname}: {error_output}")
                print(f"Error retrieving {log_file_name} from {hostname}: {error_output}")
                continue

            log_data = stdout.read().decode('utf-8', errors='ignore')

            if log_data:
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

for device in devices:
    collect_logs(device)
