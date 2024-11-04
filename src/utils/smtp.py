## \file src/utils/interface/smtp.py
## \file src/utils/smtp.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

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
    - Sensitive information such as passwords should be moved to environment variables for security.
"""

import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger import logger

# Example _connection dictionary structure (replace with actual details)
_connection = {
    'server': 'smtp.example.com',
    'port': 587,
    'user': 'user@example.com',
    'password': 'password',
    'receiver': 'receiver@example.com'
}

def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """
    Sends an email using the SMTP server specified in the `_connection` dictionary.

    Args:
        subject (str): The subject line of the email (default: '').
        body (str): The body of the email (default: '').
        to (str): The email address of the recipient (default: 'one.last.bit@gmail.com').

    Returns:
        bool: True if the email was sent successfully, False otherwise.

    Example:
        >>> send(subject="Test", body="This is a test email.")
        True
    """
    try:
        # Create an instance of the SMTP class and connect to the server
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        smtp.starttls()  # Enable encryption
        smtp.login(_connection['user'], _connection['password'])

        # Create a MIME message with the specified subject, body, and recipient
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = _connection['user']
        message["To"] = to

        # Send the email
        smtp.sendmail(_connection['user'], to, message.as_string())
        smtp.quit()
        return True

    except Exception as ex:
        # Log the error and return if a connection couldn't be established or email couldn't be sent
        logger.error(f"Error sending email. Subject: {subject}. Body: {body}. Error: {ex}", exc_info=True)
        return False

def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Retrieves emails from an IMAP server and returns them as a list of dictionaries.

    Args:
        imap_server (str): The IMAP server address.
        user (str): The username for login.
        password (str): The password for login.
        folder (str, optional): The folder from which to retrieve emails (default: 'inbox').

    Returns:
        Optional[List[Dict[str, str]]]: A list of dictionaries, each containing email details, or None if an error occurred.

    Example:
        >>> emails = receive('imap.example.com', 'user@example.com', 'password')
        >>> print(emails)
        [{'subject': 'Test Email', 'from': 'sender@example.com', 'body': 'This is a test email.'}]
    """
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(user, password)
        mail.select(folder)

        # Search for all emails in the folder
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
                'body': msg.get_payload(decode=True).decode('utf-8')
            }
            emails.append(email_data)

        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Error occurred while retrieving emails: {ex}", exc_info=True)
        return
