## File hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.endpoints.kazarinov.scenarios \n\t:platform: Windows, Unix\n\t:synopsis: Provides functionality for extracting, parsing, and processing product data from \nvarious suppliers. The module handles data preparation, AI processing, \nand integration with Facebook for product posting.\n\n"""\nMODE = \'dev\'\n\nimport asyncio\nimport random\nfrom pathlib import Path\nfrom typing import Optional, List\nfrom types import SimpleNamespace\nfrom dataclasses import field\n\nfrom src import gs\nfrom src.product.product_fields import ProductFields\nfrom src.webdriver import Driver\nfrom src.ai.gemini import GoogleGenerativeAI\nfrom src.endpoints.advertisement.facebook.scenarios import (\n    post_message_title, upload_post_media, message_publish\n)\nfrom src.suppliers.morlevi.graber import Graber as MorleviGraber\nfrom src.suppliers.ksp.graber import Graber as KspGraber\nfrom src.suppliers.ivory.graber import Graber as IvoryGraber\nfrom src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber\nfrom src.endpoints.kazarinov.react import ReportGenerator\nfrom src.utils.jjson import j_loads_ns, j_dumps\nfrom src.utils.file import read_text_file, save_text_file, recursively_get_file_path\nfrom src.utils.image import save_png_from_url, save_png\nfrom src.logger import logger\n\nclass Mexiron:\n    """\n    Handles suppliers\' product extraction, parsing, and saving processes.\n    \n    Supported suppliers:\n    - https://morlevi.co.il\n    - https://ivory.co.il\n    - https://ksp.co.il\n    - https://grandadvance.co.il\n    """\n\n    # Class attributes\n    driver: Driver\n    export_path: Path\n    mexiron_name: str\n    price: float\n    timestamp: str\n    products_list: List = field(default_factory=list)\n    model: GoogleGenerativeAI\n    model_command:str\n    config:SimpleNamespace\n\n    # ... (rest of the class is omitted for brevity)
```

```<algorithm>
**Step 1: Initialization**

*   Input: Driver instance, optional `mexiron_name`.
*   Load configuration from `kazarinov.json` (using `gs.path.endpoints`).
*   Set `timestamp`.
*   Set `mexiron_name` (defaults to timestamp if not provided).
*   Determine `export_path` based on configuration (`external_storage`, `data`, or `goog`) and `mexiron_name`.
*   Read system and command instructions for the AI model from `system_instruction_mexiron.md` and `command_instruction_mexiron.md`
*   Initialize `GoogleGenerativeAI` model with API key and instructions.

**Step 2: Data Extraction**

*   Input: List of URLs (`urls`).
*   Convert single URL to a list if necessary.
*   For each URL:
    *   Get the appropriate `Graber` instance (using `get_graber_by_supplier_url`).
    *   Navigate to the URL using the `Driver` instance.
    *   Parse the page using the `Graber` instance. (async operation).
    *   If parsing fails, log the error and skip to the next URL.
    *   Convert parsed data to a dictionary (using `convert_product_fields`).
    *   Save the product data to a JSON file (using `save_product_data`).

**Step 3: AI Processing**

*   Input: List of product data dictionaries (`products_list`), optional `price`.
*   Process the product data using the `GoogleGenerativeAI` model (using `model_command` for instructions and input data), with retries.
*   If AI processing fails, log the error and retry (up to a maximum number of attempts).
*   Check if the AI response contains valid `ru` and `he` data.
*   If successful, return the `ru` and `he` data.

**Step 4: Facebook Posting**

*   Input: Processed data in `ru` and `he` format.
*   Post product information to Facebook using `post_message_title`, `upload_post_media`, and `message_publish`.
*   Log any errors during Facebook posting.

**Step 5: Reporting**

*   Generate a report (HTML and PDF) using `ReportGenerator`.

**Data Flow Example:**

```
URLs -> get_graber_by_supplier_url -> Graber -> Driver -> ProductFields
ProductFields -> convert_product_fields -> dict -> save_product_data -> file
list of dict -> process_ai -> GoogleGenerativeAI -> ru, he data -> post_facebook, create_report
```
```

```<explanation>

**Imports:**

