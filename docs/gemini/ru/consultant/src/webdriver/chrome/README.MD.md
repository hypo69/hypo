# Анализ кода модуля `src.webdriver.chrome`

**Качество кода**
6/10
- Плюсы
    - Код хорошо структурирован и имеет четкое разделение на секции.
    - Наличие описания основных параметров и настроек для `chrome.json`.
    - Использование Singleton паттерна.
    - Подробное описание функциональности и конфигурации.

- Минусы
    - Отсутствует reStructuredText (RST) в описании модуля.
    - Не хватает инструкций по работе с `chrome.json`.
    - Отсутствуют импорты, которые должны быть использованы в коде.
    - Присутствуют неверные пути к файлам (например, `bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\chromedriver.exe`).
    - Не указана работа с `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Ошибки в структуре json файла, отсутствуют некоторые необходимые ключи, которые предположительно должны быть в конфиге.

**Рекомендации по улучшению**
1. **Документация:**
   - Переписать описание модуля в формате RST.
   - Добавить документацию к функциям и методам после их реализации.
2. **Импорты:**
   - Добавить необходимые импорты для работы с `json`, `webdriver`, `fake_useragent` и `src.logger.logger`.
3. **Конфигурация:**
   - Использовать `j_loads` или `j_loads_ns` для загрузки конфигурации из `chrome.json`.
   - Указать корректный путь к файлу `chrome.json`.
4. **Логирование:**
   - Добавить логирование ошибок через `logger.error`.
   - Обеспечить корректную обработку исключений.
5. **Пути:**
    - Уточнить относительные пути к файлам.

**Оптимизированный код**
```markdown
.. module:: src.webdriver.chrome
   :synopsis: Модуль для управления браузером Chrome с использованием Selenium.

=========================================================================================

Модуль предоставляет настраиваемый драйвер Chrome на базе Selenium с поддержкой конфигурации из файла `chrome.json`,
включая параметры user-agent, профили и пользовательские опции.
=========================================================================================

**Ключевые особенности**
-----------------------------------------------------------------------------------------

-  Централизованная конфигурация через `chrome.json`.
-  Поддержка множественных профилей браузера.
-  Расширенное журналирование и обработка ошибок.
-  Возможность передачи пользовательских опций при инициализации драйвера.
-  Реализован паттерн Singleton.

**Требования**
-----------------------------------------------------------------------------------------

Перед использованием модуля необходимо установить следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Chrome WebDriver (например, `chromedriver`)

Для установки необходимых пакетов, выполните:

.. code-block:: bash

   pip install selenium fake_useragent

Убедитесь, что `chromedriver` доступен в вашей системной переменной `PATH` или путь до него указан в конфигурации.

**Конфигурация**
-----------------------------------------------------------------------------------------

Конфигурация драйвера Chrome хранится в файле `chrome.json`.
Пример структуры файла:

.. code-block:: json

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

**Описание полей конфигурации**
-----------------------------------------------------------------------------------------

1. **options**:
   - Словарь параметров Chrome для модификации поведения браузера:
     - **log-level**: Устанавливает уровень детализации журнала. `5` соответствует самому подробному уровню.
     - **disable-dev-shm-usage**: Отключает использование `/dev/shm` в Docker-контейнерах.
     - **remote-debugging-port**: Устанавливает порт для удаленной отладки. `0` означает случайный порт.
     - **arguments**: Список аргументов командной строки. Примеры: `--kiosk` для режима киоска и `--disable-gpu` для отключения GPU.

2. **disabled_options**:
   - Опции, которые явно отключены. В данном случае, `headless` режим отключен.

3. **profile_directory**:
   - Пути к каталогам пользовательских данных Chrome для разных окружений:
     - **os**: Путь к каталогу пользовательских данных по умолчанию.
     - **internal**: Внутренний путь для профиля WebDriver по умолчанию.
     - **testing**: Путь к каталогу пользовательских данных для тестирования.

