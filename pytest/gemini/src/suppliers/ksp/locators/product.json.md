```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def product_locators():
    """Loads the product locator data from the JSON file."""
    file_path = "hypotez/src/suppliers/ksp/locators/product.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test for close_pop_up locator
def test_close_pop_up_locator(product_locators):
    """
    Test the close_pop_up locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('close_pop_up')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] == 'XPATH'
    assert locator['selector'] == "//button[@class='close']"
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] == "click()"
    assert locator['mandatory'] is True
    assert locator['locator_description'] == "Закрыти попап окна"


# Test for id locator
def test_id_locator(product_locators):
    """
    Test the id locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for id_manufacturer locator
def test_id_manufacturer_locator(product_locators):
    """
    Test the id_manufacturer locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_manufacturer')
    assert locator is not None
    assert locator['attribute'] == 'innerText'
    assert locator['by'] == 'XPATH'
    assert locator['selector'] == "//span[@class = 'ltr sku-copy']"
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None
    assert locator['locator_description'] == "SKU manufacturer"

# Test for id_supplier locator
def test_id_supplier_locator(product_locators):
    """
    Test the id_supplier locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_supplier')
    assert locator is not None
    assert locator['attribute'] == 2787
    assert locator['by'] == 'VALUE'
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 2
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None
    assert locator['locator_description'] == "SKU ksp"

# Test for id_product locator
def test_id_product_locator(product_locators):
    """
    Test the id_product locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_product')
    assert locator is not None
    assert locator['attribute'] == 'innerText'
    assert locator['by'] == 'XPATH'
    assert locator['selector'] == "(//div[contains(@data-id, 'product-')])[1]//span"
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 2
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None
    assert locator['locator_description'] == "SKU ksp"

# Test for id_category_default locator
def test_id_category_default_locator(product_locators):
    """
    Test the id_category_default locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_category_default')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for new locator
def test_new_locator(product_locators):
    """
    Test the new locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('new')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for cache_default_attribute locator
def test_cache_default_attribute_locator(product_locators):
     """
     Test the cache_default_attribute locator.
     It checks if the locator properties are correctly defined.
     """
     locator = product_locators.get('cache_default_attribute')
     assert locator is not None
     assert locator['attribute'] is None
     assert locator['by'] is None
     assert locator['selector'] is None
     assert locator['if_list'] == 'first'
     assert locator['use_mouse'] is False
     assert locator['mandatory'] is True
     assert locator['timeout'] == 0
     assert locator['timeout_for_event'] == "presence_of_element_located"
     assert locator['event'] is None

# Test for id_default_image locator
def test_id_default_image_locator(product_locators):
    """
    Test the id_default_image locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_default_image')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for default_image_url locator
def test_default_image_url_locator(product_locators):
     """
     Test the default_image_url locator.
     It checks if the locator properties are correctly defined.
     """
     locator = product_locators.get('default_image_url')
     assert locator is not None
     assert locator['attribute'] is None
     assert locator['by'] == 'XPATH'
     assert locator['selector'] == "(//li[@class = 'slide selected previous'])[1]//img"
     assert locator['if_list'] == 'first'
     assert locator['use_mouse'] is False
     assert locator['timeout'] == 0
     assert locator['timeout_for_event'] == "presence_of_element_located"
     assert locator['event'] == "screenshot()"
     assert locator['mandatory'] is True
     assert locator['locator_description'] == ""

# Test for id_default_combination locator
def test_id_default_combination_locator(product_locators):
    """
    Test the id_default_combination locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_default_combination')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for id_tax locator
def test_id_tax_locator(product_locators):
    """
    Test the id_tax locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_tax')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for position_in_category locator
def test_position_in_category_locator(product_locators):
    """
    Test the position_in_category locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('position_in_category')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for type locator
def test_type_locator(product_locators):
    """
    Test the type locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('type')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for id_shop_default locator
def test_id_shop_default_locator(product_locators):
    """
    Test the id_shop_default locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('id_shop_default')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for reference locator
def test_reference_locator(product_locators):
    """
    Test the reference locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('reference')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for supplier_reference locator
def test_supplier_reference_locator(product_locators):
    """
    Test the supplier_reference locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('supplier_reference')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for location locator
def test_location_locator(product_locators):
    """
    Test the location locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('location')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for width locator
def test_width_locator(product_locators):
    """
    Test the width locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('width')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for height locator
def test_height_locator(product_locators):
    """
    Test the height locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('height')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for depth locator
def test_depth_locator(product_locators):
    """
    Test the depth locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('depth')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for weight locator
def test_weight_locator(product_locators):
    """
    Test the weight locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('weight')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for quantity_discount locator
def test_quantity_discount_locator(product_locators):
    """
    Test the quantity_discount locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('quantity_discount')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for ean13 locator
def test_ean13_locator(product_locators):
    """
    Test the ean13 locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('ean13')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for isbn locator
def test_isbn_locator(product_locators):
    """
    Test the isbn locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('isbn')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for upc locator
def test_upc_locator(product_locators):
    """
    Test the upc locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('upc')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for mpn locator
def test_mpn_locator(product_locators):
    """
    Test the mpn locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('mpn')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for cache_is_pack locator
def test_cache_is_pack_locator(product_locators):
    """
    Test the cache_is_pack locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('cache_is_pack')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for cache_has_attachments locator
def test_cache_has_attachments_locator(product_locators):
    """
    Test the cache_has_attachments locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('cache_has_attachments')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for is_virtual locator
def test_is_virtual_locator(product_locators):
    """
    Test the is_virtual locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('is_virtual')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for state locator
def test_state_locator(product_locators):
    """
    Test the state locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('state')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for additional_delivery_times locator
def test_additional_delivery_times_locator(product_locators):
    """
    Test the additional_delivery_times locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('additional_delivery_times')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for delivery_in_stock locator
def test_delivery_in_stock_locator(product_locators):
    """
    Test the delivery_in_stock locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('delivery_in_stock')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for delivery_out_stock locator
def test_delivery_out_stock_locator(product_locators):
     """
     Test the delivery_out_stock locator.
     It checks if the locator properties are correctly defined.
     """
     locator = product_locators.get('delivery_out_stock')
     assert locator is not None
     assert locator['attribute'] is None
     assert locator['by'] is None
     assert locator['selector'] is None
     assert locator['if_list'] == 'first'
     assert locator['use_mouse'] is False
     assert locator['mandatory'] is True
     assert locator['timeout'] == 0
     assert locator['timeout_for_event'] == "presence_of_element_located"
     assert locator['event'] is None

# Test for product_type locator
def test_product_type_locator(product_locators):
    """
    Test the product_type locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('product_type')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for on_sale locator
def test_on_sale_locator(product_locators):
    """
    Test the on_sale locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('on_sale')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for online_only locator
def test_online_only_locator(product_locators):
    """
    Test the online_only locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('online_only')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for ecotax locator
def test_ecotax_locator(product_locators):
    """
    Test the ecotax locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('ecotax')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for minimal_quantity locator
def test_minimal_quantity_locator(product_locators):
    """
    Test the minimal_quantity locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('minimal_quantity')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for low_stock_threshold locator
def test_low_stock_threshold_locator(product_locators):
     """
     Test the low_stock_threshold locator.
     It checks if the locator properties are correctly defined.
     """
     locator = product_locators.get('low_stock_threshold')
     assert locator is not None
     assert locator['attribute'] is None
     assert locator['by'] is None
     assert locator['selector'] is None
     assert locator['if_list'] == 'first'
     assert locator['use_mouse'] is False
     assert locator['mandatory'] is True
     assert locator['timeout'] == 0
     assert locator['timeout_for_event'] == "presence_of_element_located"
     assert locator['event'] is None

# Test for low_stock_alert locator
def test_low_stock_alert_locator(product_locators):
    """
    Test the low_stock_alert locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('low_stock_alert')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for price locator
def test_price_locator(product_locators):
    """
    Test the price locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('price')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None


# Test for wholesale_price locator
def test_wholesale_price_locator(product_locators):
    """
    Test the wholesale_price locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('wholesale_price')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for unity locator
def test_unity_locator(product_locators):
    """
    Test the unity locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('unity')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for unit_price_ratio locator
def test_unit_price_ratio_locator(product_locators):
    """
    Test the unit_price_ratio locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('unit_price_ratio')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for additional_shipping_cost locator
def test_additional_shipping_cost_locator(product_locators):
    """
    Test the additional_shipping_cost locator.
    It checks if the locator properties are correctly defined.
    """
    locator = product_locators.get('additional_shipping_cost')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] is None
    assert locator['selector'] is None
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None

# Test for customizable locator
def test_customizable_locator(