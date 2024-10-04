#Documentation
1. Purpose
This script is designed to monitor the status of subdomains of a website, checking whether they are reachable or not. It sends HTTP requests to each subdomain, determines their status (up or down), and displays this information in a table format that is updated every minute.

2. How It Works
The script contains a predefined list of subdomains to monitor.
It uses the requests library to send HTTP requests and determine whether each subdomain is reachable.
If a subdomain responds with a status code of 200, it is marked as "Up". If there is an error (e.g., timeout, connection error), the subdomain is marked as "Down".
The results are displayed in a table using the prettytable library, and the screen is updated every 60 seconds.
3. Execution Flow
Subdomain List: You can modify the list of subdomains at the beginning of the script.
Status Check: The check_status() function checks each subdomain and returns its status.
Display Table: The PrettyTable object is used to format the output in a readable table. It is cleared and refreshed every minute.
Looping: The script continues indefinitely, checking the status every 60 seconds.
4. Dependencies
requests: For sending HTTP requests.
prettytable: For displaying the output in a table format.
time: To introduce delays (60-second intervals).

5. Usage
    1. Install dependencies:
    pip install requests prettytable
    2. Modify the list of subdomains to the ones you want to monitor.
    3. Run the script (python xyz.py)
    4. The table will automatically update every minute with the latest status of each subdomain.

6. Error Handling
The script handles common HTTP errors, such as timeouts or connection failures, and appropriately displays the error type (e.g., Timeout or ConnectionError) in the table.


