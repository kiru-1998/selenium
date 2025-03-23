import paramiko
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Setup logging
logging.basicConfig(
    filename='device_log_collection.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


devices = [
    {'hostname': '100.106.117.138', 'username': 'root', 'password': 'p@ssw0rd'},

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
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

try:

    driver.get('https://jira.cpg.dell.com/browse/DTOS-22980')


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))
    login_button = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-form-username")))
    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")

    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    attach_section = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h4[@id='attachmentmodule-label']")))
    attach_section.click()
    print("Clicked on the Attachments section.")

    browse_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "attachment-browse-button")))
    print("Browse button found.")

    file_input = driver.find_element(By.XPATH, "//input[@type='file' and @class='issue-drop-zone__file ignore-inline-attach']")

    file_path = r"C:\Users\Kiran\Desktop\Device log\100.106.117.138_check_citrix_pkg.log"

    if os.path.exists(file_path):
        file_input.send_keys(file_path)
        print(f"File found and sent for upload: {file_path}")

        uploaded_file_name = os.path.basename(file_path)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//ol[@id='attachment_thumbnails']//li[contains(., '{uploaded_file_name}')]")))
        print(f"Upload verified: {uploaded_file_name} is present on the page.")
    else:
        print(f"File not found: {file_path}")

finally:
    driver.quit()
