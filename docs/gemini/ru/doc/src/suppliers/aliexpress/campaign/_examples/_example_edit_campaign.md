# Модуль hypotez/src/suppliers/aliexpress/campaign/_examples/_example_edit_campaign.py

## Обзор

Этот модуль содержит пример реализации редактора рекламных кампаний на AliExpress. Он предоставляет класс `AliCampaignEditor`, который наследуется от класса `AliPromoCampaign` и предоставляет методы для редактирования рекламных кампаний.

## Оглавление

- [Модуль hypotez/src/suppliers/aliexpress/campaign/_examples/_example_edit_campaign.py](#модуль-hypotezsrcsuppliersaliexpresscampaign_examples_example_edit_campaignpy)
- [Класс `AliCampaignEditor`](#класс-alicampaigneditor)


## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний на AliExpress. Он расширяет функциональность базового класса `AliPromoCampaign`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `AliCampaignEditor`.

**Параметры конструктора `__init__`**:
- `campaign_name` (str): Имя рекламной кампании.
- `category_name` (str): Название категории.
- `language` (str, по умолчанию 'EN'): Язык.
- `currency` (str, по умолчанию 'USD'): Валюта.


**Примечания**:

Подробный код и функциональность методов в этом примере не предоставлены, так как в исходном коде отсутствует их реализация.


**Возвращает**:
- Экземпляр класса `AliCampaignEditor`.

**Вызывает исключения**:
- Любые исключения, которые могут быть вызваны базовым классом `AliPromoCampaign` или связанными с ним методами.




```
```python
# Пример кода для __init__ (без реализации)
def __init__(self, campaign_name: str, category_name: str, language: str = 'EN', currency: str = 'USD'):
    """
    Args:
        campaign_name (str): Имя рекламной кампании.
        category_name (str): Название категории.
        language (str, optional): Язык. Defaults to 'EN'.
        currency (str, optional): Валюта. Defaults to 'USD'.

    Returns:
        None
    
    """
    super().__init__(campaign_name, category_name, language, currency)
```