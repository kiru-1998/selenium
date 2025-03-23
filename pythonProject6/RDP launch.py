import os


def launch_rdp(remote_address, username=None, password=None):
    """
    Launch an RDP session to the specified remote address.

    Args:
        remote_address (str): The IP address or hostname of the remote machine.
        username (str, optional): The username for the RDP session.
        password (str, optional): The password for the RDP session.
    """
    # Basic command to launch mstsc with the remote address
    command = f"mstsc /v:{'100.106.116.89'}"

    if username and password:
        # Write credentials to a temporary file
        credentials = f"""
        full address:s:{remote_address}
        username:s:{'administrator'}
        password:s:{'ThinOS@123'}
        """
        temp_rdp_file = "temp_rdp.rdp"
        with open(temp_rdp_file, 'w') as file:
            file.write(credentials)

        # Launch mstsc with the credentials file
        command = f"mstsc {temp_rdp_file}"

    # Execute the command
    os.system(command)


# Example usage
remote_address = "100.106.116.89"
username = "administrator"
password = "ThinOS@123"
launch_rdp(remote_address, username, password)
