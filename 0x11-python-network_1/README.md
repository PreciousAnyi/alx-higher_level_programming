### Directory Description

This directory contains Python scripts related to network communication and web requests. Each script performs a specific task using different techniques and libraries such as urllib, requests, and sys.

---

### Files:

#### 0-hbtn_status.py
- **Description**: This script fetches the status of the website "https://alx-intranet.hbtn.io/status" using urllib.
- **Usage**: `./0-hbtn_status.py | cat -e`
- **Output Example**:
    ```
    Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
    ```

#### 1-hbtn_header.py
- **Description**: This script takes a URL as input, sends a request, and displays the value of the X-Request-Id variable found in the header of the response using urllib.
- **Usage**: `./1-hbtn_header.py https://alx-intranet.hbtn.io`
- **Output Example**: `ade2627e-41dd-4c34-b9d9-a0fa0f47b237`

#### 2-post_email.py
- **Description**: This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response using urllib.
- **Usage**: `./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com`
- **Output Example**: `Your email is: hr@holbertonschool.com`

#### 3-error_code.py
- **Description**: This script takes a URL as input, sends a request, and displays the body of the response. It handles urllib.error.HTTPError exceptions and prints the HTTP status code if it's greater than or equal to 400.
- **Usage**: `./3-error_code.py http://0.0.0.0:5000`
- **Output Example**: `Index` or `Error code: 401`

#### 4-hbtn_status.py
- **Description**: This script fetches the status of the website "https://alx-intranet.hbtn.io/status" using the requests package.
- **Usage**: `./4-hbtn_status.py | cat -e`
- **Output Example**:
    ```
    Body response:$
        - type: <class 'str'>$
        - content: OK$
    ```

#### 5-hbtn_header.py
- **Description**: This script takes a URL as input, sends a request, and displays the value of the X-Request-Id variable in the response header using the requests package.
- **Usage**: `./5-hbtn_header.py https://alx-intranet.hbtn.io`
- **Output Example**: `5e52e160-c822-4669-8b3a-8b3bbca7b090`

#### 6-post_email.py
- **Description**: This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response using the requests package.
- **Usage**: `./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com`
- **Output Example**: `Your email is: hr@holbertonschool.com`

#### 7-error_code.py
- **Description**: This script takes a URL as input, sends a request, and displays the body of the response. It prints the HTTP status code if it's greater than or equal to 400.
- **Usage**: `./7-error_code.py http://0.0.0.0:5000`
- **Output Example**: `Index` or `Error code: 401`

#### 8-json_api.py
- **Description**: This script takes a letter as input, sends a POST request to "http://0.0.0.0:5000/search_user" with the letter as a parameter, and displays the response body. It handles JSON formatting and displays the id and name if the JSON is properly formatted and not empty.
- **Usage**: `./8-json_api.py`
- **Output Example**: `No result` or `[8446] amnirqhtfjq`

#### 10-my_github.py
- **Description**: This script takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's id.
- **Usage**: `./10-my_github.py papamuziko cisfun`
- **Output Example**: `2531536`

---
