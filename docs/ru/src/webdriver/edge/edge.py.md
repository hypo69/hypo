# Модуль `edge`

## Обзор

Модуль `edge` предоставляет кастомный класс `Edge` для управления веб-драйвером Edge с расширенными функциями. Он упрощает настройку WebDriver, используя `fake_useragent` для подмены User-Agent и предоставляет возможность настройки различных параметров запуска, таких как режим окна и профили пользователей.

## Подробней

Этот модуль предназначен для упрощения и расширения возможностей управления браузером Edge в автоматизированных тестах и задачах сбора данных. Он позволяет настраивать User-Agent, устанавливать различные режимы окна (например, kiosk, windowless, full_window) и управлять профилями пользователей. Модуль использует библиотеку `selenium` для взаимодействия с Edge WebDriver и `fake_useragent` для генерации случайных User-Agent.

## Классы

### `Edge`

**Описание**:
Кастомный класс WebDriver для Edge с расширенными функциями.

**Как работает класс**:
Класс `Edge` наследуется от `selenium.webdriver.Edge` и предоставляет расширенные возможности для настройки и управления веб-драйвером Edge. При инициализации класса происходит следующее:

1.  **Инициализация параметров**: Определяется User-Agent (случайный или заданный), загружаются настройки из файла `edge.json`.
2.  **Настройка опций Edge**: Создается объект `EdgeOptions`, в который добавляются User-Agent, режим окна и другие параметры.
3.  **Настройка профиля пользователя**: Определяется директория профиля пользователя.
4.  **Запуск WebDriver**: Инициализируется WebDriver с заданными опциями и сервисом.
5.  **Загрузка payload**: Загружаются executors для локаторов и JavaScript сценариев.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `Edge`.
*   `_payload`: Загружает executors для локаторов и JavaScript сценариев.
*   `set_options`: Создает и настраивает опции запуска для Edge WebDriver.

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

**Описание**:
Инициализирует WebDriver Edge с указанным User-Agent и опциями.

**Как работает функция**:

1.  Определяет User-Agent: Если `user_agent` не указан, генерирует случайный User-Agent с помощью `fake_useragent`.
2.  Загружает настройки из `edge.json`.
3.  Инициализирует объект `EdgeOptions` и добавляет User-Agent.
4.  Устанавливает режим окна из конфига или параметров.
5.  Добавляет дополнительные опции из параметров и конфигурации.
6.  Настраивает директорию профиля.
7.  Запускает WebDriver с заданными опциями.
8.  Вызывает метод `_payload` для загрузки executors.

**Параметры**:

*   `profile_name` (Optional[str], optional): Имя профиля пользователя. По умолчанию `None`.
*   `user_agent` (Optional[str], optional): User-Agent, который будет использоваться. Если `None`, будет сгенерирован случайный User-Agent. По умолчанию `None`.
*   `options` (Optional[List[str]], optional): Список опций Edge, передаваемых при инициализации. По умолчанию `None`.
*   `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
*   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
*   `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Вызывает исключения**:

*   `WebDriverException`: Если не удается запустить Edge WebDriver.
*   `Exception`: При возникновении общей ошибки во время инициализации.

**Примеры**:

```python
driver = Edge(user_agent='Mozilla/5.0', options=['--disable-gpu'], window_mode='kiosk')
```

#### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
```

**Описание**:
Загружает executors для локаторов и JavaScript сценариев.

**Как работает функция**:

1.  Инициализирует класс `JavaScript` с текущим экземпляром WebDriver.
2.  Присваивает методы `JavaScript` экземпляру `Edge` для выполнения JavaScript-кода на странице.
3.  Инициализирует класс `ExecuteLocator` с текущим экземпляром WebDriver.
4.  Присваивает методы `ExecuteLocator` экземпляру `Edge` для выполнения поиска элементов и выполнения действий с ними.

**Параметры**:

*   Нет параметров.

**Возвращает**:

*   Нет возвращаемого значения.

**Примеры**:

```python
driver = Edge()
driver._payload()
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

**Описание**:
Создает и настраивает опции запуска для Edge WebDriver.

**Как работает функция**:

1.  Создает экземпляр класса `EdgeOptions`.
2.  Если передан список опций `opts`, добавляет каждую опцию в `EdgeOptions`.
3.  Возвращает настроенный объект `EdgeOptions`.

**Параметры**:

*   `opts` (Optional[List[str]], optional): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:

*   `EdgeOptions`: Настроенный объект `EdgeOptions`.

**Примеры**:

```python
options = driver.set_options(['--headless', '--disable-gpu'])
```

## Функции

### `__main__`

```python
if __name__ == "__main__":
    driver = Edge(window_mode='full_window')
    driver.get("https://www.example.com")
```

**Описание**:
Пример использования класса `Edge`.

**Как работает функция**:

1.  Создает экземпляр класса `Edge` с режимом окна `full_window`.
2.  Переходит на сайт "https://www.example.com".

**Параметры**:

*   Нет параметров.

**Возвращает**:

*   Нет возвращаемого значения.

**Примеры**:

```python
if __name__ == "__main__":
    driver = Edge(window_mode='full_window')
    driver.get("https://www.example.com")
```