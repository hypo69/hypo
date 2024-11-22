```rst
gspreadsheet.py
=============

.. module:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet
    :platform: Windows, Unix
    :synopsis: This module provides a class for interacting with Google Sheets.

Description
----------

This module defines the `GSpreadsheet` class, which extends the `Spreadsheet` class from `global_settingspread` to interact with Google Sheets using the gspread library. It handles tasks such as opening spreadsheets by ID or title, creating new spreadsheets, and retrieving a list of all spreadsheets.  It uses service accounts for authentication.


Functions
---------

.. autofunction:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.GSpreadsheet.__init__
.. autofunction:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.GSpreadsheet.get_project_spreadsheets_dict
.. autofunction:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.GSpreadsheet.get_by_title
.. autofunction:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.GSpreadsheet.get_by_id
.. autofunction:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.GSpreadsheet.get_all_spreadsheets_for_current_account


Classes
-------

.. autoclass:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet.GSpreadsheet
    :members:
    :undoc-members:
    :show-inheritance:

```
