## \\file /src/webdriver/playwright/executor.py

### **1. <алгоритм>**:

Этот код реализует класс `PlaywrightExecutor`, который использует библиотеку Playwright для автоматизации взаимодействия с веб-страницами.

1.  **Инициализация (`__init__`)**:
    *   При создании экземпляра класса `PlaywrightExecutor` указывается тип браузера (`browser_type`, по умолчанию 'chromium').
    *   Загружается конфигурация из файла `playwrid.json` в объект `SimpleNamespace`.
2.  **Запуск (`start`)**:
    *   Инициализируется Playwright.
    *   Запускается браузер указанного типа в headless-режиме с заданными опциями конфигурации.
    *   Создается новая страница в браузере.
3.  **Остановка (`stop`)**:
    *   Закрывается страница и браузер Playwright.
    *   Останавливается экземпляр Playwright.
4.  **Выполнение локатора (`execute_locator`)**:
    *   Принимает данные локатора (в виде `dict` или `SimpleNamespace`), сообщение, скорость печати и параметры таймаута.
    *   Преобразует `dict` в `SimpleNamespace`, если передан `dict`.
    *   Вызывает внутреннюю функцию `_parse_locator` для обработки инструкций локатора.
5.  **Разбор локатора (`_parse_locator`)**:
    *   Обрабатывает различные типы локаторов на основе атрибутов `locator.attribute`, `locator.by` и `locator.selector`.
    *   Если указаны и `event`, и `attribute`, и `mandatory` отсутствует, локатор пропускается.
    *   Если `locator.by` имеет значение `"VALUE"`, извлекается атрибут элемента.
    *   Вызывает `execute_event`, `get_attribute_by_locator` или `get_webelement_by_locator` в зависимости от атрибутов локатора.
    *   Если `locator.selector` и `locator.by` являются списками, обрабатывает их как пары, извлекая элементы и объединяя их.
6.  **Оценка локатора (`evaluate_locator`)**:
    *   Оценивает атрибуты локатора.
    *   Если атрибут является списком, оценивает каждый элемент списка.
7.  **Получение атрибута по локатору (`get_attribute_by_locator`)**:
    *   Получает атрибут элемента, найденного по локатору.
    *   Использует `get_webelement_by_locator` для получения веб-элемента.
    *   Обрабатывает строку атрибута в формате словаря (например, "{attr1:attr2}").
8.  **Получение веб-элемента по локатору (`get_webelement_by_locator`)**:
    *   Ищет веб-элемент на странице, используя `locator.selector` и `locator.by` (поддерживает XPath).
    *   Возвращает элемент или список элементов, в зависимости от значения `locator.if_list` ('all', 'first', 'last', 'even', 'odd', list, int).
9.  **Получение скриншота веб-элемента (`get_webelement_as_screenshot`)**:
    *   Делает скриншот веб-элемента, найденного по локатору.
    *   Использует `get_webelement_by_locator` для получения веб-элемента.
10. **Выполнение события (`execute_event`)**:
    *   Выполняет событие (например, "click()", "pause()", "upload_media()", "screenshot()", "clear()", "send_keys()", "type()") на элементе, найденном по локатору.
11. **Отправка сообщения (`send_message`)**:
    *   Отправляет сообщение в веб-элемент, используя `element.type()`.
    *   Поддерживает скорость печати (typing speed).
12. **Переход по URL (`goto`)**:
    *   Переходит по указанному URL, используя `page.goto()`.

```mermaid
flowchart TD
    A[Инициализация PlaywrightExecutor] --> B{Загрузка конфигурации из playwrid.json};
    B --> C{Запуск браузера};
    C --> D{Создание новой страницы};
    D --> E[Выполнение локатора (execute_locator)];
    E --> F{Преобразование dict в SimpleNamespace};
    F --> G{Разбор локатора (_parse_locator)};
    G --> H{Оценка локатора (evaluate_locator)};
    H --> I{Получение атрибута (get_attribute_by_locator)};
    I --> J{Получение веб-элемента (get_webelement_by_locator)};
    J --> K{Скриншот веб-элемента (get_webelement_as_screenshot)};
    K --> L{Выполнение события (execute_event)};
    L --> M{Отправка сообщения (send_message)};
    M --> N{Переход по URL (goto)};
```

