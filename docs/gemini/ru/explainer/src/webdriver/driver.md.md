## Анализ кода `driver.py`

### <алгоритм>

1.  **Инициализация `Driver`**:
    *   При создании экземпляра `Driver` (например, `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`) класс принимает класс веб-драйвера (`webdriver_cls`, например, `Chrome`) и любые дополнительные аргументы (`*args`, `**kwargs`).
    *   Проверяет, является ли `webdriver_cls` валидным классом веб-драйвера (наличие метода `get`). Если нет, выбрасывает исключение `TypeError`.
    *   Инициализирует внутренний драйвер (`self.driver`) с предоставленными аргументами.
    *   **Пример**:
        ```python
        driver = Driver(Chrome, executable_path='/path/to/chromedriver')
        ```
        Здесь создаётся экземпляр `Driver` с драйвером Chrome.

2.  **Инициализация подклассов `Driver`**:
    *   При создании подкласса `Driver` (например, `class MyDriver(Driver, browser_name='chrome'):`) автоматически вызывается метод `__init_subclass__`.
    *   Проверяет, был ли указан аргумент `browser_name`. Если нет, выбрасывает `ValueError`.
    *   Сохраняет `browser_name` как атрибут класса.
    *   **Пример**:
        ```python
        class MyDriver(Driver, browser_name='chrome'):
             pass
        ```
        Здесь создается класс `MyDriver`, который наследует `Driver` и имеет атрибут `browser_name` равный 'chrome'.

3.  **Доступ к атрибутам драйвера через `__getattr__`**:
    *   Если обращение к атрибуту экземпляра `Driver` не находит его среди собственных атрибутов, вызывается метод `__getattr__`.
    *   Перенаправляет запрос к атрибуту внутреннего драйвера (`self.driver`).
    *   **Пример**:
        ```python
        driver.get('https://example.com')
        ```
        Здесь `driver.get` вызывает метод `get` внутреннего объекта `self.driver`.

4.  **Прокрутка страницы (`scroll`)**:
    *   Функция `scroll` принимает количество прокруток (`scrolls`), размер кадра прокрутки (`frame_size`), направление (`direction`) и задержку (`delay`).
    *   Внутренняя функция `carousel` выполняет прокрутку в заданном направлении (`''` для вниз, `'-'` для вверх) через `execute_script`.
    *   В зависимости от значения `direction` вызывает `carousel` с разными параметрами.
    *   **Пример**:
        ```python
        driver.scroll(scrolls=2, direction='both')
        ```
        Здесь страница прокручивается дважды вниз и дважды вверх.

5.  **Определение языка страницы (`locale`)**:
    *   Функция `locale` пытается получить язык страницы из мета-тега `content-language`.
    *   Если не удается, пытается получить язык с помощью JavaScript (`get_page_lang`).
    *   Возвращает код языка или `None` в случае неудачи.
    *   **Пример**:
        ```python
        language = driver.locale
        ```
        Здесь определяется язык текущей страницы.

6.  **Переход по URL (`get_url`)**:
    *   Функция `get_url` принимает URL.
    *   Сохраняет текущий URL в `_previous_url`.
    *   Переходит по указанному URL, используя метод `get` внутреннего драйвера.
    *   Ожидает, пока страница полностью загрузится (свойство `ready_state` равно `'complete'`).
    *   Если URL отличается от `_previous_url`, сохраняет предыдущий URL в атрибуте `previous_url`.
    *   Сохраняет куки локально с помощью `_save_cookies_localy`.
    *   Обрабатывает исключения `WebDriverException` и `InvalidArgumentException`, логируя ошибки.
    *   **Пример**:
        ```python
        driver.get_url('https://example.com')
        ```
        Здесь браузер переходит на указанный URL.

7.  **Открытие нового окна (`window_open`)**:
    *   Функция `window_open` открывает новую вкладку через JavaScript и переключается на нее.
    *   Если указан URL, открывает его в новой вкладке.
    *   **Пример**:
        ```python
        driver.window_open('https://example.com')
        ```
        Здесь открывается новая вкладка и переходит по указанному URL.

8.  **Ожидание (`wait`)**:
    *   Функция `wait` приостанавливает выполнение программы на заданное время.
    *   **Пример**:
        ```python
        driver.wait(1) # Пауза на 1 секунду
        ```

