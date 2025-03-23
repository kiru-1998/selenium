import requests
from requests.auth import HTTPBasicAuth
import tkinter as tk
from tkinter import messagebox, scrolledtext

def fetch_and_display_issues():
    jira_url = "https://jira.cpg.dell.com/login.jsp"
    username = "Kirana_MS"
    password = "Kiran@1808"

    auth = HTTPBasicAuth(username, password)

    jql_query = 'project = "Dell ThinOS" AND "Bug Source" = Customer'

    search_url = jira_url + "search"

    initial_params = {
        'jql': jql_query,
        'fields': 'summary',
    }

    response = requests.get(search_url, auth=auth, params=initial_params, verify=False)
    if response.status_code == 200:
        data = response.json()
        total_issues = data['total']
    else:
        messagebox.showerror("Error", f"Failed to retrieve issue count: {response.status_code} - {response.text}")
        return

    params = {
        'jql': jql_query,
        'maxResults': total_issues,
        'fields': 'summary,status,assignee,comment',
        'expand': 'comments'
    }

    all_issues = []
    start_at = 0

    while True:
        params['startAt'] = start_at
        response = requests.get(search_url, auth=auth, params=params, verify=False)

        if response.status_code == 200:
            data = response.json()
            issues = data['issues']
            all_issues.extend(issues)

            if len(issues) < params['maxResults']:
                break

            start_at += params['maxResults']
        else:
            messagebox.showerror("Error", f"Failed to retrieve issues: {response.status_code} - {response.text}")
            return

    result_window = tk.Toplevel(root)
    result_window.title("Jira Issues")
    result_window.state('zoomed')

    additional_search_label = tk.Label(result_window, text="Search in Ticket Summaries:")
    additional_search_label.pack(padx=10, pady=10)
    additional_search_entry = tk.Entry(result_window, width=50)
    additional_search_entry.pack(padx=10, pady=10)

    result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=100, height=20)
    result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def display_issues(issues):
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"Found {len(issues)} issue(s) related to 'Customer':\n\n")
        for issue in issues:
            summary = issue['fields']['summary']
            status = issue['fields']['status']['name']
            assignee = issue['fields']['assignee']['displayName'] if issue['fields']['assignee'] else 'Unassigned'
            comments = issue['fields']['comment']['comments']

            gerrit_auto_comment = None
            important_comments = []

            for comment in comments:
                if 'Gerrit Auto' in comment['body']:
                    gerrit_auto_comment = comment['body']
                    break
                else:
                    # Look for important keywords in the comment
                    keywords = ['fix', 'issue', 'recommend', 'important', 'change', 'urgent', 'critical']
                    if any(keyword in comment['body'].lower() for keyword in keywords):
                        important_comments.append(comment['body'])

            result_text.insert(tk.END, f"Summary: {summary}\n")
            result_text.insert(tk.END, f"Status: {status}\n")
            result_text.insert(tk.END, f"Assignee: {assignee}\n")
            if gerrit_auto_comment:
                result_text.insert(tk.END, f"Gerrit Auto Command: {gerrit_auto_comment}\n")
            else:
                if important_comments:
                    result_text.insert(tk.END, "Important Comments:\n")
                    for imp_comment in important_comments:
                        result_text.insert(tk.END, f"- {imp_comment}\n")
                else:
                    result_text.insert(tk.END, "No important comments found.\n")
            result_text.insert(tk.END, '-' * 40 + '\n')

    display_issues(all_issues)

    def apply_additional_filter():
        filter_text = additional_search_entry.get().lower()
        filtered_issues = [issue for issue in all_issues if filter_text in issue['fields']['summary'].lower()]
        display_issues(filtered_issues)

    search_button = tk.Button(result_window, text="Apply Filter", command=apply_additional_filter)
    search_button.pack(padx=10, pady=10)

root = tk.Tk()
root.title("Jira Issue Tracker")

fetch_button = tk.Button(root, text="Fetch Issues", command=fetch_and_display_issues)
fetch_button.pack(pady=20)

root.mainloop()
