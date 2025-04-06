# Модуль для парсинга HTML с использованием BeautifulSoup и XPath
## Обзор

Модуль `src.webdriver.bs` предоставляет класс `BS` для парсинга HTML-контента с использованием библиотек `BeautifulSoup` и `lxml` (через XPath). Он позволяет загружать HTML как из локальных файлов, так и из URL-адресов, а также выполнять поиск элементов на странице с использованием XPath-локаторов. Этот модуль может быть полезен для извлечения данных из веб-страниц и автоматизации взаимодействия с веб-сайтами.

## Подробнее

Модуль `src.webdriver.bs` предоставляет класс `BS`, который инкапсулирует функциональность парсинга HTML-контента с использованием `BeautifulSoup` и `lxml`.

### Классы

### `BS`
**Описание**: Класс предназначен для парсинга HTML-контента с использованием BeautifulSoup и XPath.

**Принцип работы**:
1.  При инициализации класса можно передать URL, который будет сразу загружен и распарсен.
2.  Метод `get_url` загружает HTML-контент из файла или URL. Поддерживаются как локальные файлы (с префиксом `file://`), так и веб-страницы (с префиксом `https://`).
3.  Метод `execute_locator` выполняет XPath-запрос к загруженному HTML-контенту и возвращает список найденных элементов.

**Аттрибуты**:

*   `html_content` (str): HTML-контент, который будет распарсен.

**Методы**:

*   `__init__(url: Optional[str] = None)`: Инициализирует парсер `BS` с необязательным URL.
*   `get_url(url: str) -> bool`: Загружает HTML-контент из файла или URL.
*   `execute_locator(locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]`: Выполняет XPath-локатор на HTML-контенте.

### Функции

### `__init__`

```python
def __init__(self, url: Optional[str] = None):
    """
    Initializes the BS parser with an optional URL.

    :param url: The URL or file path to fetch HTML content from.
    :type url: Optional[str]
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `BS`. Если передан URL, то сразу пытается загрузить HTML-контент по этому URL.

**Параметры**:

*   `url` (Optional[str], optional): URL или путь к файлу, из которого нужно загрузить HTML-контент. По умолчанию `None`.

**Как работает функция**:

1.  Присваивает переданный URL атрибуту `url` экземпляра класса.
2.  Если `url` не равен `None`, вызывает метод `get_url(url)` для загрузки и парсинга HTML-контента.

```mermaid
graph LR
    A[Начало] --> B{url is not None?};
    B -- Yes --> C[self.get_url(url)];
    B -- No --> D[Конец];
    C --> D;
```

**Примеры**:

```python
# Инициализация без URL
parser = BS()

# Инициализация с URL
parser = BS('https://example.com')
```

### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath.

    :param url: The file path or URL to fetch HTML content from.
    :type url: str
    :return: True if the content was successfully fetched, False otherwise.
    :rtype: bool
    """
    ...
```

**Назначение**: Загружает HTML-контент из указанного URL или файла и сохраняет его в атрибуте `html_content`.

**Параметры**:

*   `url` (str): URL или путь к файлу, из которого нужно загрузить HTML-контент.

**Возвращает**:

*   `bool`: `True`, если контент успешно загружен, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, начинается ли URL с префикса `file://`.
    *   Если да, то пытается прочитать HTML-контент из локального файла.
        *   Удаляет префикс `file:///` из URL.
        *   Извлекает путь к файлу, используя регулярное выражение для поиска Windows-пути (например, `c:/...` или `C:/...`).
        *   Проверяет существование файла.
        *   Если файл существует, открывает его в кодировке `utf-8`, читает содержимое и сохраняет его в атрибуте `self.html_content`.
        *   В случае ошибки чтения файла, логирует ошибку и возвращает `False`.
        *   Если файл не найден или путь невалиден, логирует ошибку и возвращает `False`.
    *   Если URL начинается с `https://`, то пытается загрузить HTML-контент из сети.
        *   Выполняет GET-запрос к указанному URL.
        *   Проверяет статус код ответа (должен быть 200).
        *   Сохраняет HTML-контент в атрибуте `self.html_content`.
        *   В случае ошибки запроса (например, сетевые проблемы или неверный URL), логирует ошибку и возвращает `False`.
    *   Если URL не начинается ни с `file://`, ни с `https://`, логирует ошибку и возвращает `False`.

