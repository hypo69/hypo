## File hypotez/src/utils/ftp.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: interface for interacting with FTP servers
This module provides an interface for interacting with FTP servers. It includes functions to send, receive, and delete files from an FTP server.

** Purpose **:
Allows for sending media files (images, videos), spreadsheets, and other files to and from an FTP server. 

** Modules **:
- helpers (local): Local helper utilities for FTP operations.
- typing: Type hints for function parameters and return values.
- ftplib: Provides FTP protocol client capabilities.
- pathlib: For handling file system paths.

Functions:
    - `write`: Sends a file to an FTP server.
    - `read`: Retrieves a file from an FTP server.
    - `delete`: Deletes a file from an FTP server.
"""
MODE = 'dev'
from src.logger import logger
from typing import Union
import ftplib
from pathlib import Path

# Connection configuration (assumed to be defined elsewhere)
_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}

def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Sends a file to an FTP server.

    Args:
        source_file_path (str): The path of the file to be sent.
        dest_dir (str): The destination directory on the FTP server.
        dest_file_name (str): The name of the file on the FTP server.

    Returns:
        bool: True if the file is successfully sent, False otherwise.

    Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        # Establish connection to FTP server
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)
    except Exception as ex:
        # Log error if connection to FTP server fails
        logger.error(f"Failed to connect to FTP server. Error: {ex}")
        return False

    try:
        # Open the file and send it to the FTP server
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Log error if file transfer to FTP server fails
        logger.error(f"Failed to send file to FTP server. Error: {ex}")
        return False
    finally:
        try:
            # Close the FTP session
            session.quit()
        except Exception as ex:
            logger.error(f"Failed to close FTP session. Error: {ex}")

# ... (read and delete functions are similar)
```

```
<algorithm>
```
**Overall Workflow (for write function):**

```mermaid
graph TD
    A[Start] --> B{Connection to FTP};
    B -- Success --> C[Change Directory];
    B -- Failure --> D[Log Error & Return False];
    C --> E{Open Source File};
    E --> F[Send File];
    F -- Success --> G[Log Success & Return True];
    F -- Failure --> H[Log Error & Return False];
    G --> I[Close FTP Session];
    H --> I;
    I --> J[End];

    subgraph FTP Connection
        B -- Example --> C1[ftplib.FTP("ftp.example.com", "username", "password")];
        C1 --> C2[session.cwd("/remote/directory")];
        C2 --> B;
    end

    subgraph File Sending
        E -- Example --> E1[open("local_path/to/file.txt", "rb")];
        E1 --> F1[session.storbinary("STOR file.txt", E1)];
        F1 --> F;
    end
```

**Example Data Flow (write):**

* **Input:** `source_file_path` = "/tmp/myimage.jpg", `dest_dir` = "/images", `dest_file_name` = "myimage.jpg"
* **Connection:** Establishes FTP session with `ftp.example.com`, `username`, `password`
* **Directory Change:** Changes the directory on the FTP server to "/images".
* **File Open:** Opens the local file "/tmp/myimage.jpg" in binary read mode.
* **File Transfer:** Sends the content of the local file to the FTP server as "myimage.jpg" in the "/images" directory.
* **Success:** Returns `True`.


```
<explanation>

**Imports:**

* `src.logger`: Imports a logging module from the `src` package, likely for error handling and logging file operations to the server.  The relationship is that the FTP utility depends on the logging facility for error tracking.

* `typing.Union`:  Defines the `Union` type, used to specify that a function can return different types, such as a string or bytes. This improves code clarity and type safety.

* `ftplib`: Provides the FTP protocol client capabilities needed for interacting with the FTP server.

* `pathlib.Path`: Provides classes for working with filesystem paths. It's used here (though not explicitly, only hinted at with `str`)  for file path manipulation.

**Classes:**

* No classes are defined in this code.

**Functions:**

* `write(source_file_path, dest_dir, dest_file_name)`: Takes the local file path, destination directory on the server, and the desired server filename.  Opens the local file in binary read mode ('rb'), uses `ftplib.FTP` to connect to the server, and sends the file content using `storbinary`.  Critically, it handles potential errors (e.g., connection issues, transfer problems) using `try...except` blocks and logs errors to the logger.  It also includes a finally block to ensure the FTP session is closed. This is a crucial best practice for resource management.

* `read(source_file_path, dest_dir, dest_file_name)`: Retrieves a file from the FTP server.  Similar to `write`, handles connection and retrieval with error checking, and ensures the session is closed.  It's important to note that it returns either the file content (as bytes) or `None` if an error occurs. This way, the caller can check for the success of the operation.

* `delete(source_file_path, dest_dir, dest_file_name)`: Deletes a file from the FTP server.  Similar structure and error handling to the others. Importantly, the `source_file_path` argument is not used within this function, suggesting potential redundancy or a design consideration that needs to be addressed if the local path might be useful for error reporting or validation.

**Variables:**

* `_connection`: A dictionary containing FTP server credentials. This should be loaded from a configuration file or environment variables for better security and maintainability. Hardcoding credentials directly in the code is a security risk.


**Potential Errors and Improvements:**

* **Hardcoded credentials:** The `_connection` dictionary has hardcoded credentials (`'ftp.example.com'`, `'username'`, `'password'`).  This is a significant security vulnerability.  The function should read these from a configuration file or environment variables.

* **Error Handling:** While the functions handle potential exceptions, the specific type of exception and possible root causes could be logged more completely.

* **Robustness:** Missing checks for file existence (locally and remotely).  Consider adding a check if the `dest_file_name` already exists on the FTP server in `write` (to avoid overwriting existing files).


**Relationship Chain:**

This code in `hypotez/src/utils/ftp.py` depends on `src.logger` for logging.