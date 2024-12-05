rst
How to use the `utils` module
========================================================================================

Description
-------------------------
This module provides a collection of utility functions for various tasks, including data conversion, file handling, and output formatting.  It aims to streamline common programming tasks by offering reusable functions.  The module exports various functions for tasks such as converting CSV to dictionaries, JSON to XLSX, saving text to files, and more.

Execution steps
-------------------------
1. **Import necessary functions:**  Import the specific utility functions you need from the `src.utils` module.  For example, to use the `csv2dict` function, import it as shown in the example.

2. **Prepare input data:**  Ensure that the input data (e.g., a CSV file, JSON data) is available or prepared in the format expected by the function.

3. **Call the utility function:**  Execute the desired function, passing the necessary input arguments (e.g., file paths, data structures).

4. **Handle the output:**  The output of the function (e.g., a dictionary, a file) can then be used further in your program.


Usage example
-------------------------
.. code-block:: python

    from src.utils import csv2dict, save_text_file

    # Example to convert a CSV file to a dictionary
    try:
        csv_data = csv2dict('data.csv')
        print("CSV data converted successfully:", csv_data)

        # Example to save text to a file
        save_text_file('output.txt', 'This is the output text.')
        print("Text saved to output.txt successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")