# pw_executor.py

## Overview

This module defines the `pw_executor` class for handling Playwright interactions.  It encapsulates the execution of Playwright-based tests.


## Table of Contents

* [pw_executor](#pw_executor)


## Classes

### `pw_executor`

**Description**: This class provides methods for controlling Playwright browser instances and managing test executions.


**Methods**:

#### `__init__`

```python
def __init__(self, config: dict) -> None:
    """
    Args:
        config (dict): Configuration parameters for the Playwright instance.

    Returns:
        None
    """
```

#### `start_browser`

```python
def start_browser(self) -> None:
    """
    Starts the Playwright browser instance.

    Returns:
        None
    """
```

#### `stop_browser`

```python
def stop_browser(self) -> None:
    """
    Stops the Playwright browser instance.

    Returns:
        None
    """
```


#### `run_tests`

```python
def run_tests(self, test_cases: list) -> dict:
    """
    Runs the specified Playwright test cases.

    Args:
        test_cases (list): A list of test case names or paths.

    Returns:
        dict: A dictionary containing the results of the test execution.
    
    Raises:
        Exception: Any exception encountered during test execution.
    """
```

#### `report`


```python
def report(self) -> None:
    """
    Generates and displays a report of the executed tests.

    Returns:
        None
    """
```


## Global Variables

### `MODE`

```python
MODE = 'dev'
```

**Description**: Stores the execution mode of the application (e.g., 'dev', 'prod').



```