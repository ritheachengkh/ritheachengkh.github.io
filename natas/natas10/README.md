# 🕸️Natas Level 10 → Level 11

```
http://natas10.natas.labs.overthewire.org
```
Username: natas10  
Password: (natas10_password)

![n10s1](n10s1.png)

After checking the page source, we discovered that the special characters ``/[;|&]/`` were restricted this time.

![n10s2](n10s2.png)

We can leverage `grep` to access and read the file to finish this challenge — see the examples below.
```
grep .* pass.txt test.txt
```
This is a regular expression (regex) pattern.  
- ``.`` (dot) means “any single character.”  
- ``*`` (asterisk) means “zero or more times.”  
Together, ``.*`` matches any text on a line — effectively, it matches everything.

![n10s3](n10s3.png)

Next, we enter `test` into the input field and inject our command into the URL

![n10s4](n10s4.png)

### 🌐 Here are some useful URL encodings.
![URL_encoding](URL_encoding.png)

```
.*%20/etc/natas_webpass/natas11
```
![n10s5](n10s5.png)

Follow the steps above and the flag should appear.

![n10s6](n10s6.png)

Fantastic! This flag is your key to the next challenge.
