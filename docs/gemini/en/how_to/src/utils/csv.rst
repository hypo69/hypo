rst
How to use the csv utility functions
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/utils/csv.py`) provides functions for working with CSV files.  It allows saving data as CSV, reading CSV content, converting CSV to JSON, and converting CSV to a Python dictionary or a list of dictionaries using Pandas.  Error handling and logging are included for robustness.

Execution steps
-------------------------
1. **Import the module:** Import the `csv` module and other necessary libraries like `json`, `pathlib`, and `pandas` (if using `read_csv_as_ns`).

2. **Choose a function:** Select the appropriate function from the module based on the desired operation.
    * `save_csv_file`: To save a list of dictionaries to a CSV file.
    * `read_csv_file`: To read the content of a CSV file as a list of dictionaries.
    * `read_csv_as_json`: To convert a CSV file to a JSON file.
    * `read_csv_as_dict`: To convert a CSV file to a Python dictionary.
    * `read_csv_as_ns`:  To read a CSV file into a list of dictionaries using pandas.

3. **Prepare input parameters:** Provide the required arguments to the chosen function, including the file path and the data to be saved (for `save_csv_file`) or the file path to be read (for `read_csv_file`, etc.).

4. **Handle potential errors:** The functions are designed to handle potential errors like the file not being found or incorrect input data types, logging errors to prevent program crashes.

5. **Process the returned data (if applicable):** Depending on the function called, the function might return a boolean value (if the operation was successful), a list of dictionaries, a dictionary, or `None`. The calling code should handle the returned data appropriately, for instance, checking if a function returned `True` or `False` to determine if the operation was successful.

6. **Logging:** The module utilizes a `logger` (likely from a separate module) to record both successful and failed operations, providing detailed information about the actions that were performed.  Includes traceback for analysis of error conditions.


Usage example
-------------------------
.. code-block:: python

    import csv
    from pathlib import Path
    from src.utils.csv import save_csv_file, read_csv_file, read_csv_as_json, read_csv_as_ns

    # Sample data
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
    ]

    # File path
    csv_file_path = Path("my_data.csv")

    # Save data to CSV
    success = save_csv_file(data, csv_file_path, mode='w')  # Overwrites existing file

    if success:
        print("CSV file saved successfully.")

    # Read data from CSV
    read_data = read_csv_file(csv_file_path)

    if read_data:
        print("Data read from CSV:")
        print(read_data)


    # Example for read_csv_as_ns
    csv_file_path_2 = Path("my_data2.csv")
    #  ...populate my_data2.csv
    data_from_csv = read_csv_as_ns(csv_file_path_2)
    print("CSV data loaded using pandas:")
    print(data_from_csv)