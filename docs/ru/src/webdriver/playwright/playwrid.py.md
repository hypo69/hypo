# Модуль `playwrid.py`

## Обзор

Модуль `playwrid.py` представляет собой расширение класса `PlaywrightCrawler` из библиотеки `crawlee`, предназначенное для автоматизации действий в браузере Playwright. Он предоставляет удобные методы для настройки запуска браузера, навигации по страницам, извлечения контента и взаимодействия с элементами на странице.

## Подробней

Этот модуль облегчает создание веб-скрейперов и автоматизированных тестов, предоставляя простой интерфейс для работы с Playwright. Он позволяет задавать параметры запуска браузера, такие как user-agent и опции командной строки, а также предоставляет методы для получения контента страницы, поиска элементов и выполнения кликов. Модуль также включает функциональность для выполнения сложных действий с использованием локаторов через `PlaywrightExecutor`. Расположение модуля в структуре проекта `hypotez` указывает на его роль как основного инструмента для веб-скрапинга и автоматизации браузера.

## Классы

### `Playwrid`

**Описание**:
Подкласс `PlaywrightCrawler`, предоставляющий дополнительные функции для управления браузером Playwright.

**Как работает класс**:
Класс `Playwrid` наследует функциональность `PlaywrightCrawler` и добавляет методы для настройки запуска браузера, управления контекстом и выполнения действий на странице. Он использует `PlaywrightExecutor` для выполнения сложных операций с локаторами.

- Инициализирует Playwright Crawler с заданными параметрами запуска, настройками и агентом пользователя.
- Настраивает параметры запуска для Playwright Crawler.
- Запускает Playwright Crawler и переходит по указанному URL.
- Возвращает текущий URL браузера.
- Возвращает HTML-контент текущей страницы.
- Возвращает HTML-контент элемента, найденного по CSS-селектору.
- Возвращает текстовое значение элемента, найденного по XPath.
- Кликает на элемент, найденный по CSS-селектору.
- Выполняет локатор через исполнитель.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Playwrid`.
- `_set_launch_options`: Настраивает параметры запуска браузера.
- `start`: Запускает браузер и переходит по указанному URL.
- `current_url`: Возвращает текущий URL страницы.
- `get_page_content`: Возвращает HTML-содержимое текущей страницы.
- `get_element_content`: Возвращает HTML-содержимое элемента по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента по XPath.
- `click_element`: Кликает на элемент по CSS-селектору.
- `execute_locator`: Выполняет действие, определенное локатором.

**Параметры**:
- `driver_name` (str): Имя драйвера, по умолчанию 'playwrid'.
- `base_path` (Path): Базовый путь к файлам модуля.
- `config` (SimpleNamespace): Объект с конфигурацией из файла `playwrid.json`.
- `context` (Any): Контекст выполнения Playwright.
- `user_agent` (Optional[str]): User-agent для браузера.
- `options` (Optional[List[str]]): Список опций командной строки для запуска браузера.

**Примеры**:

```python
if __name__ == "__main__":
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
            print("\nСодержимое элемента h1:")
            print(element_content)
        else:
            print("\nЭлемент h1 не найден.")

        # Получение значения элемента по xpath
        xpath_value = await browser.get_element_value_by_xpath("//head/title")
        if xpath_value:
            print(f"\nЗначение элемента по XPATH //head/title: {xpath_value}")
        else:
            print("\nЭлемент по XPATH //head/title не найден")

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

## Функции

### `__init__`

```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
    """
    Initializes the Playwright Crawler with the specified launch options, settings, and user agent.
    """
```

**Описание**:
Инициализирует экземпляр класса `Playwrid`, настраивая параметры запуска браузера и передавая их в конструктор родительского класса `PlaywrightCrawler`.

**Как работает функция**:
1. Вызывает метод `_set_launch_options` для формирования словаря параметров запуска браузера.
2. Инициализирует `PlaywrightExecutor`.
3. Вызывает конструктор родительского класса `PlaywrightCrawler`, передавая ему параметры запуска браузера.
4. Если у экземпляра класса есть метод `set_launch_options`, вызывает его для установки параметров запуска.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent для браузера. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций командной строки для запуска браузера. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
browser = Playwrid(options=["--headless"], user_agent="MyUserAgent")
```

### `_set_launch_options`

```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Configures the launch options for the Playwright Crawler.

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
Настраивает параметры запуска браузера Playwright, объединяя значения из конфигурационного файла, переданного user-agent и дополнительных опций.

**Как работает функция**:
1. Инициализирует словарь `launch_options` значениями из атрибута `config` (если они определены) или значениями по умолчанию (`headless=True`, `args=[]`).
2. Если передан `user_agent`, добавляет его в словарь `launch_options`.
3. Если переданы дополнительные `options`, расширяет список аргументов `launch_options`.
4. Возвращает сформированный словарь `launch_options`.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent для браузера. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций командной строки для запуска браузера. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска браузера.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
launch_options = self._set_launch_options(user_agent="MyUserAgent", options=["--proxy-server=proxy"])
```

### `start`

```python
async def start(self, url: str) -> None:
    """
    Starts the Playwrid Crawler and navigates to the specified URL.

    :param url: The URL to navigate to.
    :type url: str
    """
