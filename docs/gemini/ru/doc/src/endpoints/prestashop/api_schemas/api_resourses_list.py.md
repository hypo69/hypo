# Модуль api_resourses_list

## Обзор

Модуль `api_resourses_list.py` содержит список всех доступных ресурсов для API вызовов в PrestaShop. Этот список используется для определения того, какие ресурсы могут быть запрошены через API.

## Подробней

Этот модуль предоставляет константу `resource`, которая представляет собой список строк. Каждая строка в списке — это название API ресурса, доступного в PrestaShop. Этот список важен для настройки и определения доступных путей API, и используется для валидации и маршрутизации запросов к API PrestaShop.

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

**Описание**: Список всех доступных ресурсов API PrestaShop.

**Назначение**: Предоставляет перечень допустимых значений для работы с API PrestaShop.

**Пример**:

```python
# Пример использования списка resource для проверки доступности ресурса
resource_name = 'products'
if resource_name in resource:
    print(f'Ресурс {resource_name} доступен через API')
else:
    print(f'Ресурс {resource_name} не доступен через API')