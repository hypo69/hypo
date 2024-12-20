# Модуль `src.webdriver.bs`

## Обзор

Модуль `src.webdriver.bs` предоставляет пользовательскую реализацию для разбора HTML-контента с использованием `BeautifulSoup` и `XPath`.

## Оглавление
- [Классы](#классы)
    - [`BS`](#bs)
- [Функции](#функции)

## Классы

### `BS`

**Описание**: Класс для разбора HTML-контента с использованием `BeautifulSoup` и `XPath`.

**Атрибуты**:
- `html_content` (str): HTML-контент, который нужно разобрать.

**Методы**:
- `__init__`: Инициализирует парсер `BS` с необязательным URL.
- `get_url`: Получает HTML-контент из файла или URL и разбирает его с помощью `BeautifulSoup` и `XPath`.
- `execute_locator`: Выполняет `XPath` локатор на HTML-контенте.

#### `__init__`

**Описание**: Инициализирует парсер `BS` с необязательным URL.

**Параметры**:
- `url` (Optional[str], optional): URL или путь к файлу, из которого нужно получить HTML-контент. По умолчанию `None`.

#### `get_url`

**Описание**: Получает HTML-контент из файла или URL и разбирает его с помощью `BeautifulSoup` и `XPath`.

**Параметры**:
- `url` (str): Путь к файлу или URL, из которого нужно получить HTML-контент.

**Возвращает**:
- `bool`: `True`, если контент был успешно получен, `False` в противном случае.

#### `execute_locator`

**Описание**: Выполняет `XPath` локатор на HTML-контенте.

**Параметры**:
- `locator` (Union[SimpleNamespace, dict]): Объект локатора, содержащий селектор и атрибут.
- `url` (Optional[str], optional): Необязательный URL или путь к файлу для получения HTML-контента. По умолчанию `None`.

**Возвращает**:
- `List[etree._Element]`: Список элементов, соответствующих локатору.

## Функции

В данном модуле функции отсутствуют.