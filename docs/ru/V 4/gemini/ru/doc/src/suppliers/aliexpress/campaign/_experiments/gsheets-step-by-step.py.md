# Модуль gsheets-step-by-step

## Обзор

Модуль `gsheets-step-by-step.py` предназначен для экспериментов с Google Sheets в контексте управления рекламными кампаниями на AliExpress. Он автоматизирует процесс обновления и редактирования категорий товаров и информации о кампаниях, используя данные из Google Sheets и API AliExpress.

## Подробней

Этот модуль является частью системы автоматизации маркетинговых кампаний на AliExpress. Он позволяет изменять категории товаров и параметры кампаний непосредственно в Google Sheets, а затем применять эти изменения к данным кампании.

Основные этапы работы модуля:

1.  Инициализация: Создается объект `AliCampaignGoogleSheet` для взаимодействия с указанной Google Sheet.
2.  Получение и преобразование данных: Категории товаров извлекаются, преобразуются в различные форматы (словарь, список) и отправляются в Google Sheets для редактирования.
3.  Обновление данных: Отредактированные категории считываются из Google Sheets и применяются к данным кампании.
4.  Применение изменений: Обновленные данные используются для изменения параметров кампании.

## Функции

### `AliCampaignGoogleSheet`

**Описание**: Класс для взаимодействия с Google Sheets, содержащими данные о рекламных кампаниях AliExpress.

**Методы**:
- `__init__`: Инициализирует объект `AliCampaignGoogleSheet` с указанием идентификатора Google Sheet.
- `set_categories`: Записывает список категорий в Google Sheet.
- `get_categories`: Считывает отредактированные категории из Google Sheet.
- `set_category_products`: Записывает продукты категории в Google Sheet.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Sheet.

**Примеры**:

```python
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
```

### `AliCampaignEditor`

**Описание**: Класс для редактирования параметров рекламных кампаний AliExpress.

**Методы**:
- `__init__`: Инициализирует объект `AliCampaignEditor` с именем кампании, языком и валютой.
- `get_category_products`: Получает продукты указанной категории.
- `update_campaign`: Обновляет параметры кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**:

```python
campaign_editor = AliCampaignEditor(campaign_name, language, currency)
```

### `set_categories`

```python
gs.set_categories(categories_list)
```

**Описание**: Устанавливает категории в Google Sheet.

**Параметры**:
- `categories_list` (list[CategoryType]): Список категорий для установки.

**Возвращает**:
- `None`

### `get_categories`

```python
edited_categories: list[dict] = gs.get_categories()
```

**Описание**: Получает отредактированные категории из Google Sheet.

**Параметры**:
- `None`

**Возвращает**:
- `list[dict]`: Список словарей, представляющих отредактированные категории.

### `set_category_products`

```python
gs.set_category_products(_cat_ns.name,products)
```

**Описание**: Устанавливает продукты категории в Google Sheet.

**Параметры**:
- `category_name` (str): Имя категории.
- `products` (Any): Продукты для установки.

**Возвращает**:
- `None`

### `get_category_products`

```python
products = campaign_editor.get_category_products(_cat_ns.name)
```

**Описание**: Получает продукты указанной категории.

**Параметры**:
- `category_name` (str): Имя категории.

**Возвращает**:
- `list[ProductType]`: Список продуктов категории.

### `update_campaign`

```python
campaign_editor.update_campaign(edited_campaign)
```

**Описание**: Обновляет параметры кампании.

**Параметры**:
- `edited_campaign` (SimpleNamespace): Объект SimpleNamespace с обновленными данными кампании.

**Возвращает**:
- `None`

### Преобразование категорий

**Описание**: Преобразует категории из формата `SimpleNamespace` в словарь, затем в список для Google Sheets и обратно.

**Примеры**:

```python
# Преобразование _categories в словарь
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}

# Преобразование категорий в список для Google Sheets
categories_list: list[CategoryType] = list(categories_dict.values())

# Преобразование categories_dict обратно в SimpleNamespace вручную
_updated_categories = SimpleNamespace(**categories_dict)
```

### Обновление словаря категорий

**Описание**: Обновляет словарь `categories_dict` данными, полученными из Google Sheets.

**Примеры**:

```python
for _cat in edited_categories:
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        'name':_cat['name'],
        'title':_cat['title'],
        'description':_cat['description'],
        'tags':_cat['tags'],
        'products_count':_cat['products_count']
    })
    logger.info(f"Updating category: {_cat_ns.name}")
    categories_dict[_cat_ns.name] = _cat_ns
    products = campaign_editor.get_category_products(_cat_ns.name)
    gs.set_category_products(_cat_ns.name, products)
```

### Создание словаря для кампании

**Описание**: Создает словарь с данными кампании, включая обновленные категории.

**Примеры**:

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}

edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
```