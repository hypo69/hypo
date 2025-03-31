# Модуль `google_search`

## Обзор

Модуль `google_search` предназначен для парсинга HTML-страниц поисковой выдачи Google и извлечения полезной информации, такой как органические результаты поиска, featured snippets, карточки знаний и данные из скроллируемых виджетов. Он предоставляет класс `GoogleHtmlParser`, который облегчает разбор HTML-кода, полученного от Google Search, и преобразует его в структурированный словарь.

## Подробней

Этот модуль полезен для автоматизации сбора данных из поисковой выдачи Google. Он может быть использован для анализа конкурентов, мониторинга упоминаний бренда, сбора информации для исследований и других задач, требующих автоматического извлечения данных из поисковых систем. Класс `GoogleHtmlParser` поддерживает как мобильную, так и десктопную версии HTML, что делает его гибким инструментом для работы с различными типами поисковых запросов и устройств.

## Классы

### `GoogleHtmlParser`

**Описание**: Класс для парсинга HTML с Google Search.

**Как работает класс**: Класс `GoogleHtmlParser` принимает HTML-код страницы поисковой выдачи Google и user agent (mobile или desktop) в качестве входных данных. Он использует библиотеку `lxml` для создания дерева документа, по которому можно перемещаться и извлекать нужные данные с помощью XPath-запросов. Класс содержит методы для извлечения различных элементов страницы, таких как органические результаты поиска, featured snippets, карточки знаний и скроллируемые виджеты. Все извлеченные данные структурируются в виде словаря, который возвращается методом `get_data`.

**Методы**:
- `__init__`: Инициализация парсера.
- `_clean`: Очистка строки от лишних символов.
- `_normalize_dict_key`: Нормализация строки для использования в качестве ключа словаря.
- `_get_estimated_results`: Получение количества результатов поиска.
- `_get_organic`: Получение органических результатов поиска.
- `_get_featured_snippet`: Получение featured snippet.
- `_get_knowledge_card`: Получение карточки знаний.
- `_get_scrolling_sections`: Получение данных из скроллируемых виджетов.
- `get_data`: Получение итоговых данных с поисковой страницы.

**Параметры**:
- `html_str` (str): HTML Google Search в виде строки.
- `user_agent` (str): User agent для получения HTML. Может быть 'mobile' или 'desktop'.

**Примеры**
```python
from lxml import html

# Пример использования класса GoogleHtmlParser
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <div id="result-stats"> Примерно 10 000 результатов </div>
    <div class="g">
        <h3><a href="https://example.com">Example</a></h3>
        <div>Описание example.com</div>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
data = parser.get_data()
print(data)
# {'estimated_results': 10000, 'featured_snippet': None, 'knowledge_card': None, 'organic_results': [{'url': 'https://example.com', 'title': 'Example', 'snippet': 'Описание example.com', 'rich_snippet': None}], 'scrolling_widgets': []}
```

## Функции

### `__init__`

```python
def __init__(self, html_str: str, user_agent: str = 'desktop') -> None:
    """Инициализация парсера.

    Создает дерево документа из строки HTML.

    Args:
        html_str (str): HTML Google Search в виде строки.
        user_agent (str): User agent для получения HTML. Может быть 'mobile' или 'desktop'.

    Returns:
        None
    """
```

**Описание**: Инициализирует экземпляр класса `GoogleHtmlParser`.

**Как работает функция**: Функция `__init__` принимает HTML-код страницы поисковой выдачи Google и user agent (по умолчанию 'desktop') в качестве аргументов. Она создает дерево документа с помощью `html.fromstring(html_str)` из библиотеки `lxml`, которое используется для дальнейшего парсинга HTML-кода. Также проверяется, является ли указанный user agent допустимым ('mobile' или 'desktop'), и устанавливает соответствующее значение атрибута `self.user_agent`.

**Параметры**:
- `html_str` (str): HTML Google Search в виде строки.
- `user_agent` (str, optional): User agent для получения HTML. Может быть 'mobile' или 'desktop'. По умолчанию 'desktop'.

**Возвращает**:
- None

**Примеры**:

```python
parser = GoogleHtmlParser(html_str='<html>...</html>', user_agent='mobile')
```

### `_clean`

```python
def _clean(self, content: str) -> str:
    """Очистка строки от лишних символов.

    Очищает строку от пробелов и лишних символов.

    Args:
        content (str): Строка для очистки.

    Returns:
        str: Очищенная строка.
    """
```

**Описание**: Очищает строку от лишних пробелов и символов.

**Как работает функция**: Функция `_clean` принимает строку в качестве аргумента и удаляет из нее лишние пробелы в начале и конце, а также заменяет множественные пробелы на одинарные. Если входная строка `content` не пуста, она сначала удаляет пробелы в начале и конце с помощью `content.strip()`, а затем заменяет все множественные пробелы на одинарные с помощью `' '.join(content.split())`. Если строка пуста или `None`, возвращается пустая строка.

