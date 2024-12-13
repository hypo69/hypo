```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def product_locators():
    """Loads the product locator JSON data."""
    with open('hypotez/src/suppliers/hb/locators/product.json', 'r') as f:
        return json.load(f)

def test_close_banner_locator(product_locators):
    """Checks the close_banner locator's attributes."""
    close_banner = product_locators.get('close_banner')
    assert close_banner is not None
    assert close_banner['attribute'] is None
    assert close_banner['by'] == 'XPATH'
    assert close_banner['selector'] == "//button[@id = 'closeXButton']"
    assert close_banner['if_list'] == 'first'
    assert close_banner['use_mouse'] is False
    assert close_banner['mandatory'] is False
    assert close_banner['timeout'] == 0
    assert close_banner['timeout_for_event'] == "presence_of_element_located"
    assert close_banner['event'] == "click()"
    assert "Закрываю pop-up окно" in close_banner['locator_description']

def test_id_locator(product_locators):
    """Checks the id locator's attributes."""
    id_locator = product_locators.get('id')
    assert id_locator is not None
    assert id_locator['attribute'] is None
    assert id_locator['by'] is None
    assert id_locator['selector'] is None
    assert id_locator['if_list'] == 'first'
    assert id_locator['use_mouse'] is False
    assert id_locator['mandatory'] is False
    assert id_locator['timeout'] == 0
    assert id_locator['timeout_for_event'] == "presence_of_element_located"
    assert id_locator['event'] is None
    assert id_locator['locator_description'] == "id"

def test_id_manufacturer_locator(product_locators):
    """Checks the id_manufacturer locator's attributes."""
    id_manufacturer = product_locators.get('id_manufacturer')
    assert id_manufacturer is not None
    assert id_manufacturer['attribute'] == 11290
    assert id_manufacturer['by'] == 'VALUE'
    assert id_manufacturer['selector'] is None
    assert id_manufacturer['if_list'] == 'first'
    assert id_manufacturer['use_mouse'] is False
    assert id_manufacturer['mandatory'] is True
    assert id_manufacturer['timeout'] == 0
    assert id_manufacturer['timeout_for_event'] == "presence_of_element_located"
    assert id_manufacturer['event'] is None
    assert id_manufacturer['locator_description'] == "id_manufacturer"

def test_id_supplier_locator(product_locators):
    """Checks the id_supplier locator's attributes."""
    id_supplier = product_locators.get('id_supplier')
    assert id_supplier is not None
    assert id_supplier['attribute'] == 11267
    assert id_supplier['by'] == 'VALUE'
    assert id_supplier['selector'] is None
    assert id_supplier['if_list'] == 'first'
    assert id_supplier['use_mouse'] is False
    assert id_supplier['mandatory'] is True
    assert id_supplier['timeout'] == 0
    assert id_supplier['timeout_for_event'] == "presence_of_element_located"
    assert id_supplier['event'] is None
    assert id_supplier['locator_description'] == "HB id_supplier"

def test_id_product_locator(product_locators):
    """Checks the id_product locator's attributes."""
    id_product = product_locators.get('id_product')
    assert id_product is not None
    assert id_product['attribute'] == ""
    assert id_product['by'] == "XPATH"
    assert id_product['selector'] is None
    assert id_product['if_list'] == 'first'
    assert id_product['use_mouse'] is False
    assert id_product['mandatory'] is True
    assert id_product['timeout'] == 0
    assert id_product['timeout_for_event'] == "presence_of_element_located"
    assert id_product['event'] is None
    assert id_product['locator_description'] == "HB id_product"


def test_id_category_default_locator(product_locators):
    """Checks the id_category_default locator's attributes."""
    id_category_default = product_locators.get('id_category_default')
    assert id_category_default is not None
    assert id_category_default['attribute'] is None
    assert id_category_default['by'] is None
    assert id_category_default['selector'] is None
    assert id_category_default['if_list'] == 'first'
    assert id_category_default['use_mouse'] is False
    assert id_category_default['mandatory'] is False
    assert id_category_default['timeout'] == 0
    assert id_category_default['timeout_for_event'] == "presence_of_element_located"
    assert id_category_default['event'] is None
    assert id_category_default['locator_description'] == "id_category_default"


def test_condition_locator(product_locators):
    """Checks the condition locator's attributes."""
    condition = product_locators.get('condition')
    assert condition is not None
    assert condition['attribute'] == "new"
    assert condition['by'] == 'VALUE'
    assert condition['selector'] is None
    assert condition['if_list'] == 'first'
    assert condition['use_mouse'] is False
    assert condition['mandatory'] is True
    assert condition['timeout'] == 0
    assert condition['timeout_for_event'] == "presence_of_element_located"
    assert condition['event'] is None
    assert condition['locator_description'] == "condition"

def test_cache_default_attribute_locator(product_locators):
    """Checks the cache_default_attribute locator's attributes."""
    cache_default_attribute = product_locators.get('cache_default_attribute')
    assert cache_default_attribute is not None
    assert cache_default_attribute['attribute'] is None
    assert cache_default_attribute['by'] is None
    assert cache_default_attribute['selector'] is None
    assert cache_default_attribute['if_list'] == 'first'
    assert cache_default_attribute['use_mouse'] is False
    assert cache_default_attribute['mandatory'] is False
    assert cache_default_attribute['timeout'] == 0
    assert cache_default_attribute['timeout_for_event'] == "presence_of_element_located"
    assert cache_default_attribute['event'] is None
    assert cache_default_attribute['locator_description'] == "cache_default_attribute"

def test_default_image_url_locator(product_locators):
    """Checks the default_image_url locator's attributes."""
    default_image_url = product_locators.get('default_image_url')
    assert default_image_url is not None
    assert default_image_url['attribute'] == "src"
    assert default_image_url['by'] == 'XPATH'
    assert default_image_url['selector'] == "//img[contains(@class, 'zoomImg')]"
    assert default_image_url['if_list'] == 'first'
    assert default_image_url['use_mouse'] is False
    assert default_image_url['mandatory'] is False
    assert default_image_url['timeout'] == 0
    assert default_image_url['timeout_for_event'] == "presence_of_element_located"
    assert default_image_url['event'] is None
    assert default_image_url['locator_description'] == "default_image_url"

def test_id_default_combination_locator(product_locators):
    """Checks the id_default_combination locator's attributes."""
    id_default_combination = product_locators.get('id_default_combination')
    assert id_default_combination is not None
    assert id_default_combination['attribute'] is None
    assert id_default_combination['by'] is None
    assert id_default_combination['selector'] is None
    assert id_default_combination['if_list'] == 'first'
    assert id_default_combination['use_mouse'] is False
    assert id_default_combination['mandatory'] is False
    assert id_default_combination['timeout'] == 0
    assert id_default_combination['timeout_for_event'] == "presence_of_element_located"
    assert id_default_combination['event'] is None
    assert id_default_combination['locator_description'] == "id_default_combination"

def test_id_tax_locator(product_locators):
    """Checks the id_tax locator's attributes."""
    id_tax = product_locators.get('id_tax')
    assert id_tax is not None
    assert id_tax['attribute'] is None
    assert id_tax['by'] is None
    assert id_tax['selector'] is None
    assert id_tax['if_list'] == 'first'
    assert id_tax['use_mouse'] is False
    assert id_tax['mandatory'] is False
    assert id_tax['timeout'] == 0
    assert id_tax['timeout_for_event'] == "presence_of_element_located"
    assert id_tax['event'] is None
    assert id_tax['locator_description'] == "id_tax"

def test_position_in_category_locator(product_locators):
    """Checks the position_in_category locator's attributes."""
    position_in_category = product_locators.get('position_in_category')
    assert position_in_category is not None
    assert position_in_category['attribute'] is None
    assert position_in_category['by'] is None
    assert position_in_category['selector'] is None
    assert position_in_category['if_list'] == 'first'
    assert position_in_category['use_mouse'] is False
    assert position_in_category['mandatory'] is False
    assert position_in_category['timeout'] == 0
    assert position_in_category['timeout_for_event'] == "presence_of_element_located"
    assert position_in_category['event'] is None
    assert position_in_category['locator_description'] == "position_in_category"


def test_type_locator(product_locators):
    """Checks the type locator's attributes."""
    type_locator = product_locators.get('type')
    assert type_locator is not None
    assert type_locator['attribute'] is None
    assert type_locator['by'] is None
    assert type_locator['selector'] is None
    assert type_locator['if_list'] == 'first'
    assert type_locator['use_mouse'] is False
    assert type_locator['mandatory'] is False
    assert type_locator['timeout'] == 0
    assert type_locator['timeout_for_event'] == "presence_of_element_located"
    assert type_locator['event'] is None
    assert type_locator['locator_description'] == "type"

def test_id_shop_default_locator(product_locators):
    """Checks the id_shop_default locator's attributes."""
    id_shop_default = product_locators.get('id_shop_default')
    assert id_shop_default is not None
    assert id_shop_default['attribute'] is None
    assert id_shop_default['by'] is None
    assert id_shop_default['selector'] is None
    assert id_shop_default['if_list'] == 'first'
    assert id_shop_default['use_mouse'] is False
    assert id_shop_default['mandatory'] is False
    assert id_shop_default['timeout'] == 0
    assert id_shop_default['timeout_for_event'] == "presence_of_element_located"
    assert id_shop_default['event'] is None
    assert id_shop_default['locator_description'] == "id_shop_default"

def test_product_reference_and_volume_and_price_for_100_locator(product_locators):
    """Checks the product_reference_and_volume_and_price_for_100 locator's attributes."""
    locator = product_locators.get('product_reference_and_volume_and_price_for_100')
    assert locator is not None
    assert locator['attribute'] is None
    assert locator['by'] == 'XPATH'
    assert locator['selector'] == "//div[@data-widget_type='shortcode.default']"
    assert locator['if_list'] == 'first'
    assert locator['use_mouse'] is False
    assert locator['mandatory'] is True
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == "presence_of_element_located"
    assert locator['event'] is None
    assert "На сайте кривой HTML" in locator['locator_description']

def test_reference_locator(product_locators):
    """Checks the reference locator's attributes."""
    reference = product_locators.get('reference')
    assert reference is not None
    assert reference['attribute'] is None
    assert reference['by'] is None
    assert reference['selector'] is None
    assert reference['if_list'] == 'first'
    assert reference['use_mouse'] is False
    assert reference['mandatory'] is False
    assert reference['timeout'] == 0
    assert reference['timeout_for_event'] == "presence_of_element_located"
    assert reference['event'] is None
    assert "Собирается в коде" in reference['locator_description']

def test_supplier_reference_locator(product_locators):
    """Checks the supplier_reference locator's attributes."""
    supplier_reference = product_locators.get('supplier_reference')
    assert supplier_reference is not None
    assert supplier_reference['attribute'] is None
    assert supplier_reference['by'] is None
    assert supplier_reference['selector'] is None
    assert supplier_reference['logic for action[AND|OR|XOR|VALUE|null]'] is None
    assert supplier_reference['if_list'] == 'first'
    assert supplier_reference['use_mouse'] is False
    assert supplier_reference['mandatory'] is False
    assert supplier_reference['timeout'] == 0
    assert supplier_reference['timeout_for_event'] == "presence_of_element_located"
    assert supplier_reference['event'] is None
    assert "Получаю через локатор product_reference_and_volume_and_price_for_100" in supplier_reference['locator_description']

def test_additional_images_urls_locator(product_locators):
    """Checks the additional_images_urls locator's attributes."""
    additional_images_urls = product_locators.get('additional_images_urls')
    assert additional_images_urls is not None
    assert additional_images_urls['attribute'] == "src"
    assert additional_images_urls['by'] == "XPATH"
    assert additional_images_urls['selector'] == "//ol[contains(@class, 'flex-control-thumbs')]//img"
    assert additional_images_urls['if_list'] == 'first'
    assert additional_images_urls['use_mouse'] is False
    assert additional_images_urls['mandatory'] is False
    assert additional_images_urls['timeout'] == 0
    assert additional_images_urls['timeout_for_event'] == "presence_of_element_located"
    assert additional_images_urls['event'] is None

def test_additional_images_alts_locator(product_locators):
    """Checks the additional_images_alts locator's attributes."""
    additional_images_alts = product_locators.get('additional_images_alts')
    assert additional_images_alts is not None
    assert additional_images_alts['attribute'] is None
    assert additional_images_alts['by'] is None
    assert additional_images_alts['selector'] is None
    assert additional_images_alts['if_list'] == 'first'
    assert additional_images_alts['use_mouse'] is False
    assert additional_images_alts['mandatory'] is False
    assert additional_images_alts['timeout'] == 0
    assert additional_images_alts['timeout_for_event'] == "presence_of_element_located"
    assert additional_images_alts['event'] is None

def test_location_locator(product_locators):
    """Checks the location locator's attributes."""
    location = product_locators.get('location')
    assert location is not None
    assert location['attribute'] is None
    assert location['by'] is None
    assert location['selector'] is None
    assert location['if_list'] == 'first'
    assert location['use_mouse'] is False
    assert location['mandatory'] is False
    assert location['timeout'] == 0
    assert location['timeout_for_event'] == "presence_of_element_located"
    assert location['event'] is None
    assert location['locator_description'] == "location"

def test_width_locator(product_locators):
    """Checks the width locator's attributes."""
    width = product_locators.get('width')
    assert width is not None
    assert width['attribute'] is None
    assert width['by'] is None
    assert width['selector'] is None
    assert width['if_list'] == 'first'
    assert width['use_mouse'] is False
    assert width['mandatory'] is False
    assert width['timeout'] == 0
    assert width['timeout_for_event'] == "presence_of_element_located"
    assert width['event'] is None
    assert width['locator_description'] == "width"

def test_height_locator(product_locators):
    """Checks the height locator's attributes."""
    height = product_locators.get('height')
    assert height is not None
    assert height['attribute'] is None
    assert height['by'] is None
    assert height['selector'] is None
    assert height['if_list'] == 'first'
    assert height['use_mouse'] is False
    assert height['mandatory'] is False
    assert height['timeout'] == 0
    assert height['timeout_for_event'] == "presence_of_element_located"
    assert height['event'] is None
    assert height['locator_description'] == "height"

def test_depth_locator(product_locators):
    """Checks the depth locator's attributes."""
    depth = product_locators.get('depth')
    assert depth is not None
    assert depth['attribute'] is None
    assert depth['by'] is None
    assert depth['selector'] is None
    assert depth['if_list'] == 'first'
    assert depth['use_mouse'] is False
    assert depth['mandatory'] is False
    assert depth['timeout'] == 0
    assert depth['timeout_for_event'] == "presence_of_element_located"
    assert depth['event'] is None
    assert depth['locator_description'] == "depth"

def test_weight_locator(product_locators):
    """Checks the weight locator's attributes."""
    weight = product_locators.get('weight')
    assert weight is not None
    assert weight['attribute'] is None
    assert weight['by'] is None
    assert weight['selector'] is None
    assert weight['logic for action[AND|OR|XOR|VALUE|null]'] is None
    assert weight['if_list'] == 'first'
    assert weight['use_mouse'] is False
    assert weight['mandatory'] is False
    assert weight['timeout'] == 0
    assert weight['timeout_for_event'] == "presence_of_element_located"
    assert weight['event'] is None
    assert weight['locator_description'] == "weight"

def test_quantity_discount_locator(product_locators):
    """Checks the quantity_discount locator's attributes."""
    quantity_discount = product_locators.get('quantity_discount')
    assert quantity_discount is not None
    assert quantity_discount['attribute'] is None
    assert quantity_discount['by'] is None
    assert quantity_discount['selector'] is None
    assert quantity_discount['if_list'] == 'first'
    assert quantity_discount['use_mouse'] is False
    assert quantity_discount['mandatory'] is False
    assert quantity_discount['timeout'] == 0
    assert quantity_discount['timeout_for_event'] == "presence_of_element_located"
    assert quantity_discount['event'] is None
    assert quantity_discount['locator_description'] == "quantity_discount"

def test_ean13_locator(product_locators):
    """Checks the ean13 locator's attributes."""
    ean13 = product_locators.get('ean13')
    assert ean13 is not None
    assert ean13['attribute'] is None
    assert ean13['by'] is None
    assert ean13['selector'] is None
    assert ean13['if_list'] == 'first'
    assert ean13['use_mouse'] is False
    assert ean13['mandatory'] is False
    assert ean13['timeout'] == 0
    assert ean13['timeout_for_event'] == "presence_of_element_located"
    assert ean13['event'] is None
    assert ean13['locator_description'] == "ean13"

def test_isbn_locator(product_locators):
    """Checks the isbn locator's attributes."""
    isbn = product_locators.get('isbn')
    assert isbn is not None
    assert isbn['attribute'] is None
    assert isbn['by'] is None
    assert isbn['selector'] is None
    assert isbn['if_list'] == 'first'
    assert isbn['use_mouse'] is False
    assert isbn['mandatory'] is False
    assert isbn['timeout'] == 0
    assert isbn['timeout_for_event'] == "presence_of_element_located"
    assert isbn['event'] is None
    assert isbn['locator_description'] == "isbn"

def test_upc_locator(product_locators):
    """Checks the upc locator's attributes."""
    upc = product_locators.get('upc')
    assert upc is not None
    assert upc['attribute'] is None
    assert upc['by'] is None
    assert upc['selector'] is None
    assert upc['if_list'] == 'first'
    assert upc['use_mouse'] is False
    assert upc['mandatory'] is False
    assert upc['timeout'] == 0
    assert upc['timeout_for_event'] == "presence_of_element_located"
    assert upc['event'] is None
    assert upc['locator_description'] == "upc"

def test_mpn_locator(product_locators):
    """Checks the mpn locator's attributes."""
    mpn = product_locators.get('mpn')
    assert mpn is not None
    assert mpn['attribute'] is None
    assert mpn['by'] is None
    assert mpn['selector'] is None
    assert mpn['if_list'] == 'first'
    assert mpn['use_mouse'] is False
    assert mpn['mandatory'] is False
    assert mpn['timeout'] == 0
    assert mpn['timeout_for_event'] == "presence_of_element_located"
    assert mpn['event'] is None
    assert mpn['locator_description'] == "mpn"

def test_cache_is_pack_locator(product_locators):
    """Checks the cache_is_pack locator's attributes."""
    cache_is_pack = product_locators.get('cache_is_pack')
    assert cache_is_pack is not None
    assert cache_is_pack['attribute'] is None
    assert cache_is_pack['by'] is None
    assert cache_is_pack['selector'] is None
    assert cache_is_pack['if_list'] == 'first'
    assert cache_is_pack['use_mouse'] is False
    assert cache_is_pack['mandatory'] is False
    assert cache_is_pack['timeout'] == 0
    assert cache_is_pack['timeout_for_event'] == "presence_of_element_located"
    assert cache_is_pack['event'] is None
    assert cache_is_pack['locator_description'] == "cache_is_pack"

def test_cache_has_attachments_locator(product_locators):
    """Checks the cache_has_attachments locator's attributes."""
    cache_has_attachments = product_locators.get('cache_has_attachments')
    assert cache_has_attachments is not None
    assert cache_has_attachments['attribute'] is None
    assert cache_has_attachments['by'] is None
    assert cache_has_attachments['selector'] is None
    assert cache_has_attachments['if_list'] == 'first'
    assert cache_has_attachments['use_mouse'] is False
    assert cache_has_attachments['mandatory'] is False
    assert cache_has_attachments['timeout'] == 0
    assert cache_has_attachments['timeout_for_event'] == "presence_of_element_located"
    assert cache_has_attachments['event'] is None
    assert cache_has_attachments['locator_description'] == "cache_has_attachments"


def test_is_virtual_locator(product_locators):
    """Checks the is_virtual locator's attributes."""
    is_virtual = product_locators.get('is_virtual')
    assert is_virtual is not None
    assert is_virtual['attribute'] == '0'
    assert is_virtual['by'] == "VALUE"
    assert is_virtual['selector'] is None
    assert is_virtual['if_list'] == 'first'
    assert is_virtual['use_mouse'] is False
    assert is_virtual['mandatory'] is False
    assert is_virtual['timeout'] == 0
    assert is_virtual['timeout_for_event'] == "presence_of_element_located"
    assert is_virtual['event'] is None
    assert is_virtual['locator_description'] == "is_virtual"


def test_out_of_stock_locator(product_locators):
    """Checks the out_of_stock locator's attributes."""
    out_of_stock = product_locators.get('out_of_stock')
    assert out_of_stock is not None
    assert out_of_stock['attribute'] is None
    assert out_of_stock['by'] == 'XPATH'
    assert out_of_stock['selector'] == "//p[contains(@class, 'out-of-stock')]"
    assert out_of_stock['if_list'] == 'first'
    assert out_of_stock['use_mouse'] is False
    assert out_of_stock['mandatory'] is True
    assert out_of_stock['timeout'] == 0
    assert out_of_stock['timeout_for_event'] == "presence_of_element_located"
    assert out_of_stock['event'] is None
    assert out_of_stock['locator_description'] == "out_of_stock"

def test_state_locator(product_locators):
    """Checks the state locator's attributes."""
    state = product_locators.get('state')
    assert state is not None
    assert state['attribute'] is None
    assert state['by'] is None
    assert state['selector'] is None
    assert state['if_list'] == 'first'
    assert state['use_mouse'] is False
    assert state['mandatory'] is False
    assert state['timeout'] == 0
    assert state['timeout_for_event'] == "presence_of_element_located"
    assert state['event'] is None
    assert state['locator_description'] == "state"

def test_additional_delivery_times_locator(product_locators):
    """Checks the additional_delivery_times locator's attributes."""
    additional_delivery_times = product_locators.get('additional_delivery_times')
    assert additional_delivery_times is not None
    assert additional_delivery_times['attribute'] is None
    assert additional_delivery_times['by'] is None
    assert additional_delivery_times['selector'] is None
    assert additional_delivery_times['if_list'] == 'first'
    assert additional_delivery_times['use_mouse'] is False
    assert additional_delivery_times['mandatory'] is False
    assert additional_delivery_times['timeout'] == 0
    assert additional_delivery_times['timeout_for_event'] == "presence_of_element_located"
    assert additional_delivery_times['event'] is None
    assert additional_delivery_times['locator_description'] == "additional_delivery_times"

def test_delivery_in_stock_locator(product_locators):
    """Checks the delivery_in_stock locator's attributes."""
    delivery_in_stock = product_locators.get('delivery_in_stock')
    assert delivery_in_stock is not None
    assert delivery_in_stock['attribute'] == "Israel Post"
    assert delivery_in_stock['by'] == 'VALUE'
    assert delivery_in_stock['selector'] is None
    assert delivery_in_stock['if_list'] == 'first'
    assert delivery_in_stock['use_mouse'] is False
    assert delivery_in_stock['mandatory'] is False
    assert delivery_in_stock['timeout'] == 0
    assert delivery_in_stock['timeout_for_event'] == "presence_of_element_located"
    assert delivery_in_stock['event'] is None
    assert delivery_in_stock['locator_description'] == "delivery_in_stock (Israel Post)"

def test_delivery_out_stock_locator(product_locators):
    """Checks the delivery_out_stock locator's attributes."""
    delivery_out_stock = product_locators.get('delivery_out_stock')
    assert delivery_out_stock is not None
    assert delivery_out_stock['attribute'] is None
    assert delivery_out_stock['by'] is None
    assert delivery_out_stock['selector'] is None
    assert delivery_out_stock['if_list'] == 'first'
    assert delivery_out_stock['use_mouse'] is False
    assert delivery_out_stock['mandatory'] is False
    assert delivery_out_stock['timeout'] == 0
    assert delivery_out_stock['timeout_for_event'] == "presence_of_element_located"
    assert delivery_out_stock['event'] is None
    assert delivery_out_stock['locator_description'] == "delivery_out_stock"

def test_product_type_locator(product_locators):
    """Checks the product_type locator's attributes."""
    product_type = product_locators.get('product_type')
    assert product_type is not None
    assert product_type['attribute'] is None
    assert product_type['by'] is None
    assert product_type['selector'] is None
    assert product_type['if_list'] == 'first'
    assert product_type['use_mouse'] is False
    assert product_type['mandatory'] is False
    assert product_type['timeout'] == 0
    assert product_type['timeout_for_event'] == "presence_of_element_located"
    assert product_type['event'] is None
    assert product_type['locator_description'] == "product_type"


def test_on_sale_locator(product_locators):
    """Checks the on_sale locator's attributes."""
    on_sale = product_locators.get('on_sale')
    assert on_sale is not None
    assert on_sale['attribute'] == 0
    assert on_sale['by'] == 'VALUE'
    assert on_sale['selector'] is None
    assert on_sale['if_list'] == 'first'
    assert on_sale['use_mouse'] is False
    assert on_sale['mandatory'] is False
    assert on_sale['timeout'] == 0
    assert on_sale['timeout_for_event'] == "presence_of_element_located"
    assert on_sale['event'] is None
    assert on_sale['locator_description'] == "on_sale"


def test_online_only_locator(product_locators):
    """Checks the online_only locator's attributes."""
    online_only = product_locators.get('online_only')
    assert online_only is not None
    assert online_only['attribute'] == 1
    assert online_only['by'] == 'VALUE'
    assert online_only['selector'] is None
    assert online_only['if_list'] == 'first'
    assert online_only['use_mouse'] is False
    assert online_only['mandatory'] is False
    assert online_only['timeout'] == 0
    assert online_only['timeout_for_event'] == "presence_of_element_located"
    assert online_only['event'] is None
    assert online_only['locator_description'] == "online_only"

def test_ecotax_locator(product_locators):
    """Checks the ecotax locator's attributes."""
    ecotax = product_locators.get('ecotax')
    assert ecotax is not None
    assert ecotax['attribute'] is None
    assert ecotax['by'] is None
    assert ecotax['selector'] is None
    assert ecotax['if_list'] == 'first'
    assert ecotax['use_mouse'] is False
    assert ecotax['mandatory'] is False
    assert ecotax['timeout'] == 0
    assert ecotax['timeout_for_event'] == "presence_of_element_located"
    assert ecotax['event'] is None
    assert ecotax['locator_description'] == "ecotax"


def test_minimal_quantity_locator(product_locators):
    """Checks the minimal_quantity locator's attributes."""
    minimal_quantity = product_locators.get('minimal_quantity')
    assert minimal_quantity is not