# Модуль `src.endpoints.prestashop.api`

## Обзор

Модуль `src.endpoints.prestashop.api` предоставляет интерфейс для взаимодействия с API PrestaShop. Он содержит классы и функции для синхронного и асинхронного доступа к API PrestaShop.

## Подорбней

Этот модуль предназначен для упрощения интеграции с PrestaShop, предоставляя удобные инструменты для выполнения запросов к API и обработки ответов. Он включает в себя как синхронные, так и асинхронные реализации, что позволяет разработчикам выбирать наиболее подходящий подход в зависимости от требований их проекта. Модуль экспортирует классы `PrestaShop` и `PrestaShopAsync`, которые инкапсулируют логику взаимодействия с API.

## Функции

### `PrestaShop`

```python
from .api import PrestaShop
```

**Описание**: Импортирует класс `PrestaShop` из модуля `.api`.

### `PrestaShopAsync`

```python
from .api_async import PrestaShopAsync
```

**Описание**: Импортирует класс `PrestaShopAsync` из модуля `.api_async`.