# api_resourses_list.py

## Обзор

Модуль содержит список всех доступных ресурсов для API вызовов PrestaShop. Этот список используется для определения того, с какими сущностями можно взаимодействовать через API.

## Подробней

Этот файл содержит единственный объект `resource`, который является списком строк. Каждая строка в списке представляет собой название ресурса, доступного через API PrestaShop. Этот список используется для валидации запросов и определения доступных операций. Он позволяет разработчикам понимать, с какими данными они могут работать через API, такими как продукты, категории, клиенты и т. д. <инструкция для модели gemini:Список используется для автоматической генерации документации и проверки корректности запросов к API.>

## Переменные

### `resource`

```python
resource: list = [
    'products',
    'categories',
    'attachments',
    'addresses',
    'carriers',
    'cart_rules',
    'carts',
    'countries',
    'content_management_system',
    'currencies',
    'customer_messages',
    'customer_threads',
    'customers',
    'customizations',
    'deliveries',
    'employees',
    'groups',
    'guests',
    'image_types',
    'customizations',
    'images',
    'languages',
    'manufacturers',
    'messages',
    'order_carriers',
    'order_cart_rules',
    'order_details',
    'order_histories',
    'order_invoices',
    'order_payments',
    'order_slip',
    'order_states',
    'orders',
    'price_ranges',
    'product_customization_fields',
    'product_feature_values',
    'product_features',
    'product_option_values',
    'product_options',
    'product_suppliers',
    'products',
    'search',
    'shop_groups',
    'shop_urls',
    'shops',
    'specific_price_rules',
    'specific_prices',
    'states',
    'stock_availables',
    'stock_movement_reasons',
    'stock_movements',
    'stocks',
    'stores',
    'suppliers',
    'supply_order_details',
    'supply_order_receipt_histories',
    'supply_order_states',
    'supply_orders',
    'tags',
    'tax_rule_groups',
    'tax_rules',
    'taxes',
    'translated_configurations',
    'warehouse_product_locations',
    'warehouses',
    'weight_ranges',
    'zones',
]
```

**Описание**: Список строк, представляющих доступные ресурсы API PrestaShop.

**Как работает переменная**:
Переменная `resource` представляет собой список строк, каждая из которых является названием ресурса, доступного через API PrestaShop. Этот список используется для определения того, с какими сущностями можно взаимодействовать через API, такими как продукты, категории, клиенты и т. д. Этот список может быть использован для валидации запросов и автоматической генерации документации.