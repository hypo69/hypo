# Модуль `gsheet`

## Обзор

Модуль `gsheet` предназначен для управления Google Sheets в рамках AliExpress кампаний. Он предоставляет класс `GptGs`, который наследуется от `SpreadSheet` и `AliCampaignEditor` для управления Google Sheets, записи данных о категориях и продуктах, а также форматирования листов.

## Подробней

Этот модуль позволяет автоматизировать работу с Google Sheets для управления данными в кампаниях AliExpress. Он предоставляет методы для чтения и записи данных о категориях и продуктах, а также для создания и удаления листов. Модуль использует библиотеку `gspread` для взаимодействия с Google Sheets и модуль `logger` для логирования.

## Классы

### `GptGs`

**Описание**: Класс для управления Google Sheets в рамках AliExpress кампаний.

**Как работает класс**:
- Класс наследуется от `SpreadSheet` и `AliCampaignEditor`.
- Инициализируется с указанием ID Google Sheets таблицы.
- Предоставляет методы для очистки данных, обновления листов, чтения и записи данных о категориях и продуктах, а также для удаления листов.

**Методы**:
- `__init__`: Инициализирует класс `GptGs`.
- `clear`: Очищает содержимое Google Sheets.
- `update_chat_worksheet`: Записывает данные кампании в Google Sheets.
- `get_campaign_worksheet`: Читает данные кампании из Google Sheets.
- `set_category_worksheet`: Записывает данные категории в Google Sheets.
- `get_category_worksheet`: Читает данные категории из Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в Google Sheets.
- `get_categories_worksheet`: Читает данные о категориях из Google Sheets.
- `set_product_worksheet`: Записывает данные продукта в Google Sheets.
- `get_product_worksheet`: Читает данные продукта из Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в Google Sheets.
- `delete_products_worksheets`: Удаляет листы продуктов из Google Sheets.
- `save_categories_from_worksheet`: Сохраняет данные категорий из Google Sheets.
- `save_campaign_from_worksheet`: Сохраняет данные кампании из Google Sheets.

### `__init__`

```python
def __init__(self):
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
    # Initialize SpreadSheet with the spreadsheet ID
    super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
```

**Как работает функция**:
- Инициализирует класс `GptGs`, вызывая конструктор родительского класса `SpreadSheet` с указанием ID Google Sheets таблицы.

**Параметры**:
- Нет явных параметров, но конструктор родительского класса `SpreadSheet` принимает ID таблицы Google Sheets.

**Примеры**:
```python
gpt_gs = GptGs()
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    try:
        self.delete_products_worksheets()
        # ws_to_clear = ['category','categories','campaign']
        # for ws in self.spreadsheet.worksheets():
        #     self.get_worksheet(ws).clear()
            
    except Exception as ex:
        logger.error("Ошибка очистки",ex)
```

**Как работает функция**:
- Пытается удалить все листы продуктов из Google Sheets.
- В закомментированном коде предполагалась очистка листов `'category'`, `'categories'` и `'campaign'`.
- В случае ошибки логирует ее с использованием `logger.error`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при удалении листов продуктов.

**Примеры**:
```python
gpt_gs.clear()
```

### `update_chat_worksheet`

