# 🌊 Leviathan Level 3 → Level 4

```
ssh leviathan3@leviathan.labs.overthewire.org -p 2223
leviathan3_password
```

![l3s1](l3s1.png)

After running the `ls` command, we found a program file named `level3` and executed it.
```
ls -la
./level3
```

![l3s2](l3s2.png)

Then we executed ltrace to analyze how the program works and saw a string comparison function.
```
ltrace ./level3 
```

![l3s3](l3s3.png)

After that, we ran level3 again and obtained a shell.
```
./level3
snlprintf
whoami
cat /etc/leviathan_pass/leviathan4
```

![l3s4](l3s4.png)

Fantastic! This flag will allow you to progress to the next round.
