rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code retrieves data from a Google Sheet using the Google Sheets API.  It authenticates the application, fetches specific data from a designated spreadsheet, and then prints the retrieved data in a formatted way.  Crucially, it handles potential authentication issues and errors gracefully.


Execution steps
-------------------------
1. **Import necessary libraries:** The code imports libraries for interacting with Google Sheets (e.g., `googleapiclient`), handling credentials (`google.oauth2.credentials`), and interacting with the operating system (`os.path`).

2. **Define constants:** It defines variables like `SCOPES` (the authorized access required), `SAMPLE_SPREADSHEET_ID` (the ID of the spreadsheet), and `SAMPLE_RANGE_NAME` (the range of data to extract from the spreadsheet).  Also defines the path for the client secret file.

3. **Authenticate with Google Sheets:** The code attempts to load credentials from a `token.json` file.
   - If the `token.json` file exists, it loads the credentials from it.
   - If `token.json` doesn't exist or the credentials are invalid, it prompts the user to authorize the application by redirecting to a browser. It obtains the necessary credentials, and saves them to `token.json` for future use.

4. **Build the API service:** It uses the acquired credentials to build a Google Sheets API service object.

5. **Fetch data from the spreadsheet:**  It makes a request to the Google Sheets API to retrieve the specified data from the sheet.

6. **Handle potential errors:** The code includes a `try...except` block to catch and report `HttpError` exceptions that might occur during the API call.

7. **Validate and process data:** The `if not values:` check ensures that the retrieved data isn't empty, preventing an error if there's no data in the specified range.  It then extracts and prints the specified columns (Name and Major in this example).


Usage example
-------------------------
.. code-block:: python

    # This example assumes the necessary libraries are installed.
    # Install required libraries using pip:
    # pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

    # Replace 'YOUR_CLIENT_SECRET_FILE.json' with the actual path to your credentials file
    # and 'YOUR_SPREADSHEET_ID', 'YOUR_RANGE_NAME' with the correct values from your Google Sheet.

    import os.path
    from pathlib import Path
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

    # ... (Your constants and function definitions from the original code) ...

    if __name__ == '__main__':
        main()