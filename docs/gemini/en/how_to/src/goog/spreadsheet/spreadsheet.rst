rst
How to use the `SpreadSheet` class for uploading data to Google Sheets
====================================================================

Description
-------------------------
This code defines a `SpreadSheet` class for interacting with Google Sheets. It handles tasks such as creating new spreadsheets, uploading data from CSV files, and managing worksheets.  The class utilizes the `gspread` library and `oauth2client` to authenticate and access the Google Sheets API.  Critically, it includes error handling and logging for robustness.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports `gspread`, `pandas`, `pathlib`, `ServiceAccountCredentials` and custom modules (`logger`, `gs`, `printer`). This ensures the required libraries are available for use.

2. **Set up credentials:** The `_create_credentials` method retrieves the service account credentials from a JSON file. This step is crucial for authenticating with the Google Sheets API. The file path (`gs.path.secrets / 'e-cat-346312-137284f4419e.json'`) must be updated with the actual path to your credentials file.

3. **Authorize the client:** The `_authorize_client` method uses the retrieved credentials to create and authorize a gspread client.

4. **Open or create the spreadsheet:** The `__init__` method either opens an existing spreadsheet using the provided `spreadsheet_id` or creates a new one if `spreadsheet_id` is `None`. This step handles situations where a spreadsheet already exists or needs to be created. If the spreadsheet doesn't exist with the provided ID, an error is raised.

5. **Upload data to the sheet:** The `upload_data_to_sheet` method:
   - Checks for the existence of the data file. If the file is not found or the path is invalid, a `ValueError` is raised.
   - Reads the data from the CSV file using `pandas`.
   - Formats the data appropriately for Google Sheets (including header row).
   - Writes the data to the specified sheet (`self.worksheet`).

6. **Handle potential errors:** The code includes `try...except` blocks around crucial operations (e.g., reading the data file, creating the spreadsheet, authorizing the client, updating the spreadsheet). This prevents the script from crashing due to unexpected errors, providing robust error handling.


Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.goog.spreadsheet.spreadsheet import SpreadSheet

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Replace with actual data file
    sheet_name = 'Sheet1'  # Replace with actual sheet name

    # Create a new Spreadsheet if spreadsheet_id is not specified
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'
    )
    try:
        google_sheet_handler.upload_data_to_sheet()
        print("Data uploaded successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")