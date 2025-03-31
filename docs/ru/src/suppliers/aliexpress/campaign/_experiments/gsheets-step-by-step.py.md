# src.suppliers.aliexpress.campaign._experiments.gsheets-step-by-step.py

## Обзор

Этот модуль предназначен для экспериментов с Google Sheets в контексте управления кампаниями AliExpress. Он включает в себя чтение и запись данных категорий и продуктов кампании из/в Google Sheets, а также обновление данных кампании на основе изменений, внесенных в Google Sheets.

## Подробней

Модуль позволяет автоматизировать процесс редактирования и обновления данных кампании AliExpress, используя Google Sheets в качестве удобного интерфейса для редактирования категорий и продуктов.
Взаимодействие с Google Sheets упрощает совместную работу и позволяет удобно управлять большими объемами данных.
Этот модуль является частью экспериментов по интеграции Google Sheets в процесс управления кампаниями AliExpress, облегчая редактирование и синхронизацию данных кампании.

## Классы

### `AliCampaignGoogleSheet`

**Описание**: Класс для взаимодействия с Google Sheets, содержащим данные кампании AliExpress.

**Как работает класс**:
Класс инициализируется с идентификатором Google Sheets, предоставляет методы для чтения и записи данных категорий и продуктов кампании. Он использует библиотеку `gspread` для взаимодействия с Google Sheets API.

**Методы**:

- `__init__(self, spreadsheet_id: str)`: Инициализирует экземпляр класса с указанным `spreadsheet_id`.
- `set_categories(self, categories: list[CategoryType])`: Записывает список категорий в Google Sheet.
- `get_categories(self) -> list[dict]`: Получает отредактированные категории из Google Sheet.
- `set_category_products(self, category_name: str, products: list)`: Устанавливает продукты для указанной категории в Google Sheet.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Sheets.
- `categories` (list[CategoryType]): Список категорий для записи в Google Sheets.
- `category_name` (str): Имя категории для установки продуктов.
- `products` (list): Список продуктов для записи в Google Sheets.

### `AliCampaignEditor`

**Описание**: Класс для редактирования данных кампании AliExpress.

**Как работает класс**:
Класс предоставляет методы для получения данных кампании, категорий и продуктов, а также для обновления данных кампании.

**Методы**:

- `__init__(self, campaign_name: str, language: str, currency: str)`: Инициализирует экземпляр класса с указанными параметрами кампании.
- `get_category_products(self, category_name: str) -> list`: Возвращает список продуктов для указанной категории.
- `update_campaign(self, campaign_data: SimpleNamespace)`: Обновляет данные кампании.

**Параметры**:

- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `category_name` (str): Имя категории для получения продуктов.
- `campaign_data` (SimpleNamespace): Данные кампании для обновления.

## Функции

### `vars(_updated_categories)`
```python
vars(_updated_categories)
```
**Описание**: Получает словарь, представляющий пространство имен объекта `_updated_categories`.
**Как работает функция**:

Функция `vars()` используется для получения словаря, содержащего атрибуты объекта `_updated_categories`. Этот словарь можно использовать для дальнейшей работы с атрибутами объекта, например, для их итерации или модификации.
В данном контексте, после преобразования категорий из Google Sheets и их обновления, `vars()` позволяет получить словарь атрибутов объекта `_updated_categories`, который содержит обновленные категории кампании.

**Параметры**:
- `_updated_categories` (SimpleNamespace): Объект, атрибуты которого необходимо получить в виде словаря.

**Возвращает**:
- `dict`: Словарь, содержащий атрибуты объекта `_updated_categories`.

**Примеры**:

```python
>>> vars(_updated_categories)
{'category1': <__main__.CategoryType object at 0x...>, 'category2': <__main__.CategoryType object at 0x...>}
```
```python
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
...
```
**Описание**: Инициализация экземпляра класса `AliCampaignGoogleSheet` для взаимодействия с Google Sheets.

**Как работает функция**:
Создается экземпляр класса `AliCampaignGoogleSheet`, который позволяет взаимодействовать с Google Sheets API для чтения и записи данных кампании.

**Параметры**:
- Нет явных параметров, но `AliCampaignGoogleSheet` инициализируется с `spreadsheet_id`.

**Примеры**:

```python
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
```

```python
campaign_name = "lighting"
language = 'EN'
currency = 'USD'
```
**Описание**: Определение параметров кампании: имя, язык и валюта.

