# Модуль: Список доступных ресурсов API PrestaShop

## Обзор

Этот модуль содержит список всех доступных ресурсов для API вызовов PrestaShop. Он предоставляет централизованный перечень ресурсов, которые могут быть использованы для взаимодействия с API PrestaShop.

## Подробней

Модуль `api_resourses_list.py` предназначен для хранения списка ресурсов API PrestaShop. Этот список может использоваться для динамической генерации документации, автоматической проверки доступности ресурсов или для других целей, связанных с интеграцией и взаимодействием с API PrestaShop.

## Переменные

### `resource`

```python
resource: list
```

**Описание**: Список ресурсов API PrestaShop.

**Принцип работы**:
Переменная `resource` представляет собой список строк, где каждая строка является названием ресурса API PrestaShop. Этот список содержит все доступные ресурсы, такие как продукты, категории, заказы и т.д.

**Пример**:

```python
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

**Назначение каждой переменной в списке**:

- `'products'`: Ресурс для управления продуктами.
- `'categories'`: Ресурс для управления категориями продуктов.
- `'attachments'`: Ресурс для управления прикрепленными файлами.
- `'addresses'`: Ресурс для управления адресами.
- `'carriers'`: Ресурс для управления службами доставки.
- `'cart_rules'`: Ресурс для управления правилами корзины.
- `'carts'`: Ресурс для управления корзинами.
- `'countries'`: Ресурс для управления странами.
- `'content_management_system'`: Ресурс для управления контентом CMS.
- `'currencies'`: Ресурс для управления валютами.
- `'customer_messages'`: Ресурс для управления сообщениями клиентов.
- `'customer_threads'`: Ресурс для управления темами клиентов.
- `'customers'`: Ресурс для управления клиентами.
- `'customizations'`: Ресурс для управления настройками.
- `'deliveries'`: Ресурс для управления доставками.
- `'employees'`: Ресурс для управления сотрудниками.
- `'groups'`: Ресурс для управления группами клиентов.
- `'guests'`: Ресурс для управления гостями.
- `'image_types'`: Ресурс для управления типами изображений.
- `'images'`: Ресурс для управления изображениями.
- `'languages'`: Ресурс для управления языками.
- `'manufacturers'`: Ресурс для управления производителями.
- `'messages'`: Ресурс для управления сообщениями.
- `'order_carriers'`: Ресурс для управления службами доставки заказов.
- `'order_cart_rules'`: Ресурс для управления правилами корзины заказов.
- `'order_details'`: Ресурс для управления деталями заказов.
- `'order_histories'`: Ресурс для управления историей заказов.
- `'order_invoices'`: Ресурс для управления счетами заказов.
- `'order_payments'`: Ресурс для управления платежами заказов.
- `'order_slip'`: Ресурс для управления платежными квитанциями заказов.
- `'order_states'`: Ресурс для управления статусами заказов.
- `'orders'`: Ресурс для управления заказами.
- `'price_ranges'`: Ресурс для управления диапазонами цен.
- `'product_customization_fields'`: Ресурс для управления полями настройки продуктов.
- `'product_feature_values'`: Ресурс для управления значениями характеристик продуктов.
- `'product_features'`: Ресурс для управления характеристиками продуктов.
- `'product_option_values'`: Ресурс для управления значениями опций продуктов.
- `'product_options'`: Ресурс для управления опциями продуктов.
- `'product_suppliers'`: Ресурс для управления поставщиками продуктов.
- `'search'`: Ресурс для выполнения поиска.
- `'shop_groups'`: Ресурс для управления группами магазинов.
- `'shop_urls'`: Ресурс для управления URL магазинов.
- `'shops'`: Ресурс для управления магазинами.
- `'specific_price_rules'`: Ресурс для управления правилами специальных цен.
- `'specific_prices'`: Ресурс для управления специальными ценами.
- `'states'`: Ресурс для управления штатами/областями.
- `'stock_availables'`: Ресурс для управления доступностью на складе.
- `'stock_movement_reasons'`: Ресурс для управления причинами движения запасов.
- `'stock_movements'`: Ресурс для управления движениями запасов.
- `'stocks'`: Ресурс для управления запасами.
- `'stores'`: Ресурс для управления магазинами (физическими).
- `'suppliers'`: Ресурс для управления поставщиками.
- `'supply_order_details'`: Ресурс для управления деталями заказов поставок.
- `'supply_order_receipt_histories'`: Ресурс для управления историей получения заказов поставок.
- `'supply_order_states'`: Ресурс для управления статусами заказов поставок.
- `'supply_orders'`: Ресурс для управления заказами поставок.
- `'tags'`: Ресурс для управления тегами.
- `'tax_rule_groups'`: Ресурс для управления группами налоговых правил.
- `'tax_rules'`: Ресурс для управления налоговыми правилами.
- `'taxes'`: Ресурс для управления налогами.
- `'translated_configurations'`: Ресурс для управления переведенными конфигурациями.
- `'warehouse_product_locations'`: Ресурс для управления местоположениями продуктов на складе.
- `'warehouses'`: Ресурс для управления складами.
- `'weight_ranges'`: Ресурс для управления диапазонами веса.
- `'zones'`: Ресурс для управления зонами.