import os
import json
import subprocess
import ctypes  # For checking admin rights

# Define the command and alternative output path
json_output_path = r"C:\Temp\MultimediaData.json"  # Alternative path
os.makedirs(r"C:\Temp", exist_ok=True)  # Ensure the directory exists
command = f'"Dell.Instrumentation.TestManager.exe" -n MultimediaData -1 -j "{json_output_path}"'
test_manager_path = r"C:\Program Files\Dell\DTP\TestManager"


# Check if the script is running with elevated privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Step 1: Execute the command
def execute_command(command, path):
    try:
        print(f"Executing command: {command} in directory: {path}")
        result = subprocess.run(
            command,
            cwd=path,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout, result.stderr
    except Exception as e:
        return None, str(e)


# Step 2: Check the generated JSON file
def validate_json(file_path):
    try:
        # Load the JSON data
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Validation logic
        test_passed = True
        issues = []

        # Check specific keys for validity
        if "NameSupportedMediaFormatsCapability" not in data or not data["NameSupportedMediaFormatsCapability"]:
            test_passed = False
            issues.append("'NameSupportedMediaFormatsCapability' is missing or empty.")

        if "SupportedMediaFormats" in data:
            if data["SupportedMediaFormats"] != []:  # Should be empty as expected
                test_passed = False
                issues.append("'SupportedMediaFormats' is not empty as expected.")

        # Return validation result
        return test_passed, issues

    except Exception as e:
        return False, [f"Error reading JSON file: {str(e)}"]


# Step 3: Main test case logic
def main_test_case():
    # Check admin privileges
    if not is_admin():
        print("Test Case Failed: This script must be run as an administrator.")
        return

    # Execute the command
    stdout, stderr = execute_command(command, test_manager_path)

    # Check for errors in command execution
    if stderr:
        print("Test Case Failed: Error in command execution.")
        print("Error Details:", stderr)
        return

    print("Command executed successfully. Checking the JSON file...")

    # Validate the JSON file
    if not os.path.exists(json_output_path):
        print(f"Test Case Failed: JSON file was not generated at {json_output_path}.")
        return

    test_passed, issues = validate_json(json_output_path)

    # Print results
    if test_passed:
        print("Test Case Passed: All checks passed.")
    else:
        print("Test Case Failed: Issues found during validation.")
        for issue in issues:
            print("-", issue)


# Run the test case
if __name__ == "__main__":
    main_test_case()
