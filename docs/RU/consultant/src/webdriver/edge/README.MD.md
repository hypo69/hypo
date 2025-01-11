# Анализ кода модуля `src.webdriver.edge`

**Качество кода**

**8/10**
-  Плюсы
    -   Хорошее описание модуля и его функций.
    -   Наличие примеров конфигурационного файла `edge.json`.
    -   Описаны основные настройки и параметры.
    -   Присутствует пример использования WebDriver.
    -   Упоминается использование паттерна Singleton.
    -   Детализировано логирование и отладка.
    -   Указана лицензия.
-   Минусы
    -   Отсутствует информация о классах и функциях внутри модуля, что затрудняет понимание внутренней структуры.
    -   Не приведены примеры документации RST для кода.
    -   Не хватает подробных docstring для функций и классов.
    -   Нет примеров обработки исключений и логирования ошибок в коде.
    -   Не все рекомендации из инструкции соблюдены.

**Рекомендации по улучшению**
1.  **Добавить описание модуля в формате reStructuredText.**
    -   В начале файла добавить блок reStructuredText с описанием модуля, как указано в примере инструкции.
2.  **Добавить docstrings к функциям и классам.**
    -   Документировать все функции и классы с использованием docstring, как показано в примерах документации.
3.  **Указать все импорты.**
    -   Указать все необходимые импорты для модуля.
4.  **Привести имена переменных и функций в соответствие с ранее обработанными файлами.**
    -   Унифицировать имена переменных и функций.
5.  **Изменить формат кавычек на одинарные.**
     -  В коде использовать одинарные кавычки (`'`) вместо двойных (`"`).
6.  **Использовать `j_loads` для загрузки json.**
    -   Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
7.  **Улучшить логирование ошибок.**
    -   Использовать `logger.error` для обработки исключений и вывода сообщений об ошибках, избегая try-except.
8.  **Указать лицензию в reStructuredText.**
     -  В конце модуля добавить лицензию в формате reStructuredText.

**Оптимизированный код**

