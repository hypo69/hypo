# Модуль для работы с Google Sheets в кампаниях AliExpress

## Обзор

Модуль `gsheet.py` предназначен для управления Google Sheets в рамках кампаний AliExpress. Он предоставляет классы и методы для чтения, записи и управления данными кампаний, категорий и продуктов в Google Sheets.

## Подробнее

Этот модуль является частью проекта `hypotez` и используется для автоматизации работы с Google Sheets при управлении кампаниями AliExpress. Он позволяет считывать данные о кампаниях, категориях и продуктах из Google Sheets, а также записывать обновленные данные обратно в таблицы.

## Классы

### `GptGs`

**Описание**: Класс `GptGs` предназначен для управления Google Sheets в кампаниях AliExpress.

**Наследует**:
- `SpreadSheet`: Управляет Google Sheets.

**Методы**:
- `__init__`: Инициализирует класс `GptGs`.
- `clear`: Очищает содержимое Google Sheets.
- `update_chat_worksheet`: Записывает данные кампании в Google Sheets.
- `get_campaign_worksheet`: Считывает данные кампании из Google Sheets.
- `set_category_worksheet`: Записывает данные категории в Google Sheets.
- `get_category_worksheet`: Считывает данные категории из Google Sheets.
- `set_categories_worksheet`: Записывает данные о категориях в Google Sheets.
- `get_categories_worksheet`: Считывает данные о категориях из Google Sheets.
- `set_product_worksheet`: Записывает данные продукта в Google Sheets.
- `get_product_worksheet`: Считывает данные продукта из Google Sheets.
- `set_products_worksheet`: Записывает данные о продуктах в Google Sheets.
- `delete_products_worksheets`: Удаляет листы продуктов из Google Sheets.
- `save_categories_from_worksheet`: Сохраняет данные категорий из Google Sheets.
- `save_campaign_from_worksheet`: Сохраняет данные кампании из Google Sheets.

### `__init__`
```python
def __init__(self):
    """ Инициализирует AliCampaignGoogleSheet с указанным ID Google Sheets и дополнительными параметрами.
    Args:
        campaign_name (str): Название кампании.
        category_name (str): Название категории.
        language (str): Язык для кампании.
        currency (str): Валюта для кампании.
    """
```
**Как работает функция**:
1. Вызывает конструктор родительского класса `SpreadSheet` с ID таблицы Google Sheets `'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'`.
2.  Инициализирует экземпляр класса `SpreadSheet` с переданным ID.

### `clear`
```python
def clear(self):
    """ Очищает содержимое Google Sheets.
    Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
    """
```
**Как работает функция**:
1. Вызывает метод `self.delete_products_worksheets()` для удаления листов продуктов.
2. Пытается выполнить очистку указанных листов (закомментировано в коде).
3. В случае возникновения ошибки логирует её с помощью `logger.error`.
```
A --> B
|     |
Удаление продуктов  ---> Обработка исключений
```
**Пример**:
```python
gpt_gs = GptGs()
gpt_gs.clear()
```

### `update_chat_worksheet`
```python
def update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None):
    """ Записывает данные кампании в Google Sheets.
    Args:
        data (SimpleNamespace | dict | list): Объект SimpleNamespace с полями данных кампании для записи.
        conversation_name (str): Имя рабочего листа.
        language (str, optional): Необязательный параметр языка. По умолчанию `None`.
    Raises:
        Exception: Если возникает ошибка при записи данных кампании в рабочий лист.
    """
```
**Как работает функция**:
1. Пытается получить рабочий лист Google Sheets по имени `conversation_name` с помощью `self.get_worksheet(conversation_name)`.
2. Извлекает данные из объекта `SimpleNamespace` или `dict`.
3. Подготавливает данные для записи в ячейки рабочего листа.
4. Выполняет пакетное обновление рабочего листа с использованием `ws.batch_update(updates)`.
5. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E
|     |     |     |     |
Получение данных  ---> Извлечение данных  ---> Подготовка обновления  ---> Пакетное обновление  ---> Обработка исключений
```

**Пример**:
```python
from types import SimpleNamespace
gpt_gs = GptGs()
data = SimpleNamespace(name='Test Campaign', title='Test Title', description='Test Description', tags=['tag1', 'tag2'], products_count=10)
gpt_gs.update_chat_worksheet(data, 'campaign')
```

### `get_campaign_worksheet`
```python
def get_campaign_worksheet(self) -> SimpleNamespace:
    """ Считывает данные кампании из рабочего листа \'campaign\'.
    Returns:
        SimpleNamespace: Объект SimpleNamespace с полями данных кампании.
    Raises:
        ValueError: Если рабочий лист \'campaign\' не найден.
        Exception: Если возникает ошибка при получении данных из рабочего листа кампании.
    """
