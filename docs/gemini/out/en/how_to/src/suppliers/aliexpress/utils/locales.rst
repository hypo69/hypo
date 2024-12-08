How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `load_locales_data` that retrieves locale data from a JSON file.  The function parses a JSON file, extracts a specific `locales` key, and returns a list of dictionaries. Each dictionary contains a locale (e.g., 'EN', 'RU') as a key and its corresponding currency (e.g., 'USD', 'EUR') as a value.  The code also defines a variable `locales` to cache the loaded locale data.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `Path` object from the `pathlib` module and `j_loads_ns` from `src.utils.jjson`. These modules are used for file path management and JSON parsing, respectively.
2. **Define `get_locales` function:** This function takes a file path (`locales_path`) as input.  It uses the `j_loads_ns` function to parse the JSON file at the specified path.
3. **Extract locales:** The function retrieves the `locales` key from the parsed JSON data.  If the key is not found, it returns `None`. Otherwise, it returns the list of dictionaries.
4. **Load default locales:** The code initializes a variable `locales` by calling the `get_locales` function, passing in the path to the 'locales.json' file located within the 'suppliers/aliexpress/utils' directory, using the `gs.path.src` object, which likely handles file paths.

Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from src import gs
    from src.suppliers.aliexpress.utils.locales import load_locales_data
    
    # Assuming you have a locales.json file in the specified location.
    # Example locales.json content:
    # {
    #   "locales": [
    #     {"EN": "USD"},
    #     {"HE": "ILS"},
    #     {"RU": "ILS"},
    #     {"EN": "EUR"},
    #     {"EN": "GBR"},
    #     {"RU": "EUR"}
    #   ]
    # }
    
    locales_path = gs.path.src / 'suppliers' / 'aliexpress' / 'utils' / 'locales.json'
    
    try:
        locales_data = load_locales_data(locales_path)
        if locales_data:
            print(locales_data)
        else:
            print("No locales data found in the file.")
    except FileNotFoundError:
        print(f"Error: File '{locales_path}' not found.")


```