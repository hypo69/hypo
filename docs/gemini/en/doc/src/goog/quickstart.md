# hypotez/src/goog/quickstart.py

## Overview

This module provides a quickstart example for interacting with the Google Apps Script API. It demonstrates how to create a new Apps Script project, upload code files (JavaScript and manifest), and retrieve the project's URL.


## Classes

### No classes defined in this module.


## Functions

### `main`

**Description**: This function orchestrates the interaction with the Google Apps Script API. It handles authentication, creating a project, uploading files, and logging the project's URL.

**Parameters**:
  None.

**Returns**:
  None.

**Raises**:
    - `errors.HttpError`: Raised if the API call encounters an error (e.g., invalid credentials, network issue). Error details are printed to the console.


## Variables

### `MODE`

**Description**:  A string variable, likely holding a mode value (e.g., 'dev', 'prod').


### `SCOPES`

**Description**: A list of scopes required by the Apps Script API.

**Value**: `['https://www.googleapis.com/auth/script.projects']`


### `SAMPLE_CODE`

**Description**: A string containing sample JavaScript code to be uploaded to the Apps Script project.

**Value**: `function helloWorld() { console.log("Hello, world!"); }`

### `SAMPLE_MANIFEST`

**Description**: A string containing a sample Apps Script manifest to be uploaded to the project.

**Value**: `{ "timeZone": "America/New_York", "exceptionLogging": "CLOUD" }`

### `token_path`

**Description**:  The path to the token.json file, used for storing the user's access and refresh tokens. This is dynamically determined.


## Modules

### `header`

**Description**: This module is imported but not used directly in this file.


### `gs`

**Description**: This module is imported but not used directly in this file. Its purpose is not defined here.


## Notes

- The code assumes a `credentials.json` file exists, containing the client secrets for accessing the Google Apps Script API.
- It uses `google-auth-oauthlib` for authentication.
- It uses `pathlib` for file handling.