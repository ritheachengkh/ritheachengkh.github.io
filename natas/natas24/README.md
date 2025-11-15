# 🕸️Natas Level 24 → Level 25

```
http://natas24.natas.labs.overthewire.org
```
Username: natas24  
Password: (natas24_password)

![n24s1](n24s1.png)

We examined the **source page** and noticed that the ``strcmp()`` function is used to verify the password.

![n24s2](n24s2.png)

We looked it up online to see what the ``strcmp()`` function does.
https://www.php.net/manual/en/function.strcmp.php

![n24s3](n24s3.png)
![n24s4](n24s4.png)

Next, we tried using an `array` instead of a `string` to compare and observed how the program reacted.

![n24s5](n24s5.png)

Then PHP displayed some warnings, and the flag appeared.

![n24s6](n24s6.png)

Alternatively, you can use the `curl` command if you prefer working from the command line.
```
curl -u natas24:MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd \
-d "passwd[]" -s \
http://natas24.natas.labs.overthewire.org | grep -iE "username|password"
```
![n24s7](n24s7.png)

You got the flag! Let’s see what the next challenge has in store.




