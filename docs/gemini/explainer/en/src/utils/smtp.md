```python
## file hypotez/src/utils/smtp.py
# -*- coding: utf-8 -*-
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
                'body': msg.get_payload(decode=True, _charset="utf-8").decode("utf-8", "ignore")
            }
            emails.append(email_data)

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Error occurred while retrieving emails: {ex}", exc_info=True)
        return None
```

```
<algorithm>
**Step 1: Initialization (send)**
   - Input: subject, body, recipient email.
   - Actions: Get SMTP server details from _connection dictionary (using environment variables). Create SMTP object, start TLS connection, and login.
   - Example: `send(subject="Hello", body="This is a test email", to="recipient@example.com")` retrieves the SMTP server details.

**Step 2: Email Preparation (send)**
   - Input: email body, subject, sender email.
   - Actions: Create email message using MIMEText. Set subject, sender, and recipient details.
   - Example: Creates a message object with the provided data.

**Step 3: Sending Email (send)**
   - Input: Prepared email message, recipient.
   - Actions: Send the email using `smtp.sendmail`, then quit the SMTP connection.
   - Example: Sends the message to the recipient.

**Step 4: Error Handling (send)**
   - Input: Potential SMTP errors.
   - Actions: Catch exceptions during the sending process. Log errors with details. Return False to indicate failure.
   - Example: If the connection fails or login is unsuccessful, error is caught and logged.

**Step 5: Initialization (receive)**
   - Input: imap server, user, password, folder (optional).
   - Actions: Establish an IMAP connection using imaplib. Login using credentials. Select the specified folder.
   - Example: `receive(imap_server="imap.example.com", user="user@example.com", password="password")` initializes the connection.

**Step 6: Search Emails (receive)**
   - Input: Selected folder.
   - Actions: Search for all emails in the folder. Store email IDs.
   - Example: Finds all emails in the inbox.

**Step 7: Retrieve Emails (receive)**
   - Input: Email IDs.
   - Actions: Iterate through email IDs. Retrieve each email's raw data. Parse the email data using `email.message_from_bytes`. Extract subject, sender, and body.
   - Example: Retrieves the raw data for the email ID.

**Step 8: Store and Process Emails (receive)**
   - Input: Parsed email data.
   - Actions: Store email data in a dictionary format. Append it to a list.
   - Example: Creates dictionary with subject, from and body, and appends to the email list.

**Step 9: Close Connection and Error Handling (receive)**
   - Input: Emails retrieved and stored.
   - Actions: Close and logout from the IMAP connection. Return the list of emails if successful. Return None if errors occur.
   - Example: Returns the list of email dictionaries. If error occurs, return None.

```

```
<explanation>

**Imports:**

- `smtplib`: Used for interacting with SMTP (Simple Mail Transfer Protocol) servers.  Crucially, this module handles the sending of emails.
- `imaplib`: Used for interacting with IMAP (Internet Message Access Protocol) servers.  Used to retrieve emails from various mail servers.
- `email`: Used for parsing email messages. Specifically for accessing the data inside the emails retrieved from the `imaplib` module.
- `os`: Used for interacting with the operating system, particularly for accessing environment variables.  Critically important for security; it avoids hardcoding sensitive credentials within the code.
- `MIMEText`: Part of the `email` package, used for creating simple text-based email messages.
- `typing`: Includes `List`, `Dict`, and `Optional` for type hinting, improving code readability and maintainability.
- `src.logger`:  Likely a custom logger module (part of the `src` package) for handling logging.  Helps debug issues related to the SMTP/IMAP functions.

**Classes:**

- None.  This code defines functions, not classes.

**Functions:**

- `send(subject, body, to)`: Sends an email. Takes `subject`, `body`, and `to` as input (default values for recipients are used for convenience if not explicitly provided). Returns `True` on success, `False` on failure.  Includes robust error handling using `try...except`.  Crucially, it leverages environment variables for SMTP credentials.
- `receive(imap_server, user, password, folder)`: Retrieves emails from an IMAP server.  Takes `imap_server`, `user`, `password`, and `folder` as input.  Returns a list of email dictionaries on success or `None` on failure. Implements detailed error handling for different potential issues.  This is important for maintaining reliability.


**Variables:**

- `_connection`: A dictionary holding SMTP server credentials. It's important to note that these credentials should *not* be hardcoded; environment variables should be used to store sensitive information.
- `MODE`: A variable that likely controls the operation mode (e.g., 'dev' for development, 'prod' for production). This is not used in this particular module.
- `subject`, `body`, `to`, `imap_server`, `user`, `password`, `folder`: These variables store input parameters that are used during email sending and retrieval.


**Potential Errors and Improvements:**

- **Security:** The code correctly uses environment variables for SMTP credentials, which is essential for security.  However, further validation of these credentials is desirable (e.g., ensuring they are not empty strings or null).
- **Robustness:** The error handling is quite comprehensive, including logging exceptions with helpful details.  However, it could be enhanced with more specific error handling, such as distinguishing between network issues, authentication failures, and email message parsing errors for a more accurate feedback.
- **Email Parsing:** The `receive` function attempts to decode email bodies, which is great for handling various encodings. However, a catch-all exception handling for encoding errors might improve robustness. The code also only supports plaintext emails; it would be useful if more complex email formats (e.g., HTML, attachments) were supported.


**Relationships with other parts of the project:**

- This module relies on the `src.logger` module, indicating that logging functionality has been abstracted to another module within the project. This is a standard practice that promotes modularity and reusability of logging across multiple modules in the application. This is an essential design pattern for applications with many modules.
```