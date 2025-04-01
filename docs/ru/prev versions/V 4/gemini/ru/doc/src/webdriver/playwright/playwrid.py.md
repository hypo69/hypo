# Модуль `playwrid`

## Обзор

Модуль `playwrid` представляет собой расширение класса `PlaywrightCrawler` из библиотеки `crawlee`, предназначенное для выполнения задач веб-сканирования с использованием Playwright. Он предоставляет дополнительные возможности, такие как настройка параметров запуска браузера, профилей и опций запуска через Playwright.

## Подробнее

Этот модуль облегчает настройку и запуск Playwright для сканирования веб-страниц, позволяя указывать различные параметры, такие как user-agent, опции запуска и другие настройки браузера. Он также включает в себя методы для взаимодействия с элементами на странице, такие как получение контента, ввод текста и выполнение кликов. Расположение файла в проекте: `hypotez/src/webdriver/playwright/playwrid.py`.

## Классы

### `Playwrid`

**Описание**:
Подкласс `PlaywrightCrawler`, предоставляющий дополнительные функции для управления Playwright.

**Методы**:

- `__init__`: Инициализирует класс `Playwrid` с указанными параметрами запуска, настройками и user-agent.
- `_set_launch_options`: Настраивает параметры запуска для Playwright Crawler.
- `start`: Запускает Playwrid Crawler и переходит по указанному URL.
- `current_url`: Возвращает текущий URL браузера.
- `get_page_content`: Возвращает HTML-контент текущей страницы.
- `get_element_content`: Возвращает внутренний HTML-контент элемента на странице по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента на странице по XPath.
- `click_element`: Кликает на элемент на странице по CSS-селектору.
- `execute_locator`: Выполняет действия с локатором через исполнитель.

**Параметры**:

- `user_agent` (Optional[str]): User-agent, который будет использоваться.
- `options` (Optional[List[str]]): Список опций Playwright, передаваемых при инициализации.
- `*args`: Дополнительные аргументы, передаваемые в `PlaywrightCrawler`.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые в `PlaywrightCrawler`.

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
    ...
```

**Описание**:
Настраивает параметры запуска для Playwright Crawler, объединяя параметры из конфигурации, пользовательского user-agent и дополнительных опций.

**Параметры**:

- `user_agent` (Optional[str]): User-agent, который будет использоваться.
- `options` (Optional[List[str]]): Список опций Playwright, передаваемых при инициализации.

**Возвращает**:

- `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

**Примеры**:

```python
launch_options = self._set_launch_options(user_agent="custom_user_agent", options=["--disable-gpu"])
print(launch_options)
# Expected output: {'headless': True, 'args': ['--disable-gpu'], 'user_agent': 'custom_user_agent'}
```

### `start`

```python
async def start(self, url: str) -> None:
    """
    Starts the Playwrid Crawler and navigates to the specified URL.

    :param url: The URL to navigate to.
    :type url: str
    """
    ...
```

**Описание**:
Запускает Playwrid Crawler и переходит по указанному URL.

**Параметры**:

- `url` (str): URL для перехода.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
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
    ...
```

**Описание**:
Возвращает текущий URL браузера.

**Возвращает**:

- `Optional[str]`: Текущий URL или `None`, если URL недоступен.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
    print(browser.current_url)
```

### `get_page_content`

```python
def get_page_content(self) -> Optional[str]:
    """
    Returns the HTML content of the current page.

    :returns: HTML content of the page.
    :rtype: Optional[str]
    """
    ...
```

**Описание**:
Возвращает HTML-контент текущей страницы.

**Возвращает**:

- `Optional[str]`: HTML-контент страницы или `None`, если контент недоступен.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
    html_content = browser.get_page_content()
    print(html_content[:100])
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
    ...
```

**Описание**:
Возвращает внутренний HTML-контент элемента на странице по CSS-селектору.

**Параметры**:

- `selector` (str): CSS-селектор элемента.

**Возвращает**:

- `Optional[str]`: Внутренний HTML-контент элемента или `None`, если элемент не найден.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
    element_content = await browser.get_element_content("h1")
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
    ...
```

**Описание**:
Возвращает текстовое значение элемента на странице по XPath.

**Параметры**:

- `xpath` (str): XPath элемента.

**Возвращает**:

- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
    xpath_value = await browser.get_element_value_by_xpath("//head/title")
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
    ...
```

**Описание**:
Кликает на элемент на странице по CSS-селектору.

**Параметры**:

- `selector` (str): CSS-селектор элемента для клика.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
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
    ...
```

**Описание**:
Выполняет локатор через исполнитель.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str]): Опциональное сообщение для событий.
- `typing_speed` (float): Опциональная скорость ввода текста для событий.

**Возвращает**:

- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")

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