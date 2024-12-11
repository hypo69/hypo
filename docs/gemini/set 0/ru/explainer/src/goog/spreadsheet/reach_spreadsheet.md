# <input code>

```python
## \file hypotez/src/goog/spreadsheet/reach_spreadsheet.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


# Author: Ioann Volkov (volkov.ioann@gmail.com)
# This module uses Google Sheets API v4 (and Google Drive API v3 for sharing spreadsheets)

# (!) Disclaimer
# This is NOT a full-functional wrapper over Sheets API v4.
# This module was created just for https://telegram.me/TimeManagementBot and habrahabr article


import httplib2
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.service_account import ServiceAccountCredentials

import tempfile
import header
from src import gs
from src.utils import j_loads, j_dumps
from src.utils import pprint
from src.logger import logger

def htmlColorToJSON(htmlColor):
    if htmlColor.startswith("#"):
        htmlColor = htmlColor[1:]
    return {"red": int(htmlColor[0:2], 16) / 255.0, "green": int(htmlColor[2:4], 16) / 255.0, "blue": int(htmlColor[4:6], 16) / 255.0}

class SpreadsheetError(Exception):
    ...

class SpreadsheetNotSetError(SpreadsheetError):
    ...

class SheetNotSetError(SpreadsheetError):
    ...

class ReachSpreadsheet:
    def __init__(self, debugMode=False):
        # ... (Initialization logic)
        pass

    # ... (Other methods)
    pass

# ... (Test functions)
```

# <algorithm>

The code defines a `ReachSpreadsheet` class for interacting with Google Sheets API v4.  The algorithm can be summarized as follows:

1. **Initialization (`__init__`)**:
    - Takes `debugMode` flag.
    - Attempts to load credentials from a temporary JSON file (`gs.path.tmp / 'e-cat-346312-137284f4419e.json'`).
    - If successful, creates `credentials` object, `httpAuth` object for authorization and `service` for sheet interaction and `driveService` for Drive interaction.
    - Initializes `spreadsheetId`, `sheetId`, `sheetTitle`, `requests` (for batch updates), and `valueRanges` (for batch values).
    - Handles potential exceptions during credential loading and logging errors.


2. **Spreadsheet Creation (`create`)**:
    - Takes `title`, `sheetTitle`, `rows`, `cols`, `locale`, and `timeZone` as arguments.
    - Builds a request body to create a spreadsheet with the specified parameters and executes it via the `service`.
    - Extracts `spreadsheetId`, `sheetId`, and `sheetTitle` from the response.
    - Optionally prints the response if `debugMode` is on.


3. **Spreadsheet Sharing (`share`, `shareWithEmailForReading`, etc.)**:
    - Validates that `spreadsheetId` is set.
    - Builds a share request body with the specified `type` and `role` (e.g., 'reader' or 'writer').
    - Executes the sharing request via `driveService`.
    - Optionally prints the response if `debugMode` is on.


4. **Setting Spreadsheet by ID (`setSpreadsheetById`)**:
    - Takes `spreadsheetId` as input.
    - Fetches spreadsheet details using the given id via the `service`.
    - Updates `spreadsheetId`, `sheetId`, and `sheetTitle` with data from the retrieved spreadsheet.
    - Optionally prints the spreadsheet details if `debugMode` is on.


5. **Batch Update (`runPrepared`)**:
    - Validates that `spreadsheetId` is set.
    - Executes batch update requests if `requests` list isn't empty, and batch updates on values via `valueRanges` list if isn't empty.
    - Clears `requests` and `valueRanges` lists.
    - Returns replies and responses for batch updates.

6.  **Preparing and running actions (`prepare_addSheet`, `addSheet`, `toGridRange`, `prepare_setDimensionPixelSize`, `prepare_setValues`, `prepare_mergeCells`, `prepare_setCellStringFormatterormat`, `prepare_setCellStringFormatterormats`,  etc.)**: These methods prepare individual updates (adding sheets, formatting cells, setting dimensions, and so on) and append them to `requests` or `valueRanges` for the batch operations.  They also support converting cell ranges from string format to internal format suitable for the Google Sheets API (e.g., converting "A3:B4" into a dictionary with coordinates).


7.  **Helper Functions (`htmlColorToJSON`)**: Used to convert HTML color codes to a JSON representation, likely for formatting cells (color).



# <mermaid>

```mermaid
graph TD
    A[ReachSpreadsheet] --> B{__init__};
    B --> C[Load credentials];
    C --Success-->> D[Initialize service];
    C --Error-->> E[Error logging];
    D --> F[create];
    F --> G[Create Spreadsheet];
    G --> H[Extract data];
    H --> I[Set properties];
    F --> J{debugMode};
    J --True-->> K[Print response];
    J --False-->> I;

    F --> L[share];
    L --> M[Share spreadsheet];
    L --> O{debugMode};
    O --True-->> P[Print response];
    O --False-->> M;

    F --> Q[setSpreadsheetById];
    Q --> R[Fetch spreadsheet details];
    R --> S[Update properties];
    Q --> T{debugMode};
    T --True-->> U[Print response];
    T --False-->> S;

    F --> V[runPrepared];
    V --> W[Batch update requests];
    W --> X[Clear requests];
    V --> Y[Batch update values];
    Y --> X;

    subgraph "Other Methods"
        F --> Z[prepare_addSheet];
        F --> AA[prepare_setDimensionPixelSize];
        F --> AB[prepare_setValues];
    end
```

