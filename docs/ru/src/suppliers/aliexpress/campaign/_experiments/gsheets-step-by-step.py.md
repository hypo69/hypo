# Модуль `gsheets-step-by-step.py`

## Обзор

Модуль предназначен для экспериментов с Google Sheets в контексте управления рекламными кампаниями AliExpress. Он автоматизирует процесс обновления категорий и продуктов в Google Sheets на основе данных, полученных и отредактированных из API AliExpress. Модуль использует классы `AliCampaignGoogleSheet` и `AliCampaignEditor` для взаимодействия с Google Sheets и API AliExpress соответственно.

## Подробней

Этот модуль является частью более крупной системы для управления рекламными кампаниями на AliExpress. Он позволяет автоматизировать процесс обновления данных о категориях и продуктах в Google Sheets, что упрощает анализ и управление рекламными кампаниями. Код использует `AliCampaignGoogleSheet` для чтения и записи данных в Google Sheets и `AliCampaignEditor` для получения данных о категориях и продуктах из API AliExpress. В данном случае, код предназначен для извлечения данных из Google Sheets, преобразования их в объекты Python, а затем для обновления информации о кампаниях.

## Функции

### `Нет функций в модуле`

В данном модуле отсутствуют отдельные функции. Весь код выполняется последовательно.

## Классы

### `Нет классов в модуле`

В данном модуле не определены классы.

## Переменные

### `gs`

```python
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
```

- **Назначение**: Экземпляр класса `AliCampaignGoogleSheet`, используемый для взаимодействия с Google Sheets.  
  Аргумент - ID Google Sheet.
- **Тип**: `AliCampaignGoogleSheet`

### `campaign_name`

```python
campaign_name = "lighting"
```

- **Назначение**: Название рекламной кампании.
- **Тип**: `str`

### `language`

```python
language = 'EN'
```

- **Назначение**: Язык рекламной кампании.
- **Тип**: `str`

### `currency`

```python
currency = 'USD'
```

- **Назначение**: Валюта рекламной кампании.
- **Тип**: `str`

### `campaign_editor`

```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
```

- **Назначение**: Экземпляр класса `AliCampaignEditor`, используемый для редактирования данных рекламной кампании. При инициализации передаются имя кампании, язык и валюта.
- **Тип**: `AliCampaignEditor`

### `campaign_data`

```python
campaign_data = campaign_editor.campaign
```

- **Назначение**: Данные рекламной кампании, полученные из `campaign_editor`.
- **Тип**: Зависит от структуры данных, возвращаемой `campaign_editor.campaign`

### `_categories`

```python
_categories: SimpleNamespace = campaign_data.category
```

- **Назначение**: Категории рекламной кампании, полученные из `campaign_data`.
- **Тип**: `SimpleNamespace`

### `categories_dict`

```python
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
```

- **Назначение**: Преобразование категорий из `_categories` в словарь, где ключ - имя категории, значение - объект `CategoryType`.
- **Тип**: `dict[str, CategoryType]`

### `categories_list`

```python
categories_list: list[CategoryType] = list(categories_dict.values())
```

- **Назначение**: Преобразование категорий из словаря `categories_dict` в список объектов `CategoryType`.
- **Тип**: `list[CategoryType]`

### `edited_categories`

```python
edited_categories: list[dict] = gs.get_categories()
```

- **Назначение**: Получение отредактированных категорий из Google Sheets в виде списка словарей.
- **Тип**: `list[dict]`

### `_cat`

```python
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    }
    )
```

- **Назначение**: Итерируемая переменная, представляющая собой словарь с данными о категории из списка `edited_categories`.
- **Тип**: `dict`

### `_cat_ns`

```python
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    }
    )
```

- **Назначение**: Преобразование данных категории из словаря `_cat` в объект `SimpleNamespace` для удобства доступа к атрибутам.
- **Тип**: `SimpleNamespace`

### `products`

```python
    products = campaign_editor.get_category_products(_cat_ns.name)
```

- **Назначение**: Получение списка продуктов для данной категории из `campaign_editor`.
- **Тип**: Зависит от структуры данных, возвращаемой `campaign_editor.get_category_products`

### `_updated_categories`

```python
_updated_categories = SimpleNamespace(**categories_dict)
```

- **Назначение**: Обновленные категории, преобразованные обратно в `SimpleNamespace` после редактирования.
- **Тип**: `SimpleNamespace`

