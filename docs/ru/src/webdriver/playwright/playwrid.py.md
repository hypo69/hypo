# Модуль `src.webdriver.playwright.playwrid`

## Обзор

Модуль `src.webdriver.playwright.playwrid` предоставляет класс `Playwrid`, который является подклассом `PlaywrightCrawler` из библиотеки `crawlee`. Этот класс предназначен для выполнения задач веб-сканирования с использованием Playwright. Он предоставляет дополнительные возможности, такие как установка пользовательских настроек браузера, профилей и параметров запуска.

## Подробней

Модуль `Playwrid` расширяет возможности `PlaywrightCrawler`, добавляя гибкость в настройке запуска браузера и выполнении действий на веб-страницах. Он позволяет указывать параметры запуска, такие как `user_agent` и другие опции Playwright. Модуль использует `PlaywrightExecutor` для выполнения действий на странице, таких как переход по URL, получение контента и взаимодействие с элементами.

## Классы

### `Playwrid`

**Описание**:
Класс `Playwrid` является подклассом `PlaywrightCrawler` и предоставляет дополнительные функции для настройки и запуска Playwright-браузера.

**Наследует**:
- `PlaywrightCrawler`: Класс, предоставляющий базовую функциональность для сканирования веб-страниц с использованием Playwright.

**Атрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию 'playwrid'.
- `base_path` (Path): Путь к базовой директории модуля.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию из файла `playwrid.json`.
- `context`: Контекст сканирования, устанавливается в методе `start`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Playwrid`, настраивает параметры запуска браузера и создает экземпляр `PlaywrightExecutor`.
- `_set_launch_options`: Конфигурирует параметры запуска Playwright, включая `headless`, `args` и `user_agent`.
- `start`: Запускает сканер Playwrid и переходит по указанному URL.
- `current_url`: Возвращает текущий URL браузера.
- `get_page_content`: Возвращает HTML-содержимое текущей страницы.
- `get_element_content`: Возвращает HTML-содержимое элемента, найденного по CSS-селектору.
- `get_element_value_by_xpath`: Возвращает текстовое значение элемента, найденного по XPath.
- `click_element`: Кликает на элемент, найденный по CSS-селектору.
- `execute_locator`: Выполняет локатор через `PlaywrightExecutor`.

### `__init__`
```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None
```

**Назначение**:
Инициализирует экземпляр класса `Playwrid`.

**Параметры**:
- `user_agent` (Optional[str], optional): User-Agent, который будет использоваться в браузере. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций командной строки для запуска браузера. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PlaywrightCrawler`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PlaywrightCrawler`.

**Как работает функция**:

1.  Вызывается метод `_set_launch_options` для конфигурации параметров запуска браузера.
2.  Создается экземпляр класса `PlaywrightExecutor`, который будет использоваться для выполнения действий в браузере.
3.  Вызывается конструктор родительского класса `PlaywrightCrawler` с необходимыми параметрами.
4.  Если у класса `PlaywrightCrawler` есть метод `set_launch_options`, то вызывается он для установки параметров запуска.

**ASCII Flowchart**:

```
A[Вызов _set_launch_options]
|
B[Создание экземпляра PlaywrightExecutor]
|
C[Вызов конструктора PlaywrightCrawler]
|
D[Проверка наличия метода set_launch_options]
|
E[Вызов set_launch_options (если есть)]
```

**Примеры**:

```python
browser = Playwrid(options=["--headless"])
browser = Playwrid(user_agent="Custom User Agent", options=["--disable-gpu"])
```

### `_set_launch_options`
```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]
```

**Назначение**:
Конфигурирует параметры запуска браузера Playwright.

**Параметры**:
- `user_agent` (Optional[str], optional): User-Agent, который будет использоваться в браузере. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций командной строки для запуска браузера. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска Playwright.

**Как работает функция**:

1.  Создается словарь `launch_options` с базовыми параметрами запуска, такими как `headless` и `args`.
2.  Если передан `user_agent`, он добавляется в словарь `launch_options`.
3.  Если переданы дополнительные опции `options`, они добавляются к списку `args` в `launch_options`.

**ASCII Flowchart**:

```
A[Создание словаря launch_options]
|
B[Проверка наличия user_agent]
|
C[Добавление user_agent в launch_options (если есть)]
|
D[Проверка наличия options]
|
E[Добавление options в launch_options (если есть)]
```

**Примеры**:

```python
launch_options = self._set_launch_options(user_agent="Custom User Agent", options=["--disable-gpu"])
launch_options = self._set_launch_options()
```

### `start`
```python
async def start(self, url: str) -> None
```

**Назначение**:
Запускает сканер Playwrid и переходит по указанному URL.

**Параметры**:
- `url` (str): URL, по которому нужно перейти.

**Как работает функция**:

1.  Логируется информация о начале сканирования.
2.  Запускается `PlaywrightExecutor`.
3.  Выполняется переход по указанному URL с помощью `PlaywrightExecutor`.
4.  Запускается процесс сканирования с использованием `super().run(url)`.
5.  Получает контекст сканирования.
6.  Обрабатываются исключения, которые могут возникнуть в процессе.

**ASCII Flowchart**:

```
A[Логирование информации о начале сканирования]
|
B[Запуск PlaywrightExecutor]
|
C[Переход по URL с помощью PlaywrightExecutor]
|
D[Запуск процесса сканирования (super().run(url))]
|
E[Получение контекста сканирования]
|
F[Обработка исключений]
```

**Примеры**:

```python
await browser.start("https://www.example.com")
```

### `current_url`
```python
@property
def current_url(self) -> Optional[str]
```

**Назначение**:
Возвращает текущий URL браузера.

**Возвращает**:
- `Optional[str]`: Текущий URL или `None`, если URL недоступен.

**Как работает функция**:

1.  Проверяется, существует ли контекст сканирования и страница.
2.  Если да, возвращается текущий URL страницы.
3.  В противном случае возвращается `None`.

**ASCII Flowchart**:

```
A[Проверка наличия контекста и страницы]
|
B[Возврат текущего URL (если есть)]
|
C[Возврат None (если нет)]
```

**Примеры**:

```python
url = browser.current_url
```

### `get_page_content`
```python
def get_page_content(self) -> Optional[str]
```

**Назначение**:
Возвращает HTML-содержимое текущей страницы.

**Возвращает**:
- `Optional[str]`: HTML-содержимое страницы или `None`, если содержимое недоступно.

**Как работает функция**:

1.  Проверяется, существует ли контекст сканирования и страница.
2.  Если да, возвращается HTML-содержимое страницы.
3.  В противном случае возвращается `None`.

**ASCII Flowchart**:

```
A[Проверка наличия контекста и страницы]
|
B[Возврат HTML-содержимого (если есть)]
|
C[Возврат None (если нет)]
```

**Примеры**:

```python
content = browser.get_page_content()
```

### `get_element_content`
```python
async def get_element_content(self, selector: str) -> Optional[str]
```

**Назначение**:
Возвращает HTML-содержимое элемента, найденного по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Возвращает**:
- `Optional[str]`: HTML-содержимое элемента или `None`, если элемент не найден.

**Как работает функция**:

1.  Проверяется, существует ли контекст сканирования и страница.
2.  Если да, выполняется поиск элемента по CSS-селектору.
3.  Возвращается HTML-содержимое элемента.
4.  Обрабатываются исключения, которые могут возникнуть в процессе.
5.  Логируется предупреждение, если элемент не найден или произошла ошибка.

**ASCII Flowchart**:

```
A[Проверка наличия контекста и страницы]
|
B[Поиск элемента по CSS-селектору]
|
C[Возврат HTML-содержимого элемента]
|
D[Обработка исключений]
```

**Примеры**:

```python
element_content = await browser.get_element_content("h1")
```

### `get_element_value_by_xpath`
```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]
```

**Назначение**:
Возвращает текстовое значение элемента, найденного по XPath.

**Параметры**:
- `xpath` (str): XPath элемента.

**Возвращает**:
- `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден.

