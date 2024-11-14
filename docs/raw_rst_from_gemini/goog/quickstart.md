```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.

https://developers.google.com/apps-script/api/quickstart/python
"""

import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

# Replace with your actual import if it exists.  This is crucial.
# from __init__ import gs  # <<-- INCORRECT, this is likely causing problems

# If using a virtual environment, adjust this path accordingly
# If using a different storage location, adjust this accordingly
TOKEN_PATH = Path(os.path.expanduser("~/.hypotez/token.json"))

# IMPORTANT: Set this to the path of your credentials.json file.
CREDENTIALS_PATH = Path(os.path.expanduser("~/.hypotez/credentials.json"))



SCOPES = ['https://www.googleapis.com/auth/script.projects']

SAMPLE_CODE = '''
function helloWorld() {
  console.log("Hello, world!");
}
'''.strip()

SAMPLE_MANIFEST = '''
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
'''.strip()


def main():
    """Calls the Apps Script API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_PATH), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with TOKEN_PATH.open('w') as token:
            token.write(creds.to_json())

    try:
        service = build('script', 'v1', credentials=creds)

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
        print(f'https://script.google.com/d/{response["scriptId"]}/edit')
    except errors.HttpError as error:
        print(f'An error occurred: {error}')
        print(error.content)  # Print the full error details


if __name__ == '__main__':
    main()
```

**Explanation of Changes and Improvements:**

* **`gs` import removal:** The original code tried to import `gs` from `__init__.py`.  This is likely incorrect and caused problems. Removed the line and replaced it with a commented out placeholder indicating that a proper way to handle it depends on the context of the project.

* **`TOKEN_PATH` and `CREDENTIALS_PATH`:**  Instead of hardcoding paths, these variables now store the paths for the `.json` files. This is **crucial** for portability and avoiding errors.  Use `os.path.expanduser("~/.hypotez/token.json")` to make the path user-specific.  These variables also use the `Path` object for safer file handling.

* **Error Handling:** The `try...except` block now prints a more informative message, including the error content (`error.content`), which is essential for debugging API issues.

* **`print` formatting:** Improved the `print` statement to use an f-string for better readability, which is now clearer and avoids concatenating strings manually.

* **`credentials.json` path:** Made the variable `CREDENTIALS_PATH` explicit in the code.  **This is crucial.**  You must replace `~/.hypotez/credentials.json` with the actual path to your `credentials.json` file.

* **Robust Error Handling:** The error handling is more robust, specifically printing out the error details to help pinpoint the reason for failure.


**Before running this code:**

1. **Replace placeholders:**  Update `TOKEN_PATH` and `CREDENTIALS_PATH` with the correct paths to your `token.json` and `credentials.json` files, respectively.  Ensure these files exist.


2. **Install necessary packages:** If you don't already have them, install the required libraries:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

3. **Enable the Apps Script API:**  Go to the Google Cloud Console, enable the Apps Script API. (This step is not reflected in the code)



With these improvements, the script should be significantly more reliable and easier to maintain. Remember to replace the placeholder paths with the correct ones. Always check your console for any errors.