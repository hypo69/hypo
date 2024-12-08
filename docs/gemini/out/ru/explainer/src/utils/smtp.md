# <input code>

```python
## \file hypotez/src/utils/smtp.py
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

# <algorithm>

**send() function algorithm:**

1. **Connection:** Establish an SMTP connection to the server specified in `_connection`.
2. **Authentication:** Authenticate with the server using the credentials from `_connection`.
3. **Email Creation:** Create an email message using `MIMEText` with the provided `subject`, `body`, and `to` address.  The `from` address is taken from `_connection`.
4. **Sending:** Send the email using `smtp.sendmail()`.
5. **Closing:** Close the SMTP connection (`smtp.quit()`).
6. **Error Handling:** A `try...except` block catches potential errors during any step and logs the error, returning `False` in case of failure.

**receive() function algorithm:**

1. **Connection:** Establish an IMAP connection to the server.
2. **Authentication:** Authenticate with the IMAP server using the provided `user` and `password`.
3. **Folder Selection:** Select the desired email folder (default is 'inbox').
4. **Email Retrieval:** Search for all emails in the selected folder.
5. **Email Processing:** Iterate through each email ID:
   - Fetch the raw email data.
   - Parse the email using `email.message_from_bytes()`.
   - Extract the `subject`, `from`, and `body`. The body is decoded to handle different encodings gracefully.
   - Store the extracted email data as a dictionary in the `emails` list.
6. **Closing:** Close and logout from the IMAP server.
7. **Error Handling:** A `try...except` block catches potential errors during any step and logs the error, returning `None` in case of failure.


# <mermaid>

```mermaid
graph TD
    A[send(subject, body, to)] --> B{Establish SMTP connection};
    B -- Success --> C[Authentication];
    C -- Success --> D{Create email message};
    D --> E[Send email];
    E -- Success --> F[Close connection];
    F --> G[Return True];
    E -- Error --> H[Log error & Return False];
    B -- Failure --> H;
    C -- Failure --> H;
    D -- Failure --> H;

    I[receive(imap_server, user, password, folder)] --> J{Establish IMAP connection};
    J -- Success --> K[Authentication];
    K -- Success --> L[Select folder];
    L --> M[Search emails];
    M --> N(Iterate through email IDs);
    N --> O{Fetch email data};
    O --> P[Parse email];
    P --> Q{Extract subject, from, body};
    Q --> R[Store email data];
    R --> S[Append to emails list];
    N -- End of emails --> T[Close and logout];
    T --> U[Return emails];
    O -- Error --> V[Log error & Return None];
    J -- Failure --> V;
    K -- Failure --> V;
    L -- Failure --> V;
    M -- Failure --> V;
    N -- Error --> V;
    P -- Error --> V;
    Q -- Error --> V;

    subgraph Dependencies
        logger --> "src.logger";
        smtplib --> "smtplib";
        imaplib --> "imaplib";
        email --> "email";
        os --> "os";
        MIMEText --> "email.mime.text";
    end
```

**Dependencies:**

The `smtp.py` file relies on several Python modules:

- `smtplib`: For interacting with SMTP servers.
- `imaplib`: For interacting with IMAP servers.
- `email`: For parsing and manipulating email messages.
- `os`: For interacting with the operating system, particularly for accessing environment variables.
- `MIMEText`: For constructing email messages from text.
- `logger`:  From a custom `logger` module presumably in the `src` directory.


# <explanation>

**Imports:**

- `smtplib`, `imaplib`, `email`, `os`: Standard Python libraries for interacting with email servers and accessing the operating system.
- `MIMEText`: Part of the `email` library, used for creating email messages.
- `from typing import List, Dict, Optional`:  For type hinting (useful for code clarity and static analysis).
- `from src.logger import logger`: Imports a custom logger from another module in the `src` project.  This is crucial for separating concerns and enabling log configuration. This module provides structured logging.

**Classes:**

There are no classes defined directly in this file. The code uses several classes and objects from standard libraries like `smtplib` and `imaplib` implicitly.


**Functions:**

- `send(subject, body, to)`: Sends an email. Takes the `subject`, `body`, and recipient `to` address as arguments.  Returns `True` on success and `False` on failure, logging errors appropriately.  Critically, it uses environment variables to retrieve SMTP server credentials (`_connection` dict), preventing hardcoding sensitive data directly into the code.

- `receive(imap_server, user, password, folder)`: Retrieves emails from an IMAP server. Takes the IMAP server details (`imap_server`, `user`, `password`) and the folder to search (`folder`, defaulting to 'inbox') as arguments.  Returns a list of email dictionaries (`subject`, `from`, `body`) if successful, `None` otherwise.  Crucially, it handles email decoding and potential errors (`decode("utf-8", "ignore")`) for robustness.


**Variables:**

- `_connection`: A dictionary that stores SMTP server configuration.  This is designed to be populated from environment variables (`os.environ`) for security reasons.
- `MODE`:  A variable (currently unused).  It might represent a development/production mode flag.

**Error Handling:**

The use of `try...except` blocks in both `send` and `receive` provides robust error handling, logging detailed error messages using the `logger` for debugging. This is crucial for production code.


**Possible Improvements:**

- **More sophisticated email handling:** The `receive` function could handle different MIME types for email content (attachments, etc.).
- **Connection pooling:** For repeated email sending, consider using a connection pool to reduce overhead.
- **Rate limiting:**  Implement rate limits to prevent overloading the mail servers.
- **Email validation:** Include validation for `to` address or email content in `send` function to reduce possible issues.

**Relationships with other parts of the project:**

The `logger` import indicates a dependency on the `src.logger` module, suggesting that this `smtp.py` module is part of a larger application where logging is handled elsewhere.  This structure promotes modularity and maintainability. The use of environment variables also points to a broader system where configuration is managed externally.