4. **binary_location**:
   - Пути к исполняемым файлам Chrome:
     - **os**: Путь к установленному Chrome.
     - **exe**: Путь к исполняемому файлу ChromeDriver.
     - **binary**: Путь к бинарному файлу Chrome для тестирования.
     - **chromium**: Путь к Chromium, как альтернатива Chrome.

5. **headers**:
   - Пользовательские HTTP-заголовки для браузера:
     - **User-Agent**: Строка user-agent.
     - **Accept**: Типы данных, которые браузер готов принимать.
     - **Accept-Charset**: Кодировка, поддерживаемая браузером.
     - **Accept-Encoding**: Методы кодирования (установлено в `none`).
     - **Accept-Language**: Предпочитаемые языки.
     - **Connection**: Тип соединения (например, `keep-alive`).

6.  **proxy_enabled**:
    - Логическое значение, указывающее, использовать ли прокси-сервер. По умолчанию `false`.

**Использование**
-----------------------------------------------------------------------------------------

Для использования драйвера, импортируйте и инициализируйте класс `Chrome`:

.. code-block:: python

   from src.webdriver.chrome import Chrome

   # Инициализация WebDriver с пользовательским user-agent и опциями
   browser = Chrome(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

   # Открытие веб-сайта
   browser.get("https://www.example.com")

   # Закрытие браузера
   browser.quit()

Класс `Chrome` автоматически загружает настройки из `chrome.json` и использует их для настройки WebDriver. Вы также можете указать `user-agent` и дополнительные опции при инициализации.

**Паттерн Singleton**
-----------------------------------------------------------------------------------------

Класс `Chrome` использует паттерн Singleton. Это означает, что будет создан только один экземпляр WebDriver. Если экземпляр уже существует, он будет переиспользован, и откроется новое окно.

**Журналирование и отладка**
-----------------------------------------------------------------------------------------

Класс использует `logger` из `src.logger` для записи ошибок и предупреждений. Все проблемы, возникающие при инициализации, настройке или выполнении, будут зафиксированы в журнале.

**Примеры записей журнала**
-----------------------------------------------------------------------------------------

- **Ошибка инициализации WebDriver**: `Error initializing Chrome WebDriver: <error details>`
- **Проблемы с конфигурацией**: `Error in chrome.json file: <issue details>`

**Лицензия**
-----------------------------------------------------------------------------------------

Проект лицензирован по лицензии MIT. Смотрите файл [LICENSE](../../LICENSE) для подробностей.
```
```python
"""
Модуль для управления браузером Chrome с использованием Selenium.
=========================================================================================

Этот модуль предоставляет настраиваемый драйвер Chrome на базе Selenium,
с поддержкой конфигурации из файла `chrome.json`.
Включает параметры user-agent, профили и пользовательские опции.

Пример использования
--------------------

Пример инициализации драйвера Chrome:

.. code-block:: python

   from src.webdriver.chrome import Chrome

   browser = Chrome(user_agent="Mozilla/5.0", options=["--headless"])
   browser.get("https://www.example.com")
   browser.quit()
"""
import json  # импорт модуля json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from src.utils.jjson import j_loads, j_loads_ns  # импорт j_loads из src.utils.jjson
from src.logger.logger import logger  # импорт logger из src.logger.logger
from pathlib import Path  # импорт Path из pathlib

_instance = None
class Chrome:
    """
    Класс для управления браузером Chrome с использованием Selenium.
    
    Использует паттерн Singleton для обеспечения единственного экземпляра драйвера.
    """
    def __new__(cls, *args, **kwargs):
        """
        Реализует паттерн Singleton для класса Chrome.

        Если экземпляр класса уже существует, метод возвращает его, иначе создаёт новый.

        :return: Экземпляр класса Chrome.
        """
        global _instance
        if not _instance:
            _instance = super(Chrome, cls).__new__(cls)
        return _instance

    def __init__(self, user_agent=None, options=None, profile=None):
        """
        Инициализирует драйвер Chrome с заданными настройками.

        :param user_agent: Пользовательский User-Agent.
        :param options: Список дополнительных опций Chrome.
        :param profile: Название профиля пользователя.
        """
        if hasattr(self, '_initialized'):
            return  # Предотвращает повторную инициализацию
        
        self._initialized = True  # Устанавливаем флаг инициализации
        self.driver = None  # Инициализируем driver как None
        self.config = self._load_config() # Загружает конфигурацию из chrome.json
        self.user_agent = user_agent  # Инициализируем user_agent
        self.options = options or []  # Инициализируем options или присваиваем пустой список
        self.profile = profile  # Инициализируем profile
        
        try:
            self.driver = self._setup_driver()
        except Exception as ex:
            logger.error(f'Ошибка инициализации Chrome WebDriver: {ex}')
            return
        
    def _load_config(self):
        """
        Загружает конфигурацию из файла chrome.json.
        
        :return: Словарь с конфигурацией.
        """
        try:
            config_path = Path(__file__).parent / 'chrome.json'
            config = j_loads_ns(config_path)  # загрузка конфига из json файла
            return config
        except FileNotFoundError:
            logger.error(f"Ошибка: Файл конфигурации chrome.json не найден в директории: {config_path.parent}")
            return {}
        except json.JSONDecodeError as ex:
            logger.error(f"Ошибка при чтении файла конфигурации: {ex}")
            return {}
        
    def _setup_driver(self):
            """
            Настраивает и возвращает экземпляр Chrome WebDriver.
            
            :return: Экземпляр Chrome WebDriver.
            """
            chrome_options = Options() # инициализация объекта Options
            
            # Настройка параметров из конфигурации
            if self.config.get('options'):
                for key, value in self.config['options'].items():
                    if value is not None and value != '':
                        chrome_options.add_argument(f'--{key}={value}')  # добавление аргументов в chrome_options из конфига
                    else:
                        chrome_options.add_argument(f'--{key}')
                        
            if self.config.get('disabled_options'):
                for key, value in self.config['disabled_options'].items():
                     chrome_options.add_argument(f'--disable-{key}')

            if self.options:
                for option in self.options:
                    chrome_options.add_argument(option) # добавление пользовательских опций

            # Установка user-agent
            user_agent = self.user_agent or self.config.get('headers', {}).get('User-Agent') or UserAgent().random
            chrome_options.add_argument(f'--user-agent={user_agent}')
            
            # Установка пути к исполняемому файлу chrome
            if self.config.get('binary_location', {}).get('binary'):
                chrome_options.binary_location = self.config['binary_location']['binary']  # устанавливаем бинарный файл
            
            # Установка пути к исполняемому файлу chromedriver
            executable_path =  self.config.get('binary_location', {}).get('exe') # получение пути к драйверу
            
            # Настройка профиля пользователя
            profile_dir = self.config.get('profile_directory', {}).get(self.profile or 'internal')
            if profile_dir:
                chrome_options.add_argument(f'--user-data-dir={profile_dir}') # установка директории пользовательских данных

            #  Инициализация ChromeDriver
            try:
                driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path) # инициализация драйвера
                return driver
            except Exception as ex:
                logger.error(f'Ошибка инициализации Chrome WebDriver: {ex}')
                return None

    def get(self, url):
        """
        Открывает указанный URL в браузере.

        :param url: URL для открытия.
        """
        if self.driver:
            try:
                self.driver.get(url)
            except Exception as ex:
                logger.error(f'Ошибка при открытии URL: {url}, {ex}')
                return
    
    def quit(self):
        """
        Закрывает браузер.
        """
        if self.driver:
            try:
                self.driver.quit()
            except Exception as ex:
                logger.error(f'Ошибка при закрытии драйвера: {ex}')
            finally:
                global _instance
                _instance = None # сбрасываем Singleton при закрытии
                self.driver = None
```