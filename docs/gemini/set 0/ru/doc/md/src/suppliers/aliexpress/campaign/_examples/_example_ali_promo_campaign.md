# Модуль hypotez/src/suppliers/aliexpress/campaign/_examples/_example_ali_promo_campaign.py

## Обзор

Этот модуль содержит примеры создания рекламной кампании на AliExpress. Он демонстрирует использование классов `AliPromoCampaign` и `AliAffiliatedProducts` для работы с кампаниями и связанными продуктами. Модуль также использует вспомогательные функции из модуля `src.utils` для работы с файлами и данными.

## Переменные

### `MODE`

**Описание**:  Переменная, хранящая режим работы (например, 'dev').

**Тип**: str

## Функции

### `get_filenames`

**Описание**: Возвращает список имен файлов в указанной директории.


**Параметры**:
- `path` (Path): Путь к директории.

**Возвращает**:
- list[str]: Список имен файлов.


### `get_directory_names`

**Описание**: Возвращает список имен поддиректорий в указанной директории.


**Параметры**:
- `path` (Path): Путь к директории.

**Возвращает**:
- list[str]: Список имен поддиректорий.


### `read_text_file`

**Описание**: Читает содержимое текстового файла.


**Параметры**:
- `file_path` (Path): Путь к файлу.

**Возвращает**:
- str: Содержимое файла.


### `csv2dict`

**Описание**: Преобразует данные из CSV-файла в список словарей.


**Параметры**:
- `file_path` (Path): Путь к CSV-файлу.

**Возвращает**:
- list[dict]: Список словарей.


### `j_loads_ns`

**Описание**: Парсит JSON строку и возвращает объект SimpleNamespace.


**Параметры**:
- `json_str` (str): JSON строка.

**Возвращает**:
- SimpleNamespace: Объект SimpleNamespace.


### `pprint`

**Описание**: Выводит данные в удобочитаемом формате.


**Параметры**:
- `obj` (any): Объект для вывода.


### `AliPromoCampaign`

**Описание**: Класс для создания и работы с рекламными кампаниями.


**Конструктор**:
- `__init__(campaign_name, category_name, language=None, currency=None)`

**Параметры**:
  - `campaign_name` (str): Название рекламной кампании.
  - `category_name` (str): Название категории.
  - `language` (Optional[str], optional): Язык.
  - `currency` (Optional[str], optional): Валюта.



## Примеры

### Создание объекта AliPromoCampaign

```python
campaign_name = '280624_cleararanse'
category_name = 'gaming_comuter_accessories'
language = 'EN'
currency = 'USD'

a = AliPromoCampaign(campaign_name=campaign_name,
                     category_name=category_name,
                     language=language,
                     currency=currency)

campaign = a.campaign
category = a.category
products = a.category.products
```

```python
a = AliPromoCampaign(campaign_name, category_name, {'EN': 'USD'})
```

```python
a = AliPromoCampaign(campaign_name, category_name, 'EN', 'USD')
```

Эти примеры демонстрируют создание экземпляров класса `AliPromoCampaign` с различными типами аргументов. Обратите внимание на использование ключевых слов при передаче параметров.


```python
```
```python

```
```python