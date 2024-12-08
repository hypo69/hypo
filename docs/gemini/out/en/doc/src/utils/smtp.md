# hypotez/src/utils/smtp.py

## Overview

This module provides functionality for sending and receiving emails using SMTP and IMAP servers.  It prioritizes security by avoiding hardcoding credentials and using environment variables instead.  Robust error handling and logging are implemented for debugging purposes.


## Table of Contents

* [Functions](#functions)


## Functions

### `send`

**Description**: Sends an email using the SMTP server specified in the `_connection` dictionary.

**Parameters**:

* `subject` (str, optional): The subject of the email. Defaults to an empty string.
* `body` (str, optional): The body of the email. Defaults to an empty string.
* `to` (str, optional): The recipient's email address. Defaults to `'one.last.bit@gmail.com'`.

**Returns**:

* `bool`: `True` if the email was sent successfully, `False` otherwise.

**Raises**:

* `Exception`: Any exception raised during the SMTP connection or sending process.  Detailed error logging is included.


### `receive`

**Description**: Retrieves emails from an IMAP server.

**Parameters**:

* `imap_server` (str): The IMAP server address.
* `user` (str): The IMAP user.
* `password` (str): The IMAP password.
* `folder` (str, optional): The email folder to retrieve from (defaults to 'inbox').

**Returns**:

* `Optional[List[Dict[str, str]]]`: A list of email dictionaries if successful, `None` otherwise.  Each dictionary contains the `subject`, `from`, and `body` of an email.

**Raises**:

* `Exception`: Any exception raised during the IMAP connection or email retrieval process. Detailed error logging is included.