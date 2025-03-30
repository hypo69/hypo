# Модуль `playwrid`

## Обзор

Модуль `playwrid` предоставляет класс `Playwrid`, который является подклассом `PlaywrightCrawler` из библиотеки `crawlee`. Он предназначен для упрощения процесса веб-скрапинга с использованием Playwright. Класс `Playwrid` позволяет настраивать параметры запуска браузера, такие как user-agent и другие опции, а также предоставляет методы для взаимодействия с веб-страницами, такие как получение контента, клики по элементам и выполнение JavaScript.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации сбора данных с веб-страниц. Он использует Playwright для управления браузером и выполнения различных действий на странице. Класс `Playwrid` расширяет возможности `PlaywrightCrawler`, добавляя удобные методы для настройки и управления браузером, а также для извлечения данных с веб-страниц.

## Классы

### `Playwrid`

**Описание**:
Подкласс `PlaywrightCrawler`, предоставляющий дополнительные функции для настройки и управления браузером Playwright.

**Методы**:
- `__init__`: Инициализирует класс `Playwrid` с заданными параметрами запуска, настройками и user-agent.
- `_set_launch_options`: Конфигурирует параметры запуска для Playwright.
- `start`: Запускает Playwright Crawler и переходит по указанному URL.
- `current_url`: Возвращает текущий URL браузера.
- `get_page_content`: Возвращает HTML-контент текущей страницы.
- `get_element_content`: Возвращает внутренний HTML-контент элемента на странице по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента на странице по XPath.
- `click_element`: Кликает на элемент на странице по CSS-селектору.
- `execute_locator`: Выполняет локатор через executor.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent для использования. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций Playwright для запуска. По умолчанию `None`.

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
Инициализирует экземпляр класса `Playwrid`.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent для использования. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций Playwright для запуска. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в `PlaywrightCrawler`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `PlaywrightCrawler`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
browser = Playwrid(user_agent='Custom User Agent', options=['--disable-web-security'])
```

### `_set_launch_options`

```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Configures the launch options for the Playwright Crawler.
    """
```

**Описание**:
Конфигурирует параметры запуска для Playwright, такие как `headless`, `args` (опции командной строки) и `user_agent`.

**Параметры**:
- `user_agent` (Optional[str], optional): User-agent для использования. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций Playwright для запуска. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
launch_options = self._set_launch_options(user_agent='Custom User Agent', options=['--disable-web-security'])
```

### `start`

```python
async def start(self, url: str) -> None:
    """
    Starts the Playwrid Crawler and navigates to the specified URL.
    """
```

**Описание**:
Запускает Playwright Crawler и переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если Playwright Crawler завершается с ошибкой.

**Примеры**:
```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
asyncio.run(main())
```

### `current_url`

```python
@property
def current_url(self) -> Optional[str]:
    """
    Returns the current URL of the browser.
    """
```

**Описание**:
Возвращает текущий URL браузера.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `Optional[str]`: Текущий URL или `None`, если URL недоступен.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
url = browser.current_url
print(f"Current URL: {url}")
```

### `get_page_content`

```python
def get_page_content(self) -> Optional[str]:
    """
    Returns the HTML content of the current page.
    """
```

**Описание**:
Возвращает HTML-контент текущей страницы.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `Optional[str]`: HTML-контент страницы или `None`, если контент недоступен.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
html_content = browser.get_page_content()
if html_content:
    print(html_content[:200])  # Выведем первые 200 символов для примера
else:
    print("Не удалось получить HTML-контент.")
```

### `get_element_content`

```python
async def get_element_content(self, selector: str) -> Optional[str]:
    """
    Returns the inner HTML content of a single element on the page by CSS selector.
    """
```

**Описание**:
Возвращает внутренний HTML-контент элемента на странице по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: Внутренний HTML-контент элемента или `None`, если элемент не найден или произошла ошибка.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
element_content = await browser.get_element_content("h1")
if element_content:
    print("\nСодержимое элемента h1:")
    print(element_content)
else:
    print("\nЭлемент h1 не найден.")
```

### `get_element_value_by_xpath`

```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
    """
    Returns the text value of a single element on the page by XPath.
    """
```

**Описание**:
Возвращает текстовое значение элемента на странице по XPath.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден или произошла ошибка.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
xpath_value = await browser.get_element_value_by_xpath("//head/title")
if xpath_value:
    print(f"\nЗначение элемента по XPATH //head/title: {xpath_value}")
else:
    print("\nЭлемент по XPATH //head/title не найден")
```

### `click_element`

```python
async def click_element(self, selector: str) -> None:
    """
    Clicks a single element on the page by CSS selector.
    """
```

**Описание**:
Кликает на элемент на странице по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
await browser.click_element("button")
```

### `execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
    """
    Executes locator through executor
    """
```

**Описание**:
Выполняет локатор через executor.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
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
```
```python
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
```
```