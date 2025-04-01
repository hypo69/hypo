# Модуль `src.webdriver.edge.edge`

## Обзор

Модуль предназначен для создания и настройки экземпляра Edge WebDriver с упрощенной конфигурацией, использующей `fake_useragent` для генерации случайных `user-agent`.

## Подробней

Модуль предоставляет класс `Edge`, который наследуется от `selenium.webdriver.Edge` и предоставляет дополнительные возможности, такие как установка `user-agent`, различных опций и заголовков. Он также загружает исполнители локаторов и JavaScript-сценарии для расширения функциональности WebDriver.

## Классы

### `Edge`

**Описание**:
Класс `Edge` представляет собой пользовательский класс WebDriver для браузера Edge, который расширяет стандартные возможности `selenium.webdriver.Edge`. Он позволяет упростить настройку и инициализацию драйвера, автоматически управляя `user-agent` и параметрами запуска.

**Принцип работы**:
Класс инициализируется с заданным или случайно сгенерированным `user-agent`, загружает настройки из JSON-файла конфигурации и применяет их к экземпляру `EdgeOptions`. Он также позволяет установить режим окна браузера (например, `windowless`, `kiosk` или `full_window`). После этого создается экземпляр `EdgeService` с указанным путем к исполняемому файлу Edge WebDriver и вызывается конструктор родительского класса `WebDriver` для завершения инициализации.