```

**Как работает функция**:
1. Пытается получить рабочий лист Google Sheets по имени `campaign` с помощью `self.get_worksheet('campaign')`.
2. Проверяет, найден ли рабочий лист. Если нет, вызывает исключение `ValueError`.
3. Считывает все значения из рабочего листа с помощью `ws.get_all_values()`.
4. Создает объект `SimpleNamespace` и заполняет его данными из рабочего листа.
5. Логирует информацию об успешном чтении данных кампании с помощью `logger.info`.
6. Возвращает объект `SimpleNamespace` с данными кампании.
7. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Получение рабочего листа  ---> Проверка наличия  ---> Чтение данных  ---> Создание объекта SimpleNamespace  ---> Логирование  ---> Обработка исключений
```

**Пример**:
```python
gpt_gs = GptGs()
campaign_data = gpt_gs.get_campaign_worksheet()
print(campaign_data.name)
```

### `set_category_worksheet`
```python
def set_category_worksheet(self, category: SimpleNamespace | str):
    """ Записывает данные из объекта SimpleNamespace в ячейки Google Sheets по вертикали.
    Args:
        category (SimpleNamespace | str): Объект SimpleNamespace с полями данных для записи.
    Raises:
        TypeError: Если передан не SimpleNamespace для category.
        Exception: Если возникает ошибка при установке рабочего листа категории.
    """
```

**Как работает функция**:
1. Проверяет, является ли `category` объектом `SimpleNamespace`. Если нет, пытается получить категорию с помощью `self.get_campaign_category(category)`.
2. Пытается получить рабочий лист Google Sheets по имени `category` с помощью `self.get_worksheet('category')`.
3. Если `category` является объектом `SimpleNamespace`, подготавливает данные для вертикальной записи в ячейки рабочего листа.
4. Выполняет обновление ячеек рабочего листа с использованием `ws.update('A1:B{}'.format(len(vertical_data)), vertical_data)`.
5. Логирует информацию об успешной записи данных категории с помощью `logger.info`.
6. Если `category` не является объектом `SimpleNamespace`, вызывает исключение `TypeError`.
7. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Проверка типа  ---> Получение рабочего листа  ---> Подготовка данных  ---> Обновление ячеек  ---> Логирование  ---> Обработка исключений
```

**Пример**:
```python
from types import SimpleNamespace
gpt_gs = GptGs()
category_data = SimpleNamespace(name='Test Category', title='Test Title', description='Test Description', tags=['tag1', 'tag2'], products_count=10)
gpt_gs.set_category_worksheet(category_data)
```

### `get_category_worksheet`
```python
def get_category_worksheet(self) -> SimpleNamespace:
    """ Считывает данные категории из рабочего листа \'category\'.
    Returns:
        SimpleNamespace: Объект SimpleNamespace с полями данных категории.
    Raises:
        ValueError: Если рабочий лист \'category\' не найден.
        Exception: Если возникает ошибка при получении данных из рабочего листа категории.
    """
```

**Как работает функция**:
1. Пытается получить рабочий лист Google Sheets по имени `category` с помощью `self.get_worksheet('category')`.
2. Проверяет, найден ли рабочий лист. Если нет, вызывает исключение `ValueError`.
3. Считывает все значения из рабочего листа с помощью `ws.get_all_values()`.
4. Создает объект `SimpleNamespace` и заполняет его данными из рабочего листа.
5. Логирует информацию об успешном чтении данных категории с помощью `logger.info`.
6. Возвращает объект `SimpleNamespace` с данными категории.
7. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Получение рабочего листа  ---> Проверка наличия  ---> Чтение данных  ---> Создание объекта SimpleNamespace  ---> Логирование  ---> Обработка исключений
```

