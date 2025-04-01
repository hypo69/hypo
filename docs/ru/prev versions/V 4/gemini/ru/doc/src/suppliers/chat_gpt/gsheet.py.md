# Модуль `gsheet`

## Обзор

Модуль `gsheet` предназначен для управления Google Sheets в рамках AliExpress кампаний. Он предоставляет классы и методы для чтения, записи и обновления данных в Google Sheets, включая информацию о категориях, продуктах и параметрах кампании.

## Подробней

Модуль `gsheet` является частью системы для автоматизации работы с Google Sheets в контексте AliExpress кампаний. Он использует библиотеку `gspread` для взаимодействия с Google Sheets API и предоставляет удобные методы для выполнения таких задач, как:

- Чтение данных о кампаниях и категориях из Google Sheets.
- Запись данных о категориях и продуктах в Google Sheets.
- Создание и удаление листов Google Sheets.
- Очистка данных на листах Google Sheets.
- Обновление данных о категориях и кампаниях на основе информации из Google Sheets.

Этот модуль упрощает интеграцию данных из Google Sheets в процессы управления кампаниями AliExpress, обеспечивая централизованное хранение и управление информацией.

## Классы

### `GptGs`

**Описание**: Класс `GptGs` предназначен для управления Google Sheets в рамках AliExpress кампаний. Он наследуется от `SpreadSheet` и предоставляет методы для чтения, записи и обновления данных в Google Sheets.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `GptGs`.
- `clear`: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и кампании.
- `update_chat_worksheet`: Записывает данные кампании в Google Sheets.
- `get_campaign_worksheet`: Читает данные кампании из Google Sheets.
- `set_category_worksheet`: Записывает данные категории в Google Sheets.
- `get_category_worksheet`: Читает данные категории из Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в Google Sheets.
- `get_categories_worksheet`: Читает данные о категориях из Google Sheets.
- `set_product_worksheet`: Записывает данные о продукте в Google Sheets.
- `get_product_worksheet`: Читает данные о продукте из Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в Google Sheets.
- `delete_products_worksheets`: Удаляет листы продуктов из Google Sheets.
- `save_categories_from_worksheet`: Сохраняет данные о категориях из Google Sheets.
- `save_campaign_from_worksheet`: Сохраняет данные о кампании из Google Sheets.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `category_name` (str): Имя категории.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    gs.clear()
```

## Функции

### `__init__`

```python
def __init__(self):
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
```

**Описание**: Инициализирует экземпляр класса `GptGs` с указанным ID Google Sheets и дополнительными параметрами.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `category_name` (str): Имя категории.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
```

**Описание**: Очищает содержимое Google Sheets, удаляя листы продуктов и очищая данные на листах категорий и кампании.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при очистке Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    gs.clear()
```

### `update_chat_worksheet`

```python
def update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None):
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
```

**Описание**: Записывает данные кампании в Google Sheets.

**Параметры**:
- `data` (SimpleNamespace | dict | list): Объект SimpleNamespace или словарь с данными кампании для записи.
- `conversation_name` (str): Имя листа Google Sheets для записи данных.
- `language` (str, optional): Необязательный параметр языка.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных кампании в Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    from types import SimpleNamespace
    gs = GptGs()
    data = SimpleNamespace(name='Test Campaign', title='Test Title', description='Test Description', tags=['tag1', 'tag2'], products_count=100)
    gs.update_chat_worksheet(data, 'campaign')
```

### `get_campaign_worksheet`

```python
def get_campaign_worksheet(self) -> SimpleNamespace:
    """ Read campaign data from the 'campaign' worksheet.
    @return `SimpleNamespace`: SimpleNamespace object with campaign data fields.
    """
```

**Описание**: Читает данные кампании из листа 'campaign' в Google Sheets.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными кампании.

**Вызывает исключения**:
- `ValueError`: Если лист 'campaign' не найден.
- `Exception`: Если возникает ошибка при чтении данных кампании из Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    campaign_data = gs.get_campaign_worksheet()
    print(campaign_data.name)
```

### `set_category_worksheet`

```python
def set_category_worksheet(self, category: SimpleNamespace | str):
    """ Write data from a SimpleNamespace object to Google Sheets cells vertically.
    @param category `SimpleNamespace`: SimpleNamespace object with data fields for writing.
    """
```

**Описание**: Записывает данные категории в Google Sheets, используя вертикальную запись.

**Параметры**:
- `category` (SimpleNamespace | str): Объект SimpleNamespace с данными категории для записи.

**Вызывает исключения**:
- `TypeError`: Если `category` не является экземпляром `SimpleNamespace`.
- `Exception`: Если возникает ошибка при записи данных категории в Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    from types import SimpleNamespace
    gs = GptGs()
    category_data = SimpleNamespace(name='Test Category', title='Test Title', description='Test Description', tags=['tag1', 'tag2'], products_count=50)
    gs.set_category_worksheet(category_data)
```

### `get_category_worksheet`

```python
def get_category_worksheet(self) -> SimpleNamespace:
    """ Read category data from the 'category' worksheet.
    @return `SimpleNamespace`: SimpleNamespace object with category data fields.
    """
```

**Описание**: Читает данные категории из листа 'category' в Google Sheets.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными категории.

