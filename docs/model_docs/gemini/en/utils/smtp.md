```rst
hypotez/src/utils/smtp.rst
=========================

.. module:: hypotez.src.utils.smtp
   :platform: Windows, Unix
   :synopsis: SMTP Email Interface


This module provides functionality to send and receive emails using an SMTP or IMAP server.
It includes functions to send emails using SMTP and retrieve emails using IMAP.


Functions
---------

.. autofunction:: hypotez.src.utils.smtp.send
   :noindex:

.. autofunction:: hypotez.src.utils.smtp.receive
   :noindex:


Important Considerations
------------------------

**Security and Robustness**

- **_connection Dictionary:**  Do *not* hardcode credentials in this file.  Move the `_connection` dictionary to environment variables (e.g., using `os.environ`). This is crucial for security.  Avoid storing passwords directly in source code.

- **Error Handling:** The code includes robust error handling, logging exceptions with details (subject, body, etc.).  This is very helpful for debugging.

- **Email Parsing:** The `receive` function handles various email formats gracefully, preventing potential issues.

- **MIME Handling:** The code correctly uses `MIMEText` for constructing the email message, crucial for sending basic text emails.


.. automodule:: hypotez.src.utils.smtp
   :members:
   :undoc-members:
   :show-inheritance:
```
