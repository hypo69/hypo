# Модуль `src.webdriver.playwright.playwrid`

## Обзор

Модуль предоставляет класс `Playwrid`, который является подклассом `PlaywrightCrawler` из библиотеки `crawlee`. Он расширяет функциональность `PlaywrightCrawler`, позволяя настраивать параметры запуска браузера, профили и опции запуска с использованием Playwright.

## Подробнее

Этот модуль предназначен для использования в качестве веб-драйвера на основе Playwright. Он предоставляет удобный интерфейс для запуска браузера, навигации по URL, взаимодействия с элементами на странице и получения их содержимого. Он интегрируется с системой логирования для отслеживания ошибок и предупреждений.

## Классы

### `Playwrid`

**Описание**: Класс `Playwrid` наследуется от `PlaywrightCrawler` и предоставляет расширенные возможности для управления браузером Playwright.

**Наследует**:
- `PlaywrightCrawler`: Базовый класс для создания веб-пауков с использованием Playwright.

**Атрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию 'playwrid'.
- `base_path` (Path): Базовый путь к директории модуля.
- `config` (SimpleNamespace): Конфигурация, загруженная из файла `playwrid.json`.
- `context`: Контекст выполнения Playwright.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Playwrid`.
- `_set_launch_options`: Настраивает параметры запуска браузера.
- `start`: Запускает браузер и переходит по указанному URL.
- `current_url`: Возвращает текущий URL открытой страницы.
- `get_page_content`: Возвращает HTML-содержимое текущей страницы.
- `get_element_content`: Возвращает HTML-содержимое элемента по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента по XPath.
- `click_element`: Кликает на элемент по CSS-селектору.
- `execute_locator`: Выполняет локатор через исполнитель.

### `Playwrid.__init__`

```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
    """
    Initializes the Playwright Crawler with the specified launch options, settings, and user agent.
    """
```

**Назначение**: Инициализирует класс `Playwrid`, настраивая параметры запуска браузера, пользовательский агент и другие опции.

**Параметры**:
- `user_agent` (Optional[str], optional): Пользовательский агент для браузера. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций командной строки для Playwright. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор `PlaywrightCrawler`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор `PlaywrightCrawler`.

**Как работает функция**:

1. **Конфигурация параметров запуска**: Вызывает метод `_set_launch_options` для настройки параметров запуска браузера на основе предоставленных аргументов `user_agent` и `options`.
2. **Инициализация исполнителя**: Создает экземпляр класса `PlaywrightExecutor`, который будет использоваться для выполнения действий в браузере.
3. **Инициализация базового класса**: Вызывает конструктор базового класса `PlaywrightCrawler`, передавая параметры запуска и другие аргументы.
4. **Настройка параметров запуска (если необходимо)**: Если базовый класс `PlaywrightCrawler` имеет метод `set_launch_options`, вызывает его для установки параметров запуска. В противном случае параметры запуска обрабатываются другим способом.

```
A: Конфигурация параметров запуска
|
B: Инициализация исполнителя
|
C: Инициализация базового класса
|
D: Настройка параметров запуска (если необходимо)
```

**Примеры**:

```python
browser = Playwrid(user_agent="My Custom Agent", options=["--disable-gpu"])
```

### `Playwrid._set_launch_options`

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

**Назначение**: Конфигурирует параметры запуска браузера Playwright, такие как режим без графического интерфейса, пользовательский агент и дополнительные опции.

**Параметры**:
- `user_agent` (Optional[str], optional): Пользовательский агент для браузера. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций командной строки для Playwright. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

**Как работает функция**:

1. **Инициализация параметров запуска**: Создает словарь `launch_options` с базовыми параметрами, такими как режим без графического интерфейса (`headless`) и опции командной строки (`args`), загруженные из конфигурации.
2. **Добавление пользовательского агента**: Если предоставлен пользовательский агент (`user_agent`), добавляет его в словарь `launch_options`.
3. **Объединение опций**: Если предоставлены дополнительные опции (`options`), объединяет их с опциями, уже присутствующими в словаре `launch_options`.
4. **Возврат параметров запуска**: Возвращает словарь `launch_options` с настроенными параметрами запуска.

```
A: Инициализация параметров запуска
|
B: Добавление пользовательского агента
|
C: Объединение опций
|
D: Возврат параметров запуска
```

**Примеры**:

```python
launch_options = self._set_launch_options(user_agent="My Custom Agent", options=["--disable-gpu"])
```

### `Playwrid.start`

```python
async def start(self, url: str) -> None:
    """
    Starts the Playwrid Crawler and navigates to the specified URL.

    :param url: The URL to navigate to.
    :type url: str
    """
