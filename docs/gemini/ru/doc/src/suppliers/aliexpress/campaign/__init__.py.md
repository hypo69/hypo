# Модуль управления рекламными кампаниями Aliexpress

## Обзор

Модуль `src.suppliers.aliexpress.campaign` предоставляет инструменты для управления рекламными кампаниями на платформе Aliexpress. Он включает в себя функциональность для редактирования кампаний, подготовки данных, генерации HTML и интеграции с Google Sheets.

## Содержание

- [Константы](#константы)
- [Классы](#классы)
  - [`AliCampaignEditor`](#alicampaigneditor)
- [Функции](#функции)
  - [`process_campaign`](#process_campaign)
  - [`process_campaign_category`](#process_campaign_category)
  - [`process_all_campaigns`](#process_all_campaigns)
- [Классы генерации HTML](#классы-генерации-html)
  - [`CategoryHTMLGenerator`](#categoryhtmlgenerator)
  - [`ProductHTMLGenerator`](#producthtmlgenerator)

## Константы

### `MODE`

- **Описание**: Режим работы модуля. По умолчанию установлен в `'dev'`.
  
  
  
  
## Классы

### `AliCampaignEditor`

- **Описание**: Класс для редактирования рекламных кампаний Aliexpress. Более подробная документация в файле `ali_campaign_editor.py`

## Функции

### `process_campaign`

- **Описание**: Функция для обработки конкретной рекламной кампании. Более подробная информация в файле `prepare_campaigns.py`

### `process_campaign_category`

- **Описание**: Функция для обработки рекламных кампаний по категориям. Более подробная информация в файле `prepare_campaigns.py`

### `process_all_campaigns`

- **Описание**: Функция для обработки всех рекламных кампаний. Более подробная информация в файле `prepare_campaigns.py`

## Классы генерации HTML

### `CategoryHTMLGenerator`
- **Описание**: Класс для генерации HTML-кода для категорий. Более подробная информация в файле `html_generators.py`

### `ProductHTMLGenerator`
- **Описание**: Класс для генерации HTML-кода для товаров. Более подробная информация в файле `html_generators.py`