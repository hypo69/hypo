# Code Explanation for hypotez/src/utils/smtp.py

## <input code>

```python
## \file hypotez/src/utils/smtp.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: SMTP Email Interface

"""
MODE = 'dev'


""" This module provides functionality to send and receive emails using an SMTP or IMAP server.
It includes functions to send emails using SMTP and retrieve emails using IMAP.

Functions:
    - `send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool`
      Sends an email using the SMTP server specified in the `_connection` dictionary.  Returns `True` on success, `False` on failure.  Includes error logging.
    
    - `receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]`
      Retrieves emails from an IMAP server and returns them as a list of dictionaries.  Returns `None` on error. Includes error logging.


** Important Considerations for Security and Robustness **:

    - **_connection Dictionary:** Do *not* hardcode credentials in this file.  Move the `_connection` dictionary to environment variables (e.g., using `os.environ`). This is crucial for security.  Avoid storing passwords directly in source code.

    - **Error Handling:** The code includes robust error handling, logging exceptions with details (subject, body, etc.).  This is very helpful for debugging.

    - **Email Parsing:** The `receive` function handles various email formats gracefully, preventing potential issues.

    - **MIME Handling:**  The code correctly uses `MIMEText` for constructing the email message, crucial for sending basic text emails.


"""

import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger import logger

# --- Configuration ---
# DO NOT HARDCODE CREDENTIALS HERE!  Use environment variables instead.
_connection = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', 587)),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'one.last.bit@gmail.com')
}


def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """Sends an email.  Returns True if successful, False otherwise. Logs errors."""
    try:
        # Create SMTP connection
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.login(_connection['user'], _connection['password'])

        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = _connection['user']
        message["To"] = to

        smtp.sendmail(_connection['user'], to, message.as_string())
        smtp.quit()
        return True

    except Exception as ex:
        logger.error(f"Error sending email. Subject: {subject}. Body: {body}. Error: {ex}", exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """Retrieves emails. Returns a list of email dictionaries if successful, None otherwise. Logs errors."""
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(user, password)
        mail.select(folder)

        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        emails = []
        for email_id in email_ids:
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                'body': msg.get_payload(decode=True, _charset="utf-8").decode("utf-8", "ignore")  # Decode & handle potential errors
            }
            emails.append(email_data)

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Error occurred while retrieving emails: {ex}", exc_info=True)
        return None
```

## <algorithm>

**Email Sending (send function):**

1. **Connection:** Establishes SMTP connection using the credentials in `_connection`.
2. **Authentication:** Authenticates the sender using username and password.
3. **Message Construction:** Creates an email message using `MIMEText` containing the subject and body.
4. **Sending:** Sends the email to the recipient specified by `to`.
5. **Disconnection:** Closes the connection.

**Email Receiving (receive function):**

1. **Connection:** Establishes IMAP connection using the provided server, user, and password.
2. **Selection:** Selects the specified folder (default: inbox).
3. **Search:** Searches for all emails in the selected folder.
4. **Email Iteration:** Iterates through each email ID.
5. **Email Data Extraction:** Fetches the raw email data and parses it using `email.message_from_bytes`.
6. **Data Extraction:** Extracts relevant email details (subject, sender, body).
7. **Storage:** Stores the extracted email data into a list of dictionaries.
8. **Disconnection:** Closes the IMAP connection.

## <mermaid>

```mermaid
graph TD
    subgraph SMTP Email Sending
        A[send(subject, body, to)] --> B{SMTP Connection};
        B --> C[Authentication];
        C --> D[Message Creation];
        D --> E[Sending Email];
        E --> F[Connection Close];
        F --> G[Return True];
    end
    subgraph IMAP Email Receiving
        A2[receive(imap_server, user, password, folder)] --> B2{IMAP Connection};
        B2 --> C2[Folder Selection];
        C2 --> D2[Search for Emails];
        D2 --> E2[Email Iteration];
        E2 --> F2[Fetch Email Data];
        F2 --> G2[Data Extraction];
        G2 --> H2[Store Email Data];
        H2 --> I2[Connection Close];
        I2 --> J2[Return Emails List];
    end
    A --> A2;
    G --> K[Error Handling];
    J2 --> K;
    G2 --> K;


    classDef error fill:#fdd
    class K, K2 error
```

