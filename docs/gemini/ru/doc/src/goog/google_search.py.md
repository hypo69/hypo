# Модуль `google_search`

## Обзор

Модуль `google_search` предназначен для парсинга HTML-страниц поисковой выдачи Google и извлечения структурированных данных. Он содержит класс `GoogleHtmlParser`, который позволяет извлекать информацию, такую как органические результаты поиска, featured snippet, карточки знаний и данные из скроллируемых виджетов.

## Подробней

Этот модуль играет важную роль в проекте, обеспечивая возможность автоматизированного анализа поисковой выдачи Google. Он может быть использован для мониторинга позиций веб-сайтов в поисковой выдаче, анализа контента featured snippets и карточек знаний, а также для сбора данных из скроллируемых виджетов, таких как "Топ новости" или "Твиты".

## Классы

### `GoogleHtmlParser`

**Описание**: Класс для парсинга HTML с Google Search.

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
from src.goog.google_search import GoogleHtmlParser

html_content = "<html><body>...</body></html>"  #  HTML-содержимое страницы Google Search
parser = GoogleHtmlParser(html_content)
data = parser.get_data()
print(data)
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
    ...
```

**Описание**: Инициализирует экземпляр класса `GoogleHtmlParser`, создавая дерево документа из предоставленной HTML-строки.

**Параметры**:
- `html_str` (str): HTML-код страницы поисковой выдачи Google.
- `user_agent` (str, optional): User agent, используемый для запроса HTML-страницы. Допустимые значения: `'mobile'` или `'desktop'`. По умолчанию `'desktop'`.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Инициализирует `self.tree` путем преобразования входной строки `html_str` в дерево HTML с помощью `html.fromstring()`.
2.  Проверяет, является ли предоставленный `user_agent` допустимым (`'mobile'` или `'desktop'`).
3.  Если `user_agent` допустим, присваивает его `self.user_agent`; в противном случае устанавливает `self.user_agent` в значение по умолчанию `'desktop'`.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример с использованием desktop user-agent
parser_desktop = GoogleHtmlParser(html_str='<html>...</html>', user_agent='desktop')
print(parser_desktop.user_agent)  # Вывод: desktop

# Пример с использованием mobile user-agent
parser_mobile = GoogleHtmlParser(html_str='<html>...</html>', user_agent='mobile')
print(parser_mobile.user_agent)  # Вывод: mobile

# Пример с некорректным user-agent (будет использован desktop по умолчанию)
parser_incorrect = GoogleHtmlParser(html_str='<html>...</html>', user_agent='incorrect')
print(parser_incorrect.user_agent)  # Вывод: desktop
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
    ...
```

**Описание**: Очищает входную строку `content` от начальных и конечных пробелов, а также от повторяющихся пробелов внутри строки.

**Параметры**:
- `content` (str): Строка, которую необходимо очистить.

**Возвращает**:
- `str`: Очищенная строка. Если входная строка `content` пуста или `None`, возвращает пустую строку.

**Как работает функция**:

1.  Проверяет, не является ли входная строка `content` пустой. Если она пуста, возвращает пустую строку.
2.  Удаляет начальные и конечные пробелы с помощью `content.strip()`.
3.  Заменяет все повторяющиеся пробелы внутри строки на одинарные пробелы, используя `' '.join(content.split())`.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

parser = GoogleHtmlParser(html_str='')  # Создаем экземпляр класса, html_str не важен для этого метода

# Пример с обычной строкой
text = "  Пример   строки   с   пробелами  "
cleaned_text = parser._clean(text)
print(cleaned_text)  # Вывод: "Пример строки с пробелами"

# Пример с пустой строкой
empty_text = ""
cleaned_empty_text = parser._clean(empty_text)
print(cleaned_empty_text)  # Вывод: ""

# Пример со строкой, содержащей только пробелы
spaces_text = "   "
cleaned_spaces_text = parser._clean(spaces_text)
print(cleaned_spaces_text)  # Вывод: ""
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
    ...
