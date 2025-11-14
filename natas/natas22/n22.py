import requests


# Credentials for natas22
username = "natas22"
password = "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz"

# Target URL
url = "http://natas22.natas.labs.overthewire.org?revelio"

# Start a session to persist cookies and headers across requests
session = requests.Session()

response = session.get(
    url,
    allow_redirects = False, ## Do not automatically follow HTTP redirects (like 302)
    auth=(username, password)
)

print(response.text)