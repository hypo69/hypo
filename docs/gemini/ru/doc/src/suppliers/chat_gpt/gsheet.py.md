# Модуль `gsheet`

## Обзор

Модуль `gsheet.py` предназначен для управления Google Sheets в контексте рекламных кампаний AliExpress. Он содержит класс `GptGs`, который наследуется от `SpreadSheet` и предоставляет функциональность для чтения и записи данных кампании, категорий и продуктов в Google Sheets.

## Подробней

Модуль `gsheet` обеспечивает интеграцию с Google Sheets для автоматизации работы с данными в рекламных кампаниях. Он позволяет читать данные о кампаниях и категориях из Google Sheets, записывать данные о продуктах, а также очищать и обновлять листы.

## Классы

### `GptGs`

**Описание**: Класс `GptGs` предназначен для управления Google Sheets в рекламных кампаниях AliExpress. Он наследуется от класса `SpreadSheet` и предоставляет методы для работы с данными категорий и продуктов.

**Как работает класс**:

Класс `GptGs` использует идентификатор Google Sheets для доступа к таблице. Он предоставляет методы для очистки листов, обновления данных кампании, чтения и записи данных категорий и продуктов.

**Методы**:

- `__init__`: Инициализирует объект `GptGs` с указанным ID Google Sheets.
- `clear`: Очищает содержимое листов продуктов, категорий и кампании.
- `update_chat_worksheet`: Записывает данные кампании в указанный лист Google Sheets.
- `get_campaign_worksheet`: Читает данные кампании из листа 'campaign'.
- `set_category_worksheet`: Записывает данные категории в лист 'category'.
- `get_category_worksheet`: Читает данные категории из листа 'category'.
- `set_categories_worksheet`: Записывает данные о категориях в лист 'categories'.
- `get_categories_worksheet`: Читает данные о категориях из листа 'categories'.
- `set_product_worksheet`: Записывает данные продукта в новый лист Google Sheets.
- `get_product_worksheet`: Читает данные продукта из листа 'products'.
- `set_products_worksheet`: Записывает данные о продуктах в лист категории.
- `delete_products_worksheets`: Удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
- `save_categories_from_worksheet`: Сохраняет данные категорий из Google Sheets в атрибут `category` объекта `campaign`.
- `save_campaign_from_worksheet`: Сохраняет данные рекламной кампании из Google Sheets, включая категории, и обновляет объект `campaign`.

## Функции

### `__init__`

```python
def __init__(self):
    """ 
    Инициализирует класс `AliCampaignGoogleSheet` с указанным ID Google Sheets spreadsheet и дополнительными параметрами.

    Args:
        campaign_name (str): Название рекламной кампании.
        category_name (str): Название категории.
        language (str): Язык рекламной кампании.
        currency (str): Валюта рекламной кампании.
    """
    # Initialize SpreadSheet with the spreadsheet ID
    super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
```

**Назначение**: Инициализация класса `GptGs` с указанием ID Google Sheets.

**Как работает функция**:

1. Вызывает конструктор родительского класса `SpreadSheet` с ID Google Sheets `'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'`.
2. Устанавливает соединение с Google Sheets для дальнейшей работы с данными.

**Примеры**:

```python
gpt_gs = GptGs()
```

### `clear`

```python
def clear(self):
    """ 
    Очищает содержимое листов.
    Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
    """
    try:
        self.delete_products_worksheets()
        # ws_to_clear = ['category','categories','campaign']
        # for ws in self.spreadsheet.worksheets():
        #     self.get_worksheet(ws).clear()

    except Exception as ex:
        logger.error("Ошибка очистки", ex)
```

**Назначение**: Очистка содержимого листов Google Sheets.

**Как работает функция**:

1. Вызывает метод `delete_products_worksheets` для удаления всех листов продуктов.
2. Пытается выполнить очистку листов категорий и кампании (закомментировано в текущей версии кода).
3. В случае ошибки логирует сообщение об ошибке.

**Примеры**:

```python
gpt_gs.clear()
```

### `update_chat_worksheet`

