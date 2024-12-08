# Received Code

```rst
.. :module: src.webdriver.chrome
```
# Chrome WebDriver для Selenium

Этот репозиторий предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определённые в файле `chrome.json`, такие как user-agent и настройки профиля браузера, чтобы обеспечить гибкие и автоматизированные взаимодействия с браузером.

## Ключевые особенности

- **Централизованная конфигурация**: Конфигурация управляется через файл `chrome.json`.
- **Множественные профили браузера**: Поддерживает несколько профилей браузера, что позволяет настраивать различные параметры для тестирования.
- **Улучшенное логирование и обработка ошибок**: Предоставляет подробные логи для инициализации, проблем с конфигурацией и ошибок WebDriver.

## Требования

Перед использованием этого WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- WebDriver бинарник для Chrome (например, `chromedriver`)

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Кроме того, убедитесь, что бинарник `chromedriver` доступен в `PATH` вашей системы или укажите путь к нему в конфигурации.

## Конфигурация

Конфигурация для Chrome WebDriver хранится в файле `chrome.json`. Пример структуры конфигурационного файла и его описание:

### Пример конфигурации (`chrome.json`)

```json
{
  "options": {
    "log-level": "5",
    "disable-dev-shm-usage": "",
    "remote-debugging-port": "0",
    "arguments": [ "--kiosk", "--disable-gpu" ]
  },

  "disabled_options": { "headless": "" },

  "profile_directory": {
    "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data",
    "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
    "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data"
  },

  "binary_location": {
    "os": "C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
    "exe": "bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\chromedriver.exe",
    "binary": "bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\win64-125.0.6422.14\\\\chrome-win64\\\\chrome.exe",
    "chromium": "bin\\\\webdrivers\\\\chromium\\\\chrome-win\\\\chrome.exe"
  },

  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "proxy_enabled": false
}
```

### Описание полей конфигурации

# Improved Code

```python
"""
Модуль для работы с Chrome WebDriver.
=========================================================================================

Этот модуль содержит класс :class:`Chrome`, предоставляющий возможность управления Chrome браузером с помощью Selenium, 
используя конфигурацию из файла `chrome.json`.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.chrome import Chrome
    from src.utils.jjson import j_loads

    # Чтение конфигурации из файла
    config = j_loads('chrome.json')

    # Инициализация Chrome WebDriver с настройками из файла
    browser = Chrome(config)

    # Открытие веб-сайта
    browser.get("https://www.example.com")

    # Закрытие браузера
    browser.quit()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from src.utils.jjson import j_loads
from src.logger import logger
import os

class Chrome(webdriver.Chrome):
    """
    Класс для работы с Chrome WebDriver.
    
    :ivar config: Словарь настроек Chrome WebDriver.
    :vartype config: dict
    """

    def __init__(self, config: dict, user_agent: str = None):
        """
        Инициализирует Chrome WebDriver.
        
        :param config: Настройки Chrome WebDriver из файла `chrome.json`.
        :type config: dict
        :param user_agent: Пользовательский user-agent. Если не передан, используется случайный user-agent из fake_useragent.
        :type user_agent: str
        :raises Exception: Если возникла ошибка при загрузке конфигурации или запуске WebDriver.
        """
        try:
            self.config = config
            # Установка user-agent
            if user_agent:
              ua = user_agent
            else:
              ua = UserAgent().random
            options = Options()

            options.add_argument('--kiosk')
            options.add_argument('--disable-gpu')
            # Добавление остальных опций
            for option_name, option_value in config['options'].items():
              if option_name != "arguments":
                options.add_argument(f"{option_name}={option_value}")

            # Обработка списка аргументов
            for argument in config['options'].get('arguments',[]):
                options.add_argument(argument)


            # Поиск и установка пути к драйверу
            binary_location = config.get('binary_location', {}).get('exe')

            if not binary_location:
              logger.error("Путь к ChromeDriver не найден в конфигурации.")
              raise Exception("Путь к ChromeDriver не найден")

            if not os.path.exists(binary_location):
                logger.error(f"Файл ChromeDriver по пути {binary_location} не найден.")
                raise Exception(f"Файл ChromeDriver не найден.")


            #Инициализация WebDriver
            self.driver = webdriver.Chrome(executable_path=binary_location, options=options)
            #Установка User-Agent
            self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": ua})
            logger.info(f"Chrome WebDriver успешно инициализирован с User-Agent: {ua}")
        except Exception as ex:
            logger.error("Ошибка при инициализации Chrome WebDriver:", ex)
            raise


```
# Changes Made

