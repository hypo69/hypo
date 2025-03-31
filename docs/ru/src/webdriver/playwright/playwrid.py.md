# Модуль `playwrid`

## Обзор

Модуль `playwrid` представляет собой подкласс `PlaywrightCrawler` и предназначен для сканирования веб-страниц с использованием Playwright. Он предоставляет расширенные возможности, такие как настройка параметров запуска браузера, профилей и опций запуска.

## Подробнее

Этот модуль является частью проекта `hypotez` и используется для автоматизированного сбора данных с веб-страниц. Он расширяет функциональность `PlaywrightCrawler`, добавляя возможность настройки параметров запуска браузера, таких как user-agent и опции командной строки. Модуль позволяет выполнять навигацию по страницам, извлекать контент элементов и выполнять другие действия, необходимые для сканирования веб-страниц.

## Классы

### `Playwrid`

**Описание**:
Класс `Playwrid` является подклассом `PlaywrightCrawler` и предоставляет дополнительные функции для управления браузером Playwright.

**Как работает класс**:
Класс инициализируется с настройками запуска браузера, такими как user-agent и опции командной строки. Он также предоставляет методы для навигации по страницам, извлечения контента элементов и выполнения других действий, необходимых для сканирования веб-страниц.

**Атрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию `playwrid`.
- `base_path` (Path): Путь к базовой директории модуля.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию из файла `playwrid.json`.
- `context`: Контекст выполнения сканирования.

**Методы**:
- `__init__`: Инициализирует класс `Playwrid` с заданными параметрами запуска, настройками и user agent.
- `_set_launch_options`: Конфигурирует параметры запуска для `Playwright Crawler`.
- `start`: Запускает `Playwrid Crawler` и переходит по указанному URL.
- `current_url`: Возвращает текущий URL браузера.
- `get_page_content`: Возвращает HTML-контент текущей страницы.
- `get_element_content`: Возвращает внутренний HTML-контент элемента на странице по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента на странице по XPath.
- `click_element`: Кликает на элемент на странице по CSS-селектору.
- `execute_locator`: Выполняет локатор через executor.

#### `__init__`

```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
    """
    Инициализирует Playwright Crawler с указанными параметрами запуска, настройками и user agent.

    Args:
        user_agent (Optional[str], optional): User-agent, который будет использоваться. По умолчанию `None`.
        options (Optional[List[str]], optional): Список опций Playwright, передаваемых при инициализации. По умолчанию `None`.
        *args: Произвольные позиционные аргументы.
        **kwargs: Произвольные именованные аргументы.

    Raises:
        Exception: Если возникает ошибка при инициализации Playwright Crawler.
    """
    ...
```

**Как работает функция**:
Инициализирует класс `Playwrid`, устанавливая параметры запуска браузера, такие как `user_agent` и опции командной строки. Она также инициализирует `PlaywrightExecutor` и передает параметры запуска в `PlaywrightCrawler`.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent, который будет использоваться. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций Playwright, передаваемых при инициализации. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

#### `_set_launch_options`

```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Конфигурирует параметры запуска для Playwright Crawler.

    Args:
        user_agent (Optional[str], optional): User-agent, который будет использоваться. По умолчанию `None`.
        options (Optional[List[str]], optional): Список опций Playwright, передаваемых при инициализации. По умолчанию `None`.

    Returns:
        Dict[str, Any]: Словарь с параметрами запуска для Playwright.

    Raises:
        Exception: Если возникает ошибка при конфигурации параметров запуска.
    """
    ...
```

**Как работает функция**:
Конфигурирует параметры запуска браузера Playwright, такие как `headless` и аргументы командной строки. Она также добавляет пользовательский `user-agent`, если он указан.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent, который будет использоваться. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций Playwright, передаваемых при инициализации. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

#### `start`

```python
async def start(self, url: str) -> None:
    """
    Запускает Playwrid Crawler и переходит по указанному URL.

    Args:
        url (str): URL для перехода.

    Raises:
        Exception: Если возникает ошибка при запуске Playwrid Crawler.
    """
    ...
```

**Как работает функция**:
Запускает Playwright Crawler и переходит по указанному URL. Она также запускает `PlaywrightExecutor` и получает контекст выполнения сканирования.

**Параметры**:
- `url` (str): URL для перехода.

