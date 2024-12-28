## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    - **Переменные**: Их типы и использование.
    - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**Класс `Driver`**

1.  **Инициализация `__init__`**:
    *   Принимает класс веб-драйвера (`webdriver_cls`), позиционные аргументы (`*args`) и ключевые аргументы (`**kwargs`).
    *   Проверяет, является ли `webdriver_cls` допустимым классом WebDriver, проверяя наличие метода `get`.
    *   Создает экземпляр `webdriver_cls` с использованием переданных аргументов и присваивает его `self.driver`.
    *   **Пример**: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`

2.  **Инициализация подкласса `__init_subclass__`**:
    *   Принимает аргумент `browser_name` и дополнительные аргументы `**kwargs`.
    *   Проверяет, был ли указан `browser_name`, вызывает исключение, если нет.
    *   Устанавливает атрибут `browser_name` для подкласса.
    *   **Пример**: Создание подкласса `class ChromeDriver(Driver, browser_name='chrome')`

3.  **Доступ к атрибутам драйвера `__getattr__`**:
    *   Принимает имя атрибута (`item`).
    *   Делегирует доступ к атрибуту экземпляру веб-драйвера (`self.driver`).
    *   **Пример**: `driver.page_source` вызовет `self.driver.page_source`.

4.  **Прокрутка страницы `scroll`**:
    *   Принимает количество прокруток (`scrolls`), размер прокрутки (`frame_size`), направление (`direction`) и задержку (`delay`).
    *   Внутренняя функция `carousel` выполняет прокрутку в заданном направлении.
    *   Вызывает `carousel` в зависимости от `direction` (forward, backward, both).
        *   **Пример**: `driver.scroll(scrolls=2, direction='down')` - прокрутит 2 раза вниз.
        *   **Пример**: `driver.scroll(scrolls=1, direction='both')` - прокрутит 1 раз вниз и 1 раз вверх.

5.  **Определение языка страницы `locale`**:
    *   Ищет мета-тег языка. Если находит, возвращает значение.
    *   Если мета-тег не найден, вызывает метод `get_page_lang` из driver.
    *   Если и этот метод не возвращает язык, возвращает `None`.
        *   **Пример**: `language = driver.locale` - попытается получить язык страницы.

6.  **Переход по URL `get_url`**:
    *   Принимает URL (`url`).
    *   Сохраняет текущий URL в `_previous_url`.
    *   Переходит по указанному URL, используя `self.driver.get(url)`.
    *   Ожидает загрузки страницы (пока `ready_state` не станет `complete`).
    *   Если URL отличается от предыдущего, сохраняет `_previous_url` в `self.previous_url`.
    *   Сохраняет куки локально с помощью `self._save_cookies_localy()`.
    *   Возвращает `True` при успешном переходе, иначе `False`.
        *   **Пример**: `driver.get_url('https://example.com')` - переходит на страницу example.com.

7.  **Открытие новой вкладки `window_open`**:
    *   Открывает новую вкладку с помощью JavaScript (`window.open();`).
    *   Переключается на новую вкладку.
    *   Если `url` указан, переходит на этот URL в новой вкладке.
        *   **Пример**: `driver.window_open('https://newtab.com')` - открывает новую вкладку с newtab.com.

8.  **Ожидание `wait`**:
    *   Принимает задержку в секундах (`delay`).
    *   Использует `time.sleep(delay)` для паузы.
        *   **Пример**: `driver.wait(delay=1)` - приостанавливает на 1 секунду.

9.  **Сохранение куки локально `_save_cookies_localy`**:
    *   Пытается сохранить текущие куки веб-драйвера в файл (`gs.cookies_filepath`) с помощью `pickle`.
    *   **Пример**: Метод вызывается внутри `get_url`, сохраняя куки после перехода.

10. **Извлечение HTML-контента `fetch_html`**:
    *   Принимает URL (`url`).
    *   Если URL начинается с `file://`:
        *   Извлекает путь к файлу.
        *   Читает содержимое файла в переменную `self.html_content`.
        *   Возвращает `True` в случае успеха, `False` если файл не найден или ошибка чтения.
    *   Если URL начинается с `http://` или `https://`:
        *   Использует `get_url` для перехода по URL.
        *   Присваивает `self.html_content` содержимое `self.page_source`.
        *   Возвращает `True` если контент получен.
    *   Возвращает `False` в случае ошибки.
        *   **Пример**: `driver.fetch_html('file://C:/example.html')` - загрузит HTML из файла.
        *   **Пример**: `driver.fetch_html('https://example.com')` - загрузит HTML с веб-страницы.

## <mermaid>