### **2. <mermaid>**:

```mermaid
flowchart TD
    A[PlaywrightExecutor: init] --> B{j_loads_ns("playwrid.json")};
    B --> C[PlaywrightExecutor: start];
    C --> D{async_playwright().start()};
    D --> E{browser.launch(headless=True, args=config.options)};
    E --> F{browser.new_page()};
    F --> G[PlaywrightExecutor: stop];
    G --> H{page.close()};
    H --> I{driver.stop()};
    I --> J[PlaywrightExecutor: execute_locator];
    J --> K{_parse_locator(locator, message)};
    K --> L[PlaywrightExecutor: evaluate_locator];
    L --> M{async _evaluate(attr)};
    M --> N[PlaywrightExecutor: get_attribute_by_locator];
    N --> O{get_webelement_by_locator(locator)};
    O --> P{_parse_dict_string(attr_string)};
    P --> Q{_get_attribute(el, attr)};
    Q --> R{_get_attributes_from_dict(element, attr_dict)};
    R --> S[PlaywrightExecutor: get_webelement_by_locator];
    S --> T{page.locator(locator.selector)};
    T --> U[PlaywrightExecutor: get_webelement_as_screenshot];
    U --> V{webelement.screenshot()};
    V --> W[PlaywrightExecutor: execute_event];
    W --> X{element.click()};
    X --> Y{element.set_input_files(message)};
    Y --> Z{element.clear()};
    Z --> AA{element.type(key)};
    AA --> BB[PlaywrightExecutor: send_message];
    BB --> CC{element.type(message)};
    CC --> DD[PlaywrightExecutor: goto];
    DD --> EE{page.goto(url)};
```

**Объяснение диаграммы:**

*   `PlaywrightExecutor: init`: Инициализация класса, загрузка конфигурации из JSON.
*   `PlaywrightExecutor: start`: Запуск браузера Playwright.
    *   `async_playwright().start()`: Запускает Playwright.
    *   `browser.launch(...)`: Запускает браузер с заданными параметрами.
    *   `browser.new_page()`: Создает новую страницу.
*   `PlaywrightExecutor: stop`: Остановка браузера Playwright.
    *   `page.close()`: Закрывает текущую страницу.
    *   `driver.stop()`: Останавливает драйвер.
*   `PlaywrightExecutor: execute_locator`: Выполнение локатора.
    *   `_parse_locator(locator, message)`: Внутренняя функция для разбора локатора.
*   `PlaywrightExecutor: evaluate_locator`: Оценка локатора.
    *   `async _evaluate(attr)`: Асинхронная оценка атрибута.
*   `PlaywrightExecutor: get_attribute_by_locator`: Получение атрибута по локатору.
    *   `get_webelement_by_locator(locator)`: Получение веб-элемента по локатору.
    *   `_parse_dict_string(attr_string)`: Разбор строки в формат словаря.
    *   `_get_attribute(el, attr)`: Получение атрибута элемента.
    *   `_get_attributes_from_dict(element, attr_dict)`: Получение нескольких атрибутов элемента на основе словаря.
*   `PlaywrightExecutor: get_webelement_by_locator`: Получение веб-элемента по локатору.
    *   `page.locator(locator.selector)`: Поиск элемента на странице.
*   `PlaywrightExecutor: get_webelement_as_screenshot`: Получение скриншота веб-элемента.
    *   `webelement.screenshot()`: Создание скриншота элемента.
*   `PlaywrightExecutor: execute_event`: Выполнение события.
    *   `element.click()`: Клик по элементу.
    *   `element.set_input_files(message)`: Загрузка файлов.
    *   `element.clear()`: Очистка поля.
    *   `element.type(key)`: Ввод текста.
*   `PlaywrightExecutor: send_message`: Отправка сообщения.
    *   `element.type(message)`: Ввод сообщения.
