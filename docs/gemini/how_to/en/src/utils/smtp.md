# Usage Guide for `hypotez/src/utils/smtp.py`

This guide describes how to use the SMTP email interface module for sending and receiving emails.  Crucially, it emphasizes secure practices by avoiding hardcoding credentials.

## Sending Emails (`send` function)

To send an email, use the `send` function:

```python
from hypotez.src.utils.smtp import send

# Configure email details.  Crucially, these values MUST be set via environment variables.
# Example using os.environ for security:
import os
os.environ['SMTP_SERVER'] = 'smtp.example.com'
os.environ['SMTP_PORT'] = '587'
os.environ['SMTP_USER'] = 'your_email@example.com'
os.environ['SMTP_PASSWORD'] = 'your_password'
os.environ['SMTP_RECEIVER'] = 'recipient@example.com'

# Optional parameters
success = send(subject="Test Email", body="This is a test email.", to='another_recipient@example.com')

if success:
    print("Email sent successfully!")
else:
    print("Failed to send email.")
```

**Explanation:**

1. **Environment Variables:**  The code retrieves SMTP server details, port, username, password, and receiver email address from environment variables.  **This is essential for security.**  Do *not* hardcode these values in your Python code.

2. **Error Handling:**  The `send` function includes a `try...except` block to catch and log any exceptions during email sending. This allows you to identify and troubleshoot problems.

3. **Clear Return Value:** The function returns `True` if the email was sent successfully and `False` otherwise.  This allows calling code to immediately understand the outcome.


## Receiving Emails (`receive` function)

To receive emails, use the `receive` function:

```python
from hypotez.src.utils.smtp import receive

# Example Usage:
imap_server = 'imap.example.com'
user = 'your_email@example.com'
password = 'your_password'
emails = receive(imap_server, user, password)

if emails:
    for email_data in emails:
        print(f"Subject: {email_data['subject']}")
        print(f"From: {email_data['from']}")
        print(f"Body: {email_data['body']}\n")

else:
    print("Failed to retrieve emails.")

```

**Explanation:**

1. **Parameters:** The `receive` function takes the IMAP server, username, password, and optional folder as input.

2. **Error Handling:** Like the `send` function, this function includes robust error handling and logs issues to the `logger` for debugging.

3. **Data Structure:**  The function returns a list of dictionaries. Each dictionary contains the email subject, sender, and body.  **Critically**, the body is decoded to handle different encodings and potential errors.

4. **Error Return:** If any error occurs, it returns `None`.  Check for this to handle potential errors.

**Important Security Notes:**

* **Environment Variables:**  Always retrieve sensitive information (passwords, API keys) from environment variables, not directly from code.  This is crucial for security.
* **Secure Email Settings:** Configure your email provider's settings for security, including enabling appropriate protocols (e.g., TLS/SSL).
* **Strong Passwords:** Use strong, unique passwords for your email accounts.

**Logging:**

The code uses a `logger` (likely from `src.logger`), which you need to implement appropriately to handle logging messages. Ensure you configure this logger properly.  The `exc_info=True` in the `logger.error` calls is critical for detailed stack traces when errors occur.