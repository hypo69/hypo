hypotez/src/utils/ftp.py
==========================

.. module:: hypotez.src.utils.ftp
   :platform: Windows, Unix
   :synopsis: interface for interacting with FTP servers

This module provides an interface for interacting with FTP servers.  It includes functions to send, receive, and delete files from an FTP server.

**Purpose**:
Allows for sending media files (images, videos), spreadsheets, and other files to and from an FTP server.

**Modules**:
- helpers (local): Local helper utilities for FTP operations.
- typing: Type hints for function parameters and return values.
- ftplib: Provides FTP protocol client capabilities.
- pathlib: For handling file system paths.

**Functions**:
- :py:func:`write`
- :py:func:`read`
- :py:func:`delete`

.. autofunction:: write
.. autofunction:: read
.. autofunction:: delete