rst
How to use the FTP utility functions
========================================================================================
Description
-------------------------
This module provides functions for interacting with FTP servers.  It allows sending files to, retrieving files from, and deleting files on an FTP server.  The functions (`write`, `read`, `delete`) handle the connection, file transfer, and closing of the FTP session.  Error handling and logging are implemented to manage potential issues during the process.  Configuration for the FTP server (e.g., address, username, password) is assumed to be stored in the `_connection` dictionary.

Execution steps
-------------------------
1. **Import necessary modules:** Import the `ftplib`, `pathlib`, and any other required modules. In this case, `ftplib` is imported for FTP operations, `pathlib` is included for file path handling, and `Union` (from `typing`) is used for type hinting in return values. The `logger` module, presumably defined elsewhere, handles logging.


2. **Establish the FTP connection:** The `write`, `read`, and `delete` functions all establish a connection to the FTP server using the credentials stored in the `_connection` dictionary.


3. **Change working directory (cwd):** The function `session.cwd(dest_dir)` is used to move to the desired directory on the FTP server before performing file operations.


4. **Send the file (`write`):**
   - Open the source file in binary read mode (`'rb'`).
   - Use `session.storbinary()` to transfer the file to the specified destination.


5. **Retrieve the file (`read`):**
   - Open a local file in binary write mode (`'wb'`) to receive the file.
   - Use `session.retrbinary()` to retrieve the file from the FTP server and write it to the local file.
   - Read the content of the locally saved file and return it.


6. **Delete the file (`delete`):**
   - Use `session.delete()` to remove the specified file from the FTP server.


7. **Close the FTP session:**  The `session.quit()` method is crucial to close the connection after each operation, preventing resource leaks. The `finally` block ensures the session is closed even if errors occur during file operations.


8. **Error handling:** Each function includes `try...except` blocks to catch potential exceptions (e.g., connection issues, file not found). These exceptions are logged using the `logger` module for error tracking.



Usage example
-------------------------
.. code-block:: python

    import ftplib
    from pathlib import Path
    from hypotez.src.utils.ftp import write

    # Assume _connection is defined elsewhere
    # Example connection configuration
    _connection = {
        'server': 'ftp.example.com',
        'port': 21,
        'user': 'your_username',
        'password': 'your_password'
    }


    source_file_path = 'path/to/your/local/file.txt'
    dest_dir = '/remote/directory'
    dest_file_name = 'file.txt'

    success = write(source_file_path, dest_dir, dest_file_name)

    if success:
        print("File sent successfully!")
    else:
        print("Failed to send file.")