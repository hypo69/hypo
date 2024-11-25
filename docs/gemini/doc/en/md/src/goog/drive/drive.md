# hypotez/src/goog/drive/drive.py

## Overview

This module provides a minimal library for interacting with Google Drive. It includes a class, `GoogleDriveHandler`, for handling file uploads and retrieval.  It utilizes the Google Drive API to perform these tasks.  The module also contains example usage to demonstrate how to use the handler.

## Classes

### `GoogleDriveHandler`

**Description**: This class manages interactions with the Google Drive API. It handles authentication and provides methods for uploading files to a specific folder.

**Methods**:

#### `__init__(self, folder_name: str)`

**Description**: Initializes the `GoogleDriveHandler` object.

**Parameters**:

- `folder_name` (str): The name of the folder in Google Drive where files should be uploaded.

#### `_create_credentials(self)`

**Description**: Authenticates with Google Drive and retrieves or creates credentials.

**Returns**:

- `Credentials`: Valid Google Drive credentials.


#### `upload_file(self, file_path: Path)`

**Description**: Uploads a file to the specified folder in Google Drive.

**Parameters**:

- `file_path` (Path): The path to the file to be uploaded.

## Functions

### `main()`

**Description**: Demonstrates basic usage of the `GoogleDriveHandler` class. It retrieves and prints a list of files from Google Drive.


**Returns**:

- None. Prints a list of files from Google Drive


## Module Level Variables


### `MODE`

**Description:** The module level variable MODE.


## Example Usage

```python
if __name__ == "__main__":
    from pathlib import Path

    file_path = Path('/mnt/data/google_extracted/sample_file.txt')  # Replace with your actual file path
    folder_name = 'My Drive Folder'  # Replace with the target folder name in Google Drive

    google_drive_handler = GoogleDriveHandler(
        folder_name=folder_name,
    )
    google_drive_handler.upload_file(file_path)
```


```python
import pickle
import os
from pathlib import Path
from googleapiclient.discovery import build
from google_auth_httplib2 import AuthorizedHttpTransport
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import header
from src import gs
from src.utils import pprint
from src.logger import logger
```

**Note**: The example usage shows how to call `upload_file` but the implementation of the method is commented out and needs to be completed for the code to function. Also, replace placeholder file paths with the actual file paths for testing purposes.



```
```
```