**Параметры**:
- `content` (str): Строка для очистки.

**Возвращает**:
- `str`: Очищенная строка.

**Примеры**:

```python
parser = GoogleHtmlParser(html_str='<html>...</html>')
cleaned_string = parser._clean(content='  Пример   строки  ')
print(cleaned_string)  # Вывод: 'Пример строки'
```

### `_normalize_dict_key`

```python
def _normalize_dict_key(self, content: str) -> str:
    """Нормализация строки для использования в качестве ключа словаря.

    Заменяет пробелы на подчеркивания, убирает двоеточия, приводит к нижнему регистру.

    Args:
        content (str): Строка для нормализации.

    Returns:
        str: Нормализованная строка.
    """
```

**Описание**: Нормализует строку для использования в качестве ключа словаря.

**Как работает функция**: Функция `_normalize_dict_key` принимает строку в качестве аргумента и выполняет следующие преобразования: заменяет все пробелы на символы подчеркивания (`_`), удаляет все двоеточия (`:`), приводит все символы к нижнему регистру и удаляет подчеркивания в начале и конце строки.

**Параметры**:
- `content` (str): Строка для нормализации.

**Возвращает**:
- `str`: Нормализованная строка.

**Примеры**:

```python
parser = GoogleHtmlParser(html_str='<html>...</html>')
normalized_key = parser._normalize_dict_key(content='  Пример строки: ')
print(normalized_key)  # Вывод: 'пример_строки'
```

### `_get_estimated_results`

```python
def _get_estimated_results(self) -> int:
    """Получение количества результатов поиска.

    Возвращает количество найденных результатов для десктопной версии Google Search.

    Returns:
        int: Число результатов поиска.
    """
```

**Описание**: Извлекает количество результатов поиска из HTML-кода страницы Google Search (desktop версия).

**Как работает функция**: Функция `_get_estimated_results` использует XPath-запрос `'//*[@id="result-stats"]/text()'` для поиска элемента, содержащего информацию о количестве результатов поиска. Если такой элемент найден, извлекает текст, разделяет его на части, чтобы получить число результатов, и возвращает это число в виде целого числа. Если элемент не найден, возвращает 0.

**Параметры**:
- None

**Возвращает**:
- `int`: Число результатов поиска.

**Примеры**:

```python
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <div id="result-stats"> Примерно 10 000 000 результатов </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
estimated_results = parser._get_estimated_results()
print(estimated_results)  # Вывод: 10000000
```

### `_get_organic`

```python
def _get_organic(self) -> list:
    """Получение органических результатов поиска.

    Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

    Returns:
        list: Список словарей с органическими результатами.
    """
```

**Описание**: Извлекает органические результаты поиска из HTML-кода страницы Google Search.

**Как работает функция**: Функция `_get_organic` использует XPath-запрос `'//div[@class="g"]'` для поиска всех блоков, содержащих органические результаты поиска. Для каждого найденного блока извлекаются URL, заголовок и сниппет. Результаты возвращаются в виде списка словарей, где каждый словарь содержит информацию об одном органическом результате поиска.

**Параметры**:
- None

**Возвращает**:
- `list`: Список словарей с органическими результатами.

**Примеры**:

```python
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <div class="g">
        <h3><a href="https://example.com">Example</a></h3>
        <div>Описание example.com</div>
    </div>
    <div class="g">
        <h3><a href="https://example.org">Example Org</a></h3>
        <div>Описание example.org</div>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
organic_results = parser._get_organic()
print(organic_results)
# Вывод:
# [{'url': 'https://example.com', 'title': 'Example', 'snippet': 'Описание example.com', 'rich_snippet': None},
#  {'url': 'https://example.org', 'title': 'Example Org', 'snippet': 'Описание example.org', 'rich_snippet': None}]
```

### `_get_featured_snippet`

```python
def _get_featured_snippet(self) -> dict | None:
    """Получение featured snippet.

    Если существует, возвращает featured snippet с заголовком и URL.

    Returns:
        dict | None: Словарь с заголовком и URL или None.
    """
```

**Описание**: Извлекает featured snippet из HTML-кода страницы Google Search.

**Как работает функция**: Функция `_get_featured_snippet` использует XPath-запрос `'//div[contains(@class, "kp-blk")]'` для поиска элемента, содержащего featured snippet. Если такой элемент найден, извлекает заголовок и URL и возвращает их в виде словаря. Если элемент не найден, возвращает `None`.

**Параметры**:
- None

**Возвращает**:
- `dict | None`: Словарь с заголовком и URL или `None`.

**Примеры**:

```python
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <div class="kp-blk">
        <h3><a href="https://example.com">Example Featured Snippet</a></h3>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
featured_snippet = parser._get_featured_snippet()
print(featured_snippet)
# Вывод: {'title': 'Example Featured Snippet', 'url': 'https://example.com'}
```

### `_get_knowledge_card`

