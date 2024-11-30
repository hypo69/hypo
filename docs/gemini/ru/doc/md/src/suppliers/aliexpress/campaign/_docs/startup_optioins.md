# Модуль `prepare_campaigns`

## Обзор

Этот модуль предназначен для подготовки данных рекламных кампаний на AliExpress. Он включает в себя функции для инициализации, создания каталогов, сохранения настроек кампании, сбора данных о продуктах, сохранения данных о продуктах, создания рекламных материалов, проверки готовности кампании и публикации кампании. Модуль использует библиотеки `asyncio`, `pathlib`, `typing` и `argparse` для управления данными и потоками.

## Оглавление

* [Функции](#функции)
    * [`update_category`](#update_category)
    * [`process_campaign_category`](#process-campaign-category)
    * [`process_campaign`](#process-campaign)
    * [`main`](#main)

## Функции

### `update_category`

**Описание**: Обновляет категорию в JSON файле.

**Параметры**:
- `json_path` (Path): Путь к файлу JSON.
- `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий данные категории.

**Возвращает**:
- bool: `True`, если обновление прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Возникает при возникновении ошибки при чтении/записи JSON файла или других операциях.


### `process_campaign_category`

**Описание**: Обрабатывает определенную категорию в кампании для всех языков и валют.

**Параметры**:
- `campaign_name` (str): Имя рекламной кампании.
- `category_name` (str): Имя категории для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.
- `force` (bool, optional): Принудительно обновить категорию. По умолчанию `False`.

**Возвращает**:
- Optional[bool]: `True`, если обработка прошла успешно, `False` в противном случае.


### `process_campaign`

**Описание**: Обрабатывает всю кампанию для всех категорий.

**Параметры**:
- `campaign_name` (str): Имя рекламной кампании.
- `categories` (List[str] | None, optional): Список категорий для кампании. По умолчанию `None`.
- `language` (str, optional): Язык для кампании (по умолчанию 'EN').
- `currency` (str, optional): Валюта для кампании (по умолчанию 'USD').
- `force` (bool, optional): Принудительно обновить категории. По умолчанию `False`.

**Возвращает**:
- None: Функция не возвращает значение.  Возвращает список кортежей (`(category, result)`), где `category` - имя категории, а `result` - результат обработки.

**Вызывает исключения**:
- `Exception`: Возникает при возникновении ошибок во время обработки категорий.


### `main`

**Описание**: Асинхронная основная функция для обработки кампании.

**Параметры**:
- `campaign_name` (str): Имя рекламной кампании.
- `categories` (List[str]): Список категорий для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.
- `force` (bool, optional): Принудительно обновить категории. По умолчанию `False`.

**Возвращает**:
- None: Функция не возвращает значение.


## Пример использования

```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD -f
```

Этот пример запускает подготовку кампании "summer_sale" с категорией "electronics", языком "EN" и валютой "USD", принудительно обновляя категории.


```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics fashion -l EN -cu USD -f
```

Этот пример обрабатывает кампанию "summer_sale" с категориями "electronics" и "fashion".