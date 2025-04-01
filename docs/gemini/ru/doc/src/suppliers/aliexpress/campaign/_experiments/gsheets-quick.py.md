# Модуль `gsheets-quick.py`

## Обзор

Модуль `gsheets-quick.py` является частью проекта `hypotez` и предназначен для быстрой работы с Google Sheets в контексте кампаний AliExpress. Он автоматизирует процессы, связанные с чтением и сохранением данных о кампаниях и продуктах из Google Sheets. Модуль позволяет устанавливать рабочие листы с продуктами, а также сохранять категории и кампании.

## Подробней

Этот модуль упрощает взаимодействие с Google Sheets для управления данными кампаний AliExpress. Он использует класс `AliCampaignGoogleSheet` для работы с таблицами и выполняет такие задачи, как установка рабочих листов с продуктами и сохранение данных о кампаниях.

## Функции

### `AliCampaignGoogleSheet`

**Описание**: Класс для работы с Google Sheets, содержащими данные о кампаниях AliExpress.

**Принцип работы**:
Класс предоставляет интерфейс для взаимодействия с Google Sheets, содержащими данные о кампаниях AliExpress. Он позволяет устанавливать рабочие листы с продуктами, сохранять категории и кампании из рабочих листов.

**Методы**:
- `__init__(campaign_name: str, language: str, currency: str)`: Инициализирует экземпляр класса `AliCampaignGoogleSheet` с именем кампании, языком и валютой.
- `set_products_worksheet(category_name: str)`: Устанавливает рабочий лист с продуктами для указанной категории.
- `save_categories_from_worksheet(save_parent: bool)`: Сохраняет категории из рабочего листа.
- `save_campaign_from_worksheet()`: Сохраняет кампанию из рабочего листа.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `category_name` (str): Имя категории.
- `save_parent` (bool): Флаг, указывающий, нужно ли сохранять родительскую категорию.

**Примеры**:

```python
campaign_name = "lighting"
category_name = "chandeliers"
language = 'EN'
currency = 'USD'

gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

gs.set_products_worksheet(category_name)
# gs.save_categories_from_worksheet(False)
gs.save_campaign_from_worksheet()
...
```

## Переменные

### `campaign_name`

**Описание**: Имя кампании.

### `category_name`

**Описание**: Имя категории.

### `language`

**Описание**: Язык кампании.

### `currency`

**Описание**: Валюта кампании.

### `gs`

**Описание**: Инстанс класса `AliCampaignGoogleSheet`, используемый для работы с Google Sheets.