9.  **Сохранение cookies локально (`_save_cookies_localy`)**:
    *   Функция `_save_cookies_localy` сохраняет куки драйвера в файл (сейчас это закомментировано и всегда возвращает `True` для отладки).
    *   Используется `pickle` для сохранения.
    *   **Пример**:
        ```python
        # Этот метод вызывается автоматически при переходе по url
        ```
       Здесь куки текущей сессии браузера будут сохранены в файл.

10. **Получение HTML контента (`fetch_html`)**:
    *   Функция `fetch_html` получает HTML контент по URL.
    *   Если URL начинается с `file://`, то пытается прочитать содержимое локального файла.
    *   Если URL начинается с `http://` или `https://`, то использует `get_url` для перехода и берет HTML из `page_source`.
    *   **Пример**:
        ```python
        driver.fetch_html('https://example.com')
        html_content = driver.html_content
        ```
        Здесь HTML-код страницы сохраняется в атрибут `html_content`.
    *   **Поток данных**:
        *   `fetch_html` -> `get_url` -> `self.driver.get()` -> `self.page_source`
        *   `fetch_html` <- `open(file)`
11. **Примеры**:
   ```python
   from selenium.webdriver import Chrome
   from selenium.webdriver.chrome.options import Options

   options = Options()
   options.add_argument("--headless")

   driver = Driver(Chrome, options=options, executable_path='/path/to/chromedriver')
   driver.get_url('https://example.com')
   print(driver.locale)
   driver.scroll(direction='down', scrolls=2)
   driver.window_open('https://google.com')
   driver.fetch_html('https://example.com')
   print(driver.html_content)
   ```

### <mermaid>

```mermaid
graph LR
    A[Driver] --> B(webdriver_cls);
    B --> C{hasattr(webdriver_cls, 'get')?};
    C -- Yes --> D[self.driver = webdriver_cls(*args, **kwargs)];
    C -- No --> E[TypeError];
    A --> F{__init_subclass__};
    F --> G{browser_name is None?};
    G -- Yes --> H[ValueError];
    G -- No --> I[cls.browser_name = browser_name];
    A --> J{__getattr__};
    J --> K[getattr(self.driver, item)];
    A --> L[scroll];
    L --> M[carousel];
    M --> N{execute_script};
    A --> O[locale];
    O --> P{find_element};
    P -- Found Meta Tag --> Q[get_attribute('content')];
    P -- Not Found --> R[get_page_lang];
    A --> S[get_url];
    S --> T[self.driver.get(url)];
    T --> U{self.ready_state == 'complete'?};
    U -- No --> T;
    U -- Yes --> V{url != _previous_url?};
    V -- Yes --> W[self.previous_url = _previous_url];
    V -- No --> X[_save_cookies_localy];
    A --> Y[window_open];
    Y --> Z[execute_script('window.open();')];
    Z --> AA[switch_to.window(self.window_handles[-1])];
     AA --> BB{url};
    BB -- yes --> CC[get(url)];
    A --> DD[wait];
    DD --> EE[time.sleep(delay)];
    A --> FF[_save_cookies_localy];
    FF --> GG{open(gs.cookies_filepath, 'wb')};
    GG --> HH[pickle.dump(self.driver.get_cookies(), cookiesfile)];
    A --> II[fetch_html];
    II --> JJ{url.startswith('file://')?};
    JJ -- Yes --> KK{re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)};
        KK -- Yes --> LL[open(file_path, 'r', encoding='utf-8')];
        LL --> MM[self.html_content = file.read()];
    JJ -- No --> NN{url.startswith('http://') or url.startswith('https://')};
        NN -- Yes --> OO[get_url(url)];
        OO --> PP[self.html_content = self.page_source];
        NN -- No --> QQ[Error];

    subgraph Driver Class
        A
        B
        C
        D
        E
        F
        G
        H
        I
        J
        K
        L
        M
        N
        O
        P
        Q
        R
        S
        T
        U
        V
        W
        X
        Y
        Z
        AA
        BB
        CC
        DD
        EE
        FF
        GG
        HH
        II
        JJ
        KK
        LL
        MM
        NN
        OO
        PP
        QQ
    end
```

