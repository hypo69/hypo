```markdown
# Модуль google_search

## Обзор

Данный модуль предоставляет класс `GoogleHtmlParser` для парсинга HTML страниц результатов поиска Google.  Он обрабатывает как мобильную, так и десктопную версии страниц, извлекая органические результаты, featured snippets, карточки знаний и данные из скроллируемых виджетов.

## Оглавление

- [GoogleHtmlParser](#googlehtmlparser)
    - [__init__](#init)
    - [_clean](#clean)
    - [_normalize_dict_key](#normalize_dict_key)
    - [_get_estimated_results](#get_estimated_results)
    - [_get_organic](#get_organic)
    - [_get_featured_snippet](#get_featured_snippet)
    - [_get_knowledge_card](#get_knowledge_card)
    - [_get_scrolling_sections](#get_scrolling_sections)
    - [get_data](#get_data)


## Классы

### `GoogleHtmlParser`

**Описание**: Класс для парсинга HTML страниц результатов поиска Google.

**Атрибуты**:

- `tree` (html.Element): Дерево документа, полученное через `html.fromstring()`.
- `user_agent` (str): User agent, использованный для получения HTML Google Search.

**Методы**:

#### `__init__`

**Описание**: Инициализация парсера.

**Параметры**:

- `html_str` (str): HTML Google Search в виде строки.
- `user_agent` (str, optional): User agent для получения HTML. Может быть 'mobile' или 'desktop'. По умолчанию 'desktop'.

**Возвращает**:
- `None`

#### `_clean`

**Описание**: Очистка строки от лишних символов.

**Параметры**:

- `content` (str): Строка для очистки.

**Возвращает**:

- `str`: Очищенная строка.


#### `_normalize_dict_key`

**Описание**: Нормализация строки для использования в качестве ключа словаря.

**Параметры**:

- `content` (str): Строка для нормализации.

**Возвращает**:

- `str`: Нормализованная строка.


#### `_get_estimated_results`

**Описание**: Получение количества результатов поиска.

**Возвращает**:

- `int`: Число результатов поиска.


#### `_get_organic`

**Описание**: Получение органических результатов поиска.

**Возвращает**:

- `list`: Список словарей с органическими результатами.


#### `_get_featured_snippet`

**Описание**: Получение featured snippet.

**Возвращает**:

- `dict | None`: Словарь с заголовком и URL или `None`.


#### `_get_knowledge_card`

**Описание**: Получение карточки знаний.

**Возвращает**:

- `dict | None`: Словарь с данными карточки знаний или `None`.


#### `_get_scrolling_sections`

**Описание**: Получение данных из скроллируемых виджетов.

**Возвращает**:

- `list`: Список словарей с данными из виджетов.


#### `get_data`

**Описание**: Получение итоговых данных с поисковой страницы.

**Возвращает**:

- `dict`: Словарь с данными поисковой страницы.
```
