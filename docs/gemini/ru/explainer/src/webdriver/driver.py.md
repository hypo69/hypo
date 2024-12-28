## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    *   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    *   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    *   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    *   **Переменные**: Их типы и использование.
    *   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

1.  **Инициализация `Driver`**:
    *   При создании экземпляра `Driver` (например, `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`), вызывается `__init__`.
    *   Проверяется, что переданный класс `webdriver_cls` имеет метод `get`.
    *   Создается экземпляр `webdriver_cls` (например, `Chrome`) с переданными аргументами, который сохраняется в `self.driver`.
    *   При наследовании класса `Driver` (например, `class MyDriver(Driver, browser_name='my_browser')`),  `__init_subclass__` проверяет, что задано `browser_name` и устанавливает его как атрибут класса.

2.  **Доступ к атрибутам драйвера**:
    *   При обращении к атрибуту `driver` через экземпляр `Driver` (например, `driver.current_url`), вызывается `__getattr__`.
    *   `__getattr__` перенаправляет запрос к соответствующему атрибуту экземпляра `self.driver` (например, `self.driver.current_url`).

3.  **Прокрутка страницы (`scroll`)**:
    *   Метод `scroll` принимает параметры: `scrolls` (количество прокруток), `frame_size` (размер прокрутки), `direction` (направление), `delay` (задержка).
    *   Внутри `scroll` определена локальная функция `carousel`, которая выполняет фактическую прокрутку.
    *   `carousel` использует JavaScript (`window.scrollBy`) для прокрутки страницы в указанном направлении.
    *   Метод `scroll` вызывает `carousel` с соответствующим направлением.
    *   Направление может быть `forward`/`down`, `backward`/`up` или `both`. В случае `both` прокрутка выполняется в обоих направлениях.

4.  **Определение языка страницы (`locale`)**:
    *   Метод `locale` пытается получить язык страницы из мета-тега `Content-Language` с помощью CSS-селектора.
    *   Если не удалось, пытается получить язык из JavaScript с помощью метода `get_page_lang`.
    *   Возвращает код языка или `None`.

5.  **Переход по URL (`get_url`)**:
    *   `get_url` принимает URL в качестве аргумента.
    *   Сохраняет текущий URL в `_previous_url`.
    *   Переходит по новому URL с помощью `self.driver.get(url)`.
    *   Ожидает загрузки страницы.
    *   Сохраняет предыдущий URL в атрибут `previous_url`, если URL изменился.
    *   Сохраняет куки локально, вызывая `_save_cookies_localy`.

6.  **Открытие нового окна/вкладки (`window_open`)**:
    *   Метод `window_open` открывает новую вкладку с помощью JavaScript.
    *   Переключает фокус на новую вкладку.
    *   Если передан URL, то переходит по нему.

7.  **Ожидание (`wait`)**:
    *   Метод `wait` приостанавливает выполнение на указанное время.

8.  **Сохранение куки (`_save_cookies_localy`)**:
    *   Метод `_save_cookies_localy` сохраняет куки браузера в локальный файл.
    *   В текущей версии метод не выполняет запись куки, а возвращает `True`

9.  **Получение HTML-контента (`fetch_html`)**:
    *   Метод `fetch_html` принимает URL как аргумент, который может быть как путем к файлу, так и URL-ом.
    *   Если URL начинается с `file://`, метод извлекает HTML из локального файла.
        *   Очищает URL от `file://`.
        *   Ищет корректный путь к файлу, например, `C:\path\to\file.html`.
        *   Если файл найден, читает его содержимое и сохраняет в `self.html_content`.
    *   Если URL начинается с `http://` или `https://`, то используется метод `get_url` для перехода по URL.
    *   Сохраняет `page_source` в `self.html_content`.

## <mermaid>

