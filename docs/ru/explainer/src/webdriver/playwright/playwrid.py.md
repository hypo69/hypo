## <алгоритм>

1. **Инициализация `Playwrid`:**
    - Создается экземпляр класса `Playwrid` с возможностью передачи пользовательского `user_agent` и списка опций `options`.
    - Вызывается метод `_set_launch_options` для настройки опций запуска Playwright, таких как `headless` и `args`. Пример: `Playwrid(options=["--start-maximized"], user_agent="CustomAgent")`.
    - Создается экземпляр класса `PlaywrightExecutor`, который будет отвечать за управление браузером.
    - Вызывается конструктор родительского класса `PlaywrightCrawler`, передавая в него тип браузера.
    - Если в `PlaywrightCrawler` есть метод `set_launch_options`, вызываем его для установки параметров запуска.

2. **`_set_launch_options`:**
   - Получает значения `headless` и `options` из конфигурационного файла `playwrid.json` (`self.config`). Если их нет, устанавливает `headless` в `True` и `options` в пустой список.
    - Если предоставлен `user_agent`, добавляет его в словарь `launch_options`. Пример: `launch_options["user_agent"] = "CustomAgent"`.
    - Если предоставлен список `options`, добавляет их к списку `args` в `launch_options`. Пример: `launch_options['args'].extend(["--start-maximized"])`.
    - Возвращает сформированный словарь `launch_options`.

3. **`start(url)`:**
    - Запускает `PlaywrightExecutor` через `self.executor.start()`.
    - Переходит по указанному URL, используя `self.executor.goto(url)`.
    - Запускает основной цикл обхода, используя метод `super().run(url)`.
    - Сохраняет контекст `crawling_context` в `self.context`.
    - Обрабатывает возможные исключения, логируя ошибки.

4. **`current_url`:**
    - Возвращает текущий URL страницы из контекста `self.context.page.url`, если контекст существует. Иначе возвращает `None`.

5. **`get_page_content()`:**
    - Возвращает HTML-контент текущей страницы из контекста `self.context.page.content()`, если контекст существует. Иначе возвращает `None`.

6. **`get_element_content(selector)`:**
    - Ищет элемент на странице по CSS-селектору `selector`, используя `self.context.page.locator(selector)`.
    - Возвращает `inner_html()` контент найденного элемента.
    - В случае ошибки логирует предупреждение и возвращает `None`.

7. **`get_element_value_by_xpath(xpath)`:**
    - Ищет элемент на странице по XPath `xpath`, используя `self.context.page.locator(f'xpath={xpath}')`.
    - Возвращает `text_content()` найденного элемента.
    - В случае ошибки логирует предупреждение и возвращает `None`.

8. **`click_element(selector)`:**
    - Ищет элемент на странице по CSS-селектору `selector`, используя `self.context.page.locator(selector)`.
    - Кликает на найденный элемент `await element.click()`.
    - В случае ошибки логирует предупреждение.

9. **`execute_locator(locator, message, typing_speed)`:**
    - Вызывает метод `execute_locator` класса `PlaywrightExecutor`, передавая ему данные `locator`, сообщение `message` и скорость печати `typing_speed`.

10. **Пример использования:**
    - Создается экземпляр `Playwrid` с опцией `--headless`.
    - Вызывается метод `start` для загрузки страницы `https://www.example.com`.
    - Используются методы для получения HTML контента страницы, контента элементов по селектору и xpath.
    - Производится клик по элементу.
    - Используется метод `execute_locator` для взаимодействия с элементами.

## <mermaid>

```mermaid
flowchart TD
    subgraph Playwrid Class
        A[Playwrid<br>Initialize with user_agent, options]
        B[Set Launch Options:<br>_set_launch_options]
        C[Start Crawler:<br>start(url)]
        D[Get Current URL:<br>current_url]
        E[Get Page Content:<br>get_page_content()]
        F[Get Element Content by CSS:<br>get_element_content(selector)]
        G[Get Element Value by XPath:<br>get_element_value_by_xpath(xpath)]
        H[Click Element by CSS:<br>click_element(selector)]
        I[Execute Locator:<br>execute_locator(locator, message, typing_speed)]
    end

    subgraph PlaywrightExecutor Class
    J[PlaywrightExecutor<br>Initialize]
        K[Start Executor:<br>start()]
        L[Navigate to URL:<br>goto(url)]
        M[Execute Locator in browser:<br>execute_locator(locator, message, typing_speed)]
    end

     A --> B
     A --> J
     B --> C
     C --> K
     C --> L
     C --> D
     C --> E
     C --> F
     C --> G
     C --> H
     C --> I
     I --> M

     K --> L

    subgraph header.py
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    end
```

**Описание зависимостей `mermaid`:**

