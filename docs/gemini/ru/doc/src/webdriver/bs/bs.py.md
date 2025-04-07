# Модуль `src.webdriver.bs`

## Обзор

Модуль `src.webdriver.bs` предоставляет инструменты для парсинга HTML-контента с использованием библиотек `BeautifulSoup` и `lxml` с поддержкой XPath. Он предназначен для извлечения данных из HTML-страниц и XML-документов, что особенно полезно при автоматизации тестирования и сборе данных из веба.

## Подробнее

Модуль содержит класс `BS`, который позволяет загружать HTML-контент из URL-адресов или локальных файлов, а затем выполнять XPath-запросы для поиска элементов на странице. Это упрощает процесс навигации по структуре HTML и извлечения нужной информации.

## Классы

### `BS`

**Описание**: Класс `BS` предназначен для парсинга HTML-контента с использованием BeautifulSoup и XPath.

**Принцип работы**:
1.  При инициализации класса можно указать URL, из которого будет загружен HTML-контент.
2.  Метод `get_url` загружает HTML-контент из указанного URL или файла. Поддерживаются URL, начинающиеся с `file://` и `https://`.
3.  Метод `execute_locator` выполняет XPath-запрос к загруженному HTML-контенту и возвращает список найденных элементов.

**Аттрибуты**:

*   `html_content` (str): HTML-контент, который будет парситься.

**Методы**:

*   `__init__(url: Optional[str] = None)`: Инициализирует экземпляр класса `BS` с необязательным URL.
*   `get_url(url: str) -> bool`: Загружает HTML-контент из URL или файла.
*   `execute_locator(locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]`: Выполняет XPath-запрос к HTML-контенту.

#### `__init__`

```python
def __init__(self, url: Optional[str] = None):
    """
    Initializes the BS parser with an optional URL.

    :param url: The URL or file path to fetch HTML content from.
    :type url: Optional[str]
    """
    ...
```

**Назначение**: Инициализирует класс `BS` с возможностью указания URL для загрузки HTML-контента.

**Параметры**:

*   `url` (Optional[str]): URL-адрес или путь к файлу, из которого нужно получить HTML-контент. По умолчанию `None`.

**Как работает функция**:
1.  Проверяет, был ли передан URL при инициализации класса.
2.  Если URL был передан, вызывает метод `get_url` для загрузки HTML-контента.

```
A[Инициализация класса BS]
|
B[Проверка наличия URL]
|
C[Вызов get_url(url), если URL существует]
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
    ...
```

**Назначение**: Загружает HTML-контент из файла или URL.

**Параметры**:

*   `url` (str): URL-адрес или путь к файлу, из которого нужно получить HTML-контент.

**Возвращает**:

*   `bool`: `True`, если контент успешно загружен, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, начинается ли URL с `file://`. Если да, то обрабатывает как локальный файл.
    *   Удаляет префикс `file:///` из URL.
    *   Извлекает путь к файлу, используя регулярное выражение.
    *   Проверяет существование файла.
    *   Если файл существует, пытается открыть его и прочитать содержимое в кодировке UTF-8.
    *   В случае успеха, сохраняет содержимое в атрибут `self.html_content` и возвращает `True`.
    *   В случае ошибки, логирует ошибку и возвращает `False`.
2.  Если URL начинается с `https://`, обрабатывает как веб-URL.
    *   Выполняет HTTP-запрос к указанному URL.
    *   Проверяет статус ответа (код 200 означает успех).
    *   Сохраняет HTML-контент из ответа в атрибут `self.html_content` и возвращает `True`.
    *   В случае ошибки, логирует ошибку и возвращает `False`.
3.  Если URL не начинается ни с `file://`, ни с `https://`, логирует ошибку и возвращает `False`.

```
A[Получение URL]
|
B[Проверка типа URL (file:// или https://)]
|
C[Обработка file:// URL]          D[Обработка https:// URL]
|                                  |
E[Извлечение пути к файлу]         F[HTTP-запрос к URL]
|                                  |
G[Чтение содержимого файла]         H[Получение HTML-контента из ответа]
|                                  |
I[Сохранение контента в self.html_content]
```

**Примеры**:

```python
parser = BS()
result = parser.get_url('file:///c:/path/to/file.html')
print(result)  # True или False

parser = BS()
result = parser.get_url('https://example.com')
print(result)  # True или False
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
    ...
```

**Назначение**: Выполняет XPath-запрос к HTML-контенту и возвращает список найденных элементов.

**Параметры**:

*   `locator` (Union[SimpleNamespace, dict]): Объект локатора, содержащий селектор и атрибут.
*   `url` (Optional[str]): URL-адрес или путь к файлу, из которого нужно получить HTML-контент. По умолчанию `None`.

**Возвращает**:

*   `List[etree._Element]`: Список элементов, соответствующих локатору.

**Как работает функция**:

1.  Если передан URL, вызывает метод `get_url` для загрузки HTML-контента.
2.  Проверяет, загружен ли HTML-контент. Если нет, логирует ошибку и возвращает пустой список.
3.  Использует `BeautifulSoup` для парсинга HTML-контента.
4.  Преобразует объект `BeautifulSoup` в дерево `lxml` для поддержки XPath.
5.  Если локатор является словарем, преобразует его в объект `SimpleNamespace`.
6.  Извлекает атрибуты `attribute`, `by` и `selector` из объекта локатора.
7.  В зависимости от значения атрибута `by`, формирует XPath-запрос и выполняет его.
8.  Возвращает список найденных элементов.

```
A[Получение локатора и URL]
|
B[Проверка наличия URL]
|
C[Вызов get_url(url), если URL существует]
|
D[Проверка наличия HTML-контента]
|
E[Парсинг HTML-контента с помощью BeautifulSoup]
|
F[Преобразование BeautifulSoup в lxml]
|
G[Извлечение атрибутов локатора]
|
H[Выполнение XPath-запроса в зависимости от типа локатора]
|
I[Возврат списка найденных элементов]
```

**Примеры**:

```python
parser = BS()
parser.get_url('https://example.com')
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
elements = parser.execute_locator(locator)
print(elements)
```
```python
parser = BS()
parser.get_url('https://example.com')
locator = {'by': 'ID', 'attribute': 'element_id', 'selector': '//*[@id="element_id"]'}
elements = parser.execute_locator(locator)
print(elements)
```

## Функции

В данном модуле функции отсутствуют.