```python
def _get_knowledge_card(self) -> dict | None:
    """Получение карточки знаний.

    Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

    Returns:
        dict | None: Словарь с данными карточки знаний или None.
    """
```

**Описание**: Извлекает карточку знаний из HTML-кода страницы Google Search.

**Как работает функция**: Функция `_get_knowledge_card` использует XPath-запрос `'//div[contains(@class, "kp-wholepage")]'` для поиска элемента, содержащего карточку знаний. Если такой элемент найден, извлекает заголовок, подзаголовок и описание и возвращает их в виде словаря. Если элемент не найден, возвращает `None`.

**Параметры**:
- None

**Возвращает**:
- `dict | None`: Словарь с данными карточки знаний или `None`.

**Примеры**:

```python
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <div class="kp-wholepage">
        <h2><span>Example Knowledge Card</span></h2>
        <div data-attrid="subtitle">Subtitle</div>
        <div class="kno-rdesc"><span>Description</span></div>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
knowledge_card = parser._get_knowledge_card()
print(knowledge_card)
# Вывод: {'title': 'Example Knowledge Card', 'subtitle': 'Subtitle', 'description': 'Description', 'more_info': []}
```

### `_get_scrolling_sections`

```python
def _get_scrolling_sections(self) -> list:
    """Получение данных из скроллируемых виджетов.

    Возвращает список данных из виджетов, например, топовые истории или твиты.

    Returns:
        list: Список словарей с данными из виджетов.
    """
```

**Описание**: Извлекает данные из скроллируемых виджетов (например, "Top stories" или "Tweets") из HTML-кода страницы Google Search.

**Как работает функция**: Функция `_get_scrolling_sections` использует XPath-запрос `'//g-section-with-header'` для поиска всех секций, содержащих скроллируемые виджеты. Для каждой найденной секции извлекается заголовок секции и данные из каждой карточки внутри секции (заголовок и URL). Результаты возвращаются в виде списка словарей, где каждый словарь содержит заголовок секции и список данных из карточек внутри этой секции.

**Параметры**:
- None

**Возвращает**:
- `list`: Список словарей с данными из виджетов.

**Примеры**:

```python
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <g-section-with-header>
        <h3>Top stories</h3>
        <g-inner-card>
            <div role="heading"><a>Example Story 1</a></div>
        </g-inner-card>
        <g-inner-card>
            <div role="heading"><a>Example Story 2</a></div>
        </g-inner-card>
    </g-section-with-header>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
scrolling_sections = parser._get_scrolling_sections()
print(scrolling_sections)
# Вывод:
# [{'section_title': 'Top stories', 'section_data': [{'title': 'Example Story 1', 'url': 'Example Story 1'}, {'title': 'Example Story 2', 'url': 'Example Story 2'}]}]
```

### `get_data`

```python
def get_data(self) -> dict:
    """Получение итоговых данных с поисковой страницы.

    Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

    Returns:
        dict: Словарь с данными поисковой страницы.
    """
```

**Описание**: Собирает итоговые данные с поисковой страницы Google Search.

**Как работает функция**: Функция `get_data` проверяет, является ли user agent `desktop`. Если это так, она вызывает методы для извлечения различных типов данных (количество результатов, featured snippet, карточка знаний, органические результаты и скроллируемые виджеты) и собирает их в словарь.

**Параметры**:
- None

**Возвращает**:
- `dict`: Словарь с данными поисковой страницы.

**Примеры**:

```python
html_string = """
<html>
<head><title>Google Search</title></head>
<body>
    <div id="result-stats"> Примерно 10 000 000 результатов </div>
    <div class="g">
        <h3><a href="https://example.com">Example</a></h3>
        <div>Описание example.com</div>
    </div>
    <div class="kp-blk">
        <h3><a href="https://example.com">Example Featured Snippet</a></h3>
    </div>
    <div class="kp-wholepage">
        <h2><span>Example Knowledge Card</span></h2>
        <div data-attrid="subtitle">Subtitle</div>
        <div class="kno-rdesc"><span>Description</span></div>
    </div>
    <g-section-with-header>
        <h3>Top stories</h3>
        <g-inner-card>
            <div role="heading"><a>Example Story 1</a></div>
        </g-inner-card>
    </g-section-with-header>
</body>
</html>
"""
parser = GoogleHtmlParser(html_string)
data = parser.get_data()
print(data)
# Вывод:
# {'estimated_results': 10000000, 'featured_snippet': {'title': 'Example Featured Snippet', 'url': 'https://example.com'}, 'knowledge_card': {'title': 'Example Knowledge Card', 'subtitle': 'Subtitle', 'description': 'Description', 'more_info': []}, 'organic_results': [{'url': 'https://example.com', 'title': 'Example', 'snippet': 'Описание example.com', 'rich_snippet': None}], 'scrolling_widgets': [{'section_title': 'Top stories', 'section_data': [{'title': 'Example Story 1', 'url': 'Example Story 1'}]}]}