**Пример**:
```python
gpt_gs = GptGs()
category_data = gpt_gs.get_category_worksheet()
print(category_data.name)
```

### `set_categories_worksheet`
```python
def set_categories_worksheet(self, categories: SimpleNamespace):
    """ Записывает данные из объекта SimpleNamespace в ячейки Google Sheets.
    Args:
        categories (SimpleNamespace): Объект SimpleNamespace с полями данных для записи.
    Raises:
        Exception: Если возникает ошибка при установке рабочего листа категорий.
    """
```

**Как работает функция**:
1. Получает рабочий лист Google Sheets по имени `categories` с помощью `self.get_worksheet('categories')`.
2. Инициализирует начальную строку для записи данных (`start_row = 2`).
3. Перебирает все атрибуты объекта `categories` с помощью `dir(categories)`.
4. Проверяет, является ли атрибут объектом `SimpleNamespace` и содержит ли он необходимые поля (`name`, `title`, `description`, `tags`, `products_count`).
5. Извлекает данные из объекта `SimpleNamespace` и подготавливает их для записи в ячейки рабочего листа.
6. Выполняет пакетное обновление рабочего листа с использованием `ws.batch_update(updates)`.
7. Логирует информацию об успешной записи данных категории с помощью `logger.info`.
8. Увеличивает номер начальной строки (`start_row += 1`).
9. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F --> G
|     |     |     |     |     |     |
Получение рабочего листа  ---> Инициализация строки  ---> Перебор атрибутов  ---> Проверка атрибута  ---> Извлечение данных  ---> Обновление ячеек  ---> Обработка исключений
```

**Пример**:
```python
from types import SimpleNamespace
gpt_gs = GptGs()
categories_data = SimpleNamespace(
    cat1=SimpleNamespace(name='Category 1', title='Title 1', description='Description 1', tags=['tag1', 'tag2'], products_count=10),
    cat2=SimpleNamespace(name='Category 2', title='Title 2', description='Description 2', tags=['tag3', 'tag4'], products_count=20)
)
gpt_gs.set_categories_worksheet(categories_data)
```

### `get_categories_worksheet`
```python
def get_categories_worksheet(self) -> List[List[str]]:
    """ Считывает данные из столбцов A-E, начиная со второй строки, из рабочего листа \'categories\'.
    Returns:
        List[List[str]]: Список строк с данными из столбцов A-E.
    Raises:
        ValueError: Если рабочий лист \'categories\' не найден.
        Exception: Если возникает ошибка при получении данных категории из рабочего листа.
    """
```

**Как работает функция**:
1. Пытается получить рабочий лист Google Sheets по имени `categories` с помощью `self.get_worksheet('categories')`.
2. Проверяет, найден ли рабочий лист. Если нет, вызывает исключение `ValueError`.
3. Считывает все значения из рабочего листа с помощью `ws.get_all_values()`.
4. Извлекает данные из столбцов A-E, начиная со второй строки.
5. Логирует информацию об успешном чтении данных категории с помощью `logger.info`.
6. Возвращает список строк с данными из столбцов A-E.
7. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Получение рабочего листа  ---> Проверка наличия  ---> Чтение данных  ---> Извлечение данных  ---> Логирование  ---> Обработка исключений
```

**Пример**:
```python
gpt_gs = GptGs()
categories_data = gpt_gs.get_categories_worksheet()
print(categories_data)
```

### `set_product_worksheet`
```python
def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str):
    """ Записывает данные продукта в новый Google Sheets.
    Args:
        category_name (str): Название категории.
        product (SimpleNamespace): Объект SimpleNamespace с полями данных продукта для записи.
    Raises:
        Exception: Если возникает ошибка при обновлении данных продукта в рабочем листе.
    """
```