- **`Playwrid Class`:** Этот блок представляет основной класс `Playwrid`, который наследуется от `PlaywrightCrawler`.
    - `Playwrid`: Инициализирует класс, принимает пользовательский агент и опции.
    - `_set_launch_options`: Настраивает параметры запуска браузера, такие как `headless` и `args`.
    - `start(url)`: Запускает краулер, переходит по URL и сохраняет контекст.
    - `current_url`: Возвращает текущий URL страницы.
    - `get_page_content()`: Возвращает HTML контент страницы.
    - `get_element_content(selector)`: Возвращает HTML контент элемента по CSS-селектору.
    - `get_element_value_by_xpath(xpath)`: Возвращает текстовое значение элемента по XPath.
    - `click_element(selector)`: Кликает по элементу на странице по CSS-селектору.
    - `execute_locator(locator, message, typing_speed)`: Выполняет действия, описанные в `locator` через `PlaywrightExecutor`.
- **`PlaywrightExecutor Class`:** Этот блок представляет класс `PlaywrightExecutor`, который управляет браузером.
    - `PlaywrightExecutor`: Инициализирует класс.
    - `start()`: Запускает браузер.
    - `goto(url)`: Переходит по указанному URL.
    - `execute_locator(locator, message, typing_speed)`: Выполняет действия с элементами на странице, используя `locator`, `message` и `typing_speed`.
- **Связи:**
    - `Playwrid` вызывает методы `_set_launch_options`, `start`, `current_url`, `get_page_content`, `get_element_content`, `get_element_value_by_xpath`, `click_element` и `execute_locator` для взаимодействия с браузером.
    - `Playwrid` создает экземпляр `PlaywrightExecutor` и вызывает его методы `start`, `goto`, и `execute_locator` для управления браузером.
    - `PlaywrightExecutor` вызывает методы Playwright для управления браузером.
- **`header.py`**:
   - `Start`: Начало выполнения скрипта `header.py`.
   - `Header`: Определение корневой директории проекта.
   - `import`: Импорт глобальных настроек из `src.gs`.

## <объяснение>

**Импорты:**
- `asyncio`: Используется для асинхронного программирования, позволяя выполнять неблокирующие операции.
- `pathlib.Path`:  Предоставляет объектно-ориентированный способ работы с путями к файлам и директориям.
- `typing.Optional, Dict, Any, List`:  Используются для аннотации типов, что делает код более понятным и проверяемым.
    - `Optional`: Указывает, что переменная может иметь значение `None`.
    - `Dict`: Словарь с произвольными ключами и значениями.
    - `Any`: Указывает на любой тип данных.
    - `List`: Список элементов.
- `types.SimpleNamespace`: Создает простые объекты, доступ к атрибутам которых осуществляется через точку.
- `crawlee.playwright_crawler.PlaywrightCrawler, PlaywrightCrawlingContext`: Импортируются классы и типы из библиотеки `crawlee`, отвечающие за работу с Playwright и контекстами обхода.
- `header`: Импортирует модуль `header`, который, вероятно, определяет корневую директорию проекта.
- `src.gs`: Импортирует глобальные настройки проекта, предположительно из модуля `gs` в пакете `src`.
- `src.webdriver.playwright.executor.PlaywrightExecutor`:  Импортирует класс `PlaywrightExecutor` из модуля `executor`, который отвечает за выполнение операций в браузере.
- `src.webdriver.js.JavaScript`: Импортирует класс `JavaScript` для работы с JavaScript кодом.
- `src.utils.jjson.j_loads_ns`: Импортирует функцию `j_loads_ns` для загрузки JSON-конфигурации в `SimpleNamespace`.
- `src.logger.logger.logger`: Импортирует объект `logger` для логирования сообщений.

**Класс `Playwrid`:**

- **Назначение:** Представляет собой расширение класса `PlaywrightCrawler` и предоставляет дополнительную функциональность для управления браузером Playwright.
- **Атрибуты:**
    - `driver_name`: Строка, идентифицирующая драйвер (по умолчанию `'playwrid'`).
    - `base_path`: `Path`, представляющий путь к каталогу `playwright` внутри `webdriver`.
    - `config`: `SimpleNamespace`, содержащий конфигурацию из файла `playwrid.json`.
    - `context`: Контекст обхода, который будет установлен после запуска краулера.
