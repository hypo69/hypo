
## Mexiron Builder Scenario

### Overview

This script is part of the `hypotez/src/endpoints/kazarinov/scenarios` directory and is designed to automate the process of creating a "Mexiron" for Sergey Kazarinov. The script extracts, parses, and processes product data from various suppliers, prepares the data, processes it through AI, and integrates with Facebook for product posting.

### Key Features

1. **Data Extraction and Parsing**: Extracts and parses product data from various suppliers.
2. **AI Processing**: Processes the extracted data through a Google Generative AI model.
3. **Data Storage**: Saves the processed data to files.
4. **Report Generation**: Generates HTML and PDF reports from the processed data.
5. **Facebook Posting**: Posts the processed data to Facebook.

### Module Structure

```mermaid
graph TD
    Start[Start] --> InitMexironBuilder[Initialize MexironBuilder]
    InitMexironBuilder --> LoadConfig[Load Configuration]
    LoadConfig --> SetExportPath[Set Export Path]
    SetExportPath --> LoadSystemInstruction[Load System Instruction]
    LoadSystemInstruction --> InitModel[Initialize AI Model]
    InitModel --> RunScenario[Run Scenario]
    RunScenario --> CheckURLs{URLs Provided?}
    CheckURLs -->|Yes| GetGraber[Get Graber by Supplier URL]
    CheckURLs -->|No| LogNoURLs[Log: No URLs Provided]
    GetGraber --> GrabPage[Grab Page Data]
    GrabPage --> ConvertFields[Convert Product Fields]
    ConvertFields --> SaveData[Save Product Data]
    SaveData --> ProcessAI[Process Data with AI]
    ProcessAI --> CreateReport[Create Report]
    CreateReport --> PostFacebook[Post to Facebook]
    PostFacebook --> End[End]
```

### Legend

1. **Start**: Start of script execution.
2. **InitMexironBuilder**: Initialize the `MexironBuilder` class.
3. **LoadConfig**: Load the configuration from the JSON file.
4. **SetExportPath**: Set the export path based on the configuration.
5. **LoadSystemInstruction**: Load the system instruction for the AI model.
6. **InitModel**: Initialize the Google Generative AI model.
7. **RunScenario**: Execute the main scenario.
8. **CheckURLs**: Check if URLs are provided for parsing.
9. **GetGraber**: Get the appropriate graber for the supplier URL.
10. **GrabPage**: Grab the page data using the graber.
11. **ConvertFields**: Convert the product fields into a dictionary.
12. **SaveData**: Save the product data to a file.
13. **ProcessAI**: Process the product data through the AI model.
14. **CreateReport**: Create HTML and PDF reports from the processed data.
15. **PostFacebook**: Post the processed data to Facebook.
16. **End**: End of script execution.

-----------------------

#### Class: `MexironBuilder`

- **Attributes**:
  - `driver`: Selenium WebDriver instance.
  - `export_path`: Path for exporting data.
  - `mexiron_name`: Custom name for the Mexiron process.
  - `price`: Price to process.
  - `timestamp`: Timestamp for the process.
  - `products_list`: List of processed product data.
  - `model`: Google Generative AI model.
  - `config`: Configuration loaded from JSON.

- **Methods**:
  - **`__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`**:
    - **Purpose**: Initializes the `MexironBuilder` class with required components.
    - **Parameters**:
      - `driver`: Selenium WebDriver instance.
      - `mexiron_name`: Custom name for the Mexiron process.

  - **`run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool`**:
    - **Purpose**: Executes the scenario: parses products, processes them via AI, and stores data.
    - **Parameters**:
      - `system_instruction`: System instructions for the AI model.
      - `price`: Price to process.
      - `mexiron_name`: Custom Mexiron name.
      - `urls`: Product page URLs.
    - **Returns**: `True` if the scenario executes successfully, `False` otherwise.

  - **`get_graber_by_supplier_url(self, url: str)`**:
    - **Purpose**: Returns the appropriate graber for a given supplier URL.
    - **Parameters**:
      - `url`: Supplier page URL.
    - **Returns**: Graber instance if a match is found, `None` otherwise.

  - **`convert_product_fields(self, f: ProductFields) -> dict`**:
    - **Purpose**: Converts product fields into a dictionary.
    - **Parameters**:
      - `f`: Object containing parsed product data.
    - **Returns**: Formatted product data dictionary.

  - **`save_product_data(self, product_data: dict)`**:
    - **Purpose**: Saves individual product data to a file.
    - **Parameters**:
      - `product_data`: Formatted product data.

  - **`process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool`**:
    - **Purpose**: Processes the product list through the AI model.
    - **Parameters**:
      - `products_list`: List of product data dictionaries as a string.
      - `attempts`: Number of attempts to retry in case of failure.
    - **Returns**: Processed response in `ru` and `he` formats.

  - **`post_facebook(self, mexiron: SimpleNamespace) -> bool`**:
    - **Purpose**: Executes the Facebook posting scenario.
    - **Parameters**:
      - `mexiron`: Processed data to post.
    - **Returns**: `True` if the post is successful, `False` otherwise.

  - **`create_report(self, data: dict, html_file: Path, pdf_file: Path)`**:
    - **Purpose**: Generates HTML and PDF reports from the processed data.
    - **Parameters**:
      - `data`: Processed data.
      - `html_file`: Path to save the HTML report.
      - `pdf_file`: Path to save the PDF report.

### Usage

To use this script, follow these steps:

1. **Initialize Driver**: Create an instance of the `Driver` class.
2. **Initialize MexironBuilder**: Create an instance of the `MexironBuilder` class with the driver.
3. **Run Scenario**: Call the `run_scenario` method with the required parameters.

#### Example

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Initialize Driver
driver = Driver(...)

# Initialize MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Run scenario
urls = ['https://example.com/product1', 'https://example.com/product2']
mexiron_builder.run_scenario(urls=urls)
```

### Dependencies

- `selenium`: For web automation.
- `asyncio`: For asynchronous operations.
- `pathlib`: For handling file paths.
- `types`: For creating simple namespaces.
- `typing`: For type annotations.
- `src.ai.gemini`: For AI processing.
- `src.suppliers.*.graber`: For data extraction from various suppliers.
- `src.endpoints.advertisement.facebook.scenarios`: For Facebook posting.

### Error Handling

The script includes robust error handling to ensure that the execution continues even if certain elements are not found or if there are issues with the web page. This is particularly useful for handling dynamic or unstable web pages.

### Contributing

Contributions to this script are welcome. Please ensure that any changes are well-documented and include appropriate tests.

### License

This script is licensed under the MIT License. See the `LICENSE` file for more details.

---

This README provides a comprehensive overview of the `scenario_pricelist.py` script, including its purpose, structure, usage, and dependencies. It is intended to help developers understand and utilize the script effectively.