```python
def update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None):
    """ 
    Записывает данные кампании в лист Google Sheets.

    Args:
        campaign (SimpleNamespace | str): Объект SimpleNamespace с полями данных кампании для записи.
        language (str): Необязательный параметр языка.
        currency (str): Необязательный параметр валюты.
    
    Raises:
        Exception: Пробрасывает исключение, если происходит ошибка при записи данных кампании в лист.
    """
    try:
        ws: Worksheet = self.get_worksheet(conversation_name)
        _ = data.__dict__
        # Extract data from the SimpleNamespace attribute
        name =  _.get('name','')
        title =  _.get('title')
        description =  _.get('description')
        tags =  ', '.join(map(str, _.get('tags', [])))
        products_count =  _.get('products_count','~')

        # Prepare updates for the given SimpleNamespace object
        updates = [
            {'range': f'A{start_row}', 'values': [[name]]},
            {'range': f'B{start_row}', 'values': [[title]]},
            {'range': f'C{start_row}', 'values': [[description]]},
            {'range': f'D{start_row}', 'values': [[tags]]},
            {'range': f'E{start_row}', 'values': [[products_count]]},
        ]

    except Exception as ex:
        logger.error("Error writing campaign data to worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных кампании в указанный лист Google Sheets.

**Как работает функция**:

1. Пытается получить указанный лист Google Sheets.
2. Извлекает данные из объекта `SimpleNamespace` или словаря.
3. Формирует список обновлений для записи данных в лист.
4. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
data = SimpleNamespace(name='Test Campaign', title='Test Title', description='Test Description', tags=['tag1', 'tag2'], products_count=100)
gpt_gs.update_chat_worksheet(data, 'campaign_name')
```

### `get_campaign_worksheet`

```python
def get_campaign_worksheet(self) -> SimpleNamespace:
    """ 
    Считывает данные кампании из листа 'campaign'.

    Returns:
        SimpleNamespace: Объект SimpleNamespace с полями данных кампании.

    Raises:
        ValueError: Если лист 'campaign' не найден.
        Exception: Пробрасывает исключение, если происходит ошибка при получении данных кампании из листа.
    """
    try:
        ws: Worksheet = self.get_worksheet('campaign')
        if not ws:
            raise ValueError("Worksheet \'campaign\' not found.")

        data = ws.get_all_values()
        campaign_data = SimpleNamespace(
            name=data[0][1],
            title=data[1][1],
            language=data[2][1],
            currency=data[3][1],
            description=data[4][1]
        )

        logger.info("Campaign data read from \'campaign\' worksheet.")
        return campaign_data

    except Exception as ex:
        logger.error("Error getting campaign worksheet data.", ex, exc_info=True)
        raise
```

**Назначение**: Чтение данных кампании из листа 'campaign'.

**Как работает функция**:

1. Пытается получить лист 'campaign'.
2. Если лист не найден, выбрасывает исключение `ValueError`.
3. Считывает все значения из листа.
4. Создает объект `SimpleNamespace` с данными кампании.
5. Логирует сообщение об успешном чтении данных.
6. Возвращает объект `SimpleNamespace` с данными кампании.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
campaign_data = gpt_gs.get_campaign_worksheet()
print(campaign_data.name)
```

### `set_category_worksheet`

```python
def set_category_worksheet(self, category: SimpleNamespace | str):
    """ 
    Записывает данные из объекта SimpleNamespace в ячейки Google Sheets по вертикали.

    Args:
        category (SimpleNamespace): Объект SimpleNamespace с полями данных для записи.

    Raises:
        TypeError: Если передан не SimpleNamespace для категории.
        Exception: Пробрасывает исключение, если происходит ошибка при установке данных категории в лист.
    """
    category = category if isinstance(category, SimpleNamespace) else self.get_campaign_category(category)
    try:
        ws: Worksheet = self.get_worksheet('category')

        if isinstance(category, SimpleNamespace):
            # Prepare data for vertical writing
            _ = category.__dict__
            vertical_data = [
                ['Name', _.get('name','')],
                ['Title', _.get('title','')],
                ['Description', _.get('description')],
                ['Tags', ', '.join(map(str, _.get('tags', [])))],
                ['Products Count', _.get('products_count', '~')]
            ]

            # Write data vertically
            ws.update('A1:B{}'.format(len(vertical_data)), vertical_data)

            logger.info("Category data written to \'category\' worksheet vertically.")
        else:
            raise TypeError("Expected SimpleNamespace for category.")

    except Exception as ex:
        logger.error("Error setting category worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных категории в лист 'category'.

**Как работает функция**:

1. Проверяет, является ли входной параметр `category` объектом `SimpleNamespace`.
2. Если `category` не является `SimpleNamespace`, пытается получить категорию кампании.
3. Пытается получить лист 'category'.
4. Формирует данные для вертикальной записи в лист.
5. Записывает данные в лист 'category'.
6. Логирует сообщение об успешной записи данных.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
category_data = SimpleNamespace(name='Test Category', title='Test Title', description='Test Description', tags=['tag1', 'tag2'], products_count=100)
gpt_gs.set_category_worksheet(category_data)
```

### `get_category_worksheet`

```python
def get_category_worksheet(self) -> SimpleNamespace:
    """ 
    Считывает данные категории из листа 'category'.

    Returns:
        SimpleNamespace: Объект SimpleNamespace с полями данных категории.

    Raises:
        ValueError: Если лист 'category' не найден.
        Exception: Пробрасывает исключение, если происходит ошибка при получении данных категории из листа.
    """
    try:
        ws: Worksheet = self.get_worksheet('category')
        if not ws:
            raise ValueError("Worksheet \'category\' not found.")

        data = ws.get_all_values()
        category_data = SimpleNamespace(
            name=data[1][1],
            title=data[2][1],
            description=data[3][1],
            tags=data[4][1].split(', '),
            products_count=int(data[5][1])
        )

        logger.info("Category data read from \'category\' worksheet.")
        return category_data

    except Exception as ex:
        logger.error("Error getting category worksheet data.", ex, exc_info=True)
        raise
```

**Назначение**: Чтение данных категории из листа 'category'.

**Как работает функция**:

1. Пытается получить лист 'category'.
2. Если лист не найден, выбрасывает исключение `ValueError`.
3. Считывает все значения из листа.
4. Создает объект `SimpleNamespace` с данными категории.
5. Логирует сообщение об успешном чтении данных.
6. Возвращает объект `SimpleNamespace` с данными категории.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
category_data = gpt_gs.get_category_worksheet()
print(category_data.name)
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ 
    Записывает данные из объекта SimpleNamespace в ячейки Google Sheets.

    Args:
        categories (SimpleNamespace): Объект SimpleNamespace с полями данных для записи.
    """
    ws: Worksheet = self.get_worksheet('categories')
    # ws.clear()  # Clear the 'categories' worksheet

    try:
        # Initialize the starting row
        start_row = 2

        # Iterate over all attributes of the categories object
        for attr_name in dir(categories):
            attr_value = getattr(categories, attr_name, None)

            # Skip non-SimpleNamespace attributes or attributes with no data
            if not isinstance(attr_value, SimpleNamespace) or not any(
                hasattr(attr_value, field) for field in ['name', 'title', 'description', 'tags', 'products_count']
            ):
                continue
            _ = attr_value.__dict__
            # Extract data from the SimpleNamespace attribute
            name =  _.get('name','')
            title =  _.get('title')
            description =  _.get('description')
            tags =  ', '.join(map(str, _.get('tags', [])))
            products_count =  _.get('products_count','~')

            # Prepare updates for the given SimpleNamespace object
            updates = [
                {'range': f'A{start_row}', 'values': [[name]]},
                {'range': f'B{start_row}', 'values': [[title]]},
                {'range': f'C{start_row}', 'values': [[description]]},
                {'range': f'D{start_row}', 'values': [[tags]]},
                {'range': f'E{start_row}', 'values': [[products_count]]},
            ]

            # Perform batch update
            if updates:
                ws.batch_update(updates)
                logger.info(f"Category data written to \'categories\' worksheet for {attr_name}.")

            # Move to the next row
            start_row += 1

    except Exception as ex:
        logger.error("Error setting categories worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных о категориях в лист 'categories'.

**Как работает функция**:

1. Пытается получить лист 'categories'.
2. Итерируется по атрибутам объекта `categories`.
3. Проверяет, является ли атрибут объектом `SimpleNamespace` и содержит ли необходимые поля.
4. Формирует список обновлений для записи данных в лист.
5. Выполняет пакетное обновление листа.
6. Логирует сообщение об успешной записи данных.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
categories_data = SimpleNamespace(cat1=SimpleNamespace(name='Cat1', title='Title1', description='Desc1', tags=['tag1'], products_count=10), 
                                 cat2=SimpleNamespace(name='Cat2', title='Title2', description='Desc2', tags=['tag2'], products_count=20))
gpt_gs.set_categories_worksheet(categories_data)
```

### `get_categories_worksheet`

```python
def get_categories_worksheet(self) -> List[List[str]]:
    """ 
    Считывает данные из столбцов A по E, начиная со второй строки, из листа 'categories'.

    Returns:
        List[List[str]]: Список строк с данными из столбцов A по E.

    Raises:
        ValueError: Если лист 'categories' не найден.
        Exception: Пробрасывает исключение, если происходит ошибка при получении данных категории из листа.
    """
    try:
        ws: Worksheet = self.get_worksheet('categories')
        if not ws:
            raise ValueError("Worksheet \'categories\' not found.")

        # Read all values from the worksheet
        data = ws.get_all_values()

        # Extract data from columns A to E, starting from the second row
        data = [row[:5] for row in data[1:] if len(row) >= 5]  

        logger.info("Category data read from \'categories\' worksheet.")
        return data

    except Exception as ex:
        logger.error("Error getting category data from worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Чтение данных о категориях из листа 'categories'.

**Как работает функция**:

1. Пытается получить лист 'categories'.
2. Если лист не найден, выбрасывает исключение `ValueError`.
3. Считывает все значения из листа.
4. Извлекает данные из столбцов A по E, начиная со второй строки.
5. Логирует сообщение об успешном чтении данных.
6. Возвращает список строк с данными о категориях.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
categories_data = gpt_gs.get_categories_worksheet()
for row in categories_data:
    print(row)
```

### `set_product_worksheet`

```python
def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str):
    """ 
    Записывает данные продукта в новый лист Google Sheets.

    Args:
        category_name Category name.
        product SimpleNamespace object with product data fields for writing.
    """
    time.sleep(10)
    ws = self.copy_worksheet('product_template', category_name)  # Copy 'product_template' to new worksheet
    try:
        headers = [
            'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
            'product_main_image_url', 'local_image_path', 'product_small_image_urls',
            'product_video_url', 'local_video_path', 'first_level_category_id',
            'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
            'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
            'target_original_price_currency', 'original_price_currency', 'product_title',
            'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
        ]
        ws.update('A1:Y1', [headers])

        _ = product.__dict__
        row_data = [
            str(_.get('product_id')),
            str(_.get('app_sale_price')),
            str(_.get('original_price')),
            str(_.get('sale_price')),
            str(_.get('discount')),
            str(_.get('product_main_image_url')),
            str(_.get('local_image_path')),
            ', '.join(map(str, _.get('product_small_image_urls', []))),
            str(_.get('product_video_url')),
            str(_.get('local_video_path')),
            str(_.get('first_level_category_id')),
            str(_.get('first_level_category_name')),
            str(_.get('second_level_category_id')),
            str(_.get('second_level_category_name')),
            str(_.get('target_sale_price')),
            str(_.get('target_sale_price_currency')),
            str(_.get('target_app_sale_price_currency')),
            str(_.get('target_original_price_currency')),
            str(_.get('original_price_currency')),
            str(_.get('product_title')),
            str(_.get('evaluate_rate')),
            str(_.get('promotion_link')),
            str(_.get('shop_url')),
            str(_.get('shop_id')),
            ', '.join(map(str, _.get('tags', [])))
        ]

        ws.update('A2:Y2', [row_data])  # Update row data in a single row

        logger.info("Product data written to worksheet.")
    except Exception as ex:
        logger.error("Error updating product data in worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных продукта в новый лист Google Sheets.

**Как работает функция**:

1. Делает паузу в 10 секунд.
2. Копирует лист 'product_template' и создает новый лист с именем `category_name`.
3. Пытается записать данные продукта в новый лист.
4. Формирует заголовки для листа.
5. Извлекает данные из объекта `product`.
6. Формирует список данных для записи в лист.
7. Записывает данные в лист.
8. Логирует сообщение об успешной записи данных.
9. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
product_data = SimpleNamespace(product_id=123, app_sale_price=10.0, original_price=20.0, sale_price=15.0, discount=0.25,
                                product_main_image_url='http://example.com/image.jpg', local_image_path='/tmp/image.jpg',
                                product_small_image_urls=['http://example.com/image1.jpg', 'http://example.com/image2.jpg'],
                                product_video_url='http://example.com/video.mp4', local_video_path='/tmp/video.mp4',
                                first_level_category_id=1, first_level_category_name='Category1',
                                second_level_category_id=2, second_level_category_name='Category2',
                                target_sale_price=12.0, target_sale_price_currency='USD',
                                target_app_sale_price_currency='USD', target_original_price_currency='USD',
                                original_price_currency='USD', product_title='Test Product', evaluate_rate=4.5,
                                promotion_link='http://example.com/promotion', shop_url='http://example.com/shop',
                                shop_id=456, tags=['tag1', 'tag2'])
gpt_gs.set_product_worksheet(product_data, 'TestCategory')
```

### `get_product_worksheet`

```python
def get_product_worksheet(self) -> SimpleNamespace:
    """ 
    Считывает данные продукта из листа 'products'.

    Returns:
        SimpleNamespace: Объект SimpleNamespace с полями данных продукта.

    Raises:
        ValueError: Если лист 'products' не найден.
        Exception: Пробрасывает исключение, если происходит ошибка при получении данных продукта из листа.
    """
    try:
        ws: Worksheet = self.get_worksheet('products')
        if not ws:
            raise ValueError("Worksheet \'products\' not found.")

        data = ws.get_all_values()
        product_data = SimpleNamespace(
            id=data[1][1],
            name=data[2][1],
            title=data[3][1],
            description=data[4][1],
            tags=data[5][1].split(', '),
            price=float(data[6][1])
        )

        logger.info("Product data read from \'products\' worksheet.")
        return product_data

    except Exception as ex:
        logger.error("Error getting product worksheet data.", ex, exc_info=True)
        raise
```

**Назначение**: Чтение данных продукта из листа 'products'.

**Как работает функция**:

1. Пытается получить лист 'products'.
2. Если лист не найден, выбрасывает исключение `ValueError`.
3. Считывает все значения из листа.
4. Создает объект `SimpleNamespace` с данными продукта.
5. Логирует сообщение об успешном чтении данных.
6. Возвращает объект `SimpleNamespace` с данными продукта.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
product_data = gpt_gs.get_product_worksheet()
print(product_data.name)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name:str):
    """ 
    Записывает данные из списка объектов SimpleNamespace в ячейки Google Sheets.

    Args:
        ns_list (List[SimpleNamespace]|SimpleNamespace): Список объектов SimpleNamespace с полями данных для записи.
    """
    if category_name:
        category_ns:SimpleNamespace = getattr(self.campaign.category,category_name)
        products_ns:SimpleNamespace = category_ns.products
    else:
        logger.warning(f"На ашел товары в {pprint(category_ns)}")
        return
    ws: Worksheet = self.get_worksheet(category_name)

    try:
        updates:list=[]
        for index, value in enumerate(products_ns, start=2):
            _ = value.__dict__
            updates.append({'range': f'A{index}', 'values': [[str(_.get('product_id',''))]]})
            updates.append({'range': f'B{index}', 'values': [[str(_.get('product_title',''))]]})
            updates.append({'range': f'C{index}', 'values': [[str(_.get('title',''))]]})
            updates.append({'range': f'D{index}', 'values': [[str(_.get('local_image_path',''))]]})
            updates.append({'range': f'D{index}', 'values': [[str(_.get('product_video_url',''))]]})
            updates.append({'range': f'F{index}', 'values': [[str(_.get('original_price',''))]]})
            updates.append({'range': f'F{index}', 'values': [[str(_.get('app_sale_price',''))]]})
            updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price',''))]]})
            updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price',''))]]})

        ws.batch_update(updates)
        logger.info("Products data written to \'products\' worksheet.")


    except Exception as ex:
        logger.error("Error setting products worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных о продуктах в лист категории.

**Как работает функция**:

1. Если `category_name` указан, пытается получить данные о категории и продуктах из атрибутов объекта `campaign`.
2. Если `category_name` не указан, логирует предупреждение и завершает работу.
3. Пытается получить лист Google Sheets с именем `category_name`.
4. Формирует список обновлений для записи данных о продуктах в лист.
5. Выполняет пакетное обновление листа.
6. Логирует сообщение об успешной записи данных.
7. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
# Предположим, что self.campaign.category.TestCategory.products содержит данные о продуктах
gpt_gs.set_products_worksheet('TestCategory')
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ 
    Удаляет все листы из Google Sheets, кроме 'categories' и 'product_template'.
    """
    excluded_titles = {'categories', 'product', 'category', 'campaign'}
    try:
        worksheets = self.spreadsheet.worksheets()
        for sheet in worksheets:
            if sheet.title not in excluded_titles:
                self.spreadsheet.del_worksheet_by_id(sheet.id)
                logger.success(f"Worksheet \'{sheet.title}\' deleted.")
    except Exception as ex:
        logger.error("Error deleting all worksheets.", ex, exc_info=True)
        raise
```

**Назначение**: Удаление всех листов, кроме 'categories', 'product', 'category' и 'campaign'.

**Как работает функция**:

1. Определяет набор листов, которые не нужно удалять (`excluded_titles`).
2. Получает список всех листов в Google Sheets.
3. Итерируется по списку листов и удаляет каждый лист, если его имя не входит в `excluded_titles`.
4. Логирует сообщение об успешном удалении каждого листа.
5. В случае ошибки логирует сообщение об ошибке и пробрасывает исключение.

**Примеры**:

```python
gpt_gs.delete_products_worksheets()
```

### `save_categories_from_worksheet`

```python
def save_categories_from_worksheet(self, update:bool=False):
    """ Сохраняю данные, отредактированные в гугл таблице """

    edited_categories: list[dict] = self.get_categories_worksheet()
    _categories_ns:SimpleNamespace = SimpleNamespace()
    for _cat in edited_categories:
        _cat_ns: SimpleNamespace = SimpleNamespace(**{
            'name':_cat[0],
            'title':_cat[1],
            'description':_cat[2],
            'tags':_cat[3].split(","),
            'products_count':_cat[4],
        }
        )
        setattr(_categories_ns,_cat_ns.name,_cat_ns)
    ...
    self.campaign.category = _categories_ns
    if update: self.update_campaign()
```

**Назначение**: Сохранение данных категорий из Google Sheets в атрибут `category` объекта `campaign`.

**Как работает функция**:

1. Получает данные из листа 'categories' с помощью `self.get_categories_worksheet()`.
2. Итерируется по списку категорий и создает объекты `SimpleNamespace` для каждой категории.
3. Устанавливает атрибуты объекта `_categories_ns` с данными каждой категории.
4. Присваивает объект `_categories_ns` атрибуту `category` объекта `campaign`.
5. Если параметр `update` равен `True`, вызывает метод `self.update_campaign()` для обновления данных кампании.

**Примеры**:

```python
gpt_gs.save_categories_from_worksheet()
```

### `save_campaign_from_worksheet`

```python
def save_campaign_from_worksheet(self):
    """ Сохраняю реклманую каманию """
    self.save_categories_from_worksheet(False)
    data = self.get_campaign_worksheet()
    data.category = self.campaign.category
    self.campaign = data
    self.update_campaign()
    ...
```

**Назначение**: Сохранение данных рекламной кампании из Google Sheets, включая категории, и обновление объекта `campaign`.

**Как работает функция**:

1. Вызывает метод `self.save_categories_from_worksheet(False)` для сохранения данных категорий.
2. Получает данные кампании из листа 'campaign' с помощью `self.get_campaign_worksheet()`.
3. Присваивает атрибуту `category` объекта `data` значение `self.campaign.category`.
4. Присваивает объект `data` атрибуту `campaign` объекта `self`.
5. Вызывает метод `self.update_campaign()` для обновления данных кампании.

**Примеры**:

```python
gpt_gs.save_campaign_from_worksheet()