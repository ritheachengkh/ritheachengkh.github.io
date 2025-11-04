# 🕸️Natas Level 9 → Level 10

```
http://natas9.natas.labs.overthewire.org
```
Username: natas9  
Password: (natas9_password)

![n9s1](n9s1.png)

`Ctrl + U` can help you uncover interesting clues — `index-source.html` looks particularly worth checking out.

![n9s2](n9s2.png)

We found the ``passthru()`` function, which runs a standard `grep -i $key dictionary.txt`, where ``$key`` comes directly from user input obtained via `needle`.  

In PHP, the ``passthru()`` function is used to execute an external program or command and directly output the raw result to the browser (or the standard output).

![n9s2p2](n9s2p2.png)

Now, we can test it by typing `test` in the input box and pressing Enter. 

![n9s3](n9s3.png)

It returns every word from `dictionary.txt` that contains the string `test`, which is the expected behavior of the `grep` command.

![n9s4](n9s4.png)


### 💉what is shell injection?
**Shell injection** (or command injection) is named after UNIX shells but applies to most systems that allow software to programmatically execute a command line.
![shell_injection](shell_injection.png)

Now, we’ll inject our command by replacing test with the payload we want.
```
;cat+/etc/natas_webpass/natas10
```
The ``;`` in the shell is used to separate multiple commands. It signals the end of the previous command and the start of a new command, allowing you to run them sequentially on a single line.  
The `+` in a URL query string is interpreted as a space in the context of URL-encoded form data.
So `cat+/etc/natas_webpass/natas10` → `cat /etc/natas_webpass/natas10` when the server reads the needle parameter.

![n9s5](n9s5.png)

The flag should be revealed after pressing Enter.

![n9s6](n9s6.png)

Here are more examples we can use to achieve the same result.
```
;cat%20/etc/natas_webpass/natas10
```
`%20` is the percent-encoded representation of a space character in URLs.
So `cat%20/etc/natas_webpass/natas10` → `cat /etc/natas_webpass/natas10` when decoded by the server.
```
|cat%20/etc/natas_webpass/natas10
||cat+/etc/natas_webpass/natas10
;more%20/etc/natas_webpass/natas10
;less+/etc/natas_webpass/natas10
;head%20/etc/natas_webpass/natas10
||tail+/etc/natas_webpass/natas10
```
![n9s7](n9s7.png)

### 💡 Handy percent-encodings for URLs you should know!
![URL_encoding](URL_encoding.png)

🛤️ You can also solve this challenge in a different way.

### 🧭 What is a Path Traversal Attack?
A **path traversal attack** (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths.
```
;cat ../../../../../etc/natas_webpass/natas10
```

![n9s8](n9s8.png)

Awesome work! You’ve got the flag needed for the next challenge.











