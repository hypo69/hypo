# Список ресурсов API PrestaShop

## Обзор

Этот модуль определяет список доступных ресурсов для API вызовов PrestaShop. Он содержит константное значение `resource:list` с перечислением всех поддерживаемых ресурсов.

## Переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, 'dev', 'prod').

**Значение**: `'dev'`

### `resource:list`

**Описание**: Список доступных ресурсов API.

**Значение**: Список строк, представляющих названия ресурсов.

## Список ресурсов

```
products, categories, attachments, addresses, carriers, cart_rules, carts, countries, content_management_system, currencies, customer_messages, customer_threads, customers, customizations, deliveries, employees, groups, guests, image_types, customizations, images, languages, manufacturers, messages, order_carriers, order_cart_rules, order_details, order_histories, order_invoices, order_payments, order_slip, order_states, orders, price_ranges, product_customization_fields, product_feature_values, product_features, product_option_values, product_options, product_suppliers, products, search, shop_groups, shop_urls, shops, specific_price_rules, specific_prices, states, stock_availables, stock_movement_reasons, stock_movements, stocks, stores, suppliers, supply_order_details, supply_order_receipt_histories, supply_order_states, supply_orders, tags, tax_rule_groups, tax_rules, taxes, translated_configurations, warehouse_product_locations, warehouses, weight_ranges, zones
```
```
```
```python
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.prestashop.api_schemas
	:platform: Windows, Unix
	:synopsis: Список всех доступных ресурсов для API вызовов
"""
MODE = 'dev'

resource:list = [
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