import paramiko

def collect_logs_thinos('100.106.126.111', 'root', 'p@ssw0rd', '/compat/linux/var/log', "C:\Users\Kiran\Desktop\Device log"):
    """
    Collects logs from a ThinOS device via SSH.

    Args:
        hostname (str): IP address or hostname of the ThinOS device.
        username (str): Username for SSH login.
        password (str): Password for SSH login.
        log_path (str): Path to the log file on the ThinOS device.
        save_path (str): Local path where the log file will be saved.

    Returns:
        None
    """

    # Initialize SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the ThinOS device
        ssh_client.connect(hostname, username=username, password=password)
        print("Connected to the ThinOS device successfully.")

        # Use SFTP to download the log file
        sftp = ssh_client.open_sftp()
        sftp.get(log_path, save_path)
        sftp.close()

        print(f"Log file downloaded successfully to {save_path}.")

    except paramiko.AuthenticationException:
        print("Authentication failed, please check your credentials.")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
    except paramiko.Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()

# Example usage
# Replace with actual hostname, username, password, log path, and save path
hostname = "192.168.1.100"
username = "admin"
password = "password"
log_path = "/var/log/thinos.log"
save_path = "thinos.log"

# Uncomment the following line to run the function
# collect_logs_thinos(hostname, username, password, log_path, save_path)