**Как работает функция**:
1. Делает паузу в 10 секунд с помощью `time.sleep(10)`.
2. Копирует рабочий лист `product_template` и присваивает ему имя `category_name` с помощью `self.copy_worksheet('product_template', category_name)`.
3. Записывает заголовки столбцов в первую строку рабочего листа.
4. Извлекает данные из объекта `SimpleNamespace` и подготавливает их для записи во вторую строку рабочего листа.
5. Выполняет обновление ячеек рабочего листа с использованием `ws.update('A2:Y2', [row_data])`.
6. Логирует информацию об успешной записи данных продукта с помощью `logger.info`.
7. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Пауза  ---> Копирование шаблона  ---> Запись заголовков  ---> Извлечение данных  ---> Обновление ячеек  ---> Обработка исключений
```

**Пример**:
```python
from types import SimpleNamespace
gpt_gs = GptGs()
product_data = SimpleNamespace(product_id=123, app_sale_price=10.0, original_price=15.0, sale_price=12.0, discount=0.2, product_main_image_url='http://example.com/image.jpg', local_image_path='/path/to/image.jpg', product_small_image_urls=['http://example.com/image1.jpg', 'http://example.com/image2.jpg'], product_video_url='http://example.com/video.mp4', local_video_path='/path/to/video.mp4', first_level_category_id=1, first_level_category_name='Category 1', second_level_category_id=2, second_level_category_name='Category 2', target_sale_price=11.0, target_sale_price_currency='USD', target_app_sale_price_currency='USD', target_original_price_currency='USD', original_price_currency='USD', product_title='Test Product', evaluate_rate=4.5, promotion_link='http://example.com/promotion', shop_url='http://example.com/shop', shop_id=1, tags=['tag1', 'tag2'])
gpt_gs.set_product_worksheet(product_data, 'Test Category')
```

### `get_product_worksheet`
```python
def get_product_worksheet(self) -> SimpleNamespace:
    """ Считывает данные продукта из рабочего листа \'products\'.
    Returns:
        SimpleNamespace: Объект SimpleNamespace с полями данных продукта.
    Raises:
        ValueError: Если рабочий лист \'products\' не найден.
        Exception: Если возникает ошибка при получении данных из рабочего листа продукта.
    """
```

**Как работает функция**:
1. Пытается получить рабочий лист Google Sheets по имени `products` с помощью `self.get_worksheet('products')`.
2. Проверяет, найден ли рабочий лист. Если нет, вызывает исключение `ValueError`.
3. Считывает все значения из рабочего листа с помощью `ws.get_all_values()`.
4. Создает объект `SimpleNamespace` и заполняет его данными из рабочего листа.
5. Логирует информацию об успешном чтении данных продукта с помощью `logger.info`.
6. Возвращает объект `SimpleNamespace` с данными продукта.
7. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Получение рабочего листа  ---> Проверка наличия  ---> Чтение данных  ---> Создание объекта SimpleNamespace  ---> Логирование  ---> Обработка исключений
```

**Пример**:
```python
gpt_gs = GptGs()
product_data = gpt_gs.get_product_worksheet()
print(product_data.name)
```

### `set_products_worksheet`
```python
def set_products_worksheet(self, category_name:str):
    """ Записывает данные из списка объектов SimpleNamespace в ячейки Google Sheets.
    Args:
        ns_list (List[SimpleNamespace] | SimpleNamespace): Список объектов SimpleNamespace с полями данных для записи.
    """
```