**Анализ `mermaid` диаграммы:**

*   **`Driver`**: Центральный узел, представляющий класс `Driver`.
*   **`webdriver_cls`**: Класс веб-драйвера, переданный при инициализации `Driver`.
*   **`hasattr(webdriver_cls, 'get')?`**: Проверка, есть ли у переданного класса `webdriver_cls` метод `get`.
*   **`self.driver = webdriver_cls(*args, **kwargs)`**: Инициализация внутреннего драйвера.
*   **`TypeError`**: Ошибка, если `webdriver_cls` не является валидным классом веб-драйвера.
*   **`__init_subclass__`**: Метод, вызываемый при наследовании от класса `Driver`.
*   **`browser_name is None?`**: Проверка наличия аргумента `browser_name` при наследовании.
*   **`ValueError`**: Ошибка, если `browser_name` не указан при наследовании.
*   **`cls.browser_name = browser_name`**: Присваивание значения `browser_name` атрибуту класса.
*   **`__getattr__`**: Метод для перенаправления доступа к атрибутам внутреннего драйвера.
*   **`getattr(self.driver, item)`**: Получение атрибута `item` из внутреннего драйвера.
*   **`scroll`**: Метод для прокрутки страницы.
*   **`carousel`**: Внутренняя функция для прокрутки в заданном направлении.
*   **`execute_script`**: Выполнение JavaScript для прокрутки.
*   **`locale`**: Метод для определения языка страницы.
*   **`find_element`**: Поиск мета-тега.
*   **`get_attribute('content')`**: Получение значения атрибута `content`.
*   **`get_page_lang`**: Функция для получения языка с помощью JavaScript.
*   **`get_url`**: Метод для перехода по URL.
*   **`self.driver.get(url)`**: Переход по URL с помощью драйвера.
*   **`self.ready_state == 'complete'?`**: Проверка готовности страницы.
*   **`url != _previous_url?`**: Проверка, изменился ли URL.
*   **`self.previous_url = _previous_url`**: Сохранение предыдущего URL.
*   **`_save_cookies_localy`**: Метод для сохранения куки локально.
*   **`window_open`**: Метод для открытия нового окна.
*  **`execute_script('window.open();')`**: Открытие нового окна с помощью JavaScript.
*  **`switch_to.window(self.window_handles[-1])`**: Переключение на новое окно.
*   **`get(url)`**: Переход по URL в новом окне.
*   **`wait`**: Метод для ожидания.
*   **`time.sleep(delay)`**: Приостановка выполнения на заданное время.
*   **`open(gs.cookies_filepath, 'wb')`**: Открытие файла для записи куки.
*  **`pickle.dump(self.driver.get_cookies(), cookiesfile)`**: Сохранение куки в файл.
*   **`fetch_html`**: Метод для получения HTML-кода.
*   **`url.startswith('file://')?`**: Проверка, является ли URL локальным файлом.
*   **`re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)`**: Поиск пути к файлу.
*   **`open(file_path, 'r', encoding='utf-8')`**: Открытие файла для чтения.
*   **`self.html_content = file.read()`**: Загрузка HTML-кода из файла.
*    **`url.startswith('http://') or url.startswith('https://')`**: Проверка, является ли URL веб-страницей.
*   **`get_url(url)`**: Загрузка HTML-кода с веб-страницы.
*   **`self.html_content = self.page_source`**: Загрузка HTML-кода из `page_source`.
*   **`Error`**: Обработка ошибки.
*   Диаграмма наглядно демонстрирует поток выполнения и зависимости между методами класса `Driver`, а также его взаимодействие с внешними библиотеками и классами.

### <объяснение>

#### Импорты:

