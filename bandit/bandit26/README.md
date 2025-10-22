# Bandit Level 26 → Level 27

## Level Goal

Good job getting a shell! Now hurry and grab the password for bandit27!

## Commands you may need to solve this level

    ls


### 🔑 Solution

```
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220 
```
![b26s1](b26s1.png)

Strange — the session terminates right after a successful login.

![b26s2](b26s2.png)

As we remember from the previous challenge, the shell for user *bandit26* is set to ``/usr/bin/showtext``, which runs `more ~/text.txt` and then exits.

![b26s3](b26s3.png)

We then used the `ssh` command with the ``-t`` option followed by `more` to force a pseudo-terminal. This produced some output, but the message seemed shorter than usual — which matches the expected behavior of the *bandit26* shell. As mentioned earlier, it simply runs `more ~/text.txt` and then exits. The file `text.txt` just contains the word 'bandit26' in ASCII art.
```
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220 -t more
```
![b26s4](b26s4.png)

### How does the `more` command work? 
If you try to view a large file — like `rockyou.txt`, which contains around 14 million lines — using the `cat` command, it would be overwhelming because it displays the entire content at once.

Using the `more` command to view a file lets you read the content one page at a time by pressing the `spacebar`, or one line at a time by pressing `Enter` — depending on your terminal's window size.

The `more` command continues displaying the content until you either reach the end of the file or exit manually by pressing `q`.

![more](more.png)

To take advantage of the `more` command’s behavior, we can reduce the size of our terminal window significantly and then run the command again.

![b26s5](b26s5.png)

Next, restore your terminal to its normal size. As expected, more displays only half of text.txt. Pressing `Spacebar`, `Enter`, or `q` causes more ~/text.txt to finish and exit — which we don’t want, because we intend to exploit this behavior.

To take advantage of this, press `V` to enter vi's visual mode.

![b26s6](b26s6.png)

🧭 The 6 Main Vim Modes
![vim](vim.jpg)

Now that we're viewing `text.txt` in the vi editor, we can manipulate it.

![b26s7](b26s7.png)

Run the following command to gain access to a regular bash shell.
```
:set shell=/bin/bash
Enter
:shell
Enter
```
![b26s8](b26s8.png)
![b26s9](b26s9.png)

Run `whoami` and `pwd` to verify that you are logged in as user *bandit26*.

![b26s10](b26s10.png)

List the files in the home directory with `ls`; we discovered a setuid program that lets us run commands with *bandit27* privileges.

![b26s11](b26s11.png)

Execute the command below to reveal the bandit27 password.
```
./bandit27-do cat /etc/bandit_pass/bandit27
```

![b26s12](b26s12.png)

🎉🎉 CHEERS — YOU’VE SECURED THE FLAG TO ADVANCE TO THE NEXT CHALLENGE! 🎉🎉