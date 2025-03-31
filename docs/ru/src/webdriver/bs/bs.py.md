# Модуль `src.webdriver.bs`

## Обзор

Модуль `src.webdriver.bs` предназначен для парсинга HTML-контента с использованием библиотек `BeautifulSoup` и `lxml` (через XPath). Он предоставляет класс `BS`, который позволяет загружать HTML-контент из URL-адресов или локальных файлов и извлекать элементы на основе XPath-локаторов.

## Подробнее

Этот модуль предоставляет удобный интерфейс для извлечения данных из HTML-страниц. Он поддерживает загрузку контента как из веб-адресов, так и из локальных файлов, что делает его гибким инструментом для веб-скрапинга и автоматизации. Класс `BS` использует `BeautifulSoup` для предварительной обработки HTML и `lxml` для выполнения XPath-запросов.

## Оглавление

- [Классы](#Классы)
    - [BS](#BS)
        - [Описание](#Описание)
        - [Методы](#Методы)
            - [`__init__`](#__init__)
            - [`get_url`](#get_url)
            - [`execute_locator`](#execute_locator)

## Классы

### `BS`

**Описание**: Класс для парсинга HTML-контента с использованием `BeautifulSoup` и XPath.

**Как работает класс**:
Класс `BS` инициализируется с возможностью указания URL-адреса для загрузки HTML-контента. Он предоставляет методы для загрузки HTML из URL-адресов или файлов, а также для выполнения XPath-запросов к загруженному контенту. Внутренне класс использует `BeautifulSoup` для парсинга HTML и `lxml` для выполнения XPath-запросов.

**Атрибуты**:

-   `html_content` (str): HTML-контент для парсинга.

#### Методы

##### `__init__`

```python
def __init__(self, url: Optional[str] = None):
    """
    Initializes the BS parser with an optional URL.

    :param url: The URL or file path to fetch HTML content from.
    :type url: Optional[str]
    """
    if url:
        self.get_url(url)
```

**Назначение**: Инициализирует парсер `BS` с опциональным URL.

**Как работает функция**:
Конструктор класса `BS`. Если передан URL, он сразу вызывает метод `get_url` для загрузки HTML-контента.

**Параметры**:

-   `url` (Optional[str], optional): URL-адрес или путь к файлу для получения HTML-контента. По умолчанию `None`.

##### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath.

    :param url: The file path or URL to fetch HTML content from.
    :type url: str
    :return: True if the content was successfully fetched, False otherwise.
    :rtype: bool
    """
    if url.startswith('file://'):
        # Remove 'file://' prefix and clean up the path
        cleaned_url = url.replace(r'file:///', '')

        # Extract the Windows path if it's in the form of 'c:/...' or 'C:/...'
        match = re.search(r'[a-zA-Z]:[\\\\/].*', cleaned_url)
        if match:
            file_path = Path(match.group(0))
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.html_content = file.read()
                    return True
                except Exception as ex:
                    logger.error('Exception while reading the file:', ex)
                    return False
            else:
                logger.error('Local file not found:', file_path)
                return False
        else:
            logger.error('Invalid file path:', cleaned_url)
            return False
    elif url.startswith('https://'):
        # Handle web URLs
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP request errors
            self.html_content = response.text
            return True
        except requests.RequestException as ex:
            logger.error(f"Error fetching {url}:", ex)
            return False
    else:
        logger.error('Invalid URL or file path:', url)
        return False
```

**Назначение**: Получает HTML-контент из файла или URL-адреса и парсит его с помощью `BeautifulSoup` и XPath.

**Как работает функция**:
Метод `get_url` загружает HTML-контент из указанного URL-адреса или файла. Если URL начинается с `file://`, он пытается прочитать файл локально. Если URL начинается с `https://`, он выполняет HTTP-запрос для получения контента. В случае успеха контент сохраняется в атрибуте `html_content`.

**Параметры**:

-   `url` (str): Путь к файлу или URL-адрес для получения HTML-контента.

**Возвращает**:

-   `bool`: `True`, если контент успешно получен, `False` в противном случае.

**Вызывает исключения**:

-   `requests.RequestException`: Если возникает ошибка при выполнении HTTP-запроса.

##### `execute_locator`

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
    if url:
        self.get_url(url)

    if not self.html_content:
        logger.error('No HTML content available for parsing.')
        return []

    soup = BeautifulSoup(self.html_content, 'lxml')
    tree = etree.HTML(str(soup))  # Convert BeautifulSoup object to lxml tree

    if isinstance(locator, dict):
        locator = SimpleNamespace(**locator)

    attribute = locator.attribute
    by = locator.by.upper()
    selector = locator.selector
    elements = None

    if by == 'ID':
        elements = tree.xpath(f'//*[@id="{attribute}"]')
    elif by == 'CSS':
        elements = tree.xpath(f'//*[contains(@class, "{attribute}")]')
    elif by == 'TEXT':
        elements = tree.xpath(f'//input[@type="{attribute}"]')
    else:
        elements = tree.xpath(selector)

    return elements
```

**Назначение**: Выполняет XPath-локатор на HTML-контенте.

**Как работает функция**:
Метод `execute_locator` выполняет XPath-запрос к HTML-контенту. Он принимает локатор, который может быть объектом `SimpleNamespace` или словарем, содержащим информацию о селекторе и атрибуте. Метод использует `BeautifulSoup` для парсинга HTML и `lxml` для выполнения XPath-запроса. Результатом является список элементов, соответствующих локатору.

**Параметры**:

-   `locator` (Union[SimpleNamespace, dict]): Объект локатора, содержащий селектор и атрибут.
-   `url` (Optional[str], optional): Опциональный URL-адрес или путь к файлу для получения HTML-контента. По умолчанию `None`.

**Возвращает**:

-   `List[etree._Element]`: Список элементов, соответствующих локатору.