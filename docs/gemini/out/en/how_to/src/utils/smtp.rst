rst
How to use the smtp.py module
========================================================================================

Description
-------------------------
This module provides functions for sending and receiving emails using SMTP and IMAP servers.  It includes robust error handling and utilizes environment variables for security, preventing hardcoding of credentials.  `send` sends emails, and `receive` retrieves them from an IMAP server.

Execution steps
-------------------------
1. **Configure Environment Variables:**  Set environment variables for SMTP server details (e.g., `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_RECEIVER`).  Crucially, *do not* hardcode these credentials directly into the script.  Use `os.environ.get()` to retrieve values from the environment.


2. **Import the Module:** Import the `send` and `receive` functions from the `smtp.py` module.  For example:

   ```python
   from hypotez.src.utils.smtp import send, receive
   ```

3. **Sending Email (send function):**
   - Call the `send` function, providing the email subject, body, and recipient address.
   - The `to` parameter defaults to the value in the `_connection` dictionary (which itself defaults to `one.last.bit@gmail.com`) unless specified.  For example:
     ```python
     success = send(subject="Test Email", body="This is a test email.", to="recipient@example.com")
     if success:
         print("Email sent successfully")
     else:
         print("Failed to send email")
     ```

4. **Receiving Email (receive function):**
   - Call the `receive` function, supplying the IMAP server, user, password, and optional folder.
   - The `receive` function returns a list of email dictionaries if successful, or `None` on error.   Each dictionary in the list contains the email's subject, sender, and body.
   - For example:

     ```python
     imap_server = "imap.example.com"
     user = "your_imap_user"
     password = "your_imap_password"
     inbox_emails = receive(imap_server, user, password)
     if inbox_emails:
         for email in inbox_emails:
             print(f"Subject: {email['subject']}\nFrom: {email['from']}\nBody: {email['body']}\n")
     else:
         print("Failed to retrieve emails.")
     ```

Usage example
-------------------------
.. code-block:: python

    import os
    from hypotez.src.utils.smtp import send, receive

    # Set environment variables (crucial for security!)
    os.environ['SMTP_SERVER'] = 'smtp.example.com'
    os.environ['SMTP_PORT'] = '587'
    os.environ['SMTP_USER'] = 'your_smtp_user'
    os.environ['SMTP_PASSWORD'] = 'your_smtp_password'
    os.environ['SMTP_RECEIVER'] = 'recipient@example.com'
    
    # Send an email
    success = send(subject="Test Email", body="This is a test message.", to="recipient@example.com")
    if success:
        print("Email sent successfully")
    else:
        print("Failed to send email.")

    # Receive emails (replace with your IMAP server details)
    imap_server = 'imap.gmail.com'
    imap_user = 'your_gmail_user'
    imap_password = 'your_gmail_password'
    emails = receive(imap_server, imap_user, imap_password)
    if emails:
        for email in emails:
            print(f"Subject: {email['subject']}\nFrom: {email['from']}\nBody: {email['body']}\n")
    else:
        print("Failed to retrieve emails.")