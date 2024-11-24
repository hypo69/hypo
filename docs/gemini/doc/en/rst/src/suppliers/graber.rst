hypotez/src/suppliers/graber.py
=================================

.. module:: hypotez.src.suppliers.graber
   :platform: Windows, Unix
   :synopsis: Basic data grabbing class for all suppliers. For non-standard product field handling, just override the function in your class.
   :module: src.suppliers

   Example:
   ```python
   s = 'suppler_prefix'
   from src.suppliers import Graber
   locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

   class G(Graber):

       @close_pop_up()
       async def name(self, value: Any = None):
           self.fields.name = <Your implementation>
           )
   ```

Classes
-------

.. autoclass:: hypotez.src.suppliers.graber.Context
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hypotez.src.suppliers.graber.Graber
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.suppliers.graber.close_pop_up
   :noindex:

   
Methods
-------

.. automethod:: hypotez.src.suppliers.graber.Graber.error
.. automethod:: hypotez.src.suppliers.graber.Graber.set_field_value
.. automethod:: hypotez.src.suppliers.graber.Graber.grab_page
.. automethod:: hypotez.src.suppliers.graber.Graber.additional_shipping_cost
.. automethod:: hypotez.src.suppliers.graber.Graber.delivery_in_stock
.. automethod:: hypotez.src.suppliers.graber.Graber.active
.. automethod:: hypotez.src.suppliers.graber.Graber.additional_delivery_times
.. automethod:: hypotez.src.suppliers.graber.Graber.advanced_stock_management
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_short_link
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_summary
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_summary_2
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_text
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_image_large
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_image_medium
.. automethod:: hypotez.src.suppliers.graber.Graber.affiliate_image_small
.. automethod:: hypotez.src.suppliers.graber.Graber.available_date
.. automethod:: hypotez.src.suppliers.graber.Graber.available_for_order
.. automethod:: hypotez.src.suppliers.graber.Graber.available_later
.. automethod:: hypotez.src.suppliers.graber.Graber.available_now
.. automethod:: hypotez.src.suppliers.graber.Graber.cache_default_attribute
.. automethod:: hypotez.src.suppliers.graber.Graber.cache_has_attachments
.. automethod:: hypotez.src.suppliers.graber.Graber.cache_is_pack
.. automethod:: hypotez.src.suppliers.graber.Graber.condition
.. automethod:: hypotez.src.suppliers.graber.Graber.customizable
.. automethod:: hypotez.src.suppliers.graber.Graber.date_add
.. automethod:: hypotez.src.suppliers.graber.Graber.date_upd
.. automethod:: hypotez.src.suppliers.graber.Graber.delivery_out_stock
.. automethod:: hypotez.src.suppliers.graber.Graber.depth
.. automethod:: hypotez.src.suppliers.graber.Graber.description
.. automethod:: hypotez.src.suppliers.graber.Graber.description_short
.. automethod:: hypotez.src.suppliers.graber.Graber.id_category_default
.. automethod:: hypotez.src.suppliers.graber.Graber.id_default_combination
.. automethod:: hypotez.src.suppliers.graber.Graber.id_product
.. automethod:: hypotez.src.suppliers.graber.Graber.locale
.. automethod:: hypotez.src.suppliers.graber.Graber.id_default_image
.. automethod:: hypotez.src.suppliers.graber.Graber.ean13
.. automethod:: hypotez.src.suppliers.graber.Graber.ecotax
.. automethod:: hypotez.src.suppliers.graber.Graber.height
.. automethod:: hypotez.src.suppliers.graber.Graber.how_to_use
.. automethod:: hypotez.src.suppliers.graber.Graber.id_manufacturer
.. automethod:: hypotez.src.suppliers.graber.Graber.id_supplier
.. automethod:: hypotez.src.suppliers.graber.Graber.id_tax
.. automethod:: hypotez.src.suppliers.graber.Graber.id_type_redirected
.. automethod:: hypotez.src.suppliers.graber.Graber.images_urls
.. automethod:: hypotez.src.suppliers.graber.Graber.indexed
.. automethod:: hypotez.src.suppliers.graber.Graber.ingredients
.. automethod:: hypotez.src.suppliers.graber.Graber.meta_description
.. automethod:: hypotez.src.suppliers.graber.Graber.meta_keywords
.. automethod:: hypotez.src.suppliers.graber.Graber.meta_title
.. automethod:: hypotez.src.suppliers.graber.Graber.is_virtual
.. automethod:: hypotez.src.suppliers.graber.Graber.isbn
.. automethod:: hypotez.src.suppliers.graber.Graber.link_rewrite
.. automethod:: hypotez.src.suppliers.graber.Graber.location
.. automethod:: hypotez.src.suppliers.graber.Graber.low_stock_alert
.. automethod:: hypotez.src.suppliers.graber.Graber.low_stock_threshold
.. automethod:: hypotez.src.suppliers.graber.Graber.minimal_quantity
.. automethod:: hypotez.src.suppliers.graber.Graber.mpn
.. automethod:: hypotez.src.suppliers.graber.Graber.name
.. automethod:: hypotez.src.suppliers.graber.Graber.online_only
.. automethod:: hypotez.src.suppliers.graber.Graber.on_sale
.. automethod:: hypotez.src.suppliers.graber.Graber.out_of_stock
.. automethod:: hypotez.src.suppliers.graber.Graber.pack_stock_type
.. automethod:: hypotez.src.suppliers.graber.Graber.price
.. automethod:: hypotez.src.suppliers.graber.Graber.product_type
.. automethod:: hypotez.src.suppliers.graber.Graber.quantity
.. automethod:: hypotez.src.suppliers.graber.Graber.quantity_discount
.. automethod:: hypotez.src.suppliers.graber.Graber.redirect_type
.. automethod:: hypotez.src.suppliers.graber.Graber.reference
.. automethod:: hypotez.src.suppliers.graber.Graber.show_condition
.. automethod:: hypotez.src.suppliers.graber.Graber.show_price
.. automethod:: hypotez.src.suppliers.graber.Graber.state
.. automethod:: hypotez.src.suppliers.graber.Graber.text_fields
.. automethod:: hypotez.src.suppliers.graber.Graber.unit_price_ratio
.. automethod:: hypotez.src.suppliers.graber.Graber.unity
.. automethod:: hypotez.src.suppliers.graber.Graber.upc
.. automethod:: hypotez.src.suppliers.graber.Graber.uploadable_files
.. automethod:: hypotez.src.suppliers.graber.Graber.default_image_url
.. automethod:: hypotez.src.suppliers.graber.Graber.visibility
.. automethod:: hypotez.src.suppliers.graber.Graber.weight
.. automethod:: hypotez.src.suppliers.graber.Graber.wholesale_price
.. automethod:: hypotez.src.suppliers.graber.Graber.width
.. automethod:: hypotez.src.suppliers.graber.Graber.specification
.. automethod:: hypotez.src.suppliers.graber.Graber.link
.. automethod:: hypotez.src.suppliers.graber.Graber.byer_protection
.. automethod:: hypotez.src.suppliers.graber.Graber.customer_reviews
.. automethod:: hypotez.src.suppliers.graber.Graber.link_to_video
.. automethod:: hypotez.src.suppliers.graber.Graber.local_saved_image
.. automethod:: hypotez.src.suppliers.graber.Graber.local_saved_video