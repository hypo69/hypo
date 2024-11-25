# hypotez/src/goog/quickstart.py

## Overview

This module provides a quickstart example for interacting with the Google Apps Script API in Python. It demonstrates how to create a new script project, upload files (JavaScript and manifest), and retrieve the script's URL.

## Table of Contents

* [Overview](#overview)
* [Constants](#constants)
* [Functions](#functions)
    * [`main`](#main)


## Constants

### `SCOPES`

**Description**: Defines the required scopes for accessing the Google Apps Script API.

**Value**: `['https://www.googleapis.com/auth/script.projects']`


### `SAMPLE_CODE`

**Description**: A sample JavaScript code snippet to be uploaded to the script project.

**Value**:  ```javascript
function helloWorld() {
  console.log("Hello, world!");
}
```


### `SAMPLE_MANIFEST`

**Description**: A sample manifest JSON to configure the script project.

**Value**: ```json
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
```


### `MODE`

**Description**: A constant that currently holds the value 'dev'.

**Value**: `'dev'`


## Functions

### `main`

**Description**: This function handles the interaction with the Google Apps Script API. It authenticates, creates a script project, uploads files, and prints the script's URL.


**Parameters**:
None


**Returns**:
None


**Raises**:
* `errors.HttpError`: An error occurred during the API request. The error content will be printed.


```python
def main():
    """Calls the Apps Script API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    token_path = gs.path.tmp / 'e-cat-346312-137284f4419e.json'
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with Path('token.json').open('w') as token:
            token.write(creds.to_json())

    try:
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        request = {'title': 'My Script'}
        response = service.projects().create(body=request).execute()

        # Upload two files to the project
        request = {
            'files': [
                {
                    'name': 'hello',
                    'type': 'SERVER_JS',
                    'source': SAMPLE_CODE
                },
                {
                    'name': 'appsscript',
                    'type': 'JSON',
                    'source': SAMPLE_MANIFEST
                }
            ]
        }
        response = service.projects().updateContent(
            body=request,
            scriptId=response['scriptId']).execute()
        print('https://script.google.com/d/' + response['scriptId'] + '/edit')
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)
```