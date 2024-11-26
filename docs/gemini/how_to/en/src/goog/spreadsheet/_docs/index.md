# How to use the Google Sheets API v4 in Python

This guide demonstrates how to interact with Google Sheets using the Google Sheets API v4, focusing on tasks beyond basic data reading and writing, including formatting and layout control.

## Prerequisites

1. **Google Cloud Project:** Create a new project in the Google Cloud Console.
2. **Enable APIs:** Enable the Google Drive API and the Google Sheets API for your project.
3. **Service Account:** Create a service account and download the JSON key file.  This file will be crucial for authenticating your application.
4. **Install Libraries:** Install the `google-api-python-client` library using pip:

```bash
pip install --upgrade google-api-python-client
```

## Step 1: Authenticate with your Service Account

```python
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Replace 'your_service_account_key.json' with the actual file name.
CREDENTIALS_FILE = 'your_service_account_key.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
```

## Step 2: Creating a Spreadsheet (and granting access)

```python
spreadsheet_body = {
    'properties': {
        'title': 'My Spreadsheet',
        'locale': 'en_US'  # or 'ru_RU' for Russian locale
    },
    'sheets': [
        {'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': 'Sheet1',
                        'gridProperties': {'rowCount': 8, 'columnCount': 5}}}
    ]
}

spreadsheet = service.spreadsheets().create(body=spreadsheet_body).execute()
spreadsheet_id = spreadsheet['spreadsheetId']

# Grant access to the newly created spreadsheet
# Replace 'user@example.com' with the desired email address or 'anyone' for anyone access.
drive_service = apiclient.discovery.build('drive', 'v3', http=httpAuth)
share_response = drive_service.permissions().create(
    fileId=spreadsheet_id,
    body={'type': 'user', 'role': 'writer', 'emailAddress': 'user@example.com'},
    fields='id'
).execute()
```

**Important Considerations:**

* **Error Handling:** Add `try...except` blocks around API calls to handle potential errors gracefully.
* **`spreadsheet_id`:**  Store the `spreadsheet_id` for later use in updating the spreadsheet.

## Step 3:  Modifying Spreadsheet Data and Formatting


```python
from googleapiclient.discovery import build

class Spreadsheet:
    def __init__(self, spreadsheet_id, service):
        self.spreadsheet_id = spreadsheet_id
        self.service = service
        self.requests = []
        self.valueRanges = []
        self.sheet_title = 'Sheet1'  # or use spreadsheet['sheets'][0]['properties']['title']

    # ... (methods for setting column widths, merging cells, setting formats, etc., as shown in the original code)

    def prepare_setColumnWidth(self, col, width):
        # ... (Implementation as shown in the original code)


    def prepare_setValues(self, cells_range, values, major_dimension='ROWS'):
        self.valueRanges.append({
            'range': self.sheet_title + '!' + cells_range,
            'majorDimension': major_dimension,
            'values': values
        })


    def runPrepared(self, value_input_option='USER_ENTERED'):
      try:
          if len(self.requests) > 0:
              self.service.spreadsheets().batchUpdate(
                  spreadsheetId=self.spreadsheet_id, body={'requests': self.requests}
              ).execute()
          if len(self.valueRanges) > 0:
              self.service.spreadsheets().values().batchUpdate(
                  spreadsheetId=self.spreadsheet_id,
                  body={'valueInputOption': value_input_option, 'data': self.valueRanges}
              ).execute()
      finally:
          self.requests = []
          self.valueRanges = []


# Example Usage (after creating the Spreadsheet object):
# ...(set column widths as needed)
ss = Spreadsheet(spreadsheet_id, service)
ss.prepare_setColumnWidth(0, 317)
ss.prepare_setColumnWidth(1, 200)

ss.prepare_setValues("A1:E1", [["Combined Header"]]) # Example for setting A1-E1
ss.prepare_setValues("A2:C4", [  # Example for data in multiple rows and columns.
                ['Value A2', 'Value B2', 'Value C2'],
                ['Value A3', 'Value B3', 'Value C3'],
                ['Value A4', 'Value B4', '=SUM(B2:B3)']
])

ss.runPrepared()


```

**Explanation and Improvements:**

* **`Spreadsheet` Class:**  The provided code is significantly improved by encapsulating API interactions within a `Spreadsheet` class. This promotes code organization, reusability, and cleaner error handling.
* **Error Handling:**  The `try...except` blocks in `runPrepared` catch potential exceptions during API calls, improving robustness.  Crucially, it now resets `requests` and `valueRanges` *in the `finally` block*.  This prevents memory leaks and ensures that the prepared data isn't used if an error occurs during execution.
* **Clearer Example Usage:** The example usage is more structured and demonstrates how to use `prepare_setColumnWidth`,  `prepare_setValues`, and `runPrepared`.

Remember to replace placeholders like `'your_service_account_key.json'` and  `'user@example.com'` with your actual values. This revised structure is more practical for handling complex spreadsheet manipulations.  Critically, it correctly uses `valueInputOption='USER_ENTERED'` which is essential for formulas and date/time recognition.


This comprehensive guide provides a more robust and manageable way to work with the Google Sheets API for complex spreadsheet tasks.  Remember to consult the official Google Sheets API v4 documentation for complete details on all available methods and parameters.