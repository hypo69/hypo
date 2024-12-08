rst
How to use the ReachSpreadsheet class
========================================================================================

Description
-------------------------
This code defines a `ReachSpreadsheet` class for interacting with Google Sheets using the Google Sheets API v4.  It handles tasks like creating spreadsheets, adding sheets, setting column/row widths, formatting cells, sharing spreadsheets, and updating data.  The class uses service account credentials for authentication, providing a structured way to interact with Google Sheets from Python code. It includes error handling for potential issues like missing credentials or invalid spreadsheet IDs.  The class also contains methods for preparing and executing batch updates to improve efficiency.


Execution steps
-------------------------
1. **Import necessary libraries:** The code imports libraries like `httplib2`, `googleapiclient`, `oauth2client`, `tempfile`, custom modules (`gs`, `jjson`, `printer`, `logger`), and potentially others, for handling HTTP requests, Google API interaction, file management, data processing, and logging.

2. **Define the `ReachSpreadsheet` class:**  The `ReachSpreadsheet` class initializes with an optional `debugMode` flag. This flag, if set, enables additional print statements for debugging.

3. **Load credentials:**  The class attempts to load credentials (`self.credentials`) from a JSON key file (`e-cat-346312-137284f4419e.json`).  This file is likely stored in a temporary directory and contains the service account credentials for interacting with Google Sheets.  Error handling (`try...except`) is included to manage potential issues during credential loading.

4. **Authorize and build the Google API service:** The loaded credentials are used to authorize an HTTP object (`self.httpAuth`).  This HTTP object is then used to build the Google Sheets API service (`self.service`).   This step establishes the connection to Google Sheets.  Similarly, a Google Drive service (`self.driveService`) is initialized for sharing functionality.

5. **Initialize spreadsheet and sheet properties:**  Variables (`self.spreadsheetId`, `self.sheetId`, `self.sheetTitle`, `self.requests`, `self.valueRanges`) are initialized to `None`. These variables store crucial information about the currently active spreadsheet and sheet for subsequent operations.

6. **`create()` method:** This method creates a new spreadsheet with a given title and a sheet within it. The method takes parameters like `title`, `sheetTitle`, rows, cols, locale, and timeZone to customize the spreadsheet.  It returns the `spreadsheetId`, `sheetId`, and `sheetTitle`.

7. **`share()` method:**  This method handles sharing the spreadsheet with specific users or roles (e.g., readers, writers). It takes a `shareRequestBody` dictionary to define the sharing parameters.

8. **`share...()` methods:** These methods (e.g., `shareWithEmailForReading`, `shareWithAnybodyForWriting`) provide specific sharing options.

9. **`getSheetURL()` method:** This retrieves the URL for the spreadsheet in Google Sheets.

10. **`setSpreadsheetById()` method:** This method sets the current spreadsheet based on its ID.

11. **`runPrepared()` method:** This method executes batch updates to the spreadsheet. It processes any previously prepared update requests (`self.requests`) and values (`self.valueRanges`) stored in the class.  This function handles both spreadsheet updates and data input operations.  It's crucial for efficiency.

12. **`prepare_addSheet()` method:**  This method prepares a request to add a new sheet to the spreadsheet. It's important for preparing and storing operations for batch execution.

13. **`addSheet()` method:** This method adds a new sheet with specified parameters and returns the newly added sheet's ID.

14. **`toGridRange()` method:** Converts a string cell range specification (e.g., "A1:B2") to a structured dictionary. This is helpful for specifying update ranges within the spreadsheet.

15. **`prepare_setDimensionPixelSize()`/`prepare_*Width`/`prepare_*Height` methods:** These methods prepare requests for adjusting column and row widths and heights.

16. **`prepare_setValues()` method:** Prepares data to be written into the spreadsheet. Takes a cell range, values, and the dimension. This method is used for large-scale data insertion.

17. **`prepare_mergeCells()` method:**  Prepares a merge cell request.

18. **`prepare_setCellStringFormatterormat`/`prepare_setCellStringFormatterormats` methods:** Prepare formatting requests for cells or ranges within a spreadsheet.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet.reach_spreadsheet import ReachSpreadsheet

    # Replace with your actual credentials file path
    ss = ReachSpreadsheet(debugMode=True)
    ss.create("My Spreadsheet", "Sheet 1", rows=10, cols=5)
    ss.shareWithEmailForWriting("user@example.com")
    values = [
        ["Header 1", "Header 2"],
        ["Value 1", "Value 2"],
        ["Value 3", "Value 4"],
    ]

    ss.prepare_setValues("A1:B3", values)
    ss.runPrepared()

    print("Spreadsheet created and data added successfully. URL:", ss.getSheetURL())