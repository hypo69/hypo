# file hypotez/src/scenario/executor.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.scenario.executor
   :platform: Windows, Unix
   :synopsis: Module for executing scenarios.

This module contains functions for executing scenarios, loading them from files,
and handling the process of extracting product information and inserting it into PrestaShop.
"""


import os
import sys
import requests
import asyncio
import time
import tempfile
from datetime import datetime
from math import log, prod
from pathlib import Path
from typing import Dict, List
import json

import header
from src import gs
from src.utils.printer import pprint
from src.utils.jjson import j_loads, j_dumps
from src.product import Product, ProductFields, translate_presta_fields_dict
from src.endpoints.prestashop import PrestaShop
from src.db import ProductCampaignsManager
from src.logger import logger
from src.logger.exceptions import ProductFieldException


_journal: dict = {'scenario_files': ''}
_journal['name'] = timestamp = gs.now


def dump_journal(s, journal: dict):
    """
    Save the journal data to a JSON file.

    :param s: Supplier instance.
    :param journal: Dictionary containing the journal data.
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)


def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Executes a list of scenario files.

    :param s: Supplier instance.
    :param scenario_files_list: List of file paths for scenario files, or a single file path.
    :raises TypeError: if scenario_files_list is not a list or a string.
    :return: True if all scenarios were executed successfully, False otherwise.
    """
    # Handles single file input
    if isinstance(scenario_files_list, Path):
        scenario_files_list = [scenario_files_list]
    elif not isinstance(scenario_files_list, list):
        raise TypeError("scenario_files_list must be a list or a Path object.")
    # Handles empty input
    scenario_files_list = scenario_files_list if scenario_files_list else s.scenario_files

    _journal['scenario_files'] = {}
    for scenario_file in scenario_files_list:
        _journal['scenario_files'][scenario_file.name] = {}
        try:
            if run_scenario_file(s, scenario_file):
                _journal['scenario_files'][scenario_file.name]['message'] = f"{scenario_file} completed successfully!"
                logger.success(f'Scenario {scenario_file} completed successfully!')
            else:
                _journal['scenario_files'][scenario_file.name]['message'] = f"{scenario_file} FAILED!"
                logger.error(f'Scenario {scenario_file} failed to execute!')
        except Exception as e:
            logger.critical(f"An error occurred while processing {scenario_file}: {e}")
            _journal['scenario_files'][scenario_file.name]['message'] = f"Error: {e}"
    return True


# ... (rest of the code)
```

```
<algorithm>
```
1. **Input**: Supplier instance (`s`) and a list of scenario file paths (`scenario_files_list`).

2. **Initialization**:
   - Creates an empty dictionary `_journal` to store execution results.
   - Stores the current timestamp in `_journal['name']`.


3. **File Processing Loop**:
   - Iterates through each `scenario_file` in the input list.
   - Tries to run each `scenario_file` using `run_scenario_file()`.
   - If successful, logs success and updates `_journal`.
   - If failure, logs error and updates `_journal`.
   - Catches any exceptions and logs critical errors, updating `_journal`.

4. **Return**: Returns `True` if all scenarios were processed successfully.


```
<explanation>

**Imports**:
- `os`, `sys`, `requests`, `asyncio`, `time`, `tempfile`, `datetime`, `math`, `pathlib`, `typing`, `json`: Standard Python libraries for various functionalities.
- `header`: Likely a custom module for header-related tasks,  part of the project's `src` package.
- `gs`: Part of `src`, possibly for global state management or utilities.
- `pprint`: From `src.utils.printer`, for formatted printing.
- `j_loads`, `j_dumps`: From `src.utils.jjson`, for JSON encoding/decoding.
- `Product`, `ProductFields`, `translate_presta_fields_dict`: From `src.product`, likely related to product data handling.
- `PrestaShop`: From `src.endpoints.prestashop`, for interacting with the PrestaShop API.
- `ProductCampaignsManager`: From `src.db`, for interacting with the database related to product campaigns.
- `logger`: From `src.logger`, for logging messages and errors.
- `ProductFieldException`: From `src.logger.exceptions`, a custom exception type related to product fields.

**Classes**:
- `Product`: Likely represents a product with attributes like `supplier_prefix` and `presta_fields_dict`. Interactions with `ProductFields` and data from URLs.
- `ProductFields`: Contains data for a product's fields.
- `PrestaShop`: Contains methods for interacting with the PrestaShop API.
- `ProductCampaignsManager`: Manages product campaigns in the database.

**Functions**:
- `dump_journal()`: Saves the `_journal` data to a JSON file.
- `run_scenario_files()`: Executes a list of scenario files. Takes a supplier instance `s` and list of file paths. Catches errors during execution, logging them appropriately and keeping the journal consistent.
- `run_scenario_file()`: Loads scenarios from a JSON file and executes them sequentially. Takes a supplier instance `s` and path to the file. Handles `FileNotFoundError` and `json.JSONDecodeError`.
- `run_scenarios()`: Executes a list of scenarios (NOT FILES). Takes a supplier instance `s`, and a list of scenario dictionaries. Handles empty scenario lists gracefully.
- `run_scenario()`: Executes a single scenario. Takes a supplier instance `s` , scenario dictionary, and scenario name. Handles product data acquisition and PrestaShop insertion.
- `insert_grabbed_data()`: Inserts grabbed product data into PrestaShop. Calls `execute_PrestaShop_insert()` which handles the actual API calls.
- `execute_PrestaShop_insert()`: Inserts a product into PrestaShop. Uses the PrestaShop class to make the API call.

**Variables**:
- `_journal`: A dictionary used to keep track of scenario execution status and errors.

**Potential Errors/Improvements**:
- Error handling could be more robust in `run_scenario_file()`.
- Using a more structured, possibly object-oriented, approach for product data processing (instead of `insert_grabbed_data`).
- Async operations are used but not always handled using `async`. The structure needs to be optimized for asynchronous operations.
- `run_scenario()` could benefit from better input validation to handle various scenarios (e.g., missing `url`).
- The code lacks explicit error handling for missing product data or other issues during product insertion.
- The `_journal` variable would benefit from a logging class for easier manipulation and potentially better integration with other log systems.
- `dump_journal` is called at each iteration. This may cause unnecessary I/O operations.



**Relationships**:
The code is deeply integrated with the `src` package, specifically with modules for product data handling (`src.product`), interacting with the PrestaShop API (`src.endpoints.prestashop`), database interactions (`src.db`), logging (`src.logger`), and general utility functions (`src.utils`). The `gs` module likely interacts with the global state related to scenario execution.  The `supplier` instance holds essential information for the execution process.