**Как работает функция**:
1. Проверяет, передано ли имя категории (`category_name`).
2. Если имя категории передано, получает объект `SimpleNamespace` категории и объект `SimpleNamespace` продуктов из кампании.
3. Если имя категории не передано, логирует предупреждение и возвращает `None`.
4. Получает рабочий лист Google Sheets по имени категории с помощью `self.get_worksheet(category_name)`.
5. Инициализирует пустой список для хранения обновлений (`updates`).
6. Перебирает объекты `SimpleNamespace` продуктов и подготавливает данные для записи в ячейки рабочего листа.
7. Выполняет пакетное обновление рабочего листа с использованием `ws.batch_update(updates)`.
8. Логирует информацию об успешной записи данных продуктов с помощью `logger.info`.
9. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E --> F
|     |     |     |     |     |
Проверка имени категории  ---> Получение данных  ---> Получение рабочего листа  ---> Инициализация списка  ---> Перебор продуктов  ---> Обновление ячеек  ---> Обработка исключений
```

**Пример**:
```python
from types import SimpleNamespace
gpt_gs = GptGs()
category_name = 'Test Category'
# Предположим, что self.campaign.category.Test Category.products содержит данные о продуктах
gpt_gs.set_products_worksheet(category_name)
```

### `delete_products_worksheets`
```python
def delete_products_worksheets(self):
    """ Удаляет все листы из Google Sheets, кроме \'categories\', \'product\', \'category\' и \'campaign\'.
    """
```

**Как работает функция**:
1. Определяет набор исключенных названий листов (`excluded_titles`).
2. Получает список всех рабочих листов в Google Sheets с помощью `self.spreadsheet.worksheets()`.
3. Перебирает все листы и удаляет те, чьи названия не входят в список исключенных.
4. Логирует информацию об успешном удалении листа с помощью `logger.success`.
5. В случае возникновения ошибки логирует её с помощью `logger.error` и поднимает исключение.

```
A --> B --> C --> D --> E
|     |     |     |     |
Определение исключений  ---> Получение листов  ---> Перебор листов  ---> Удаление листов  ---> Обработка исключений
```

**Пример**:
```python
gpt_gs = GptGs()
gpt_gs.delete_products_worksheets()
```

### `save_categories_from_worksheet`
```python
def save_categories_from_worksheet(self, update:bool=False):
    """ Сохраняю данные, отредактированные в гугл таблице
    Args:
        update (bool, optional): Нужно ли обновить кампанию?. По умолчанию False.
    """
```

**Как работает функция**:
1.  Извлекает отредактированные данные категорий из Google Sheets с помощью `self.get_categories_worksheet()`.
2.  Создает экземпляр `SimpleNamespace` для хранения категорий.
3.  Перебирает извлеченные данные категорий и создает экземпляры `SimpleNamespace` для каждой категории, заполняя их данными из Google Sheets.
4.  Устанавливает атрибуты для `_categories_ns`, используя имена категорий.
5.  Присваивает `self.campaign.category` значение `_categories_ns`.
6.  Если `update` имеет значение `True`, обновляет кампанию с помощью `self.update_campaign()`.

```
Получение отредактированных категорий --> Создание экземпляра SimpleNamespace для категорий --> Перебор отредактированных категорий --> Создание экземпляра SimpleNamespace для каждой категории --> Установка атрибутов для _categories_ns --> Присваивание self.campaign.category значения _categories_ns --> Обновление кампании (если update=True)
```

### `save_campaign_from_worksheet`
```python
def save_campaign_from_worksheet(self):
    """ Сохраняю рекламную кампанию.
    """
```
**Как работает функция**:
1. Сохраняет категории из Google Sheets с помощью `self.save_categories_from_worksheet(False)`.
2. Получает данные кампании из Google Sheets с помощью `self.get_campaign_worksheet()`.
3. Присваивает атрибуту `category` объекта `data` значение `self.campaign.category`.
4. Присваивает атрибуту `self.campaign` значение `data`.
5. Обновляет кампанию с помощью `self.update_campaign()`.
```
Сохранение категорий из Google Sheets --> Получение данных кампании из Google Sheets --> Присваивание атрибуту category объекта data значения self.campaign.category --> Присваивание атрибуту self.campaign значения data --> Обновление кампании
```
```python
from types import SimpleNamespace

# Пример использования для save_campaign_from_worksheet
gpt_gs = GptGs()
# Перед вызовом save_campaign_from_worksheet убедитесь, что self.campaign уже инициализирован
# Например:
gpt_gs.campaign = SimpleNamespace()
gpt_gs.campaign.category = SimpleNamespace()
gpt_gs.save_campaign_from_worksheet()