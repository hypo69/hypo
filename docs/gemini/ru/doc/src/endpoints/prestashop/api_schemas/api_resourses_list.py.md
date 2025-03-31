# Модуль api_resourses_list

## Обзор

Модуль `api_resourses_list.py` содержит список всех доступных ресурсов для API вызовов PrestaShop. Этот список используется для определения того, к каким ресурсам можно обращаться через API.

## Подробней

Этот файл предоставляет переменную `resource`, которая содержит список строк. Каждая строка в этом списке представляет собой имя ресурса, доступного через API PrestaShop. Этот список используется для валидации запросов к API и для автоматической генерации документации API.

## Переменные

### `resource`

**Описание**: Список ресурсов API PrestaShop.

**Как работает**:
Переменная `resource` представляет собой список строк, каждая из которых является названием доступного ресурса API PrestaShop.

**Пример**:

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