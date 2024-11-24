hypotez/src/goog/spreadsheet/bberyakov/grender.py
==============================================

.. module:: hypotez.src.goog.spreadsheet.bberyakov.grender
   :platform: Windows, Unix
   :synopsis: This module provides functions for rendering Google Spreadsheet data.


Module Description
------------------

This module contains the `GSRender` class and related functions for formatting and rendering data within Google Sheets.  It leverages the `gspread` library for interacting with the Google Sheets API.  The module is designed to provide specific formatting options, including header rendering, cell formatting, and merging cells based on given criteria.


Classes
-------

.. autoclass:: GSRender
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: GSRender.render_header
.. autofunction:: GSRender.merge_range
.. autofunction:: GSRender.set_worksheet_direction
.. autofunction:: GSRender.header
.. autofunction:: GSRender.write_category_title
.. autofunction:: GSRender.get_first_empty_row


Example Usage (Illustrative)
----------------------------

The following code snippets demonstrate how to use some of the functions in this module.  These are intended as examples and not complete, working applications.


```python
# Example usage (Illustrative)
# ... (Import necessary modules) ...

# Create a GSRender object
render_obj = GSRender()

# Assuming 'sh' is an instance of Spreadsheet and 'ws' is an instance of Worksheet
# ... (Get Spreadsheet and Worksheet objects) ...

# Example: Rendering a header
render_obj.header(ws, 'My Table Header')

# Example: Merging cells
render_obj.merge_range(ws, 'A1:C1', 'MERGE_ALL')

# Example: Setting worksheet direction
render_obj.set_worksheet_direction(sh, ws, 'rtl')

# ... (Further usage of other functions) ...
```