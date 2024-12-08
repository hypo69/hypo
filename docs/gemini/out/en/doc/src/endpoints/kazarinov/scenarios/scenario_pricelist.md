# hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py

## Overview

This module provides functionality for extracting, parsing, and processing product data from various suppliers. It handles data preparation, AI processing, and integration with Facebook for product posting.  It utilizes various helper modules and classes for data retrieval, conversion, and storage.  The core class `Mexiron` coordinates the entire process.


## Classes

### `Mexiron`

**Description**: This class handles product extraction, parsing, and saving for multiple suppliers.  It manages data flow, AI processing, and Facebook advertisement integration.

**Attributes**:

- `driver`: Selenium WebDriver instance.
- `export_path`: Path to the directory for storing extracted and processed data.
- `mexiron_name`: Name for the current Mexiron process (defaults to timestamp).
- `price`: Price of the products.
- `timestamp`: Timestamp of the process initiation.
- `products_list`: List to store product data.
- `model`: Google Generative AI instance.
- `model_command`: Command string for the AI model.
- `config`: Configuration settings from a JSON file.


**Methods**:

#### `__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`

**Description**: Initializes the `Mexiron` object with the driver, optionally a custom name. Loads configuration, sets up export path, initializes the AI model, and loads system & command instructions.

**Parameters**:

- `driver` (Driver): Selenium WebDriver instance.
- `mexiron_name` (Optional[str], optional): Custom name for the Mexiron process. Defaults to the current timestamp.

**Raises**:

- `Exception`: Errors during configuration loading, export path construction, or instruction/API key loading.  Errors are logged and the function may return early.

#### `run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, update: Update = None) -> bool`

**Description**: Executes the scenario: parses products, processes them via AI, and stores data.

**Parameters**:

- `system_instruction` (Optional[str], optional): System instructions for the AI model. Defaults to None.
- `price` (Optional[str], optional): Price to process. Defaults to None.
- `mexiron_name` (Optional[str], optional): Custom Mexiron name. Defaults to None.
- `urls` (Optional[str | List[str]], optional): Product page URLs. Defaults to None.
- `update` (Update, optional): Telegram Update object for sending updates (optional). Defaults to None.


**Returns**:

- `bool`: True if the scenario executes successfully, False otherwise.


**Raises**:

- `Exception`: Errors during product processing, AI request, or saving data.


#### `get_graber_by_supplier_url(self, url: str) -> Optional[object]`

**Description**: Returns the appropriate graber for a given supplier URL.

**Parameters**:

- `url` (str): Supplier page URL.

**Returns**:

- `Optional[object]`: Graber instance if a match is found, None otherwise.

**Raises**:

- `Exception`:  (Not explicitly documented, but implied by the code) Errors during graber selection.


#### `convert_product_fields(self, f: ProductFields) -> dict`

**Description**: Converts product fields into a dictionary.

**Parameters**:

- `f` (ProductFields): Object containing parsed product data.

**Returns**:

- `dict`: Formatted product data dictionary.


#### `save_product_data(self, product_data: dict) -> bool`

**Description**: Saves individual product data to a file.

**Parameters**:

- `product_data` (dict): Formatted product data.

**Returns**:

- `bool`: True if saving was successful, False otherwise.


#### `process_ai(self, products_list: str, attempts: int = 3) -> tuple | bool`

**Description**: Processes the product list through the AI model.

**Parameters**:

- `products_list` (str): List of product data dictionaries.
- `attempts` (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

**Returns**:

- `tuple`: Processed response in `ru` and `he` formats.
- `bool`: False if unable to get a valid response after retries.


**Raises**:

- `Exception`:  Errors during AI processing and data extraction.


#### `post_facebook(self, mexiron:SimpleNamespace) -> bool`

**Description**: Executes Facebook advertisement posting.

**Parameters**:

- `mexiron` (SimpleNamespace): Data for the post.

**Returns**:

- `bool`: True if posting successful, False otherwise.


#### `create_report(self, data: dict, html_file: Path, pdf_file: Path)`

**Description**: Generates reports in HTML and PDF formats.


**Parameters**:

- `data` (dict): Report data.
- `html_file` (Path): Path to save the HTML report.
- `pdf_file` (Path): Path to save the PDF report.

## Functions

(List functions if any exist)

## Modules