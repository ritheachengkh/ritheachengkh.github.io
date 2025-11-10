# 🕸️Natas Level 1 → Level 2

```
http://natas1.natas.labs.overthewire.org
```
Username: natas1  
Password: (natas1_password)


### Useful `curl -w` or ``--write-out`` Variable
| **Variable**            | **Meaning**                                  |
|-------------------------|----------------------------------------------|
| `%{time_total}`         | Total transaction time in seconds            |
| `%{time_starttransfer}` | Time until the first byte is received (TTFB) |
| `%{time_connect}`       | Time until TCP connection established        |
| `%{time_appconnect}`    | Time until SSL/TLS handshake completes       |
| `%{time_namelookup}`    | Time until DNS resolution completed          |
| `%{time_pretransfer}`   | Time until transfer about to start           |
| `%{size_download}`      | Total bytes downloaded                       |
| `%{size_upload}`        | Total bytes uploaded                         |
| `%{size_header}`        | Size of headers received                     |
| `%{size_request}`       | Request size sent (headers + body)           |
| `%{speed_download}`     | Average download speed (bytes/sec)           |
| `%{speed_upload}`       | Average upload speed (bytes/sec)             |
| `%{http_code}`          | Final HTTP response code                     |
| `%{num_redirects}`      | Number of redirects followed                 |
| `%{url_effective}`      | Final effective URL (after redirects)        |
| `%{content_type}`       | Content-Type of response                     |
| `%{remote_ip}`          | IP address of remote server                  |
| `%{remote_port}`        | Remote port used                             |
| `%{local_ip}`           | Local IP used for the connection             |
| `%{local_port}`         | Local port used                              |
| `%{num_connects}`       | Number of new connections made               |
| `%{filename_effective}` | Final output filename (after redirects)      |
| `%{scheme}`             | URL scheme used (`http`, `https`, etc.)      |
| `%{http_connect}`       | HTTP response code from a proxy CONNECT      |
| `%{redirect_url}`       | URL a redirect points to (if any)            |
| `%{stderr}`             | Send output to stderr (useful for scripting) |
| `%{json}`               | Output all available metrics in JSON         |