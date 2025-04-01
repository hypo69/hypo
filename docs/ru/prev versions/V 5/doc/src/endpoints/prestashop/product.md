# Документация для разработчика: `hypotez/src/endpoints/prestashop/product.md`

## Обзор

Этот файл содержит описание структуры JSON, используемой для создания и обновления товаров в PrestaShop API. Он предоставляет подробную информацию о каждом поле, его назначении и возможных значениях. Также содержит примеры использования на Python.

## Подробней

Этот файл предназначен для разработчиков, работающих с PrestaShop API и желающих автоматизировать процесс добавления или обновления товаров. Понимание структуры JSON и требований к данным необходимо для успешной интеграции и избежания ошибок. В файле подробно описаны все поля JSON, включая обязательные и необязательные параметры, их типы данных и допустимые значения. Это позволяет разработчикам создавать корректные запросы к API PrestaShop, обеспечивая успешное добавление и обновление товаров в магазине.

## Структура JSON для продукта PrestaShop

```json
{
  "product": {
    "id_default_combination": null,
    "id_tax_rules_group": "1",
    "id_manufacturer": "0",
    "id_supplier": "0",
    "reference": "REF-001",
    "ean13": "1234567890123",
    "upc": "987654321098",
    "ecotax": "0.000000",
    "quantity": "100",
    "minimal_quantity": "1",
    "price": "10.000000",
    "wholesale_price": "5.000000",
    "on_sale": "0",
    "online_only": "0",
    "unity": null,
    "unit_price": "0.000000",
    "reduction_price": "0.000000",
    "reduction_percent": "0.000000",
    "reduction_from": "0000-00-00",
    "reduction_to": "0000-00-00",
    "cache_is_pack": "0",
    "cache_has_attachments": "0",
    "cache_default_attribute": "0",
    "advanced_stock_management": "0",
    "pack_stock_type": "3",
    "state": "1",
    "available_for_order": "1",
    "show_price": "1",
    "visibility": "both",
    "id_category_default": "2",
    "associations": {
      "categories": [
        {
          "id": "2"
        }
      ],
      "images": [
        {
          "id": "1"
        }
      ]
    },
    "name": [
      {
        "language": {
          "id": "1"
        },
        "value": "Новый продукт"
      }
    ],
    "description": [
      {
        "language": {
          "id": "1"
        },
        "value": "<p>Описание нового продукта.</p>"
      }
    ],
    "description_short": [
      {
        "language": {
          "id": "1"
        },
        "value": "<p>Краткое описание нового продукта.</p>"
      }
    ],
    "meta_title": [
      {
        "language": {
          "id": "1"
        },
        "value": "Мета заголовок продукта"
      }
    ],
    "meta_description": [
      {
        "language": {
          "id": "1"
        },
        "value": "Мета описание продукта"
      }
    ],
    "meta_keywords": [
      {
        "language": {
          "id": "1"
        },
        "value": "ключевые слова, продукта"
      }
    ],
    "link_rewrite": [
      {
        "language": {
          "id": "1"
        },
        "value": "novyj-produkt"
      }
    ],
    "available_now": [
      {
        "language": {
          "id": "1"
        },
        "value": "В наличии"
      }
    ],
    "available_later": [
      {
        "language": {
          "id": "1"
        },
        "value": "Скоро в продаже"
      }
    ]
  }
}
```

### `product`

**Описание**: Корневой элемент, содержащий все данные продукта.

**Как работает класс**:
Класс представляет собой контейнер для всей информации о продукте, который будет отправлен в API PrestaShop. Он содержит поля, определяющие основные характеристики продукта, такие как цена, количество, описание и другие параметры.

## Общие поля

