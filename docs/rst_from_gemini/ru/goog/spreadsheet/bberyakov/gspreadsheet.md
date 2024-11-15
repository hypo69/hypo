```python
# -*- coding: utf-8 -*-
 # <- venv win
""" module: src.goog.spreadsheet.bberyakov """
"""  Module for interacting with Google Sheets. """
""" \package beeryakov.goog """
""" \file gspreadsheet.py """
 
"""
@section libs imports:
  - gspread
  - json
  - typing
"""
from global_settingspread import Spreadsheet, service_account
import gspread
import json
from typing import List, Type, Union


class GSpreadsheet(Spreadsheet):
    """
    Class for interacting with Google Sheets.  Inherits from Spreadsheet.

    Implements methods to create, open, and manage Google Sheets.
    """
    gsh: gspread.Spreadsheet = None  # Store the opened spreadsheet object
    
    def __init__(self, s_id: str = None, s_title: str = None, *args, **kwards):
        """
        Initializes a GSpreadsheet object.  Loads service account credentials.

        Parameters:
            s_id:  Spreadsheet ID (optional).
            s_title: Spreadsheet title (optional).
            *args:  Additional positional arguments (not used).
            **kwards: Additional keyword arguments (not used).
        """
        secret_file = 'goog/onela-hypotez-1aafa5e5d1b5.json'  # Use a more robust path
        self.gc = service_account(filename=secret_file)
        
        if s_id:
            try:
                self.gsh = self.gc.open_by_key(s_id)
            except gspread.exceptions.SpreadsheetNotFound:
                print(f"Spreadsheet with ID {s_id} not found.")
                self.gsh = None  # Important: Indicate failure
        elif s_title:
            try:
                self.gsh = self.gc.open_by_title(s_title)
            except gspread.exceptions.SpreadsheetNotFound:
                print(f"Spreadsheet with title {s_title} not found.")
                self.gsh = None

        #Important: Check for successful initialization
        if self.gsh is None:
            raise Exception("Failed to open spreadsheet.")


    def get_project_spreadsheets_dict(self) -> dict:
        """
        Loads spreadsheet metadata from a JSON file.  
        This method is not robust and likely needs updating.

        Returns:
            dict: Dictionary containing spreadsheet metadata.
        """
        try:
            with open('goog/spreadsheets.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: spreadsheets.json not found.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}



    def get_by_title(self, sh_title: str = 'New Spreadsheet') -> gspread.Spreadsheet:
        """Creates or opens a Google Sheet by title. Handles existing sheets."""
        try:
            spreadsheet = self.gc.open_by_title(sh_title)
            print(f'Spreadsheet {sh_title} already exists.')
            return spreadsheet
        except gspread.exceptions.SpreadsheetNotFound:
            spreadsheet = self.gc.create(sh_title)
            spreadsheet.share('d07708766@gmail.com', perm_type='user', role='writer')  # Share with specified user
            print(f'Spreadsheet {sh_title} created.')
            return spreadsheet


    def get_by_id(self, sh_id: str) -> gspread.Spreadsheet:
        """Opens a Google Sheet by ID. Handles errors more robustly."""
        try:
            return self.gc.open_by_key(sh_id)
        except gspread.exceptions.SpreadsheetNotFound:
            print(f"Spreadsheet with ID {sh_id} not found.")
            return None  # Indicate failure



    def get_all_spreadsheets_for_current_account(self) -> List[gspread.Spreadsheet]:
        """Opens all spreadsheets for the current account.
           Returns a list of spreadsheets objects or None on failure."""
        try:
            return self.gc.openall()
        except Exception as e:
            print(f"Error opening spreadsheets: {e}")
            return None

```

**Explanation of Improvements and Key Changes:**

* **Error Handling:**  The code now includes `try...except` blocks to handle potential `SpreadsheetNotFound` exceptions from gspread.  Crucially, it returns `None` or prints an error message when a spreadsheet isn't found, preventing the program from crashing. This is vital for production code.
* **`__init__` Robustness:** The `__init__` method now verifies that a spreadsheet was successfully opened. If not, it raises an exception, signaling an error to the calling code instead of silently failing.
* **Clearer Variable Names:**  `gclient` was changed to `gc` for brevity and consistency.  `gsh` was kept for better readability.
* **File Path Fix:** The `secret_file` path is now `'goog/onela-hypotez-1aafa5e5d1b5.json'`. This assumes the JSON file is in a subdirectory called `goog`.  **Crucially**, you should **replace this with the actual path** to your service account credentials file.
* **JSON Loading:** The `get_project_spreadsheets_dict` method now includes basic error handling for file not found and incorrect JSON.
* **Type Hinting:**  More explicit type hinting for clarity and to help with static analysis.
* **`get_by_title` Improvement:** Now returns the spreadsheet object instead of None, which makes the method more useful. It also prints a message whether the spreadsheet exists or not.
* **`get_by_id` Improvement:** Handles errors from `open_by_key` and returns `None` if the sheet isn't found.
* **`get_all_spreadsheets_for_current_account`:** Improved error handling and returns `None` if there's a problem opening the spreadsheets.


**How to Use (Example):**

```python
from gspreadsheet import GSpreadsheet

try:
    spreadsheet_obj = GSpreadsheet(s_title='MySpreadsheet')  # Use title or ID
    # ... do something with the spreadsheet_obj ...
    all_sheets = spreadsheet_obj.get_all_spreadsheets_for_current_account()
    if all_sheets:
        for sheet in all_sheets:
            print(sheet.title)
except Exception as e:
    print(f"An error occurred: {e}")
```


**Before running:**

1. **Install necessary libraries:**
   ```bash
   pip install gspread google-auth-httplib2 google-auth-oauthlib
   ```

2. **Install `pyOpenSSL`:** (If needed)
   ```bash
   pip install pyOpenSSL
   ```

3. **Configure the service account:**
   - Download the JSON key file from Google Cloud Console (credentials) and place it in the appropriate location (likely a `goog` subdirectory).


This improved code is more robust, handles errors better, and is more suitable for production use. Remember to replace placeholder values with your actual data. Remember to handle the `None` return values appropriately in your code.