**Как работает функция**:
Устанавливаются значения для имени кампании, языка и валюты, которые будут использоваться при создании и редактировании данных кампании.

**Параметры**:
- Нет параметров.

**Примеры**:

```python
campaign_name = "lighting"
language = 'EN'
currency = 'USD'
```

```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
campaign_data = campaign_editor.campaign
_categories: SimpleNamespace = campaign_data.category
```
**Описание**: Создание экземпляра `AliCampaignEditor` и получение данных о категориях.

**Как работает функция**:
1. Создается экземпляр класса `AliCampaignEditor` с указанными параметрами кампании.
2. Извлекаются данные кампании из экземпляра `AliCampaignEditor`.
3. Получается объект `SimpleNamespace`, содержащий категории кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**:

```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
campaign_data = campaign_editor.campaign
_categories: SimpleNamespace = campaign_data.category
```

```python
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
```

**Описание**: Преобразование категорий из `SimpleNamespace` в словарь.

**Как работает функция**:
Создается словарь `categories_dict`, где ключами являются имена категорий, а значениями - объекты `CategoryType`, полученные из `_categories`.

**Параметры**:
- `_categories` (SimpleNamespace): Объект, содержащий категории кампании.

**Примеры**:

```python
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
```

```python
categories_list: list[CategoryType] = list(categories_dict.values())
```

**Описание**: Преобразование категорий из словаря в список.

**Как работает функция**:
Создается список `categories_list`, содержащий значения (объекты `CategoryType`) из словаря `categories_dict`.

**Параметры**:
- `categories_dict` (dict[str, CategoryType]): Словарь категорий.

**Примеры**:

```python
categories_list: list[CategoryType] = list(categories_dict.values())
```

```python
gs.set_categories(categories_list)
```

**Описание**: Установка категорий в Google Sheet.

**Как работает функция**:
Вызывается метод `set_categories` объекта `AliCampaignGoogleSheet` для записи списка категорий в Google Sheet.

**Параметры**:
- `categories_list` (list[CategoryType]): Список категорий для записи в Google Sheets.

**Примеры**:

```python
gs.set_categories(categories_list)
```

```python
edited_categories: list[dict] = gs.get_categories()
```

**Описание**: Получение отредактированных категорий из Google Sheet.

**Как работает функция**:
Вызывается метод `get_categories` объекта `AliCampaignGoogleSheet` для получения списка отредактированных категорий из Google Sheet.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `list[dict]`: Список словарей, представляющих отредактированные категории.

**Примеры**:

```python
edited_categories: list[dict] = gs.get_categories()
```

```python
for _cat in edited_categories:
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    }
    )
    # Логирование для отладки
    logger.info(f"Updating category: {_cat_ns.name}")
    categories_dict[_cat_ns.name] = _cat_ns
    products = campaign_editor.get_category_products(_cat_ns.name)
    gs.set_category_products(_cat_ns.name,products)
```

**Описание**: Обновление словаря `categories_dict` с отредактированными данными из Google Sheet.

**Как работает функция**:
1. Итерируется по списку `edited_categories`, полученному из Google Sheet.
2. Для каждой категории создается объект `SimpleNamespace` с данными из словаря `_cat`.
3. Обновляется словарь `categories_dict` с данными из `_cat_ns`.
4. Получаются продукты для категории с помощью `campaign_editor.get_category_products(_cat_ns.name)`.
5. Устанавливаются продукты для категории в Google Sheet с помощью `gs.set_category_products(_cat_ns.name, products)`.
6. Логируется информация об обновляемой категории.

**Параметры**:
- `edited_categories` (list[dict]): Список словарей, представляющих отредактированные категории.
- `_cat_ns` (SimpleNamespace): Объект, содержащий данные отредактированной категории.
- `products` (list): Список продуктов для установки в Google Sheet.

**Примеры**:

```python
for _cat in edited_categories:
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    }
    )
    # Логирование для отладки
    logger.info(f"Updating category: {_cat_ns.name}")
    categories_dict[_cat_ns.name] = _cat_ns
    products = campaign_editor.get_category_products(_cat_ns.name)
    gs.set_category_products(_cat_ns.name,products)
```

```python
_updated_categories = SimpleNamespace(**categories_dict)
```

**Описание**: Преобразование `categories_dict` обратно в `SimpleNamespace`.

**Как работает функция**:
Создается объект `SimpleNamespace` из словаря `categories_dict`, содержащего обновленные данные категорий.

