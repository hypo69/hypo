# Модуль hypotez/src/webdriver/bs/bs.py

## Обзор

Модуль `bs.py` предоставляет класс `BS` для работы с HTML-контентом, полученным из файла или URL, используя библиотеку `BeautifulSoup` и XPath. Он поддерживает чтение из файлов и запрос веб-страниц.  Модуль позволяет локализовать элементы на странице по различным селекторам.

## Классы

### `BS`

**Описание**: Класс `BS` предназначен для парсинга HTML-контента, полученного из файла или URL.  Он предоставляет методы для загрузки и обработки HTML-данных.

**Методы**:

#### `__init__`

**Описание**: Конструктор класса `BS`.

**Параметры**:

- `url` (str, необязательно): URL или путь к файлу, содержащий HTML-контент. Если не указано, `url` устанавливается в `None`.

**Возвращает**:
-  None

#### `get_url`

**Описание**: Загружает HTML-контент из файла или URL.

**Параметры**:

- `url` (str): Путь к файлу или URL, откуда нужно загрузить HTML-контент.

**Возвращает**:
- bool: `True`, если загрузка успешна, `False` иначе.

**Обрабатывает исключения**:

- `Exception`: Логирует ошибку при чтении файла.
- `requests.RequestException`: Логирует ошибку при запросе URL.

#### `execute_locator`

**Описание**: Выполняет поиск элементов на странице по заданному локатору.

**Параметры**:

- `locator` (SimpleNamespace | dict): Объект `SimpleNamespace` или словарь с локатором.
    - `attribute`: Атрибут для поиска (например, id, класс).
    - `by`: Тип локатора (`ID`, `CSS`, `TEXT`).
    - `selector`: XPath селектор для поиска.
- `url` (str, необязательно): URL страницы для парсинга, если он не содержится в локаторе.

**Возвращает**:
- list: Список найденных элементов (объекты lxml). Возвращает `None` в случае ошибки.

**Обрабатывает исключения**:

- `Exception`: Логирует любую другую ошибку.

## Функции

(Нет функций в этом модуле)

## Примеры использования

```python
from hypotez.src.webdriver.bs import BS
from src.logger import logger

# Пример использования для файла
file_url = 'file:///path/to/your/file.html'  # Замените на правильный путь
bs_instance = BS()
success = bs_instance.get_url(file_url)

if success:
    locator = SimpleNamespace(attribute='my_element_id', by='ID', selector='//div[@id="my_element_id"]')
    elements = bs_instance.execute_locator(locator)
    if elements:
        for element in elements:
            print(element.text)
    else:
        logger.error("No elements found.")

# Пример использования для URL
url = 'https://example.com'
bs_instance = BS()
success = bs_instance.get_url(url)
if success:
    locator = SimpleNamespace(attribute='search', by='CSS', selector='//input[@type="text"]')
    elements = bs_instance.execute_locator(locator, url)  # Укажите URL, если он не задан в locator
    if elements:
        for element in elements:
            print(element.text)
    else:
        logger.error("No elements found.")

```

**Примечание:**  Замените `'path/to/your/file.html'` на фактический путь к вашему HTML-файлу и `'https://example.com'` на нужный URL.  Также убедитесь, что соответствующие импорты и настройки `logger` у вас работают.