```mermaid
flowchart TD
    subgraph DriverClass [Class: `Driver`]
        Init[<code>__init__</code><br>Initialize Driver Instance]
        SubclassInit[<code>__init_subclass__</code><br>Handle Subclass Initialization]
        GetAttr[<code>__getattr__</code><br>Proxy Attribute Access]
        Scroll[<code>scroll</code><br>Scroll Web Page]
        Carousel[<code>carousel</code><br>Scroll Implementation]
        Locale[<code>locale</code><br>Get Page Language]
        GetURL[<code>get_url</code><br>Navigate to URL]
        WindowOpen[<code>window_open</code><br>Open New Tab]
        Wait[<code>wait</code><br>Pause Execution]
        SaveCookies[<code>_save_cookies_localy</code><br>Save Cookies]
        FetchHTML[<code>fetch_html</code><br>Fetch HTML Content]
    end

    Start --> Init
    Init --> SubclassInit
    SubclassInit --> GetAttr
    GetAttr --> Scroll
    Scroll --> Carousel
    Scroll --> Locale
    Locale --> GetURL
    GetURL --> WindowOpen
    WindowOpen --> Wait
    Wait --> SaveCookies
     SaveCookies --> FetchHTML
    
    
    subgraph DriverUsage [Example Usage]
        CreateDriver[Create `Driver` Instance <br> e.g., `driver = Driver(Chrome, executable_path='path')`]
        AccessAttribute[Access Driver Attribute <br> e.g., `driver.current_url`]
        CallScroll[Call `scroll` Method <br> e.g., `driver.scroll()`]
        CallLocale[Call `locale` Property <br> e.g., `lang = driver.locale`]
        CallGetURL[Call `get_url` Method <br> e.g., `driver.get_url('https://example.com')`]
        CallWindowOpen[Call `window_open` Method <br> e.g., `driver.window_open()`]
         CallWait[Call `wait` Method <br> e.g., `driver.wait(1)`]
         CallFetchHTML[Call `fetch_html` Method <br> e.g., `driver.fetch_html('file:///local_path.html')`]
        end
    
    
    CreateDriver --> Init
    AccessAttribute --> GetAttr
    CallScroll --> Scroll
    CallLocale --> Locale
    CallGetURL --> GetURL
    CallWindowOpen --> WindowOpen
    CallWait --> Wait
    CallFetchHTML --> FetchHTML
    
    
   subgraph HeaderModule [<code>header.py</code>]
    HeaderStart[Start <br><code>header.py</code>]
       ImportGlobalSettings[Import Global Settings: <br><code>from src import gs</code>]
   end

   HeaderStart --> ImportGlobalSettings
```

### Описание диаграммы `mermaid`:

*   **`DriverClass`**: Подграф, представляющий класс `Driver` и его методы.
    *   `Init`: Метод `__init__`, используемый для инициализации экземпляра `Driver`.
    *   `SubclassInit`: Метод `__init_subclass__`, обрабатывает инициализацию при наследовании класса `Driver`.
    *   `GetAttr`: Метод `__getattr__`, обеспечивает проксирование вызовов к методам и атрибутам `webdriver`.
    *   `Scroll`: Метод `scroll`, используемый для прокрутки веб-страницы.
    *   `Carousel`: Локальный метод `carousel`, который фактически выполняет прокрутку.
    *   `Locale`: Метод `locale`, используется для определения языка текущей страницы.
    *   `GetURL`: Метод `get_url`, используется для перехода по URL.
    *   `WindowOpen`: Метод `window_open`, для открытия нового окна или вкладки.
    *   `Wait`: Метод `wait`, используется для приостановки выполнения на заданное время.
    *   `SaveCookies`: Метод `_save_cookies_localy`, для сохранения куков в локальный файл.
    *   `FetchHTML`: Метод `fetch_html`, для извлечения HTML контента из файла или URL.
*   **`DriverUsage`**: Подграф, демонстрирующий пример использования класса `Driver`.
    *   `CreateDriver`: Пример создания экземпляра класса `Driver`.
    *   `AccessAttribute`: Пример доступа к атрибуту драйвера, через проксирование.
    *   `CallScroll`: Пример вызова метода `scroll`.
    *   `CallLocale`: Пример вызова метода `locale`.
    *  `CallGetURL`: Пример вызова метода `get_url`.
    *   `CallWindowOpen`: Пример вызова метода `window_open`.
     *   `CallWait`: Пример вызова метода `wait`.
    *    `CallFetchHTML`: Пример вызова метода `fetch_html`.

*   **`HeaderModule`**: Подграф, представляющий функциональность `header.py`.
    *   `HeaderStart`: Начальная точка `header.py`.
    *    `ImportGlobalSettings`: Импорт глобальных настроек из пакета `src`.

### Зависимости `mermaid`:

Диаграмма показывает, как методы и атрибуты класса `Driver` используются при работе с Selenium WebDriver, а так же демонстрирует зависимости и порядок вызовов методов класса `Driver`.
Дополнительно, блок `HeaderModule` показывает как импортируется и используется `header.py`.

## <объяснение>

### Импорты:

*   `copy`: Используется для создания копии URL, чтобы избежать проблем с ссылками на один и тот же объект.
*   `pickle`: Используется для сериализации и десериализации данных, в данном случае для сохранения и загрузки куки.
*   `time`: Используется для задержки выполнения кода с помощью `time.sleep()`.
*   `re`: Используется для работы с регулярными выражениями, например, для разбора URL.
*   `pathlib`: Используется для работы с путями к файлам.
*   `typing.Optional`: Используется для определения необязательных типов, например, `Optional[str]`.
*   `selenium.webdriver.common.by.By`: Используется для поиска элементов на веб-странице с помощью различных селекторов.
*   `selenium.common.exceptions`: Набор исключений, которые могут возникнуть при работе с веб-драйвером.
*   `header`: Пользовательский модуль для определения корневой директории проекта.
*   `src`:  Содержит `gs` (global settings) для доступа к глобальным настройкам приложения, а так же `logger`,  который предоставляет функции для логирования.