```python
def update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None):
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
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

**Как работает функция**:
- Записывает данные кампании в Google Sheets.
- Получает лист Google Sheets по имени `conversation_name`.
- Извлекает данные из объекта `SimpleNamespace` или словаря `data`.
- Подготавливает обновления для записи в Google Sheets.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Параметры**:
- `data` (SimpleNamespace | dict | list): Объект `SimpleNamespace`, словарь или список с данными кампании для записи.
- `conversation_name` (str): Имя листа Google Sheets для записи данных.
- `language` (str, optional): Необязательный параметр языка. По умолчанию `None`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных в Google Sheets.

**Примеры**:
```python
from types import SimpleNamespace
data = SimpleNamespace(name='test', title='Test', description='Test', tags=['test'], products_count=1)
gpt_gs.update_chat_worksheet(data, 'test')
```

### `get_campaign_worksheet`

```python
def get_campaign_worksheet(self) -> SimpleNamespace:
    """ Read campaign data from the 'campaign' worksheet.
    @return `SimpleNamespace`: SimpleNamespace object with campaign data fields.
    """
    try:
        ws: Worksheet = self.get_worksheet('campaign')
        if not ws:
            raise ValueError("Worksheet 'campaign' not found.")
        
        data = ws.get_all_values()
        campaign_data = SimpleNamespace(
            name=data[0][1],
            title=data[1][1],
            language=data[2][1],
            currency=data[3][1],
            description=data[4][1]
        )
        
        logger.info("Campaign data read from 'campaign' worksheet.")
        return campaign_data

    except Exception as ex:
        logger.error("Error getting campaign worksheet data.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Читает данные кампании из листа `'campaign'` Google Sheets.
- Получает лист Google Sheets по имени `'campaign'`.
- Извлекает данные из листа и создает объект `SimpleNamespace` с данными кампании.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными кампании.

**Вызывает исключения**:
- `ValueError`: Если лист `'campaign'` не найден.
- `Exception`: В случае ошибки при чтении данных из Google Sheets.

**Примеры**:
```python
campaign_data = gpt_gs.get_campaign_worksheet()
print(campaign_data.name)
```

### `set_category_worksheet`

```python
def set_category_worksheet(self, category: SimpleNamespace | str):
    """ Write data from a SimpleNamespace object to Google Sheets cells vertically.
    @param category `SimpleNamespace`: SimpleNamespace object with data fields for writing.
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

            logger.info("Category data written to 'category' worksheet vertically.")
        else:
            raise TypeError("Expected SimpleNamespace for category.")

    except Exception as ex:
        logger.error("Error setting category worksheet.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Записывает данные категории в лист `'category'` Google Sheets.
- Получает лист Google Sheets по имени `'category'`.
- Извлекает данные из объекта `SimpleNamespace` `category`.
- Подготавливает данные для вертикальной записи в Google Sheets.
- Записывает данные в Google Sheets.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Параметры**:
- `category` (SimpleNamespace | str): Объект `SimpleNamespace` с данными категории для записи.

**Вызывает исключения**:
- `TypeError`: Если `category` не является объектом `SimpleNamespace`.
- `Exception`: В случае ошибки при записи данных в Google Sheets.

**Примеры**:
```python
from types import SimpleNamespace
category = SimpleNamespace(name='test', title='Test', description='Test', tags=['test'], products_count=1)
gpt_gs.set_category_worksheet(category)
```

### `get_category_worksheet`

```python
def get_category_worksheet(self) -> SimpleNamespace:
    """ Read category data from the 'category' worksheet.
    @return `SimpleNamespace`: SimpleNamespace object with category data fields.
    """
    try:
        ws: Worksheet = self.get_worksheet('category')
        if not ws:
            raise ValueError("Worksheet 'category' not found.")
        
        data = ws.get_all_values()
        category_data = SimpleNamespace(
            name=data[1][1],
            title=data[2][1],
            description=data[3][1],
            tags=data[4][1].split(', '),
            products_count=int(data[5][1])
        )
        
        logger.info("Category data read from 'category' worksheet.")
        return category_data

    except Exception as ex:
        logger.error("Error getting category worksheet data.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Читает данные категории из листа `'category'` Google Sheets.
- Получает лист Google Sheets по имени `'category'`.
- Извлекает данные из листа и создает объект `SimpleNamespace` с данными категории.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными категории.

**Вызывает исключения**:
- `ValueError`: Если лист `'category'` не найден.
- `Exception`: В случае ошибки при чтении данных из Google Sheets.

**Примеры**:
```python
category_data = gpt_gs.get_category_worksheet()
print(category_data.name)
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Write data from a SimpleNamespace object to Google Sheets cells.
    @param categories `SimpleNamespace`: SimpleNamespace object with data fields for writing.
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
                logger.info(f"Category data written to 'categories' worksheet for {attr_name}.")
        
            # Move to the next row
            start_row += 1

    except Exception as ex:
        logger.error("Error setting categories worksheet.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Записывает данные о категориях в лист `'categories'` Google Sheets.
- Получает лист Google Sheets по имени `'categories'`.
- Итерируется по атрибутам объекта `categories`.
- Извлекает данные из каждого атрибута, который является объектом `SimpleNamespace`.
- Подготавливает обновления для записи в Google Sheets.
- Записывает данные в Google Sheets с использованием `batch_update`.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Параметры**:
- `categories` (SimpleNamespace): Объект `SimpleNamespace` с данными о категориях для записи.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных в Google Sheets.

**Примеры**:
```python
from types import SimpleNamespace
categories = SimpleNamespace(
    cat1=SimpleNamespace(name='test1', title='Test1', description='Test1', tags=['test1'], products_count=1),
    cat2=SimpleNamespace(name='test2', title='Test2', description='Test2', tags=['test2'], products_count=2)
)
gpt_gs.set_categories_worksheet(categories)
```

### `get_categories_worksheet`

```python
def get_categories_worksheet(self) -> List[List[str]]:
    """ Read data from columns A to E, starting from the second row, from the 'categories' worksheet.
    @return `List[List[str]]`: List of rows with data from columns A to E.
    """
    try:
        ws: Worksheet = self.get_worksheet('categories')
        if not ws:
            raise ValueError("Worksheet 'categories' not found.")
    
        # Read all values from the worksheet
        data = ws.get_all_values()
    
        # Extract data from columns A to E, starting from the second row
        data = [row[:5] for row in data[1:] if len(row) >= 5]  
    
        logger.info("Category data read from 'categories' worksheet.")
        return data

    except Exception as ex:
        logger.error("Error getting category data from worksheet.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Читает данные о категориях из листа `'categories'` Google Sheets.
- Получает лист Google Sheets по имени `'categories'`.
- Извлекает данные из столбцов A по E, начиная со второй строки.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Возвращает**:
- `List[List[str]]`: Список строк с данными о категориях.

**Вызывает исключения**:
- `ValueError`: Если лист `'categories'` не найден.
- `Exception`: В случае ошибки при чтении данных из Google Sheets.

**Примеры**:
```python
categories_data = gpt_gs.get_categories_worksheet()
print(categories_data)
```

### `set_product_worksheet`

```python
def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str):
    """ Write product data to a new Google Sheets spreadsheet.
    @param category_name Category name.
    @param product SimpleNamespace object with product data fields for writing.
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

**Как работает функция**:
- Записывает данные продукта в новый лист Google Sheets, копируя лист `'product_template'`.
- Копирует лист `'product_template'` и присваивает ему имя `category_name`.
- Записывает заголовки в первую строку листа.
- Извлекает данные из объекта `SimpleNamespace` `product`.
- Записывает данные продукта во вторую строку листа.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Параметры**:
- `product` (SimpleNamespace | str): Объект `SimpleNamespace` с данными продукта для записи.
- `category_name` (str): Имя категории продукта.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных в Google Sheets.

**Примеры**:
```python
from types import SimpleNamespace
product = SimpleNamespace(
    product_id='123', app_sale_price='10', original_price='20', sale_price='15', discount='5',
    product_main_image_url='http://example.com/image.jpg', local_image_path='/tmp/image.jpg',
    product_small_image_urls=['http://example.com/image1.jpg', 'http://example.com/image2.jpg'],
    product_video_url='http://example.com/video.mp4', local_video_path='/tmp/video.mp4',
    first_level_category_id='1', first_level_category_name='Category1',
    second_level_category_id='2', second_level_category_name='Category2',
    target_sale_price='12', target_sale_price_currency='USD', target_app_sale_price_currency='USD',
    target_original_price_currency='USD', original_price_currency='USD', product_title='Product Title',
    evaluate_rate='4.5', promotion_link='http://example.com/promotion', shop_url='http://example.com/shop',
    shop_id='456', tags=['tag1', 'tag2']
)
gpt_gs.set_product_worksheet(product, 'test_category')
```

### `get_product_worksheet`

```python
def get_product_worksheet(self) -> SimpleNamespace:
    """ Read product data from the 'products' worksheet.
    @return `SimpleNamespace`: SimpleNamespace object with product data fields.
    """
    try:
        ws: Worksheet = self.get_worksheet('products')
        if not ws:
            raise ValueError("Worksheet 'products' not found.")
        
        data = ws.get_all_values()
        product_data = SimpleNamespace(
            id=data[1][1],
            name=data[2][1],
            title=data[3][1],
            description=data[4][1],
            tags=data[5][1].split(', '),
            price=float(data[6][1])
        )
        
        logger.info("Product data read from 'products' worksheet.")
        return product_data

    except Exception as ex:
        logger.error("Error getting product worksheet data.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Читает данные продукта из листа `'products'` Google Sheets.
- Получает лист Google Sheets по имени `'products'`.
- Извлекает данные из листа и создает объект `SimpleNamespace` с данными продукта.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с данными продукта.

**Вызывает исключения**:
- `ValueError`: Если лист `'products'` не найден.
- `Exception`: В случае ошибки при чтении данных из Google Sheets.

**Примеры**:
```python
product_data = gpt_gs.get_product_worksheet()
print(product_data.name)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name:str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param ns_list `List[SimpleNamespace]`|`SimpleNamespace`: List of SimpleNamespace objects with data fields for writing.
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
        logger.info("Products data written to 'products' worksheet.")

    
    except Exception as ex:
        logger.error("Error setting products worksheet.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Записывает данные о продуктах в лист Google Sheets с именем `category_name`.
- Получает лист Google Sheets по имени `category_name`.
- Итерируется по списку объектов `SimpleNamespace` `products_ns`.
- Извлекает данные из каждого объекта `SimpleNamespace`.
- Подготавливает обновления для записи в Google Sheets.
- Записывает данные в Google Sheets с использованием `batch_update`.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Параметры**:
- `category_name` (str): Имя категории продукта.

**Вызывает исключения**:
- `Exception`: В случае ошибки при записи данных в Google Sheets.

**Примеры**:
```python
from types import SimpleNamespace
category_name = 'test_category'
gpt_gs.set_products_worksheet(category_name)
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
    excluded_titles = {'categories', 'product', 'category', 'campaign'}
    try:
        worksheets = self.spreadsheet.worksheets()
        for sheet in worksheets:
            if sheet.title not in excluded_titles:
                self.spreadsheet.del_worksheet_by_id(sheet.id)
                logger.success(f"Worksheet '{sheet.title}' deleted.")
    except Exception as ex:
        logger.error("Error deleting all worksheets.", ex, exc_info=True)
        raise
```

**Как работает функция**:
- Удаляет все листы из Google Sheets, кроме `'categories'`, `'product'`, `'category'` и `'campaign'`.
- Получает список всех листов в Google Sheets.
- Итерируется по списку листов и удаляет каждый лист, если его имя не входит в список исключений.
- В случае ошибки логирует ее с использованием `logger.error` и пробрасывает исключение выше.

**Вызывает исключения**:
- `Exception`: В случае ошибки при удалении листов из Google Sheets.

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

**Как работает функция**:
- Сохраняет данные категорий, отредактированные в Google Sheets.
- Получает данные категорий из Google Sheets с помощью `get_categories_worksheet`.
- Итерируется по списку категорий и создает объекты `SimpleNamespace` для каждой категории.
- Устанавливает атрибуты объекта `_categories_ns` с данными каждой категории.
- Если `update` равен `True`, вызывает метод `update_campaign`.

**Параметры**:
- `update` (bool, optional): Флаг, указывающий, нужно ли обновлять кампанию. По умолчанию `False`.

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

**Как работает функция**:
- Сохраняет данные рекламной кампании из Google Sheets.
- Вызывает метод `save_categories_from_worksheet` с параметром `False`.
- Получает данные кампании из Google Sheets с помощью `get_campaign_worksheet`.
- Устанавливает атрибут `category` объекта `data` равным `self.campaign.category`.
- Обновляет кампанию с помощью метода `update_campaign`.

**Примеры**:
```python
gpt_gs.save_campaign_from_worksheet()
```