```mermaid
flowchart TD
    classDef classStyle fill:#f9f,stroke:#333,stroke-width:2px
    classDef methodStyle fill:#ccf,stroke:#333,stroke-width:2px
    classDef propertyStyle fill:#cfc,stroke:#333,stroke-width:2px
    
    Start[Start] --> DriverInit
    
    subgraph Driver Class
    	DriverInit[<code>__init__</code><br> Initialize Driver Instance]:::methodStyle
        DriverInit --> InitSubclass[<code>__init_subclass__</code><br> Setup Browser Name]:::methodStyle
    	InitSubclass --> GetAttr[<code>__getattr__</code><br> Access Driver Attributes]:::methodStyle
		GetAttr --> Scroll[<code>scroll</code><br> Scroll Page]:::methodStyle
        Scroll --> Carousel[<code>carousel</code><br> Scroll Logic (nested func)]:::methodStyle
		Scroll --> ScrollErrorCheck[Scroll Error Check]
		Carousel --> ScrollErrorCheck
        ScrollErrorCheck -- "Error" --> LogScrollError[Log Scroll Error]
		ScrollErrorCheck -- "Success" --> ScrollEnd[End Scroll]
		ScrollEnd --> Locale[<code>locale</code><br> Get Page Locale]:::propertyStyle
		Locale --> GetMetaLang[Get Meta Language]
		GetMetaLang -- "Success" --> MetaLangEnd[MetaLang End]
		GetMetaLang -- "Error" --> GetPageLang[Get Page Lang]
		GetPageLang -- "Success" --> PageLangEnd[PageLang End]
		GetPageLang -- "Error" --> GetLocaleEnd[Get Locale End (None)]
		MetaLangEnd --> GetLocaleEnd
		PageLangEnd --> GetLocaleEnd
		
        GetLocaleEnd --> GetUrl[<code>get_url</code><br> Navigate to URL]:::methodStyle
        GetUrl --> SavePrevUrl[Save Previous URL]
        SavePrevUrl --> WebDriverGet[<code>self.driver.get(url)</code>]
        WebDriverGet --> AwaitReadyState[Await <code>ready_state = 'complete'</code>]
        AwaitReadyState --> CheckUrlChange[Check if URL changed]
        CheckUrlChange -- "Yes" --> SaveUrlPrev[Save Previous URL]
        CheckUrlChange -- "No" --> SaveCookiesLocal[<code>_save_cookies_localy</code><br> Save Cookies]:::methodStyle
		SaveUrlPrev --> SaveCookiesLocal
        SaveCookiesLocal --> GetUrlEnd[Get URL End]
        GetUrl --"Error WebDriverException"--> LogWebDriverError[Log WebDriverException]
        GetUrl --"Error InvalidArgumentException"--> LogInvalidArgError[Log InvalidArgumentException]
        GetUrl -- "Error Other" --> LogGetUrlError[Log Get URL Error]
        LogWebDriverError --> GetUrlEnd
        LogInvalidArgError --> GetUrlEnd
        LogGetUrlError --> GetUrlEnd
        
        GetUrlEnd --> WindowOpen[<code>window_open</code><br> Open New Window]:::methodStyle
        WindowOpen --> ExecuteScript[<code>self.execute_script('window.open();')</code>]
        ExecuteScript --> SwitchToWindow[<code>self.switch_to.window(self.window_handles[-1])</code>]
        SwitchToWindow --> OptionalGetUrl[Optional URL]
        OptionalGetUrl -- "Yes" --> WebDriverGet2[<code>self.driver.get(url)</code>]
        OptionalGetUrl -- "No" --> WindowOpenEnd[Window Open End]
		WebDriverGet2 --> WindowOpenEnd
        
        WindowOpenEnd --> Wait[<code>wait</code><br> Wait for Delay]:::methodStyle
        Wait --> Sleep[<code>time.sleep(delay)</code>]
        Sleep --> WaitEnd[Wait End]
        
        WaitEnd --> FetchHtml[<code>fetch_html</code><br> Fetch HTML Content]:::methodStyle
        FetchHtml --> CheckUrlProtocol[Check URL Protocol]
		CheckUrlProtocol -- "file://" --> FetchFromFile[Fetch HTML from File]
        CheckUrlProtocol -- "http:// or https://" --> FetchFromUrl[Fetch HTML from URL]
        CheckUrlProtocol -- "Other" --> LogFetchHtmlError[Log Fetch HTML Error]
        FetchFromFile --> ReadLocalFile[Read HTML from local file]
        ReadLocalFile -- "Success" --> FetchHtmlSuccess[Set self.html_content and end]
        ReadLocalFile -- "Error" --> LogReadFileError[Log Read File Error]
        LogReadFileError --> FetchHtmlEnd[End Fetch HTML]
        FetchFromUrl --> GetUrlFromFetch[<code>self.get_url(url)</code>]
        GetUrlFromFetch -- "Success" --> SetPageSource[Set <code>self.html_content = self.page_source</code>]
        GetUrlFromFetch -- "Error" --> LogGetUrlErrorFetch[Log Get URL Error]
        SetPageSource --> FetchHtmlSuccess
		LogGetUrlErrorFetch --> FetchHtmlEnd
        FetchHtmlSuccess --> FetchHtmlEnd
        LogFetchHtmlError --> FetchHtmlEnd
    end
    
	DriverInit:::classStyle
	
    Start --> DriverInit
```

