html
<h1>Module: hypotez/src/endpoints/prestashop/api_schemas/api_resourses_list.py</h1>

<h2>Overview</h2>
<p>This module defines a list of all available resources for API calls. It's used to specify the endpoints for different data points within a PrestaShop application. The list is stored in a variable called <code>resource</code>.  The module also defines a constant <code>MODE</code>.</p>

<h2>Variables</h2>

<h3><code>resource</code></h3>

<p><strong>Description</strong>: A list containing strings representing the available resources for the API.  Each string corresponds to a specific data endpoint.</p>

<p><strong>Value</strong>:</p>
<pre><code>
['products', 'categories', 'attachments', 'addresses', 'carriers', 'cart_rules', 'carts', 'countries', 'content_management_system', 'currencies', 'customer_messages', 'customer_threads', 'customers', 'customizations', 'deliveries', 'employees', 'groups', 'guests', 'image_types', 'customizations', 'images', 'languages', 'manufacturers', 'messages', 'order_carriers', 'order_cart_rules', 'order_details', 'order_histories', 'order_invoices', 'order_payments', 'order_slip', 'order_states', 'orders', 'price_ranges', 'product_customization_fields', 'product_feature_values', 'product_features', 'product_option_values', 'product_options', 'product_suppliers', 'products', 'search', 'shop_groups', 'shop_urls', 'shops', 'specific_price_rules', 'specific_prices', 'states', 'stock_availables', 'stock_movement_reasons', 'stock_movements', 'stocks', 'stores', 'suppliers', 'supply_order_details', 'supply_order_receipt_histories', 'supply_order_states', 'supply_orders', 'tags', 'tax_rule_groups', 'tax_rules', 'taxes', 'translated_configurations', 'warehouse_product_locations', 'warehouses', 'weight_ranges', 'zones']
</code></pre>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A string constant defining the current mode (e.g., 'dev', 'prod').</p>

<p><strong>Value</strong>: 'dev'</p>

<h2>Module Docstring</h2>
<p>The module includes a multiline docstring that contains metadata about the module (platform and synopsis). It provides a more descriptive overview of the module and its purpose, but it is not used for the generated API directly.</p>