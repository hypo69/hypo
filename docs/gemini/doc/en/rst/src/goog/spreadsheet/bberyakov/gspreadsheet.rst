Module gspreadsheet
==================

.. module:: hypotez.src.goog.spreadsheet.bberyakov.gspreadsheet
    :platform: Windows, Unix
    :synopsis: This module provides a class for interacting with Google Sheets.

Description
----------

This module defines the `GSpreadsheet` class, which facilitates interactions with Google Sheets using the gspread library.  It inherits from the `Spreadsheet` class.  It includes methods for retrieving spreadsheets by ID or title, creating spreadsheets, and accessing all spreadsheets within a user's account.


Classes
-------

.. autoclass:: GSpreadsheet
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: GSpreadsheet.__init__
.. autofunction:: GSpreadsheet.get_project_spreadsheets_dict
.. autofunction:: GSpreadsheet.get_by_title
.. autofunction:: GSpreadsheet.get_by_id
.. autofunction:: GSpreadsheet.get_all_spreadsheets_for_current_account