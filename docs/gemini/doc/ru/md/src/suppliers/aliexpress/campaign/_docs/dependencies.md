# Модуль управления кампаниями AliExpress

## Обзор

Данный модуль предоставляет инструменты для управления кампаниями на AliExpress. Он включает в себя функции для редактирования, подготовки и управления промо-кампаниями. Модуль использует Google Sheets для хранения и обработки данных, а также предоставляет возможность интеграции с другими системами.


## Оглавление

* [Модуль управления кампаниями AliExpress](#модуль-управления-кампаниями-aliexpress)
* [Обзор](#обзор)
* [Файлы модуля](#файлы-модуля)
* [Классы](#классы)
* [Функции](#функции)
* [Зависимости](#зависимости)

## Файлы модуля

- `__init__.py`: Инициализирует модуль.
- `ali_campaign_editor.py`: Основной логический файл для редактирования кампаний AliExpress.
- `ali_promo_campaign.py`: Управляет рекламными кампаниями AliExpress.
- `gsheet.py`: Обрабатывает взаимодействие с Google Sheets для данных кампаний.
- `header.py`: Общие функции и классы, используемые в модуле.
- `prepare_campaigns.py`: Подготовка и организация данных для кампаний.
- `ttypes.py`: Определяет типы и структуры, используемые в модуле.
- `version.py`: Содержит информацию о версии модуля.

## Классы

Не определены классы.


## Функции

Не определены функции.


## Зависимости

Модуль использует следующие зависимости:

- `gspread` (для работы с Google Sheets)
- `pandas` (для работы с данными в формате таблиц)
- `src.settings.gs` (для настроек Google Sheets)
- `AliCampaignGoogleSheet` (из `src.suppliers.aliexpress`)