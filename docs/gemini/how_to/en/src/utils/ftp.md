How to use the `hypotez/src/utils/ftp.py` module

This module provides functions for interacting with FTP servers.  It allows sending, receiving, and deleting files.  Crucially, it handles potential errors and closes the FTP session to prevent issues.


**Before you begin:**

* **Configuration:** The code assumes an `_connection` dictionary (defined outside this module) holds FTP server details: server address, port, username, and password.  This dictionary must be pre-populated with correct values.

* **Error Handling:** The functions include `try...except` blocks to catch and log errors during connection, file transfer, and session closure.  Always check the log for any issues.


**Functions:**

* **`write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`**

    * **Purpose:** Sends a file to the FTP server.
    * **Arguments:**
        * `source_file_path` (str): The local path to the file to be sent.  **Must be a valid path to an existing file.**
        * `dest_dir` (str): The destination directory on the FTP server (e.g., `/remote/directory`). **Must be a valid directory on the remote server.**
        * `dest_file_name` (str): The name of the file on the FTP server.
    * **Return Value:**
        * `bool`: `True` if the file is successfully sent, `False` otherwise.  Check the log for any errors.
    * **Example Usage:**

```python
import os
# ... other imports and _connection initialization ...

# Create a sample file for testing
file_to_send = "path/to/test_file.txt"
with open(file_to_send, "w") as f:
  f.write("This is a test file.")

success = write(file_to_send, "/remote/directory", "test_file.txt")

if success:
    print("File sent successfully!")
else:
    print("Failed to send file.")

# Clean up the test file
os.remove(file_to_send)
```

* **`read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]`**

    * **Purpose:** Retrieves a file from the FTP server.
    * **Arguments:**
        * `source_file_path` (str): The local path where the retrieved file will be saved. **Must be a valid path.**  The file will be created locally.
        * `dest_dir` (str): The directory on the FTP server where the file is located.
        * `dest_file_name` (str): The name of the file on the FTP server.
    * **Return Value:**
        * `Union[str, bytes, None]`: The file content as bytes if successfully retrieved, `None` otherwise.  Check the log for errors.
    * **Example Usage:**
```python
import os

# ... _connection initialization ...
local_path = "path/to/retrieve_test.txt"
success = read(local_path, "/remote/directory", "test_file.txt")

if success:
    with open(local_path, 'wb') as f:
        f.write(success)
    print("File retrieved successfully!")
else:
    print("Failed to retrieve file.")

# Clean up the downloaded file (if needed)
os.remove(local_path)
```
* **`delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`**

    * **Purpose:** Deletes a file from the FTP server.
    * **Arguments and Return Value:** Similar to `write`, but this function doesn't use the `source_file_path` argument.
    * **Example Usage:**  Similar to the other examples, but replace the `read` call with the `delete` function.


**Important Considerations:**

* **Error Logging:** The `logger` module is crucial.  Examine its output to diagnose issues.
* **File Paths:** Double-check that file and directory paths are correctly specified, both locally and on the FTP server.
* **Permissions:** Ensure that the user account has the necessary permissions to read, write, and delete files on the FTP server.
* **Connection Details:**  Make sure the `_connection` dictionary contains the correct FTP server details.


This expanded guide provides a more complete understanding of how to use the FTP functions effectively, focusing on error handling and crucial considerations for successful file operations. Remember to install the necessary packages (`ftplib`, `pathlib`, and your chosen logging library).