- **Методы:**
    - `__init__`: Конструктор класса, инициализирует параметры запуска браузера.
        - `user_agent`: Опциональная строка user-agent.
        - `options`: Опциональный список опций командной строки для запуска браузера.
        - Создает экземпляр `PlaywrightExecutor`.
        - Вызывает конструктор родительского класса `PlaywrightCrawler`, передавая ему тип браузера.
        - Вызывает `set_launch_options`, если метод доступен в `PlaywrightCrawler` для установки параметров запуска.
    - `_set_launch_options`: Настраивает опции запуска браузера, такие как `headless` и `args`, на основе конфигурации и переданных аргументов.
        - Принимает `user_agent` и `options`.
        - Создает словарь `launch_options`, включающий `headless` и `args`.
        - Добавляет `user_agent` если он передан.
        - Расширяет `args` опциями из аргумента `options`, если такие переданы.
        - Возвращает настроенный словарь `launch_options`.
    - `start(url)`: Запускает браузер, переходит по указанному URL и запускает краулер.
        - Запускает `PlaywrightExecutor` через `self.executor.start()`.
        - Вызывает `self.executor.goto(url)` для перехода по URL.
        - Запускает `super().run(url)` для старта обхода страницы.
        - Сохраняет контекст обхода `self.crawling_context` в `self.context`.
        - Обрабатывает исключения, логируя их через `logger.critical`.
    - `current_url`: Возвращает текущий URL страницы из контекста `self.context`.
    - `get_page_content`: Возвращает HTML-содержимое текущей страницы из контекста `self.context`.
    - `get_element_content(selector)`: Возвращает внутреннее HTML-содержимое элемента по CSS-селектору.
        - Находит элемент с помощью `self.context.page.locator(selector)`.
        - Возвращает inner_html() контент элемента.
        - Логирует предупреждение и возвращает None в случае ошибки.
    - `get_element_value_by_xpath(xpath)`: Возвращает текстовое содержимое элемента по XPath.
        - Находит элемент с помощью `self.context.page.locator(f'xpath={xpath}')`.
        - Возвращает text_content() элемента.
        - Логирует предупреждение и возвращает None в случае ошибки.
    - `click_element(selector)`: Кликает по элементу на странице по CSS-селектору.
        - Находит элемент с помощью `self.context.page.locator(selector)`.
        - Кликает на элемент с помощью `await element.click()`.
        - Логирует предупреждение в случае ошибки.
    -  `execute_locator(locator, message, typing_speed)`: Выполняет действие с элементом через `PlaywrightExecutor`.

**Функции:**
- `main`:  Асинхронная функция, демонстрирующая использование класса `Playwrid`.
    - Создает экземпляр `Playwrid` с опцией `--headless`.
    - Запускает браузер и переходит на `https://www.example.com`.
    - Выводит HTML-содержимое страницы, контент элемента `h1`, значение элемента `title` и кликает по элементу `button` (если он есть).
    -  Использует метод `execute_locator` для получения названия товара и клика на элемент.

**Переменные:**
- `driver_name`: Имя драйвера.
- `base_path`: Базовый путь к каталогу драйвера `webdriver/playwright`.
- `config`: Объект `SimpleNamespace` с конфигурацией из файла `playwrid.json`.
- `context`: Контекст обхода страницы, полученный после запуска краулера.
- `launch_options`: Словарь, содержащий опции запуска браузера.
- `executor`: Экземпляр класса `PlaywrightExecutor` для управления браузером.

**Цепочка взаимосвязей:**

1.  **`Playwrid`** (текущий файл) наследуется от **`PlaywrightCrawler`** из `crawlee`.
2.  **`Playwrid`** использует **`PlaywrightExecutor`** из `src.webdriver.playwright.executor` для управления браузером.
3.  **`Playwrid`** использует `j_loads_ns` из `src.utils.jjson` для загрузки конфигурации из `playwrid.json`.
4.  **`Playwrid`** использует **`header`** для определения корневого каталога проекта, который импортирует `src.gs` для глобальных настроек.
5.  **`Playwrid`** использует **`logger`** из `src.logger.logger` для логирования сообщений.
6.  **`Playwrid`** обращается к методам `PlaywrightExecutor`, для управления браузером, например, переходит по URL (`goto`), выполняет действия с элементами (`execute_locator`) и так далее.
7.  В свою очередь, `PlaywrightExecutor` вызывает методы Playwright для реального управления браузером.
8.  `main` функция является примером использования `Playwrid`, демонстрируя его основные возможности.

**Потенциальные ошибки и улучшения:**

-   В конструкторе `__init__` класса `Playwrid` проверяется наличие метода `set_launch_options` в `PlaywrightCrawler`. Если метод отсутствует, то параметры запуска не будут установлены.
-   Не все методы обрабатывают возможные исключения, например, `current_url` и `get_page_content` не обрабатывают исключения, если `self.context` равен None.
-   Используется `hasattr` для проверки наличия параметров в `config`. Можно было бы упростить чтение настроек через `getattr(self.config, 'headless', True)` с дефолтными значениями.
-   Логирование ошибок могло бы быть более детализированным (например, выводить стек ошибки).
-   Пример использования в `if __name__ == "__main__":` не закрывает браузер. Необходимо добавить явное закрытие браузера после окончания работы.
-   Не все методы асинхронны, хотя выполняют операции, которые могли бы быть асинхронными.
-   Можно добавить обработку таймаутов для операций с элементами, например, при клике или получении контента.