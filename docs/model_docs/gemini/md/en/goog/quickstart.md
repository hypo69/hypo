```markdown
# hypotez/src/goog/quickstart.py

## Overview

This module provides a Python script for interacting with the Google Apps Script API.  It demonstrates creating a new Apps Script project, uploading code and manifest files, and retrieving the script's URL.  It leverages the `googleapiclient` library and handles authentication and error handling.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`main`](#main)


## Functions

### `main`

**Description**: This function orchestrates the interaction with the Google Apps Script API. It handles authentication, creating a new script project, uploading code and manifest files, and printing the script's URL to the console.

**Parameters**: None

**Returns**: None

**Raises**:
- `googleapiclient.errors.HttpError`: Raised if there's an issue communicating with the Google Apps Script API, such as invalid credentials or a server error.


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
            'files': [{
                'name': 'hello',
                'type': 'SERVER_JS',
                'source': SAMPLE_CODE
            }, {
                'name': 'appsscript',
                'type': 'JSON',
                'source': SAMPLE_MANIFEST
            }]
        }
        response = service.projects().updateContent(
            body=request,
            scriptId=response['scriptId']).execute()
        print('https://script.google.com/d/' + response['scriptId'] + '/edit')
    except errors.HttpError as ex:
        # The API encountered a problem.
        print(ex.content)


```
```