**Аттрибуты**:
- `driver_name` (str): Имя используемого драйвера WebDriver, по умолчанию `edge`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Edge` с заданными параметрами.
- `_payload`: Загружает исполнителей для локаторов и JavaScript-сценариев.
- `set_options`: Создает и настраивает параметры запуска для Edge WebDriver.

#### `__init__`

```python
def __init__(self,  profile_name: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 options: Optional[List[str]] = None,
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
    """
    Initializes the Edge WebDriver with the specified user agent and options.

    :param user_agent: The user-agent string to be used. If `None`, a random user agent is generated.
    :type user_agent: Optional[str]
    :param options: A list of Edge options to be passed during initialization.
    :type options: Optional[List[str]]
    :param window_mode: Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)
    :type window_mode: Optional[str]
    """
```

**Назначение**:
Инициализирует Edge WebDriver с указанным user-agent и опциями.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя профиля пользователя. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Строка user-agent для использования. Если `None`, генерируется случайный user-agent.
- `options` (Optional[List[str]], optional): Список опций Edge, передаваемых при инициализации.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.

**Как работает функция**:

1.  **Инициализация User-Agent**:
    - Если `user_agent` не предоставлен, генерируется случайный user-agent с использованием `UserAgent().random`.

2.  **Загрузка Настроек**:
    - Загружаются настройки из JSON-файла (`edge.json`), расположенного в каталоге `src/webdriver/edge`.

3.  **Инициализация Опций Edge**:
    - Создается объект `EdgeOptions`.
    - Добавляется аргумент для установки `user-agent`.
    - `options_obj.add_argument(f'user-agent={self.user_agent}')`

4.  **Установка Режима Окна**:
    - Если в конфигурации указан режим окна (`window_mode`), он используется.
    - Если режим окна указан в параметрах, он имеет приоритет.
    - В зависимости от выбранного режима окна, добавляются соответствующие аргументы:
        - `--kiosk` для режима киоска.
        - `--headless` для безголового режима.
        - `--start-maximized` для полноэкранного режима.

5.  **Добавление Пользовательских Опций**:
    - Если предоставлены пользовательские опции (`options`), они добавляются в `EdgeOptions`.

6.  **Добавление Опций из Конфигурации**:
    - Если в конфигурационном файле указаны опции, они также добавляются в `EdgeOptions`.

7.  **Добавление Заголовков из Конфигурации**:
    - Если в конфигурационном файле указаны заголовки, они добавляются в `EdgeOptions`.

8.  **Настройка Директории Профиля**:
    - Определяется директория профиля на основе настроек в конфигурационном файле.
    - Если указано имя профиля (`profile_name`), используется подкаталог в директории профиля.
    - Если в директории профиля присутствует `%LOCALAPPDATA%`, она заменяется на значение переменной окружения `LOCALAPPDATA`.
    - Добавляется аргумент для указания директории профиля.

9.  **Запуск Edge WebDriver**:
    - Инициализируется `EdgeService` с путем к исполняемому файлу Edge WebDriver.
    - Вызывается конструктор родительского класса `WebDriver` для инициализации драйвера с заданными опциями и сервисом.
    - Вызывается метод `_payload` для загрузки исполнителей локаторов и JavaScript-сценариев.

10. **Обработка Исключений**:
    - Если происходит исключение `WebDriverException` при запуске драйвера, регистрируется критическая ошибка.
    - Если происходит общее исключение, регистрируется критическая ошибка.

**ASCII схема работы функции**:

```
    Начало
    │
    ├───► Инициализация User-Agent
    │
    ├───► Загрузка Настроек из JSON
    │
    ├───► Инициализация EdgeOptions
    │
    ├───► Установка Режима Окна (kiosk/headless/full_window)
    │
    ├───► Добавление Пользовательских Опций
    │
    ├───► Добавление Опций из Конфигурации
    │
    ├───► Добавление Заголовков из Конфигурации
    │
    ├───► Настройка Директории Профиля
    │
    ├───► Инициализация EdgeService
    │
    ├───► super().__init__(options=options_obj, service=service)
    │
    ├───► _payload()
    │
    └───► Обработка исключений (WebDriverException, Exception)
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Инициализация Edge WebDriver с настройками по умолчанию
driver = Edge()

# Пример 2: Инициализация Edge WebDriver с указанием user-agent
driver = Edge(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')

# Пример 3: Инициализация Edge WebDriver с указанием дополнительных опций
driver = Edge(options=['--disable-gpu', '--disable-extensions'])

# Пример 4: Инициализация Edge WebDriver в режиме kiosk
driver = Edge(window_mode='kiosk')

# Пример 5: Инициализация Edge WebDriver с указанием имени профиля
driver = Edge(profile_name='MyProfile')
```

#### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
```

**Назначение**:
Загружает исполнителей для локаторов и JavaScript-сценариев.

**Как работает функция**:

1.  **Инициализация JavaScript**:
    - Создается экземпляр класса `JavaScript` и передается текущий экземпляр `self` (Edge WebDriver).
    - `j = JavaScript(self)`

2.  **Присвоение JavaScript-функций**:
    - Различные JavaScript-функции из экземпляра `j` присваиваются атрибутам текущего экземпляра `self`.
        - `self.get_page_lang = j.get_page_lang`
        - `self.ready_state = j.ready_state`
        - `self.get_referrer = j.ready_state`
        - `self.unhide_DOM_element = j.unhide_DOM_element`
        - `self.window_focus = j.window_focus`

3.  **Инициализация ExecuteLocator**:
    - Создается экземпляр класса `ExecuteLocator` и передается текущий экземпляр `self` (Edge WebDriver).
    - `execute_locator = ExecuteLocator(self)`

4.  **Присвоение методов ExecuteLocator**:
    - Различные методы из экземпляра `execute_locator` присваиваются атрибутам текущего экземпляра `self`.
        - `self.execute_locator = execute_locator.execute_locator`
        - `self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot`
        - `self.get_webelement_by_locator = execute_locator.get_webelement_by_locator`
        - `self.get_attribute_by_locator = execute_locator.get_attribute_by_locator`
        - `self.send_message = self.send_key_to_webelement = execute_locator.send_message`

**ASCII схема работы функции**:

```
    Начало
    │
    ├───► Инициализация JavaScript (j = JavaScript(self))
    │
    ├───► Присвоение JavaScript-функций (self.get_page_lang = j.get_page_lang, ...)
    │
    ├───► Инициализация ExecuteLocator (execute_locator = ExecuteLocator(self))
    │
    └───► Присвоение методов ExecuteLocator (self.execute_locator = execute_locator.execute_locator, ...)
    │
    Конец
```

**Примеры**:

```python
# Пример вызова после инициализации Edge WebDriver
driver = Edge()
driver._payload()

# Теперь можно использовать методы, присвоенные в _payload
# Например:
# page_lang = driver.get_page_lang()
# element = driver.execute_locator(locator)
```

#### `set_options`

```python
def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:  
    """  
    Create and configure launch options for the Edge WebDriver.  

    :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.  
    :return: Configured `EdgeOptions` object.  
    """
```

**Назначение**:
Создает и настраивает параметры запуска для Edge WebDriver.

**Параметры**:
- `opts` (Optional[List[str]], optional): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Настроенный объект `EdgeOptions`.

**Как работает функция**:

1.  **Инициализация EdgeOptions**:
    - Создается новый объект `EdgeOptions`.
    - `options = EdgeOptions()`

2.  **Добавление Опций**:
    - Если предоставлен список опций `opts`, каждая опция добавляется в объект `EdgeOptions`.
    - `if opts:`
    - `for opt in opts:`
    - `options.add_argument(opt)`

3.  **Возврат EdgeOptions**:
    - Возвращается настроенный объект `EdgeOptions`.
    - `return options`

**ASCII схема работы функции**:

```
    Начало
    │
    ├───► Инициализация EdgeOptions (options = EdgeOptions())
    │
    ├───► Проверка наличия опций (if opts)
    │   └───► Добавление опций (options.add_argument(opt))
    │
    └───► Возврат EdgeOptions (return options)
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Создание EdgeOptions с дополнительными опциями
driver = Edge()
options = driver.set_options(opts=['--disable-gpu', '--disable-extensions'])

# Теперь можно использовать эти опции при инициализации драйвера
# driver = Edge(options=options)

# Пример 2: Создание EdgeOptions без дополнительных опций
driver = Edge()
options = driver.set_options()  # Возвращает пустой объект EdgeOptions
```

## Функции

В данном модуле функции отсутствуют.

## Примеры

```python
if __name__ == "__main__":
    driver = Edge(window_mode='full_window')
    driver.get("https://www.example.com")