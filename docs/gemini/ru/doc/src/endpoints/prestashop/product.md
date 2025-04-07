# Документация для работы с данными о продуктах в PrestaShop (product.md)

## Обзор

Этот документ предназначен для разработчиков, работающих с данными о продуктах в PrestaShop. Здесь представлено описание структуры JSON, используемой для создания и обновления информации о продуктах через API PrestaShop. Описаны ключевые поля, их назначение и требования к формату данных.

## Подробней

В этом файле описывается структура данных в формате JSON, которая используется для обмена информацией о продуктах с PrestaShop. Он содержит спецификации для различных полей продукта, включая идентификаторы, цены, описания, метаданные и связи с другими сущностями, такими как категории и изображения. Этот файл служит руководством для понимания структуры запросов API, необходимых для работы с продуктами в PrestaShop. Также приводятся примеры использования API для создания продуктов.

## Структура JSON для данных о продукте

### `product`

Корневой элемент, содержащий все данные о продукте.

#### Общие поля

*   `id_default_combination`: ID комбинации по умолчанию (если есть комбинации).  `null`, если нет комбинаций.
*   `id_tax_rules_group`: ID группы налогов. Важно! Должно существовать в Prestashop.
*   `id_manufacturer`: ID производителя.
*   `id_supplier`: ID поставщика.
*   `reference`: Артикул.
*   `ean13`: EAN-13 штрихкод.
*   `upc`: UPC штрихкод.
*   `ecotax`: Экологический налог.
*   `quantity`: Количество на складе.
*   `minimal_quantity`: Минимальное количество для заказа.
*   `price`: Цена (без налога).  Обратите внимание на формат (дробное число).
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

#### `associations`

Ассоциации с другими сущностями.

*   `categories`: Массив категорий, к которым принадлежит продукт. `id` категорий должны существовать.
*   `images`: Массив ID изображений, связанных с продуктом. `id` изображений должны существовать (обычно сначала загружаются изображения, а потом привязываются к продукту).

#### Многоязычные поля

*   `name`: Название продукта (для каждого языка).
*   `description`: Полное описание продукта (для каждого языка).
*   `description_short`: Краткое описание продукта (для каждого языка).
*   `meta_title`: Мета-заголовок (для каждого языка).
*   `meta_description`: Мета-описание (для каждого языка).
*   `meta_keywords`: Мета-ключевые слова (для каждого языка).
*   `link_rewrite`: URL-адрес (для каждого языка). Генерируется автоматически на основе названия, но можно указать вручную. Важно, чтобы был уникальным.
*   `available_now`: Текст, отображаемый, когда товар в наличии.
*   `available_later`: Текст, отображаемый, когда товара нет в наличии.

## Пример использования (Python)

```python
import requests
import json

API_URL = "http://your-prestashop-domain/api/products"  # Замените
API_KEY = "YOUR_API_KEY"  # Замените

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
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
    print("Product created successfully!")
    print(response.json()) # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"Error creating product: {e}")
    if response is not None:
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}") # Print the response content for debugging