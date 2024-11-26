How to Use the Product Fields in `hypotez/src/product/product_fields/fields_list.txt`

This document provides a guide to the various product fields defined in the `hypotez/src/product/product_fields/fields_list.txt` file.  Understanding these fields is crucial for accurately and comprehensively representing products within your system.

**Categorizing the Fields:**

The fields can be broadly grouped into categories for better understanding:

* **Product Identification & Metadata:** `id_product`, `link_rewrite`, `name`, `reference`, `supplier_reference`, `mpn`, `isbn`, `upc`, `ean13`, `id_category_default`, `id_manufacturer`, `id_supplier`, `id_shop`, `id_shop_default`, `id_type_redirected`, `id_default_image`, `id_default_combination`, `locale`.  These fields uniquely identify and describe the product, its associated categories, manufacturers, and suppliers.

* **Product Attributes & Details:** `description`, `description_short`, `how_to_use`, `specification`, `ingredients`, `associations`, `product_type`, `customizable`, `text_fields`. These fields provide detailed information about the product, including its features, usage instructions, specifications, ingredients, and any associated items.

* **Pricing & Availability:** `price`, `wholesale_price`, `unit_price_ratio`, `minimal_quantity`, `quantity_discount`, `available_date`, `available_now`, `available_later`, `available_for_order`, `out_of_stock`, `low_stock_alert`, `low_stock_threshold`, `on_sale`, `online_only`, `delivery_in_stock`, `delivery_out_of_stock`, `show_price`.  This group handles pricing, availability, and discounts for the product.

* **Shipping & Logistics:** `additional_delivery_times`, `additional_shipping_cost`, `depth`, `height`, `weight`, `width`, `volume`, `pack_stock_type`, `unity`. These fields deal with shipping information and packaging details.

* **Marketing & Display:** `meta_title`, `meta_description`, `meta_keywords`, `affliate_short_link`, `affliate_summary`, `affliate_summary_2`, `affliate_text`, `affliate_image_large`, `affliate_image_medium`, `affliate_image_small`, `show_condition`.  These fields support marketing and display of the product.

* **Stock Management:** `advanced_stock_management`, `quantity_discount`, `low_stock_alert`, `low_stock_threshold`, `pack_stock_type`, `available_now`, `available_later`.  These fields provide tools for managing stock levels and tracking availability.

* **Conditions and States:** `condition`, `show_condition`, `state`,  This section manages product conditions like new, used, refurbished, etc.

* **Attachments and Files:** `uploadable_files`, `cache_has_attachments`, `local_saved_image`, `local_saved_video`. This section deals with any files associated with the product.

* **Redirects & Special Handling:** `redirect_type`, `cache_default_attribute`, `cache_is_pack`. These fields handle redirects or specialized processing needs.

**Recommendations:**

* **Data Validation:** Ensure robust validation checks for each field to maintain data integrity.  Consider the data type for each field (e.g., numerical for price, text for description).

* **Documentation:** Document the allowed values for each field.  If applicable, include examples and potential error messages for user reference.  This will save valuable troubleshooting time.

* **Field Usage:**  Specify how each field should be used in the context of your application.  For example,  how are `quantity_discount` and `minimal_quantity` interrelated?

* **Scalability:** Design your code to handle a potentially large volume of products and associated data.


This guide aims to provide a high-level overview.  More specific instructions on using individual fields may be found in other sections of the `hypotez` codebase or through debugging your application. Remember to consult the context of your application to understand how these fields are used together.