```

**Описание**: Нормализует входную строку для использования в качестве ключа словаря.

**Параметры**:
- `content` (str): Строка, которую необходимо нормализовать.

**Возвращает**:
- `str`: Нормализованная строка, преобразованная в нижний регистр, с замененными пробелами на подчеркивания и удаленными двоеточиями.

**Как работает функция**:

1.  Преобразует входной `content` в строковый тип данных.
2.  Заменяет все пробелы в строке на символы подчеркивания.
3.  Удаляет все символы двоеточия из строки.
4.  Приводит все символы в строке к нижнему регистру.
5.  Удаляет символы подчеркивания с начала и конца строки.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

parser = GoogleHtmlParser(html_str='')  #  Создаем экземпляр класса, html_str не важен для этого метода

# Пример нормализации строки
text = "Пример строки: Для нормализации"
normalized_text = parser._normalize_dict_key(text)
print(normalized_text)  # Вывод: "пример_строки_для_нормализации"

# Пример нормализации строки с пробелами в начале и конце
text_with_spaces = "  Строка с пробелами в начале и конце  "
normalized_text_with_spaces = parser._normalize_dict_key(text_with_spaces)
print(normalized_text_with_spaces)  # Вывод: "строка_с_пробелами_в_начале_и_конце"

# Пример нормализации пустой строки
empty_text = ""
normalized_empty_text = parser._normalize_dict_key(empty_text)
print(normalized_empty_text)  # Вывод: ""
```

### `_get_estimated_results`

```python
def _get_estimated_results(self) -> int:
    """Получение количества результатов поиска.

    Возвращает количество найденных результатов для десктопной версии Google Search.

    Returns:
        int: Число результатов поиска.
    """
    ...
```

**Описание**: Извлекает количество оценочных результатов поиска со страницы результатов поиска Google (только для desktop версии).

**Возвращает**:
- `int`: Количество найденных результатов поиска в виде целого числа. Возвращает 0, если информация о количестве результатов не найдена.

**Как работает функция**:

1.  Инициализирует переменную `estimated_results` значением 0.
2.  Выполняет XPath-запрос к дереву HTML (`self.tree`) для поиска элемента, содержащего текст с информацией о количестве результатов поиска (например, "About 1,230,000 results").
3.  Проверяет, был ли найден элемент.
4.  Если элемент найден, извлекает текст из элемента, разделяет его на слова, берет второе слово (которое является числом результатов), удаляет символы запятой и преобразует строку в целое число.
5.  Возвращает полученное целое число `estimated_results`.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример HTML-кода с информацией о количестве результатов
html_content = """
<html>
<body>
    <div id="result-stats">About 1,230,000 results (0.35 seconds) </div>
</body>
</html>
"""

parser = GoogleHtmlParser(html_content)
estimated_results = parser._get_estimated_results()
print(estimated_results)  # Вывод: 1230000

# Пример HTML-кода без информации о количестве результатов
html_content_no_results = """
<html>
<body>
    <div>Some other content</div>
</body>
</html>
"""

parser_no_results = GoogleHtmlParser(html_content_no_results)
estimated_results_no_results = parser_no_results._get_estimated_results()
print(estimated_results_no_results)  # Вывод: 0
```

### `_get_organic`

```python
def _get_organic(self) -> list:
    """Получение органических результатов поиска.

    Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

    Returns:
        list: Список словарей с органическими результатами.
    """
    ...
