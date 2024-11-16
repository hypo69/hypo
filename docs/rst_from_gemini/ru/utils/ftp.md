```markdown
# ftp.py

This module provides an interface for interacting with FTP servers.  It includes functions to send, receive, and delete files from an FTP server.

**Purpose:**

Allows for sending media files (images, videos), spreadsheets, and other files to and from an FTP server.


**Modules Used:**

* `src.logger`: For logging errors and information.
* `typing`: For type hinting function parameters and return values.
* `ftplib`: Provides the FTP protocol client capabilities.
* `pathlib`: (implicitly used) for handling file system paths, though not directly used in these functions.

**Functions:**

* **`write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`**:
    * Sends a file to an FTP server.
    * **Args:**
        * `source_file_path` (str): The path to the file on the local file system.
        * `dest_dir` (str): The destination directory on the FTP server.  Must be an absolute path.
        * `dest_file_name` (str): The name of the file on the FTP server.
    * **Returns:**
        * `bool`: `True` if the file is successfully sent, `False` otherwise.
    * **Error Handling:**  Includes robust error handling for connection failures, file operations, and closing the FTP session.  Critically important for production code.
    * **Example:**
```python
success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
```

* **`read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]`**:
    * Retrieves a file from an FTP server.
    * **Args:**
        * `source_file_path` (str): The path where the file will be saved on the local file system.
        * `dest_dir` (str): The directory on the FTP server where the file is located. Must be an absolute path.
        * `dest_file_name` (str): The name of the file on the FTP server.
    * **Returns:**
        * `Union[str, bytes, None]`: The file content as bytes if successfully retrieved, `None` otherwise.
    * **Error Handling:**  Similar error handling to `write`, crucial for reliability.
    * **Example:**
```python
content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
if content:
  print(content)  # Output: the file content as bytes
```

* **`delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`**:
    * Deletes a file from an FTP server.
    * **Args:**
        * `source_file_path` (str):  The path where the file is located locally (not used in the implementation; should be removed).
        * `dest_dir` (str): The directory on the FTP server where the file is located. Must be an absolute path.
        * `dest_file_name` (str): The name of the file on the FTP server.
    * **Returns:**
        * `bool`: `True` if the file is successfully deleted, `False` otherwise.
    * **Error Handling:** Includes error handling for connection and deletion failures.
    * **Important Consideration:** The `source_file_path` parameter is not used in the `delete` function.  This is a potential bug; the parameter should be removed to reflect that the local path is not necessary for deletion.


**Important Considerations:**

* **`_connection` Dictionary:** The `_connection` dictionary is used for storing connection details.  This is a good practice for maintainability. Consider making it more configurable, perhaps a class or a config file.
* **Error Logging:**  The use of `logger` from `src.logger` is excellent for debugging and monitoring.
* **Robust Error Handling:**  The `try...except...finally` blocks are essential to ensure the FTP session is always properly closed, even if errors occur. This prevents resource leaks.
* **`source_file_path` in `delete`:** As mentioned, the `source_file_path` parameter in the `delete` function is redundant and should be removed.
* **Type Hinting:** Using type hints makes the code more readable and maintainable.
* **Absolute Paths:** Ensure that `dest_dir` values are absolute paths, not relative ones.  Relative paths will break.


**How to use:**

1.  Import the `ftp` module.
2.  Call the appropriate function (`write`, `read`, or `delete`) with the necessary parameters.  Remember to replace placeholder values like `ftp.example.com`, `username`, and `password` with your actual FTP server details.
3.  Handle the return value appropriately, checking for success or failure.



```