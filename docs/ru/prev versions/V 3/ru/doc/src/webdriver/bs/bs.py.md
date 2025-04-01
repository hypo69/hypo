# Модуль `src.webdriver.bs`

## Обзор

Модуль `src.webdriver.bs` предоставляет инструменты для парсинга HTML-контента с использованием библиотек `BeautifulSoup` и `lxml` (через XPath). Он позволяет извлекать данные из веб-страниц или локальных HTML-файлов, используя как CSS-селекторы, так и XPath-выражения.

## Подробнее

Этот модуль предназначен для облегчения анализа HTML-структуры документов. Он предоставляет класс `BS`, который может загружать HTML-контент из URL-адресов или локальных файлов и выполнять XPath-запросы для поиска определенных элементов. Модуль активно использует логирование для отслеживания ошибок и предупреждений, что помогает в отладке и обслуживании.
Данный модуль используется для парсинга загруженных HTML страниц, для дальнейшего извлечения данных.

## Классы

### `BS`

**Описание**: Класс для парсинга HTML-контента с использованием BeautifulSoup и XPath.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `BS`.
- `get_url`: Получает HTML-контент из URL или файла.
- `execute_locator`: Выполняет XPath-локатор для поиска элементов в HTML-контенте.

#### `__init__`

```python
    def __init__(self, url: Optional[str] = None):
        """
        Initializes the BS parser with an optional URL.

        :param url: The URL or file path to fetch HTML content from.
        :type url: Optional[str]
        """
```

**Описание**: Инициализирует класс `BS` с возможностью сразу загрузить HTML-контент из указанного URL.

**Параметры**:
- `url` (Optional[str], optional): URL или путь к файлу, из которого нужно получить HTML-контент. По умолчанию `None`.

**Примеры**:
```python
parser = BS('https://example.com')
```

#### `get_url`

```python
    def get_url(self, url: str) -> bool:
        """
        Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath.

        :param url: The file path or URL to fetch HTML content from.
        :type url: str
        :return: True if the content was successfully fetched, False otherwise.
        :rtype: bool
        """
```

**Описание**: Получает HTML-контент из указанного URL-адреса или локального файла. Поддерживает `file://` и `https://` протоколы.

**Параметры**:
- `url` (str): URL-адрес или путь к локальному файлу.

**Возвращает**:
- `bool`: `True`, если контент успешно получен, `False` в противном случае.

**Вызывает исключения**:
- `requests.RequestException`: Если возникает ошибка при выполнении HTTP-запроса.
- `Exception`: Если возникает ошибка при чтении локального файла.

**Примеры**:
```python
parser = BS()
success = parser.get_url('https://example.com')
if success:
    print('HTML content loaded successfully.')
else:
    print('Failed to load HTML content.')
```

#### `execute_locator`

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
```

**Описание**: Выполняет XPath-запрос к HTML-контенту для поиска элементов, соответствующих заданному локатору.

**Параметры**:
- `locator` (Union[SimpleNamespace, dict]): Объект, содержащий параметры локатора, такие как тип поиска (`by`) и значение атрибута (`attribute`).
- `url` (Optional[str], optional): URL-адрес или путь к файлу, из которого нужно получить HTML-контент. Если указан, HTML-контент будет загружен перед выполнением локатора. По умолчанию `None`.

**Возвращает**:
- `List[etree._Element]`: Список найденных элементов, соответствующих локатору.

**Примеры**:
```python
parser = BS('https://example.com')
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
elements = parser.execute_locator(locator)
if elements:
    print(f'Found {len(elements)} elements.')
else:
    print('No elements found.')
```

## Функции

В данном модуле функции отсутствуют.