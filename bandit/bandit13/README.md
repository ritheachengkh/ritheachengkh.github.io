# Bandit Level 13 → Level 14

## Level Goal

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

## Commands you may need to solve this level

    ssh, telnet, nc, openssl, s_client, nmap

## Helpful Reading Material

    SSH/OpenSSH/Keys

### 🔑 Solution

```
ssh bandit13@bandit.labs.overthewire.org -p 2220
```
Now type in the password you grabbed from the last challenge.

Rather than capturing a password as before, this challenge involves retrieving the private key for SSH authentication.

![b13s1](b13s1.png)

Use the `cat` command to display the contents of the SSH private key. Then, select all the text, right-click to copy, or press Ctrl + Shift + C. Finally, type exit to close the session.

![b13s2](b13s2.png)

Next, create a directory, navigate into it using `cd`, and use the `nano` command to create a new file.

![b13s3](b13s3.png)

In the new session, press **Ctrl + Shift + V** to paste the content you copied earlier.

![b13s4](b13s4.png)

Then, press **Ctrl + X**, respond with **Y**, and press **Enter** to complete the process.

![b13s5](b13s5.png)

With the new session closed, you return to the prior session. Congrats on successfully creating and saving your new file!

![b13s6](b13s6.png)

Alternatively, you can use `scp` to copy the sshkey.private file.  

**SCP (Secure Copy Protocol)** is a command-line tool used to securely transfer files between computers over a network. It uses SSH (Secure Shell) to provide encryption, ensuring that data is safely transmitted without being intercepted.

You can do this by running the command below:
```
scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .
```
![b13s7](b13s7.png)

You’ve got the key — on to the next challenge!


