# Модуль `edge.py`

## Обзор

Модуль `edge.py` представляет собой пользовательский класс `Edge` для управления веб-браузером Microsoft Edge с использованием Selenium WebDriver. Он предоставляет упрощенную настройку, включая управление user-agent, опциями запуска, и интеграцию с пользовательскими JavaScript-функциями.

## Подробней

Этот модуль предназначен для упрощения и расширения возможностей стандартного Selenium WebDriver для Edge. Он позволяет легко настраивать user-agent, добавлять различные опции запуска, управлять режимами окна (например, kiosk, windowless, full_window) и использовать пользовательские профили.

## Классы

### `Edge`

**Описание**:
Класс `Edge` наследуется от `selenium.webdriver.Edge` и предоставляет расширенные возможности для управления браузером Edge.

**Как работает класс**:
1.  **Инициализация**:
    *   При инициализации класса `Edge` происходит загрузка настроек из файла `edge.json`.
    *   Создается объект `EdgeOptions`, в который добавляются различные аргументы, такие как `user-agent`, параметры режима окна и другие опции, указанные в конфигурации или переданные при инициализации.
    *   Настраивается директория профиля пользователя. Если указано имя профиля, используется соответствующая директория.
    *   Создается и запускается экземпляр `EdgeService` с указанным путем к исполняемому файлу `edgedriver`.
    *   Вызывается метод `_payload` для загрузки пользовательских JavaScript-функций и установки атрибутов для взаимодействия с веб-страницами.
2.  **Управление опциями**:
    *   Поддерживается установка различных режимов окна, таких как `kiosk`, `windowless` и `full_window`.
    *   Добавление пользовательских опций запуска через метод `add_argument`.
3.  **Обработка исключений**:
    *   Обрабатываются исключения, возникающие при запуске WebDriver, с использованием модуля `logger` для логирования критических ошибок.
4.  **Интеграция JavaScript**:
    *   Метод `_payload` загружает и устанавливает различные JavaScript-функции для выполнения задач, таких как получение языка страницы, проверка состояния готовности, получение referrer, отображение скрытых элементов DOM и фокусировка окна.

**Методы**:

*   `__init__(self, profile_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`:
    *   Инициализирует экземпляр класса `Edge`.
    *   Настраивает user-agent, опции запуска и профиль пользователя.
    *   Запускает WebDriver с заданными параметрами.

*   `_payload(self) -> None`:
    *   Загружает пользовательские JavaScript-функции и устанавливает атрибуты для взаимодействия с веб-страницами.

*   `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`:
    *   Создает и настраивает опции запуска для Edge WebDriver.
    *   Позволяет добавлять дополнительные опции запуска.

**Параметры**:

*   `driver_name` (str): Имя используемого WebDriver, по умолчанию `'edge'`.

**Примеры**:

```python
from src.webdriver.edge.edge import Edge
# Инициализация Edge WebDriver с пользовательским user-agent и опциями
driver = Edge(user_agent='CustomUserAgent', options=['--disable-gpu'], window_mode='full_window')
driver.get("https://www.example.com")
```

## Функции

### `__init__`

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

**Как работает функция**:
Функция инициализирует класс `Edge`, настраивая user-agent, параметры запуска и профиль пользователя. Она загружает настройки из файла `edge.json`, создает объект `EdgeOptions`, добавляет аргументы (user-agent, режим окна, пользовательские опции), настраивает директорию профиля и запускает WebDriver с заданными параметрами. Также обрабатываются исключения, возникающие при запуске WebDriver, с использованием модуля `logger` для логирования критических ошибок.

**Параметры**:

*   `profile_name` (Optional[str], optional): Имя профиля пользователя. По умолчанию `None`.
*   `user_agent` (Optional[str], optional): User-agent для браузера. Если `None`, генерируется случайный user-agent. По умолчанию `None`.
*   `options` (Optional[List[str]], optional): Список опций для Edge WebDriver. По умолчанию `None`.
*   `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
*   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
*   `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:

*   `WebDriverException`: Если не удается запустить Edge WebDriver.
*   `Exception`: При возникновении общей ошибки во время инициализации.

**Примеры**:

```python
from src.webdriver.edge.edge import Edge
# Инициализация Edge WebDriver с пользовательским user-agent и опциями
driver = Edge(user_agent='CustomUserAgent', options=['--disable-gpu'], window_mode='full_window')
```

### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
```

**Как работает функция**:
Функция `_payload` загружает и устанавливает различные JavaScript-функции для выполнения задач, таких как получение языка страницы, проверка состояния готовности, получение referrer, отображение скрытых элементов DOM и фокусировка окна. Она создает экземпляр класса `JavaScript` и устанавливает соответствующие атрибуты для взаимодействия с веб-страницами.

**Параметры**:

*   `self`: Ссылка на экземпляр класса `Edge`.

**Примеры**:

```python
from src.webdriver.edge.edge import Edge
# Инициализация Edge WebDriver
driver = Edge()
# Загрузка пользовательских JavaScript-функций
driver._payload()
```

### `set_options`

```python
def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:
    """
    Create and configure launch options for the Edge WebDriver.

    :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.
    :return: Configured `EdgeOptions` object.
    """
```

**Как работает функция**:
Функция `set_options` создает и настраивает опции запуска для Edge WebDriver. Она позволяет добавлять дополнительные опции запуска, переданные в виде списка. Функция создает объект `EdgeOptions` и добавляет в него переданные опции.

**Параметры**:

*   `opts` (Optional[List[str]], optional): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:

*   `EdgeOptions`: Конфигурированный объект `EdgeOptions`.

**Примеры**:

```python
from src.webdriver.edge.edge import Edge
# Инициализация Edge WebDriver
driver = Edge()
# Создание и настройка опций запуска
options = driver.set_options(opts=['--disable-gpu', '--mute-audio'])