**Вызывает исключения**:
- `ValueError`: Если лист 'category' не найден.
- `Exception`: Если возникает ошибка при чтении данных категории из Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    category_data = gs.get_category_worksheet()
    print(category_data.name)
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Write data from a SimpleNamespace object to Google Sheets cells.
    @param categories `SimpleNamespace`: SimpleNamespace object with data fields for writing.
    """
```

**Описание**: Записывает данные о категориях в Google Sheets.

**Параметры**:
- `categories` (SimpleNamespace): Объект SimpleNamespace с данными о категориях для записи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о категориях в Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    from types import SimpleNamespace
    gs = GptGs()
    categories_data = SimpleNamespace(cat1=SimpleNamespace(name='Category 1', title='Title 1', description='Description 1', tags=['tag1'], products_count=10), 
                                     cat2=SimpleNamespace(name='Category 2', title='Title 2', description='Description 2', tags=['tag2'], products_count=20))
    gs.set_categories_worksheet(categories_data)
```

### `get_categories_worksheet`

```python
def get_categories_worksheet(self) -> List[List[str]]:
    """ Read data from columns A to E, starting from the second row, from the 'categories' worksheet.
    @return `List[List[str]]`: List of rows with data from columns A to E.
    """
```

**Описание**: Читает данные о категориях из листа 'categories' в Google Sheets.

**Возвращает**:
- `List[List[str]]`: Список строк с данными из столбцов A по E.

**Вызывает исключения**:
- `ValueError`: Если лист 'categories' не найден.
- `Exception`: Если возникает ошибка при чтении данных о категориях из Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    categories_data = gs.get_categories_worksheet()
    for row in categories_data:
        print(row)
```

### `set_product_worksheet`

```python
def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str):
    """ Write product data to a new Google Sheets spreadsheet.
    @param category_name Category name.
    @param product SimpleNamespace object with product data fields for writing.
    """
```

**Описание**: Записывает данные о продукте в Google Sheets.

**Параметры**:
- `product` (SimpleNamespace | str): Объект SimpleNamespace с данными о продукте для записи.
- `category_name` (str): Имя категории.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о продукте в Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    from types import SimpleNamespace
    gs = GptGs()
    product_data = SimpleNamespace(product_id=123, app_sale_price=10.0, original_price=15.0, sale_price=12.0, discount=20, 
                                  product_main_image_url='http://example.com/image.jpg', local_image_path='/path/to/image.jpg', 
                                  product_small_image_urls=['http://example.com/image1.jpg', 'http://example.com/image2.jpg'], 
                                  product_video_url='http://example.com/video.mp4', local_video_path='/path/to/video.mp4', 
                                  first_level_category_id=1, first_level_category_name='Category 1', second_level_category_id=2, 
                                  second_level_category_name='Category 2', target_sale_price=11.0, target_sale_price_currency='USD', 
                                  target_app_sale_price_currency='USD', target_original_price_currency='USD', original_price_currency='USD', 
                                  product_title='Test Product', evaluate_rate=4.5, promotion_link='http://example.com/promotion', 
                                  shop_url='http://example.com/shop', shop_id=12345, tags=['tag1', 'tag2'])
    gs.set_product_worksheet(product_data, 'TestCategory')
```

### `get_product_worksheet`

```python
def get_product_worksheet(self) -> SimpleNamespace:
    """ Read product data from the 'products' worksheet.
    @return `SimpleNamespace`: SimpleNamespace object with product data fields.
    """
```

**Описание**: Читает данные о продукте из листа 'products' в Google Sheets.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с данными о продукте.

**Вызывает исключения**:
- `ValueError`: Если лист 'products' не найден.
- `Exception`: Если возникает ошибка при чтении данных о продукте из Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    product_data = gs.get_product_worksheet()
    print(product_data.name)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name:str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param ns_list `List[SimpleNamespace]`|`SimpleNamespace`: List of SimpleNamespace objects with data fields for writing.
    """
```

**Описание**: Записывает данные о продуктах в Google Sheets.

**Параметры**:
- `category_name` (str): Имя категории.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи данных о продуктах в Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    from types import SimpleNamespace
    gs = GptGs()
    # Предположим, что self.campaign.category.TestCategory.products - это список объектов SimpleNamespace
    # product1 = SimpleNamespace(product_id=1, product_title='Product 1', title='Title 1', local_image_path='/path/1', product_video_url='http://example.com/video1', original_price=10.0, app_sale_price=8.0, target_sale_price=7.0)
    # product2 = SimpleNamespace(product_id=2, product_title='Product 2', title='Title 2', local_image_path='/path/2', product_video_url='http://example.com/video2', original_price=20.0, app_sale_price=16.0, target_sale_price=14.0)
    # self.campaign.category.TestCategory.products = [product1, product2]
    gs.set_products_worksheet('TestCategory')
```

### `delete_products_worksheets`

```python
def delete_products_worksheets(self):
    """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
    """
```

**Описание**: Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении листов.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    gs.delete_products_worksheets()
```

### `save_categories_from_worksheet`

```python
def save_categories_from_worksheet(self, update:bool=False):
    """ Сохраняю данные, отредактированные в гугл таблице """
```

**Описание**: Сохраняет данные о категориях из Google Sheets.

**Параметры**:
- `update` (bool, optional): Флаг, указывающий, нужно ли обновлять кампанию. По умолчанию `False`.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    gs.save_categories_from_worksheet()
```

### `save_campaign_from_worksheet`

```python
def save_campaign_from_worksheet(self):
    """ Сохраняю реклманую каманию """
```

**Описание**: Сохраняет данные о рекламной кампании из Google Sheets.

**Примеры**:
```python
    from src.suppliers.chat_gpt.gsheet import GptGs
    gs = GptGs()
    gs.save_campaign_from_worksheet()