*   `PlaywrightExecutor: goto`: Переход по URL.
    *   `page.goto(url)`: Переход по URL.

### **3. <объяснение>**:

**Импорты:**

*   `asyncio`: Используется для асинхронного программирования.
*   `re`: Используется для работы с регулярными выражениями (например, при разборе `pause()` события).
*   `typing.Optional, typing.List, typing.Union`: Используются для аннотации типов.
*   `pathlib.Path`: Используется для работы с путями к файлам.
*   `playwright.async_api.async_playwright, playwright.async_api.Page, playwright.async_api.Locator`: Импортируются классы и функции из библиотеки Playwright для управления браузером, страницами и элементами.
*   `types.SimpleNamespace`: Используется для создания объектов, к атрибутам которых можно обращаться через точку.
*   `src.gs`: Глобальные настройки проекта. Определяет корневую директорию проекта.
*   `src.logger.logger`: Модуль логирования для записи информации о работе скрипта.
*   `src.utils.jjson.j_loads_ns`: Функция для загрузки JSON-файлов в `SimpleNamespace`.

**Классы:**

*   `PlaywrightExecutor`:
    *   **Роль**: Управляет взаимодействием с веб-страницами через Playwright.
    *   **Атрибуты**:
        *   `driver`: Экземпляр Playwright.
        *   `browser_type`: Тип используемого браузера (по умолчанию 'chromium').
        *   `page`: Текущая страница браузера.
        *   `config`: Конфигурация, загруженная из `playwrid.json`.
    *   **Методы**:
        *   `__init__`: Инициализирует класс, загружает конфигурацию.
        *   `start`: Запускает Playwright и браузер.
        *   `stop`: Останавливает Playwright и браузер.
        *   `execute_locator`: Выполняет действия с элементом на основе локатора.
        *   `evaluate_locator`: Оценивает атрибуты локатора.
        *   `get_attribute_by_locator`: Получает значение атрибута элемента.
        *   `get_webelement_by_locator`: Получает веб-элемент по локатору.
        *   `get_webelement_as_screenshot`: Получает скриншот веб-элемента.
        *   `execute_event`: Выполняет событие (клик, ввод текста и т.д.) на элементе.
        *   `send_message`: Отправляет сообщение в веб-элемент.
        *   `goto`: Переходит по указанному URL.

**Функции:**

*   `__init__(self, browser_type: str = 'chromium', **kwargs)`:
    *   **Аргументы**:
        *   `browser_type` (str): Тип браузера для запуска (по умолчанию 'chromium').
        *   `**kwargs`: Дополнительные аргументы.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Инициализирует экземпляр класса `PlaywrightExecutor`, устанавливая тип браузера и загружая конфигурацию из файла `playwrid.json`.
    *   **Пример**:
        ```python
        executor = PlaywrightExecutor(browser_type='firefox')
        ```
*   `async def start(self) -> None`:
    *   **Аргументы**: `None`
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Запускает Playwright и браузер.
    *   **Пример**:
        ```python
        await executor.start()
        ```
*   `async def stop(self) -> None`:
    *   **Аргументы**: `None`
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Останавливает Playwright и браузер.
    *   **Пример**:
        ```python
        await executor.stop()
        ```
*   `async def execute_locator(...) -> Union[str, list, dict, Locator, bool, None]`:
    *   **Аргументы**:
        *   `locator` (Union[dict, SimpleNamespace]): Данные локатора.
        *   `message` (Optional[str]): Сообщение для событий.
        *   `typing_speed` (float): Скорость печати.
        *   `timeout` (Optional[float]): Таймаут для поиска элемента.
        *   `timeout_for_event` (Optional[str]): Условие ожидания.
    *   **Возвращаемое значение**: Union[str, list, dict, Locator, bool, None]
    *   **Назначение**: Выполняет действия с элементом на основе локатора.
    *   **Пример**:
        ```python
        result = await executor.execute_locator(locator_data, message='example')
        ```
*   `async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`:
    *   **Аргументы**:
        *   `attribute` (str | List[str] | dict): Атрибут для оценки.
    *   **Возвращаемое значение**: Optional[str | List[str] | dict]
    *   **Назначение**: Оценивает атрибуты локатора.
    *   **Пример**:
        ```python
        result = await executor.evaluate_locator(attribute)
        ```
