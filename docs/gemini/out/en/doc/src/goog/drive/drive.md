# src.goog.drive

## Overview

This module provides a minimal library for interacting with Google Drive. It includes a class (`GoogleDriveHandler`) to manage authentication and uploading files.

## Classes

### `GoogleDriveHandler`

**Description**: This class handles interactions with the Google Drive API. It manages authentication and provides a method for uploading files.

**Methods**:

#### `__init__(self, folder_name: str)`

**Description**: Initializes the `GoogleDriveHandler` object.

**Parameters**:

- `folder_name` (str): The name of the folder in Google Drive where the file should be uploaded.


#### `_create_credentials(self)`

**Description**: Retrieves or creates valid Google Drive API credentials.  It checks for existing credentials in a 'token.pickle' file.  If no valid credentials are found, it prompts the user to authorize the application.

**Returns**:

- `Credentials`: The authenticated credentials object.


#### `upload_file(self, file_path: Path)`

**Description**: Uploads a file to the specified folder in Google Drive.

**Parameters**:

- `file_path` (Path): The path to the file to be uploaded.


## Functions

### `main()`

**Description**: This function demonStartes basic usage of the `GoogleDriveHandler` class by creating an instance, getting credentials, and listing files in the user's Google Drive.

**Returns**:

- None


## Usage Example

```python
from pathlib import Path

file_path = Path('/mnt/data/google_extracted/sample_file.txt')  # Replace with your actual file path
folder_name = 'My Drive Folder'  # Replace with the target folder name in Google Drive

google_drive_handler = GoogleDriveHandler(
    folder_name=folder_name,
)
google_drive_handler.upload_file(file_path)
```


```python
if __name__ == '__main__':
    main()
```

This example demonStartes how to create a `GoogleDriveHandler` instance, specify the folder name, and then call the `upload_file` method to upload a file.  Remember to replace placeholders like `'/mnt/data/google_extracted/sample_file.txt'` with the actual file path and desired folder name.


## Notes

- Ensure that the necessary Google Drive API client libraries are installed (`google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`).
- Replace the example file path with the actual path to the file you want to upload.
- You need to replace `'hypo69-c32c8736ca62.json'` with the correct path to your service account credentials file.
- This code assumes the existence of the `header`, `gs`, `printer`, and `logger` modules, which are not provided in the snippet, and need to be included in the project's structure.  Please define them appropriately in your project to complete the library.