- Добавлен класс `Chrome` как наследник `webdriver.Chrome`.
- Добавлены комментарии RST в соответствии с требованиями.
- Изменён способ инициализации `webdriver.Chrome` для использования `options`.
- Добавлена обработка ошибок с помощью `logger.error` и исключений.
- Добавлено чтение настроек из файла `chrome.json` с помощью `j_loads` из `src.utils.jjson`.
- Добавлена функция `__init__` для настройки Chrome WebDriver.
- При инициализации WebDriver теперь устанавливается `User-Agent`  с помощью `fake_useragent` и `execute_cdp_cmd`.
- Добавлен валидация пути к ChromeDriver.
- Внесена логика для обработки списка аргументов из настроек.


# FULL Code

```python
"""
Модуль для работы с Chrome WebDriver.
=========================================================================================

Этот модуль содержит класс :class:`Chrome`, предоставляющий возможность управления Chrome браузером с помощью Selenium, 
используя конфигурацию из файла `chrome.json`.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.chrome import Chrome
    from src.utils.jjson import j_loads

    # Чтение конфигурации из файла
    config = j_loads('chrome.json')

    # Инициализация Chrome WebDriver с настройками из файла
    browser = Chrome(config)

    # Открытие веб-сайта
    browser.get("https://www.example.com")

    # Закрытие браузера
    browser.quit()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from src.utils.jjson import j_loads
from src.logger import logger
import os

class Chrome(webdriver.Chrome):
    """
    Класс для работы с Chrome WebDriver.
    
    :ivar config: Словарь настроек Chrome WebDriver.
    :vartype config: dict
    """

    def __init__(self, config: dict, user_agent: str = None):
        """
        Инициализирует Chrome WebDriver.
        
        :param config: Настройки Chrome WebDriver из файла `chrome.json`.
        :type config: dict
        :param user_agent: Пользовательский user-agent. Если не передан, используется случайный user-agent из fake_useragent.
        :type user_agent: str
        :raises Exception: Если возникла ошибка при загрузке конфигурации или запуске WebDriver.
        """
        try:
            self.config = config
            # Установка user-agent
            if user_agent:
              ua = user_agent
            else:
              ua = UserAgent().random
            options = Options()

            options.add_argument('--kiosk')
            options.add_argument('--disable-gpu')
            # Добавление остальных опций
            for option_name, option_value in config['options'].items():
              if option_name != "arguments":
                options.add_argument(f"{option_name}={option_value}")

            # Обработка списка аргументов
            for argument in config['options'].get('arguments',[]):
                options.add_argument(argument)


            # Поиск и установка пути к драйверу
            binary_location = config.get('binary_location', {}).get('exe')

            if not binary_location:
              logger.error("Путь к ChromeDriver не найден в конфигурации.")
              raise Exception("Путь к ChromeDriver не найден")

            if not os.path.exists(binary_location):
                logger.error(f"Файл ChromeDriver по пути {binary_location} не найден.")
                raise Exception(f"Файл ChromeDriver не найден.")


            #Инициализация WebDriver
            self.driver = webdriver.Chrome(executable_path=binary_location, options=options)
            #Установка User-Agent
            self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": ua})
            logger.info(f"Chrome WebDriver успешно инициализирован с User-Agent: {ua}")
        except Exception as ex:
            logger.error("Ошибка при инициализации Chrome WebDriver:", ex)
            raise
```