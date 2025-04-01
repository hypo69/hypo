# Модуль для быстрой работы с Google Sheets в кампаниях AliExpress

## Обзор

Модуль `gsheets-quick.py` предназначен для быстрой настройки и сохранения данных кампаний AliExpress из Google Sheets. Он использует библиотеку `gspread` для взаимодействия с таблицами и классы из других модулей проекта для обработки данных кампаний и категорий.

## Подробней

Этот скрипт является экспериментом для ускорения работы с Google Sheets при настройке кампаний AliExpress. Он позволяет задать имя кампании, категорию, язык и валюту, а затем быстро сохранить продукты и кампанию из указанного Google Sheet.

## Функции

### `AliCampaignGoogleSheet`

```python
class AliCampaignGoogleSheet():
    """
    ...
    """
```

**Описание**:
Класс `AliCampaignGoogleSheet` предназначен для работы с Google Sheets, содержащими данные для кампаний AliExpress. Он предоставляет методы для чтения, записи и обработки данных, связанных с категориями и продуктами кампании.

**Принцип работы**:
Класс инициализируется с именем кампании, языком и валютой. Затем он использует `gspread` для подключения к Google Sheets и выполняет операции чтения и записи данных, необходимые для настройки и сохранения кампании.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliCampaignGoogleSheet` с заданными параметрами.
- `set_products_worksheet`: Устанавливает рабочий лист для продуктов на основе имени категории.
- `save_categories_from_worksheet`: Сохраняет категории из рабочего листа.
- `save_campaign_from_worksheet`: Сохраняет данные кампании из рабочего листа.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Примеры**:
```python
campaign_name = "lighting"
category_name = "chandeliers"
language = 'EN'
currency = 'USD'

gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

gs.set_products_worksheet(category_name)
gs.save_campaign_from_worksheet()
```

## Переменные

### `campaign_name`

```python
campaign_name = "lighting"
```

**Описание**:
Имя кампании, используемое для идентификации и настройки кампании в Google Sheets.

### `category_name`

```python
category_name = "chandeliers"
```

**Описание**:
Имя категории, используемое для указания рабочего листа с продуктами в Google Sheets.

### `language`

```python
language = 'EN'
```

**Описание**:
Язык, используемый в кампании.

### `currency`

```python
currency = 'USD'
```

**Описание**:
Валюта, используемая в кампании.

### `gs`

```python
gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
```

**Описание**:
Инстанс класса `AliCampaignGoogleSheet`, используемый для работы с Google Sheets и выполнения операций, связанных с кампанией.