**Dependencies Analysis:**

* `smtplib`: Provides SMTP (Simple Mail Transfer Protocol) functionality for sending emails.
* `imaplib`: Provides IMAP (Internet Message Access Protocol) functionality for retrieving emails.
* `email`: Provides email parsing capabilities.
* `os`: Used for getting environment variables (critical for security).
* `typing`: Used for type hinting.
* `MIMEText`: A subclass of `email.mime.Message` for creating simple email messages.
* `logger`: Custom logger from the `src.logger` package for error handling.  Crucial for maintaining a unified logging approach within the project.

## <explanation>

**Imports:**

* `smtplib`, `imaplib`, `email`: Standard Python libraries for interacting with SMTP and IMAP servers.
* `os`: Used to retrieve environment variables.
* `MIMEText`:  For constructing email messages (critical for sending textual emails).
* `typing`:  Adds type hints (`List`, `Dict`, `Optional`) for better code readability and maintainability.
* `src.logger`:  Indicates that the module leverages a custom logging system (likely from the `logger.py` file located within the `src` package). This is a best practice to centralized logging.


**Classes:**

* No custom classes are defined. The module relies on standard Python library classes such as `smtplib.SMTP` and `imaplib.IMAP4_SSL`.

**Functions:**

* `send(subject, body, to)`: Sends an email.
    * Takes subject, body, and recipient email address as input.
    * Uses the `_connection` dictionary for SMTP server details.
    * Returns `True` for successful sending, `False` otherwise.
    * Includes robust error handling with `try-except` blocks and logs exceptions to the `logger`. Example:
      ```python
      send("Hello", "This is a test email", "recipient@example.com")
      ```

* `receive(imap_server, user, password, folder)`: Retrieves emails from an IMAP server.
    * Takes IMAP server details, user, password and optional folder (default 'inbox').
    * Returns a list of email dictionaries containing 'subject', 'from', and 'body' or `None` in case of failure.
    * Includes error handling and logs exceptions to the `logger`.  Handles various email formats, including decoding issues. Example:
      ```python
      emails = receive("imap.example.com", "user", "password", "important")
      ```

**Variables:**

* `_connection`: A dictionary storing SMTP server credentials.  This is crucial to avoid hardcoding secrets directly into the code (high-risk practice).  It's crucial to get these values from environment variables for security.
* `MODE`: A variable set to 'dev' (possibly for conditional logic or logging).
* `logger`: A variable assigned to a `logger` object from the `src.logger` package.



**Potential Errors/Improvements:**

* **Security:** The most critical aspect is the use of environment variables for storing credentials.  This significantly improves the security of the code by avoiding storing sensitive data directly in the source code.
* **Error Logging:** The use of `logger.error` is good. Consider adding more specific logging information (e.g., SMTP response codes in the `send` function).
* **Robustness:** The `receive` function handles email body decoding (`decode("utf-8", "ignore")`). This is a good step to ensure code stability in various environments.
* **Input Validation:** Consider adding checks for invalid input types and values to `send` and `receive` (e.g., checking if `to` is a valid email address).
* **Email Structure:** The `receive` function handles basic email structure well.  Adding checks for potentially malformed emails may enhance future robustness, especially if dealing with complex email structures (e.g., multipart MIME).


**Relationship with other project parts:**

The `src.logger` import suggests a larger project structure where logging functionality is centralized in a separate module (`logger.py`) within the `src` package. This promotes better code organization and maintainability.  This `smtp.py` module leverages this centralized logging to improve code health and maintainability within the project.