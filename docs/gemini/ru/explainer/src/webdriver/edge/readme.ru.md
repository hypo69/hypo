## АНАЛИЗ КОДА: `src/webdriver/edge/readme.ru.md`

### 1. <алгоритм>

1.  **Инициализация WebDriver:**
    *   При создании экземпляра класса `Edge`, он считывает конфигурацию из `edge.json`.
    *   Пример: `browser = Edge()`
    *   Если `edge.json` не найден, возникает ошибка.

2.  **Настройка параметров WebDriver:**
    *   Разбираются параметры из `edge.json`, такие как `options`, `profiles`, `executable_path` и `headers`.
    *   Пример: Чтение пути к `msedgedriver.exe` из `executable_path.default`
        ```json
        "executable_path": {
            "default": "webdrivers\\\\edge\\\\123.0.2420.97\\\\msedgedriver.exe"
        }
        ```
    *   Пример: Использование параметров `options`:
        ```json
        "options": [
            "--disable-dev-shm-usage",
            "--remote-debugging-port=0"
        ]
        ```
    *   Пример: Установка пользовательских заголовков:
        ```json
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
            ...
        }
        ```
    *   Если путь к `msedgedriver.exe` не указан или не найден, возникает ошибка.

3.  **Применение пользовательских настроек:**
    *   Пользовательский `user_agent` и `options`, передаваемые при инициализации, применяются поверх настроек из `edge.json`.
    *   Пример:
        ```python
        browser = Edge(user_agent="Custom User Agent", options=["--headless"])
        ```

4.  **Создание или использование существующего экземпляра WebDriver (Singleton):**
    *   Если экземпляр WebDriver уже создан, возвращается существующий экземпляр.
    *   Если нет, то создаётся новый экземпляр WebDriver.

5.  **Использование WebDriver:**
    *   Вызываются методы WebDriver для взаимодействия с браузером (например, `get`, `quit`).
    *   Пример: `browser.get("https://www.example.com")`

6.  **Логирование:**
    *   Все действия, ошибки и предупреждения логируются с помощью `logger` из `src.logger`.
    *   Пример: Запись в лог ошибки инициализации.

7.  **Завершение работы:**
    *   При вызове `browser.quit()` закрывается браузер и экземпляр WebDriver.
    *   Если экземпляр WebDriver не создан, ошибок не возникает.

### 2. <mermaid>

```mermaid
flowchart TD
    Start --> ReadConfig[Read <code>edge.json</code> Configuration File]
    ReadConfig -- Configuration Loaded --> ApplySettings[Apply Configuration Settings]
    ApplySettings --> CheckSingleton[Check if WebDriver Singleton Exists]
    CheckSingleton -- Yes --> UseExistingInstance[Use Existing WebDriver Instance]
    CheckSingleton -- No --> CreateWebDriver[Create New WebDriver Instance]
    CreateWebDriver --> SetWebDriverOptions[Set WebDriver Options (from <code>edge.json</code> and user-provided)]
    SetWebDriverOptions --> SetWebDriverHeaders[Set WebDriver Headers (from <code>edge.json</code>)]
    SetWebDriverHeaders --> InitializeDriver[Initialize WebDriver]
    InitializeDriver --> LogInitialization[Log Initialization Status]
    LogInitialization -- Success --> WebDriverReady[WebDriver Ready]
    LogInitialization -- Failure --> LogError[Log Error]
    LogError --> WebDriverNotReady[WebDriver Not Ready]
    UseExistingInstance --> WebDriverReady
    WebDriverReady --> BrowserAction[Perform Browser Actions (e.g., get, quit)]
    BrowserAction --> End
     
    subgraph WebDriver Initialization
       ReadConfig
       ApplySettings
       CheckSingleton
       CreateWebDriver
       SetWebDriverOptions
       SetWebDriverHeaders
       InitializeDriver
       LogInitialization
       LogError
    end

     subgraph WebDriver Usage
       WebDriverReady
       UseExistingInstance
       BrowserAction
    end

    
```

**Объяснение `mermaid` диаграммы:**

