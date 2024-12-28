## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:
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

### Класс `Driver`

1. **Инициализация (`__init__`)**:
    - Принимает класс веб-драйвера (`webdriver_cls`) и аргументы для его инициализации.
    - Проверяет, является ли `webdriver_cls` валидным классом веб-драйвера (имеет метод `get`).
    - Создает экземпляр веб-драйвера и сохраняет его в `self.driver`.

    *Пример*:
    ```python
    from selenium.webdriver import Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    ```

2. **Инициализация подкласса (`__init_subclass__`)**:
    - Проверяет, что при создании подкласса `Driver` указан аргумент `browser_name`.
    - Сохраняет `browser_name` как атрибут класса.
    *Пример*:
    ```python
        class ChromeDriver(Driver, browser_name='chrome'):
            pass
    ```

3. **Перенаправление атрибутов (`__getattr__`)**:
    - Перенаправляет обращение к атрибутам экземпляра `Driver` на соответствующий атрибут в `self.driver`.
        
     *Пример*:
      ```python
      driver.get('https://example.com') # вызывает driver.driver.get('https://example.com')
      ```
4. **Прокрутка страницы (`scroll`)**:
    - Принимает количество прокруток (`scrolls`), размер прокрутки (`frame_size`), направление (`direction`) и задержку (`delay`).
    - Вызывает внутреннюю функцию `carousel` для фактической прокрутки.
    -  `carousel`:
        - Прокручивает страницу заданное количество раз в заданном направлении (вверх, вниз или оба направления).
        - Использует JavaScript `window.scrollBy` для прокрутки.
        -  Делает паузу после каждой прокрутки
    - Возвращает `True`, если прокрутка прошла успешно, иначе `False`.

    *Пример*:
    ```python
    driver.scroll(scrolls=2, direction='down', frame_size=400, delay=0.5)
    ```

5. **Определение языка страницы (`locale`)**:
    - Пытается определить язык страницы из мета-тега `Content-Language`.
    - Если не удается, пытается получить язык с помощью JavaScript, вызывая метод `get_page_lang`
    - Возвращает код языка или `None`.

6. **Навигация (`get_url`)**:
    - Сохраняет текущий URL.
    - Переходит на заданный URL.
    - Ожидает полную загрузку страницы.
    - Обновляет `previous_url` и сохраняет cookies.
    - Возвращает `True`, если навигация успешна, иначе `False`.

    *Пример*:
    ```python
    driver.get_url('https://example.com/page')
    ```

7. **Открытие нового окна/вкладки (`window_open`)**:
    - Открывает новую вкладку.
    - Переключается на новую вкладку.
    - Если URL указан, открывает его в новой вкладке.

    *Пример*:
    ```python
    driver.window_open('https://example.com/newtab')
    ```

8. **Ожидание (`wait`)**:
    - Пауза на заданное время.

    *Пример*:
    ```python
    driver.wait(2) # задержка на 2 секунды
    ```
9.  **Сохранение cookies локально (`_save_cookies_localy`)**:
    - Сохраняет cookies веб-драйвера в файл (если не закомментирован).

10. **Получение HTML контента (`fetch_html`)**:
    -   Если URL начинается с `file://`, считывает HTML контент из локального файла.
    -   Если URL начинается с `http://` или `https://`, загружает контент с веб-страницы через `get_url` и сохраняет `page_source` в `html_content`.
    -  Возвращает True в случае успеха или None при неудаче

*Пример*:
    ```python
    driver.fetch_html('file:///path/to/localfile.html')
    driver.fetch_html('https://example.com/page')
    ```

### Поток данных

1. **Инициализация**:
    - Класс `Driver` получает класс веб-драйвера (например, `Chrome`) и аргументы.
    - Создает экземпляр веб-драйвера.

2.  **Навигация**:
    - Метод `get_url` использует `self.driver.get(url)` для перехода на страницу.
    -  `get_url` сохраняет cookies
    - Метод `fetch_html` получает HTML-контент через `get_url` или локальный файл.

3. **Прокрутка**:
    - Метод `scroll` использует JavaScript (`execute_script`) для прокрутки.
