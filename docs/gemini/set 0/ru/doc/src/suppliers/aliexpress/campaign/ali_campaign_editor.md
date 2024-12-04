# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py`

## Обзор

Этот модуль предоставляет класс `AliCampaignEditor` для редактирования рекламных кампаний на AliExpress. Он позволяет удалять, обновлять и получать информацию о товарах и категориях кампании, а также обновлять общие свойства кампании. Модуль использует данные, хранящиеся в файлах JSON, и взаимодействует с Google Sheets (через класс `AliCampaignGoogleSheet`).

## Классы

### `AliCampaignEditor`

**Описание**: Класс для редактирования рекламных кампаний AliExpress. Наследуется от класса `AliPromoCampaign`.

**Методы**:

* **`__init__`**: Инициализирует экземпляр класса.
    * **Описание**:  Инициализирует объект, загружает данные из файла JSON (если предоставлен), или создаёт новые по параметрам.
    * **Параметры**:
        * `campaign_name` (str): Название кампании.
        * `language` (Optional[str | dict], optional): Язык кампании. По умолчанию 'EN'.
        * `currency` (Optional[str], optional): Валюта кампании. По умолчанию 'USD'.
        * `campaign_file` (Optional[str | Path]): Путь к файлу JSON с данными о кампании. По умолчанию None.
    * **Возвращает**:
        * `None`
    * **Исключения**:
        * `CriticalError`: Если не указаны ни `campaign_name`, ни `campaign_file`.

* **`delete_product`**: Удаляет товар из кампании.
    * **Описание**: Удаляет запись о товаре, если у него нет аффилиатной ссылки. Удаляет запись о товаре из файла `sources.txt` или переименовывает файл товара, если он не найден.
    * **Параметры**:
        * `product_id` (str): ID товара для удаления.
        * `exc_info` (bool, optional): Флаг, указывающий на включение информации об ошибке в логи. По умолчанию `False`.
    * **Пример**:
        ```python
        editor = AliCampaignEditor(campaign_name="Summer Sale")
        editor.delete_product("12345")
        ```

* **`update_product`**: Обновляет данные о товаре в категории.
    * **Описание**: Обновляет информацию о товаре в указанной категории.
    * **Параметры**:
        * `category_name` (str): Имя категории.
        * `lang` (str): Язык кампании.
        * `product` (dict): Словарь с данными о товаре.
    * **Пример**:
        ```python
        editor = AliCampaignEditor(campaign_name="Summer Sale")
        editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
        ```

* **`update_campaign`**: Обновляет свойства кампании.
    * **Описание**: Обновляет свойства кампании, такие как описание, теги и т.д.
    * **Пример**:
        ```python
        editor = AliCampaignEditor(campaign_name="Summer Sale")
        editor.update_campaign()
        ```

* **`update_category`**: Обновляет категорию в файле JSON.
    * **Описание**: Обновляет данные о категории в файле JSON.
    * **Параметры**:
        * `json_path` (Path): Путь к файлу JSON.
        * `category` (SimpleNamespace): Объект категории для обновления.
    * **Возвращает**:
        * bool: `True`, если обновление успешно, `False` - в противном случае.
    * **Пример**:
        ```python
        category = SimpleNamespace(name="New Category", description="Updated description")
        editor = AliCampaignEditor(campaign_name="Summer Sale")
        result = editor.update_category(Path("category.json"), category)
        print(result)
        ```

* **`get_category`**: Возвращает объект категории по имени.
    * **Описание**: Возвращает `SimpleNamespace` объект для заданного имени категории.
    * **Параметры**:
        * `category_name` (str): Имя категории.
    * **Возвращает**:
        * `Optional[SimpleNamespace]`: Объект `SimpleNamespace` или `None`, если не найден.

* **`list_categories`**: Получение списка категорий.
    * **Описание**: Возвращает список имён категорий.
    * **Возвращает**:
        * `Optional[List[str]]`: Список категорий или `None` при отсутствии.

* **`get_category_products`**: Чтение данных о товарах из JSON файлов для конкретной категории.
    * **Описание**: Возвращает список объектов `SimpleNamespace` представляющих товары из указанной категории.
    * **Параметры**:
        * `category_name` (str): Имя категории.
    * **Возвращает**:
        * `Optional[List[SimpleNamespace]]`: Список товаров или `None` в случае ошибки.


## Функции

(Список функций из модуля, если они есть)