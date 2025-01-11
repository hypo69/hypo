# Модуль `src.endpoints`

## Обзор

Модуль `src.endpoints` предназначен для интеграции с различными внешними сервисами и API. В текущей версии модуля содержатся импорты для интеграции с PrestaShop и Telegram-ботом Kazarinov. Модуль обеспечивает централизованную точку доступа для запросов к различным сервисам.

## Содержание

1. [Обзор](#обзор)
2. [Импорты](#импорты)

## Импорты

В текущей версии файла импортируются следующие модули:

-  `PrestaShop`, `PrestaCategory`, `PrestaCustomer`, `PrestaLanguage`, `PrestaProduct`, `PrestaShopShop`, `PrestaSupplier`, `PrestaWarehouse`, `PriceListRequester` из модуля `src.endpoints.prestashop`. Эти импорты позволяют взаимодействовать с API PrestaShop для управления магазинами, категориями, клиентами, продуктами и т.д. (закомментировано в текущей версии файла).
- `KazarinovTelegramBot` из модуля `src.endpoints.kazarinov`. Этот импорт позволяет взаимодействовать с Telegram-ботом Kazarinov (закомментировано в текущей версии файла).