1.  `time`: Используется для реализации задержки в методе `wait` с помощью `time.sleep()`.
2.  `copy`:  Используется для создания копии URL перед переходом в методе `get_url` для отслеживания изменений URL и предотвращения гонок данных.
3.  `pickle`: Используется для сериализации и десериализации куки в методе `_save_cookies_localy`.
4.  `logging`: Используется для регистрации ошибок и отладочной информации.
5.  `re`:  Используется для поиска пути к локальному файлу в функции `fetch_html`.
6.  `typing`:  Используется для аннотации типов, в частности `Optional`.
7.  `pathlib.Path`: Используется для представления пути к локальному файлу и его проверки в функции `fetch_html`.
8.  `selenium.webdriver.remote.webdriver.WebDriver`: Импортируется базовый класс для работы с веб-драйверами.
9.   `selenium.common.exceptions.WebDriverException`: Импортируется для перехвата исключений веб-драйвера.
10.  `selenium.common.exceptions.InvalidArgumentException`: Импортируется для перехвата исключений некорректного аргумента.
11.  `selenium.webdriver.common.by.By`: Импортируется для поиска элементов на странице.
12.  `src.config.globals` as `gs`: Импортируется модуль `globals` из `src.config`, предоставляющий общие настройки, в том числе пути к файлам (например, `gs.cookies_filepath`).

#### Классы:

*   **`Driver`**:
    *   **Роль**: Предоставляет унифицированный интерфейс для работы с Selenium WebDriver.
    *   **Атрибуты**:
        *   `driver`: Экземпляр конкретного WebDriver (например, Chrome, Firefox).
        *   `previous_url`: URL предыдущей страницы.
        *   `html_content`: HTML-код, загруженный из URL.
        *   `browser_name`: Название браузера (только для подклассов).
    *   **Методы**:
        *   `__init__`: Конструктор класса, принимающий класс веб-драйвера и его параметры.
        *   `__init_subclass__`: Метод для настройки подклассов, проверяет наличие `browser_name`.
        *   `__getattr__`: Перенаправляет обращения к атрибутам экземпляра на внутренний драйвер.
        *   `scroll`: Прокручивает страницу в заданном направлении.
        *   `locale`: Определяет язык страницы.
        *   `get_url`: Переходит по URL и сохраняет куки.
        *   `window_open`: Открывает новое окно браузера.
        *   `wait`: Делает паузу в выполнении программы.
        *   `_save_cookies_localy`: Сохраняет куки в файл.
        *   `fetch_html`: Загружает HTML контент по URL (из файла или веб-страницы).
        *  `ready_state`: Свойство, которое возвращает текущий статус загрузки страницы.
        * `current_url`: Свойство, которое возвращает текущий URL.
        * `window_handles`: Свойство, которое возвращает список окон.
        * `page_source`: Свойство, которое возвращает HTML-код страницы.
    *   **Взаимодействие**:
        *   Использует классы из `selenium.webdriver` для управления браузером.
        *   Использует модуль `src.config.globals` для доступа к общим настройкам, таким как путь к файлу куки.
        *   Использует модуль `logging` для записи ошибок.

#### Функции:

*   `__init__(self, webdriver_cls, *args, **kwargs)`:
    *   **Аргументы**: `webdriver_cls` (класс веб-драйвера), `*args` и `**kwargs` (параметры драйвера).
    *   **Назначение**: Инициализирует экземпляр драйвера, проверяет валидность класса веб-драйвера.
    *   **Возвращаемое значение**: None.
    *   **Пример**: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`.
*   `__init_subclass__(cls, *, browser_name=None, **kwargs)`:
    *   **Аргументы**: `cls` (подкласс), `browser_name` (имя браузера).
    *   **Назначение**: Инициализирует подкласс, устанавливает атрибут `browser_name`.
    *   **Возвращаемое значение**: None.
    *   **Пример**: `class MyDriver(Driver, browser_name='chrome'):`.
*   `__getattr__(self, item)`:
    *   **Аргументы**: `item` (имя атрибута).
    *   **Назначение**: Перехватывает доступ к атрибутам, перенаправляя их к внутреннему драйверу.
    *   **Возвращаемое значение**: Атрибут внутреннего драйвера.
    *   **Пример**: `driver.get('https://example.com')` вызовет `self.driver.get()`.
*   `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3)`:
    *   **Аргументы**: `scrolls` (количество прокруток), `frame_size` (размер прокрутки в пикселях), `direction` (направление), `delay` (задержка между прокрутками).
    *   **Назначение**: Прокручивает страницу в заданном направлении.
    *   **Возвращаемое значение**: `True` в случае успеха, `False` в случае ошибки.
    *   **Пример**: `driver.scroll(direction='down', scrolls=2)`.
*   `locale(self) -> Optional[str]`:
    *   **Аргументы**: None.
    *   **Назначение**: Получает язык страницы.
    *   **Возвращаемое значение**: Код языка (например, 'en', 'ru') или `None` в случае ошибки.
    *   **Пример**: `language = driver.locale`.
*    `get_url(self, url: str) -> bool`:
    *   **Аргументы**: `url` (адрес страницы).
    *   **Назначение**: Открывает страницу по указанному URL.
    *   **Возвращаемое значение**: `True` в случае успеха, `False` в случае ошибки.
    *   **Пример**: `driver.get_url('https://example.com')`.
*   `window_open(self, url: Optional[str] = None) -> None`:
    *   **Аргументы**: `url` (адрес страницы).
    *   **Назначение**: Открывает новую вкладку и переходит по URL, если он указан.
    *   **Возвращаемое значение**: None.
    *   **Пример**: `driver.window_open('https://example.com')`.
*   `wait(self, delay: float = .3) -> None`:
    *   **Аргументы**: `delay` (время ожидания).
    *   **Назначение**: Задерживает выполнение программы на указанное время.
    *   **Возвращаемое значение**: None.
    *   **Пример**: `driver.wait(1)`.
*   `_save_cookies_localy(self) -> None`:
    *   **Аргументы**: None.
    *   **Назначение**: Сохраняет куки в файл.
    *   **Возвращаемое значение**: None.
    *   **Пример**: Вызывается автоматически при `get_url`.
*    `fetch_html(self, url: str) -> Optional[bool]`:
    *   **Аргументы**: `url` (адрес или путь к файлу).
    *   **Назначение**: Получает HTML-код страницы или из файла.
    *   **Возвращаемое значение**: `True` в случае успеха, `False` или `None` в случае ошибки.
    *    **Пример**: `driver.fetch_html('https://example.com')`.

#### Переменные:

*   `self.driver`: Экземпляр веб-драйвера.
*   `self.previous_url`: URL предыдущей страницы.
*   `self.html_content`: Содержимое HTML-кода, полученного по url.
*   `scrolls`, `frame_size`, `direction`, `delay`  аргументы для функции `scroll`.
*   `url`: URL-адрес (string).
*   `meta_language`: HTML-элемент (meta tag) для определения языка.
*   `_previous_url`: Временная переменная для сохранения url.
*  `cookiesfile`: Объект файла для записи куки.
* `cleaned_url`:  Очищенная URL-адрес.
* `file_path`:  Путь к файлу в объекте `Path`.

#### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок**: В некоторых местах используются общие исключения (`except Exception as ex:`), что затрудняет отладку. Следует перехватывать более конкретные исключения, чтобы точнее определять причины ошибок.
2.  **Сохранение куки**: В текущей реализации сохранение куки закомментировано для отладки (`return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`). В рабочей версии эту строку нужно будет убрать. Также, стоит рассмотреть вариант сохранение куки в базу данных или облачное хранилище, а не в файл.
3.  **Определение языка**: Метод `locale` сначала пробует мета-тег, а затем JavaScript. Стоит рассмотреть вариант использования HTTP-заголовков для определения языка (например, `Accept-Language`).
4.  **Зависимость от `globals`**: Зависимость от `src.config.globals` может сделать класс менее переиспользуемым. Следует рассмотреть внедрение зависимостей.
5.  **Ожидание загрузки**: Ожидание загрузки страницы через `ready_state` может быть ненадежным в некоторых случаях. Стоит рассмотреть использование `WebDriverWait` из `selenium.webdriver.support.ui`.
6.   **Безопасность**: Проверка локального пути к файлу в `fetch_html` может быть неполной, лучше использовать более строгие проверки и использовать абсолютные пути.

#### Взаимосвязь с другими частями проекта:

*   **`src.config.globals`**: Используется для получения общих параметров, например, пути к файлу для сохранения куки.
*   **`selenium`**: Используется для управления браузером.
*   **`logging`**: Используется для ведения логов.

**Цепочка взаимосвязей**:

`Driver` <--> `selenium.webdriver` <--> `src.config.globals` <--> `logging` <--> `time`, `copy`, `pickle`

Этот анализ предоставляет полное Разбор кода `driver.py`, его структуры, функций и зависимостей, а также предлагает пути для улучшения и доработок.