```

**Назначение**: Запускает Playwright Crawler и переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Как работает функция**:

1. **Логирование**: Записывает информационное сообщение о начале запуска Playwright Crawler для указанного URL.
2. **Запуск исполнителя**: Запускает исполнитель (`self.executor`), который управляет браузером Playwright.
3. **Переход по URL**: Вызывает метод `goto` исполнителя для перехода по указанному URL.
4. **Запуск паука**: Вызывает метод `run` базового класса `PlaywrightCrawler` для запуска процесса сбора данных.
5. **Получение контекста**: Получает контекст выполнения (`self.crawling_context`) и сохраняет его в атрибуте `self.context`.
6. **Обработка исключений**: Перехватывает возможные исключения и записывает критическое сообщение об ошибке в лог.

```
A: Логирование
|
B: Запуск исполнителя
|
C: Переход по URL
|
D: Запуск паука
|
E: Получение контекста
|
F: Обработка исключений
```

**Примеры**:

```python
await browser.start("https://www.example.com")
```

### `Playwrid.current_url`

```python
@property
def current_url(self) -> Optional[str]:
    """
    Returns the current URL of the browser.

    :returns: The current URL.
    :rtype: Optional[str]
    """
```

**Назначение**: Возвращает текущий URL открытой страницы в браузере.

**Возвращает**:
- `Optional[str]`: Текущий URL или `None`, если контекст или страница не определены.

**Как работает функция**:

1. **Проверка контекста и страницы**: Проверяет, определены ли атрибуты `self.context` и `self.context.page`.
2. **Получение URL**: Если контекст и страница определены, возвращает URL страницы (`self.context.page.url`).
3. **Возврат None**: Если контекст или страница не определены, возвращает `None`.

```
A: Проверка контекста и страницы
|
B: Получение URL
|
C: Возврат None
```

**Примеры**:

```python
current_url = browser.current_url
if current_url:
    print(f"Текущий URL: {current_url}")
```

### `Playwrid.get_page_content`

```python
def get_page_content(self) -> Optional[str]:
    """
    Returns the HTML content of the current page.

    :returns: HTML content of the page.
    :rtype: Optional[str]
    """
```

**Назначение**: Возвращает HTML-содержимое текущей страницы.

**Возвращает**:
- `Optional[str]`: HTML-содержимое страницы или `None`, если контекст или страница не определены.

**Как работает функция**:

1. **Проверка контекста и страницы**: Проверяет, определены ли атрибуты `self.context` и `self.context.page`.
2. **Получение содержимого**: Если контекст и страница определены, возвращает HTML-содержимое страницы (`self.context.page.content()`).
3. **Возврат None**: Если контекст или страница не определены, возвращает `None`.

```
A: Проверка контекста и страницы
|
B: Получение содержимого
|
C: Возврат None
```

**Примеры**:

```python
page_content = browser.get_page_content()
if page_content:
    print(f"Содержимое страницы: {page_content[:200]}...")
```

### `Playwrid.get_element_content`

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

**Назначение**: Возвращает внутреннее HTML-содержимое элемента на странице, найденного по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: Внутреннее HTML-содержимое элемента или `None`, если элемент не найден или произошла ошибка.

**Как работает функция**:

1. **Проверка контекста и страницы**: Проверяет, определены ли атрибуты `self.context` и `self.context.page`.
2. **Поиск элемента**: Если контекст и страница определены, пытается найти элемент на странице с использованием CSS-селектора (`self.context.page.locator(selector)`).
3. **Извлечение содержимого**: Если элемент найден, извлекает его внутреннее HTML-содержимое (`await element.inner_html()`).
4. **Обработка исключений**: Перехватывает возможные исключения и записывает предупреждающее сообщение в лог.
5. **Возврат содержимого или None**: Возвращает внутреннее HTML-содержимое элемента или `None`, если элемент не найден или произошла ошибка.

```
A: Проверка контекста и страницы
|
B: Поиск элемента
|
C: Извлечение содержимого
|
D: Обработка исключений
|
E: Возврат содержимого или None
```

**Примеры**:

```python
element_content = await browser.get_element_content("h1")
if element_content:
    print(f"Содержимое элемента h1: {element_content}")
