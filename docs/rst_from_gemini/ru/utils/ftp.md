```markdown
# `hypotez/src/utils/ftp.py`

This module provides an interface for interacting with FTP servers. It allows sending, receiving, and deleting files from an FTP server.

## Purpose

This module is designed to facilitate the transfer of various file types (images, videos, spreadsheets) to and from an FTP server.


## Modules Used

- `src.logger`: For logging errors and status messages.  (Assume this module exists and provides logging functionality.)
- `typing`: Provides type hints for function parameters and return values.
- `ftplib`: Provides the FTP protocol client capabilities.
- `pathlib`: Used for handling file system paths (though not directly used in the current code, the docstring is incomplete regarding usage).


## Functions

### `write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`

Sends a file to an FTP server.

**Args:**

* `source_file_path` (str): The path to the file to be sent on the local machine.  **Crucially, this should be an absolute path, not relative to the current working directory.**
* `dest_dir` (str): The destination directory on the FTP server.  **Must be a valid, existing directory on the server.**
* `dest_file_name` (str): The name of the file on the FTP server.

**Returns:**

* bool: `True` if the file is successfully sent, `False` otherwise.

**Raises:**

* `FileNotFoundError`: If the `source_file_path` does not exist.
* Other exceptions related to FTP connection or file operations.

**Example:**

```python
success = write("/path/to/local/file.jpg", "/remote/destination/directory", "remote_file.jpg")
if success:
  print("File sent successfully")
else:
  print("Failed to send file")
```

**Important Considerations:**

* **Error Handling:**  The function includes `try...except` blocks to catch and log potential errors during the connection and transfer. This is good practice, but could be improved with more specific error handling.  For example, knowing if the error is due to a network issue or a permission problem on the FTP server would be helpful.
* **Connection Details:** The `_connection` dictionary is not externally defined.  This needs to be a global variable, an environment variable, or passed in as a function parameter for improved maintainability.
* **File Existence Check:** The code doesn't verify if the source file exists, which could lead to errors. Add a `if not Path(source_file_path).is_file():` check before opening the file.

### `read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]`

Retrieves a file from an FTP server.

**Args:**

* `source_file_path` (str): The local path where the file will be saved. **Must be an absolute path or one relative to the current working directory.**
* `dest_dir` (str): The directory on the FTP server containing the file.
* `dest_file_name` (str): The name of the file on the FTP server.


**Returns:**

* `Union[str, bytes, None]`: The file content if successfully retrieved, `None` otherwise.


**Example:**

```python
content = read("/path/to/local/save/destination.txt", "/remote/directory", "remote_file.txt")
if content:
    print(content)
else:
    print("Failed to retrieve file")
```

**Important Considerations:**

* **Error Handling:**  Similar to `write`, improved error handling is needed.
* **File Overwrite:** The code does not handle the case where a file with the same name already exists in the destination location.  Consider adding a mechanism for handling potential file overwrite.

### `delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`

Deletes a file from an FTP server.

**Args:**

* `source_file_path` (str): The local path to the file (not used in the deletion process).
* `dest_dir` (str): The directory on the FTP server containing the file to be deleted.
* `dest_file_name` (str): The name of the file to be deleted on the FTP server.

**Returns:**

* `bool`: `True` if the file is successfully deleted, `False` otherwise.

**Example:**

```python
success = delete("/tmp/path/to/file.txt", "/remote/directory", "remote_file.txt")
if success:
    print("File deleted successfully")
else:
    print("Failed to delete file")
```

**Important Considerations:**

* **Error Handling:** The `try...except` block is good, but more specific error handling is recommended.  For example, the error type should be checked if the file doesn't exist.
* **Unnecessary Argument:** The `source_file_path` parameter is not needed; remove it.


This improved documentation provides a more comprehensive understanding of the functions and their usage, including crucial error handling considerations and critical parameters like file paths. Remember to address the critical error handling and file existence issues to create robust and reliable FTP operations.
