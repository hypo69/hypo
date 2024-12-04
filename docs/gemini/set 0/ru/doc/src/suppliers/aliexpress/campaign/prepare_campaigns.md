# Модуль `hypotez/src/suppliers/aliexpress/campaign/prepare_campaigns.py`

## Обзор

Этот модуль отвечает за подготовку кампаний AliExpress. Он обрабатывает категории, данные о кампаниях и генерирует рекламные материалы.  Модуль использует классы для обработки отдельных кампаний, поддерживает работу с различными языками и валютами. Поддерживает обработку отдельных кампаний и всех кампаний в директории.

## Оглавление

- [Функции](#функции)
    - [`process_campaign_category`](#process_campaign_category)
    - [`process_campaign`](#process_campaign)
    - [`process_all_campaigns`](#process_all_campaigns)
    - [`main_process`](#main_process)
    - [`main`](#main)


## Функции

### `process_campaign_category`

**Описание**: Обрабатывает определенную категорию в рамках кампании для заданного языка и валюты. Возвращает список названий продуктов в данной категории.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список названий продуктов в указанной категории.

**Пример**:
```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)  # Вывод: ['Product 1', 'Product 2']
```


### `process_campaign`

**Описание**: Обрабатывает кампанию, выполняя ее настройку и обработку. Обрабатывает одну кампанию для заданных языка и валюты (или для всех, если не указаны).

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str], optional): Язык для кампании. Если не указан, обрабатываются все доступные языки.
- `currency` (Optional[str], optional): Валюта для кампании. Если не указана, обрабатываются все доступные валюты.
- `campaign_file` (Optional[str], optional): Опциональный путь к файлу с данными о кампании.

**Возвращает**:
- `bool`: `True`, если кампания обработана успешно, иначе `False`.

**Пример**:

```python
res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
```


### `process_all_campaigns`

**Описание**: Обрабатывает все кампании в директории `campaigns` для указанного языка и валюты (или для всех, если не указаны).

**Параметры**:
- `language` (Optional[str], optional): Язык для кампаний. Если не указан, обрабатываются все доступные языки.
- `currency` (Optional[str], optional): Валюта для кампаний. Если не указана, обрабатываются все доступные валюты.

**Пример**:

```python
process_all_campaigns("EN", "USD")
```


### `main_process`

**Описание**: Основная функция для обработки одной кампании. Обрабатывает кампанию с учетом опциональных категорий и языка/валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `categories` (List[str]): Список категорий для кампании. Если пустой, обрабатывается вся кампания.
- `language` (Optional[str], optional): Язык для кампании.
- `currency` (Optional[str], optional): Валюта для кампании.


**Пример**:

```python
main_process("summer_sale", ["electronics"], "EN", "USD")
main_process("summer_sale", [], "EN", "USD")
```


### `main`

**Описание**: Основная функция, парсит аргументы командной строки и запускает обработку кампании или всех кампаний.

**Пример**:

```python
main()
```

## Примеры использования (из документации):

**Запуск для конкретной кампании:**

```
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
```

**Обработка всех кампаний:**

```
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD
```


```