```python
"""
Модуль для управления Edge WebDriver с использованием Selenium.
=========================================================================================

Этот модуль предоставляет класс :class:`Edge`, который управляет экземпляром Edge WebDriver,
используя настройки из файла конфигурации `edge.json`. Модуль поддерживает
различные профили браузера, параметры командной строки и пользовательские заголовки.

Пример использования
--------------------

Пример инициализации и использования класса `Edge`:

.. code-block:: python

    from src.webdriver.edge import Edge

    # Инициализация Edge WebDriver с пользовательским user-agent и параметрами
    browser = Edge(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)', options=['--headless', '--disable-gpu'])

    # Открытие веб-сайта
    browser.get('https://www.example.com')

    # Закрытие браузера
    browser.quit()
"""
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from fake_useragent import UserAgent
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger
import os

_instance = None

class Edge:
    """
    Класс для управления Edge WebDriver с использованием Selenium.

    Этот класс обеспечивает настройку и управление Edge WebDriver,
    используя конфигурацию из файла `edge.json`. Поддерживает
    различные профили браузера, параметры командной строки и
    пользовательские заголовки.

    Attributes:
        driver (webdriver.Edge): Экземпляр Edge WebDriver.
    """
    def __new__(cls, *args, **kwargs):
        """
        Реализация паттерна Singleton для класса Edge.

        Если экземпляр класса уже существует, возвращает существующий,
        иначе создает новый экземпляр.

        Returns:
            Edge: Экземпляр класса Edge.
        """
        global _instance
        if not _instance:
            _instance = super(Edge, cls).__new__(cls)
        else:
            _instance.driver.execute_script("window.open();")  # Открываем новое окно если браузер уже запущен
        return _instance
    
    def __init__(self, user_agent: str = None, options: list = None):
        """
        Инициализирует Edge WebDriver с заданными настройками.

        Args:
            user_agent (str, optional): Пользовательский user-agent. Defaults to None.
            options (list, optional): Список дополнительных опций Edge. Defaults to None.
        """
        self.driver = None
        self.config = self._load_config()
        self.user_agent = user_agent
        self.options = options or []
        self._init_driver()

    def _load_config(self) -> dict:
        """
        Загружает конфигурацию из файла `edge.json`.

        Returns:
            dict: Словарь с конфигурационными настройками.
        """
        try:
            config_path = Path(__file__).parent / 'edge.json'
            with open(config_path, 'r', encoding='utf-8') as f:
                config = j_loads(f)
            return config
        except FileNotFoundError as e:
             logger.error(f'Конфигурационный файл `edge.json` не найден: {e}')
             return {}
        except Exception as e:
            logger.error(f'Ошибка при загрузке конфигурации из `edge.json`: {e}')
            return {}

    def _init_driver(self):
        """
        Инициализирует и настраивает Edge WebDriver.

        Применяет настройки из конфигурационного файла, пользовательские
        настройки и запускает WebDriver.
        """
        edge_options = EdgeOptions()

        if self.config and self.config.get('options'):
            # Добавляем опции из конфигурационного файла.
            for option in self.config.get('options'):
                edge_options.add_argument(option)
        
        if self.options:
             # Добавляем дополнительные опции если есть
            for option in self.options:
                edge_options.add_argument(option)

        if self.config and self.config.get('profiles') and self.config.get('profiles').get('os'):
            # Устанавливаем путь к профилю, если он задан в конфиге
             user_data_dir = self.config['profiles']['os']
             if '%LOCALAPPDATA%' in user_data_dir:
                 user_data_dir = user_data_dir.replace('%LOCALAPPDATA%', os.getenv('LOCALAPPDATA'))
             edge_options.add_argument(f'user-data-dir={user_data_dir}')

        if self.user_agent:
            # Устанавливаем user-agent, если он передан
            edge_options.add_argument(f'--user-agent={self.user_agent}')
        elif self.config and self.config.get('headers') and self.config.get('headers').get('User-Agent'):
            # Устанавливаем user-agent из конфига, если он там есть
           edge_options.add_argument(f'--user-agent={self.config["headers"]["User-Agent"]}')
        else:
            #  Генерируем user-agent если его нет
            ua = UserAgent()
            user_agent = ua.random
            edge_options.add_argument(f'--user-agent={user_agent}')

        if self.config and self.config.get('executable_path') and self.config.get('executable_path').get('default'):
             # Устанавливаем путь к исполняемому файлу драйвера если он задан в конфиге
             executable_path = self.config['executable_path']['default']
             try:
                  self.driver = webdriver.Edge(options=edge_options, executable_path=executable_path)
             except Exception as e:
                 logger.error(f'Ошибка при инициализации Edge WebDriver: {e}')
        else:
            try:
                 self.driver = webdriver.Edge(options=edge_options)
            except Exception as e:
                 logger.error(f'Ошибка при инициализации Edge WebDriver: {e}')

        if not self.driver:
            logger.error('Не удалось инициализировать Edge WebDriver.')

    def get(self, url: str):
        """
        Открывает URL в браузере.

        Args:
            url (str): URL для открытия.
        """
        if self.driver:
            self.driver.get(url)
        else:
            logger.error('Драйвер не инициализирован. Невозможно открыть URL.')

    def quit(self):
        """
        Закрывает браузер и завершает сессию WebDriver.
        """
        if self.driver:
            self.driver.quit()
            global _instance
            _instance = None #  Сбрасываем синглтон
        else:
             logger.error('Драйвер не инициализирован. Нечего закрывать.')
"""
This module provides a custom implementation of the Edge WebDriver using Selenium. It integrates configuration settings defined in the `edge.json` file, such as user-agent and browser profile settings, to enable flexible and automated browser interactions.

Key Features:

- Centralized Configuration: Configuration is managed via the `edge.json` file.
- Multiple Browser Profiles: Supports multiple browser profiles, allowing you to configure different settings for testing.
- Enhanced Logging and Error Handling: Provides detailed logs for initialization, configuration issues, and WebDriver errors.
- Ability to Pass Custom Options: Supports passing custom options during WebDriver initialization.

Requirements:

Before using this WebDriver, ensure the following dependencies are installed:

- Python 3.x
- Selenium
- Fake User Agent
- Edge WebDriver binary (e.g., `msedgedriver`)

Install the required Python dependencies:

```bash
pip install selenium fake_useragent
```

Additionally, ensure the `msedgedriver` binary is available in your system's `PATH` or specify its path in the configuration.

Configuration:

The configuration for the Edge WebDriver is stored in the `edge.json` file. Below is an example structure of the configuration file and its description:

Example Configuration (`edge.json`):

```json
{
  "options": [
    "--disable-dev-shm-usage",
    "--remote-debugging-port=0"
  ],
  "profiles": {
    "os": "%LOCALAPPDATA%\\\\Microsoft\\\\Edge\\\\User Data\\\\Default",
    "internal": "webdriver\\\\edge\\\\profiles\\\\default"
  },
  "executable_path": {
    "default": "webdrivers\\\\edge\\\\123.0.2420.97\\\\msedgedriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  }
}
```

Configuration Fields Description:

1. `options`: A list of command-line arguments passed to Edge. Examples:
   - `--disable-dev-shm-usage`: Disables the use of `/dev/shm` in Docker containers (useful to prevent errors in containerized environments).
   - `--remote-debugging-port=0`: Sets the port for remote debugging in Edge. A value of `0` means a random port will be assigned.

2. `profiles`: Paths to Edge user data directories for different environments:
   - `os`: Path to the default user data directory (typically for Windows systems).
   - `internal`: Internal path for the default WebDriver profile.

3. `executable_path`: Path to the Edge WebDriver binary:
   - `default`: Path to the `msedgedriver.exe` binary.

4. `headers`: Custom HTTP headers used in browser requests:
   - `User-Agent`: Sets the user-agent string for the browser.
   - `Accept`: Sets the types of data the browser is willing to accept.
   - `Accept-Charset`: Sets the character encoding supported by the browser.
   - `Accept-Encoding`: Sets the supported encoding methods (set to `none` to disable).
   - `Accept-Language`: Sets the preferred languages.
   - `Connection`: Sets the connection type the browser should use (e.g., `keep-alive`).

Usage:

To use the `Edge` WebDriver in your project, simply import and initialize it:

```python
from src.webdriver.edge import Edge

# Initialize Edge WebDriver with user-agent settings and custom options
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Open a website
browser.get("https://www.example.com")

# Close the browser
browser.quit()
```

The `Edge` class automatically loads settings from the `edge.json` file and uses them to configure the WebDriver. You can also specify a custom user-agent and pass additional options during WebDriver initialization.

Singleton Pattern:

The `Edge` WebDriver uses the Singleton pattern. This means only one instance of the WebDriver will be created. If an instance already exists, the same instance will be reused, and a new window will be opened.

Logging and Debugging:

The WebDriver class uses the `logger` from `src.logger` to log errors, warnings, and general information. All issues encountered during initialization, configuration, or execution will be logged for easy debugging.

Example Logs:

- Error during WebDriver initialization: `Error initializing Edge WebDriver: <error details>`
- Configuration issues: `Error in edge.json file: <issue details>`
"""
```