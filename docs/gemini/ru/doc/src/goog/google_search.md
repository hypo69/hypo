# Модуль `hypotez/src/goog/google_search.py`

## Обзор

Этот модуль содержит класс `GoogleHtmlParser` для парсинга HTML-страниц поисковой выдачи Google. Он позволяет извлечь органические результаты, featured snippet, карточку знаний и данные из скроллируемых виджетов. Класс обрабатывает как мобильную, так и десктопную версии HTML.

## Оглавление

* [GoogleHtmlParser](#googlehtmlparser)
    * [__init__](#init)
    * [_clean](#_clean)
    * [_normalize_dict_key](#_normalize_dict_key)
    * [_get_estimated_results](#_get_estimated_results)
    * [_get_organic](#_get_organic)
    * [_get_featured_snippet](#_get_featured_snippet)
    * [_get_knowledge_card](#_get_knowledge_card)
    * [_get_scrolling_sections](#_get_scrolling_sections)
    * [get_data](#get_data)


## Классы

### `GoogleHtmlParser`

**Описание**: Класс для парсинга HTML-страниц поисковой выдачи Google.

**Атрибуты**:

- `tree` (html.Element): Дерево документа, полученное из HTML-строки.
- `user_agent` (str): User agent, использованный для получения HTML.

#### `__init__`

**Описание**: Инициализирует парсер.

**Параметры**:

- `html_str` (str): HTML Google Search в виде строки.
- `user_agent` (str, optional): User agent для получения HTML. Может быть 'mobile' или 'desktop'. По умолчанию 'desktop'.

**Возвращает**:
- `None`

#### `_clean`

**Описание**: Очищает строку от лишних символов.

**Параметры**:

- `content` (str): Строка для очистки.

**Возвращает**:
- `str`: Очищенная строка.


#### `_normalize_dict_key`

**Описание**: Нормализует строку для использования в качестве ключа словаря.

**Параметры**:

- `content` (str): Строка для нормализации.

**Возвращает**:
- `str`: Нормализованная строка.


#### `_get_estimated_results`

**Описание**: Получает количество результатов поиска.

**Возвращает**:
- `int`: Число результатов поиска.


#### `_get_organic`

**Описание**: Получает органические результаты поиска.

**Возвращает**:
- `list`: Список словарей с органическими результатами.


#### `_get_featured_snippet`

**Описание**: Получает featured snippet.

**Возвращает**:
- `dict | None`: Словарь с заголовком и URL или `None`, если featured snippet не найден.


#### `_get_knowledge_card`

**Описание**: Получает карточку знаний.

**Возвращает**:
- `dict | None`: Словарь с данными карточки знаний или `None`, если карточка не найдена.


#### `_get_scrolling_sections`

**Описание**: Получает данные из скроллируемых виджетов.

**Возвращает**:
- `list`: Список словарей с данными из виджетов.


#### `get_data`

**Описание**: Получает итоговые данные с поисковой страницы.

**Возвращает**:
- `dict`: Словарь с данными поисковой страницы.