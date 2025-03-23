import requests
from requests.auth import HTTPBasicAuthnnnnnnnnnnnnnn
import tkinter as tk
from tkinter import messagebox, scrolledtext


# Function to fetch Jira issues and display in a new window
def fetch_and_display_issues():
    # Replace with your Jira instance URL, username, and password
    jira_url = "https://jira.cpg.dell.com/rest/api/2/"
    username = "Kirana_MS"
    password = "Kiran@1808"

    # Authentication
    auth = HTTPBasicAuth(username, password)

    # JQL query using the user input
    jql_query = 'project = "Dell ThinOS" AND "Bug Source" = Customer'

    # API URL for searching issues
    search_url = jira_url + "search"

    # Parameters for the search API
    params = {
        'jql': jql_query,
        'maxResults': 100,  # Adjust as needed
        'fields': ['summary', 'status', 'assignee']  # Adjust fields as needed
    }

    # Send the request to Jira
    response = requests.get(search_url, auth=auth, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        issues = data['issues']

        # Create a new window to display results
        result_window = tk.Toplevel(root)
        result_window.title("Jira Issues")

        # Create and place the label and entry for additional search parameter
        additional_search_label = tk.Label(result_window, text="Search in Ticket Summaries:")
        additional_search_label.pack(padx=10, pady=10)
        additional_search_entry = tk.Entry(result_window, width=50)
        additional_search_entry.pack(padx=10, pady=10)

        # Create a scrolled text widget to display the results
        result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=100, height=20)
        result_text.pack(padx=10, pady=10)

        # Function to display issues
        def display_issues(issues):
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END,
                               f"Found {len(issues)} issue(s) related to 'Customer':\n\n")
            for issue in issues:
                summary = issue['fields']['summary']
                status = issue['fields']['status']['name']
                assignee = issue['fields']['assignee']['displayName']  if issue['fields']['assignee'] else 'Unassigned'
                result_text.insert(tk.END, f"Summary: {summary}\n")
                result_text.insert(tk.END, f"Status: {status}\n")
                result_text.insert(tk.END, f"Assignee: {assignee}\n")
                result_text.insert(tk.END, '-' * 40 + '\n')

        # Display the initial results
        display_issues(issues)

        # Function to apply additional filter
        def apply_additional_filter():
            filter_text = additional_search_entry.get().lower()
            filtered_issues = [issue for issue in issues if filter_text in issue['fields']['summary'].lower()]
            display_issues(filtered_issues)

        # Create and place the button to apply additional filter
        filter_button = tk.Button(result_window, text="Apply Filter", command=apply_additional_filter)
        filter_button.pack(padx=10, pady=10)

    else:
        messagebox.showerror("Error", f"Failed to retrieve issues: {response.status_code} - {response.text}")


# Create the main window
root = tk.Tk()
root.title("Jira Issue Tracker")

# Create and place the button to fetch and display issues
fetch_button = tk.Button(root, text="Fetch and Display Issues", command=fetch_and_display_issues)
fetch_button.pack(padx=20, pady=20)

# Run the application
root.mainloop()
