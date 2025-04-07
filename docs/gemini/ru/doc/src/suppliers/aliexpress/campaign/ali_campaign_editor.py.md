# Модуль для редактирования рекламных кампаний AliExpress

## Обзор

Модуль `ali_campaign_editor.py` предоставляет инструменты для редактирования рекламных кампаний на платформе AliExpress. Он включает в себя функциональность для добавления, удаления, обновления продуктов и категорий, а также для управления свойствами самой кампании.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процесса управления рекламными кампаниями на AliExpress. Он позволяет программно взаимодействовать с данными кампании, хранящимися в файлах JSON, и выполнять различные операции, такие как обновление информации о продуктах, изменение параметров кампании и управление категориями.

Модуль расширяет функциональность класса `AliPromoCampaign` и использует другие модули проекта, такие как `src.gs`, `src.suppliers.aliexpress.utils`, `src.utils.jjson` и `src.utils.file`.

## Классы

### `AliCampaignEditor`

**Описание**: Редактор рекламных кампаний.

**Наследует**: `AliPromoCampaign`

**Принцип работы**:
Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress. Он инициализируется с именем кампании, языком и валютой. Он предоставляет методы для удаления продуктов, обновления информации о продуктах, обновления свойств кампании и управления категориями. Класс использует другие модули проекта для чтения и записи данных в файлы JSON, а также для взаимодействия с Google Sheets.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.
- `delete_product`: Удаляет продукт, у которого нет партнерской ссылки.
- `update_product`: Обновляет информацию о продукте в категории.
- `update_campaign`: Обновляет свойства кампании, такие как описание и теги.
- `update_category`: Обновляет категорию в файле JSON.
- `get_category`: Возвращает объект `SimpleNamespace` для заданной категории.
- `list_categories`: Возвращает список категорий в текущей кампании.
- `get_category_products`: Читает данные о товарах из JSON файлов для конкретной категории.

#### `__init__`

```python
    def __init__(self, 
                 campaign_name: str, 
                 language: Optional[str | dict] = None, 
                 currency: Optional[str] = None):
        """ Initialize the AliCampaignEditor with the given parameters.
        
        Args:
            campaign_name (Optional[str]): The name of the campaign. Defaults to `None`.
            language (Optional[str | dict]): The language of the campaign. Defaults to 'EN'.
            currency (Optional[str]): The currency for the campaign. Defaults to 'USD'.
            campaign_file (Optional[str | Path]): Optionally load a `<lang>_<currency>.json` file from the campaign root folder. Defaults to `None`.

        Raises:
            CriticalError: If neither `campaign_name` nor `campaign_file` is provided.
        
        Example:
        # 1. by campaign parameters
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
        # 2. load fom file
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
        """
        ...
        super().__init__(campaign_name = campaign_name, language = language, currency = currency)
        #self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)
```

**Назначение**: Инициализирует экземпляр класса `AliCampaignEditor`.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (Optional[str | dict]): Язык кампании. По умолчанию `None`.
- `currency` (Optional[str]): Валюта кампании. По умолчанию `None`.

**Как работает функция**:

1.  Вызывает конструктор родительского класса `AliPromoCampaign` с переданными параметрами `campaign_name`, `language` и `currency`.

2.  Закомментирована строка, которая, по-видимому, должна была инициализировать атрибут `google_sheet` экземпляром класса `AliCampaignGoogleSheet`.

**Примеры**:
```python
# 1. Создание экземпляра класса с указанием имени кампании, языка и валюты
editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")

# 2. Создание экземпляра класса с указанием имени кампании и файла кампании
editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
```

#### `delete_product`

```python
    def delete_product(self, product_id: str, exc_info: bool = False):\
        """ Delete a product that does not have an affiliate link.
        
        Args:
            product_id (str): The ID of the product to be deleted.
            exc_info (bool): Whether to include exception information in logs. Defaults to `False`.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.delete_product("12345")
        """
        ...
        _product_id = extract_prod_ids(product_id)
        
        product_path = self.category_path / 'sources.txt'
        prepared_product_path = self.category_path / '_sources.txt'
        products_list = read_text_file(product_path)
        if products_list:
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), prepared_product_path)
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), product_path)
                    
        else:
            product_path = self.category_path / 'sources' / f'{product_id}.html'    
            try:
                product_path.rename(self.category_path / 'sources' / f'{product_id}_.html')
                logger.success(f"Product file {product_path=} renamed successfully.")
            except FileNotFoundError as ex:
                logger.error(f"Product file {product_path=} not found.", exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)
```

