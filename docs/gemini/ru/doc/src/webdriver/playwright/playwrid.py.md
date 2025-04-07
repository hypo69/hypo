# Модуль `src.webdriver.playwright.playwrid`

## Обзор

Модуль `src.webdriver.playwright.playwrid` предоставляет класс `Playwrid`, который является подклассом `PlaywrightCrawler` из библиотеки `crawlee`. Этот класс предназначен для создания веб-скрейперов с использованием Playwright. Он включает в себя дополнительную функциональность, такую как настройка параметров запуска браузера, профилей и опций запуска.

## Подробнее

Модуль позволяет настраивать запуск браузера Playwright с использованием различных опций, таких как user-agent и другие параметры командной строки. Он также предоставляет методы для взаимодействия со страницей, такие как получение контента, выполнение JavaScript и нажатие на элементы. Модуль использует библиотеку `crawlee` для управления процессом сканирования веб-страниц.

## Классы

### `Playwrid`

**Описание**:
Класс `Playwrid` наследуется от `PlaywrightCrawler` и предоставляет функциональность для управления браузером Playwright и выполнения задач сканирования веб-страниц. Он позволяет настраивать параметры запуска браузера, получать контент страницы и выполнять действия с элементами на странице.

**Наследует**:
- `PlaywrightCrawler`

**Атрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию `'playwrid'`.
- `base_path` (Path): Базовый путь к директории с конфигурационными файлами.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию из файла `playwrid.json`.
- `context` (None): Контекст выполнения Playwright.

**Методы**:
- `__init__`: Инициализирует класс `Playwrid` с заданными параметрами запуска, настройками и user agent.
- `_set_launch_options`: Конфигурирует параметры запуска для Playwright Crawler.
- `start`: Запускает Playwrid Crawler и переходит по указанному URL.
- `current_url`: Возвращает текущий URL браузера.
- `get_page_content`: Возвращает HTML-содержимое текущей страницы.
- `get_element_content`: Возвращает внутреннее HTML-содержимое элемента на странице по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента на странице по XPath.
- `click_element`: Кликает на элемент на странице по CSS-селектору.
- `execute_locator`: Выполняет локатор через executor.

### `__init__`

```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None
```

**Назначение**:
Инициализирует экземпляр класса `Playwrid`.

**Параметры**:
- `user_agent` (Optional[str]): User-agent, который будет использоваться в браузере. По умолчанию `None`.
- `options` (Optional[List[str]]): Список опций для запуска Playwright. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Как работает функция**:
1. Конфигурирует опции запуска с помощью `_set_launch_options`.
2. Инициализирует `PlaywrightExecutor`.
3. Инициализирует родительский класс `PlaywrightCrawler`.
4. Если у экземпляра класса есть метод `set_launch_options`, вызывает его для установки опций запуска.

```
_set_launch_options
    ↓
PlaywrightExecutor
    ↓
PlaywrightCrawler
    ↓
set_launch_options (опционально)
```

### `_set_launch_options`

```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]
```

**Назначение**:
Конфигурирует опции запуска для Playwright.

**Параметры**:
- `user_agent` (Optional[str]): User-agent, который будет использоваться в браузере. По умолчанию `None`.
- `options` (Optional[List[str]]): Список опций для запуска Playwright. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с опциями запуска для Playwright.

**Как работает функция**:
1. Инициализирует словарь `launch_options` с опциями `headless` и `args` из конфигурации.
2. Если передан `user_agent`, добавляет его в `launch_options`.
3. Если переданы дополнительные `options`, расширяет список `args` в `launch_options`.

```
Инициализация launch_options
    ↓
Добавление user_agent (если есть)
    ↓
Добавление options (если есть)
    ↓
Возврат launch_options
```

### `start`

```python
async def start(self, url: str) -> None
```

**Назначение**:
Запускает Playwrid Crawler и переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Как работает функция**:
1. Логирует информацию о запуске краулера.
2. Запускает `PlaywrightExecutor`.
3. Переходит по указанному URL с помощью `PlaywrightExecutor`.
4. Запускает сканирование с помощью `super().run(url)`.
5. Получает контекст сканирования.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время запуска или выполнения краулера.

```
Логирование запуска
    ↓
Запуск PlaywrightExecutor
    ↓
Переход по URL
    ↓
Запуск сканирования
    ↓
Получение контекста
```

### `current_url`

```python
@property
def current_url(self) -> Optional[str]
```

**Назначение**:
Возвращает текущий URL браузера.

**Возвращает**:
- `Optional[str]`: Текущий URL или `None`, если URL не удалось получить.

**Как работает функция**:
1. Проверяет, существует ли контекст и страница.
2. Если да, возвращает текущий URL страницы.
3. Если нет, возвращает `None`.

```
Проверка контекста и страницы
    ↓
Возврат URL или None
```

### `get_page_content`

```python
def get_page_content(self) -> Optional[str]
```

**Назначение**:
Возвращает HTML-содержимое текущей страницы.

**Возвращает**:
- `Optional[str]`: HTML-содержимое страницы или `None`, если содержимое не удалось получить.

**Как работает функция**:
1. Проверяет, существует ли контекст и страница.
2. Если да, возвращает HTML-содержимое страницы.
3. Если нет, возвращает `None`.

```
Проверка контекста и страницы
    ↓
Возврат содержимого или None
```

### `get_element_content`

```python
async def get_element_content(self, selector: str) -> Optional[str]
```

**Назначение**:
Возвращает внутреннее HTML-содержимое элемента на странице по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: Внутреннее HTML-содержимое элемента или `None`, если элемент не найден.

**Как работает функция**:
1. Проверяет, существует ли контекст и страница.
2. Если да, пытается получить элемент по селектору.
3. Возвращает внутреннее HTML-содержимое элемента.
4. Если элемент не найден или произошла ошибка, возвращает `None`.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время получения содержимого элемента.

```
Проверка контекста и страницы
    ↓
Получение элемента по селектору
    ↓
Возврат содержимого или None
```

### `get_element_value_by_xpath`

```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]
```

**Назначение**:
Возвращает текстовое значение элемента на странице по XPath.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден.

**Как работает функция**:
1. Проверяет, существует ли контекст и страница.
2. Если да, пытается получить элемент по XPath.
3. Возвращает текстовое значение элемента.
4. Если элемент не найден или произошла ошибка, возвращает `None`.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время получения значения элемента.

```
Проверка контекста и страницы
    ↓
Получение элемента по XPath
    ↓
Возврат значения или None
```

### `click_element`

```python
async def click_element(self, selector: str) -> None
```

**Назначение**:
Кликает на элемент на странице по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Как работает функция**:
1. Проверяет, существует ли контекст и страница.
2. Если да, пытается получить элемент по селектору и кликает на него.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время клика на элемент.

```
Проверка контекста и страницы
    ↓
Получение элемента по селектору и клик
```

### `execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
```

**Назначение**:
Выполняет локатор через executor.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str]): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

**Как работает функция**:
1. Вызывает метод `execute_locator` объекта `self.executor`, передавая параметры `locator`, `message` и `typing_speed`.
2. Возвращает результат выполнения локатора.

```
Вызов executor.execute_locator
    ↓
Возврат статуса выполнения
```

## Примеры

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