```

**Описание**: Извлекает органические результаты поиска из HTML-кода страницы поисковой выдачи Google.

**Возвращает**:

- `list`: Список словарей, где каждый словарь представляет один органический результат поиска. Каждый словарь содержит следующие ключи:
  - `'url'` (str): URL найденного сайта.
  - `'title'` (str): Заголовок результата поиска.
  - `'snippet'` (str): Текстовый сниппет результата поиска.
  - `'rich_snippet'` (str): Расширенный сниппет (если есть).

**Как работает функция**:

1.  Инициализирует пустой список `organic` для хранения результатов.
2.  Выполняет XPath-запрос для поиска всех элементов `div` с классом `"g"`, которые содержат отдельные результаты поиска.
3.  Для каждого найденного элемента:
    - Извлекает сниппет (фрагмент текста) результата поиска.
    - Извлекает URL, заголовок и, если есть, расширенный сниппет.
    - Создает словарь с извлеченными данными и добавляет его в список `organic`.
4.  Возвращает список `organic`.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример HTML-кода с органическими результатами
html_content = """
<html>
<body>
    <div class="g">
        <div>
            <div>
                <div>
                    <div>Текстовый сниппет</div>
                </div>
            </div>
        </div>
        <a href="https://www.example.com">
            <h3>Заголовок результата</h3>
        </a>
    </div>
    <div class="g">
        <div>
            <div>
                <div>
                    <div>Текстовый сниппет 2</div>
                </div>
            </div>
        </div>
        <a href="https://www.example2.com">
            <h3>Заголовок результата 2</h3>
        </a>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_content)
organic_results = parser._get_organic()
print(organic_results)
# Вывод:
# [
#     {'url': 'https://www.example.com', 'title': 'Заголовок результата', 'snippet': 'Текстовый сниппет', 'rich_snippet': ''},
#     {'url': 'https://www.example2.com', 'title': 'Заголовок результата 2', 'snippet': 'Текстовый сниппет 2', 'rich_snippet': ''}
# ]

# Пример HTML-кода без органических результатов
html_content_no_results = """
<html>
<body>
    <div>Нет результатов</div>
</body>
</html>
"""
parser_no_results = GoogleHtmlParser(html_content_no_results)
organic_results_no_results = parser_no_results._get_organic()
print(organic_results_no_results)  # Вывод: []
```

### `_get_featured_snippet`

```python
def _get_featured_snippet(self) -> dict | None:
    """Получение featured snippet.

    Если существует, возвращает featured snippet с заголовком и URL.

    Returns:
        dict | None: Словарь с заголовком и URL или None.
    """
    ...
```

**Описание**: Извлекает featured snippet (избранный сниппет) из HTML-кода страницы поисковой выдачи Google.

**Возвращает**:

- `dict | None`: Словарь, содержащий заголовок и URL featured snippet, если он найден. В противном случае возвращает `None`.
  - `'title'` (str): Заголовок featured snippet.
  - `'url'` (str): URL, связанный с featured snippet.

**Как работает функция**:

1.  Инициализирует переменную `fs` значением `None`.
2.  Выполняет XPath-запрос для поиска элемента `div`, содержащего класс `"kp-blk"`.
3.  Если элемент найден:
    - Извлекает заголовок и URL featured snippet из элемента.
    - Если заголовок и URL существуют, создает словарь `fs` с этими данными.
4.  Возвращает словарь `fs` или `None`, если featured snippet не найден.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример HTML-кода с featured snippet
html_content = """
<html>
<body>
    <div class="kp-blk">
        <h3>Заголовок featured snippet</h3>
        <a href="https://www.example.com">Ссылка</a>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_content)
featured_snippet = parser._get_featured_snippet()
print(featured_snippet)
# Вывод: {'title': 'Заголовок featured snippet', 'url': 'https://www.example.com'}

# Пример HTML-кода без featured snippet
html_content_no_snippet = """
<html>
<body>
    <div>Нет featured snippet</div>
