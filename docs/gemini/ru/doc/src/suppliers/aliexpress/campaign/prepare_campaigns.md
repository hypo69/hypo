# Модуль `hypotez/src/suppliers/aliexpress/campaign/prepare_campaigns.py`

## Обзор

Модуль `prepare_campaigns.py` отвечает за подготовку рекламных кампаний AliExpress. Он обрабатывает категории, данные кампаний, и генерирует рекламные материалы.  Модуль использует данные из директории `campaigns`, хранящейся в Google Drive.

## Функции

### `process_campaign_category`

**Описание**: Обрабатывает определенную категорию в рамках кампании для заданного языка и валюты. Возвращает список заголовков продуктов для указанной категории.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Возвращает**:
- `List[str]`: Список названий продуктов в категории.

**Пример**:
```python
>>> titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
>>> print(titles)
['Product 1', 'Product 2']
```

### `process_campaign`

**Описание**: Обрабатывает кампанию, включая настройку и выполнение необходимых операций.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str], optional): Язык кампании. Если не указан, обрабатывается для всех языков. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта кампании. Если не указан, обрабатывается для всех валют. По умолчанию `None`.
- `campaign_file` (Optional[str], optional): Путь к файлу с кампанией (опционально). По умолчанию `None`.

**Возвращает**:
- `bool`: `True` если кампания обработана, иначе `False`.

**Пример**:
```python
>>> res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
```


### `process_all_campaigns`

**Описание**: Обрабатывает все кампании в директории `campaigns` для заданного языка и валюты.

**Параметры**:
- `language` (Optional[str], optional): Язык кампании. Если не указан, обрабатывается для всех языков. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта кампании. Если не указан, обрабатывается для всех валют. По умолчанию `None`.

**Пример**:
```python
>>> process_all_campaigns("EN", "USD")
```

### `main_process`

**Описание**: Главный метод для обработки одной кампании.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `categories` (List[str] | str): Список категорий для кампании. Если пуст, обрабатываются все категории.
- `language` (Optional[str], optional): Язык кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта кампании. По умолчанию `None`.

**Пример**:
```python
>>> main_process("summer_sale", ["electronics"], "EN", "USD")
>>> main_process("summer_sale", [], "EN", "USD")
```

### `main`

**Описание**: Главный метод для обработки аргументов командной строки и запуска процесса.

**Пример**:
```python
>>> main()
```

## Постоянные переменные

- `MODE`: Строка, хранящая режим работы (`dev`).
- `campaigns_directory`: Путь к директории с кампаниями в Google Drive.

## Использование

Модуль используется через интерпретатор Python, принимая аргументы командной строки.  Примеры запуска:

- Для обработки конкретной кампании:
  ```bash
  python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
  ```
- Для обработки всех кампаний:
  ```bash
  python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD
  ```

## Зависимости

- `header`
- `argparse`
- `copy`
- `pathlib`
- `typing`
- `gs`
- `AliCampaignEditor`
- `locales`
- `pprint`
- `get_directory_names`
- `j_loads_ns`
- `logger`