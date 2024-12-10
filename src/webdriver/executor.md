```rst
.. module:: src.webdriver.excutor
```
[Русский](https://github.com/hypo69/hypo/blob/master/src/webdriver/executor.ru.md)

# `executor.py` Documentation

## Overview

The `executor.py` module is a part of the `src.webdriver` package and is designed to automate interactions with web elements using Selenium. This module provides a flexible and versatile framework for locating, interacting with, and extracting information from web elements based on provided configurations, known as "locators."

## Key Features

1. **Parsing and Handling Locators**: Converts dictionaries with configurations into `SimpleNamespace` objects, allowing for flexible manipulation of locator data.
2. **Interacting with Web Elements**: Performs various actions such as clicks, sending messages, executing events, and retrieving attributes from web elements.
3. **Error Handling**: Supports continuing execution in case of an error, enabling the processing of web pages with unstable elements or requiring a special approach.
4. **Support for Multiple Locator Types**: Handles both single and multiple locators, allowing the identification and interaction with one or several web elements simultaneously.

## Module Structure

### Classes

#### `ExecuteLocator`

This class is the core of the module, responsible for handling web element interactions based on provided locators.

- **Attributes**:
  - `driver`: The Selenium WebDriver instance.
  - `actions`: An `ActionChains` object for performing complex actions.
  - `by_mapping`: A dictionary mapping locator types to Selenium's `By` methods.
  - `mode`: The execution mode (`debug`, `dev`, etc.).

- **Methods**:
  - `__post_init__`: Initializes the `ActionChains` object if a driver is provided.
  - `execute_locator`: Executes actions on a web element based on the provided locator.
  - `evaluate_locator`: Evaluates and processes locator attributes.
  - `get_attribute_by_locator`: Retrieves attributes from an element or list of elements found by the given locator.
  - `get_webelement_by_locator`: Extracts web elements based on the provided locator.
  - `get_webelement_as_screenshot`: Takes a screenshot of the located web element.
  - `execute_event`: Executes the events associated with a locator.
  - `send_message`: Sends a message to a web element.

### Flow Diagrams

The module includes Mermaid flow diagrams to illustrate the flow of execution for key methods:

- **`execute_locator`**:
  ```mermaid
  graph TD
  Start[Start] --> CheckLocatorType[Check if locator is SimpleNamespace or dict]
  CheckLocatorType --> IsSimpleNamespace{Is locator SimpleNamespace?}
  IsSimpleNamespace -->|Yes| UseLocatorAsIs[Use locator as is]
  IsSimpleNamespace -->|No| ConvertDictToSimpleNamespace[Convert dict to SimpleNamespace]
  ConvertDictToSimpleNamespace --> UseLocatorAsIs
  UseLocatorAsIs --> DefineParseLocator[Define async function _parse_locator]
  DefineParseLocator --> CheckEventAttributeMandatory[Check if locator has event, attribute, or mandatory]
  CheckEventAttributeMandatory -->|No| ReturnNone[Return None]
  CheckEventAttributeMandatory -->|Yes| TryMapByEvaluateAttribute[Try to map by and evaluate attribute]
  TryMapByEvaluateAttribute --> CatchExceptionsAndLog[Catch exceptions and log if needed]
  CatchExceptionsAndLog --> HasEvent{Does locator have event?}
  HasEvent -->|Yes| ExecuteEvent[Execute event]
  HasEvent -->|No| HasAttribute{Does locator have attribute?}
  HasAttribute -->|Yes| GetAttributeByLocator[Get attribute by locator]
  HasAttribute -->|No| GetWebElementByLocator[Get web element by locator]
  ExecuteEvent --> ReturnEventResult[Return result of event]
  GetAttributeByLocator --> ReturnAttributeResult[Return attribute result]
  GetWebElementByLocator --> ReturnWebElementResult[Return web element result]
  ReturnEventResult --> ReturnFinalResult[Return final result of _parse_locator]
  ReturnAttributeResult --> ReturnFinalResult
  ReturnWebElementResult --> ReturnFinalResult
  ReturnFinalResult --> ReturnExecuteLocatorResult[Return result of execute_locator]
  ReturnExecuteLocatorResult --> End[End]
  ```

- **`evaluate_locator`**:
  ```mermaid
  graph TD
  Start[Start] --> CheckIfAttributeIsList[Check if attribute is list]
  CheckIfAttributeIsList -->|Yes| IterateOverAttributes[Iterate over each attribute in list]
  IterateOverAttributes --> CallEvaluateForEachAttribute[Call _evaluate for each attribute]
  CallEvaluateForEachAttribute --> ReturnGatheredResults[Return gathered results from asyncio.gather]
  CheckIfAttributeIsList -->|No| CallEvaluateForSingleAttribute[Call _evaluate for single attribute]
  CallEvaluateForSingleAttribute --> ReturnEvaluateResult[Return result of _evaluate]
  ReturnEvaluateResult --> End[End]
  ReturnGatheredResults --> End
  ```

- **`get_attribute_by_locator`**:
  ```mermaid
  graph TD
  Start[Start] --> CheckIfLocatorIsSimpleNamespaceOrDict[Check if locator is SimpleNamespace or dict]
  CheckIfLocatorIsSimpleNamespaceOrDict -->|Yes| ConvertLocatorToSimpleNamespaceIfNeeded[Convert locator to SimpleNamespace if needed]
  ConvertLocatorToSimpleNamespaceIfNeeded --> CallGetWebElementByLocator[Call get_webelement_by_locator]
  CallGetWebElementByLocator --> CheckIfWebElementIsFound[Check if web_element is found]
  CheckIfWebElementIsFound -->|No| LogDebugMessageAndReturn[Log debug message and return]
  CheckIfWebElementIsFound -->|Yes| CheckIfAttributeIsDictionaryLikeString[Check if locator.attribute is a dictionary-like string]
  CheckIfAttributeIsDictionaryLikeString -->|Yes| ParseAttributeStringToDict[Parse locator.attribute string to dict]
  ParseAttributeStringToDict --> CheckIfWebElementIsList[Check if web_element is a list]
  CheckIfWebElementIsList -->|Yes| RetrieveAttributesForEachElementInList[Retrieve attributes for each element in list]
  RetrieveAttributesForEachElementInList --> ReturnListOfAttributes[Return list of attributes]
  CheckIfWebElementIsList -->|No| RetrieveAttributesForSingleWebElement[Retrieve attributes for a single web_element]
  RetrieveAttributesForSingleWebElement --> ReturnListOfAttributes
  CheckIfAttributeIsDictionaryLikeString -->|No| CheckIfWebElementIsListAgain[Check if web_element is a list]
  CheckIfWebElementIsListAgain -->|Yes| RetrieveAttributesForEachElementInListAgain[Retrieve attributes for each element in list]
  RetrieveAttributesForEachElementInListAgain --> ReturnListOfAttributesOrSingleAttribute[Return list of attributes or single attribute]
  CheckIfWebElementIsListAgain -->|No| RetrieveAttributeForSingleWebElementAgain[Retrieve attribute for a single web_element]
  RetrieveAttributeForSingleWebElementAgain --> ReturnListOfAttributesOrSingleAttribute
  ReturnListOfAttributesOrSingleAttribute --> End[End]
  LogDebugMessageAndReturn --> End
  ```

## Usage

To use this module, instantiate the `ExecuteLocator` class with a Selenium WebDriver instance and then call the various methods to interact with web elements based on the provided locators.

### Example

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

# Initialize the WebDriver
driver = webdriver.Chrome()

# Initialize the ExecuteLocator class
executor = ExecuteLocator(driver=driver)

# Define a locator
locator = {
    "by": "ID",
    "selector": "some_element_id",
    "event": "click()"
}

# Execute the locator
result = await executor.execute_locator(locator)
print(result)
```

## Dependencies

- `selenium`: For web automation.
- `asyncio`: For asynchronous operations.
- `re`: For regular expressions.
- `dataclasses`: For creating data classes.
- `enum`: For creating enumerations.
- `pathlib`: For handling file paths.
- `types`: For creating simple namespaces.
- `typing`: For type annotations.

## Error Handling

The module includes robust error handling to ensure that the execution continues even if certain elements are not found or if there are issues with the web page. This is particularly useful for handling dynamic or unstable web pages.

## Contributing

Contributions to this module are welcome. Please ensure that any changes are well-documented and include appropriate tests.

## License

This module is licensed under the MIT License. See the `LICENSE` file for more details.

---

This README provides a comprehensive overview of the `executor.py` module, including its purpose, structure, usage, and dependencies. It is intended to help developers understand and utilize the module effectively.