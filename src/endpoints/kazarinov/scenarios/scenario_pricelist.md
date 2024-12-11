## Sergey Kazarinov's Mechiron Creation Script

### Overview

This script is part of the `hypotez/src/endpoints/kazarinov/scenarios` directory and is designed to automate the process of creating a "mechiron" for Sergey Kazarinov. The script extracts, parses, and processes product data from various suppliers, prepares the data, processes it through AI, and integrates with Facebook for product publication.

### Key Features

1. **Data Extraction and Parsing**: Extracts and parses product data from various suppliers.
2. **AI Data Processing**: Processes the extracted data through the Google Generative AI model.
3. **Data Storage**: Saves the processed data to files.
4. **Report Generation**: Generates HTML and PDF reports from the processed data.
5. **Facebook Publication**: Publishes the processed data to Facebook.

### Module Flowchart

```mermaid
graph TD
    Start[Start] --> InitMexironBuilder[Initialize MexironBuilder]
    InitMexironBuilder --> LoadConfig[Load Configuration]
    LoadConfig --> SetExportPath[Set Export Path]
    SetExportPath --> LoadSystemInstruction[Load System Instructions]
    LoadSystemInstruction --> InitModel[Initialize AI Model]
    InitModel --> RunScenario[Run Scenario]
    RunScenario --> CheckURLs{URLs Provided?}
    CheckURLs -->|Yes| GetGraber[Get Graber by Supplier URL]
    CheckURLs -->|No| LogNoURLs[Log: URLs Not Provided]
    GetGraber --> GrabPage[Grab Page Data]
    GrabPage --> ConvertFields[Convert Product Fields]
    ConvertFields --> SaveData[Save Product Data]
    SaveData --> ProcessAI[Process Data via AI]
    ProcessAI --> CreateReport[Create Report]
    CreateReport --> PostFacebook[Post to Facebook]
    PostFacebook --> End[End]
```

### Legend

1. **Start**: Start of script execution.
2. **InitMexironBuilder**: Initialization of the `MexironBuilder` class.
3. **LoadConfig**: Loads configuration from a JSON file.
4. **SetExportPath**: Sets the path for data export.
5. **LoadSystemInstruction**: Loads system instructions for the AI model.
6. **InitModel**: Initializes the Google Generative AI model.
7. **RunScenario**: Executes the main scenario.
8. **CheckURLs**: Checks if URLs for parsing are provided.
9. **GetGraber**: Retrieves the appropriate graber for the supplier URL.
10. **GrabPage**: Extracts page data using the graber.
11. **ConvertFields**: Converts product fields into a dictionary.
12. **SaveData**: Saves product data to a file.
13. **ProcessAI**: Processes product data through the AI model.
14. **CreateReport**: Creates HTML and PDF reports from the processed data.
15. **PostFacebook**: Publishes the processed data to Facebook.
16. **End**: End of script execution.

-----------------------

#### Class: `MexironBuilder`

- **Attributes**:
  - `driver`: Selenium WebDriver instance.
  - `export_path`: Path for data export.
  - `mexiron_name`: Custom name for the mechiron process.
  - `price`: Price for processing.
  - `timestamp`: Timestamp for the process.
  - `products_list`: List of processed product data.
  - `model`: Google Generative AI model.
  - `config`: Configuration loaded from JSON.

