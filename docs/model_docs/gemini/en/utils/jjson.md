```rst
hypotez/src/utils/jjson.py
==========================

.. module:: hypotez.src.utils.jjson
   :platform: Windows, Unix
   :synopsis: Module for handling JSON and CSV files, including loading, dumping, and merging data.

This module provides functions to:
- **Dump JSON data**: Convert JSON or SimpleNamespace objects into JSON format and write to a file, or return the JSON data as a dictionary.
- **Load JSON and CSV data**: Read JSON or CSV data from a file, directory, or string, and convert it into dictionaries or lists of dictionaries.
- **Convert to SimpleNamespace**: Convert loaded JSON data into SimpleNamespace objects for easier manipulation.
- **Merge JSON files**: Combine multiple JSON files from a directory into a single JSON file.
- **Parse Markdown**: Convert Markdown strings to JSON format for structured data representation.

The functions in this module handle various aspects of working with JSON and CSV data, ensuring that data is loaded, saved, and merged efficiently and effectively.


Functions
---------

.. autofunction:: hypotez.src.utils.jjson.j_dumps
.. autofunction:: hypotez.src.utils.jjson.j_loads
.. autofunction:: hypotez.src.utils.jjson.j_loads_ns
.. autofunction:: hypotez.src.utils.jjson.replace_key_in_json
.. autofunction:: hypotez.src.utils.jjson.process_json_file
.. autofunction:: hypotez.src.utils.jjson.recursive_process_json_files
.. autofunction:: hypotez.src.utils.jjson.extract_json_from_string


```