# hypotez/src/utils/ftp.py

## Overview

This module provides an interface for interacting with FTP servers. It includes functions to send, receive, and delete files from an FTP server.  It facilitates the transfer of various file types, including images, videos, and spreadsheets, to and from an FTP server.

## Table of Contents

- [Functions](#functions)
    - [`write`](#write)
    - [`read`](#read)
    - [`delete`](#delete)


## Functions

### `write`

**Description**: Sends a file to an FTP server.

**Parameters**:
- `source_file_path` (str): The path of the file to be sent.
- `dest_dir` (str): The destination directory on the FTP server.
- `dest_file_name` (str): The name of the file on the FTP server.

**Returns**:
- bool: True if the file is successfully sent, False otherwise.

**Example Usage**:
```python
success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
```

**Raises**:
- `Exception`: Any exception during FTP connection or file transfer will be caught and logged, preventing the function from crashing.


### `read`

**Description**: Retrieves a file from an FTP server.

**Parameters**:
- `source_file_path` (str): The path where the file will be saved locally.
- `dest_dir` (str): The directory on the FTP server where the file is located.
- `dest_file_name` (str): The name of the file on the FTP server.

**Returns**:
- Union[str, bytes, None]: The file content if successfully retrieved, `None` otherwise.

**Example Usage**:
```python
content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(content)
```

**Raises**:
- `Exception`: Any exception during FTP connection or file retrieval will be caught and logged.


### `delete`

**Description**: Deletes a file from an FTP server.

**Parameters**:
- `source_file_path` (str): The path where the file is located locally (not used in this operation).
- `dest_dir` (str): The directory on the FTP server where the file is located.
- `dest_file_name` (str): The name of the file on the FTP server.

**Returns**:
- bool: True if the file is successfully deleted, False otherwise.


**Example Usage**:
```python
success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
```

**Raises**:
- `Exception`: Any exception during FTP connection or file deletion will be caught and logged.