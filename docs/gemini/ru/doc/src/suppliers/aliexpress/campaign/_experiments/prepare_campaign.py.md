# Модуль для подготовки рекламной кампании AliExpress

## Обзор

Модуль `prepare_campaign.py` предназначен для подготовки и создания рекламной кампании AliExpress. Он включает в себя функциональность для проверки существования рекламной кампании и, при необходимости, создания новой.

## Подробней

Этот модуль является частью процесса управления рекламными кампаниями AliExpress. Он использует функцию `process_campaign` из модуля `src.suppliers.aliexpress.campaign` для создания или обновления рекламной кампании.
Анализ модуля показывает, что его основная задача - инициировать процесс создания или обновления рекламной кампании, используя имя кампании, язык и валюту.

## Функции

### `process_campaign`

```python
process_campaign(campaign_name: str) -> None
```

**Назначение**: Создает или обновляет рекламную кампанию на AliExpress.

**Параметры**:

-   `campaign_name` (str): Имя рекламной кампании.

**Возвращает**:

-   `None`: Функция ничего не возвращает.

**Как работает функция**:

1.  Функция `process_campaign` принимает имя кампании в качестве аргумента.
2.  Она вызывает функцию `process_campaign` из модуля `src.suppliers.aliexpress.campaign`, передавая ей имя кампании.

    ```ascii
    Начало
    ↓
    Передача campaign_name в process_campaign
    ↓
    Вызов process_campaign из src.suppliers.aliexpress.campaign
    ↓
    Конец
    ```

**Примеры**:

```python
process_campaign(campaign_name='brands')
```

В этом примере вызывается функция `process_campaign` с именем кампании `'brands'`.

## Переменные модуля

-   `locales` (dict): Словарь, содержащий соответствия между языками и валютами.
    Пример:
    `{'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}`
-   `language` (str): Язык рекламной кампании. По умолчанию `'EN'`.
-   `currency` (str): Валюта рекламной кампании. По умолчанию `'USD'`.
-   `campaign_name` (str): Имя рекламной кампании. По умолчанию `'brands'`.

```python
locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
language: str = 'EN'
currency: str = 'USD'
campaign_name:str = 'brands'