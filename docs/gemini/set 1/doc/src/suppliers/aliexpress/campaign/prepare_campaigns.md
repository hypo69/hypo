# Модуль `hypotez/src/suppliers/aliexpress/campaign/prepare_campaigns.py`

## Обзор

Этот модуль предназначен для подготовки рекламных кампаний AliExpress. Он обрабатывает категории, данные кампаний и генерирует рекламные материалы. Модуль предоставляет функции для обработки одной кампании, всех кампаний в директории и отдельных категорий внутри кампании, поддерживая различные языки и валюты.

## Функции

### `process_campaign_category`

**Описание**: Обрабатывает определенную категорию внутри кампании для заданного языка и валюты.

**Параметры**:

- `campaign_name` (str): Имя рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:

- `List[str]`: Список названий продуктов в категории.

**Пример**:

```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)  # Вывод: ['Product 1', 'Product 2']
```


### `process_campaign`

**Описание**: Обрабатывает кампанию и отвечает за настройку и обработку кампании.

**Параметры**:

- `campaign_name` (str): Имя рекламной кампании.
- `language` (Optional[str], optional): Язык для кампании. Если не указан, обрабатывается для всех языков.
- `currency` (Optional[str], optional): Валюта для кампании. Если не указан, обрабатывается для всех валют.
- `campaign_file` (Optional[str], optional): Опциональный путь к файлу конкретной кампании.


**Возвращает**:

- bool: `True`, если кампания обработана успешно, иначе `False`.


**Пример**:

```python
res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
```



### `process_all_campaigns`

**Описание**: Обрабатывает все кампании в директории `campaigns` для указанного языка и валюты.

**Параметры**:

- `language` (Optional[str]): Язык для кампаний.
- `currency` (Optional[str]): Валюта для кампаний.

**Пример**:

```python
process_all_campaigns("EN", "USD")
```


### `main_process`

**Описание**: Главная функция для обработки кампании.

**Параметры**:

- `campaign_name` (str): Имя рекламной кампании.
- `categories` (List[str]): Список категорий для кампании. Если пустой, обрабатывается вся кампания без конкретных категорий.
- `language` (Optional[str]): Язык для кампании.
- `currency` (Optional[str]): Валюта для кампании.

**Пример**:

```python
main_process("summer_sale", ["electronics"], "EN", "USD")
main_process("summer_sale", [], "EN", "USD")
```


### `main`

**Описание**: Главная функция для парсинга аргументов и запуска обработки.

**Пример**:

```python
main()
```

## Аргументы командной строки

Модуль принимает следующие аргументы командной строки:

- `campaign_name`: Имя кампании.
- `-c`, `--categories`: Список категорий (если не указан, будут использованы все категории).
- `-l`, `--language`: Язык для кампании.
- `-cu`, `--currency`: Валюта для кампании.
- `--all`: Обработать все кампании.


## Использование

Для запуска скрипта для конкретной кампании:

```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
```

Для обработки всех кампаний:

```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD
```


##  Примечания

- Путь к директории с кампаниями задан в переменной `campaigns_directory`.
- Модуль использует библиотеки `argparse`, `copy`, `pathlib`, `typing`, `gs`, `AliCampaignEditor`, `locales`, `pprint`, `get_directory_names`, `j_loads_ns`, `logger`.
- Обработка выполняется для каждой пары язык/валюта из списка `locales`.
-  Флаг `--all` обрабатывает все кампании в указанной директории.