**Как работает функция**:

1.  Проверяется, существует ли контекст сканирования и страница.
2.  Если да, выполняется поиск элемента по XPath.
3.  Возвращается текстовое значение элемента.
4.  Обрабатываются исключения, которые могут возникнуть в процессе.
5.  Логируется предупреждение, если элемент не найден или произошла ошибка.

**ASCII Flowchart**:

```
A[Проверка наличия контекста и страницы]
|
B[Поиск элемента по XPath]
|
C[Возврат текстового значения элемента]
|
D[Обработка исключений]
```

**Примеры**:

```python
xpath_value = await browser.get_element_value_by_xpath("//head/title")
```

### `click_element`
```python
async def click_element(self, selector: str) -> None
```

**Назначение**:
Кликает на элемент, найденный по CSS-селектору.

**Параметры**:
- `selector` (str): CSS-селектор элемента.

**Как работает функция**:

1.  Проверяется, существует ли контекст сканирования и страница.
2.  Если да, выполняется поиск элемента по CSS-селектору.
3.  Выполняется клик на элемент.
4.  Обрабатываются исключения, которые могут возникнуть в процессе.
5.  Логируется предупреждение, если элемент не найден или произошла ошибка.

**ASCII Flowchart**:

```
A[Проверка наличия контекста и страницы]
|
B[Поиск элемента по CSS-селектору]
|
C[Клик на элемент]
|
D[Обработка исключений]
```

**Примеры**:

```python
await browser.click_element("button")
```

### `execute_locator`
```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool
```

**Назначение**:
Выполняет локатор через `PlaywrightExecutor`.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:
- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

**Как работает функция**:

1.  Вызывает метод `execute_locator` у экземпляра `PlaywrightExecutor` с переданными параметрами.

**ASCII Flowchart**:

```
A[Вызов self.executor.execute_locator]
```

**Примеры**:

```python
result = await browser.execute_locator(locator_data)
```

## Функции

В данном модуле не обнаружены отдельные функции, кроме методов класса `Playwrid`.

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

Эта секция кода демонстрирует пример использования класса `Playwrid`. Внутри асинхронной функции `main()` создается экземпляр `Playwrid`, запускается браузер, выполняются различные действия на странице (получение контента, клик по элементу), а также демонстрируется использование `execute_locator`.