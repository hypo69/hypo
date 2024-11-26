## File: hypotez/src/goog/spreadsheet/bberyakov/gworksheets.py

# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet.bberyakov 
	:platform: Windows, Unix
	:synopsis:
"""
MODE = 'dev'


from global_settingspread import Spreadsheet, Worksheet
#from goog.gspreadsheet import GSpreadsheet
from goog.grender import GSRender
#from global_settings import GSpreadsheet, GSRender

from typing import Union


class GWorksheet(Worksheet):
    """
     [Class's description]

    ## Inheritances : 
        - Implements Worksheet : [description]
    """
    sh = None
    ws: Worksheet = None
    render: GSRender = GSRender()

    def __init__(self, sh, ws_title: str = 'new', rows = None, cols = None, direcion = 'rtl', wipe_if_exist: bool = True, *args, **kwards) -> None:
        """
         [Function's description]

        Parameters : 
             self : [description]
             sh : [description]
             ws_title : str = 'new' : [description]
             rows = None : [description]
             cols = None : [description]
             direcion = 'rtl' : [description]
             wipe_if_exist : bool = True : [description]
             *args : [description]
             **kwards : [description]
        Returns : 
             None : [description]

        """
        self.sh = sh
        self.get(self.sh, ws_title)
        # ... (rest of the init method is commented out)
    

    def get(self, sh, ws_title: str = 'new', rows: int = 100, cols: int = 100, direction: str = 'rtl', wipe_if_exist: bool = True):
        """
         [Function's description]

        Parameters : 
             self : [description]
             sh : [description]
             ws_title : str = 'new' : [description]
             rows : int = 100 : [description]
             cols : int = 100 : [description]
             direction : str = 'rtl' : [description]
             wipe_if_exist : bool = True : [description]

        """
            """
            Создаю новую таблицу в книге, если ws_title == 'new', 
            иначе открываю по ws_title 
            `ws_title` (str) - Название таблицы(worksheet) в книге(spreadsheet) 
            `rows` (int) - кол -во строк 
            `cols` (int) - кол -во колонок 
            `wipe_if_exist` (bool) - очистить от старых данных
            """

            if ws_title == 'new':
                self.ws = sh.gsh.get() #Alternative implementation
            else:
                if ws_title in [ws.title for ws in sh.gsh.worksheets()]:
                    print(f'worksheet {ws_title} already exist !')
                    self.ws = sh.gsh.worksheet(ws_title)
                    if wipe_if_exist:
                        self.ws.clear()
                else:
                    self.ws = sh.gsh.add_worksheet(ws_title, rows, cols)

            self.render.set_worksheet_direction(sh.gsh, self.ws, 'rtl')


    def header(self, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None:
        """
         [Function's description]

        Parameters : 
             self : [description]
             world_title : str : [description]
             range : Z1' = 'A1 : [description]
             merge_type : str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL' : [description]
        Returns : 
             None : [description]

        """
        self.render.header(self.ws, world_title)


    def category(self, ws_category_title):
        """
         [Function's description]

        Parameters : 
             self : [description]
             ws_category_title : [description]

        """
        self.render.write_category_title(self, ws_category_title)


    def direction(self, direction: str = 'rtl'):
        """
         [Function's description]

        Parameters : 
             self : [description]
             direction : str = 'rtl' : [description]

        """
        self.render.set_worksheet_direction(sh=self.sh, ws=self, direction='rtl')
```

```
<algorithm>
```
1. **Initialization:**
   - The code initializes a `GWorksheet` object.
   - `sh` is expected to hold a spreadsheet object.
   - `ws` is initialized to None and gets populated by the `get` method.

2. **`get` Method Execution:**
   - **Check if the worksheet exists:** It checks if the worksheet with `ws_title` already exists in the spreadsheet.
   - **Create/Open Worksheet:**
     - If `ws_title` is 'new', it creates a new worksheet using `sh.gsh.get()`.
     - Otherwise, it opens the existing worksheet with `ws_title` by using `sh.gsh.worksheet(ws_title)`. If `wipe_if_exist` is True, it clears the existing data.
   - **Set Direction:** Sets the direction of the worksheet using `self.render.set_worksheet_direction`.

3. **Other Methods:**
   - **`header`:** Sets the header for the worksheet by calling the `render` methods.
   - **`category`:** Writes the category title by calling the `render` method.
   - **`direction`:** Sets the direction for the worksheet using `render` method.


```
<example>
```
```
# Example Usage (Illustrative)
# Assuming you have a Spreadsheet object 'spreadsheet' and a GSRender object.
from global_settingspread import Spreadsheet #Import required libraries 
from goog.grender import GSRender

# Create a Spreadsheet object.  (This part is critical and missing in the example)
spreadsheet = Spreadsheet()

# Create a worksheet within the Spreadsheet
worksheet_obj = GWorksheet(spreadsheet)

# Get an existing worksheet (or create a new one)
worksheet_obj.get(spreadsheet, "MyWorksheet")

# Set header (range and merge type can be customized)
worksheet_obj.header("My Header", "A1:B1", "MERGE_ALL")

# Write a category title
worksheet_obj.category("Category Title")
```
```
<explanation>
```

**Imports:**

- `global_settingspread`: Likely contains classes for handling spreadsheets and worksheets.  The relationship is likely that this package provides the core functionality for spreadsheet interaction. The `Spreadsheet` and `Worksheet` classes allow the interaction with the underlying spreadsheet.
- `goog.grender`:  Provides rendering capabilities (e.g., formatting, writing to the worksheet). It's a dependency for rendering tasks related to the spreadsheet.
- `typing`: Provides type hints for better code readability and maintainability.


**Classes:**

- `GWorksheet`: Inherits from `Worksheet` to extend the base functionality.
   - `sh`: Spreadsheet object for context.
   - `ws`: Worksheet object (the one in use)
   - `render`: Object for formatting and rendering.
   - `__init__`: Initializes the worksheet with spreadsheet and options (like title, size, direction).
   - `get`: Creates or retrieves a worksheet (clearing existing content if needed).
   - `header`: Sets the worksheet's header.
   - `category`: Writes category titles.
   - `direction`: Sets the worksheet's direction.

**Functions:**

- `__init__`: Takes arguments to initialize the worksheet.
- `get`: Creates or opens a worksheet.  It's the core function for interacting with the spreadsheet's structure.
- `header`: Formats the header (and potentially merges cells).
- `category`: Writes category titles (potential for formatting).
- `direction`: Sets the worksheet direction.

**Variables:**

- `MODE`: Represents the operational mode ('dev' in this case).
- `sh`, `ws`, and `render` are attributes of the `GWorksheet` class, used for interacting with the spreadsheet and rendering functionalities.


**Potential Errors/Improvements:**

- **Missing Spreadsheet Object:** The code assumes a `Spreadsheet` object (`sh`) is passed. This crucial part is absent in the example.  The program needs a way to obtain a valid spreadsheet object to interact with. Error handling for invalid or unavailable spreadsheet objects should be implemented.

- **Unclear Purpose of `ws`:**  The `ws` attribute seems to be assigned twice. The code seems to assign `self.ws = sh.gsh.get()`. If the GSheet or Spreadsheet structure is correct, this might be a problem. It should only assign a worksheet when an action is performed upon the worksheet.
- **Missing `gsh`:**  The `gsh` attribute (likely representing Google Sheets handle or similar) isn't defined within the `Spreadsheet` object.  The provided code fragments refer to it as if it's a standard part of the `Spreadsheet` object.  Proper implementation of such an attribute needs to be clarified and validated.
- **`...`:** The `...` in the `__init__` method signifies incomplete or missing code.  This needs to be filled in to complete the functionality.


**Relationships with Other Parts:**

- `global_settingspread` likely provides the `Spreadsheet` and `Worksheet` classes.
- `goog.grender` provides functions for formatting/rendering elements on the worksheet.
- Further analysis is necessary to determine relationships with other parts of the project not specified in the code excerpt.