</body>
</html>
"""
parser_no_snippet = GoogleHtmlParser(html_content_no_snippet)
featured_snippet_no_snippet = parser_no_snippet._get_featured_snippet()
print(featured_snippet_no_snippet)  # Вывод: None
```

### `_get_knowledge_card`

```python
def _get_knowledge_card(self) -> dict | None:
    """Получение карточки знаний.

    Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

    Returns:
        dict | None: Словарь с данными карточки знаний или None.
    """
    ...
```

**Описание**: Извлекает карточку знаний из HTML-кода страницы поисковой выдачи Google.

**Возвращает**:

- `dict | None`: Словарь, содержащий информацию о карточке знаний, если она найдена. В противном случае возвращает `None`.

  - `'title'` (str): Заголовок карточки знаний.
  - `'subtitle'` (str): Подзаголовок карточки знаний.
  - `'description'` (str): Описание карточки знаний.
  - `'more_info'` (list): Список словарей с дополнительной информацией о карточке знаний.

**Как работает функция**:

1.  Выполняет XPath-запрос для поиска элемента `div`, содержащего класс `"kp-wholepage"`, который представляет карточку знаний.
2.  Если карточка знаний найдена:
    - Извлекает заголовок, подзаголовок и описание карточки знаний.
    - Извлекает дополнительную информацию из элементов, содержащих атрибут `data-attrid` с префиксом `":/"`.
    - Создает словарь с извлеченными данными и возвращает его.
3.  Если карточка знаний не найдена, возвращает `None`.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример HTML-кода с карточкой знаний
html_content = """
<html>
<body>
    <div class="kp-wholepage">
        <h2><span>Заголовок карточки знаний</span></h2>
        <div data-attrid="subtitle">Подзаголовок карточки знаний</div>
        <div class="kno-rdesc"><span>Описание карточки знаний</span></div>
    </div>
</body>
</html>
"""
parser = GoogleHtmlParser(html_content)
knowledge_card = parser._get_knowledge_card()
print(knowledge_card)
# Вывод:
# {
#     'title': 'Заголовок карточки знаний',
#     'subtitle': 'Подзаголовок карточки знаний',
#     'description': 'Описание карточки знаний',
#     'more_info': []
# }

# Пример HTML-кода без карточки знаний
html_content_no_card = """
<html>
<body>
    <div>Нет карточки знаний</div>
</body>
</html>
"""
parser_no_card = GoogleHtmlParser(html_content_no_card)
knowledge_card_no_card = parser_no_card._get_knowledge_card()
print(knowledge_card_no_card)  # Вывод: None
```

### `_get_scrolling_sections`

```python
def _get_scrolling_sections(self) -> list:
    """Получение данных из скроллируемых виджетов.

    Возвращает список данных из виджетов, например, топовые истории или твиты.

    Returns:
        list: Список словарей с данными из виджетов.
    """
    ...
```

**Описание**: Извлекает данные из скроллируемых виджетов на странице поисковой выдачи Google, таких как "Главные новости" или "Твиты".

**Возвращает**:

- `list`: Список словарей, где каждый словарь представляет собой раздел виджета со своим заголовком и данными.

  - `'section_title'` (str): Заголовок раздела виджета.
  - `'section_data'` (list): Список словарей с данными для каждого элемента в разделе.

    - `'title'` (str): Заголовок элемента в разделе.
    - `'url'` (str): URL, связанный с элементом.

**Как работает функция**:

1.  Выполняет XPath-запрос для поиска всех элементов `<g-section-with-header>`, которые представляют разделы с заголовками.
2.  Для каждого найденного раздела:
    - Извлекает заголовок раздела.
    - Выполняет XPath-запрос для поиска элементов `<g-inner-card>`, которые представляют отдельные элементы данных в разделе.
    - Для каждого элемента данных извлекает заголовок и URL.
    - Создает словарь для элемента данных и добавляет его в список `section_data`.
    - Создает словарь для раздела, содержащий заголовок раздела и список данных, и добавляет его в список `data`.
3.  Возвращает список `data`, содержащий информацию о всех найденных разделах и их элементах.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример HTML-кода с скроллируемыми секциями
html_content = """
<html>
<body>
    <g-section-with-header>
        <h3>Заголовок секции</h3>
        <g-inner-card>
            <div role="heading">Заголовок данных</div>
            <a href="https://www.example.com">Ссылка</a>
        </g-inner-card>
    </g-section-with-header>
</body>
</html>
"""
parser = GoogleHtmlParser(html_content)
scrolling_sections = parser._get_scrolling_sections()
print(scrolling_sections)
# Вывод:
# [
#     {
#         'section_title': 'Заголовок секции',
#         'section_data': [{'title': 'Заголовок данных', 'url': 'https://www.example.com'}]
#     }
# ]

# Пример HTML-кода без скроллируемых секций
html_content_no_sections = """
<html>
<body>
    <div>Нет скроллируемых секций</div>
