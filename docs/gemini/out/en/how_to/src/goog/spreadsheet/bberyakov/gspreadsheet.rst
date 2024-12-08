rst
How to use the GSpreadsheet class
========================================================================================

Description
-------------------------
This code defines a `GSpreadsheet` class for interacting with Google Sheets.  It utilizes the `gspread` library to manage spreadsheets, allowing functions like opening spreadsheets by ID or title, creating new spreadsheets, and retrieving a dictionary of all spreadsheets.  The class inherits from a `Spreadsheet` class (defined elsewhere), and is designed to work with service accounts for authentication.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports `gspread`, `json`, and `typing` for interacting with Google Sheets, handling JSON data, and type hinting, respectively.  It also imports the `Spreadsheet` and `service_account` classes from a file named `global_settingspread.py`.

2. **Define the `GSpreadsheet` class:** This class encapsulates methods for interacting with Google Sheets.
   - `__init__(self, s_id=None, s_title=None, *args, **kwards)`: Initializes the `GSpreadsheet` object. It loads a service account from a JSON file ('goog\\onela-hypotez-1aafa5e5d1b5.json'). If `s_id` is provided, it opens the spreadsheet with that ID. If `s_title` is provided, it attempts to open the spreadsheet with that title.  If the spreadsheet doesn't exist, it will create the spreadsheet.
   - `get_project_spreadsheets_dict(self)`: Returns a dictionary loaded from 'goog\\spreadsheets.json'.  (Likely used to get a list of spreadsheet metadata).
   - `get_by_title(self, sh_title='New Spreadsheet')`: Checks if a spreadsheet with the given title exists. If not, it creates a new one with the specified title and shares it with a specific email address ('d07708766@gmail.com') with write access. If the spreadsheet already exists, it opens the existing spreadsheet and prints a message.
   - `get_by_id(self, sh_id)`: Opens a spreadsheet by its ID and returns the spreadsheet object.
   - `get_all_spreadsheets_for_current_account(self)`: Returns a list of all spreadsheets for the current account.

3. **Authentication:** The crucial part is the service account setup (`service_account`) in the constructor.  This avoids needing user logins, making the code more robust for automated tasks.

4. **Error Handling:** The code includes checks to see if a spreadsheet already exists before creating a new one.  It also uses `json.loads()` to ensure the spreadsheet configuration files load properly.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet

    # Create a GSpreadsheet object, opening a spreadsheet by ID.
    spreadsheet = GSpreadsheet(s_id='1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')

    # Access a list of all spreadsheets for the account
    all_spreadsheets = spreadsheet.get_all_spreadsheets_for_current_account()

    # Open a spreadsheet by title
    spreadsheet.get_by_title('My Spreadsheet Title')


    # ... (further operations with the spreadsheet object, such as accessing worksheets, updating data, etc.) ...


    #To get a list of spreadsheets
    spreadsheets_dict = spreadsheet.get_project_spreadsheets_dict()
    print(spreadsheets_dict)