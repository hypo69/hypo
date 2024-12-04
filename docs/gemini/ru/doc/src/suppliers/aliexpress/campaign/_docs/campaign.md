# Модуль `campaign` для управления рекламными кампаниями AliExpress

## Обзор

Модуль `campaign` предназначен для управления и редактирования рекламных кампаний в системе AliExpress. Он взаимодействует с Google Таблицами для получения и обработки данных, а также готовит данные кампаний к использованию.

## Алгоритм и рабочий процесс

Модуль `campaign` реализует следующий алгоритм:

1. **Инициализация**: Модуль инициализируется при помощи класса `AliPromoCampaign`.
2. **Загрузка данных**: Загружаются данные из Google Таблиц, используя `gs.path` и путь к файлам кампаний.
3. **Инициализация кампании**: Метод `initialize_campaign` создаёт объект `SimpleNamespace` для хранения данных кампании.
4. **Получение категорий**: Метод `get_category_from_campaign` извлекает информацию о категории кампании.
5. **Получение продуктов**: Метод `get_category_products` получает список продуктов для данной категории, используя JSON файлы или другой формат.
6. **Обработка продуктов**: Метод `prepare_products` обрабатывает данные о продуктах, подготавливая их к использованию.  Это может включать чтение из файлов, преобразование данных, и фильтрацию.
7. **Подготовка данных**: Метод `prepare_products` осуществляет подготовку данных для дальнейшей обработки и использования в других частях приложения.

## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламными кампаниями AliExpress.

**Методы**:

- `__init__(campaign_name, category_name, language, currency, force_update)`: Инициализирует объект `AliPromoCampaign`.
    - `campaign_name` (str): Название кампании.
    - `category_name` (str): Название категории.
    - `language` (str): Язык.
    - `currency` (str): Валюта.
    - `force_update` (bool, optional): Принудительно обновить данные. По умолчанию `False`.
- `initialize_campaign()`: Инициализирует данные кампании.
- `get_category_from_campaign()`: Получает данные о категории из кампании.
- `get_category_products(force_update)`: Получает продукты для данной категории.
    - `force_update` (bool): Принудительно обновить данные.


## Функции

### `create_campaign_namespace(**kwargs)`

**Описание**: Создаёт объект `SimpleNamespace` для данных кампании.

**Параметры**:
- `**kwargs`: Аргументы, которые будут использоваться для создания `SimpleNamespace`.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными кампании.


### `create_product_namespace(**kwargs)`

**Описание**: Создаёт объект `SimpleNamespace` для данных продукта.

**Параметры**:
- `**kwargs`: Аргументы, которые будут использоваться для создания `SimpleNamespace`.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными продукта.

## Подмодули и зависимост

- Модули: `gs`, `AliCampaignGoogleSheet`, `ali_campaign_editor`, `ali_promo_campaign`, `gsheet`, `header`, `prepare_campaigns`, `ttypes`, `version`
- Библиотеки: `gspread`, `pandas`, `re`, `shutil`, `pathlib`
- Файлы и папки: `_docs`, `_dot`, `_mermaid`, `_examples`, `_pytest`
- Утилиты: `j_loads_ns`, `j_loads`, `j_dumps`, `list2string`, `csv2dict`, `pprint`, `read_text_file`, `get_filenames`, `extract_prod_ids`, `ensure_https`, `logger`, `AliAffiliatedProducts`


## Примеры использования

### Обработка одной категории кампании
```python
process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)
```

### Обработка конкретной кампании
```python
process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)
```

### Обработка всех кампаний
```python
process_all_campaigns(language="EN", currency="USD", force=True)
```


## Замечания

Этот пример документации основан на предоставленном тексте.  Для более подробной и эффективной документации, необходимо дополнить её детальным описанием каждой функции и класса, включая примеры использования и обработки исключений (с использованием `ex`).