**Параметры**:
- `categories_dict` (dict): Словарь, содержащий обновленные данные категорий.

**Примеры**:

```python
_updated_categories = SimpleNamespace(**categories_dict)
```

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}
```

**Описание**: Создание словаря для кампании.

**Как работает функция**:
Создается словарь `campaign_dict`, содержащий данные кампании, включая имя, заголовок, язык, валюту и обновленные категории.

**Параметры**:
- `campaign_data` (SimpleNamespace): Объект, содержащий данные кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `_updated_categories` (SimpleNamespace): Объект, содержащий обновленные категории.

**Примеры**:

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}
```

```python
edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
```

**Описание**: Создание `SimpleNamespace` для отредактированной кампании.

**Как работает функция**:
Создается объект `SimpleNamespace` из словаря `campaign_dict`, содержащего данные отредактированной кампании.

**Параметры**:
- `campaign_dict` (dict): Словарь, содержащий данные кампании.

**Примеры**:

```python
edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
```

```python
campaign_editor.update_campaign(edited_campaign)
```

**Описание**: Обновление данных кампании.

**Как работает функция**:
Вызывается метод `update_campaign` объекта `AliCampaignEditor` для обновления данных кампании с использованием объекта `edited_campaign`.

**Параметры**:
- `edited_campaign` (SimpleNamespace): Объект, содержащий данные отредактированной кампании.

**Примеры**:

```python
campaign_editor.update_campaign(edited_campaign)
```
```python
pprint(_updated_categories)
```
**Описание**: Вывод данных для отладки
**Как работает функция**:

Функция `pprint` используется для форматированного вывода содержимого объекта `_updated_categories` в консоль. Это полезно для отладки и проверки данных, чтобы убедиться, что они имеют ожидаемый формат и значения.

**Параметры**:
- `_updated_categories` (SimpleNamespace): Объект, который необходимо вывести для отладки.
```python
pprint(edited_campaign)
```
**Описание**: Вывод данных для отладки
**Как работает функция**:

Функция `pprint` используется для форматированного вывода содержимого объекта `edited_campaign` в консоль. Это полезно для отладки и проверки данных, чтобы убедиться, что они имеют ожидаемый формат и значения.

**Параметры**:
- `edited_campaign` (SimpleNamespace): Объект, который необходимо вывести для отладки.
```python
logger.info(f"Updating category: {_cat_ns.name}")
```
**Описание**: Логирование обновления категории.

**Как работает функция**:
Используется модуль логирования `logger` для записи сообщения об обновлении категории. Логирование необходимо для отслеживания процесса обновления данных и выявления возможных проблем.

**Параметры**:
- `_cat_ns.name` (str): Имя категории, которая обновляется.

```python
_cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    })
```
**Описание**: Создание экземпляра SimpleNamespace с данными категории.

**Как работает функция**:
Создается объект SimpleNamespace `_cat_ns` из словаря `_cat`, содержащего данные о категории (имя, заголовок, описание, теги и количество продуктов). Это упрощает доступ к данным категории через атрибуты объекта.

**Параметры**:
- `_cat` (dict): Словарь с данными о категории.

```python
campaign_data = campaign_editor.campaign
```
**Описание**: Получение данных кампании из редактора кампании.

**Как работает функция**:
Извлекает объект кампании из экземпляра `AliCampaignEditor`.

**Параметры**:
Нет входных параметров.

```python
_categories: SimpleNamespace = campaign_data.category
```
**Описание**: Получение объекта категорий кампании.

**Как работает функция**:
Извлекает категории из объекта данных кампании `campaign_data`.

**Параметры**:
Нет входных параметров.
```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
```

**Описание**: Создание экземпляра редактора кампании AliExpress.

**Как работает функция**:
Создается экземпляр класса `AliCampaignEditor` с указанными параметрами кампании для редактирования данных.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

```python
edited_categories: list[dict] = gs.get_categories()
```

**Описание**: Получение отредактированных категорий из Google Sheets.

**Как работает функция**:
Вызывает метод `get_categories` объекта `AliCampaignGoogleSheet` для получения списка категорий, отредактированных в Google Sheets.

**Параметры**:
Нет входных параметров.

```python
gs.set_categories(categories_list)
```
**Описание**: Установка списка категорий в Google Sheets.

**Как работает функция**:
Вызывает метод `set_categories` объекта `AliCampaignGoogleSheet` для записи списка категорий в Google Sheets.

