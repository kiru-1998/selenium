import os
import subprocess
import json

# Function to execute commands
def run_command(command):
    try:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error while running command: {e}")
        print(e.stderr)
        return None

# Test Case Execution
def execute_test_cases():
    print("Starting Test Case Execution...")

    # Step 1: Plugin AC Adapter
    print("Step 1: Ensure AC Adapter is plugged into the test unit.")

    # Step 2: Run TestManager to gather static info
    print("\nStep 2: Running TestManager to gather Charger Static Info...")
    command_static_info = r"TestManager.exe -n ChargerStaticInfo -1 -j"
    run_command(command_static_info)

    # Step 3: Validate Charger Static Info
    print("\nStep 3: Validating Charger Static Info...")
    with open("ChargerStaticInfo.json", "r") as static_file:
        static_data = json.load(static_file)
        print("Static Info Data:", static_data)

    # Step 4: Run TestManager to gather dynamic info
    print("\nStep 4: Running TestManager to gather Charger Dynamic Info...")
    command_dynamic_info = r"TestManager.exe -n ChargerDynamicInfo -1 -j"
    run_command(command_dynamic_info)

    # Step 5: Validate Charger Dynamic Info
    print("\nStep 5: Validating Charger Dynamic Info...")
    with open("ChargerDynamicInfo.json", "r") as dynamic_file:
        dynamic_data = json.load(dynamic_file)
        print("Dynamic Info Data:", dynamic_data)

    # Step 6: Non-Dell Platform Check
    print("\nStep 6: Running Non-Dell Platform Validation...")
    command_non_dell_check = r"Test.CPS.AgentController.exe -d 10"
    run_command(command_non_dell_check)

    print("\nAll test cases executed.")

# Main Function
if __name__ == "__main__":
    print("Starting DTP Test Case Automation...")
    execute_test_cases()
