# Модуль `src.webdriver.bs`

## Обзор

Модуль `src.webdriver.bs` предоставляет функциональность для парсинга HTML-контента с использованием библиотек `BeautifulSoup` и `lxml` (через XPath). Он предназначен для извлечения данных из HTML-страниц, как локальных, так и полученных из сети, на основе заданных локаторов XPath.

## Подробнее

Этот модуль предоставляет класс `BS`, который инкапсулирует логику парсинга HTML. Он поддерживает загрузку HTML-контента из URL-адресов и локальных файлов, а также позволяет выполнять XPath-запросы для поиска элементов на странице. Модуль использует `BeautifulSoup` для предварительной обработки HTML и `lxml` для выполнения XPath-запросов, обеспечивая гибкий и мощный механизм парсинга.

В проекте `hypotez` данный модуль может использоваться для автоматического извлечения данных с веб-страниц или из HTML-файлов, что полезно для задач, требующих сбора и обработки информации из различных источников.

## Классы

### `BS`

**Описание**: Класс для парсинга HTML-контента с использованием `BeautifulSoup` и XPath.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `BS`.
- `get_url`: Загружает HTML-контент из URL или файла.
- `execute_locator`: Выполняет XPath-локатор на HTML-контенте.

**Параметры**:
- `url` (Optional[str]): URL или путь к файлу для загрузки HTML-контента.

**Примеры**

```python
from src.webdriver.bs.bs import BS
from types import SimpleNamespace

# Пример использования класса BS
parser = BS()
parser.get_url('https://example.com')
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
elements = parser.execute_locator(locator)
print(elements)
```

## Функции

### `__init__`

```python
def __init__(self, url: Optional[str] = None):
    """
    Initializes the BS parser with an optional URL.

    :param url: The URL or file path to fetch HTML content from.
    :type url: Optional[str]
    """
```

**Описание**: Инициализирует класс `BS` с возможностью загрузки HTML-контента из указанного URL.

**Параметры**:
- `url` (Optional[str]): URL-адрес или путь к файлу, из которого будет загружен HTML-контент.

**Примеры**:
```python
from src.webdriver.bs.bs import BS

# Инициализация BS без URL
parser = BS()

# Инициализация BS с URL
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
```

**Описание**: Загружает HTML-контент из указанного URL-адреса или файла и сохраняет его во внутреннем атрибуте `html_content`.

**Параметры**:
- `url` (str): URL-адрес или путь к файлу для загрузки HTML-контента.

**Возвращает**:
- `bool`: `True`, если контент успешно загружен, `False` в противном случае.

**Вызывает исключения**:
- `requests.RequestException`: Возникает при проблемах с сетевым запросом.
- `Exception`: Возникает при проблемах с чтением локального файла.

**Примеры**:
```python
from src.webdriver.bs.bs import BS

parser = BS()
# Загрузка из URL
success = parser.get_url('https://example.com')
print(success)

# Загрузка из локального файла
success = parser.get_url('file:///path/to/your/file.html')
print(success)
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
```

**Описание**: Выполняет XPath-локатор на HTML-контенте, используя `lxml`.

**Параметры**:
- `locator` (Union[SimpleNamespace, dict]): Объект локатора, содержащий селектор и атрибут.
- `url` (Optional[str], optional): URL-адрес или путь к файлу для загрузки HTML-контента, если он еще не загружен. По умолчанию `None`.

**Возвращает**:
- `List[etree._Element]`: Список элементов, соответствующих локатору.

**Примеры**:
```python
from src.webdriver.bs.bs import BS
from types import SimpleNamespace

parser = BS()
parser.get_url('https://example.com')
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
elements = parser.execute_locator(locator)
print(elements)