**Параметры**:
- `categories_list` (list[CategoryType]): Список категорий для записи.
```python
categories_list: list[CategoryType] = list(categories_dict.values())
```

**Описание**: Преобразование словаря категорий в список.

**Как работает функция**:
Извлекает значения (объекты категорий) из словаря `categories_dict` и преобразует их в список.

**Параметры**:
- `categories_dict` (dict[str, CategoryType]): Словарь, содержащий объекты категорий.

```python
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
```

**Описание**: Преобразование SimpleNamespace категорий в словарь.

**Как работает функция**:
Преобразует SimpleNamespace объект `_categories` в словарь, где ключами являются имена категорий, а значениями - соответствующие объекты `CategoryType`.

**Параметры**:
- `_categories` (SimpleNamespace): Объект SimpleNamespace, содержащий объекты категорий.

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}
```

**Описание**: Создание словаря данных кампании.

**Как работает функция**:
Создает словарь `campaign_dict`, содержащий данные кампании, включая имя, заголовок, язык, валюту и обновленные категории.

**Параметры**:
- `campaign_data` (SimpleNamespace): Объект SimpleNamespace, содержащий данные кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `_updated_categories` (SimpleNamespace): Объект SimpleNamespace, содержащий обновленные объекты категорий.

```python
edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
```

**Описание**: Создание объекта SimpleNamespace для отредактированной кампании.

**Как работает функция**:
Создает SimpleNamespace объект `edited_campaign` из словаря `campaign_dict`, содержащего данные отредактированной кампании.

**Параметры**:
- `campaign_dict` (dict): Словарь, содержащий данные кампании.

```python
campaign_editor.update_campaign(edited_campaign)
```

**Описание**: Обновление данных кампании с помощью редактора кампании.

**Как работает функция**:
Вызывает метод `update_campaign` объекта `campaign_editor` для обновления данных кампании с использованием объекта `edited_campaign`.

**Параметры**:
- `edited_campaign` (SimpleNamespace): Объект SimpleNamespace, содержащий данные отредактированной кампании.

```python
products = campaign_editor.get_category_products(_cat_ns.name)
```
**Описание**: Получение списка продуктов для категории.

**Как работает функция**:
Вызывает метод `get_category_products` объекта `campaign_editor` для получения списка продуктов, связанных с категорией `_cat_ns.name`.

**Параметры**:
- `_cat_ns.name` (str): Имя категории, для которой нужно получить список продуктов.

```python
gs.set_category_products(_cat_ns.name, products)
```
**Описание**: Установка списка продуктов для категории в Google Sheets.

**Как работает функция**:
Вызывает метод `set_category_products` объекта `AliCampaignGoogleSheet` для установки списка продуктов `products` для категории `_cat_ns.name` в Google Sheets.

**Параметры**:
- `_cat_ns.name` (str): Имя категории, для которой нужно установить список продуктов.
- `products` (list): Список продуктов для установки.
```python
_updated_categories = SimpleNamespace(**categories_dict)
```
**Описание**: Преобразование обновленного словаря категорий в объект SimpleNamespace.

**Как работает функция**:
Создает объект `SimpleNamespace` из словаря `categories_dict`, который содержит обновленные данные категорий.

**Параметры**:
- `categories_dict` (dict): Словарь, содержащий обновленные данные категорий.
```python
campaign_name = "lighting"
language = 'EN'
currency = 'USD'
```

**Описание**: Установка параметров кампании.

**Как работает функция**:
Устанавливаются значения для имени кампании, языка и валюты.

**Параметры**:
Нет входных параметров.

```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
```

**Описание**: Создание экземпляра класса `AliCampaignEditor`.

**Как работает функция**:
Создает экземпляр класса `AliCampaignEditor` с указанными параметрами кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

```python
campaign_data = campaign_editor.campaign
```

**Описание**: Получение данных кампании из редактора.

**Как работает функция**:
Извлекает объект кампании из экземпляра `AliCampaignEditor`.

**Параметры**:
Нет входных параметров.

```python
_categories: SimpleNamespace = campaign_data.category
```

**Описание**: Получение категорий из данных кампании.

**Как работает функция**:
Извлекает объект категорий из объекта данных кампании.

**Параметры**:
Нет входных параметров.

```python
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
```

**Описание**: Преобразование категорий из SimpleNamespace в словарь.

**Как работает функция**:
Создает словарь, где ключами являются имена категорий, а значениями - соответствующие объекты `CategoryType`.

**Параметры**:
- `_categories` (SimpleNamespace): Объект SimpleNamespace, содержащий объекты категорий.

```python
categories_list: list[CategoryType] = list(categories_dict.values())
```

**Описание**: Преобразование категорий из словаря в список.

**Как работает функция**:
Извлекает объекты категорий из словаря и преобразует их в список.

**Параметры**:
- `categories_dict` (dict[str, CategoryType]): Словарь, содержащий объекты категорий.

```python
gs.set_categories(categories_list)
```

**Описание**: Установка категорий в Google Sheets.

**Как работает функция**:
Вызывает метод `set_categories` объекта `AliCampaignGoogleSheet` для записи списка категорий в Google Sheets.

**Параметры**:
- `categories_list` (list[CategoryType]): Список категорий для записи.

```python
edited_categories: list[dict] = gs.get_categories()
```

**Описание**: Получение отредактированных категорий из Google Sheets.

**Как работает функция**:
Вызывает метод `get_categories` объекта `AliCampaignGoogleSheet` для получения списка категорий, отредактированных в Google Sheets.

**Параметры**:
Нет входных параметров.
```python
for _cat in edited_categories:
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    }
    )
    # Логирование для отладки
    logger.info(f"Updating category: {_cat_ns.name}")
    categories_dict[_cat_ns.name] = _cat_ns
    products = campaign_editor.get_category_products(_cat_ns.name)
    gs.set_category_products(_cat_ns.name,products)
