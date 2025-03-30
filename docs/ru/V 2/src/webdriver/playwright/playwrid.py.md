# Модуль `playwrid`

## Обзор

Модуль `playwrid.py` представляет собой расширение класса `PlaywrightCrawler`, предоставляя дополнительные возможности для управления браузером через Playwright. Он позволяет настраивать параметры запуска браузера, профили, а также предоставляет удобные методы для взаимодействия со страницей, такие как получение контента, клики и выполнение JavaScript.

## Содержание

- [Классы](#классы)
    - [`Playwrid`](#playwrid)
- [Функции](#функции)
    - [`_set_launch_options`](#_set_launch_options)
    - [`start`](#start)
    - [`current_url`](#current_url)
    - [`get_page_content`](#get_page_content)
    - [`get_element_content`](#get_element_content)
    - [`get_element_value_by_xpath`](#get_element_value_by_xpath)
    - [`click_element`](#click_element)
    - [`execute_locator`](#execute_locator)

## Классы

### `Playwrid`

**Описание**:
Подкласс `PlaywrightCrawler`, предоставляющий дополнительные функциональные возможности.

**Атрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию `playwrid`.
- `base_path` (Path): Путь к каталогу с файлами драйвера.
- `config` (SimpleNamespace): Конфигурация драйвера, загруженная из `playwrid.json`.
- `context` : Контекст выполнения браузера.

**Методы**:
- [`__init__`](#__init__): Инициализирует Playwright Crawler с заданными параметрами запуска, настройками и user-agent.
- [`_set_launch_options`](#_set_launch_options): Настраивает параметры запуска для Playwright Crawler.
- [`start`](#start): Запускает Playwrid Crawler и переходит по указанному URL.
- [`current_url`](#current_url): Возвращает текущий URL браузера.
- [`get_page_content`](#get_page_content): Возвращает HTML-контент текущей страницы.
- [`get_element_content`](#get_element_content): Возвращает внутренний HTML-контент элемента по CSS-селектору.
- [`get_element_value_by_xpath`](#get_element_value_by_xpath): Возвращает текстовое значение элемента по XPath.
- [`click_element`](#click_element): Кликает по элементу на странице по CSS-селектору.
- [`execute_locator`](#execute_locator): Выполняет действия с элементом, используя локатор.

#### `__init__`
```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
    """
    Инициализирует Playwright Crawler с заданными параметрами запуска, настройками и user-agent.
    """
```
    
**Описание**:
Инициализирует экземпляр класса `Playwrid`. Принимает настройки запуска, пользовательский агент и прочие параметры для `PlaywrightCrawler`.

**Параметры**:
- `user_agent` (Optional[str], optional): Пользовательский агент для браузера. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Дополнительные параметры запуска Playwright. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `_set_launch_options`

```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Настраивает параметры запуска для Playwright Crawler.

    :param settings: A SimpleNamespace object containing launch settings.
    :type settings: SimpleNamespace
    :param user_agent: The user-agent string to be used.
    :type user_agent: Optional[str]
    :param options: A list of Playwright options to be passed during initialization.
    :type options: Optional[List[str]]
    :returns: A dictionary with launch options for Playwright.
    :rtype: Dict[str, Any]
    """
```

**Описание**:
Настраивает параметры запуска для браузера Playwright.

**Параметры**:
- `user_agent` (Optional[str], optional): Пользовательский агент. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список дополнительных опций Playwright. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска.

#### `start`
```python
async def start(self, url: str) -> None:
    """
    Запускает Playwrid Crawler и переходит по указанному URL.

    :param url: The URL to navigate to.
    :type url: str
    """
```

**Описание**:
Запускает браузер и переходит на указанный URL.

**Параметры**:
- `url` (str): URL для навигации.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `Exception`: В случае ошибки при запуске браузера или перехода по URL.

#### `current_url`

```python
@property
def current_url(self) -> Optional[str]:
    """
    Возвращает текущий URL браузера.

    :returns: The current URL.
    :rtype: Optional[str]
    """
```

**Описание**:
Возвращает текущий URL страницы в браузере.

**Параметры**:
- Нет

**Возвращает**:
- `Optional[str]`: Текущий URL или `None`, если URL не найден.

#### `get_page_content`
```python
def get_page_content(self) -> Optional[str]:
    """
    Возвращает HTML-контент текущей страницы.

    :returns: HTML content of the page.
    :rtype: Optional[str]
    """
```

**Описание**:
Получает HTML-содержимое текущей страницы.

**Параметры**:
- Нет

**Возвращает**:
- `Optional[str]`: HTML-содержимое страницы или `None`, если не удалось получить контент.

#### `get_element_content`
```python
async def get_element_content(self, selector: str) -> Optional[str]:
    """
    Возвращает внутренний HTML-контент элемента по CSS-селектору.

    :param selector: CSS selector for the element.
    :type selector: str
    :returns: Inner HTML content of the element, or None if not found.
    :rtype: Optional[str]
    """
```

**Описание**:
Извлекает внутренний HTML-контент элемента по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: HTML-содержимое элемента или `None`, если элемент не найден.

#### `get_element_value_by_xpath`
```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
    """
    Возвращает текстовое значение элемента по XPath.

    :param xpath: XPath of the element.
    :type xpath: str
    :returns: The text value of the element, or None if not found.
    :rtype: Optional[str]
    """
```

**Описание**:
Извлекает текстовое значение элемента по XPath.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден.

#### `click_element`
```python
async def click_element(self, selector: str) -> None:
    """
    Кликает по элементу на странице по CSS-селектору.

    :param selector: CSS selector of the element to click.
    :type selector: str
    """
```

**Описание**:
Выполняет клик по элементу на странице, определенному CSS-селектором.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `execute_locator`
```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
    """
    Executes locator through executor

    :param locator: Locator data (dict or SimpleNamespace).
    :type locator: dict | SimpleNamespace
    :param message: Optional message for events.
    :type message: Optional[str]
    :param typing_speed: Optional typing speed for events.
    :type typing_speed: float
    :returns: Execution status.
    :rtype: str | List[str] | bytes | List[bytes] | bool
    """
```

**Описание**:
Выполняет действие, определенное в локаторе, через исполнитель.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость ввода текста. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Результат выполнения действия.

## Функции

### `_set_launch_options`

Смотрите описание в разделе [Классы - `Playwrid`](#_set_launch_options).

### `start`

Смотрите описание в разделе [Классы - `Playwrid`](#start).

### `current_url`

Смотрите описание в разделе [Классы - `Playwrid`](#current_url).

### `get_page_content`

Смотрите описание в разделе [Классы - `Playwrid`](#get_page_content).

### `get_element_content`

Смотрите описание в разделе [Классы - `Playwrid`](#get_element_content).

### `get_element_value_by_xpath`

Смотрите описание в разделе [Классы - `Playwrid`](#get_element_value_by_xpath).

### `click_element`

Смотрите описание в разделе [Классы - `Playwrid`](#click_element).
### `execute_locator`

Смотрите описание в разделе [Классы - `Playwrid`](#execute_locator).