# Модуль gsheets-quick.py

## Обзор

Модуль `gsheets-quick.py` предназначен для быстрой работы с Google Sheets в контексте кампаний AliExpress. Он позволяет загружать данные о кампаниях и категориях товаров из Google Sheets, а также сохранять информацию о кампаниях обратно в таблицы. Модуль использует классы и функции из других модулей проекта, таких как `AliCampaignGoogleSheet`, `CampaignType`, `CategoryType` и `ProductType`.

## Подробней

Этот модуль предоставляет возможность автоматизировать процесс импорта и экспорта данных между Google Sheets и системой управления кампаниями AliExpress. Он позволяет упростить и ускорить процесс обновления информации о товарах, категориях и параметрах кампаний. В частности, модуль используется для извлечения данных из Google Sheets, их преобразования и сохранения в структурах данных, используемых в других частях проекта.

## Функции

### `AliCampaignGoogleSheet`

```python
AliCampaignGoogleSheet(campaign_name: str, language: str, currency: str) -> None:
    """
    Args:
        campaign_name (str): Название кампании.
        language (str): Язык кампании.
        currency (str): Валюта кампании.

    Returns:
        None

    Raises:
        Отсутствуют.
    """
```

**Описание**: Конструктор класса `AliCampaignGoogleSheet`.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
campaign_name = "lighting"
language = 'EN'
currency = 'USD'
gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)
```

### `set_products_worksheet`

```python
def set_products_worksheet(category_name: str) -> None:
    """
    Args:
        category_name (str): Название категории.

    Returns:
        None

    Raises:
        Отсутствуют.
    """
```

**Описание**: Устанавливает рабочий лист с продуктами для заданной категории.

**Параметры**:
- `category_name` (str): Название категории.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
category_name = "chandeliers"
gs.set_products_worksheet(category_name)
```

### `save_campaign_from_worksheet`

```python
def save_campaign_from_worksheet() -> None:
    """
    Args:
        Отсутствуют.

    Returns:
        None

    Raises:
        Отсутствуют.
    """
```

**Описание**: Сохраняет данные о кампании из рабочего листа.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:

```python
gs.save_campaign_from_worksheet()