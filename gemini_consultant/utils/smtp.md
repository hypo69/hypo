```python
## \file hypotez/src/utils/smtp.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.utils """


"""
SMTP Email Interface

This module provides functionality to send and receive emails using an SMTP or IMAP server.
It includes functions to send emails using SMTP and retrieve emails using IMAP.

Functions:
    - `send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool`
      Sends an email using the SMTP server specified in the `_connection` dictionary.
    
    - `receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[dict]]`
      Retrieves emails from an IMAP server and returns them as a list of dictionaries.

** Notes **:
    - Replace placeholders in the `_connection` dictionary with actual server details and credentials.
    - Sensitive information such as passwords should be moved to environment variables for security.  **CRITICALLY IMPORTANT**.
    - Use `email.message_from_string()` instead of `email.message_from_bytes()`.
"""

import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from typing import List, Dict, Optional
import os

from src.logger import logger

# Critically important: Get connection details from environment variables.
# NEVER hardcode passwords in code.
_connection = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', 587)),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'one.last.bit@gmail.com')
}

# CRITICAL: Check if necessary environment variables are set.
for key in ['SMTP_USER', 'SMTP_PASSWORD']:
  if os.environ.get(key) is None:
    logger.critical(f"Environment variable {key} not set! Exiting.")
    exit(1)


def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """
    Sends an email using the SMTP server specified in the `_connection` dictionary.
    """
    try:
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.login(_connection['user'], _connection['password'])

        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = _connection['user']
        message["To"] = to

        smtp.send_message(message)  # Use send_message for better efficiency
        smtp.quit()
        return True

    except Exception as ex:
        logger.error(f"Error sending email: {ex}", exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Retrieves emails from an IMAP server.
    """
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
            msg = email.message_from_string(raw_email.decode('utf-8'))  # Decode to string

            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                'body': msg.get_payload(decode=True).decode('utf-8', errors='ignore')  # Decode and handle errors
            }
            emails.append(email_data)

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Error receiving emails: {ex}", exc_info=True)
        return None
```

**Explanation of Improvements and Crucial Changes:**

* **Environment Variables:** The code now retrieves SMTP server details, username, and password from environment variables.  This is **absolutely critical** for security.  You **must** set these variables in your system (e.g., using `export SMTP_USER=your_email@example.com` in Linux/macOS, or similar methods in Windows).
* **Error Handling (Crucial):** The `send` and `receive` functions now include more robust error handling, logging exceptions with `exc_info=True` for better debugging.
* **Environment Variable Check:** Checks if `SMTP_USER` and `SMTP_PASSWORD` environment variables are set.  If not, it logs a critical error and exits, preventing the script from running with potentially dangerous missing credentials.
* **`smtp.send_message`:** Using `send_message` instead of `sendmail` for sending the email is more efficient and often preferred.
* **Error Handling in `receive`:** Added `errors='ignore'` to `decode` when extracting the email body.  This will prevent the script from crashing if there are issues with email encoding.
* **Decoding to string:** Now `email.message_from_string` is used. This is crucial, as the data fetched from `imaplib.IMAP4_SSL` is byte-oriented, and the email library expects a string object.
* **`mail.close()`:** Added `mail.close()` to properly disconnect from the IMAP server.

**How to Use:**

1.  **Set Environment Variables:**
    ```bash
    export SMTP_SERVER="your_smtp_server"
    export SMTP_PORT="587"  #or the appropriate port
    export SMTP_USER="your_email@example.com"
    export SMTP_PASSWORD="your_password"
    export SMTP_RECEIVER="recipient_email@example.com"
    ```
2.  **Run the script:**
    ```bash
    python your_script.py
    ```

**Important Considerations:**

*   **Security:**  Never hardcode passwords in your Python code.  Always use environment variables.
*   **Error Handling:**  The improved error handling will give you much more information if something goes wrong.
*   **Email Libraries:** Use the `email` library for handling email content—avoid manually constructing MIME messages.


This revised solution is much safer, more robust, and easier to maintain in a production setting. Remember to replace the placeholders with your actual server details. Remember to install the necessary libraries. `pip install imaplib` and `email` if you don't have them.