### Классы:

*   `Driver`:
    *   **Роль**: Предоставляет унифицированный интерфейс для работы с Selenium WebDriver.
    *   **Атрибуты**:
        *   `driver`: Экземпляр Selenium WebDriver (например, `Chrome`, `Firefox`).
        *   `browser_name`: (атрибут класса) название браузера.
        *   `html_content`: (атрибут экземпляра) для хранения html страницы.
        *   `previous_url`: (атрибут экземпляра) для хранения предыдущего url.
    *   **Методы**:
        *   `__init__(self, webdriver_cls, *args, **kwargs)`: Инициализирует драйвер, проверяя, что переданный класс имеет метод `get`.
        *   `__init_subclass__(cls, *, browser_name=None, **kwargs)`: Автоматически вызывается при создании подкласса `Driver`, устанавливает имя браузера.
        *   `__getattr__(self, item)`: Проксирует вызовы атрибутов и методов к экземпляру `self.driver`.
        *   `scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)`: Прокручивает страницу в указанном направлении.
        *   `locale(self)`: Определяет язык страницы.
        *   `get_url(self, url)`: Переходит по указанному URL и сохраняет куки.
        *   `window_open(self, url=None)`: Открывает новую вкладку.
        *   `wait(self, delay=.3)`: Приостанавливает выполнение на заданное время.
        *   `_save_cookies_localy(self)`: Сохраняет куки в файл.
        *   `fetch_html(self, url)`: Извлекает HTML контент из файла или URL.

### Функции:

*   В классе `Driver` описаны методы, которые ведут себя как функции
*   `carousel(direction='', scrolls=1, frame_size=600, delay=.3)`: Локальная функция в методе `scroll` для фактической прокрутки страницы.
    *   **Аргументы**: `direction` (направление прокрутки), `scrolls` (количество прокруток), `frame_size` (размер прокрутки), `delay` (задержка).
    *   **Возвращает**: `True` при успешной прокрутке, `False` при ошибке.
    *   **Назначение**: Прокручивает страницу с использованием JavaScript `window.scrollBy`.

### Переменные:

*   `MODE`: Глобальная переменная, определяющая режим работы приложения (например, `dev`, `prod`).
*   `webdriver_cls`: Класс WebDriver, переданный при инициализации Driver.
*   `url`: URL для загрузки или навигации.
*   `scrolls`, `frame_size`, `direction`, `delay`: Параметры для метода `scroll`.
*   `file_path`: Путь к файлу при загрузке HTML.
*   `meta_language`: Объект найденный с помощью селектора `By.CSS_SELECTOR, "meta[http-equiv=\'Content-Language\']"`
*   `_previous_url`: URL перед переходом на новый.

### Потенциальные ошибки и области для улучшения:

*   **Обработка исключений**: В методах `scroll` и `fetch_html` используется общая обработка исключений `except Exception as ex`,  нужно уточнить типы исключений для более точной обработки.
*   **Метод `_save_cookies_localy`**: В текущем виде не сохраняет куки, требуется исправить на корректную реализацию.
*   **Определение языка страницы**: Метод `locale` использует `try-except` блоки, можно рассмотреть использование более надежных методов.
*   **Проверка типов**: Можно добавить проверки типов для аргументов методов с помощью `isinstance()`, чтобы избежать ошибок в рантайме.
*   **Логирование**: В некоторых местах логируется только сообщение об ошибке без стектрейса.
*   **Управление задержками**: Жестко заданные задержки `time.sleep(delay)` могут замедлить выполнение кода, нужно рассмотреть более гибкие стратегии ожидания.
*   **Сохранение предыдущего URL**: Условие `if url != _previous_url:` может не работать если url заканчивается слешем (`/`), и нужно сделать нормализацию URL перед сравнением.

### Взаимосвязи с другими частями проекта:

*   `header.py`: Используется для определения корневой директории проекта, что важно для загрузки настроек и ресурсов.
*   `src.gs`: Используется для доступа к глобальным настройкам, например, пути к файлу для сохранения куки.
*   `src.logger`: Используется для логирования ошибок и отладочной информации, что помогает отслеживать работу драйвера и обнаруживать проблемы.
*   `selenium`: Обеспечивает функциональность для взаимодействия с веб-браузерами.

Данный код является базовым модулем для управления Selenium Webdriver, он предоставляет удобный интерфейс для выполнения навигации, прокрутки, работы с куками и загрузки контента. Но требует некоторых улучшений для обеспечения стабильности и надежности.