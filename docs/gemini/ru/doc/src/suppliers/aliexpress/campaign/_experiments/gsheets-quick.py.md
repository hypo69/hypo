# Модуль gsheets-quick.py

## Обзор

Модуль `gsheets-quick.py` предназначен для быстрой работы с Google Sheets в контексте кампаний AliExpress. Он использует библиотеку `gspread` для взаимодействия с Google Sheets и позволяет сохранять категории и кампании из рабочих листов.

## Подробней

Модуль является экспериментальным и служит для упрощения и ускорения процесса работы с Google Sheets. Основная цель модуля - автоматизация чтения и сохранения данных о кампаниях и категориях товаров AliExpress из Google Sheets. В коде создается экземпляр класса `AliCampaignGoogleSheet`, после чего вызываются методы для установки рабочего листа продуктов, сохранения категорий и сохранения кампании из рабочего листа.

## Функции

В данном коде не предоставлены классы и функции для документирования. Однако, опишем логику работы кода.

1.  **Инициализация параметров**:

    *   Определяются параметры кампании: `campaign_name`, `category_name`, `language` и `currency`.
    *   `campaign_name` (str): Название кампании ("lighting").
    *   `category_name` (str): Название категории ("chandeliers").
    *   `language` (str): Язык ("EN").
    *   `currency` (str): Валюта ("USD").
2.  **Создание экземпляра класса `AliCampaignGoogleSheet`**:

    *   Создается экземпляр класса `AliCampaignGoogleSheet` с использованием определенных параметров.
    *   `gs` = `AliCampaignGoogleSheet`(campaign\_name=campaign\_name, language=language, currency=currency)
3.  **Вызов методов для работы с Google Sheets**:

    *   Вызывается метод `set_products_worksheet` для установки рабочего листа продуктов.
        *   `gs.set_products_worksheet(category_name)`
    *   Вызывается метод `save_campaign_from_worksheet` для сохранения кампании из рабочего листа.
        *   `gs.save_campaign_from_worksheet()`

## ASCII flowchart:

```
    Начало
     ↓
Определение параметров кампании
     ↓
Создание экземпляра AliCampaignGoogleSheet
     ↓
Установка рабочего листа продуктов (set_products_worksheet)
     ↓
Сохранение кампании из рабочего листа (save_campaign_from_worksheet)
     ↓
    Конец
```

```python
campaign_name = "lighting"
category_name = "chandeliers"
language = 'EN'
currency = 'USD'

gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

gs.set_products_worksheet(category_name)
gs.save_campaign_from_worksheet()