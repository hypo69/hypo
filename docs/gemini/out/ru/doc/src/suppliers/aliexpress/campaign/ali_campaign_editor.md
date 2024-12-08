# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py`

## Обзор

Модуль `ali_campaign_editor.py` предоставляет класс `AliCampaignEditor` для редактирования рекламных кампаний на AliExpress.  Класс наследуется от `AliPromoCampaign` и предоставляет методы для добавления, удаления, обновления продуктов и категорий, а также для получения списка категорий.  Модуль использует внешние библиотеки для работы с файлами, JSON, Google Sheets и т.д.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования данных рекламных кампаний на AliExpress.  Он позволяет добавлять, удалять, обновлять продукты и категории, а также получать информацию о категориях.

**Методы**:

- `__init__(campaign_name: str, language: Optional[str | dict] = None, currency: Optional[str] = None)`: Инициализирует объект `AliCampaignEditor`.
    * **Описание**:  Инициализирует класс с данными кампании.
    * **Параметры**:
        * `campaign_name` (str): Название кампании.
        * `language` (Optional[str | dict], optional): Язык кампании. По умолчанию `'EN'`.
        * `currency` (Optional[str], optional): Валюта кампании. По умолчанию `'USD'`.
        * `campaign_file` (Optional[str | Path], optional): Опционально загрузить `<lang>_<currency>.json` файл из корня кампании. По умолчанию `None`.
    * **Возвращает**:  None
    * **Исключения**:
        * `CriticalError`: Если не указаны ни `campaign_name`, ни `campaign_file`.

- `delete_product(product_id: str, exc_info: bool = False)`: Удаляет продукт, если у него нет аффилиатной ссылки.
    * **Описание**: Удаляет продукт из списка, если его ID совпадает с предоставленным. Если файла с товаром нет, переименовывает соответствующий файл.
    * **Параметры**:
        * `product_id` (str): ID продукта.
        * `exc_info` (bool, optional):  Включать ли информацию об исключении в логи. По умолчанию `False`.
    * **Возвращает**: None
    * **Исключения**:
        * `FileNotFoundError`: Если файл продукта не найден.
        * `Exception`: В случае любой другой ошибки.


- `update_product(category_name: str, lang: str, product: dict)`: Обновляет данные продукта в категории.
    * **Описание**: Обновляет данные продукта в указанной категории.
    * **Параметры**:
        * `category_name` (str): Название категории.
        * `lang` (str): Язык.
        * `product` (dict): Словарь с данными продукта.
    * **Возвращает**: None
    * **Исключения**:  Возможны исключения при работе с файловой системой или JSON.


- `update_campaign()`: Обновляет свойства кампании (описание, тэги и т.д.).
    * **Описание**: Обновляет свойства кампании.
    * **Параметры**:  Нет
    * **Возвращает**: None
    * **Исключения**: Возможны исключения, связанные с обновлением данных.


- `update_category(json_path: Path, category: SimpleNamespace) -> bool`: Обновляет категорию в JSON файле.
    * **Описание**: Обновляет категорию в JSON файле.
    * **Параметры**:
        * `json_path` (Path): Путь к JSON файлу.
        * `category` (SimpleNamespace): Объект категории для обновления.
    * **Возвращает**: `bool`: True, если обновление прошло успешно; False иначе.
    * **Исключения**: Возможны исключения при работе с JSON файлом.


- `get_category(category_name: str) -> Optional[SimpleNamespace]`: Возвращает SimpleNamespace объект для заданного имени категории.
    * **Описание**: Возвращает объект категории по имени.
    * **Параметры**:
        * `category_name` (str): Имя категории.
    * **Возвращает**: `Optional[SimpleNamespace]`: Объект SimpleNamespace или `None`, если не найден.
    * **Исключения**: Возможны исключения при работе с данными.

- `list_categories() -> Optional[List[str]]`: Возвращает список категорий в текущей кампании.
    * **Описание**: Возвращает список имен категорий.
    * **Параметры**: Нет
    * **Возвращает**: `Optional[List[str]]`: Список имен категорий или `None`, если категорий не найдено.
    * **Исключения**: Возможны исключения при работе с данными кампании.

- `get_category_products(category_name: str) -> Optional[List[SimpleNamespace]]`: Чтение данных о товарах из JSON файлов для конкретной категории.
    * **Описание**: Чтение данных о товарах из JSON файлов.
    * **Параметры**:
        * `category_name` (str): Имя категории.
    * **Возвращает**: `Optional[List[SimpleNamespace]]`: Список объектов SimpleNamespace, представляющих товары или `None`.
    * **Исключения**:  `FileNotFoundError`, `JSONDecodeError`.



## Функции


## Модули

- `src.suppliers.aliexpress.campaign.ali_promo_campaign`
- `src.suppliers.aliexpress.campaign.gsheet`
- `src.suppliers.aliexpress.utils`
- `src.utils.jjson`
- `src.utils.convertors.csv`
- `src.utils.printer`
- `src.utils.file`
- `src.logger`