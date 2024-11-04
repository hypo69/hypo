
### Module Overview

The `scenario` module is designed to automate the collection of information from web pages using Selenium WebDriver. It reads predefined scenarios from JSON files and directs the WebDriver to perform actions according to these scenarios. The gathered information can be of any type, encompassing everything that can be listed and cataloged.

### Directory Structure

- `__init__.py`: Initializes the module.
- `executor.py`: Contains the main logic for executing the scenarios using Selenium WebDriver.
- `version.py`: Manages the version information of the module.
- `_docs`: Contains documentation files in multiple languages.
- `_dot`: Contains DOT files for graph representations.
- `_examples`: Provides example scripts and markdown files demonstrating the usage of the module.
- `json`: Contains JSON files that define execution scenarios for different suppliers.

### Key Components

1. **Executor**
    - **Purpose**: Executes the scenarios defined in the JSON files.
    - **Functionality**:
        - Reads the scenario files.
        - Directs Selenium WebDriver to perform actions such as navigating to URLs, clicking elements, and extracting information.
        - Handles exceptions and logs errors for debugging purposes.

2. **Version Management**
    - **Purpose**: Manages the versioning of the module.
    - **Functionality**:
        - Defines the current version of the module.
        - Provides version information for compatibility and updates.

3. **Documentation and Examples**
    - **Purpose**: Provides detailed documentation and usage examples for developers.
    - **Functionality**:
        - Explains the functionality and usage of the `executor`.
        - Provides example scripts to demonstrate how to define and execute scenarios.

4. **JSON Scenarios**
    - **Purpose**: Defines the sequence of actions for the WebDriver to perform.
    - **Functionality**:
        - Contains lists of actions for different suppliers.
        - Specifies URLs, locators, and actions (e.g., click, extract text) for the WebDriver.

### Usage

To use the `scenario` module, follow these steps:

1. **Define a Scenario**:
    - Create a JSON file in the `json` directory with the sequence of actions.
    - Specify the URL and actions (e.g., navigate, click, extract) in the JSON file.

2. **Execute the Scenario**:
    - Use the `executor` to read the JSON file.
    - The `executor` directs the WebDriver to perform the actions specified in the JSON file.
    - The WebDriver navigates to the specified URL and performs the actions to gather information.

### Example Scenario

Here is an example of a JSON scenario file:

```json
{
    "supplier": "example",
    "actions": [
        {
            "type": "navigate",
            "url": "https://example.com"
        },
        {
            "type": "click",
            "locator": "//*[@id='login-button']"
        },
        {
            "type": "extract",
            "locator": "//*[@id='user-name']"
        }
    ]
}
```

### Example Usage

```python
from scenario.executor import Executor

# Initialize the executor with the path to the JSON scenario file
executor = Executor("json/example_scenario.json")

# Execute the scenario
executor.run()
```


<pre>
   +-----------+
  |  Scenario |
  +-----------+
        |
        | Defines
        |
        v
  +-----------+
  | Executor  |
  +-----------+
        |
        | Uses
        |
        v
  +-----------+        +-----------+
  |  Supplier | <----> |  Driver   |
  +-----------+        +-----------+
        |                     |
        | Provides Data        | Provides Interface
        |                     |
        v                     v
  +-----------+        +-----------+
  |  Prestashop       | Other Suppliers |
  +-----------+        +-----------+
</pre>

