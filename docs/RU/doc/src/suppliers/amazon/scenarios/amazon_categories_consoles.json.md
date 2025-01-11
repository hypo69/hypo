# Документация для `amazon_categories_consoles.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценария импорта товаров категории "Consoles Entrance chests" из Amazon. Он определяет URL, условие (condition) товара, категории PrestaShop и правило ценообразования.

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [Сценарии](#сценарии)
        - [`Consoles Entrance chests`](#consoles-entrance-chests)

## Структура JSON

### Сценарии
Здесь определены сценарии импорта.

#### `Consoles Entrance chests`
**Описание**: Сценарий для импорта товаров из категории "Consoles Entrance chests".

**Параметры**:
-   `url` (str): URL-адрес страницы Amazon, с которой производится импорт товаров. В данном случае `https://amzn.to/3K1wqqD`.
-   `condition` (str): Условие товара. В данном случае `new` (новый).
-   `presta_categories` (dict): Категории PrestaShop, в которые будут импортированы товары.
    -   `default_category` (dict): Категории по умолчанию. В данном случае `{"11199": "Consoles Entrance chests"}` , где ключ - ID категории, а значение - её название.
    -   `additional_categories` (list): Список дополнительных категорий. В данном случае пустой список `[""]`.
-   `price_rule` (int): Правило ценообразования. В данном случае `1`.