#### `current_url`

```python
@property
def current_url(self) -> Optional[str]:
    """
    Возвращает текущий URL браузера.

    Returns:
        Optional[str]: Текущий URL.
    """
    ...
```

**Как работает функция**:
Возвращает текущий URL браузера, используя контекст выполнения сканирования.

**Возвращает**:
- `Optional[str]`: Текущий URL.

#### `get_page_content`

```python
def get_page_content(self) -> Optional[str]:
    """
    Возвращает HTML-контент текущей страницы.

    Returns:
        Optional[str]: HTML-контент страницы.
    """
    ...
```

**Как работает функция**:
Возвращает HTML-контент текущей страницы, используя контекст выполнения сканирования.

**Возвращает**:
- `Optional[str]`: HTML-контент страницы.

#### `get_element_content`

```python
async def get_element_content(self, selector: str) -> Optional[str]:
    """
    Возвращает внутренний HTML-контент элемента на странице по CSS-селектору.

    Args:
        selector (str): CSS-селектор элемента.

    Returns:
        Optional[str]: Внутренний HTML-контент элемента.
    """
    ...
```

**Как работает функция**:
Возвращает внутренний HTML-контент элемента на странице по CSS-селектору, используя контекст выполнения сканирования.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: Внутренний HTML-контент элемента.

#### `get_element_value_by_xpath`

```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
    """
    Возвращает текстовое значение элемента на странице по XPath.

    Args:
        xpath (str): XPath элемента.

    Returns:
        Optional[str]: Текстовое значение элемента.
    """
    ...
```

**Как работает функция**:
Возвращает текстовое значение элемента на странице по XPath, используя контекст выполнения сканирования.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента.

#### `click_element`

```python
async def click_element(self, selector: str) -> None:
    """
    Кликает на элемент на странице по CSS-селектору.

    Args:
        selector (str): CSS-селектор элемента для клика.
    """
    ...
```

**Как работает функция**:
Кликает на элемент на странице по CSS-селектору, используя контекст выполнения сканирования.

**Параметры**:
- `selector` (str): CSS-селектор элемента для клика.

#### `execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
    """
    Выполняет локатор через executor

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        message (Optional[str], optional): Optional message for events. Defaults to None.
        typing_speed (float, optional): Optional typing speed for events. Defaults to 0.

    Returns:
        str | List[str] | bytes | List[bytes] | bool: Execution status.
    """
    ...
```

**Как работает функция**:
Выполняет локатор через executor, передавая данные локатора, сообщение и скорость набора текста.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Опциональное сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Опциональная скорость набора текста для событий. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

## Функции

### `main`

```python
async def main():
    """
    Основная функция для демонстрации работы Playwrid Crawler.
    """
    ...
```

**Как работает функция**:
Создает экземпляр `Playwrid`, запускает его, получает контент страницы, контент элемента по селектору, значение элемента по XPath и кликает на кнопку.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
    
    # Получение HTML всего документа
    html_content = browser.get_page_content()
    if html_content:
        print(html_content[:200])  # Выведем первые 200 символов для примера
    else:
        print("Не удалось получить HTML-контент.")
    
    # Получение HTML элемента по селектору
    element_content = await browser.get_element_content("h1")
    if element_content:
        print("\\nСодержимое элемента h1:")
        print(element_content)
    else:
        print("\\nЭлемент h1 не найден.")
    
    # Получение значения элемента по xpath
    xpath_value = await browser.get_element_value_by_xpath("//head/title")
    if xpath_value:
         print(f"\\nЗначение элемента по XPATH //head/title: {xpath_value}")
    else:
         print("\\nЭлемент по XPATH //head/title не найден")

    # Нажатие на кнопку (при наличии)
    await browser.click_element("button")

    locator_name = {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//h1",
    "if_list": "first",
    "use_mouse": False,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": None,
    "mandatory": True,
    "locator_description": "Название товара"
    }

    name = await browser.execute_locator(locator_name)
    print("Name:", name)

    locator_click = {
    "attribute": None,
    "by": "CSS",
    "selector": "button",
    "if_list": "first",
    "use_mouse": False,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": "click()",
    "mandatory": True,
    "locator_description": "название товара"
    }
    await browser.execute_locator(locator_click)
    await asyncio.sleep(3)
asyncio.run(main())
```