**Назначение**: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `product_id` (str): ID продукта, который нужно удалить.
- `exc_info` (bool): Определяет, нужно ли включать информацию об исключении в логи. По умолчанию `False`.

**Как работает функция**:

1.  Извлекает ID продукта из `product_id` с помощью функции `extract_prod_ids`. Результат сохраняется в переменной `_product_id`.

2.  Определяет пути к файлам `sources.txt` и `_sources.txt` в каталоге категории.

3.  Читает содержимое файла `sources.txt` в список `products_list` с помощью функции `read_text_file`.

4.  Если `products_list` не пуст, то происходит итерация по списку продуктов.

    *   Если `_product_id` не пуст, то извлекается ID записи из `record` с помощью функции `extract_prod_ids`. Если ID записи равен `product_id`, то запись удаляется из списка `products_list` и список сохраняется в файл `_sources.txt` с помощью функции `save_text_file`.

    *   Если `_product_id` пуст, то если запись равна `product_id`, то запись удаляется из списка `products_list` и список сохраняется в файл `product_path` с помощью функции `save_text_file`.

5.  Если `products_list` пуст, то определяется путь к файлу продукта в каталоге `sources`.

6.  Попытка переименовать файл продукта с добавлением символа `_` в конце имени. Если переименование успешно, то записывается сообщение об успехе в лог. Если файл не найден, то записывается сообщение об ошибке в лог. Если произошла другая ошибка, то записывается критическая ошибка в лог.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.delete_product("12345")
```

#### `update_product`

```python
    def update_product(self, category_name: str, lang: str, product: dict):\
        """ Update product details within a category.

        Args:
            category_name (str): The name of the category where the product should be updated.
            lang (str): The language of the campaign.
            product (dict): A dictionary containing product details.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
        """
        ...
        self.dump_category_products_files(category_name, lang, product)
```

**Назначение**: Обновляет информацию о продукте в категории.

**Параметры**:
- `category_name` (str): Имя категории, в которой нужно обновить продукт.
- `lang` (str): Язык кампании.
- `product` (dict): Словарь, содержащий информацию о продукте.

**Как работает функция**:

Вызывает метод `dump_category_products_files` с переданными параметрами `category_name`, `lang` и `product`.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
```

#### `update_campaign`

```python
    def update_campaign(self):\
        """ Update campaign properties such as `description`, `tags`, etc.
        
        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.update_campaign()
        """
        ...
```

**Назначение**: Обновляет свойства кампании, такие как описание и теги.

**Как работает функция**:
Функция `update_campaign` не имеет конкретной реализации (код отсутствует). Она предназначена для обновления свойств кампании, таких как описание и теги.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
editor.update_campaign()
```

#### `update_category`

```python
    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:\
        """ Update the category in the JSON file.

        Args:
            json_path (Path): Path to the JSON file.
            category (SimpleNamespace): Category object to be updated.

        Returns:
            bool: True if update is successful, False otherwise.

        Example:
            >>> category = SimpleNamespace(name="New Category", description="Updated description")
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> result = editor.update_category(Path("category.json"), category)
            >>> print(result)  # True if successful
        """
        ...
        try:
            data = j_loads(json_path)  # Read JSON data from file
            data['category'] = category.__dict__  # Convert SimpleNamespace to dict
            j_dumps(data, json_path)  # Write updated JSON data back to file
            return True
        except Exception as ex:
            logger.error(f"Failed to update category {json_path}: {ex}")
            return False
```

**Назначение**: Обновляет категорию в файле JSON.

**Параметры**:
- `json_path` (Path): Путь к файлу JSON.
- `category` (SimpleNamespace): Объект категории, который нужно обновить.

**Возвращает**:
- `bool`: `True`, если обновление прошло успешно, `False` в противном случае.

**Как работает функция**:

1.  Пытается прочитать данные из файла JSON, используя функцию `j_loads`.
2.  Преобразует объект `SimpleNamespace` `category` в словарь, используя атрибут `__dict__`, и присваивает его ключу `'category'` в данных JSON.
3.  Записывает обновленные данные JSON обратно в файл, используя функцию `j_dumps`.
4.  В случае успеха возвращает `True`.
5.  В случае возникновения исключения записывает сообщение об ошибке в лог и возвращает `False`.

**Примеры**:
```python
category = SimpleNamespace(name="New Category", description="Updated description")
editor = AliCampaignEditor(campaign_name="Summer Sale")
result = editor.update_category(Path("category.json"), category)
print(result)  # True if successful
```

#### `get_category`

```python
    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:\
        """ Returns the SimpleNamespace object for a given category name.

        Args:
            category_name (str): The name of the category to retrieve.

        Returns:
            Optional[SimpleNamespace]: SimpleNamespace object representing the category or `None` if not found.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> category = editor.get_category("Electronics")
            >>> print(category)  # SimpleNamespace or None
        """
        ...
        try:
            if hasattr(self.campaign.category, category_name):
                return getattr(self.campaign.category, category_name)
            else:
                logger.warning(f"Category {category_name} not found in the campaign.")
                return
        except Exception as ex:
            logger.error(f"Error retrieving category {category_name}.", ex, exc_info=True)
            return
