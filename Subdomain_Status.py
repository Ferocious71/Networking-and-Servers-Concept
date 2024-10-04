import requests
import time
from prettytable import PrettyTable

# List of subdomains to check
subdomains = [
    "https://www.linkedin.com/feed/",
    "https://gemini.google.com/app",
    "https://hashnode.com/"
]

# Function to check the status of a subdomain
def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "Up"
        else:
            return f"Down (Status code: {response.status_code})"
    except requests.RequestException as e:
        return f"Down ({e.__class__.__name__})"

# Main monitoring loop
def monitor_subdomains(subdomains):
    while True:
        # Create a table to display the results
        table = PrettyTable(["Subdomain", "Status"])
        
        # Check each subdomain
        for subdomain in subdomains:
            status = check_status(subdomain)
            table.add_row([subdomain, status])
        
        # Clear the screen (this works on most terminals)
        print("\033c", end="")  # For Linux/OS X, use 'cls' for Windows
        
        # Print the table
        print(table)
        
        # Wait for 60 seconds before checking again
        time.sleep(60)

# Start monitoring
if __name__ == "__main__":
    monitor_subdomains(subdomains)
