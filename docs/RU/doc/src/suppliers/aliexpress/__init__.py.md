# Модуль `src.suppliers.aliexpress`

## Обзор

Модуль `src.suppliers.aliexpress` предоставляет инструменты для работы с AliExpress. Он включает в себя классы для взаимодействия с API AliExpress, выполнения запросов, редактирования кампаний и генерации HTML для различных компонентов.

## Содержание

- [Обзор](#обзор)
- [Переменные](#переменные)
- [Импорты](#импорты)

## Переменные

### `MODE`

- **Описание**: Определяет режим работы модуля. В данном случае установлен в `'dev'`.

## Импорты

### `from .aliexpress import Aliexpress`

- **Описание**: Импортирует класс `Aliexpress` из модуля `aliexpress`.

### `from .aliapi import AliApi`

- **Описание**: Импортирует класс `AliApi` из модуля `aliapi`.

### `from .alirequests import AliRequests`

- **Описание**: Импортирует класс `AliRequests` из модуля `alirequests`.

### `from .campaign import AliCampaignEditor`

- **Описание**: Импортирует класс `AliCampaignEditor` из модуля `campaign`.

### `from .campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator`

- **Описание**: Импортирует классы `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator` из модуля `html_generators` в пакете `campaign`.