```

**Описание**: Обновление словаря категорий с отредактированными данными из Google Sheets.

**Как работает функция**:
Итерируется по списку отредактированных категорий, создает объект `SimpleNamespace` для каждой категории и обновляет словарь категорий, а также обновляет продукты для каждой категории в Google Sheets.

**Параметры**:
- `edited_categories` (list[dict]): Список словарей, содержащих отредактированные данные категорий.

```python
_updated_categories = SimpleNamespace(**categories_dict)
```

**Описание**: Преобразование обновленного словаря категорий в SimpleNamespace.

**Как работает функция**:
Создает SimpleNamespace объект из словаря, содержащего обновленные данные категорий.

**Параметры**:
- `categories_dict` (dict): Словарь, содержащий обновленные данные категорий.

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}
```

**Описание**: Создание словаря данных кампании.

**Как работает функция**:
Создает словарь, содержащий данные кампании, включая имя, заголовок, язык, валюту и обновленные категории.

**Параметры**:
- `campaign_data` (SimpleNamespace): Объект SimpleNamespace, содержащий данные кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `_updated_categories` (SimpleNamespace): Объект SimpleNamespace, содержащий обновленные объекты категорий.

```python
edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
```

**Описание**: Создание объекта SimpleNamespace для отредактированной кампании.

**Как работает функция**:
Создает SimpleNamespace объект из словаря, содержащего данные отредактированной кампании.

**Параметры**:
- `campaign_dict` (dict): Словарь, содержащий данные кампании.

```python
campaign_editor.update_campaign(edited_campaign)
```

**Описание**: Обновление данных кампании с помощью редактора кампании.

**Как работает функция**:
Вызывает метод `update_campaign` объекта `campaign_editor` для обновления данных кампании с использованием объекта `edited_campaign`.

**Параметры**:
- `edited_campaign` (SimpleNamespace): Объект SimpleNamespace, содержащий данные отредактированной кампании.
```python
products = campaign_editor.get_category_products(_cat_ns.name)
```

**Описание**: Получение списка продуктов для категории.

**Как работает функция**:
Вызывает метод `get_category_products` объекта `campaign_editor` для получения списка продуктов, связанных с категорией `_cat_ns.name`.

**Параметры**:
- `_cat_ns.name` (str): Имя категории, для которой нужно получить список продуктов.

```python
gs.set_category_products(_cat_ns.name, products)
```

**Описание**: Установка списка продуктов для категории в Google Sheets.

**Как работает функция**:
Вызывает метод `set_category_products` объекта `AliCampaignGoogleSheet` для установки списка продуктов `products` для категории `_cat_ns.name` в Google Sheets.

**Параметры**:
- `_cat_ns.name` (str): Имя категории, для которой нужно установить список продуктов.
- `products` (list): Список продуктов для установки.

```python
logger.info(f"Updating category: {_cat_ns.name}")
```

