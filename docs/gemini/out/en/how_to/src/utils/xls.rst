How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines two functions for converting Excel (.xls) files to JSON and vice-versa.  `read_xls_as_dict` reads an Excel file, optionally selecting a specific sheet, and converts it to a Python dictionary.  `save_xls_file` takes a dictionary representing the Excel data (with sheet names and rows) and saves it to an Excel file.  Both functions incorporate error handling and logging.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports `pandas`, `json`, `typing`, `pathlib`, and `logging` for data manipulation, file handling, type hinting, and error logging, respectively.

2. **Configure logging:**  Sets up a basic logging mechanism to record information and errors during file processing. This makes debugging easier.

3. **Define `read_xls_as_dict`:**
   - Takes the Excel file path (`xls_file`), optional JSON output file path (`json_file`), and optional sheet name (`sheet_name`) as input.
   - Checks if the Excel file exists; if not, logs an error and returns `False` to signal failure.
   - Reads the Excel file using `pd.ExcelFile`.
   - If no sheet name is specified, it iterates through all sheets, attempts to convert each to a dictionary, and handles potential errors for each sheet.
   - If a sheet name is specified, it reads that specific sheet.
   - Optionally, saves the converted data to a JSON file if a `json_file` path is provided.
   - Returns the converted data as a dictionary or `False` if an error occurred.

4. **Define `save_xls_file`:**
   - Takes the data to save (`data`), which is a dictionary of sheet names mapped to lists of dictionaries representing rows, and the Excel output file path (`file_path`).
   - Uses `pd.ExcelWriter` to create a new Excel file.
   - Iterates through each sheet in the input data.
   - Creates a pandas DataFrame from the sheet data.
   - Writes the DataFrame to the specified sheet in the Excel file, preventing the inclusion of the index.
   - Returns `True` on successful saving or `False` if an error occurs.
   - Logs informative messages about successful file operations.

5. **Error Handling:**  Both functions include `try...except` blocks to gracefully handle potential errors like `FileNotFoundError` or general exceptions during file reading, conversion, or writing, logging these errors for troubleshooting and returning `False` to signal an unsuccessful operation.


Usage example
-------------------------
.. code-block:: python

    import pandas as pd
    from hypotez.src.utils.xls import read_xls_as_dict, save_xls_file

    # Example usage for reading and saving to JSON (optional)
    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
    if data:
        print(data)  # Output will be {'Sheet1': [{...}]}

    # Example usage for saving from JSON data
    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Successfully saved to output.xlsx")

    # Example usage for reading all sheets
    data = read_xls_as_dict('input.xlsx')
    if data:
        print(data)

**Important:**
- Replace `'input.xlsx'` with the actual path to your input Excel file.
- Replace `'output.json'` (if used) or `'output.xlsx'` with the desired output file path.
- Ensure the input Excel file exists.
- This example assumes you have the `pandas` library installed.  If not, install it using `pip install pandas`.