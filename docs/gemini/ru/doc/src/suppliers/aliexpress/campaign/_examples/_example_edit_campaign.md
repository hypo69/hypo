# Модуль `hypotez/src/suppliers/aliexpress/campaign/_examples/_example_edit_campaign.py`

## Обзор

Этот модуль содержит пример реализации редактора рекламных кампаний для AliExpress. Он предоставляет класс `AliCampaignEditor`, наследующийся от `AliPromoCampaign`, для работы с рекламными кампаниями.  Модуль включает вспомогательные функции для работы с данными, такие как парсинг и форматирование.

## Оглавление

* [Модуль `AliCampaignEditor`](#модуль-alicampaigneditor)
* [Функции](#функции)


## Модуль `AliCampaignEditor`

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования рекламных кампаний AliExpress. Он предоставляет методы для управления различными аспектами кампаний. Наследует от `AliPromoCampaign`.

**Методы**:

* `__init__(self, campaign_name: str, category_name: str, language: str = 'EN', currency: str = 'USD')`:  Инициализирует экземпляр `AliCampaignEditor`.
    * **Описание**: Конструктор класса.
    * **Параметры**:
        * `campaign_name` (str): Название рекламной кампании.
        * `category_name` (str): Название категории.
        * `language` (str, опционально): Язык кампании (по умолчанию 'EN').
        * `currency` (str, опционально): Валюта кампании (по умолчанию 'USD').
    * **Возвращает**:
        * None.


## Функции

Пока в модуле нет других функций, помимо методов класса `AliCampaignEditor`.


```