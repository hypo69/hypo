```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def product_locators():
    """Loads the product locator JSON data."""
    file_path = "hypotez/src/suppliers/grandadvance/locators/product.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def test_close_pop_up_locator(product_locators):
    """
    Test the 'close_pop_up' locator configuration.
    Verifies correct values for attributes related to locating and interacting with the close popup element.
    """
    close_pop_up = product_locators.get('close_pop_up')
    assert close_pop_up is not None, "close_pop_up locator not found"
    assert close_pop_up['attribute'] is None, "Attribute should be null"
    assert close_pop_up['by'] == "XPATH", "By should be XPATH"
    assert close_pop_up['selector'] == "//button[@class='close']", "Incorrect selector"
    assert close_pop_up['if_list'] == "first", "If_list should be first"
    assert close_pop_up['use_mouse'] is False, "Use_mouse should be False"
    assert close_pop_up['timeout'] == 0, "Timeout should be 0"
    assert close_pop_up['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert close_pop_up['event'] == "click()", "Incorrect event"
    assert close_pop_up['mandatory'] is True, "Mandatory should be True"
    assert close_pop_up['locator_description'] == "Закрыти попап окна", "Incorrect locator_description"


def test_id_locator(product_locators):
    """
    Test the 'id' locator configuration.
    Verify that it's configured as a basic locator with default settings.
    """
    id_locator = product_locators.get('id')
    assert id_locator is not None, "'id' locator not found"
    assert id_locator['attribute'] is None, "Attribute should be null"
    assert id_locator['by'] is None, "By should be null"
    assert id_locator['selector'] is None, "Selector should be null"
    assert id_locator['if_list'] == "first", "If_list should be 'first'"
    assert id_locator['use_mouse'] is False, "use_mouse should be false"
    assert id_locator['mandatory'] is True, "Mandatory should be true"
    assert id_locator['timeout'] == 0, "timeout should be 0"
    assert id_locator['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_locator['event'] is None, "event should be null"


def test_id_manufacturer_locator(product_locators):
    """
        Test the 'id_manufacturer' locator configuration.
        Verifies correct configuration for extracting manufacturer ID using XPATH.
    """
    id_manufacturer = product_locators.get('id_manufacturer')
    assert id_manufacturer is not None, "id_manufacturer locator not found"
    assert id_manufacturer['attribute'] == "innerText", "Attribute should be innerText"
    assert id_manufacturer['by'] == "XPATH", "By should be XPATH"
    assert id_manufacturer['selector'] == "//span[@class = 'ltr sku-copy']", "Incorrect selector"
    assert id_manufacturer['if_list'] == "first", "If_list should be first"
    assert id_manufacturer['use_mouse'] is False, "Use_mouse should be False"
    assert id_manufacturer['mandatory'] is True, "Mandatory should be True"
    assert id_manufacturer['timeout'] == 0, "Timeout should be 0"
    assert id_manufacturer['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_manufacturer['event'] is None, "Event should be None"
    assert id_manufacturer['locator_description'] == "SKU morlevi", "Incorrect locator_description"


def test_id_supplier_locator(product_locators):
    """
        Test the 'id_supplier' locator configuration.
         Verify that it uses VALUE and has an integer attribute.
    """
    id_supplier = product_locators.get('id_supplier')
    assert id_supplier is not None, "'id_supplier' locator not found"
    assert id_supplier['attribute'] == 2789, "Attribute should be 2789"
    assert id_supplier['by'] == "VALUE", "By should be VALUE"
    assert id_supplier['selector'] is None, "Selector should be null"
    assert id_supplier['if_list'] == "first", "if_list should be 'first'"
    assert id_supplier['use_mouse'] is False, "use_mouse should be false"
    assert id_supplier['mandatory'] is True, "Mandatory should be true"
    assert id_supplier['timeout'] == 0, "timeout should be 0"
    assert id_supplier['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_supplier['event'] is None, "event should be None"
    assert id_supplier['locator_description'] == "SKU morlevi", "Incorrect locator_description"

def test_id_product_locator(product_locators):
    """
    Test the 'id_product' locator configuration.
    Verifies the settings for identifying a product ID using XPATH.
    """
    id_product = product_locators.get('id_product')
    assert id_product is not None, "id_product locator not found"
    assert id_product['attribute'] == "innerText", "Attribute should be 'innerText'"
    assert id_product['by'] == "XPATH", "By should be 'XPATH'"
    assert id_product['selector'] == "//span[@class = 'part_number']", "Incorrect selector"
    assert id_product['if_list'] == "first", "If_list should be 'first'"
    assert id_product['use_mouse'] is False, "Use_mouse should be False"
    assert id_product['mandatory'] is True, "Mandatory should be True"
    assert id_product['timeout'] == 0, "Timeout should be 0"
    assert id_product['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_product['event'] is None, "Event should be None"
    assert id_product['locator_description'] == "SKU morlevi", "Incorrect locator_description"


def test_id_category_default_locator(product_locators):
        """
            Test the 'id_category_default' locator configuration.
            Verify that it has all the default configuration values.
        """
        id_category_default = product_locators.get('id_category_default')
        assert id_category_default is not None, "'id_category_default' locator not found"
        assert id_category_default['attribute'] is None, "Attribute should be null"
        assert id_category_default['by'] is None, "By should be null"
        assert id_category_default['selector'] is None, "Selector should be null"
        assert id_category_default['if_list'] == "first", "if_list should be 'first'"
        assert id_category_default['use_mouse'] is False, "use_mouse should be false"
        assert id_category_default['mandatory'] is True, "Mandatory should be true"
        assert id_category_default['timeout'] == 0, "timeout should be 0"
        assert id_category_default['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
        assert id_category_default['event'] is None, "event should be null"


def test_new_locator(product_locators):
    """
        Test the 'new' locator configuration.
        Verify that it has all the default configuration values.
    """
    new_locator = product_locators.get('new')
    assert new_locator is not None, "'new' locator not found"
    assert new_locator['attribute'] is None, "Attribute should be null"
    assert new_locator['by'] is None, "By should be null"
    assert new_locator['selector'] is None, "Selector should be null"
    assert new_locator['if_list'] == "first", "if_list should be 'first'"
    assert new_locator['use_mouse'] is False, "use_mouse should be false"
    assert new_locator['mandatory'] is True, "Mandatory should be true"
    assert new_locator['timeout'] == 0, "timeout should be 0"
    assert new_locator['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert new_locator['event'] is None, "event should be null"


def test_cache_default_attribute_locator(product_locators):
    """
        Test the 'cache_default_attribute' locator configuration.
        Verify that it has all the default configuration values.
    """
    cache_default_attribute = product_locators.get('cache_default_attribute')
    assert cache_default_attribute is not None, "'cache_default_attribute' locator not found"
    assert cache_default_attribute['attribute'] is None, "Attribute should be null"
    assert cache_default_attribute['by'] is None, "By should be null"
    assert cache_default_attribute['selector'] is None, "Selector should be null"
    assert cache_default_attribute['if_list'] == "first", "if_list should be 'first'"
    assert cache_default_attribute['use_mouse'] is False, "use_mouse should be false"
    assert cache_default_attribute['mandatory'] is True, "Mandatory should be true"
    assert cache_default_attribute['timeout'] == 0, "timeout should be 0"
    assert cache_default_attribute['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert cache_default_attribute['event'] is None, "event should be null"


def test_id_default_image_locator(product_locators):
    """
        Test the 'id_default_image' locator configuration.
        Verify that it has all the default configuration values.
    """
    id_default_image = product_locators.get('id_default_image')
    assert id_default_image is not None, "'id_default_image' locator not found"
    assert id_default_image['attribute'] is None, "Attribute should be null"
    assert id_default_image['by'] is None, "By should be null"
    assert id_default_image['selector'] is None, "Selector should be null"
    assert id_default_image['if_list'] == "first", "if_list should be 'first'"
    assert id_default_image['use_mouse'] is False, "use_mouse should be false"
    assert id_default_image['mandatory'] is True, "Mandatory should be true"
    assert id_default_image['timeout'] == 0, "timeout should be 0"
    assert id_default_image['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_default_image['event'] is None, "event should be null"


def test_default_image_url_locator(product_locators):
    """
     Test the 'default_image_url' locator configuration.
     Verifies that it is configured correctly to extract the default image URL using XPATH.
    """
    default_image_url = product_locators.get('default_image_url')
    assert default_image_url is not None, "default_image_url locator not found"
    assert default_image_url['attribute'] == "src", "Attribute should be 'src'"
    assert default_image_url['by'] == "XPATH", "By should be 'XPATH'"
    assert default_image_url['selector'] == "//div[@class = 'big_image']//img", "Incorrect selector"
    assert default_image_url['if_list'] == "first", "If_list should be 'first'"
    assert default_image_url['use_mouse'] is False, "Use_mouse should be False"
    assert default_image_url['timeout'] == 0, "Timeout should be 0"
    assert default_image_url['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert default_image_url['event'] is False, "Event should be False"
    assert default_image_url['mandatory'] is True, "Mandatory should be True"
    assert default_image_url['locator_description'] == "", "Incorrect locator_description"


def test_id_default_combination_locator(product_locators):
    """
        Test the 'id_default_combination' locator configuration.
        Verify that it has all the default configuration values.
    """
    id_default_combination = product_locators.get('id_default_combination')
    assert id_default_combination is not None, "'id_default_combination' locator not found"
    assert id_default_combination['attribute'] is None, "Attribute should be null"
    assert id_default_combination['by'] is None, "By should be null"
    assert id_default_combination['selector'] is None, "Selector should be null"
    assert id_default_combination['if_list'] == "first", "if_list should be 'first'"
    assert id_default_combination['use_mouse'] is False, "use_mouse should be false"
    assert id_default_combination['mandatory'] is True, "Mandatory should be true"
    assert id_default_combination['timeout'] == 0, "timeout should be 0"
    assert id_default_combination['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_default_combination['event'] is None, "event should be null"


def test_id_tax_locator(product_locators):
    """
        Test the 'id_tax' locator configuration.
        Verify that it has all the default configuration values.
    """
    id_tax = product_locators.get('id_tax')
    assert id_tax is not None, "'id_tax' locator not found"
    assert id_tax['attribute'] is None, "Attribute should be null"
    assert id_tax['by'] is None, "By should be null"
    assert id_tax['selector'] is None, "Selector should be null"
    assert id_tax['if_list'] == "first", "if_list should be 'first'"
    assert id_tax['use_mouse'] is False, "use_mouse should be false"
    assert id_tax['mandatory'] is True, "Mandatory should be true"
    assert id_tax['timeout'] == 0, "timeout should be 0"
    assert id_tax['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_tax['event'] is None, "event should be null"


def test_position_in_category_locator(product_locators):
    """
        Test the 'position_in_category' locator configuration.
        Verify that it has all the default configuration values.
    """
    position_in_category = product_locators.get('position_in_category')
    assert position_in_category is not None, "'position_in_category' locator not found"
    assert position_in_category['attribute'] is None, "Attribute should be null"
    assert position_in_category['by'] is None, "By should be null"
    assert position_in_category['selector'] is None, "Selector should be null"
    assert position_in_category['if_list'] == "first", "if_list should be 'first'"
    assert position_in_category['use_mouse'] is False, "use_mouse should be false"
    assert position_in_category['mandatory'] is True, "Mandatory should be true"
    assert position_in_category['timeout'] == 0, "timeout should be 0"
    assert position_in_category['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert position_in_category['event'] is None, "event should be null"

def test_type_locator(product_locators):
    """
    Test the 'type' locator configuration.
    Verify that it has all the default configuration values.
    """
    type_locator = product_locators.get('type')
    assert type_locator is not None, "'type' locator not found"
    assert type_locator['attribute'] is None, "Attribute should be null"
    assert type_locator['by'] is None, "By should be null"
    assert type_locator['selector'] is None, "Selector should be null"
    assert type_locator['if_list'] == "first", "if_list should be 'first'"
    assert type_locator['use_mouse'] is False, "use_mouse should be false"
    assert type_locator['mandatory'] is True, "Mandatory should be true"
    assert type_locator['timeout'] == 0, "timeout should be 0"
    assert type_locator['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert type_locator['event'] is None, "event should be null"

def test_id_shop_default_locator(product_locators):
    """
     Test the 'id_shop_default' locator configuration.
     Verify that it has all the default configuration values.
     """
    id_shop_default = product_locators.get('id_shop_default')
    assert id_shop_default is not None, "'id_shop_default' locator not found"
    assert id_shop_default['attribute'] is None, "Attribute should be null"
    assert id_shop_default['by'] is None, "By should be null"
    assert id_shop_default['selector'] is None, "Selector should be null"
    assert id_shop_default['if_list'] == "first", "if_list should be 'first'"
    assert id_shop_default['use_mouse'] is False, "use_mouse should be false"
    assert id_shop_default['mandatory'] is True, "Mandatory should be true"
    assert id_shop_default['timeout'] == 0, "timeout should be 0"
    assert id_shop_default['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert id_shop_default['event'] is None, "event should be null"


def test_reference_locator(product_locators):
    """
    Test the 'reference' locator configuration.
     Verify that it has all the default configuration values.
    """
    reference = product_locators.get('reference')
    assert reference is not None, "'reference' locator not found"
    assert reference['attribute'] is None, "Attribute should be null"
    assert reference['by'] is None, "By should be null"
    assert reference['selector'] is None, "Selector should be null"
    assert reference['if_list'] == "first", "if_list should be 'first'"
    assert reference['use_mouse'] is False, "use_mouse should be false"
    assert reference['mandatory'] is True, "Mandatory should be true"
    assert reference['timeout'] == 0, "timeout should be 0"
    assert reference['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert reference['event'] is None, "event should be null"


def test_supplier_reference_locator(product_locators):
    """
    Test the 'supplier_reference' locator configuration.
     Verify that it has all the default configuration values.
    """
    supplier_reference = product_locators.get('supplier_reference')
    assert supplier_reference is not None, "'supplier_reference' locator not found"
    assert supplier_reference['attribute'] is None, "Attribute should be null"
    assert supplier_reference['by'] is None, "By should be null"
    assert supplier_reference['selector'] is None, "Selector should be null"
    assert supplier_reference['if_list'] == "first", "if_list should be 'first'"
    assert supplier_reference['use_mouse'] is False, "use_mouse should be false"
    assert supplier_reference['mandatory'] is True, "Mandatory should be true"
    assert supplier_reference['timeout'] == 0, "timeout should be 0"
    assert supplier_reference['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert supplier_reference['event'] is None, "event should be null"


def test_location_locator(product_locators):
    """
    Test the 'location' locator configuration.
    Verify that it has all the default configuration values.
    """
    location = product_locators.get('location')
    assert location is not None, "'location' locator not found"
    assert location['attribute'] is None, "Attribute should be null"
    assert location['by'] is None, "By should be null"
    assert location['selector'] is None, "Selector should be null"
    assert location['if_list'] == "first", "if_list should be 'first'"
    assert location['use_mouse'] is False, "use_mouse should be false"
    assert location['mandatory'] is True, "Mandatory should be true"
    assert location['timeout'] == 0, "timeout should be 0"
    assert location['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert location['event'] is None, "event should be null"


def test_width_locator(product_locators):
    """
       Test the 'width' locator configuration.
       Verify that it has all the default configuration values.
    """
    width = product_locators.get('width')
    assert width is not None, "'width' locator not found"
    assert width['attribute'] is None, "Attribute should be null"
    assert width['by'] is None, "By should be null"
    assert width['selector'] is None, "Selector should be null"
    assert width['if_list'] == "first", "if_list should be 'first'"
    assert width['use_mouse'] is False, "use_mouse should be false"
    assert width['mandatory'] is True, "Mandatory should be true"
    assert width['timeout'] == 0, "timeout should be 0"
    assert width['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert width['event'] is None, "event should be null"

def test_height_locator(product_locators):
    """
        Test the 'height' locator configuration.
        Verify that it has all the default configuration values.
    """
    height = product_locators.get('height')
    assert height is not None, "'height' locator not found"
    assert height['attribute'] is None, "Attribute should be null"
    assert height['by'] is None, "By should be null"
    assert height['selector'] is None, "Selector should be null"
    assert height['if_list'] == "first", "if_list should be 'first'"
    assert height['use_mouse'] is False, "use_mouse should be false"
    assert height['mandatory'] is True, "Mandatory should be true"
    assert height['timeout'] == 0, "timeout should be 0"
    assert height['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert height['event'] is None, "event should be null"

def test_depth_locator(product_locators):
    """
    Test the 'depth' locator configuration.
    Verify that it has all the default configuration values.
    """
    depth = product_locators.get('depth')
    assert depth is not None, "'depth' locator not found"
    assert depth['attribute'] is None, "Attribute should be null"
    assert depth['by'] is None, "By should be null"
    assert depth['selector'] is None, "Selector should be null"
    assert depth['if_list'] == "first", "if_list should be 'first'"
    assert depth['use_mouse'] is False, "use_mouse should be false"
    assert depth['mandatory'] is True, "Mandatory should be true"
    assert depth['timeout'] == 0, "timeout should be 0"
    assert depth['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert depth['event'] is None, "event should be null"


def test_weight_locator(product_locators):
    """
    Test the 'weight' locator configuration.
    Verify that it has all the default configuration values.
    """
    weight = product_locators.get('weight')
    assert weight is not None, "'weight' locator not found"
    assert weight['attribute'] is None, "Attribute should be null"
    assert weight['by'] is None, "By should be null"
    assert weight['selector'] is None, "Selector should be null"
    assert weight['if_list'] == "first", "if_list should be 'first'"
    assert weight['use_mouse'] is False, "use_mouse should be false"
    assert weight['mandatory'] is True, "Mandatory should be true"
    assert weight['timeout'] == 0, "timeout should be 0"
    assert weight['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert weight['event'] is None, "event should be null"

def test_quantity_discount_locator(product_locators):
    """
        Test the 'quantity_discount' locator configuration.
        Verify that it has all the default configuration values.
    """
    quantity_discount = product_locators.get('quantity_discount')
    assert quantity_discount is not None, "'quantity_discount' locator not found"
    assert quantity_discount['attribute'] is None, "Attribute should be null"
    assert quantity_discount['by'] is None, "By should be null"
    assert quantity_discount['selector'] is None, "Selector should be null"
    assert quantity_discount['if_list'] == "first", "if_list should be 'first'"
    assert quantity_discount['use_mouse'] is False, "use_mouse should be false"
    assert quantity_discount['mandatory'] is True, "Mandatory should be true"
    assert quantity_discount['timeout'] == 0, "timeout should be 0"
    assert quantity_discount['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert quantity_discount['event'] is None, "event should be null"

def test_ean13_locator(product_locators):
    """
        Test the 'ean13' locator configuration.
         Verify that it has all the default configuration values.
    """
    ean13 = product_locators.get('ean13')
    assert ean13 is not None, "'ean13' locator not found"
    assert ean13['attribute'] is None, "Attribute should be null"
    assert ean13['by'] is None, "By should be null"
    assert ean13['selector'] is None, "Selector should be null"
    assert ean13['if_list'] == "first", "if_list should be 'first'"
    assert ean13['use_mouse'] is False, "use_mouse should be false"
    assert ean13['mandatory'] is True, "Mandatory should be true"
    assert ean13['timeout'] == 0, "timeout should be 0"
    assert ean13['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert ean13['event'] is None, "event should be null"


def test_isbn_locator(product_locators):
    """
      Test the 'isbn' locator configuration.
     Verify that it has all the default configuration values.
    """
    isbn = product_locators.get('isbn')
    assert isbn is not None, "'isbn' locator not found"
    assert isbn['attribute'] is None, "Attribute should be null"
    assert isbn['by'] is None, "By should be null"
    assert isbn['selector'] is None, "Selector should be null"
    assert isbn['if_list'] == "first", "if_list should be 'first'"
    assert isbn['use_mouse'] is False, "use_mouse should be false"
    assert isbn['mandatory'] is True, "Mandatory should be true"
    assert isbn['timeout'] == 0, "timeout should be 0"
    assert isbn['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert isbn['event'] is None, "event should be null"


def test_upc_locator(product_locators):
    """
     Test the 'upc' locator configuration.
     Verify that it has all the default configuration values.
    """
    upc = product_locators.get('upc')
    assert upc is not None, "'upc' locator not found"
    assert upc['attribute'] is None, "Attribute should be null"
    assert upc['by'] is None, "By should be null"
    assert upc['selector'] is None, "Selector should be null"
    assert upc['if_list'] == "first", "if_list should be 'first'"
    assert upc['use_mouse'] is False, "use_mouse should be false"
    assert upc['mandatory'] is True, "Mandatory should be true"
    assert upc['timeout'] == 0, "timeout should be 0"
    assert upc['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert upc['event'] is None, "event should be null"


def test_mpn_locator(product_locators):
    """
     Test the 'mpn' locator configuration.
     Verify that it has all the default configuration values.
    """
    mpn = product_locators.get('mpn')
    assert mpn is not None, "'mpn' locator not found"
    assert mpn['attribute'] is None, "Attribute should be null"
    assert mpn['by'] is None, "By should be null"
    assert mpn['selector'] is None, "Selector should be null"
    assert mpn['if_list'] == "first", "if_list should be 'first'"
    assert mpn['use_mouse'] is False, "use_mouse should be false"
    assert mpn['mandatory'] is True, "Mandatory should be true"
    assert mpn['timeout'] == 0, "timeout should be 0"
    assert mpn['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert mpn['event'] is None, "event should be null"


def test_cache_is_pack_locator(product_locators):
    """
    Test the 'cache_is_pack' locator configuration.
     Verify that it has all the default configuration values.
    """
    cache_is_pack = product_locators.get('cache_is_pack')
    assert cache_is_pack is not None, "'cache_is_pack' locator not found"
    assert cache_is_pack['attribute'] is None, "Attribute should be null"
    assert cache_is_pack['by'] is None, "By should be null"
    assert cache_is_pack['selector'] is None, "Selector should be null"
    assert cache_is_pack['if_list'] == "first", "if_list should be 'first'"
    assert cache_is_pack['use_mouse'] is False, "use_mouse should be false"
    assert cache_is_pack['mandatory'] is True, "Mandatory should be true"
    assert cache_is_pack['timeout'] == 0, "timeout should be 0"
    assert cache_is_pack['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert cache_is_pack['event'] is None, "event should be null"

def test_cache_has_attachments_locator(product_locators):
    """
        Test the 'cache_has_attachments' locator configuration.
        Verify that it has all the default configuration values.
    """
    cache_has_attachments = product_locators.get('cache_has_attachments')
    assert cache_has_attachments is not None, "'cache_has_attachments' locator not found"
    assert cache_has_attachments['attribute'] is None, "Attribute should be null"
    assert cache_has_attachments['by'] is None, "By should be null"
    assert cache_has_attachments['selector'] is None, "Selector should be null"
    assert cache_has_attachments['if_list'] == "first", "if_list should be 'first'"
    assert cache_has_attachments['use_mouse'] is False, "use_mouse should be false"
    assert cache_has_attachments['mandatory'] is True, "Mandatory should be true"
    assert cache_has_attachments['timeout'] == 0, "timeout should be 0"
    assert cache_has_attachments['timeout_for_event'] == "presence_of_element_located", "Incorrect timeout_for_event"
    assert cache_has_attachments['event'] is None, "event should be null"


def test_is_virtual_locator(product_locators):
    """
        Test the 'is_virtual' locator configuration.
         Verify that it has all the default configuration values.
    """
    is_virtual = product_locators.get('is_virtual')
    assert is_