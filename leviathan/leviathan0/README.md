# 🌊 Leviathan Level 0 → Level 1

```
ssh leviathan0@leviathan.labs.overthewire.org -p 2223
leviathan0
```

![l0s1](l0s1.png)

After you log in successfully, this will appear.

![l0s2](l0s2.png)

After running the `ls` command, you’ll notice a hidden folder called ``.backup``.
```
ls -la
cd .backup
```

![l0s3](l0s3.png)

Inside the ``.backup`` folder, you’ll find `bookmarks.html`. Use the following command to grep the flag.
```
cat bookmarks.html | grep leviathan
```

![l0s4](l0s4.png)

Great job! Use this flag to advance to the next stage.
