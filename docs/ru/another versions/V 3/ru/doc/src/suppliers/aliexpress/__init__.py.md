# Модуль `aliexpress`

## Обзор

Модуль `aliexpress` предоставляет инструменты для работы с AliExpress, включая классы для взаимодействия с API AliExpress, управления кампаниями и генерации HTML-кода для представления товаров и категорий.

## Подробней

Этот модуль предназначен для упрощения интеграции с AliExpress. Он включает в себя классы для выполнения запросов к API, обработки ответов и управления рекламными кампаниями. Модуль также предоставляет функциональность для автоматической генерации HTML-кода, который может быть использован для отображения товаров и категорий на веб-сайтах или в рекламных материалах.

## Содержание

- [Классы](#Классы)
    - [Aliexpress](#Aliexpress)
    - [AliApi](#AliApi)
    - [AliRequests](#AliRequests)
    - [AliCampaignEditor](#AliCampaignEditor)
    - [ProductHTMLGenerator](#ProductHTMLGenerator)
    - [CategoryHTMLGenerator](#CategoryHTMLGenerator)
    - [CampaignHTMLGenerator](#CampaignHTMLGenerator)
- [Импортированные модули](#Импортированные-модули)

## Классы

### `Aliexpress`

**Описание**: Класс для работы с AliExpress.
### `AliApi`

**Описание**: Класс для взаимодействия с API AliExpress.

### `AliRequests`

**Описание**: Класс для выполнения запросов к AliExpress.

### `AliCampaignEditor`

**Описание**: Класс для управления кампаниями AliExpress.

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для товаров.

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для категорий.

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для кампаний.

## Импортированные модули

- `aliexpress`:  Импортирует класс `Aliexpress` из модуля `.aliexpress`.
- `aliapi`: Импортирует класс `AliApi` из модуля `.aliapi`.
- `alirequests`: Импортирует класс `AliRequests` из модуля `.alirequests`.
- `campaign`: Импортирует класс `AliCampaignEditor` из модуля `.campaign`.
- `campaign.html_generators`: Импортирует классы `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator` из модуля `.campaign.html_generators`.