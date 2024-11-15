## \file hypotez/consultant/gemini/endpoints/advertisement/facebook/scenarios/switch_account.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.advertisement.facebook.scenarios """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.advertisement.facebook.scenarios """
""" Переключение на аккунт. 
Если есть кнопка `Переключить` - нажимаю её """


from pathlib import Path

from __init__ import gs
from src.webdriver import Driver
from src.utils import j_loads_ns

# Crucial: Check if the file exists before loading.
if not Path(gs.path.src, 'advertisement', 'facebook', 'locators', 'switch_account.json').exists():
    raise FileNotFoundError(
        f"Locator file 'switch_account.json' not found at {Path(gs.path.src, 'advertisement', 'facebook', 'locators', 'switch_account.json')}"
    )


locator = j_loads_ns(Path(gs.path.src, 'advertisement', 'facebook', 'locators', 'switch_account.json'))

def switch_account(driver: Driver):
    try:
        driver.execute_locator(locator.switch_to_account_button)
    except AttributeError as e:
        print(f"Error: 'switch_to_account_button' key not found in locator JSON: {e}")
    except Exception as e:
        print(f"Error switching account: {e}")

```

**Improvements and explanations:**

* **Error Handling:** The code now includes `try...except` blocks.  This is absolutely vital.  If the `switch_to_account_button` key isn't present in the JSON file, or if there's any other error during the process (e.g., the element isn't found on the page), the script won't crash.  Instead, it prints an informative error message, allowing you to debug it.  Crucially, it catches a general `Exception` in case an unexpected problem arises during the `driver.execute_locator` call.

* **File Existence Check:**  The code now checks if the `switch_account.json` file actually exists.  This prevents a cryptic `AttributeError` later if `locator` is not properly initialized.  It raises a `FileNotFoundError` with a descriptive message.  This is best practice.


* **Clear Error Messages:** The error messages are more specific, making it easier to pinpoint the problem.  Knowing *which* key is missing in the JSON is very helpful.


* **`gs` variable handling:** Assuming `gs.path.src` is a string representing the path to the project's source directory, it's likely to be correctly concatenated, but best practice would be to use `os.path.join` to construct the file path. This would make your code more portable across operating systems.

**Example `switch_account.json` (locators):**

```json
{
  "switch_to_account_button": {
    "selector": "css selector",
    "value": ".switch-account-button"
  }
}
```

**Important Considerations:**

* **`__init__.py`:**  Make sure you have `__init__.py` files in the appropriate directories in your project's structure to ensure proper package import recognition.


* **`gs` Variable:** The `gs` object and how it's used are not shown in the provided context.  If this `gs` object provides the project base directory or a similar concept, ensure it's correctly initialized and populated with the project path.


* **Error Logging:**  For production code, consider using a logging framework instead of `print`.  This allows you to configure the logging level (e.g., info, warning, error) and save logs to files for easier analysis.

With these changes, your code will be more robust, reliable, and easier to debug, especially in a production environment. Remember to replace the example `switch_account.json` with your actual locator values.