4. **Cookies**:
  - Метод `_save_cookies_localy` использует `self.driver.get_cookies()` для сохранения.

## <mermaid>

```mermaid
flowchart TD
    subgraph Driver Class
        Init["__init__ (webdriver_cls, *args, **kwargs)"]
        InitSubclass["__init_subclass__ (cls, *, browser_name=None, **kwargs)"]
        GetAttr["__getattr__ (item)"]
        Scroll["scroll(scrolls, frame_size, direction, delay)"]
        Locale["locale"]
        GetUrl["get_url(url)"]
        WindowOpen["window_open(url)"]
        Wait["wait(delay)"]
        SaveCookies["_save_cookies_localy()"]
        FetchHtml["fetch_html(url)"]
    end
    
    Init --> CheckWebDriver[Check webdriver_cls]
    CheckWebDriver -- "Valid WebDriver" --> CreateDriverInstance[Create driver instance]
    CheckWebDriver -- "Invalid WebDriver" --> RaiseTypeError[Raise TypeError]
    CreateDriverInstance --> InitSubclass
    
    InitSubclass --> CheckBrowserName[Check browser_name]
    CheckBrowserName -- "browser_name Specified" --> SetBrowserName[Set cls.browser_name]
    CheckBrowserName -- "browser_name not Specified" --> RaiseValueError[Raise ValueError]
    SetBrowserName --> GetAttr
    
    GetAttr --> DriverAttributeAccess[Access attribute on self.driver]
    
    Scroll --> CallCarousel[Call carousel()]
    CallCarousel --> ExecuteScript[Execute JavaScript scrollBy]
    ExecuteScript --> Wait
    
    Locale --> MetaTagCheck[Check meta tag for language]
    MetaTagCheck -- "Language Found" --> ReturnLanguage[Return meta-language]
    MetaTagCheck -- "Language not found" --> JavaScriptCheck[Attempt to get language using JavaScript get_page_lang()]
    JavaScriptCheck -- "Language Found" --> ReturnLanguageJS[Return JS-language]
     JavaScriptCheck -- "Language not found" --> ReturnNone[Return None]

    GetUrl --> SaveCurrentURL[Save previous_url]
    SaveCurrentURL --> NavigateDriver[Call self.driver.get(url)]
    NavigateDriver --> WaitForPageLoad[Wait for ready_state 'complete']
    WaitForPageLoad --> UpdatePreviousURL[Update self.previous_url if needed]
    UpdatePreviousURL --> SaveCookies
    SaveCookies --> ReturnTrue[Return True on Success]

    WindowOpen --> OpenNewTab[Execute window.open() JS]
    OpenNewTab --> SwitchToNewTab[Switch to the new tab]
    SwitchToNewTab --> CheckURLProvided[Check if url argument provided]
    CheckURLProvided -- "URL Provided" --> NavigateToURL[Navigate to URL]
    CheckURLProvided -- "URL Not provided" -->  End
    NavigateToURL --> End

    Wait --> TimeSleep[time.sleep(delay)]

    FetchHtml --> CheckProtocol[Check URL protocol: file://, http://, https://]
     CheckProtocol -- "file://" --> FilePathExtraction[Extract Path]
     FilePathExtraction --> CheckPathValid[Validate file path]
     CheckPathValid -- "Valid path" --> ReadFile[Read file to html_content]
     ReadFile -->  ReturnTrueF[Return True]
      CheckPathValid -- "Invalid path" --> ReturnFalseF[Return False]
    
    CheckProtocol -- "http:// or https://" --> GetURLCall[Call get_url(url)]
    GetURLCall -- "get_url success" --> SavePageSource[Save self.page_source to self.html_content]
    SavePageSource -->  ReturnTrueH[Return True]
    GetURLCall -- "get_url fail" --> ReturnFalseH[Return False]
     CheckProtocol -- "Unsupported Protocol" --> ReturnFalseP[Return False]

     subgraph SubFunctions
        carousel["carousel(direction, scrolls, frame_size, delay)"]
     end
    
    style Driver Class fill:#f9f,stroke:#333,stroke-width:2px
    style SubFunctions fill:#ccf,stroke:#333,stroke-width:2px
```

### Анализ зависимостей `mermaid`

