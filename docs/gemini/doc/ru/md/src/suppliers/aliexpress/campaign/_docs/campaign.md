# Модуль `campaign` для AliExpress

## Обзор

Модуль `campaign` предназначен для управления и редактирования рекламных кампаний AliExpress, взаимодействия с Google Таблицами для обработки данных и подготовки данных кампаний для использования.  Он предоставляет функции для инициализации кампаний, извлечения данных о продуктах и категориях, а также подготовки данных для дальнейшей обработки.


## Алгоритм работы

1. **Инициализация**: Модуль `campaign` инициализируется через конструктор класса `AliPromoCampaign`, принимающий имя кампании, категорию, язык, валюту и флаг принудительной перезагрузки данных.

2. **Обработка кампаний**:
   - Внутри конструктора происходит получение пути к файлам кампаний в Google Диске.
   - Вызывается метод `initialize_campaign()`, который загружает данные из JSON файлов и создает экземпляры `SimpleNamespace` для хранения данных кампании и категории.
   - Метод `get_category_products()` извлекает данные о продуктах из Google Таблиц (или JSON файлов), если необходимо (при `force_update=True`).
   - Метод `prepare_products()` подготавливает данные для дальнейшей обработки, читая данные из `sources.txt` и `sources.csv`.

3. **Взаимодействие с Google Таблицами**:
   - Модуль использует библиотеку `gspread` для работы с Google Таблицами (или аналогичными источниками данных).
   - Конфигурация доступа к Google Таблицам хранится в настройках проекта (`src.settings.gs`).

4. **Поддержка типов данных**:
   - Используются типы данных из `typing` для явной типизации и повышения качества кода.

5. **Обработка исключений**:
   - Используется `ex` вместо `e` в блоках обработки исключений, чтобы избежать конфликтов с именованными переменными.

## Классы

### `AliPromoCampaign`

**Описание**: Основной класс модуля, представляющий рекламную кампанию AliExpress.

**Атрибуты**:
- `campaign_name` (str): Название кампании.
- `category_name` (str): Название категории.
- `language` (str): Язык.
- `currency` (str): Валюта.
- `force_update` (bool): Флаг принудительной перезагрузки данных.
- `campaign_root` (Path): Путь к корневой директории кампании.
- `campaign` (SimpleNamespace): Экземпляр `SimpleNamespace` содержащий данные кампании.
- `category` (SimpleNamespace): Экземпляр `SimpleNamespace` содержащий данные категории.
- `title` (str): Заголовок кампании.


**Методы**:
- `__init__(campaign_name, category_name, language, currency, force_update)`: Инициализирует объект `AliPromoCampaign`.
- `initialize_campaign()`: Инициализирует атрибуты `campaign` и `category` объекта.
- `get_category_from_campaign()`: Возвращает объект категории из данных кампании.
- `get_category_products(force_update=False)`: Возвращает список продуктов для данной категории.
- `create_product_namespace(**kwargs)`: Создает объект `SimpleNamespace` для продукта.
- `create_campaign_namespace(**kwargs)`: Создает объект `SimpleNamespace` для кампании.
- `prepare_products()`: Подготавливает данные о продуктах для дальнейшего использования.


## Функции

### `get_filenames(category_path, extension='.json')`

**Описание**: Возвращает список путей к файлам в заданной директории с указанным расширением.

**Параметры**:
- `category_path` (Path): Путь к директории.
- `extension` (str): Расширение файлов.

**Возвращает**:
- `List[Path]`: Список путей к файлам.


### `j_loads_ns(file_path)`

**Описание**: Загружает данные из JSON файла и возвращает объект `SimpleNamespace`.

**Параметры**:
- `file_path` (Path): Путь к файлу.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с загруженными данными.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `json.JSONDecodeError`: Если файл содержит невалидный JSON.


### `csv2dict(file_path)`

**Описание**: Преобразует данные из CSV файла в словарь.

**Параметры**:
- `file_path` (Path): Путь к CSV файлу.

**Возвращает**:
- `dict`: Словарь с данными из CSV файла.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `csv.Error`: Если данные в файле имеют неверный формат CSV.


### `extract_prod_ids(prod_ids)`

**Описание**: Извлекает идентификаторы продуктов из входного списка.

**Параметры**:
- `prod_ids` (List): Список идентификаторов.

**Возвращает**:
- `List`: Список извлечённых идентификаторов.

### `process_affiliate_products(prod_ids)`

**Описание**: Обрабатывает список идентификаторов продуктов.

**Параметры**:
- `prod_ids` (List): Список идентификаторов продуктов.

**Возвращает**:
- `List`: Обработанный список идентификаторов.


## Примеры использования

```python
# Пример использования AliPromoCampaign
campaign = AliPromoCampaign("SummerSale", "Electronics", "EN", "USD", force_update=True)
campaign.prepare_products()
```

```python
# Пример использования get_filenames
filenames = get_filenames(Path("./category_data"))
```


## Модули зависимостей

- `typing`
- `pathlib`
- `json`
- `csv`
- `gspread` (или аналогичные библиотеки)
- `pandas` (при необходимости)
- `SimpleNamespace` (from `types`)
- `src.settings.gs`
- `src.utils`
- `src.utils.convertors`
- `src.utils.file`
- `src.logger`
- `src.suppliers.aliexpress.affiliated_products_generator`
- `src.suppliers.aliexpress.utils.extract_product_id`
- `src.suppliers.aliexpress.utils.set_full_https`