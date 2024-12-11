rst
How to Use Google Sheets API v4 to Create and Modify Spreadsheets
=========================================================================

Description
-------------------------
This document provides a step-by-step guide on how to create, modify, and populate Google Sheets using the Google Sheets API v4.  It explains how to manage spreadsheet access, set column widths, populate cells with data, and handle formatting options.  It also includes examples using a custom wrapper class.

Execution steps
-------------------------
1. **Project Setup:**
   - Navigate to the Google Cloud Console.
   - Create a new project or select an existing one.
   - Enable the Google Drive API and the Google Sheets API for your project.
   - Create credentials for your service account, downloading the JSON key file.  This key file will be required for authorization.  It should be saved to a location and named as `CREDENTIALS_FILE`.

2. **Install Necessary Libraries:**
   - Use pip to install the `google-api-python-client`:
     ```bash
     pip install --upgrade google-api-python-client
     ```
     This will install the required `google-api-python-client` library along with its dependencies, like `oauth2client`.

3. **Authorization:**
   - Import necessary modules:
     ```python
     import httplib2
     import apiclient.discovery
     from oauth2client.service_account import ServiceAccountCredentials
     ```
   - Create service account credentials using the JSON key file:
     ```python
     CREDENTIALS_FILE = 'your_credentials_file.json'
     credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
     httpAuth = credentials.authorize(httplib2.Http())
     service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
     ```
   - Replace `'your_credentials_file.json'` with the actual path to your JSON key file.  Note that you need drive and spreadsheet scopes.

4. **Create a Spreadsheet:**
   - Use the `spreadsheets.create` method to initiate a new spreadsheet with custom settings (title, locale, sheet properties).
     ```python
     spreadsheet = service.spreadsheets().create(body={
         'properties': {'title': 'My Spreadsheet', 'locale': 'en_US'},
         'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': 'Sheet1', 'gridProperties': {'rowCount': 10, 'columnCount': 5}}}]
     }).execute()

     spreadsheet_id = spreadsheet.get('spreadsheetId')  # Retrieve the ID.
     ```

5. **Share the Spreadsheet (Crucial):**
   - The service account needs explicit access to the newly created spreadsheet.  Use the Drive API:
     ```python
     driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)
     shareRes = driveService.permissions().create(
         fileId=spreadsheet_id,
         body={'type': 'anyone', 'role': 'writer'},  # Adjust role as needed
         fields='id'
     ).execute()
     ```

6. **Set Column Widths:**
   - Use `spreadsheets.batchUpdate` to update dimensions in a single request:
     ```python
     # ... (Spreadsheet class initialization and prepare_setColumnWidth methods as shown in the code) ...

     spreadsheet_obj.prepare_setColumnWidth(0, 150)  # Set width of column A to 150 pixels.
     spreadsheet_obj.runPrepared()
     ```
7. **Populate Cells with Data:**
   - Populate cells using the `spreadsheets.values.batchUpdate` method within the `Spreadsheet` class.

   ```python
   spreadsheet_obj.prepare_setValues("A1:B2", [["Hello", "World"], ["This", "That"]])
   spreadsheet_obj.runPrepared()
   ```

8. **Formatting (e.g., merging, borders, fonts):**
   - Utilize the API's formatting methods (`mergeCells`, `repeatCell`, etc.) within the `Spreadsheet` class. Refer to the linked Google Sheets API documentation for details.

9. **Handling Errors:**
   - Wrap API calls in `try...except` blocks to catch potential errors and handle them gracefully.

**Usage Example (IlluStartive Spreadsheet class):**
```python
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

class Spreadsheet:
    def __init__(self, credentials_file, spreadsheet_id):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build('sheets', 'v4', http=self.httpAuth)
        self.spreadsheetId = spreadsheet_id
        self.sheetId = 0  #  Set your sheet ID.
        self.requests = []
        self.valueRanges = []  # For cells data.
        self.sheetTitle = "Sheet1"  # Set the sheet name.

    def prepare_setColumnWidth(self, col, width):
        # ... (Implementation similar to the example in the original code) ...

    def prepare_setValues(self, cellsRange, values, majorDimension="ROWS"):
      # ... (Implementation similar to the example in the original code) ...


    def runPrepared(self, valueInputOption="USER_ENTERED"):
        # ... (Implementation similar to the example in the original code) ...
```

Remember to replace placeholders with your actual values.  For a more robust solution, adapt the `Spreadsheet` class with comprehensive methods for various formatting and data manipulation tasks. This example should greatly improve readability and usability.


```