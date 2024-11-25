# hypotez/src/utils/smtp.py

## Overview

This module provides an interface for sending and receiving emails using SMTP and IMAP protocols.  It includes functions for sending emails and retrieving emails from an IMAP server.  Crucially, it prioritizes security by storing credentials (SMTP server, username, password) in environment variables, preventing hardcoding sensitive information.

## Table of Contents

* [Sending Emails](#sending-emails)
* [Receiving Emails](#receiving-emails)


## Sending Emails

### `send`

**Description**: Sends an email using the configured SMTP server.

**Parameters**:

- `subject` (str, optional): The subject of the email. Defaults to an empty string.
- `body` (str, optional): The body of the email. Defaults to an empty string.
- `to` (str, optional): The recipient's email address. Defaults to 'one.last.bit@gmail.com'.

**Returns**:

- bool: `True` if the email was sent successfully, `False` otherwise.

**Raises**:

- `Exception`: Any exception raised during the SMTP connection, authentication, or sending process.  Error details are logged.


## Receiving Emails

### `receive`

**Description**: Retrieves emails from an IMAP server.

**Parameters**:

- `imap_server` (str): The IMAP server address.
- `user` (str): The IMAP user (email) address.
- `password` (str): The IMAP password.
- `folder` (str, optional): The folder to retrieve emails from. Defaults to 'inbox'.

**Returns**:

- Optional[List[Dict[str, str]]]: A list of dictionaries containing email data (subject, from, body) if successful, `None` otherwise.


**Raises**:

- `Exception`: Any exception raised during the IMAP connection, authentication, or email retrieval process.  Error details are logged.