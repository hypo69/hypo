hypotez/src/goog/spreadsheet/reach_spreadsheet.py
==================================================

.. module:: hypotez.src.goog.spreadsheet.reach_spreadsheet
   :platform: Windows, Unix
   :synopsis: Module for interacting with Google Sheets using the Google Sheets API v4.

Module Description
------------------

This module provides a class, `ReachSpreadsheet`, for creating, interacting with, and managing Google Sheets via the Google Sheets API v4.  It includes methods for creating spreadsheets, adding sheets, formatting cells, sharing spreadsheets, and setting spreadsheet dimensions. It handles potential errors during API interactions.  It also includes helper functions for conversion and various testing functions.


Classes
-------

.. autoclass:: SpreadsheetError
   :members:

.. autoclass:: SpreadsheetNotSetError
   :members:

.. autoclass:: SheetNotSetError
   :members:


.. autoclass:: ReachSpreadsheet
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: htmlColorToJSON
.. autofunction:: testCreateSpreadsheet
.. autofunction:: testSetSpreadsheet
.. autofunction:: testAddSheet
.. autofunction:: testSetDimensions
.. autofunction:: testGridRangeForStr
.. autofunction:: testSetCellStringFormatterormat
.. autofunction:: testPureBlackBorder
.. autofunction:: testUpdateCellStringFormatterieldsArg
.. autofunction:: create_pricelist
.. autofunction:: testCreateTimeManagementReport


Module Variables
----------------

.. autovariable:: MODE