```

### `Playwrid.get_element_value_by_xpath`

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

**Назначение**: Возвращает текстовое значение элемента на странице, найденного по XPath.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден или произошла ошибка.

**Как работает функция**:

1. **Проверка контекста и страницы**: Проверяет, определены ли атрибуты `self.context` и `self.context.page`.
2. **Поиск элемента**: Если контекст и страница определены, пытается найти элемент на странице с использованием XPath (`self.context.page.locator(f'xpath={xpath}')`).
3. **Извлечение значения**: Если элемент найден, извлекает его текстовое значение (`await element.text_content()`).
4. **Обработка исключений**: Перехватывает возможные исключения и записывает предупреждающее сообщение в лог.
5. **Возврат значения или None**: Возвращает текстовое значение элемента или `None`, если элемент не найден или произошла ошибка.

```
A: Проверка контекста и страницы
|
B: Поиск элемента
|
C: Извлечение значения
|
D: Обработка исключений
|
E: Возврат значения или None
```

**Примеры**:

```python
xpath_value = await browser.get_element_value_by_xpath("//head/title")
if xpath_value:
    print(f"Значение элемента по XPATH //head/title: {xpath_value}")
```

### `Playwrid.click_element`

```python
async def click_element(self, selector: str) -> None:
    """
    Clicks a single element on the page by CSS selector.

    :param selector: CSS selector of the element to click.
    :type selector: str
    """
```

**Назначение**: Кликает на элемент на странице, найденный по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента для клика.

**Как работает функция**:

1. **Проверка контекста и страницы**: Проверяет, определены ли атрибуты `self.context` и `self.context.page`.
2. **Поиск элемента**: Если контекст и страница определены, пытается найти элемент на странице с использованием CSS-селектора (`self.context.page.locator(selector)`).
3. **Клик на элемент**: Если элемент найден, выполняет клик на элементе (`await element.click()`).
4. **Обработка исключений**: Перехватывает возможные исключения и записывает предупреждающее сообщение в лог.

```
A: Проверка контекста и страницы
|
B: Поиск элемента
|
C: Клик на элемент
|
D: Обработка исключений
```

**Примеры**:

```python
await browser.click_element("button")
```

### `Playwrid.execute_locator`

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

**Назначение**: Выполняет локатор через исполнитель (`self.executor`).

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

**Как работает функция**:

1. **Вызов исполнителя**: Вызывает метод `execute_locator` исполнителя (`self.executor.execute_locator`), передавая данные локатора, сообщение и скорость печати.
2. **Возврат статуса**: Возвращает статус выполнения, полученный от исполнителя.

```
A: Вызов исполнителя
|
B: Возврат статуса
```

**Примеры**:

```python
locator_data = {
    "by": "XPATH",
    "selector": "//h1",
}
result = await browser.execute_locator(locator_data)
print(f"Результат выполнения локатора: {result}")
```

## Функции

### `main` (внутри `if __name__ == "__main__":`)

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
```

**Назначение**: Функция `main` представляет собой асинхронную функцию, которая демонстрирует использование класса `Playwrid` для выполнения различных действий в браузере, таких как запуск браузера, переход по URL, получение содержимого страницы и взаимодействие с элементами.

**Как работает функция**:

1. **Создание экземпляра `Playwrid`**: Создается экземпляр класса `Playwrid` с опцией запуска браузера в режиме без графического интерфейса (`--headless`).

2. **Запуск браузера и переход по URL**: Вызывается метод `start` для запуска браузера и перехода по указанному URL ("https://www.example.com").

3. **Получение HTML-содержимого страницы**: Вызывается метод `get_page_content` для получения HTML-содержимого текущей страницы. Если содержимое получено, выводятся первые 200 символов.

4. **Получение содержимого элемента по селектору**: Вызывается метод `get_element_content` для получения содержимого элемента `h1` по CSS-селектору. Если элемент найден, его содержимое выводится.

5. **Получение значения элемента по XPath**: Вызывается метод `get_element_value_by_xpath` для получения значения элемента `title` по XPath. Если элемент найден, его значение выводится.

6. **Клик на элемент**: Вызывается метод `click_element` для выполнения клика на элементе `button`.

7. **Выполнение локатора**:
   - Определяется локатор `locator_name` для получения названия товара (элемента `h1`). Вызывается метод `execute_locator` для выполнения локатора и выводится полученное название.
   - Определяется локатор `locator_click` для клика на кнопку. Вызывается метод `execute_locator` для выполнения клика на кнопке.

8. **Пауза**: Выполняется пауза в течение 3 секунд с помощью `asyncio.sleep(3)`.

```
A: Создание экземпляра Playwrid
|
B: Запуск браузера и переход по URL
|
C: Получение HTML-содержимого страницы
|
D: Получение содержимого элемента по селектору
|
E: Получение значения элемента по XPath
|
F: Клик на элемент
|
G: Выполнение локатора (получение названия товара)
|
H: Выполнение локатора (клик на кнопку)
|
I: Пауза
```

**Примеры**:

```python
async def main():
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")
    
    html_content = browser.get_page_content()
    if html_content:
        print(html_content[:200])