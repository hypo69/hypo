# Module: hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py

## Overview

This module provides functionality for extracting, parsing, and processing product data from various suppliers. It handles data preparation, AI processing, and integration with Facebook for product posting.  It utilizes various components, including Selenium WebDriver (Driver), an AI model (GoogleGenerativeAI), and grabbers for different suppliers (Morlevi, KSP, Ivory, Grandadvance).  The module aims to automate the process of extracting product data, processing it using AI, and publishing the results to Facebook.


## Classes

### `Mexiron`

**Description**: This class encapsulates the process of extracting product data from suppliers, processing it with an AI model, and publishing results to Facebook.  It handles data retrieval, conversion, saving, AI processing, and Facebook posting.

**Attributes**:

- `driver (Driver)`: Selenium WebDriver instance for interacting with web pages.
- `export_path (Path)`: Directory for saving extracted product data.
- `mexiron_name (str)`: Name for the current processing run.
- `price (float)`: Price of the products being processed.
- `timestamp (str)`: Timestamp indicating the processing time.
- `products_list (List)`: List to store parsed product data.
- `model (GoogleGenerativeAI)`: Instance of the AI model for processing product data.
- `model_command (str)`:  Command instructions for the AI model.
- `config (SimpleNamespace)`: Configuration data from `kazarinov.json`.


**Methods**:

#### `__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`

**Description**: Initializes the Mexiron class with required components.

**Parameters**:
- `driver (Driver)`: Selenium WebDriver instance.
- `mexiron_name (Optional[str], optional): Custom name for the Mexiron process. Defaults to the current timestamp.


#### `run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None) -> bool`

**Description**: Executes the scenario: parses products, processes them via AI, and stores data.

**Parameters**:
- `system_instruction (Optional[str], optional): System instructions for the AI model. Defaults to None.
- `price (Optional[str], optional): Price to process. Defaults to None.
- `mexiron_name (Optional[str], optional): Custom Mexiron name. Defaults to None.
- `urls (Optional[str | List[str]], optional): Product page URLs. Defaults to None.

**Returns**:
- `bool`: True if the scenario executes successfully, False otherwise.

#### `get_graber_by_supplier_url(self, url: str) -> Optional[object]`

**Description**: Returns the appropriate graber for a given supplier URL.

**Parameters**:
- `url (str)`: Supplier page URL.

**Returns**:
- `Optional[object]`: Graber instance if a match is found, None otherwise.


#### `convert_product_fields(self, f: ProductFields) -> dict`

**Description**: Converts product fields into a dictionary.

**Parameters**:
- `f (ProductFields)`: Object containing parsed product data.

**Returns**:
- `dict`: Formatted product data dictionary.


#### `save_product_data(self, product_data: dict)`

**Description**: Saves individual product data to a file.

**Parameters**:
- `product_data (dict)`: Formatted product data.

#### `process_ai(self, products_list: str, attemts: int = 3) -> tuple | bool`

**Description**: Processes the product list through the AI model.

**Parameters**:
- `products_list (str)`: List of product data dictionaries.
- `attemts (int, optional): Number of retry attempts. Defaults to 3.

**Returns**:
- `tuple`: Processed response in `ru` and `he` formats.
  
**Raises**:
- Various exceptions potentially raised during AI processing or data handling.

#### `post_facebook(self, mexiron:SimpleNamespace) -> bool`

**Description**: Posts data to Facebook.

**Parameters**:
- `mexiron (SimpleNamespace)`: Data to post.

**Returns**:
- `bool`: True if posting is successful, False otherwise.

**Raises**:
- Various exceptions potentially raised during Facebook API interaction.



#### `create_report(self)`

**Description**: Generates a report.


## Functions (none found)

## Modules (imported)

- `asyncio`
- `random`
- `pathlib`
- `typing`
- `types`
- `dataclasses`
- `src.gs`
- `src.product.product_fields`
- `src.webdriver`
- `src.ai.gemini`
- `src.endpoints.advertisement.facebook.scenarios`
- `src.suppliers.morlevi.graber`
- `src.suppliers.ksp.graber`
- `src.suppliers.ivory.graber`
- `src.suppliers.grandadvance.graber`
- `src.endpoints.kazarinov.react`
- `src.utils.jjson`
- `src.utils.file`
- `src.utils.image`
- `src.logger`