*   `id_default_combination`: ID комбинации по умолчанию (если есть комбинации). `null`, если нет комбинаций.
*   `id_tax_rules_group`: ID группы налогов. Важно! Должно существовать в Prestashop.
*   `id_manufacturer`: ID производителя.
*   `id_supplier`: ID поставщика.
*   `reference`: Артикул.
*   `ean13`: EAN-13 штрихкод.
*   `upc`: UPC штрихкод.
*   `ecotax`: Экологический налог.
*   `quantity`: Количество на складе.
*   `minimal_quantity`: Минимальное количество для заказа.
*   `price`: Цена (без налога). Обратите внимание на формат (дробное число).
*   `wholesale_price`: Оптовая цена.
*   `on_sale`: Показывать значок "Распродажа" (0 или 1).
*   `online_only`: Доступен только онлайн (0 или 1).
*   `unity`: Единица измерения (например, "шт").
*   `unit_price`: Цена за единицу измерения.
*   `reduction_price`: Скидка в валюте.
*   `reduction_percent`: Скидка в процентах.
*   `reduction_from`: Дата начала скидки.
*   `reduction_to`: Дата окончания скидки.
*   `cache_is_pack`: Является ли товар комплектом (0 или 1).
*   `cache_has_attachments`: Есть ли прикрепленные файлы (0 или 1).
*   `cache_default_attribute`: ID атрибута по умолчанию (для комбинаций).
*   `advanced_stock_management`: Использовать ли расширенное управление складом (0 или 1).
*   `pack_stock_type`: Тип управления складом для комплектов (1-3).
*   `state`: Активен (0 или 1).
*   `available_for_order`: Доступен для заказа (0 или 1).
*   `show_price`: Показывать цену (0 или 1).
*   `visibility`: Видимость (`both`, `catalog`, `search`, `none`).
*   `id_category_default`: ID категории по умолчанию. Важно! Должна существовать в Prestashop.

## `associations`

**Описание**: Ассоциации с другими сущностями.

**Как работает класс**:
Этот класс содержит информацию о связях продукта с другими сущностями в PrestaShop, такими как категории и изображения. Он позволяет указывать, к каким категориям принадлежит продукт и какие изображения связаны с ним.

### `categories`

Массив категорий, к которым принадлежит продукт. `id` категорий должны существовать.

### `images`

Массив ID изображений, связанных с продуктом. `id` изображений должны существовать (обычно сначала загружаются изображения, а потом привязываются к продукту).

## Многоязычные поля

*   `name`: Название продукта (для каждого языка).
*   `description`: Полное описание продукта (для каждого языка).
*   `description_short`: Краткое описание продукта (для каждого языка).
*   `meta_title`: Мета-заголовок (для каждого языка).
*   `meta_description`: Мета-описание (для каждого языка).
*   `meta_keywords`: Мета-ключевые слова (для каждого языка).
*   `link_rewrite`: URL-адрес (для каждого языка). Генерируется автоматически на основе названия, но можно указать вручную. Важно, чтобы был уникальным.
*   `available_now`: Текст, отображаемый, когда товар в наличии.
*   `available_later`: Текст, отображаемый, когда товара нет в наличии.

## Пример использования (Python):

```python
import requests
import json

API_URL = "http://your-prestashop-domain/api/products" # Замените
API_KEY = "YOUR_API_KEY" # Замените

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {API_KEY}"
}

data = {
  "product": {
    "id_default_combination": None,
    "id_tax_rules_group": "1",
    "reference": "REF-001",
    "quantity": "100",
    "price": "10.000000",
    "state": "1",
    "available_for_order": "1",
    "show_price": "1",
    "visibility": "both",
    "id_category_default": "2",
    "name": [
      {
        "language": {
          "id": "1"
        },
        "value": "Новый продукт"
      }
    ],
    "description_short": [
      {
        "language": {
          "id": "1"
        },
        "value": "<p>Краткое описание нового продукта.</p>"
      }
    ],
    "link_rewrite": [
      {
        "language": {
          "id": "1"
        },
        "value": "novyj-produkt"
      }
    ]
  }
}

try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response.raise
```