# Firefox WebDriver

## <input code>

```python
#### Firefox versions:
Чтобы установить standalone версию Firefox, выполните следующие шаги:

[versions](https://support.mozilla.org/en-US/kb/install-older-version-firefox?redirectslug=install-older-version-of-firefox&redirectlocale=en-US#:~:text=Please%20note%2C%20however%2C%20that%20using%20older,use%20the%20newest%20version%20of%20Firefox.&text=Please%20note%2C%20however%2C%20that,newest%20version%20of%20Firefox.&text=however%2C%20that%20using%20older,use%20the%20newest%20version)

1. Перейдите на сайт [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/all/#product-desktop-beta) и скачайте версию браузера, которая вам подходит.

2. Используйте 7-ZIP для распаковки скачанного архива. Для этого:
   - Установите 7-ZIP, если он еще не установлен. Скачать можно [здесь](https://www.7-zip.org/).
   - Откройте скачанный архив с помощью 7-ZIP.

3. После открытия архива найдите и извлеките содержимое папки `core` в `bin\\webdrivers\\firefox\\ff\\<version> для вас место на компьютере.



""" вебдрайвер Firefox

 This code defines a subclass of webdriver.Firefox called Firefox. 
 It provides additional functionality such as the ability to launch Firefox 
 in kiosk mode and the ability to set up a Firefox profile for the webdriver.

 @details класс webdriver.Firefox 
 @image html class_firefox.png
 @section libs imports:
  - pathlib 
  - attr 
  - os 
  - selenium.webdriver 
  - selenium.webdriver.firefox.options 
  - selenium.webdriver.firefox.service 
  - selenium.webdriver.firefox.firefox_profile 
  - selenium.common.exceptions 
  - gs 
  - gs 
  - gs 
"""

import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, Any
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException
from fake_useragent import UserAgent

from src import gs
from src.utils.jjson import j_loads_ns
from src.logger import logger

class Firefox(WebDriver):
    """ Subclass of `webdriver.Firefox` that provides additional functionality."""

    driver_name = 'firefox'

    def __init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None:
        """ Initializes the Firefox webdriver with the specified launch options and profile.
        @param user_agent `dict`: A dictionary containing user agent settings.
        """
        self.user_agent = user_agent if user_agent else UserAgent().random       

        settings: SimpleNamespace = j_loads_ns(Path(gs.path.src, 'webdriver', 'firefox', 'firefox.json'))

        geckodriver_path_parts: list[str] = settings.geckodriver
        geckodriver_path: str = str(Path(gs.path.bin, *geckodriver_path_parts))

        profile: FirefoxProfile = self._set_profile(settings.profile)
        options: Options = self._set_options(settings)

        service = Service(geckodriver_path)

        if profile:
            options.profile = profile

        try:
            logger.info("Start Firefox")
            super().__init__(options=options, service=service)
        except WebDriverException as ex:
            logger.critical(f"""
                ---------------------------------
                    Не поднялся драйвер
                    так бывает при обновлениях самого Firefox
                    ну, или он не установлен в ос.
            ----------------------------------""", ex)
            return
        except Exception as ex:
            logger.critical(f' Упал webdriver Firefox. Общая ошибка:  {ex}')
            return


    # ... (rest of the code)
```

## <algorithm>

N/A - The provided code snippet is primarily a class definition, not a procedural algorithm. The algorithm is implicit in the method calls and data flows within the class.

## <mermaid>

```mermaid
graph TD
    subgraph WebDriver Initialization
        A[Firefox Class] --> B{__init__};
        B --> C[Load Settings];
        C --> D[Get Geckodriver Path];
        C --> E[Get Firefox Profile];
        C --> F[Get Firefox Options];
        E --> G[Set Profile];
        F --> H[Set Options];
        G -- Profile -- E;
        H -- Options -- F;
        D --> I[Create Service];
        G --> I;
        H --> I;
        I --> J[Initialize WebDriver];
    end
    J --> K[Start Firefox];
    subgraph Error Handling
        J -- Exception -- L{WebDriverException};
        J -- Exception -- M{Exception};
        L --> N[Log Critical Error];
        M --> O[Log Critical Error];
    end
