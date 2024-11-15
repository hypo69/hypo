## \file hypotez/src/webdriver/firefox/_docs/firefox.md
# -*- coding: utf-8 -*-

""" module: src.webdriver.firefox._docs """
MODE = 'debug'
#### Firefox versions:
Чтобы установить standalone версию Firefox, выполните следующие шаги:

[versions](https://support.mozilla.org/en-US/kb/install-older-version-firefox?redirectslug=install-older-version-of-firefox&redirectlocale=en-US#:~:text=Please%20note%2C%20however%2C%20that%20using%20older,use%20the%20newest%20version%20of%20Firefox.&text=Please%20note%2C%20however%2C%20that,newest%20version%20of%20Firefox.&text=however%2C%20that%20using%20older,use%20the%20newest%20version)

1. Перейдите на сайт [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/all/#product-desktop-beta) и скачайте версию браузера, которая вам подходит.

2. Используйте 7-ZIP для распаковки скачанного архива. Для этого:
   - Установите 7-ZIP, если он еще не установлен. Скачать можно [здесь](https://www.7-zip.org/).
   - Откройте скачанный архив с помощью 7-ZIP. 

3. После открытия архива найдите и извлеките содержимое папки `core` в `bin\webdrivers\firefox\ff\<version> для вас место на компьютере.


```python

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

from __init__ import gs
from src.utils import j_loads_ns
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
  
    def _set_options(self, settings: SimpleNamespace) -> Options:
        """ Launch options for the Firefox webdriver.
        @param settings `SimpleNamespace`: Settings for the Firefox options.
        @returns selenium.webdriver.firefox.options.Options: An Options object with the specified launch options.
        """
        options = Options()
        
        if settings.options:
            for opt in settings.options:
                if 'headless' in opt:
                    options.headless = True
                else:
                    options.add_argument(opt)
        
        if settings.headers:
            [options.add_argument(f"--{key}={value}") for key, value in settings.headers.items()]
            
        return options

    def _set_profile(self, profile: SimpleNamespace) -> FirefoxProfile:
        """ Sets up a Firefox profile for the webdriver.
        @param profile `SimpleNamespace`: A SimpleNamespace object containing profile settings.
        @returns FirefoxProfile: A FirefoxProfile object representing the profile.
        """
        
        profile_directory = profile.profile_path[profile.default_profile_from]
        if '%APPDATA%' in profile_directory:
            profile_directory = Path(profile_directory.replace('%APPDATA%', os.environ.get('APPDATA')))
            profile_directory = Path(profile_directory / profile.default_profile_directory[0])
        else:
            profile_directory = Path(gs.path.src / 'webdriver' / 'firefox' / 'profiles' / profile.default_profile_directory[0])

        profile = FirefoxProfile(profile_directory=str(profile_directory))
        return profile
```

### Обновленный файл `firefox.md`

```markdown
# Firefox WebDriver

## Overview

This code defines a subclass of `webdriver.Firefox` called `Firefox`. It provides additional functionality such as the ability to launch Firefox in kiosk mode and the ability to set up a Firefox profile for the webdriver.

## Class: Firefox

### Attributes

- `driver_name`: A class attribute set to `'firefox'`.

### Methods

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

Initializes the Firefox webdriver with the specified launch options and profile.

- **Parameters:**
  - `user_agent` (`dict`, optional): A dictionary containing user agent settings. If not provided, a random user agent is generated.

#### `_set_options(self, settings: SimpleNamespace) -> Options`

Sets the launch options for the Firefox webdriver.

- **Parameters:**
  - `settings` (`SimpleNamespace`): Settings for the Firefox options.

- **Returns:**
  - `Options`: An Options object with the specified launch options.

#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

Sets up a Firefox profile for the webdriver.

- **Parameters:**
  - `profile` (`SimpleNamespace`): A SimpleNamespace object containing profile settings.

- **Returns:**
  - `FirefoxProfile`: A FirefoxProfile object representing the profile.

## Usage

### Creating a Profile with User Agent

```python
profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "user-agent-string")
```

### Disabling Images

```python
profile = FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
```

### Blocking Pop-up Windows

```python
profile = FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
```

### Setting File Download Path

```python
profile = FirefoxProfile()
profile.set_preference("browser.download.dir", "/path/to/download/folder")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
```

### Disabling Browser Notifications

```python
profile = FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
```

## Options Examples

### Launching in Headless Mode

```python
options = Options()
options.headless = True
```

### Setting Browser Language

```python
options = Options()
options.add_argument('-lang=es')
```

### Custom Command Line Parameters

```python
options = Options()
options.add_argument('--some-option=value')
```

### Managing Debug Messages

```python
options = Options()
options.add_argument('-vv')
```

### Launching in Fullscreen Mode

```python
options = Options()
options.add_argument('--kiosk')
```

## Links

- [Documentation on Firefox Profile Settings](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Documentation on Firefox Options](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)
```

Теперь `profile` правильно определяется как `SimpleNamespace`, и обновленный файл документации включает всю необходимую информацию.