### <объяснение>

**Импорты:**

*   `time`: Используется для функции `sleep` в методе `wait`, чтобы добавить задержку.
*   `copy`: Используется для создания копии URL в методе `get_url`, чтобы сохранить предыдущий URL до перехода на новый.
*   `pickle`: Используется для сериализации и десериализации объектов Python, в данном случае - для сохранения куки в файл и загрузки из файла.
*   `re`: Используется для работы с регулярными выражениями в методе `fetch_html` для извлечения пути к локальному файлу.
*   `typing.Optional`: Используется для определения типов переменных, которые могут принимать значение `None`, например `locale`, `html_content`.
*   `selenium.webdriver.remote.webdriver.WebDriverException`,  `selenium.common.exceptions.InvalidArgumentException`: Эти исключения используются для обработки конкретных ошибок, связанных с Selenium WebDriver.
*   `selenium.webdriver.common.by.By`: Используется для поиска элементов на странице через CSS-селекторы
*   `Path` from `pathlib`: Используется для работы с путями к файлам в методе `fetch_html`.

Все эти импорты, за исключением стандартных библиотек, являются частью экосистемы Selenium или Python, необходимых для работы веб-драйверов.

**Класс `Driver`:**

*   **Роль:** Класс `Driver` предоставляет абстракцию над конкретными веб-драйверами Selenium (Chrome, Firefox и т.д.). Он содержит общую логику, необходимую для управления веб-драйвером: инициализация, навигация, работа с куки, обработка исключений, и т.д.
*   **Атрибуты:**
    *   `self.driver`: Экземпляр веб-драйвера, который был передан в конструкторе.
    *   `self.previous_url`: Сохраняет предыдущий URL, который был посещен.
    *    `self.html_content`: Сохраняет HTML контент, загруженный через `fetch_html`
    *    `self.browser_name`: Имя браузера, заданное в подклассе.
*   **Методы:**
    *   `__init__`: Конструктор класса, инициализирует экземпляр WebDriver.
    *   `__init_subclass__`: Метод для инициализации подклассов, гарантирует наличие `browser_name`.
    *   `__getattr__`: Позволяет перенаправлять доступ к атрибутам экземпляра `self.driver`.
    *   `scroll`: Выполняет прокрутку страницы.
    *   `locale`: Определяет язык страницы.
    *   `get_url`: Переходит по URL.
    *   `window_open`: Открывает новую вкладку.
    *   `wait`: Добавляет задержку.
    *   `_save_cookies_localy`: Сохраняет куки локально.
    *  `fetch_html`: Извлекает HTML контент с файла или URL.

**Функции:**

*   `__init__(self, webdriver_cls, *args, **kwargs)`:
    *   **Аргументы:**
        *   `webdriver_cls`: Класс веб-драйвера (например, `selenium.webdriver.Chrome`).
        *   `*args`: Позиционные аргументы для инициализации драйвера.
        *   `**kwargs`: Ключевые аргументы для инициализации драйвера.
    *   **Возвращает:** `None`
    *   **Назначение:** Инициализирует экземпляр класса `Driver` с предоставленным веб-драйвером.
    *   **Пример:** `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`.
*   `__init_subclass__(cls, *, browser_name=None, **kwargs)`:
    *   **Аргументы:**
        *  `browser_name`: Имя браузера
        *   `**kwargs`: Дополнительные аргументы.
    *  **Возвращает**: `None`.
    *   **Назначение:** Инициализирует подкласс драйвера, требуя аргумент `browser_name`
*   `__getattr__(self, item)`:
    *   **Аргументы:** `item`: Имя атрибута.
    *   **Возвращает:** Значение атрибута, полученное от экземпляра `self.driver`.
    *   **Назначение:** Позволяет проксировать доступ к атрибутам веб-драйвера.
    *  **Пример:** `driver.page_source` перенаправляется к `self.driver.page_source`
