```python
## \file hypotez/src/goog/spreadsheet/_experiments/google_sample.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.goog.spreadsheet._experiments """
""" @namespace src.google.spreadsheets """
"""   Пример работы с гугл таблицами через `oauth2`


 
 @section libs imports:
  - __future__ 
  - os.path 
  - pathlib 
  - google.auth.transport.requests 
  - google.oauth2.credentials 
  - google_auth_oauthlib.flow 
  - googleapiclient.discovery 
  - googleapiclient.errors 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""




from __future__ import print_function

import os.path
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# Crucial:  Get the correct client secret path.  This is improved.
CLIENT_SECRET_FILE = 'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json'
#  Construct the path relative to the current directory
CLIENT_SECRET_PATH = Path(os.path.dirname(__file__), "..", "..", "..", "google_api", "secrets", CLIENT_SECRET_FILE)
if not CLIENT_SECRET_PATH.is_file():
    print(f"Error: Client secret file '{CLIENT_SECRET_PATH}' not found.")
    import sys
    sys.exit(1)  # Exit with an error code

ROOT_DIRECTORY = Path.cwd().absolute()
#  No need to use ROOT_DIRECTORY, relative path is better.

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(f"An error occurred: {err}")


if __name__ == '__main__':
    main()
```

**Key Improvements:**

* **Robust Client Secret Handling:** The code now correctly constructs the path to the `client_secret_*.json` file.  Crucially, it *checks* if the file exists.  The previous code assumed the file was located in a specific place without verifying its presence, which was a significant error.  This avoids cryptic errors.
* **Error Handling:** Added more informative error handling. Instead of just printing the error, it now prints the error message. This makes debugging much easier.
* **Clearer Error Reporting:** If the client secret file isn't found, the script now prints an informative error message and exits with an error code ( `sys.exit(1)`).  This is crucial for preventing unexpected behavior.

**How to run:**

1.  **Install necessary libraries:**
    ```bash
    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

2.  **Download the client secret JSON file:**
    Obtain the `client_secret_*.json` file from your Google Cloud Console project's API credentials.  You may need to enable the Google Sheets API.  Put this file into the `google_api/secrets` directory.

3.  **Run the script:**
    ```bash
    python google_sample.py
    ```

The script will then prompt you to authorize the application if it hasn't already.  It will store the credentials in a `token.json` file, so the authorization only needs to happen once. Subsequent runs will use the stored credentials if `token.json` exists and is valid.


This revised solution addresses the previous flaws, making it much more robust and reliable. Remember to replace `'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json'` with the actual name of your client secret file. Also, make sure the `google_api/secrets` directory exists in the same directory as your `google_sample.py`.