**Описание**: Логирование обновления категории.

**Как работает функция**:
Использует модуль логирования `logger` для записи сообщения об обновлении категории.

**Параметры**:
- `_cat_ns.name` (str): Имя обновляемой категории.
```python
_cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    })
```

**Описание**: Создание объекта SimpleNamespace для категории.

**Как работает функция**:
Создает объект SimpleNamespace `_cat_ns` из словаря `_cat`, содержащего данные о категории (имя, заголовок, описание, теги и количество продуктов).

**Параметры**:
- `_cat` (dict): Словарь с данными о категории.
```python
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
```

**Описание**: Инициализация экземпляра класса AliCampaignGoogleSheet.

**Как работает функция**:
Создает экземпляр класса `AliCampaignGoogleSheet` для взаимодействия с Google Sheets.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Sheets. В данном случае `'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'`.
```python
campaign_name = "lighting"
```

**Описание**: Определение имени кампании.

**Как работает функция**:
Присваивает значение `"lighting"` переменной `campaign_name`.

**Параметры**:
Отсутствуют.

```python
language = 'EN'
```

**Описание**: Определение языка кампании.

**Как работает функция**:
Присваивает значение `'EN'` переменной `language`.

**Параметры**:
Отсутствуют.

```python
currency = 'USD'
```

**Описание**: Определение валюты кампании.

**Как работает функция**:
Присваивает значение `'USD'` переменной `currency`.

**Параметры**:
Отсутствуют.
```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
```

**Описание**: Инициализация экземпляра класса AliCampaignEditor.

**Как работает функция**:
Создает экземпляр класса `AliCampaignEditor` с указанными параметрами кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
```python
campaign_data = campaign_editor.campaign
```

**Описание**: Получение данных кампании.

**Как работает функция**:
Извлекает данные кампании из объекта `campaign_editor`.

**Параметры**:
Отсутствуют.

```python
_categories: SimpleNamespace = campaign_data.category
```

**Описание**: Получение категорий кампании.

**Как работает функция**:
Извлекает объект категорий из данных кампании.

**Параметры**:
Отсутствуют.
```python
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
```

**Описание**: Преобразование категорий из SimpleNamespace в словарь.

**Как работает функция**:
Создает словарь, где ключами являются имена категорий, а значениями - соответствующие объекты `CategoryType`.

**Параметры**:
- `_categories` (SimpleNamespace): Объект SimpleNamespace, содержащий объекты категорий.
```python
categories_list: list[CategoryType] = list(categories_dict.values())
```

**Описание**: Преобразование категорий из словаря в список.

**Как работает функция**:
Извлекает объекты категорий из словаря и преобразует их в список.

**Параметры**:
- `categories_dict` (dict[str, CategoryType]): Словарь, содержащий объекты категорий.
```python
gs.set_categories(categories_list)
```

**Описание**: Установка категорий в Google Sheets.

**Как работает функция**:
Вызывает метод `set_categories` объекта `AliCampaignGoogleSheet` для записи списка категорий в Google Sheets.

**Параметры**:
- `categories_list` (list[CategoryType]): Список категорий для записи.
```python
edited_categories: list[dict] = gs.get_categories()
```

**Описание**: Получение отредактированных категорий из Google Sheets.

**Как работает функция**:
Вызывает метод `get_categories` объекта `AliCampaignGoogleSheet` для получения списка категорий, отредактированных в Google Sheets.

**Параметры**:
Отсутствуют.
```python
for _cat in edited_categories:
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    }
    )
    # Логирование для отладки
    logger.info(f"Updating category: {_cat_ns.name}")
    categories_dict[_cat_ns.name] = _cat_ns
    products = campaign_editor.get_category_products(_cat_ns.name)
    gs.set_category_products(_cat_ns.name,products)
```

**Описание**: Обновление словаря категорий с отредактированными данными из Google Sheets.

**Как работает функция**:
Итерируется по списку отредактированных категорий, создает объект `SimpleNamespace` для каждой категории и обновляет словарь категорий, а также обновляет продукты для каждой категории в Google Sheets.

**Параметры**:
- `edited_categories` (list[dict]): Список словарей, содержащих отредактированные данные категорий.

```python
_updated_categories = SimpleNamespace(**categories_dict)
```

**Описание**: Преобразование обновленного словаря категорий в SimpleNamespace.

**Как работает функция**:
Создает SimpleNamespace объект из словаря, содержащего