*   `asyncio`: For asynchronous operations, crucial for potentially long-running tasks like web scraping and AI processing.
*   `random`:  (Potentially used for random behavior, not immediately clear from the snippet).
*   `pathlib`: For working with file paths.
*   `typing`: For type hinting, improving code readability and maintainability.
*   `types`: `SimpleNamespace` for representing structured data in a more flexible way.
*   `dataclasses`: `field` for customising data classes.
*   `src.gs`: Likely a global state/configuration module.
*   `src.product.product_fields`: Defines `ProductFields` - a class or dataclass holding product data from suppliers, likely used for parsing.
*   `src.webdriver`: Selenium WebDriver interactions for web scraping.
*   `src.ai.gemini`: Google Gemini API interaction.
*   `src.endpoints.advertisement.facebook.scenarios`: Functions for posting to Facebook.
*   `src.suppliers.*.graber`: Modules containing `Graber` classes for specific suppliers (e.g., Morlevi, KSP, Ivory, Grandadvance), enabling specific product parsing.
*   `src.endpoints.kazarinov.react`: Module for report generation.
*   `src.utils.jjson`: JSON handling (`j_loads_ns`, `j_dumps`).
*   `src.utils.file`: File handling (`read_text_file`, `save_text_file`).
*   `src.utils.image`: Image handling (potentially used for storing/saving images extracted from product pages).
*   `src.logger`: Logging framework.

**Classes:**

*   `Mexiron`:
    *   Handles the entire product extraction, processing, and Facebook posting pipeline.
    *   `driver`: Selenium WebDriver instance.
    *   `export_path`: Directory for saving extracted product data.
    *   `products_list`: List of parsed product data (dictionaries).
    *   `model`: Instance of the AI model.
    *   `model_command`: Additional command instructions for the AI model.
    *   `config`: Configuration settings loaded from `kazarinov.json`.
    *   `__init__`: Initializes `Mexiron` with required components, including config, driver, timestamp, name, and export path. It has error handling and checks for config file.
    *   `run_scenario`: Executes the entire scenario, handling URL input, data processing, AI model interaction, Facebook posting, and report generation. It uses asynchronous operations and error handling to prevent application crashes and to manage possible timeouts.
    *   `get_graber_by_supplier_url`: Determines the appropriate `Graber` class based on the URL, supporting different suppliers.
    *   `convert_product_fields`: Converts product fields into a dictionary format usable by the AI.
    *   `save_product_data`: Saves individual product data to files.
    *   `process_ai`: Sends product data to the AI model, handling retries for unsuccessful requests.
    *   `post_facebook`: Posts processed data to the designated Facebook page, handling images.
    *   `create_report`: Creates and saves the report (HTML/PDF).

**Functions:**

*   `run_scenario`:  Takes URLs and other parameters to initiate the product processing. Includes error handling for invalid URLs, scraping failures, and AI failures.
*   `get_graber_by_supplier_url`:  Determines which product parser to use, based on the supplier URL.
*   `convert_product_fields`: Formats the product data (e.g., extracted from HTML) for input to the AI model.
*   `save_product_data`: Saves each parsed product to a separate JSON file.
*   `process_ai`: Sends extracted data to the AI model for translation and processing. Includes retry logic.
*   `post_facebook`: Handles the Facebook posting part of the scenario.
*   `create_report`: Generates and saves a report.



**Variables:**

*   `MODE`: String variable defining the application mode (e.g., 'dev', 'prod').
*   `gs`: Likely a global state/configuration module used for accessing configuration settings and other global variables (path, credentials, now timestamp).
*   `api_key`: API key for the AI model.


**Potential Errors/Improvements:**

*   **Error Handling:** While the code has error handling (`try...except`), it could be more robust by adding logging of specific error types.  Explicitly defining exception types that might be caught would be beneficial.
*   **Robustness:** The `process_ai` function includes multiple retries, but it could be more robust with more specific error handling and logging during each retry step.
*   **`process_ai` Function Complexity:** The `process_ai` function is very complex and potentially prone to errors. Using more structured code (more functions) might improve readability and maintainability.
*   **Data Validation:** The code should validate the data received from the AI (e.g., checking if the response has the expected format) to avoid unexpected failures.
*   **Logging**:  The use of `...` to skip code is undesirable; instead, add explicit logs or error handling for better debugging.
*   **Concurrency:** Asynchronous operations are used, but the handling of concurrent requests to various suppliers could be improved. Consider using a `ThreadPoolExecutor` for improved performance.


**Relationships to Other Parts:**

*   `Mexiron` relies on `src.product.product_fields`, `src.webdriver`, `src.ai.gemini`, `src.endpoints.advertisement.facebook.scenarios`,  `src.suppliers.*.graber`, `src.endpoints.kazarinov.react`,  `src.utils.*`, and `src.logger`.
*   `Graber` classes likely depend on the `src.webdriver` for web interaction and `src.product.product_fields` for holding parsed data structures.
*   The structure suggests a modular design; other parts likely contain utility functions or data models used by `Mexiron`.


This analysis provides a high-level understanding of the code. A deeper dive into specific functions, handling of errors, etc., would require more time.