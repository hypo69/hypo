# Модуль для работы с Google Sheets в кампаниях AliExpress
=============================================================

Модуль предоставляет класс `AliCampaignGoogleSheet` для управления данными в Google Sheets, связанными с рекламными кампаниями AliExpress. Он позволяет автоматизировать запись данных о категориях и продуктах, а также форматировать листы Google Sheets для удобного представления информации.

## Обзор

Этот модуль предназначен для упрощения работы с данными рекламных кампаний AliExpress, хранящимися в Google Sheets. Он предоставляет инструменты для автоматического создания и обновления листов с информацией о категориях и продуктах, а также для форматирования этих листов в соответствии с заданными стандартами. Модуль использует классы `SpreadSheet` для базовой работы с Google Sheets и `AliCampaignEditor` для управления данными кампаний AliExpress.

## Подробней

Модуль `gsheets_check_this_code.py` предназначен для автоматизации работы с Google Sheets в контексте управления рекламными кампаниями на AliExpress. Он обеспечивает создание, обновление и форматирование листов Google Sheets, содержащих информацию о кампаниях, категориях и продуктах.

Основные этапы работы модуля:

1.  **Инициализация**: Создается экземпляр класса `AliCampaignGoogleSheet`, который наследуется от `SpreadSheet`. При инициализации указывается название кампании, язык и валюта.
2.  **Очистка листов**: При инициализации происходит очистка существующих листов, связанных с продуктами, чтобы избежать устаревших данных.
3.  **Запись данных о кампании**: Данные о кампании (название, заголовок, язык, валюта, описание) записываются в лист Google Sheets под названием "campaign".
4.  **Запись данных о категориях**: Данные о категориях (название, заголовок, описание, теги, количество продуктов) записываются в лист Google Sheets под названием "categories".
5.  **Запись данных о продуктах**: Для каждой категории создается отдельный лист Google Sheets, в который записываются данные о продуктах этой категории (ID продукта, цена, изображения, описание и т.д.).
6.  **Форматирование листов**: Листы Google Sheets форматируются для удобства чтения и анализа данных (установка ширины столбцов, высоты строк, форматирование заголовков).

Модуль использует классы `SpreadSheet` для взаимодействия с Google Sheets API и `AliCampaignEditor` для получения данных о кампаниях, категориях и продуктах. Также используется модуль `logger` для логирования действий и ошибок.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets в рамках кампаний AliExpress.

**Наследует**:

*   `SpreadSheet`: Предоставляет базовые методы для работы с Google Sheets.

**Атрибуты**:

*   `spreadsheet_id` (str): Идентификатор Google Sheets таблицы.
*   `spreadsheet` (SpreadSheet): Экземпляр класса SpreadSheet для работы с таблицей.
*   `worksheet` (Worksheet): Экземпляр класса Worksheet для работы с листом таблицы.
*   `driver` (Driver): Экземпляр класса Driver для управления браузером. Используется `Chrome` в качестве браузера по умолчанию.
*   `editor` (AliCampaignEditor): Редактор кампании AliExpress.

**Методы**:

*   `__init__(campaign_name: str, language: str | dict = None, currency: str = None)`: Инициализирует класс `AliCampaignGoogleSheet`.
*   `clear()`: Очищает содержимое листов Google Sheets.
*   `delete_products_worksheets()`: Удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
*   `set_campaign_worksheet(campaign: SimpleNamespace)`: Записывает данные кампании в лист Google Sheets.
*   `set_products_worksheet(category_name: str)`: Записывает данные о продуктах категории в лист Google Sheets.
*   `set_categories_worksheet(categories: SimpleNamespace)`: Записывает данные о категориях в лист Google Sheets.
*   `get_categories()`: Получает данные о категориях из листа Google Sheets.
*   `set_category_products(category_name: str, products: dict)`: Записывает данные о продуктах категории в лист Google Sheets.
*   `_format_categories_worksheet(ws: Worksheet)`: Форматирует лист с категориями.
*   `_format_category_products_worksheet(ws: Worksheet)`: Форматирует лист с продуктами категории.

## Функции

### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
    # Initialize SpreadSheet with the spreadsheet ID
    super().__init__(spreadsheet_id=self.spreadsheet_id)
    self.editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
    self.clear()
    self.set_campaign_worksheet(self.editor.campaign)
    self.set_categories_worksheet(self.editor.campaign.category)
    self.driver.get_url(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')
```

**Назначение**: Инициализация экземпляра класса `AliCampaignGoogleSheet`.

**Параметры**:

*   `campaign_name` (str): Имя кампании.
*   `language` (str | dict, optional): Язык кампании. По умолчанию `None`.
*   `currency` (str, optional): Валюта кампании. По умолчанию `None`.

**Как работает функция**:

1.  Вызывает конструктор родительского класса `SpreadSheet`, передавая идентификатор таблицы Google Sheets (`self.spreadsheet_id`).
2.  Создает экземпляр класса `AliCampaignEditor`, передавая имя кампании, язык и валюту.
3.  Вызывает метод `clear()` для очистки существующих листов.
4.  Вызывает метод `set_campaign_worksheet()` для записи данных кампании в лист "campaign".
5.  Вызывает метод `set_categories_worksheet()` для записи данных о категориях в лист "categories".
6.  Открывает таблицу Google Sheets в браузере, используя URL, сформированный на основе `self.spreadsheet_id`.

**ASCII Flowchart**:

```
A: Инициализация AliCampaignGoogleSheet
|
B: Инициализация SpreadSheet
|
C: Инициализация AliCampaignEditor
|
D: Очистка листов (clear())
|
E: Запись данных кампании (set_campaign_worksheet())
|
F: Запись данных категорий (set_categories_worksheet())
|
G: Открытие таблицы в браузере (driver.get_url())
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale', language='en', currency='USD')
campaign_sheet = AliCampaignGoogleSheet(campaign_name='WinterDeals', language={'ru': 'Русский'}, currency='RUB')
```

### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    try:
        self.delete_products_worksheets()
    except Exception as ex:
        logger.error("Ошибка очистки", ex)
```

**Назначение**: Очистка содержимого Google Sheets, удаление листов продуктов и очистка данных на листах категорий и других указанных листах.

**Как работает функция**:

1.  Вызывает метод `delete_products_worksheets()` для удаления всех листов, связанных с продуктами.
2.  В случае возникновения исключения при удалении листов продуктов, логирует ошибку с помощью `logger.error()`.

**ASCII Flowchart**:

```
A: clear()
|
B: delete_products_worksheets()
|
C: Обработка исключений (если возникла ошибка при удалении листов)
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
campaign_sheet.clear()
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

**Назначение**: Удаление всех листов из Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.

**Как работает функция**:

1.  Определяет набор исключенных названий листов (`excluded_titles`).
2.  Получает список всех листов в таблице Google Sheets с помощью `self.spreadsheet.worksheets()`.
3.  Итерируется по списку листов и для каждого листа проверяет, входит ли его название в `excluded_titles`.
4.  Если название листа не входит в `excluded_titles`, удаляет лист с помощью `self.spreadsheet.del_worksheet_by_id(sheet.id)` и логирует успешное удаление.
5.  В случае возникновения исключения, логирует ошибку с помощью `logger.error()` и пробрасывает исключение дальше.

**ASCII Flowchart**:

```
A: delete_products_worksheets()
|
B: Получение списка листов (worksheets())
|
C: Итерация по листам
|
D: Проверка названия листа (sheet.title not in excluded_titles)
|
E: Удаление листа (del_worksheet_by_id())
|
F: Логирование успешного удаления
|
G: Обработка исключений
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
campaign_sheet.delete_products_worksheets()
```

### `set_campaign_worksheet`

```python
def set_campaign_worksheet(self, campaign: SimpleNamespace):
    """ Write campaign data to a Google Sheets worksheet.
    @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
    @param language `str`: Optional language parameter.
    @param currency `str`: Optional currency parameter.
    """
    try:
        ws: Worksheet = self.get_worksheet('campaign')  # Clear the 'campaign' worksheet

        # Prepare data for vertical writing
        updates = []
        vertical_data = [
            ('A1', 'Campaign Name', campaign.name),
            ('A2', 'Campaign Title', campaign.title),
            ('A3', 'Campaign Language', campaign.language),
            ('A4', 'Campaign Currency', campaign.currency),
            ('A5', 'Campaign Description', campaign.description),              
        ]

        # Add update operations to batch_update list
        for cell, header, value in vertical_data:
            updates.append({'range': cell, 'values': [[header]]})
            updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})

        # Perform batch update
        if updates:
            ws.batch_update(updates)

        logger.info("Campaign data written to 'campaign' worksheet vertically.")

    except Exception as ex:
        logger.error("Error setting campaign worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных кампании в лист Google Sheets.

**Параметры**:

*   `campaign` (SimpleNamespace): Объект SimpleNamespace с данными кампании.

**Как работает функция**:

1.  Получает лист Google Sheets с названием 'campaign' с помощью `self.get_worksheet('campaign')`.
2.  Подготавливает данные для записи в вертикальном формате в виде списка кортежей `vertical_data`. Каждый кортеж содержит ячейку, заголовок и значение.
3.  Итерируется по списку `vertical_data` и формирует список операций обновления `updates` для метода `batch_update`.
4.  Вызывает метод `ws.batch_update(updates)` для выполнения пакетного обновления ячеек в листе Google Sheets.
5.  Логирует успешную запись данных кампании.
6.  В случае возникновения исключения, логирует ошибку с помощью `logger.error()` и пробрасывает исключение дальше.

**ASCII Flowchart**:

```
A: set_campaign_worksheet()
|
B: Получение листа 'campaign' (get_worksheet())
|
C: Подготовка данных для записи (vertical_data)
|
D: Формирование списка операций обновления (updates)
|
E: Пакетное обновление ячеек (batch_update())
|
F: Логирование успешной записи
|
G: Обработка исключений
```

**Примеры**:

```python
from types import SimpleNamespace
campaign_data = SimpleNamespace(
    name='SummerSale',
    title='Летняя распродажа',
    language='ru',
    currency='RUB',
    description='Большая летняя распродажа!'
)
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
campaign_sheet.set_campaign_worksheet(campaign_data)
```

### `set_products_worksheet`

```python
def set_products_worksheet(self, category_name: str):
    """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
    @param category_name `str`: The name of the category to fetch products from.
    """
    if category_name:
        category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
        products: list[SimpleNamespace] = category.products
    else:
        logger.warning("No products found for category.")
        return

    ws = self.copy_worksheet('product', category_name)

    try:
        # headers = [
        #     'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
        #     'product_main_image_url', 'local_image_path', 'product_small_image_urls',
        #     'product_video_url', 'local_video_path', 'first_level_category_id',
        #     'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
        #     'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
        #     'target_original_price_currency', 'original_price_currency', 'product_title',
        #     'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
        # ]
        # updates = [{'range': 'A1:Y1', 'values': [headers]}]  # Add headers to the worksheet

        row_data = []
        for product in products:
            _ = product.__dict__
            row_data.append([
                str(_.get('product_id')),
                _.get('product_title'),
                _.get('promotion_link'),
                str(_.get('app_sale_price')),
                _.get('original_price'),
                _.get('sale_price'),
                _.get('discount'),
                _.get('product_main_image_url'),
                _.get('local_image_path'),
                ', '.join(_.get('product_small_image_urls', [])),
                _.get('product_video_url'),
                _.get('local_video_path'),
                _.get('first_level_category_id'),
                _.get('first_level_category_name'),
                _.get('second_level_category_id'),
                _.get('second_level_category_name'),
                _.get('target_sale_price'),
                _.get('target_sale_price_currency'),
                _.get('target_app_sale_price_currency'),
                _.get('target_original_price_currency'),
                _.get('original_price_currency'),

                _.get('evaluate_rate'),

                _.get('shop_url'),
                _.get('shop_id'),
                ', '.join(_.get('tags', []))
            ])

        for index, row in enumerate(row_data, start=2):
            ws.update(f'A{index}:Y{index}', [row])
            logger.info(f"Products {str(_.get('product_id'))} updated .")

        self._format_category_products_worksheet(ws)

        logger.info("Products updated in worksheet.")


    except Exception as ex:
        logger.error("Error setting products worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных о продуктах из списка объектов SimpleNamespace в ячейки Google Sheets.

**Параметры**:

*   `category_name` (str): Название категории, из которой нужно получить продукты.

**Как работает функция**:

1.  Проверяет, передано ли название категории. Если нет, логирует предупреждение и выходит из функции.
2.  Получает объект категории и список продуктов из `self.editor.campaign.category` по названию категории.
3.  Копирует лист 'product' и переименовывает его в название категории с помощью `self.copy_worksheet('product', category_name)`.
4.  Формирует список `row_data`, содержащий данные о каждом продукте в виде списка строк.
5.  Итерируется по списку `row_data` и записывает данные о каждом продукте в соответствующую строку листа Google Sheets с помощью `ws.update()`.
6.  Вызывает метод `self._format_category_products_worksheet(ws)` для форматирования листа.
7.  Логирует успешное обновление продуктов.
8.  В случае возникновения исключения, логирует ошибку с помощью `logger.error()` и пробрасывает исключение дальше.

**ASCII Flowchart**:

```
A: set_products_worksheet()
|
B: Проверка наличия названия категории
|
C: Получение объекта категории и списка продуктов
|
D: Копирование листа 'product'
|
E: Формирование списка row_data
|
F: Итерация по row_data и запись данных в лист
|
G: Форматирование листа (_format_category_products_worksheet())
|
H: Логирование успешного обновления
|
I: Обработка исключений
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
campaign_sheet.set_products_worksheet(category_name='shoes')
```

### `set_categories_worksheet`

```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
    @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
    """
    ws: Worksheet = self.get_worksheet('categories')
    ws.clear()  # Очистка рабочей таблицы перед записью данных

    try:
        # Получение всех ключей (категорий) и соответствующих значений
        category_data = categories.__dict__

        # Проверка, что все объекты категории имеют необходимые атрибуты
        required_attrs = ['name', 'title', 'description', 'tags', 'products_count']

        if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values()):
            # Заголовки для таблицы
            headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
            ws.update('A1:E1', [headers])

            # Подготовка данных для записи
            rows = []
            for category in category_data.values():
                row_data = [
                    category.name,
                    category.title,
                    category.description,
                    ', '.join(category.tags),
                    category.products_count,
                ]
                rows.append(row_data)

            # Обновляем строки данных
            ws.update(f'A2:E{1 + len(rows)}', rows)

            # Форматируем таблицу
            self._format_categories_worksheet(ws)

            logger.info("Category fields updated from SimpleNamespace object.")
        else:
            logger.warning("One or more category objects do not contain all required attributes.")

    except Exception as ex:
        logger.error("Error updating fields from SimpleNamespace object.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных о категориях из объекта SimpleNamespace в ячейки Google Sheets.

**Параметры**:

*   `categories` (SimpleNamespace): Объект, где ключи — это категории с данными для записи.

**Как работает функция**:

1.  Получает лист Google Sheets с названием 'categories' с помощью `self.get_worksheet('categories')`.
2.  Очищает лист с помощью `ws.clear()`.
3.  Получает данные о категориях из объекта `categories` в виде словаря `category_data`.
4.  Проверяет, что все объекты категории имеют необходимые атрибуты (name, title, description, tags, products\_count).
5.  Если все объекты категории имеют необходимые атрибуты, записывает заголовки таблицы (Name, Title, Description, Tags, Products Count) в первую строку листа.
6.  Формирует список `rows`, содержащий данные о каждой категории в виде списка строк.
7.  Записывает данные о категориях в лист Google Sheets с помощью `ws.update()`.
8.  Вызывает метод `self._format_categories_worksheet(ws)` для форматирования листа.
9.  Логирует успешное обновление полей категорий.
10. Если не все объекты категории имеют необходимые атрибуты, логирует предупреждение.
11. В случае возникновения исключения, логирует ошибку с помощью `logger.error()` и пробрасывает исключение дальше.

**ASCII Flowchart**:

```
A: set_categories_worksheet()
|
B: Получение листа 'categories' (get_worksheet())
|
C: Очистка листа (ws.clear())
|
D: Получение данных о категориях (category_data)
|
E: Проверка наличия необходимых атрибутов
|
F: Запись заголовков таблицы
|
G: Формирование списка rows
|
H: Запись данных о категориях в лист
|
I: Форматирование листа (_format_categories_worksheet())
|
J: Логирование успешного обновления
|
K: Логирование предупреждения (если не все атрибуты присутствуют)
|
L: Обработка исключений
```

**Примеры**:

```python
from types import SimpleNamespace
categories_data = SimpleNamespace(
    shoes=SimpleNamespace(
        name='shoes',
        title='Обувь',
        description='Различная обувь для всех случаев жизни',
        tags=['обувь', 'ботинки', 'кроссовки'],
        products_count=100
    ),
    clothes=SimpleNamespace(
        name='clothes',
        title='Одежда',
        description='Различная одежда для всех случаев жизни',
        tags=['одежда', 'брюки', 'рубашки'],
        products_count=200
    )
)
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
campaign_sheet.set_categories_worksheet(categories_data)
```

### `get_categories`

```python
def get_categories(self):
    """ Получение данных из таблицы Google Sheets.
    @return Данные из таблицы в виде списка словарей.
    """
    ws = self.get_worksheet('categories') 
    data = ws.get_all_records()
    logger.info("Categories data retrieved from worksheet.")
    return data
```

**Назначение**: Получение данных о категориях из таблицы Google Sheets.

**Возвращает**:

*   `list[dict]`: Данные из таблицы в виде списка словарей, где каждый словарь представляет собой строку таблицы.

**Как работает функция**:

1.  Получает лист Google Sheets с названием 'categories' с помощью `self.get_worksheet('categories')`.
2.  Получает все записи из листа с помощью `ws.get_all_records()`.
3.  Логирует успешное получение данных о категориях.
4.  Возвращает полученные данные.

**ASCII Flowchart**:

```
A: get_categories()
|
B: Получение листа 'categories' (get_worksheet())
|
C: Получение всех записей (get_all_records())
|
D: Логирование успешного получения данных
|
E: Возврат данных
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
categories = campaign_sheet.get_categories()
print(categories)
```

### `set_category_products`

```python
def set_category_products(self, category_name: str, products: dict):
    """ Запись данных о продуктах в новую таблицу Google Sheets.
    @param category_name Название категории.
    @param products Словарь с данными о продуктах.
    """
    if category_name:
        category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
        products_ns: list[SimpleNamespace] = category_ns.products
    else:
        logger.warning("No products found for category.")
        return

    ws = self.copy_worksheet('product', category_name)
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
        updates = [{'range': 'A1:Y1', 'values': [headers]}]  # Add headers to the worksheet

        row_data = []
        for product in products:
            _ = product.__dict__
            row_data.append([
                str(_.get('product_id')),
                str(_.get('app_sale_price')),
                _.get('original_price'),
                _.get('sale_price'),
                _.get('discount'),
                _.get('product_main_image_url'),
                _.get('local_image_path'),
                ', '.join(_.get('product_small_image_urls', [])),
                _.get('product_video_url'),
                _.get('local_video_path'),
                _.get('first_level_category_id'),
                _.get('first_level_category_name'),
                _.get('second_level_category_id'),
                _.get('second_level_category_name'),
                _.get('target_sale_price'),
                _.get('target_sale_price_currency'),
                _.get('target_app_sale_price_currency'),
                _.get('target_original_price_currency'),
                _.get('original_price_currency'),
                _.get('product_title'),
                _.get('evaluate_rate'),
                _.get('promotion_link'),
                _.get('shop_url'),
                _.get('shop_id'),
                ', '.join(_.get('tags', []))
            ])

        for index, row in enumerate(row_data, start=2):
            ws.update(f'A{index}:Y{index}', [row])
            logger.info(f"Products {str(_.get('product_id'))} updated .")

        self._format_category_products_worksheet(ws)

        logger.info("Products updated in worksheet.")
    except Exception as ex:
        logger.error("Error updating products in worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Запись данных о продуктах в новую таблицу Google Sheets.

**Параметры**:

*   `category_name` (str): Название категории.
*   `products` (dict): Словарь с данными о продуктах.

**Как работает функция**:

1.  Проверяет, передано ли название категории. Если нет, логирует предупреждение и выходит из функции.
2.  Получает объект категории и список продуктов из `self.editor.campaign.category` по названию категории.
3.  Копирует лист 'product' и переименовывает его в название категории с помощью `self.copy_worksheet('product', category_name)`.
4.  Определяет заголовки таблицы `headers`.
5.  Формирует список `row_data`, содержащий данные о каждом продукте в виде списка строк.
6.  Итерируется по списку `row_data` и записывает данные о каждом продукте в соответствующую строку листа Google Sheets с помощью `ws.update()`.
7.  Вызывает метод `self._format_category_products_worksheet(ws)` для форматирования листа.
8.  Логирует успешное обновление продуктов.
9.  В случае возникновения исключения, логирует ошибку с помощью `logger.error()` и пробрасывает исключение дальше.

**ASCII Flowchart**:

```
A: set_category_products()
|
B: Проверка наличия названия категории
|
C: Получение объекта категории и списка продуктов
|
D: Копирование листа 'product'
|
E: Определение заголовков таблицы (headers)
|
F: Формирование списка row_data
|
G: Итерация по row_data и запись данных в лист
|
H: Форматирование листа (_format_category_products_worksheet())
|
I: Логирование успешного обновления
|
J: Обработка исключений
```

**Примеры**:

```python
products_data = [
    {'product_id': '123', 'app_sale_price': '10.00', 'original_price': '20.00', 'sale_price': '15.00', 'discount': '50%', 'product_title': 'Кроссовки'},
    {'product_id': '456', 'app_sale_price': '20.00', 'original_price': '40.00', 'sale_price': '30.00', 'discount': '50%', 'product_title': 'Ботинки'}
]
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
campaign_sheet.set_category_products(category_name='shoes', products=products_data)
```

### `_format_categories_worksheet`

```python
def _format_categories_worksheet(self, ws: Worksheet):
    """ Форматирование листа 'categories'.
    @param ws Лист Google Sheets для форматирования.
    """
    try:
        # Установка ширины столбцов
        set_column_width(ws, 'A:A', 150)  # Ширина столбца A
        set_column_width(ws, 'B:B', 200)  # Ширина столбца B
        set_column_width(ws, 'C:C', 300)  # Ширина столбца C
        set_column_width(ws, 'D:D', 200)  # Ширина столбца D
        set_column_width(ws, 'E:E', 150)  # Ширина столбца E

        # Установка высоты строк
        set_row_height(ws, '1:1', 40)  # Высота заголовков

        # Форматирование заголовков
        header_format = cellFormat(
            textFormat=textFormat(bold=True, fontSize=12),
            horizontalAlignment='CENTER',
            verticalAlignment='MIDDLE',  # Добавлено вертикальное выравнивание
            backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
        )
        format_cell_range(ws, 'A1:E1', header_format)

        logger.info("Categories worksheet formatted.")
    except Exception as ex:
        logger.error("Error formatting categories worksheet.", ex, exc_info=True)
        raise
```

**Назначение**: Форматирование листа 'categories' в Google Sheets.

**Параметры**:

*   `ws` (Worksheet): Лист Google Sheets для форматирования.

**Как работает функция**:

1.  Устанавливает ширину столбцов A, B, C, D и E с помощью `set_column_width()`.
2.  Устанавливает высоту первой строки (заголовков) с помощью `set_row_height()`.
3.  Определяет формат заголовков с использованием `cellFormat`, `textFormat` и `Color`.
4.  Применяет формат заголовков к диапазону ячеек A1:E1 с помощью `format_cell_range()`.
5.  Логирует успешное форматирование листа категорий.
6.  В случае возникновения исключения, логирует ошибку с помощью `logger.error()` и пробрасывает исключение дальше.

**ASCII Flowchart**:

```
A: _format_categories_worksheet()
|
B: Установка ширины столбцов
|
C: Установка высоты строки заголовков
|
D: Определение формата заголовков
|
E: Применение формата к диапазону ячеек
|
F: Логирование успешного форматирования
|
G: Обработка исключений
```

**Примеры**:

```python
campaign_sheet = AliCampaignGoogleSheet(campaign_name='SummerSale')
ws = campaign_sheet.get_worksheet('categories')
campaign_sheet._format_categories_worksheet(ws)
```

### `_format_category_products_worksheet`

```python
def _format_category_products_worksheet(self, ws: Worksheet):
    """ Форматирование листа с продуктами категории.
    @param ws Лист