*   **Driver Class**: Главный класс `Driver`, который инкапсулирует логику работы с веб-драйвером.
*   **SubFunctions**: Выделенные вспомогательные функции.
    *   `carousel`: Внутренняя функция для прокрутки страницы.
*   **`__init__`**: Конструктор класса, принимает класс веб-драйвера и аргументы, создает экземпляр драйвера.
*   **`__init_subclass__`**: Метод, вызываемый при создании подкласса, проверяет наличие `browser_name`
*   **`__getattr__`**: Перехватывает вызовы атрибутов, перенаправляет на `self.driver`.
*   **`scroll`**: Метод для прокрутки страницы, вызывает `carousel`.
*  **`locale`**: Метод для получения локали
*   **`get_url`**: Метод для навигации на URL.
*   **`window_open`**: Метод для открытия нового окна.
*   **`wait`**: Метод для ожидания.
*   **`_save_cookies_localy`**: Метод для сохранения cookies.
*   **`fetch_html`**: Метод для загрузки HTML-контента.
*   **CheckWebDriver**: Проверка валидности класса веб-драйвера.
*   **CreateDriverInstance**: Создание экземпляра веб-драйвера.
*   **RaiseTypeError**: Выброс исключения, если `webdriver_cls` невалидный.
*   **CheckBrowserName**: Проверка наличия `browser_name`.
*    **SetBrowserName**: Установка `browser_name` в классе.
*   **RaiseValueError**: Выброс исключения, если `browser_name` не указан.
*   **DriverAttributeAccess**: Доступ к атрибуту `self.driver`.
*   **CallCarousel**: Вызов внутренней функции `carousel`.
*    **ExecuteScript**: Выполнение JavaScript для прокрутки.
*   **MetaTagCheck**: Поиск мета-тега с языком.
*   **ReturnLanguage**: Возврат языка из мета-тега.
*   **JavaScriptCheck**: Попытка получить язык через JS.
*   **ReturnLanguageJS**: Возврат языка из JS.
*   **ReturnNone**: Возврат `None`, если язык не найден.
*   **SaveCurrentURL**: Сохранение предыдущего URL.
*   **NavigateDriver**: Вызов метода `get()` веб-драйвера.
*   **WaitForPageLoad**: Ожидание полной загрузки страницы.
*   **UpdatePreviousURL**: Обновление предыдущего URL.
*   **ReturnTrue**: Возврат True в случае успеха.
*   **OpenNewTab**: Выполнение JavaScript для открытия новой вкладки.
*    **SwitchToNewTab**: Переключение на новую вкладку
*   **CheckURLProvided**: Проверка, передан ли URL
*   **NavigateToURL**: Вызов `get()` для новой вкладки
*   **TimeSleep**: Ожидание `delay`.
*   **CheckProtocol**: Проверка протокола URL.
*   **FilePathExtraction**: Извлечение пути из `file://`.
*    **CheckPathValid**: Проверка корректности пути файла
*    **ReadFile**: Чтение файла
*    **ReturnTrueF**: Возврат `True`, если файл прочитан успешно
*    **ReturnFalseF**: Возврат `False`, если не удалось прочитать файл
*   **GetURLCall**: Вызов `get_url()` для HTTP/HTTPS.
*   **SavePageSource**: Сохранение `page_source`.
*    **ReturnTrueH**: Возврат `True`, если `get_url()` успешен
*    **ReturnFalseH**: Возврат `False`, если `get_url()` не успешен
*    **ReturnFalseP**: Возврат `False`, если протокол не поддерживается

## <объяснение>

### Импорты:

