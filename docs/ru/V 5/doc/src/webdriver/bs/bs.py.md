# Модуль `src.webdriver.bs`

## Обзор

Модуль `src.webdriver.bs` предоставляет функциональность для парсинга HTML-контента с использованием библиотек `BeautifulSoup` и `lxml` (через XPath). Он предназначен для извлечения данных из HTML-страниц или файлов, позволяя выполнять поиск элементов по различным атрибутам и селекторам.

## Подробней

Этот модуль предоставляет класс `BS`, который инкапсулирует логику парсинга HTML. Он поддерживает загрузку HTML-контента как из URL-адресов (включая `https://`), так и из локальных файлов (с использованием протокола `file://`). Основной функциональностью является метод `execute_locator`, который принимает локатор XPath и возвращает список элементов, соответствующих этому локатору. Этот модуль может быть полезен для автоматизированного извлечения информации из веб-страниц, анализа структуры HTML и выполнения задач, связанных с веб-скрапингом.

## Классы

### `BS`

**Описание**: Класс для парсинга HTML-контента с использованием `BeautifulSoup` и XPath.

**Как работает класс**:
Класс `BS` инициализируется с возможностью указания URL-адреса для загрузки HTML-контента. Он содержит методы для загрузки HTML из URL или файла (`get_url`) и выполнения XPath-запросов для извлечения элементов (`execute_locator`). Внутренне использует `BeautifulSoup` для предварительной обработки HTML и `lxml` для выполнения XPath-запросов.

**Атрибуты**:
- `html_content` (str): HTML-контент для парсинга. Изначально устанавливается в `None`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `BS`.
- `get_url`: Загружает HTML-контент из указанного URL или файла.
- `execute_locator`: Выполняет XPath-запрос и возвращает список найденных элементов.

#### `__init__`

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

**Описание**: Инициализирует класс `BS` с возможностью сразу загрузить HTML-контент из указанного URL.

**Как работает функция**:
Конструктор класса, который принимает необязательный параметр `url`. Если URL предоставлен, он сразу вызывает метод `get_url` для загрузки HTML-контента.

**Параметры**:
- `url` (Optional[str], optional): URL-адрес или путь к файлу для загрузки HTML-контента. По умолчанию `None`.

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

**Описание**: Загружает HTML-контент из указанного URL или файла.

**Как работает функция**:
Метод `get_url` принимает URL-адрес или путь к файлу и пытается загрузить HTML-контент. Он поддерживает протоколы `file://` для локальных файлов и `https://` для веб-страниц. Для локальных файлов он извлекает путь к файлу, проверяет его существование и читает содержимое. Для веб-страниц он использует библиотеку `requests` для выполнения HTTP-запроса и извлекает HTML-контент из ответа. В случае возникновения ошибок при чтении файла или выполнении HTTP-запроса, он логирует ошибку и возвращает `False`.

**Параметры**:
- `url` (str): URL-адрес или путь к файлу для загрузки HTML-контента.

**Возвращает**:
- `bool`: `True`, если контент был успешно загружен, `False` в противном случае.

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

**Описание**: Выполняет XPath-запрос на HTML-контенте.

**Как работает функция**:
Метод `execute_locator` принимает локатор XPath (в виде `SimpleNamespace` или `dict`) и выполняет его на HTML-контенте. Он использует `BeautifulSoup` для парсинга HTML и `lxml` для выполнения XPath-запроса. Локатор должен содержать атрибуты `attribute`, `by` и `selector`, определяющие, как искать элементы. В зависимости от значения атрибута `by` (ID, CSS, TEXT или XPath), он формирует XPath-запрос и выполняет его. Возвращает список элементов, соответствующих запросу.

**Параметры**:
- `locator` (Union[SimpleNamespace, dict]): Локатор, содержащий атрибуты `attribute`, `by` и `selector`.
- `url` (Optional[str], optional): URL-адрес или путь к файлу для загрузки HTML-контента. По умолчанию `None`.

**Возвращает**:
- `List[etree._Element]`: Список элементов, соответствующих локатору.

## Функции

В данном модуле функции отсутствуют.