*   **`Start`**: Начало процесса инициализации и использования WebDriver.
*   **`ReadConfig`**: Читает конфигурационные данные из `edge.json`.
*   **`ApplySettings`**: Применяет основные настройки из `edge.json`.
*   **`CheckSingleton`**: Проверяет, существует ли уже экземпляр WebDriver (паттерн Singleton).
*   **`UseExistingInstance`**: Если экземпляр существует, то используется он.
*   **`CreateWebDriver`**: Если экземпляр отсутствует, создаётся новый.
*   **`SetWebDriverOptions`**: Устанавливает опции WebDriver, комбинируя настройки из `edge.json` и пользовательские параметры.
*   **`SetWebDriverHeaders`**: Устанавливает пользовательские HTTP-заголовки из `edge.json`.
*   **`InitializeDriver`**: Инициализирует WebDriver с заданными опциями и заголовками.
*   **`LogInitialization`**: Логирует результат инициализации WebDriver (успех или ошибка).
*   **`WebDriverReady`**: WebDriver готов к использованию.
*   **`LogError`**: Логирует ошибки, возникшие в процессе инициализации.
*   **`WebDriverNotReady`**: WebDriver не готов к использованию из-за ошибки.
*   **`BrowserAction`**: Выполнение действий в браузере (переход на страницу, закрытие браузера).
*   **`End`**: Конец процесса.

### 3. <объяснение>

**Импорты:**

*   В данном коде, в явном виде, нет `import`. Но из контекста описания подразумевается импорт:
    - `from src.logger import logger`: Импортируется модуль `logger` из пакета `src.logger`, который используется для логирования событий. Это обеспечивает централизованное логирование в приложении.
    - `from selenium import webdriver`: Импортируется библиотека `webdriver` из пакета `selenium`, которая используется для управления браузером. Это основной компонент для автоматизации браузера.
*   Взаимосвязь с `src`: `src` является корневым пакетом проекта, и `src.logger` является модулем для логирования, который используется внутри других модулей проекта для записи сообщений о событиях.

**Классы:**

*   **`Edge`**: Это основной класс, который инкапсулирует логику для работы с Edge WebDriver.
    *   **Атрибуты**:
        *   `_instance` (static): Хранит единственный экземпляр WebDriver (реализация Singleton).
        *   `driver`: Объект WebDriver, предоставляемый Selenium.
        *   `_config`: Словарь, хранящий конфигурацию, загруженную из `edge.json`.
        *   `logger`: Объект `logger` для логирования.
    *   **Методы**:
        *   `__init__(self, user_agent=None, options=None)`: Конструктор класса, инициализирует WebDriver, применяет настройки из `edge.json` и переданные параметры.
        *   `get_config(self)`: Загружает и обрабатывает данные из `edge.json`.
        *   `_get_driver_instance(self)`: Возвращает существующий экземпляр WebDriver или создаёт новый (Singleton).
        *   `quit(self)`: Закрывает браузер и освобождает ресурсы WebDriver.
        *   `get(self, url)`: Переходит по заданному URL.
    *   **Взаимодействие:**
        *   Класс `Edge` использует `webdriver` из `selenium` для управления браузером.
        *   Класс `Edge` использует `logger` из `src.logger` для логирования ошибок, предупреждений и информации.

**Функции:**
*  `get_config(self)`: Загружает конфигурацию из файла `edge.json`, обрабатывает пути, заменяя переменные окружения и возвращает данные в формате словаря. 
  *  Аргументы: `self` - ссылка на экземпляр класса.
  *  Возвращаемое значение: Словарь, содержащий конфигурацию из `edge.json`.
    *  Пример: 
    ```python
    def get_config(self):
      with open("edge.json", "r") as f:
        config = json.load(f)
      # Замена переменных окружения в путях
      for key in config["profiles"]:
        if isinstance(config["profiles"][key], str):
          config["profiles"][key] = os.path.expandvars(config["profiles"][key])
      for key in config["executable_path"]:
        if isinstance(config["executable_path"][key], str):
          config["executable_path"][key] = os.path.expandvars(config["executable_path"][key])
      return config
      ```
*   `__init__(self, user_agent=None, options=None)`: Конструктор класса, инициализирует WebDriver, применяет настройки из `edge.json` и переданные параметры.
    *   Аргументы: `self` - ссылка на экземпляр класса, `user_agent` - строка, задающая user-agent, `options` - список дополнительных параметров.
    *   Возвращаемое значение: Нет (конструктор).
    *   Пример:
        ```python
        def __init__(self, user_agent=None, options=None):
            self.logger = logger
            if Edge._instance:
                self.driver = Edge._instance.driver
                logger.info("Using existing WebDriver instance")
                return
            
            self._config = self.get_config()
             
            edge_options = webdriver.EdgeOptions()

            if options:
                for option in options:
                    edge_options.add_argument(option)

            for option in self._config.get("options", []):
                edge_options.add_argument(option)
           
            if self._config["executable_path"]:
                executable_path = self._config["executable_path"].get("default")
                if not os.path.exists(executable_path):
                    self.logger.error(f"Ошибка: msedgedriver не найден по пути '{executable_path}'.")
                    raise FileNotFoundError(f"msedgedriver не найден по пути '{executable_path}'.")
            else:
                executable_path = None
            
            if not executable_path:
                 self.logger.error("Ошибка: Не указан путь к msedgedriver")
                 raise FileNotFoundError("Не указан путь к msedgedriver")
            
            if self._config["profiles"]:
               user_data_dir = self._config["profiles"].get("os",None)
               if user_data_dir:
                    edge_options.add_argument(f'--user-data-dir={user_data_dir}')
               
            if user_agent:
              edge_options.add_argument(f"--user-agent={user_agent}")
            elif self._config["headers"].get("User-Agent", None):
              edge_options.add_argument(f'--user-agent={self._config["headers"].get("User-Agent")}')


            self.driver = webdriver.Edge(options=edge_options, executable_path=executable_path)
            Edge._instance = self
            
            logger.info(f"Edge WebDriver initialized with user agent: {edge_options.arguments}")
        ```