*   `copy`: Используется для создания копии текущего URL в методе `get_url`, чтобы сохранить предыдущий URL.
*   `re`: Используется для работы с регулярными выражениями в методе `fetch_html` для извлечения пути к файлу.
*   `time`: Используется для реализации задержки в методе `wait`.
*   `pickle`: Используется для сериализации и десериализации cookies в методе `_save_cookies_localy`.
*   `typing.Optional`: Используется для аннотации типов, указывая, что функция может вернуть `None`.
*   `selenium.webdriver.remote.webdriver`: Импортирует абстрактный класс WebDriver, от которого наследуются классы конкретных браузеров.
*   `selenium.webdriver.common.by`: Используется для определения методов поиска элементов на странице (например, By.CSS_SELECTOR).
*   `selenium.common.exceptions`:  Используется для перехвата исключений, которые могут возникнуть при взаимодействии с веб-драйвером.
*   `Pathlib.Path`: Используется для работы с путями к файлам в методе `fetch_html`.
*   `src.header`: Используется для импорта глобальных настроек из `src.gs`.
*   `src.logger`: Используется для логирования ошибок.

    ```mermaid
    flowchart TD
        Start --> header[<code>header.py</code><br> Determine Project Root]

        header --> import[Import Global Settings: <br><code>from src import gs</code>]
        header --> import_logger[Import Logger:<br><code>from src import logger</code>]

        
    ```

### Классы:

*   **`Driver`**:
    *   **Роль**:  Предоставляет унифицированный интерфейс для работы с разными веб-драйверами Selenium. Инкапсулирует логику инициализации драйвера, навигации, скроллинга, ожидания, работы с cookies и обработки исключений.
    *   **Атрибуты**:
        *   `driver`: Экземпляр веб-драйвера (например, `Chrome` или `Firefox`).
        * `html_content`: HTML-контент страницы, полученный через `fetch_html`
    *   **Методы**:
        *   `__init__`: Конструктор для инициализации драйвера.
        *  `__init_subclass__`: Метод, вызываемый при создании подкласса
        *   `__getattr__`: Перенаправляет вызовы атрибутов к экземпляру веб-драйвера.
        *   `scroll`: Прокрутка страницы.
        *   `locale`: Определение языка страницы.
        *   `get_url`: Переход на URL.
        *   `window_open`: Открытие нового окна или вкладки.
        *   `wait`: Ожидание заданного времени.
        *   `_save_cookies_localy`: Сохранение cookies.
        *   `fetch_html`: Получение HTML-кода страницы или файла.

    *   **Взаимодействие**:  Класс `Driver` взаимодействует с классами веб-драйверов Selenium (`Chrome`, `Firefox` и др.), предоставляя им унифицированный интерфейс. Использует модули `copy`, `re`, `time`, `pickle`, `typing`, `selenium`, `pathlib`, `src.header` для своей функциональности.

### Функции:

*   **`__init__(self, webdriver_cls, *args, **kwargs)`**:
    *   **Аргументы**:
        *   `webdriver_cls`: Класс веб-драйвера (например, `Chrome`, `Firefox`).
        *   `*args`: Позиционные аргументы для конструктора класса веб-драйвера.
        *   `**kwargs`: Именованные аргументы для конструктора класса веб-драйвера.
    *   **Назначение**: Инициализация экземпляра драйвера, проверка на валидность веб-драйвера, создание экземпляра веб-драйвера.
        ```python
            from selenium.webdriver import Chrome
            driver = Driver(Chrome, executable_path='/path/to/chromedriver')
        ```
    *   **Возвращаемое значение**: None.

*    **`__init_subclass__(cls, *, browser_name=None, **kwargs)`**:
    *   **Аргументы**:
         *  `cls`: Класс-подкласс.
         *  `browser_name`: Название браузера
         * `**kwargs`: Дополнительные аргументы
    *  **Назначение**: Проверка, что при создании подкласса указан `browser_name`, сохранение этого имени в классе
       ```python
        class ChromeDriver(Driver, browser_name='chrome'):
            pass
       ```
    *   **Возвращаемое значение**: None.

*  **`__getattr__(self, item)`**:
   *   **Аргументы**:
       * `item`: Имя атрибута.
   *   **Назначение**: Перехват вызовов несуществующих атрибутов и перенаправление их к атрибутам веб-драйвера.
        ```python
             driver.get('https://example.com') # вызывает driver.driver.get('https://example.com')
        ```
   *   **Возвращаемое значение**: Значение атрибута из `self.driver`.