</body>
</html>
"""
parser_no_sections = GoogleHtmlParser(html_content_no_sections)
scrolling_sections_no_sections = parser_no_sections._get_scrolling_sections()
print(scrolling_sections_no_sections)  # Вывод: []
```

### `get_data`

```python
def get_data(self) -> dict:
    """Получение итоговых данных с поисковой страницы.

    Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

    Returns:
        dict: Словарь с данными поисковой страницы.
    """
    ...
```

**Описание**: Извлекает и собирает все доступные данные со страницы результатов поиска Google (SERP).

**Возвращает**:

- `dict`: Словарь, содержащий различные типы данных, извлеченные из SERP.

  - `'estimated_results'` (int): Оценочное количество результатов поиска.
  - `'featured_snippet'` (dict | None): Избранный сниппет (если есть).
  - `'knowledge_card'` (dict | None): Карточка знаний (если есть).
  - `'organic_results'` (list): Список органических результатов поиска.
  - `'scrolling_widgets'` (list): Данные из скроллируемых виджетов (например, "Топ новости").

**Как работает функция**:

1.  Создает пустой словарь `data`.
2.  Проверяет значение атрибута `self.user_agent`. Если `self.user_agent` равен `'desktop'`:
    - Вызывает методы для извлечения различных типов данных (количество результатов, избранный сниппет, карточка знаний, органические результаты, скроллируемые виджеты).
    - Добавляет полученные данные в словарь `data` под соответствующими ключами.
3.  Возвращает словарь `data`.

**Примеры**:

```python
from src.goog.google_search import GoogleHtmlParser

# Пример HTML-кода с различными элементами
html_content = """
<html>
<body>
    <div id="result-stats">About 1,230,000 results (0.35 seconds) </div>
    <div class="kp-blk">
        <h3>Заголовок featured snippet</h3>
        <a href="https://www.example.com">Ссылка</a>
    </div>
    <div class="kp-wholepage">
        <h2><span>Заголовок карточки знаний</span></h2>
        <div data-attrid="subtitle">Подзаголовок карточки знаний</div>
        <div class="kno-rdesc"><span>Описание карточки знаний</span></div>
    </div>
    <div class="g">
        <div>
            <div>
                <div>
                    <div>Текстовый сниппет</div>
                </div>
            </div>
        </div>
        <a href="https://www.example.com">
            <h3>Заголовок результата</h3>
        </a>
    </div>
    <g-section-with-header>
        <h3>Заголовок секции</h3>
        <g-inner-card>
            <div role="heading">Заголовок данных</div>
            <a href="https://www.example.com">Ссылка</a>
        </g-inner-card>
    </g-section-with-header>
</body>
</html>
"""
parser = GoogleHtmlParser(html_content)
data = parser.get_data()
print(data)
# Вывод (может отличаться в зависимости от полноты HTML-кода):
# {
#     'estimated_results': 1230000,
#     'featured_snippet': {'title': 'Заголовок featured snippet', 'url': 'https://www.example.com'},
#     'knowledge_card': {
#         'title': 'Заголовок карточки знаний',
#         'subtitle': 'Подзаголовок карточки знаний',
#         'description': 'Описание карточки знаний',
#         'more_info': []
#     },
#     'organic_results': [
#         {'url': 'https://www.example.com', 'title': 'Заголовок результата', 'snippet': 'Текстовый сниппет', 'rich_snippet': ''}
#     ],
#     'scrolling_widgets': [
#         {
#             'section_title': 'Заголовок секции',
#             'section_data': [{'title': 'Заголовок данных', 'url': 'https://www.example.com'}]
#         }
#     ]
# }

# Пример с пустым HTML-кодом
html_content_empty = """
<html>
<body>
</body>
</html>
"""
parser_empty = GoogleHtmlParser(html_content_empty)
data_empty = parser_empty.get_data()
print(data_empty)
# Вывод:
# {
#     'estimated_results': 0,
#     'featured_snippet': None,
#     'knowledge_card': None,
#     'organic_results': [],
#     'scrolling_widgets': []
# }