```

**Назначение**: Возвращает объект `SimpleNamespace` для заданной категории.

**Параметры**:
- `category_name` (str): Имя категории, которую нужно получить.

**Возвращает**:
- `Optional[SimpleNamespace]`: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.

**Как работает функция**:

1.  Пытается получить категорию из атрибута `self.campaign.category`.
2.  Если категория найдена, возвращает ее.
3.  Если категория не найдена, записывает предупреждение в лог и возвращает `None`.
4.  В случае возникновения исключения записывает сообщение об ошибке в лог и возвращает `None`.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
category = editor.get_category("Electronics")
print(category)  # SimpleNamespace or None
```

#### `list_categories`

```python
    @property
    def list_categories(self) -> Optional[List[str]]:\
        """ Retrieve a list of categories in the current campaign.

        Returns:
            Optional[List[str]]: A list of category names, or None if no categories are found.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> categories = editor.categories_list
            >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
        """
        try:
            # Ensure campaign has a category attribute and it is a SimpleNamespace
            if hasattr(self.campaign, 'category') and isinstance(self.campaign.category, SimpleNamespace):
                return list(vars(self.campaign.category).keys())
            else:
                logger.warning("No categories found in the campaign.")
                return
        except Exception as ex:
            logger.error(f"Error retrieving categories list: {ex}")
            return
```

**Назначение**: Возвращает список категорий в текущей кампании.

**Возвращает**:
- `Optional[List[str]]`: Список имен категорий или `None`, если категории не найдены.

**Как работает функция**:

1.  Пытается получить список категорий из атрибута `self.campaign.category`.
2.  Если атрибут `category` существует и является экземпляром `SimpleNamespace`, возвращает список ключей атрибута.
3.  Если атрибут `category` не существует или не является экземпляром `SimpleNamespace`, записывает предупреждение в лог и возвращает `None`.
4.  В случае возникновения исключения записывает сообщение об ошибке в лог и возвращает `None`.

**Примеры**:
```python
editor = AliCampaignEditor(campaign_name="Summer Sale")
categories = editor.categories_list
print(categories)  # ['Electronics', 'Fashion', 'Home']
```

#### `get_category_products`

```python
    async def get_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Чтение данных о товарах из JSON файлов для конкретной категории.

        Args:
            category_name (str): Имя категории.

        Returns:
            Optional[List[SimpleNamespace]]: Список объектов SimpleNamespace, представляющих товары.

        Example:
            >>> products = campaign.get_category_products("Electronics")
            >>> print(len(products))
            15
        """
        category_path = (
            self.base_path
            / "category"
            / category_name
            / f"{self.language}_{self.currency}"
        )
        json_filenames = await get_filenames_from_directory (category_path, extensions="json")
        products = []

        if json_filenames:
            for json_filename in json_filenames:
                product_data = j_loads_ns(category_path / json_filename)
                product = SimpleNamespace(**vars(product_data))
                products.append(product)
            return products
        else:
            logger.error(
                f"No JSON files found for {category_name=} at {category_path=}.\\nStart prepare category"
            )
            self.process_category_products(category_name)
            return 
```

**Назначение**: Чтение данных о товарах из JSON файлов для конкретной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары.

**Как работает функция**:

1.  Формирует путь к каталогу категории на основе `base_path`, `category_name`, `language` и `currency`.
2.  Получает список имен файлов JSON в каталоге категории с помощью асинхронной функции `get_filenames_from_directory`.
3.  Если файлы JSON найдены, то для каждого файла:

    *   Читает данные из файла JSON с помощью функции `j_loads_ns`.
    *   Преобразует данные в объект `SimpleNamespace`.
    *   Добавляет объект `SimpleNamespace` в список `products`.
4.  Если файлы JSON не найдены, то записывает сообщение об ошибке в лог и вызывает метод `process_category_products` для подготовки категории.
5.  Возвращает список `products`.

**Примеры**:
```python
products = campaign.get_category_products("Electronics")
print(len(products))
15
```

## Функции

В данном модуле не представлены отдельные функции, не относящиеся к классам. Все основные операции выполняются методами класса `AliCampaignEditor`.