*   `_get_driver_instance(self)`: Возвращает существующий экземпляр WebDriver, если он есть, или создаёт новый.
    *   Аргументы: `self` - ссылка на экземпляр класса.
    *   Возвращаемое значение: Экземпляр WebDriver.
    *   Пример:
        ```python
        def _get_driver_instance(self):
            if Edge._instance is None:
                Edge()
            return Edge._instance
        ```

*   `quit(self)`: Закрывает браузер и освобождает ресурсы WebDriver.
    *   Аргументы: `self` - ссылка на экземпляр класса.
    *   Возвращаемое значение: Нет.
    *   Пример:
        ```python
         def quit(self):
            if self.driver:
                self.driver.quit()
                self.logger.info("Edge WebDriver closed")
                Edge._instance = None
            else:
                self.logger.warning("No WebDriver instance to quit")
        ```

*   `get(self, url)`: Переходит по заданному URL.
    *   Аргументы: `self` - ссылка на экземпляр класса, `url` - строка с URL-адресом.
    *   Возвращаемое значение: Нет.
    *   Пример:
        ```python
        def get(self, url):
            if self.driver:
                self.driver.get(url)
                self.logger.info(f"Navigated to {url}")
            else:
                 self.logger.error("WebDriver instance is not available.")
        ```

**Переменные:**

*   `_instance`: Статическая переменная, хранящая экземпляр класса `Edge` (реализация Singleton).
*   `driver`: Экземпляр WebDriver, используемый для управления браузером.
*   `_config`: Словарь, хранящий конфигурацию, загруженную из `edge.json`.
*   `logger`: Экземпляр `logger` из `src.logger` для логирования.

**Потенциальные ошибки и области для улучшения:**

1.  **Отсутствие обработки ошибок:**
    *   Ошибки при загрузке `edge.json`, при отсутствии `msedgedriver` обрабатываются, но можно добавить более специфическую обработку, например, исключения для каждого этапа.
    *   При невалидном содержимом `edge.json` могут возникать ошибки - следует валидировать `json` схему.
2.  **Нехватка настроек для `EdgeOptions`:**
    *   Не все возможные опции `webdriver.EdgeOptions` используются. Можно добавить возможность настраивать больше опций через `edge.json`.
3.  **Обработка Singleton:**
    *   При использовании Singleton можно добавить проверку, чтобы не допустить создание нового экземпляра при некорректном состоянии.
4.  **Не хватает методов `webdriver`**:
  * Класс `Edge` предоставляет минимальный набор методов `get`, `quit` - можно добавить другие, такие как: `find_element`, `click` и другие.
5.  **Отсутствие обработки исключений**:
  * Все методы, кроме `quit` не имеют блока `try/except` для обработки исключений, которые может вернуть `webdriver`.

**Цепочка взаимосвязей:**

1.  **`src.webdriver.edge.Edge` → `src.logger.logger`**: Класс `Edge` использует `logger` из `src.logger` для логирования.
2.  **`src.webdriver.edge.Edge` → `selenium.webdriver`**: Класс `Edge` использует `webdriver` из `selenium` для управления браузером Edge.
3.  **`src.webdriver.edge.Edge` → `edge.json`**: Класс `Edge` считывает конфигурацию из файла `edge.json`.
4.  **`src.webdriver.edge.Edge` → `os`**: Класс `Edge` использует `os.path.expandvars` для подстановки переменных окружения в пути к `edge.json`.

Таким образом, класс `Edge` является центральным элементом для управления Edge WebDriver, интегрируя настройки конфигурации, логирования и возможности автоматизации браузера через Selenium.