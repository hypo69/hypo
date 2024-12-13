# Категории AliExpress и PrestaShop

## Обзор

Этот файл `category_aliexpress_prestashop.json` содержит информацию о соответствии категорий товаров на AliExpress и PrestaShop. Данные представлены в формате JSON, где ключи - это идентификаторы категорий AliExpress, а значения - это объекты с информацией о названии категории AliExpress, родительской категории, связанных категориях PrestaShop и основной категории PrestaShop.

## Структура данных

### JSON

JSON объект представляет собой словарь, где:

-   **Ключи (keys)**: Идентификаторы категорий AliExpress (например, `"39"`).
-   **Значения (values)**: Объекты, содержащие следующую информацию:
    -   `ali_category_name` (str): Название категории на AliExpress.
    -   `ali_parent` (str): Идентификатор родительской категории на AliExpress. Пустая строка `""`, если категория является корневой.
    -   `PrestaShop_categories` (list): Список связанных категорий PrestaShop (может быть пуст).
    -   `PrestaShop_main_category` (str): Основная категория PrestaShop, к которой относится данная категория AliExpress. Пустая строка `""`, если основная категория не задана.

### Пример

```json
{
  "39": {
    "ali_category_name": "Lights & Lighting",
    "ali_parent": "",
    "PrestaShop_categories": [],
    "PrestaShop_main_category": ""
  },
  "1504": {
    "ali_category_name": "Indoor Lighting",
    "ali_parent": "39",
    "PrestaShop_categories": [],
    "PrestaShop_main_category": ""
  }
}
```

В данном примере:
- Категория AliExpress с идентификатором `"39"` называется "Lights & Lighting", является корневой категорией, и пока не имеет связанных категорий PrestaShop и основной категории.
- Категория AliExpress с идентификатором `"1504"` называется "Indoor Lighting", является дочерней категорией `"39"`, и пока не имеет связанных категорий PrestaShop и основной категории.

## Использование

Данный файл используется для:

- Сопоставления категорий товаров AliExpress с категориями PrestaShop.
- Автоматизации импорта товаров с AliExpress в PrestaShop.
- Организации и структурирования категорий товаров в PrestaShop на основе данных AliExpress.

## Зависимости

Файл не имеет зависимостей.