```

**Описание**:
Запускает Playwright Crawler и переходит по указанному URL.

**Как работает функция**:
1. Логирует информацию о запуске краулера для указанного URL.
2. Запускает `PlaywrightExecutor`.
3. Переходит по указанному URL с помощью `PlaywrightExecutor`.
4. Запускает основной цикл краулера с помощью `super().run(url)`.
5. Получает контекст краулера.
6. Обрабатывает исключения, логируя критическую информацию об ошибке.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время запуска или выполнения краулера.

**Примеры**:

```python
await browser.start("https://www.example.com")
```

### `current_url`

```python
@property
def current_url(self) -> Optional[str]:
    """
    Returns the current URL of the browser.

    :returns: The current URL.
    :rtype: Optional[str]
    """
```

**Описание**:
Возвращает текущий URL браузера.

**Как работает функция**:
1. Проверяет, существует ли контекст краулера и страницу в контексте.
2. Если контекст и страница существуют, возвращает текущий URL страницы.
3. В противном случае возвращает `None`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Optional[str]`: Текущий URL страницы или `None`, если URL недоступен.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
url = browser.current_url
if url:
    print(f"Current URL: {url}")
```

### `get_page_content`

```python
def get_page_content(self) -> Optional[str]:
    """
    Returns the HTML content of the current page.

    :returns: HTML content of the page.
    :rtype: Optional[str]
    """
```

**Описание**:
Возвращает HTML-содержимое текущей страницы.

**Как работает функция**:
1. Проверяет, существует ли контекст краулера и страницу в контексте.
2. Если контекст и страница существуют, возвращает HTML-содержимое страницы.
3. В противном случае возвращает `None`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Optional[str]`: HTML-содержимое страницы или `None`, если содержимое недоступно.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
html_content = browser.get_page_content()
if html_content:
    print(html_content[:200])
```

### `get_element_content`

```python
async def get_element_content(self, selector: str) -> Optional[str]:
    """
    Returns the inner HTML content of a single element on the page by CSS selector.

    :param selector: CSS selector for the element.
    :type selector: str
    :returns: Inner HTML content of the element, or None if not found.
    :rtype: Optional[str]
    """
```

**Описание**:
Возвращает внутреннее HTML-содержимое элемента на странице, найденного по CSS-селектору.

**Как работает функция**:
1. Проверяет, существует ли контекст краулера и страницу в контексте.
2. Если контекст и страница существуют, пытается найти элемент по CSS-селектору с помощью `self.context.page.locator(selector)`.
3. Если элемент найден, возвращает его внутреннее HTML-содержимое.
4. Если элемент не найден или произошла ошибка, логирует предупреждение и возвращает `None`.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: Внутреннее HTML-содержимое элемента или `None`, если элемент не найден или произошла ошибка.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
element_content = await browser.get_element_content("h1")
if element_content:
    print(element_content)
```

### `get_element_value_by_xpath`

```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
    """
    Returns the text value of a single element on the page by XPath.

    :param xpath: XPath of the element.
    :type xpath: str
    :returns: The text value of the element, or None if not found.
    :rtype: Optional[str]
    """
```

**Описание**:
Возвращает текстовое значение элемента на странице, найденного по XPath.

**Как работает функция**:
1. Проверяет, существует ли контекст краулера и страницу в контексте.
2. Если контекст и страница существуют, пытается найти элемент по XPath с помощью `self.context.page.locator(f'xpath={xpath}')`.
3. Если элемент найден, возвращает его текстовое значение.
4. Если элемент не найден или произошла ошибка, логирует предупреждение и возвращает `None`.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден или произошла ошибка.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
xpath_value = await browser.get_element_value_by_xpath("//head/title")
if xpath_value:
    print(xpath_value)
```

### `click_element`

```python
async def click_element(self, selector: str) -> None:
    """
    Clicks a single element on the page by CSS selector.

    :param selector: CSS selector of the element to click.
    :type selector: str
    """
```

**Описание**:
Кликает на элемент на странице, найденный по CSS-селектору.

**Как работает функция**:
1. Проверяет, существует ли контекст краулера и страницу в контексте.
2. Если контекст и страница существуют, пытается найти элемент по CSS-селектору с помощью `self.context.page.locator(selector)`.
3. Если элемент найден, выполняет клик на элементе.
4. Если элемент не найден или произошла ошибка, логирует предупреждение.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
await browser.click_element("button")
```

### `execute_locator`

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
Выполняет действие, определенное локатором, с помощью `PlaywrightExecutor`.

**Как работает функция**:
1. Вызывает метод `execute_locator` экземпляра `PlaywrightExecutor`, передавая ему данные локатора, сообщение и скорость печати.
2. Возвращает результат выполнения локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Результат выполнения локатора.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
locator = {
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
name = await browser.execute_locator(locator)
print(f"Name: {name}")
```