# Анализ кода класса ExecuteLocator

## <input code>

```
The `executor.py` file in the `src.webdriver` module contains the `ExecuteLocator` class, which is designed for performing various actions on web page elements using Selenium WebDriver. Let’s break down the main components and functions of this class:

## General Structure and Purpose

### Main Purpose

The `ExecuteLocator` class is designed to execute navigation algorithms and interactions with a web page based on configuration data provided in the form of locator dictionaries.

### Main Components

1. **Imports and Dependencies**

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.keys import Keys
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.action_chains import ActionChains
   from selenium.common.exceptions import NoSuchElementException, TimeoutException

   from src import gs
   from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
   
   from src.logger import logger
   from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
   ```

   Here, essential libraries and modules are imported, including Selenium WebDriver for interacting with web pages, and internal modules for settings, logging, and exception handling.

2. **Class `ExecuteLocator`**

   The `ExecuteLocator` class is the core component of this file and contains methods for performing actions on web elements and handling locators. Let’s look at its methods and attributes in more detail.

### Class Attributes

- **`driver`**: A reference to the WebDriver instance used for browser interactions.
- **`actions`**: An `ActionChains` instance for performing complex actions on web page elements.
- **`by_mapping`**: A dictionary that maps string representations of locators to Selenium `By` objects.

### Class Methods

1. **`__init__(self, driver, *args, **kwargs)`**

   The class constructor initializes the WebDriver and `ActionChains`:

   ```python
   def __init__(self, driver, *args, **kwargs):
       self.driver = driver
       self.actions = ActionChains(driver)
   ```

2. **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**

   The main method for performing actions based on the locator:

   ```python
   def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
       ...
   ```

3. ... (other methods are listed)
```

## <algorithm>

(Diagram omitted here due to limitations.  A Mermaid diagram would be needed and is provided in the <mermaid> section).

**Conceptual Algorithm (for execute_locator):**

1. **Input:**  `locator` (dictionary), `message` (optional), `typing_speed` (optional), `continue_on_error` (optional).
2. **Check Locator Structure:** Validate the format of the `locator` dictionary.
3. **Retrieve Element:** Use `get_webelement_by_locator` to find the element(s) using the locator's criteria.
4. **Perform Action:**
   * **If `event` is present:**
      * Identify the action to be performed (e.g., `click()`, `send_keys()`).
      * Perform the action using the WebDriver or `ActionChains` based on `event`'s value.
   * **If `attribute` is present:**
      * Retrieve the attribute using `get_attribute_by_locator`.
5. **Error Handling:** If errors occur (e.g., element not found, timeout), handle them based on `continue_on_error`.
6. **Output:**  Return the result of the action or attribute retrieval.  This could be a string, a list of elements, a WebElement, or boolean (indicating success/failure).

## <mermaid>

```mermaid
graph TD
    A[ExecuteLocator] --> B{Validate locator};
    B -- Valid -- C[get_webelement_by_locator];
    B -- Invalid -- D[Handle Error];
    C --> E{Perform action?};
    E -- Yes -- F[performAction];
    E -- No -- G[getAttribute];
    F --> H[Return result];
    G --> I[Return result];
    D --> J[Return Error];
    subgraph Selenium Interactions
        F --> K[Element Click/Send Keys/Other];
        K --> L[WebDriver/ActionChains];
    end
    subgraph Exception Handling
        D --> M{continue_on_error};
        M -- True -- N[Continue];
        M -- False -- O[Stop and Log Error];
    end

    H --> P[Output];
    I --> P[Output];
    J --> P[Output];
```

**Dependencies:**

* **`selenium`**: Core library for interacting with web browsers.
* **`src`**: Internal project modules.
* **`gs`**: Likely a settings module.
* **`utils.printer`**: Utility functions for printing and potentially saving data.
* **`logger`**: Logging module for debugging and error reporting.
* **`logger.exceptions`**: Custom exceptions for the project.

## <explanation>

**Imports:**

The imports include Selenium libraries for web driver interaction (`webdriver`, `Keys`, `By`, `WebElement`, `WebDriverWait`, `EC`, `ActionChains`), and custom modules for data handling, logging, and exception management within the project (`src`, `gs`, `utils.printer`, `logger`, `logger.exceptions`).  This structure suggests a well-organized project with clear responsibilities for various aspects of the automation process.

**Classes:**

* **`ExecuteLocator`**: This class encapsulates the logic for interacting with web elements based on locator dictionaries.  Its key attributes (`driver`, `actions`, `by_mapping`) are essential for controlling the browser and identifying elements on the page.  The methods within this class handle the core operations (finding elements, sending messages, evaluating locators).

**Functions:**

* **`__init__`**: Initializes the class with a `driver` and `ActionChains` instance. This sets up the necessary resources for interaction.
* **`execute_locator`**: This is the main entry point, taking a `locator` dictionary and optional parameters for messages, typing speed, and error handling. It orchestrates the actions based on the configuration and returns the result.
* **`get_webelement_by_locator`**: Finds elements on the page.  It's crucial for retrieving elements based on provided locators.
* **`get_attribute_by_locator`**: Gets attributes from located elements, essential for extracting information from the page.
* **`_get_element_attribute`**: A helper function for getting single attributes from a `WebElement`.
* **`send_message`**: Sends messages (likely text input) to the found elements, potentially simulating typing.
* **`evaluate_locator`**: Evaluates the locator's attributes (e.g., `selector`).  This likely handles dynamic parts of the locator.
* **`_evaluate`**: A helper function for evaluating individual locator attributes.
* **`get_locator_keys`**: Returns available locator types (static method).

**Variables:**

Locator dictionaries (`locator`) contain the instructions for identifying web elements and performing actions on them.  Data types like `WebElement` are central to interacting with the browser through Selenium.

**Possible Errors/Improvements:**

* **Robust Error Handling:**  While the code includes error handling, more specific exception handling (e.g., checking for `StaleElementReferenceException`) could improve resilience.
* **Clearer Validation:** More explicit validation of the `locator` dictionary's structure could prevent unexpected behavior.
* **Logging:** More detailed logging within methods could enhance debugging and provide insights into the process.
* **Data Structure Design:** Refactoring the locator format for better readability (using namedtuples or classes) might improve maintainability, especially as the locators become more complex.

**Relationship with Other Parts of the Project:**

The `ExecuteLocator` class depends on the `Driver` and `Chrome` classes (likely from the `src.webdriver.driver` module) for the browser instance, indicating that this module is a part of a larger framework for web automation.  The `src.utils.printer` suggests this might be part of a broader automation framework that also handles data output and storage.