# Модуль `src.suppliers.aliexpress.campaign`

## Обзор

Модуль `src.suppliers.aliexpress.campaign` содержит классы и функции для управления рекламными кампаниями на платформе Aliexpress. Он включает в себя инструменты для редактирования кампаний, обработки данных, генерации HTML и другие вспомогательные функции.

## Содержание

- [Обзор](#обзор)
- [Модули](#модули)
    - [`AliCampaignEditor`](#alicampaigneditor)
    - [`process_campaign`](#process_campaign)
    - [`process_campaign_category`](#process_campaign_category)
    - [`process_all_campaigns`](#process_all_campaigns)
    - [`CategoryHTMLGenerator`](#categoryhtmlgenerator)
    - [`ProductHTMLGenerator`](#producthtmlgenerator)

## Модули

### `AliCampaignEditor`

Импортируется из `ali_campaign_editor.py`.
Класс для редактирования рекламных кампаний Aliexpress.

### `process_campaign`

Импортируется из `prepare_campaigns.py`.
Функция для обработки конкретной рекламной кампании.

### `process_campaign_category`

Импортируется из `prepare_campaigns.py`.
Функция для обработки рекламных кампаний по категориям.

### `process_all_campaigns`

Импортируется из `prepare_campaigns.py`.
Функция для обработки всех рекламных кампаний.

### `CategoryHTMLGenerator`

Импортируется из `html_generators.py`.
Класс для генерации HTML для категорий.

### `ProductHTMLGenerator`

Импортируется из `html_generators.py`.
Класс для генерации HTML для продуктов.