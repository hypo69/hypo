```rst
hypotez/src/utils/ftp.rst
=========================

.. module:: hypotez.src.utils.ftp
    :platform: Windows, Unix
    :synopsis: Interface for interacting with FTP servers

This module provides an interface for interacting with FTP servers. It includes functions to send, receive, and delete files from an FTP server.

**Purpose**:
Allows for sending media files (images, videos), spreadsheets, and other files to and from an FTP server.

**Modules**:
- helpers (local): Local helper utilities for FTP operations.
- typing: Type hints for function parameters and return values.
- ftplib: Provides FTP protocol client capabilities.
- pathlib: For handling file system paths.

Functions
---------

.. autofunction:: hypotez.src.utils.ftp.write
.. autofunction:: hypotez.src.utils.ftp.read
.. autofunction:: hypotez.src.utils.ftp.delete
```