*   `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool`:
    *   **Аргументы:**
        *   `scrolls`: Количество прокруток.
        *   `frame_size`: Размер прокрутки в пикселях.
        *   `direction`: Направление прокрутки (`both`, `down`, `up`).
        *   `delay`: Задержка между прокрутками.
    *   **Возвращает:** `True`, если прокрутка прошла успешно, `False` в противном случае.
    *   **Назначение:** Прокручивает страницу в указанном направлении.
    *  **Пример:** `driver.scroll(scrolls=2, direction='down', frame_size=300)`
*  `locale(self) -> Optional[str]`:
    *   **Аргументы:** Нет.
    *   **Возвращает:** Код языка, если найден, иначе `None`.
    *   **Назначение:** Определяет язык страницы.
    *  **Пример:** `lang = driver.locale`
*   `get_url(self, url: str) -> bool`:
    *   **Аргументы:**
        *   `url`: URL для перехода.
    *   **Возвращает:** `True`, если переход успешен, `False` в противном случае.
    *   **Назначение:** Переходит по указанному URL.
    *  **Пример:** `driver.get_url('https://example.com')`.
*   `window_open(self, url: Optional[str] = None) -> None`:
    *   **Аргументы:**
        *   `url`: URL для открытия в новой вкладке (необязательный).
    *   **Возвращает:** `None`.
    *   **Назначение:** Открывает новую вкладку и переключается на неё.
    *  **Пример:** `driver.window_open('https://newtab.com')`
*   `wait(self, delay: float = .3) -> None`:
    *   **Аргументы:**
        *   `delay`: Время задержки в секундах.
    *   **Возвращает:** `None`.
    *   **Назначение:** Ожидает указанное количество времени.
    *   **Пример:** `driver.wait(delay=1)`.
*   `_save_cookies_localy(self) -> None`:
    *   **Аргументы:** Нет.
    *   **Возвращает:** `None`.
    *   **Назначение:** Сохраняет куки веб-драйвера в локальный файл.
*  `fetch_html(self, url: str) -> Optional[bool]`:
    *    **Аргументы:**
        *   `url`: URL или путь к файлу для извлечения HTML.
    *    **Возвращает**: `True` в случае успеха, `False` в случае ошибки, `None` в случае неподдерживаемого протокола.
    *    **Назначение**: Извлекает HTML контент из файла или URL.
    *    **Пример**: `driver.fetch_html("file://C:/my_file.html")` или `driver.fetch_html("https://example.com")`

**Переменные:**

*   `webdriver_cls`: Класс WebDriver (например, `selenium.webdriver.Chrome`).
*   `args`: Позиционные аргументы, используемые при инициализации драйвера.
*   `kwargs`: Ключевые аргументы, используемые при инициализации драйвера.
*   `item`: Имя атрибута, к которому осуществляется доступ через `__getattr__`.
*   `scrolls`: Количество прокруток.
*   `frame_size`: Размер прокрутки в пикселях.
*   `direction`: Направление прокрутки.
*   `delay`: Задержка в секундах.
*   `url`: URL для перехода или открытия в новой вкладке.
*   `meta_language`: HTML-элемент `<meta>` с атрибутом `Content-Language`.
*   `_previous_url`: Сохраненный предыдущий URL.
*   `file_path`:  Путь к локальному файлу при `fetch_html`.
*    `cleaned_url`:  Путь к файлу без префикса `file://`
*    `match`:  Результат поиска регулярного выражения пути в `cleaned_url`

**Области для улучшения:**

1.  **Логирование:** Добавить больше контекста в логи сообщений, включая данные (например, текущий URL, параметры прокрутки).
2.  **Обработка исключений:** Рассмотреть более гранулярную обработку исключений для более точной диагностики проблем.
3.  **Повторные попытки:** Добавить механизмы повторных попыток для ситуаций, когда, например, страница не загружается с первого раза.
4.  **Зависимости:** Рассмотреть возможность инъекции зависимостей для большей гибкости и тестируемости.
5.  **Комментарии:** Добавить больше документации к классам и методам для лучшего понимания кода.
6.  **`_save_cookies_localy`**: Метод сейчас закомментирован в режиме debug. Это нужно исправить для корректного сохранения куки.
7.  **Состояния**: Необходимо добавить сохранение текущего состояния браузера (например, в виде JSON).

**Цепочка взаимосвязей с другими частями проекта:**

*   Класс `Driver` используется в других частях проекта, которые нуждаются в управлении веб-браузерами. Например, для веб-скрапинга или автоматизированного тестирования.
*   Зависимость от `src.gs` говорит о том, что класс использует глобальные настройки (путь к файлу для куки).
*   Класс `Driver` также имеет неявную зависимость от классов веб-драйверов `selenium.webdriver` (например, `Chrome`, `Firefox`).

Этот анализ предоставляет полное понимание структуры и функциональности модуля `driver.py`.