*   `async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]`:
    *   **Аргументы**:
        *   `locator` (dict | SimpleNamespace): Данные локатора.
    *   **Возвращаемое значение**: Optional[str | List[str] | dict]
    *   **Назначение**: Получает значение атрибута элемента.
    *   **Пример**:
        ```python
        attribute = await executor.get_attribute_by_locator(locator_data)
        ```
*   `async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]`:
    *   **Аргументы**:
        *   `locator` (dict | SimpleNamespace): Данные локатора.
    *   **Возвращаемое значение**: Optional[Locator | List[Locator]]
    *   **Назначение**: Получает веб-элемент по локатору.
    *   **Пример**:
        ```python
        element = await executor.get_webelement_by_locator(locator_data)
        ```
*   `async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]`:
    *   **Аргументы**:
        *   `locator` (dict | SimpleNamespace): Данные локатора.
        *   `webelement` (Optional[Locator]): Веб-элемент.
    *   **Возвращаемое значение**: Optional[bytes]
    *   **Назначение**: Получает скриншот веб-элемента.
    *   **Пример**:
        ```python
        screenshot = await executor.get_webelement_as_screenshot(locator_data)
        ```
*   `async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]`:
    *   **Аргументы**:
        *   `locator` (dict | SimpleNamespace): Данные локатора.
        *   `message` (Optional[str]): Сообщение для событий.
        *   `typing_speed` (float): Скорость печати.
    *   **Возвращаемое значение**: Union[str, List[str], bytes, List[bytes], bool]
    *   **Назначение**: Выполняет событие на элементе.
    *   **Пример**:
        ```python
        result = await executor.execute_event(locator_data, event='click()')
        ```
*   `async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool`:
    *   **Аргументы**:
        *   `locator` (dict | SimpleNamespace): Данные локатора.
        *   `message` (str): Сообщение для отправки.
        *   `typing_speed` (float): Скорость печати.
    *   **Возвращаемое значение**: bool
    *   **Назначение**: Отправляет сообщение в веб-элемент.
    *   **Пример**:
        ```python
        result = await executor.send_message(locator_data, message='hello')
        ```
*   `async def goto(self, url: str) -> None`:
    *   **Аргументы**:
        *   `url` (str): URL для перехода.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Переходит по указанному URL.
    *   **Пример**:
        ```python
        await executor.goto('https://example.com')
        ```

**Переменные:**

*   `self.driver`: Экземпляр Playwright. Используется для управления браузером.
*   `self.browser_type`: Тип браузера (например, 'chromium', 'firefox', 'webkit').
*   `self.page`: Текущая страница, с которой происходит взаимодействие.
*   `self.config`: Конфигурация, загруженная из JSON-файла.

**Потенциальные ошибки и области для улучшения:**

*   Обработка исключений: В некоторых местах обработка исключений выполняется с использованием `logger.debug`, что может быть недостаточно для критических ошибок. Рекомендуется использовать `logger.error` или `logger.critical` для более серьезных проблем.
*   Валидация входных данных: Недостаточная валидация входных данных (например, `locator`) может привести к непредсказуемому поведению.
*   Использование `j_loads_ns`: Правильное использование `j_loads_ns` для загрузки конфигурационных файлов улучшает читаемость и управляемость конфигурацией.
*   Обработка таймаутов: Параметры таймаута (`timeout`, `timeout_for_event`) не используются, что может привести к проблемам при работе с медленными веб-страницами.

**Взаимосвязи с другими частями проекта:**

*   `src.gs`: Используется для получения пути к конфигурационному файлу, что указывает на зависимость от глобальных настроек проекта.
*   `src.logger.logger`: Используется для логирования, что обеспечивает возможность отслеживания работы `PlaywrightExecutor`.
*   `src.utils.jjson.j_loads_ns`: Используется для загрузки конфигурации из JSON-файла, что упрощает управление параметрами `PlaywrightExecutor`.