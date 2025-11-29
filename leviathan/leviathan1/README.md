# 🌊 Leviathan Level 1 → Level 2

```
ssh leviathan1@leviathan.labs.overthewire.org -p 2223
leviathan1_password
```

![l1s1](l1s1.png)

After running the `ls` command, we noticed a file named `check`, and then we executed it.
```
ls -la 
./check
```

![l1s2](l1s2.png)

Next, we ran `ltrace` to observe how the program operates and noticed it performing a string-comparison function.
```
ltrace ./check
```

![l1s3](l1s3.png)

After that, we used the word we found to capture the flag.
```
./check
sex
whoami
cat /etc/leviathan_pass/leviathan2
```

![l1s4](l1s4.png)

Well done! This flag will take you to the next round.