*   **`scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool`**:
    *   **Аргументы**:
        *   `scrolls`: Количество прокруток.
        *   `frame_size`: Размер прокрутки в пикселях.
        *   `direction`: Направление прокрутки ('both', 'forward', 'backward', 'down', 'up').
        *   `delay`: Задержка между прокрутками в секундах.
    *   **Назначение**: Выполнение прокрутки страницы в заданном направлении.
        ```python
            driver.scroll(scrolls=3, direction='down', frame_size=500, delay=0.2)
        ```
    *   **Возвращаемое значение**: `True`, если прокрутка успешна, иначе `False`.
*   **`locale(self) -> Optional[str]`**:
    *   **Аргументы**: None
    *  **Назначение**: Определение языка страницы по мета-тегу или через JavaScript.
        ```python
            language = driver.locale
        ```
    *   **Возвращаемое значение**: Строка, содержащая код языка, или `None`.

*   **`get_url(self, url: str) -> bool`**:
    *   **Аргументы**:
        *   `url`: URL для перехода.
    *   **Назначение**: Переход на указанный URL, сохранение предыдущего URL, обновление cookies.
        ```python
            driver.get_url('https://example.com/page')
        ```
    *   **Возвращаемое значение**: `True`, если навигация успешна, иначе `False`.
*   **`window_open(self, url: Optional[str] = None) -> None`**:
    *   **Аргументы**:
        *   `url`: URL для открытия в новом окне (необязательный).
    *   **Назначение**: Открытие нового окна или вкладки в браузере.
        ```python
            driver.window_open('https://example.com/newtab')
        ```
    *   **Возвращаемое значение**: None.

*   **`wait(self, delay: float = .3) -> None`**:
    *   **Аргументы**:
        *   `delay`: Время задержки в секундах.
    *   **Назначение**: Ожидание заданного времени.
    ```python
    driver.wait(2) # задержка на 2 секунды
    ```
    *   **Возвращаемое значение**: None.

*    **`_save_cookies_localy(self) -> None`**:
    *   **Аргументы**: None.
    *   **Назначение**: Сохранение cookies в локальный файл.
        ```python
            driver._save_cookies_localy()
        ```
    *   **Возвращаемое значение**: None

*   **`fetch_html(self, url: str) -> Optional[bool]`**:
    *   **Аргументы**:
        *   `url`: URL или путь к файлу.
    *   **Назначение**: Загрузка HTML-контента с веб-страницы или локального файла.
        ```python
          driver.fetch_html('file:///path/to/localfile.html')
          driver.fetch_html('https://example.com/page')
        ```
    *   **Возвращаемое значение**: `True`, если контент получен успешно, иначе `None`.

### Переменные:

*   `self.driver`: Экземпляр веб-драйвера, созданный в конструкторе.
*   `self.previous_url`: URL текущей страницы до перехода на новую.
*   `self.html_content`: Содержит HTML-код страницы, если был вызван `fetch_html`.
*  `cls.browser_name`: Содержит название браузера для подкласса

### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок**: В коде есть общие блоки `except Exception as ex`, которые отлавливают все ошибки. Лучше использовать более конкретные исключения (например, `WebDriverException`, `TimeoutException`), чтобы точно определять причину ошибок.
2.  **Сохранение cookies**: Сохранение cookies закомментировано (`return True`).
3.  **Ожидание**: Для ожидания загрузки страницы используется  `while self.ready_state != 'complete'`, что может быть недостаточно надежным.  Лучше использовать более надежные способы, например `WebDriverWait`.
4.  **Выбор локали**:  Возможно, стоит добавить больше способов определения локали, если мета-тег или JavaScript не работают.
5. **`fetch_html`**: Метод `fetch_html` выполняет две задачи — считывает локальный HTML и загружает веб-страницу. Возможно, лучше разнести эти функции в разные методы.
6. **JavaScript**:  Используется `execute_script` для прокрутки, что может быть медленнее, чем встроенные методы, например `ActionChains`.

### Взаимосвязи с другими частями проекта:

*   `src.header`: Используется для получения глобальных настроек, таких как путь к файлу для сохранения cookies.
*   `src.logger`: Используется для логирования ошибок и отладочной информации.
*   `selenium`: Используется для управления браузером.

Этот модуль можно использовать в веб-скрепинге, автоматизации тестирования, и других задачах, где требуется взаимодействие с веб-браузером.