```

**Dependencies Analysis:**

- `pathlib`: For path manipulation.
- `types`: For `SimpleNamespace` type.
- `typing`: For type hinting (`Optional`, `Any`).
- `selenium.webdriver`: Core Selenium WebDriver library.
- `selenium.webdriver.firefox.*`: Specific modules for Firefox WebDriver functionality.
- `selenium.common.exceptions`: Exceptions related to Selenium WebDriver.
- `fake_useragent`: For generating user agents.
- `src.gs`: Likely a custom module for global settings or paths.
- `src.utils.jjson`: For loading JSON data into `SimpleNamespace` objects.
- `src.logger`: For logging messages.

## <explanation>

**Imports:**

- `os`, `pathlib`: Standard Python modules for interacting with the operating system and paths.
- `types.SimpleNamespace`: A lightweight class that acts like a dictionary, useful for representing configuration objects.
- `typing.Optional`, `typing.Any`: Types from `typing` for type hints, making the code more readable and maintainable.
- `selenium.webdriver`, `selenium.webdriver.firefox.*`: Parts of the Selenium library for interacting with web browsers, specifically Firefox.  Critically, these provide the necessary components for creating and controlling a Firefox webdriver instance.
- `selenium.common.exceptions`: Used for handling potential exceptions during WebDriver interaction.
- `fake_useragent`: Generates realistic user agent strings.
- `src.gs`, `src.utils.jjson`, `src.logger`: Modules from the `src` package; `gs` likely handles global settings, `jjson` parses JSON, and `logger` manages logging. The specific role of these within the project is not entirely clear from the code.

**Classes:**

- `Firefox`: A subclass of `selenium.webdriver.Firefox`. It extends the base class to provide additional functionality.  The crucial additions are the `__init__` method and profile handling. This enhanced class is likely to be used in testing or automation scripts to customize the Firefox webdriver setup, handling profile configurations and error conditions during the initialization process.
- `WebDriver`: The base class for web drivers in Selenium.


**Methods:**

- `__init__`: Initializes the Firefox WebDriver. This method is designed to set up the webdriver with specific options, a profile (for persistent user data), and the geckodriver. Importantly, it incorporates error handling (`try...except`) to catch potential issues during initialization, which is vital in robust automation.
- `_set_options`: Configures the Firefox launch options. This method handles headless mode, custom arguments, and headers, ensuring that the webdriver starts with the desired parameters. This allows for creating a Firefox driver instance with customized settings.
- `_set_profile`: Creates and configures a Firefox profile. This is crucial for managing persistent browser settings, such as cookies, extensions, and history. It effectively initializes a user profile for the Firefox browser.

**Functions:**

- `j_loads_ns`: Takes the JSON configuration and transforms it to a `SimpleNamespace` object for easier access to settings.  It's a useful helper function that simplifies accessing JSON data.


**Variables:**

- `user_agent`: Stores the user-agent string used by the webdriver.  Crucially, it supports customization by allowing external dictionaries to be passed in.
- `settings`: Holds the configuration for Firefox.
- `geckodriver_path`: Path to the geckodriver executable.
- `profile`, `options`, `service`: Objects related to the Firefox profile, launch options, and the webdriver service, respectively.


**Potential Errors/Improvements:**

- **Error Handling:** The `try...except` block is good but could be improved by more specific exception handling. Different exceptions (e.g., `FileNotFoundError`) during geckodriver loading would provide more context.
- **Configuration:** Loading configurations from `firefox.json` is a good practice.  Consider adding validation to ensure that the expected keys and types are present in the file.
- **Logging:** The logging messages (`logger.info`, `logger.critical`) are informative, but potentially further information about failed driver startup (e.g., geckodriver version mismatch) could be added to help with debugging.

**Relationships with other parts of the project (`src`):**

The `gs`, `jjson`, and `logger` modules are from the `src` package, suggesting a larger project structure with reusable components and consistent logging mechanisms. The code likely forms part of a broader automation framework.