```mermaid
graph LR
    A[Начало] --> B{url.startswith('file://')?};
    B -- Yes --> C[Удаление префикса 'file://' и извлечение пути к файлу];
    C --> D{Проверка существования файла};
    D -- Yes --> E[Чтение содержимого файла в self.html_content];
    E --> F[Возврат True];
    D -- No --> G[Логирование ошибки 'Local file not found:'];
    G --> H[Возврат False];
    B -- No --> I{url.startswith('https://')?};
    I -- Yes --> J[Выполнение GET-запроса к URL];
    J --> K{Проверка статуса ответа};
    K -- OK --> L[Сохранение HTML-контента в self.html_content];
    L --> F;
    K -- Error --> M[Логирование ошибки запроса];
    M --> H;
    I -- No --> N[Логирование ошибки 'Invalid URL or file path:'];
    N --> H;
```

**Примеры**:

```python
# Загрузка из URL
result = parser.get_url('https://example.com')

# Загрузка из локального файла
result = parser.get_url('file:///c:/path/to/file.html')
```

### `execute_locator`

```python
def execute_locator(self, locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]:
    """
    Execute an XPath locator on the HTML content.

    :param locator: The locator object containing the selector and attribute.
    :type locator: Union[SimpleNamespace, dict]
    :param url: Optional URL or file path to fetch HTML content from.
    :type url: Optional[str]
    :return: A list of elements matching the locator.
    :rtype: List[etree._Element]
    """
    ...
```

**Назначение**: Выполняет XPath-локатор на HTML-контенте и возвращает список найденных элементов.

**Параметры**:

*   `locator` (Union[SimpleNamespace, dict]): Объект, содержащий информацию о локаторе (тип, атрибут, селектор). Может быть представлен как `SimpleNamespace` или `dict`.
*   `url` (Optional[str], optional): URL или путь к файлу, из которого нужно загрузить HTML-контент. Если указан, то HTML-контент будет загружен из этого URL перед выполнением локатора. По умолчанию `None`.

**Возвращает**:

*   `List[etree._Element]`: Список элементов, соответствующих локатору.

**Как работает функция**:

1.  Если передан параметр `url`, вызывает метод `get_url(url)` для загрузки HTML-контента.
2.  Проверяет, что атрибут `self.html_content` не пустой. Если пустой, логирует ошибку и возвращает пустой список.
3.  Создает объект `BeautifulSoup` из HTML-контента, используя парсер `lxml`.
4.  Преобразует объект `BeautifulSoup` в дерево `lxml.etree` для поддержки XPath.
5.  Если `locator` является словарем, преобразует его в объект `SimpleNamespace`.
6.  Извлекает значения атрибутов `attribute`, `by` и `selector` из объекта `locator`.
7.  В зависимости от значения атрибута `by` (ID, CSS, TEXT или XPath), формирует XPath-запрос.
8.  Выполняет XPath-запрос к дереву `lxml.etree` и возвращает список найденных элементов.

```mermaid
graph LR
    A[Начало] --> B{url is not None?};
    B -- Yes --> C[self.get_url(url)];
    C --> D{self.html_content is not None?};
    B -- No --> D;
    D -- Yes --> E[Создание BeautifulSoup объекта];
    E --> F[Преобразование BeautifulSoup в lxml.etree];
    F --> G{locator is dict?};
    G -- Yes --> H[Преобразование dict в SimpleNamespace];
    H --> I[Извлечение attribute, by, selector из locator];
    G -- No --> I;
    I --> J{by == 'ID'?};
    J -- Yes --> K[Формирование XPath-запроса для ID];
    J -- No --> L{by == 'CSS'?};
    L -- Yes --> M[Формирование XPath-запроса для CSS];
    L -- No --> N{by == 'TEXT'?};
    N -- Yes --> O[Формирование XPath-запроса для TEXT];
    N -- No --> P[Использование selector как XPath];
    K --> Q[Выполнение XPath-запроса];
    M --> Q;
    O --> Q;
    P --> Q;
    Q --> R[Возврат списка найденных элементов];
    D -- No --> S[Логирование ошибки 'No HTML content available for parsing.'];
    S --> T[Возврат []];
```

**Примеры**:

```python
# Создание объекта locator
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')

# Выполнение локатора
elements = parser.execute_locator(locator)

# Выполнение локатора с загрузкой HTML из URL
elements = parser.execute_locator(locator, url='https://example.com')
```