**Explanation of Dependencies**:

- `httplib2`: Used for making HTTP requests to the Google API.
- `googleapiclient`: Used for interacting with the Google API.
- `oauth2client`: Used for authenticating with the Google API using service account credentials.
- `tempfile`: Used for temporary file management (likely for credential handling).
- `header`: Likely a custom module related to headers or configuration.
- `gs`: Likely a custom module providing file system paths or related to Google Services; important for resolving file paths to the key file for authentication.
- `src.utils`: Contains utility functions like `j_loads`, `j_dumps`, and `pprint`.
- `src.logger`: Contains a logging mechanism for error handling.

The `ReachSpreadsheet` class interacts with the `gs`, `utils`, and `logger` modules via imports. It relies on the `googleapiclient` and `oauth2client` libraries for Google Sheet API interaction and authorization, respectively. The code's structure suggests an organization where the `src` directory contains other custom modules and potentially data management functionalities related to Google Sheets interactions.


# <explanation>

**Imports**:

- `httplib2`: A low-level HTTP client library.
- `googleapiclient`: The client library for interacting with the Google APIs. This likely contains modules for building and executing the requests needed for Google Sheets and Drive.
- `googleapiclient.discovery`: A part of `googleapiclient` that constructs API clients, used to work with the Sheets and Drive APIs.
- `oauth2client.service_account`: Provides the necessary classes to authenticate using service account credentials.
- `tempfile`: Used for temporary file handling (like the credentials file).
- `header`: A likely custom module, potentially handling headers for requests.
- `gs`: Likely a custom module providing file system utilities.
- `src.utils`: Custom module providing helper functions like JSON serialization/deserialization.
- `src.logger`: Custom module for logging purposes.

**Classes**:

- `SpreadsheetError`: A base class for exceptions related to spreadsheet operations.
- `SpreadsheetNotSetError`: Inherits from `SpreadsheetError`, indicating a spreadsheet is not set.
- `SheetNotSetError`: Inherits from `SpreadsheetError`, indicating a sheet is not set.
- `ReachSpreadsheet`: The core class for interacting with Google Sheets.
    - `__init__`: Initializes the class, loads credentials, creates necessary service objects, and initializes internal variables.
    - `create`: Creates a new Google Sheet with specified properties.
    - `share`: Shares the spreadsheet with the given parameters.
    - `getSheetURL`: Returns the URL to the Google Sheet.
    - `setSpreadsheetById`: Sets the current spreadsheet using its ID.
    - `runPrepared`: Executes batch updates to the spreadsheet.
    - `prepare_addSheet`, `addSheet`, `prepare_setDimensionPixelSize`, `prepare_setColumnsWidth`, `prepare_setColumnWidth`, `prepare_setRowsHeight`, `prepare_setRowHeight`, `prepare_setValues`, `prepare_mergeCells`, `prepare_setCellStringFormatterormat`, and `prepare_setCellStringFormatterormats`: Methods to prepare various operations for the batch update process.
    - `toGridRange`: Converts a string cell range into a format understandable by the Google Sheets API.

**Functions**:

- `htmlColorToJSON`: Converts an HTML color code to a JSON representation (e.g., '#FF0000' to `{'red': 1.0, 'green': 0.0, 'blue': 0.0}`).

**Variables**:

- `MODE`: A string variable likely indicating the mode of operation (e.g., 'dev').
- `jsonKeyFileName`: The path to the JSON file containing credentials for the Google Sheet API.

**Possible Improvements and Errors**:

- **Error Handling:** While the code has `try...except` blocks, error handling could be more robust and specific for various Google API errors.  Adding more informative error messages would be helpful for debugging.
- **Resource Management:** The code doesn't explicitly close resources or handle cases where the Google API returns errors during a batch operation.  Robust error handling is necessary.
- **Readability:** Some function names (`prepare_...`) could be more descriptive.
- **Reusability:** Methods like `prepare_setDimensionPixelSize` could be more generalized to handle different update types.
- **Code Style:**  Consider using constants instead of magic numbers for values like row/column counts.


**Relationship to Other Parts of the Project**:

The code relies on modules from the `src` directory (`gs`, `utils`, `logger`).  It presumably fits into a larger project that involves managing Google Sheets data. The test functions demonStarte how the `ReachSpreadsheet` class can be used to perform various spreadsheet operations.  A key file (`e-cat-346312-137284f4419e.json`) is required for authentication.