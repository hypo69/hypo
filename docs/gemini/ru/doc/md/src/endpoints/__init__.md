# Модуль hypotez/src/endpoints

## Обзор

Этот модуль содержит определения и импорты для различных конечных точек, используемых в проекте.  Он предоставляет классы для работы с данными из разных источников (например, PrestaShop, Kazarinov).

## Импорты

Модуль импортирует следующие классы и объекты:

- `PrestaShop`, `PrestaCategory`, `PrestaCustomer`, `PrestaLanguage`, `PrestaProduct`, `PrestaShopShop`, `PrestaSupplier`, `PrestaWarehouse`, `PriceListRequester` из подмодуля `.prestashop`
- `KazarinovTelegramBot` из подмодуля `.kazarinov`

## Переменные

### `MODE`

**Описание**:  Указывает режим работы приложения (например, 'dev', 'prod').


## Подмодули

### `prestashop`

Содержит классы для взаимодействия с API PrestaShop.  Подробная документация по этим классам находится в файле `hypotez/src/endpoints/prestashop.py`.


### `kazarinov`

Содержит классы для взаимодействия с ботом Kazarinov Telegram.  Подробная документация по этим классам находится в файле `hypotez/src/endpoints/kazarinov.py`.