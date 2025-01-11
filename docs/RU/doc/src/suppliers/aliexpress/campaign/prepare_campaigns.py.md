# Модуль `prepare_campaigns.py`

## Обзор

Модуль `prepare_campaigns.py` предназначен для подготовки рекламных кампаний AliExpress. Он обрабатывает категории товаров, управляет данными кампаний и генерирует рекламные материалы.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [process_campaign_category](#process_campaign_category)
    - [process_campaign](#process_campaign)
    - [process_all_campaigns](#process_all_campaigns)
    - [main_process](#main_process)
    - [main](#main)
- [Примеры](#примеры)

## Функции

### `process_campaign_category`

**Описание**: Обрабатывает конкретную категорию в рамках кампании для заданного языка и валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для обработки.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список заголовков товаров в пределах категории.

**Пример**:
```python
>>> titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
>>> print(titles)
['Product 1', 'Product 2']
```
### `process_campaign`

**Описание**: Обрабатывает кампанию, включая настройку и обработку данных.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str], optional): Язык для кампании. Если не указан, обрабатываются все локали. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампании. Если не указана, обрабатываются все локали. По умолчанию `None`.
- `campaign_file` (Optional[str], optional): Путь к файлу конкретной кампании. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если кампания обработана успешно, иначе `False`.

**Пример**:
```python
>>> res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
```

### `process_all_campaigns`

**Описание**: Обрабатывает все кампании в директории `campaigns` для указанных языка и валюты.

**Параметры**:
- `language` (Optional[str], optional): Язык для кампаний. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампаний. По умолчанию `None`.

**Пример**:
```python
>>> process_all_campaigns("EN", "USD")
```

### `main_process`

**Описание**: Главная функция для обработки кампании. Она может обрабатывать либо отдельные категории, либо всю кампанию целиком.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `categories` (List[str] | str): Список категорий для обработки. Если пуст, обрабатывается вся кампания.
- `language` (Optional[str], optional): Язык для кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта для кампании. По умолчанию `None`.

**Примеры**:
```python
>>> main_process("summer_sale", ["electronics"], "EN", "USD")
>>> main_process("summer_sale", [], "EN", "USD")
```

### `main`

**Описание**: Главная функция для разбора аргументов командной строки и запуска обработки.

**Пример**:
```python
>>> main()
```

## Примеры

Для запуска скрипта для конкретной кампании:
```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
```

Для обработки всех кампаний:
```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD
```