### `campaign_dict`

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}
```

- **Назначение**: Создание словаря для хранения данных о рекламной кампании.
- **Тип**: `dict`

### `edited_campaign`

```python
edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
```

- **Назначение**: Преобразование словаря `campaign_dict` в объект `SimpleNamespace` для представления отредактированной рекламной кампании.
- **Тип**: `SimpleNamespace`

## Как работает код

1.  **Инициализация**:
    *   Создается экземпляр `AliCampaignGoogleSheet` для работы с Google Sheets.
    *   Устанавливаются основные параметры кампании: `campaign_name`, `language` и `currency`.
    *   Создается экземпляр `AliCampaignEditor` для работы с данными кампании.
2.  **Получение и преобразование категорий**:
    *   Категории извлекаются из `campaign_data` и преобразуются в словарь `categories_dict`.
    *   Словарь преобразуется в список `categories_list` для записи в Google Sheets.
3.  **Работа с Google Sheets**:
    *   `categories_list` записывается в Google Sheets с помощью `gs.set_categories()`.
    *   Отредактированные категории извлекаются из Google Sheets с помощью `gs.get_categories()` в виде списка словарей `edited_categories`.
4.  **Обновление категорий**:
    *   Для каждой отредактированной категории создается объект `SimpleNamespace` (`_cat_ns`).
    *   Данные категории обновляются в словаре `categories_dict`.
    *   Для каждой категории извлекаются продукты с помощью `campaign_editor.get_category_products()` и записываются в Google Sheets.
5.  **Финальное преобразование и обновление**:
    *   Обновленный словарь `categories_dict` преобразуется обратно в `SimpleNamespace` (`_updated_categories`).
    *   Создается словарь `campaign_dict` с данными кампании, включая обновленные категории.
    *   Словарь `campaign_dict` преобразуется в `SimpleNamespace` (`edited_campaign`).
    *   Обновленные данные кампании передаются в `campaign_editor` для обновления кампании.

## ASCII Flowchart

```
Начало
│
├──► Инициализация (gs, campaign_name, language, currency, campaign_editor)
│
├──► Получение категорий (_categories = campaign_data.category)
│
├──► Преобразование категорий (categories_dict, categories_list)
│
├──► Запись категорий в Google Sheets (gs.set_categories(categories_list))
│
├──► Получение отредактированных категорий из Google Sheets (edited_categories = gs.get_categories())
│
├──► Цикл по отредактированным категориям (for _cat in edited_categories):
│   │
│   ├──► Преобразование категории в SimpleNamespace (_cat_ns)
│   │
│   ├──► Логирование (logger.info(f"Updating category: {_cat_ns.name}"))
│   │
│   ├──► Обновление категории в categories_dict
│   │
│   ├──► Получение продуктов категории (products = campaign_editor.get_category_products(_cat_ns.name))
│   │
│   └──► Запись продуктов в Google Sheets (gs.set_category_products(_cat_ns.name, products))
│
├──► Преобразование categories_dict в SimpleNamespace (_updated_categories)
│
├──► Создание словаря кампании (campaign_dict)
│
├──► Преобразование словаря кампании в SimpleNamespace (edited_campaign)
│
└──► Обновление кампании (campaign_editor.update_campaign(edited_campaign))
│
Конец
```

## Примеры

```python
from types import SimpleNamespace
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.campaign import AliCampaignGoogleSheet


# Пример инициализации AliCampaignGoogleSheet
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')

# Пример инициализации AliCampaignEditor
campaign_name = "lighting"
language = 'EN'
currency = 'USD'
campaign_editor = AliCampaignEditor(campaign_name, language, currency)

# Пример получения категорий
campaign_data = campaign_editor.campaign
_categories: SimpleNamespace = campaign_data.category
categories_dict = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
categories_list = list(categories_dict.values())

# Пример обновления словаря categories_dict с отредактированными данными
edited_categories = gs.get_categories()
for _cat in edited_categories:
    _cat_ns = SimpleNamespace(**{
        'name': _cat['name'],
        'title': _cat['title'],
        'description': _cat['description'],
        'tags': _cat['tags'],
        'products_count': _cat['products_count']
    })
    categories_dict[_cat_ns.name] = _cat_ns

# Пример создания словаря для кампании
_updated_categories = SimpleNamespace(**categories_dict)
campaign_dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}
edited_campaign = SimpleNamespace(**campaign_dict)