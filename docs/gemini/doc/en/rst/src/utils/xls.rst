hypotez/src/utils/xls.py
=========================

.. module:: hypotez.src.utils.xls
    :platform: Windows, Unix
    :synopsis: Converter for Excel (`xls`) to JSON and JSON to Excel (`xls`)


This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.


Functions
---------

.. autofunction:: hypotez.src.utils.xls.read_xls_as_dict
.. autofunction:: hypotez.src.utils.xls.save_xls_file


Examples
--------

.. code-block:: python

    # Reading and optionally saving to JSON
    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Reads sheet named 'Sheet1'
    if data:
        print(data)  # Output will be {'Sheet1': [{...}]}

    # Saving from JSON data
    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Successfully saved to output.xlsx")