- **Methods**:
  - **`__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`**:
    - **Purpose**: Initializes the `MexironBuilder` class with necessary components.
    - **Parameters**:
      - `driver`: Selenium WebDriver instance.
      - `mexiron_name`: Custom name for the mechiron process.
    ----
  - **`run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool`**:
    - **Purpose**: Executes the scenario: parses products, processes them through AI, and saves the data.
    - **Parameters**:
      - `system_instruction`: System instructions for the AI model.
      - `price`: Price for processing.
      - `mexiron_name`: Custom mechiron name.
      - `urls`: URLs of product pages.
    - **Returns**: `True` if the scenario runs successfully, otherwise `False`.



    -  **Flowchart**:
        ```mermaid
        flowchart TD
        Start[Start] --> IsOneTab{URL is from OneTab?}
        IsOneTab -->|Yes| GetDataFromOneTab[Get data from OneTab]
        IsOneTab -->|No| ReplyTryAgain[Reply - Try again]
        GetDataFromOneTab --> IsDataValid{Data valid?}
        IsDataValid -->|No| ReplyIncorrectData[Reply Incorrect data]
        IsDataValid -->|Yes| RunMexironScenario[Run Mexiron scenario]
        RunMexironScenario --> IsGraberFound{Graber found?}
        IsGraberFound -->|Yes| StartParsing[Start parsing: <code>url</code>]
        IsGraberFound -->|No| LogNoGraber[Log: No graber for <code>url</code>]
        StartParsing --> IsParsingSuccessful{Parsing successful?}
        IsParsingSuccessful -->|Yes| ConvertProductFields[Convert product fields]
        IsParsingSuccessful -->|No| LogParsingFailed[Log: Failed to parse product fields]
        ConvertProductFields --> IsConversionSuccessful{Conversion successful?}
        IsConversionSuccessful -->|Yes| SaveProductData[Save product data]
        IsConversionSuccessful -->|No| LogConversionFailed[Log: Failed to convert product fields]
        SaveProductData --> IsDataSaved{Data saved?}
        IsDataSaved -->|Yes| AppendToProductsList[Append to products_list]
        IsDataSaved -->|No| LogDataNotSaved[Log: Data not saved]
        AppendToProductsList --> ProcessAIHe[AI processing lang = he]
        ProcessAIHe --> ProcessAIRu[AI processing lang = ru]
        ProcessAIRu --> SaveHeJSON{Save JSON for he?}
        SaveHeJSON -->|Yes| SaveRuJSON[Save JSON for ru]
        SaveHeJSON -->|No| LogHeJSONError[Log: Error saving he JSON]
        SaveRuJSON --> IsRuJSONSaved{Save JSON for ru?}
        IsRuJSONSaved -->|Yes| GenerateReports[Generate reports]
        IsRuJSONSaved -->|No| LogRuJSONError[Log: Error saving ru JSON]
        GenerateReports --> IsReportGenerationSuccessful{Report generation successful?}
        IsReportGenerationSuccessful -->|Yes| SendPDF[Send PDF via Telegram]
        IsReportGenerationSuccessful -->|No| LogPDFError[Log: Error creating PDF]
        SendPDF --> ReturnTrue[Return True]
        LogPDFError --> ReturnTrue[Return True]
        ReplyIncorrectData --> ReturnTrue[Return True]
        ReplyTryAgain --> ReturnTrue[Return True]
        LogNoGraber --> ReturnTrue[Return True]
        LogParsingFailed --> ReturnTrue[Return True]
        LogConversionFailed --> ReturnTrue[Return True]
        LogDataNotSaved --> ReturnTrue[Return True]
        LogHeJSONError --> ReturnTrue[Return True]
        LogRuJSONError --> ReturnTrue[Return True]
        ```

        - **Legend**

    1. **Start**: The scenario begins execution.

    2. **URL Source Check (IsOneTab)**:
       - If the URL is from OneTab, data is extracted from OneTab.
       - If the URL is not from OneTab, the user is sent a "Try again" message.

    3. **Data Validity Check (IsDataValid)**:
       - If the data is invalid, the user is sent an "Incorrect data" message.
       - If the data is valid, the Mexiron scenario is initiated.

    4. **Grabber Search (IsGraberFound)**:
       - If a grabber is found, the page parsing begins.
       - If a grabber is not found, a log message is generated indicating that no grabber is available for the given URL.

    5. **Page Parsing (StartParsing)**:
       - If parsing is successful, the data is converted into the required format.
       - If parsing fails, an error is logged.

    6. **Data Conversion (ConvertProductFields)**:
       - If the conversion is successful, the data is saved.
       - If the conversion fails, an error is logged.

    7. **Data Saving (SaveProductData)**:
       - If the data is saved, it is added to the products list.
       - If the data is not saved, an error is logged.

    8. **AI Processing (ProcessAIHe, ProcessAIRu)**:
       - The data is processed by AI for the languages `he` (Hebrew) and `ru` (Russian).

    9. **JSON Saving (SaveHeJSON, SaveRuJSON)**:
       - The processing results are saved in JSON format for each language.
       - If saving fails, an error is logged.

    10. **Report Generation (GenerateReports)**:
        - HTML and PDF reports are generated for each language.
        - If report generation fails, an error is logged.

    11. **PDF Sending via Telegram (SendPDF)**:
        - PDF files are sent via Telegram.
        - If sending fails, an error is logged.

    12. **Completion (ReturnTrue)**:
        - The scenario ends by returning `True`.

#### **Error Logging**:
- At each stage where errors may occur, nodes are included to log errors (e.g., `LogNoGraber`, `LogParsingFailed`, `LogHeJSONError`, etc.).

----
  - **`get_graber_by_supplier_url(self, url: str)`**:
    - **Purpose**: Returns the appropriate graber for the given supplier URL.
    - **Parameters**:
      - `url`: Supplier page URL.
    - **Returns**: Graber instance if found, otherwise `None`.
----
  - **`convert_product_fields(self, f: ProductFields) -> dict`**:
    - **Purpose**: Converts product fields into a dictionary.
    - **Parameters**:
      - `f`: Object containing parsed product data.
    - **Returns**: Formatted dictionary of product data.
----
  - **`save_product_data(self, product_data: dict)`**:
    - **Purpose**: Saves product data to a file.
    - **Parameters**:
      - `product_data`: Formatted product data.
----
  - **`process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool`**:
    - **Purpose**: Processes a list of products through the AI model.
    - **Parameters**:
      - `products_list`: List of product data dictionaries as strings.
      - `attempts`: Number of retry attempts in case of failure.
    - **Returns**: Processed response in `ru` and `he` formats.
----
  - **`post_facebook(self, mexiron: SimpleNamespace) -> bool`**:
    - **Purpose**: Executes the Facebook publication scenario.
    - **Parameters**:
      - `mexiron`: Processed data for publication.
    - **Returns**: `True` if publication is successful, otherwise `False`.
----
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
3. **Run Scenario**: Call the `run_scenario` method with the necessary parameters.

#### Example

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Initialize Driver
driver = Driver(...)

# Initialize MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Run Scenario
urls = ['https://example.com/product1', 'https://example.com/product2']
mexiron_builder.run_scenario(urls=urls)
```

### Dependencies

- `selenium`: For web automation.
- `asyncio`: For asynchronous operations.
- `pathlib`: For file path handling.
- `types`: For creating simple namespaces.
- `typing`: For type annotations.
- `src.ai.gemini`: For AI data processing.
- `src.suppliers.*.graber`: For data extraction from various suppliers.
- `src.endpoints.advertisement.facebook.scenarios`: For Facebook publication.

### Error Handling

The script includes robust error handling to ensure continued execution even if some elements are not found or if there are issues with the web page. This is particularly useful for handling dynamic or unstable web pages.

### Contribution

Contributions to this script are welcome. Please ensure that any changes are well-documented and include appropriate tests.

### License

This script is licensed under the MIT License. See the `LICENSE` file for details.