```rst
hypotez/src/goog/spreadsheet/reach_spreadsheet.py
================================================

.. module:: hypotez.src.goog.spreadsheet.reach_spreadsheet
   :platform: Windows, Unix
   :synopsis: Module for interacting with Google Sheets using the Google Sheets API v4.

.. automodule:: hypotez.src.goog.spreadsheet.reach_spreadsheet
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: htmlColorToJSON
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

    .. automethod:: ReachSpreadsheet.__init__
    .. automethod:: ReachSpreadsheet.create
    .. automethod:: ReachSpreadsheet.share
    .. automethod:: ReachSpreadsheet.shareWithEmailForReading
    .. automethod:: ReachSpreadsheet.shareWithEmailForWriting
    .. automethod:: ReachSpreadsheet.shareWithAnybodyForReading
    .. automethod:: ReachSpreadsheet.shareWithAnybodyForWriting
    .. automethod:: ReachSpreadsheet.getSheetURL
    .. automethod:: ReachSpreadsheet.setSpreadsheetById
    .. automethod:: ReachSpreadsheet.runPrepared
    .. automethod:: ReachSpreadsheet.prepare_addSheet
    .. automethod:: ReachSpreadsheet.addSheet
    .. automethod:: ReachSpreadsheet.toGridRange
    .. automethod:: ReachSpreadsheet.prepare_setDimensionPixelSize
    .. automethod:: ReachSpreadsheet.prepare_setColumnsWidth
    .. automethod:: ReachSpreadsheet.prepare_setColumnWidth
    .. automethod:: ReachSpreadsheet.prepare_setRowsHeight
    .. automethod:: ReachSpreadsheet.prepare_setRowHeight
    .. automethod:: ReachSpreadsheet.prepare_setValues
    .. automethod:: ReachSpreadsheet.prepare_mergeCells
    .. automethod:: ReachSpreadsheet.prepare_setCellStringFormatterormat
    .. automethod:: ReachSpreadsheet.prepare_setCellStringFormatterormats


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


```