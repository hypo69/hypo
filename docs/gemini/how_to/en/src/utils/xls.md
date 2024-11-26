```
# How to use the xls.py module for converting Excel files to and from JSON

This module provides functions for converting Excel files (`.xls`) to JSON and vice-versa.  It handles multiple sheets and errors gracefully.

**1. Installing Dependencies:**

Before using this module, ensure you have the necessary libraries installed:

```bash
pip install pandas xlsxwriter
```

**2. Reading Excel to JSON:**

The `read_xls_as_dict` function reads an Excel file and converts it to a Python dictionary.  It can optionally convert a specific sheet and save the results to a JSON file.


```python
import json
from hypotez.src.utils.xls import read_xls_as_dict

# Example 1: Reading all sheets
data = read_xls_as_dict('input.xlsx')  
if data:
    print(data) # Output:  a dictionary like {'Sheet1': [{...}, {...}], 'Sheet2': [{...}, {...}]}

# Example 2: Reading a specific sheet
data_specific_sheet = read_xls_as_dict('input.xlsx', sheet_name='Sheet1')
if data_specific_sheet:
    print(json.dumps(data_specific_sheet, indent=4)) #Output: JSON representation of the Sheet1 data


# Example 3: Reading and saving to a JSON file
data_saved = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
if data_saved:
    print(f"Data successfully read and saved to 'output.json'.")

```

*   **`xls_file`:** The path to the Excel file.
*   **`json_file` (optional):** The path to save the JSON output. If omitted, the function just returns the dictionary, without saving to a file.
*   **`sheet_name` (optional):** The name or index of the sheet to process. If omitted, all sheets are read.

**Error Handling:**  The function includes `try...except` blocks to handle potential errors like the file not existing or errors reading a particular sheet.  It logs any errors using the Python `logging` module and returns `False` if an error occurs. Check the returned value to confirm the operation was successful.



**3. Saving JSON to Excel:**

The `save_xls_file` function saves JSON data to an Excel file.

```python
from hypotez.src.utils.xls import save_xls_file

# Example data (replace with your data)
data_to_save = {
    'Sheet1': [{'column1': 'value1', 'column2': 'value2'}, {'column1': 'value3', 'column2': 'value4'}],
    'Sheet2': [{'colA': 'valA'}]
}

success = save_xls_file(data_to_save, 'output.xlsx')
if success:
    print("Successfully saved to output.xlsx")
```

*   **`data`:** A dictionary where keys are sheet names and values are lists of dictionaries representing data rows.
*   **`file_path`:** The path to save the Excel file.



**Important Considerations:**

*   **Data Structure:**  The `data` dictionary used for saving to Excel must follow the specified format.
*   **Error Handling:**  Always check the return value of these functions to ensure the operation was successful.


This guide provides a complete understanding of how to use the `xls.py` module for your Excel to JSON and JSON to Excel conversions. Remember to adjust the file paths and sheet names as needed for your specific use cases.  The added logging will help with troubleshooting potential issues, especially when dealing with large or complex spreadsheets.