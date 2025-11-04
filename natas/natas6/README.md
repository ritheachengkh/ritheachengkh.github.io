# 🕸️Natas Level 6 → Level 7

```
http://natas6.natas.labs.overthewire.org
```
Username: natas6  
Password: (natas6_password)

![n6s1](n6s1.png)

We start by looking at the source page to uncover potential clues.

![n6s2](n6s2.png)

The file `includes/secret.inc` caught our attention, so we decided to check it out.

![n6s3](n6s3.png)

We found the value of ``$secret`` and copied it.

![n6s4](n6s4.png)

### 🌀Useful curl command
![curl_command](curl_command.png)

```
curl -u natas6:0RoJwHdSKWFTYR5WuiAewauSuNaBXned \
-d "secret=FOEIUWGHFEEUHOFUOIU&submit=Submit" \
http://natas6.natas.labs.overthewire.org/
```
``-u user:pass`` — Supplies Basic Auth credentials.  
`-d` (short for ``--data``) sends the provided string as POST body data. When you use -d, curl sets the request method to POST automatically (unless overridden with -X).  
``URL`` — The target server/page.  

![n6s5](n6s5.png)

Alternatively, you can simply copy and paste `FOEIUWGHFEEUHOFUOIU` into the secret input box and click submit.

![n6s6](n6s6.png)

Following these steps, the flag should be displayed.

![n6s7](n6s7.png)

Excellent! Use this flag to proceed to the next round.


