```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def product_locators():
    """Loads the product locators from the JSON file."""
    with open("hypotez/src/suppliers/ksp/locators/product_mobile_site.json", "r") as f:
        return json.load(f)

# Test case for the 'close_pop_up' locator
def test_close_pop_up_locator(product_locators):
    """
    Checks the correctness of the 'close_pop_up' locator configuration.
    Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    close_pop_up = product_locators.get("close_pop_up")
    assert close_pop_up is not None
    assert close_pop_up["by"] == "XPATH"
    assert close_pop_up["selector"] == "//button[@class='close']"
    assert close_pop_up["if_list"] == "first"
    assert close_pop_up["use_mouse"] is False
    assert close_pop_up["timeout"] == 0
    assert close_pop_up["timeout_for_event"] == "presence_of_element_located"
    assert close_pop_up["event"] == "click()"
    assert close_pop_up["mandatory"] is True
    assert close_pop_up["locator_description"] == "Закрыти попап окна"

# Test case for the 'id' locator
def test_id_locator(product_locators):
    """
    Checks the correctness of the 'id' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_locator = product_locators.get("id")
    assert id_locator is not None
    assert id_locator["by"] is None
    assert id_locator["selector"] is None
    assert id_locator["if_list"] == "first"
    assert id_locator["use_mouse"] is False
    assert id_locator["mandatory"] is True
    assert id_locator["timeout"] == 0
    assert id_locator["timeout_for_event"] == "presence_of_element_located"
    assert id_locator["event"] is None


# Test case for the 'id_manufacturer' locator
def test_id_manufacturer_locator(product_locators):
    """
    Checks the correctness of the 'id_manufacturer' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_manufacturer = product_locators.get("id_manufacturer")
    assert id_manufacturer is not None
    assert id_manufacturer["by"] == "XPATH"
    assert id_manufacturer["selector"] is None
    assert id_manufacturer["if_list"] == "first"
    assert id_manufacturer["use_mouse"] is False
    assert id_manufacturer["mandatory"] is True
    assert id_manufacturer["timeout"] == 0
    assert id_manufacturer["timeout_for_event"] == "presence_of_element_located"
    assert id_manufacturer["event"] is None
    assert id_manufacturer["locator_description"] == "SKU manufacturer"

# Test case for the 'id_supplier' locator
def test_id_supplier_locator(product_locators):
    """
     Checks the correctness of the 'id_supplier' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_supplier = product_locators.get("id_supplier")
    assert id_supplier is not None
    assert id_supplier["attribute"] == "2787"
    assert id_supplier["by"] == "VALUE"
    assert id_supplier["selector"] is None
    assert id_supplier["if_list"] == "first"
    assert id_supplier["use_mouse"] is False
    assert id_supplier["mandatory"] is True
    assert id_supplier["timeout"] == 2
    assert id_supplier["timeout_for_event"] == "presence_of_element_located"
    assert id_supplier["event"] is None
    assert id_supplier["locator_description"] == "SKU ksp"


# Test case for the 'id_product' locator
def test_id_product_locator(product_locators):
    """
    Checks the correctness of the 'id_product' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event', 'attribute' and 'mandatory' properties.
    """
    id_product = product_locators.get("id_product")
    assert id_product is not None
    assert id_product["attribute"] == "innerText"
    assert id_product["by"] == "XPATH"
    assert id_product["selector"] == "//span[contains(text(),\'מקט\')]"
    assert id_product["if_list"] == "first"
    assert id_product["use_mouse"] is False
    assert id_product["mandatory"] is True
    assert id_product["timeout"] == 2
    assert id_product["timeout_for_event"] == "presence_of_element_located"
    assert id_product["event"] is None
    assert id_product["locator_description"] == "mobile version SKU ksp"


# Test case for the 'id_category_default' locator
def test_id_category_default_locator(product_locators):
    """
    Checks the correctness of the 'id_category_default' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_category_default = product_locators.get("id_category_default")
    assert id_category_default is not None
    assert id_category_default["attribute"] is None
    assert id_category_default["by"] is None
    assert id_category_default["selector"] is None
    assert id_category_default["if_list"] == "first"
    assert id_category_default["use_mouse"] is False
    assert id_category_default["mandatory"] is True
    assert id_category_default["timeout"] == 0
    assert id_category_default["timeout_for_event"] == "presence_of_element_located"
    assert id_category_default["event"] is None


# Test case for the 'new' locator
def test_new_locator(product_locators):
    """
    Checks the correctness of the 'new' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    new_locator = product_locators.get("new")
    assert new_locator is not None
    assert new_locator["attribute"] is None
    assert new_locator["by"] is None
    assert new_locator["selector"] is None
    assert new_locator["if_list"] == "first"
    assert new_locator["use_mouse"] is False
    assert new_locator["mandatory"] is True
    assert new_locator["timeout"] == 0
    assert new_locator["timeout_for_event"] == "presence_of_element_located"
    assert new_locator["event"] is None

# Test case for the 'cache_default_attribute' locator
def test_cache_default_attribute_locator(product_locators):
    """
    Checks the correctness of the 'cache_default_attribute' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    cache_default_attribute = product_locators.get("cache_default_attribute")
    assert cache_default_attribute is not None
    assert cache_default_attribute["attribute"] is None
    assert cache_default_attribute["by"] is None
    assert cache_default_attribute["selector"] is None
    assert cache_default_attribute["if_list"] == "first"
    assert cache_default_attribute["use_mouse"] is False
    assert cache_default_attribute["mandatory"] is True
    assert cache_default_attribute["timeout"] == 0
    assert cache_default_attribute["timeout_for_event"] == "presence_of_element_located"
    assert cache_default_attribute["event"] is None


# Test case for the 'id_default_image' locator
def test_id_default_image_locator(product_locators):
    """
     Checks the correctness of the 'id_default_image' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_default_image = product_locators.get("id_default_image")
    assert id_default_image is not None
    assert id_default_image["attribute"] is None
    assert id_default_image["by"] is None
    assert id_default_image["selector"] is None
    assert id_default_image["if_list"] == "first"
    assert id_default_image["use_mouse"] is False
    assert id_default_image["mandatory"] is True
    assert id_default_image["timeout"] == 0
    assert id_default_image["timeout_for_event"] == "presence_of_element_located"
    assert id_default_image["event"] is None


# Test case for the 'default_image_url' locator
def test_default_image_url_locator(product_locators):
    """
    Checks the correctness of the 'default_image_url' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    default_image_url = product_locators.get("default_image_url")
    assert default_image_url is not None
    assert default_image_url["attribute"] is None
    assert default_image_url["by"] == "XPATH"
    assert default_image_url["selector"] == "//div[contains(@class, 'swiper-slide')]//img"
    assert default_image_url["if_list"] == "first"
    assert default_image_url["use_mouse"] is False
    assert default_image_url["timeout"] == 0
    assert default_image_url["timeout_for_event"] == "presence_of_element_located"
    assert default_image_url["event"] == "screenshot()"
    assert default_image_url["mandatory"] is True
    assert default_image_url["locator_description"] == ""


# Test case for the 'id_default_combination' locator
def test_id_default_combination_locator(product_locators):
    """
    Checks the correctness of the 'id_default_combination' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_default_combination = product_locators.get("id_default_combination")
    assert id_default_combination is not None
    assert id_default_combination["attribute"] is None
    assert id_default_combination["by"] is None
    assert id_default_combination["selector"] is None
    assert id_default_combination["if_list"] == "first"
    assert id_default_combination["use_mouse"] is False
    assert id_default_combination["mandatory"] is True
    assert id_default_combination["timeout"] == 0
    assert id_default_combination["timeout_for_event"] == "presence_of_element_located"
    assert id_default_combination["event"] is None

# Test case for the 'id_tax' locator
def test_id_tax_locator(product_locators):
    """
    Checks the correctness of the 'id_tax' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_tax = product_locators.get("id_tax")
    assert id_tax is not None
    assert id_tax["attribute"] is None
    assert id_tax["by"] is None
    assert id_tax["selector"] is None
    assert id_tax["if_list"] == "first"
    assert id_tax["use_mouse"] is False
    assert id_tax["mandatory"] is True
    assert id_tax["timeout"] == 0
    assert id_tax["timeout_for_event"] == "presence_of_element_located"
    assert id_tax["event"] is None


# Test case for the 'position_in_category' locator
def test_position_in_category_locator(product_locators):
    """
    Checks the correctness of the 'position_in_category' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    position_in_category = product_locators.get("position_in_category")
    assert position_in_category is not None
    assert position_in_category["attribute"] is None
    assert position_in_category["by"] is None
    assert position_in_category["selector"] is None
    assert position_in_category["if_list"] == "first"
    assert position_in_category["use_mouse"] is False
    assert position_in_category["mandatory"] is True
    assert position_in_category["timeout"] == 0
    assert position_in_category["timeout_for_event"] == "presence_of_element_located"
    assert position_in_category["event"] is None


# Test case for the 'type' locator
def test_type_locator(product_locators):
    """
    Checks the correctness of the 'type' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    type_locator = product_locators.get("type")
    assert type_locator is not None
    assert type_locator["attribute"] is None
    assert type_locator["by"] is None
    assert type_locator["selector"] is None
    assert type_locator["if_list"] == "first"
    assert type_locator["use_mouse"] is False
    assert type_locator["mandatory"] is True
    assert type_locator["timeout"] == 0
    assert type_locator["timeout_for_event"] == "presence_of_element_located"
    assert type_locator["event"] is None


# Test case for the 'id_shop_default' locator
def test_id_shop_default_locator(product_locators):
    """
    Checks the correctness of the 'id_shop_default' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    id_shop_default = product_locators.get("id_shop_default")
    assert id_shop_default is not None
    assert id_shop_default["attribute"] is None
    assert id_shop_default["by"] is None
    assert id_shop_default["selector"] is None
    assert id_shop_default["if_list"] == "first"
    assert id_shop_default["use_mouse"] is False
    assert id_shop_default["mandatory"] is True
    assert id_shop_default["timeout"] == 0
    assert id_shop_default["timeout_for_event"] == "presence_of_element_located"
    assert id_shop_default["event"] is None


# Test case for the 'reference' locator
def test_reference_locator(product_locators):
    """
    Checks the correctness of the 'reference' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    reference = product_locators.get("reference")
    assert reference is not None
    assert reference["attribute"] is None
    assert reference["by"] is None
    assert reference["selector"] is None
    assert reference["if_list"] == "first"
    assert reference["use_mouse"] is False
    assert reference["mandatory"] is True
    assert reference["timeout"] == 0
    assert reference["timeout_for_event"] == "presence_of_element_located"
    assert reference["event"] is None

# Test case for the 'supplier_reference' locator
def test_supplier_reference_locator(product_locators):
    """
    Checks the correctness of the 'supplier_reference' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    supplier_reference = product_locators.get("supplier_reference")
    assert supplier_reference is not None
    assert supplier_reference["attribute"] is None
    assert supplier_reference["by"] is None
    assert supplier_reference["selector"] is None
    assert supplier_reference["if_list"] == "first"
    assert supplier_reference["use_mouse"] is False
    assert supplier_reference["mandatory"] is True
    assert supplier_reference["timeout"] == 0
    assert supplier_reference["timeout_for_event"] == "presence_of_element_located"
    assert supplier_reference["event"] is None

# Test case for the 'location' locator
def test_location_locator(product_locators):
    """
    Checks the correctness of the 'location' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    location = product_locators.get("location")
    assert location is not None
    assert location["attribute"] is None
    assert location["by"] is None
    assert location["selector"] is None
    assert location["if_list"] == "first"
    assert location["use_mouse"] is False
    assert location["mandatory"] is True
    assert location["timeout"] == 0
    assert location["timeout_for_event"] == "presence_of_element_located"
    assert location["event"] is None

# Test case for the 'width' locator
def test_width_locator(product_locators):
    """
    Checks the correctness of the 'width' locator configuration.
    Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    width = product_locators.get("width")
    assert width is not None
    assert width["attribute"] is None
    assert width["by"] is None
    assert width["selector"] is None
    assert width["if_list"] == "first"
    assert width["use_mouse"] is False
    assert width["mandatory"] is True
    assert width["timeout"] == 0
    assert width["timeout_for_event"] == "presence_of_element_located"
    assert width["event"] is None

# Test case for the 'height' locator
def test_height_locator(product_locators):
    """
    Checks the correctness of the 'height' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    height = product_locators.get("height")
    assert height is not None
    assert height["attribute"] is None
    assert height["by"] is None
    assert height["selector"] is None
    assert height["if_list"] == "first"
    assert height["use_mouse"] is False
    assert height["mandatory"] is True
    assert height["timeout"] == 0
    assert height["timeout_for_event"] == "presence_of_element_located"
    assert height["event"] is None

# Test case for the 'depth' locator
def test_depth_locator(product_locators):
    """
     Checks the correctness of the 'depth' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    depth = product_locators.get("depth")
    assert depth is not None
    assert depth["attribute"] is None
    assert depth["by"] is None
    assert depth["selector"] is None
    assert depth["if_list"] == "first"
    assert depth["use_mouse"] is False
    assert depth["mandatory"] is True
    assert depth["timeout"] == 0
    assert depth["timeout_for_event"] == "presence_of_element_located"
    assert depth["event"] is None

# Test case for the 'weight' locator
def test_weight_locator(product_locators):
    """
    Checks the correctness of the 'weight' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    weight = product_locators.get("weight")
    assert weight is not None
    assert weight["attribute"] is None
    assert weight["by"] is None
    assert weight["selector"] is None
    assert weight["if_list"] == "first"
    assert weight["use_mouse"] is False
    assert weight["mandatory"] is True
    assert weight["timeout"] == 0
    assert weight["timeout_for_event"] == "presence_of_element_located"
    assert weight["event"] is None


# Test case for the 'quantity_discount' locator
def test_quantity_discount_locator(product_locators):
    """
    Checks the correctness of the 'quantity_discount' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    quantity_discount = product_locators.get("quantity_discount")
    assert quantity_discount is not None
    assert quantity_discount["attribute"] is None
    assert quantity_discount["by"] is None
    assert quantity_discount["selector"] is None
    assert quantity_discount["if_list"] == "first"
    assert quantity_discount["use_mouse"] is False
    assert quantity_discount["mandatory"] is True
    assert quantity_discount["timeout"] == 0
    assert quantity_discount["timeout_for_event"] == "presence_of_element_located"
    assert quantity_discount["event"] is None


# Test case for the 'ean13' locator
def test_ean13_locator(product_locators):
    """
    Checks the correctness of the 'ean13' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    ean13 = product_locators.get("ean13")
    assert ean13 is not None
    assert ean13["attribute"] is None
    assert ean13["by"] is None
    assert ean13["selector"] is None
    assert ean13["if_list"] == "first"
    assert ean13["use_mouse"] is False
    assert ean13["mandatory"] is True
    assert ean13["timeout"] == 0
    assert ean13["timeout_for_event"] == "presence_of_element_located"
    assert ean13["event"] is None

# Test case for the 'isbn' locator
def test_isbn_locator(product_locators):
    """
     Checks the correctness of the 'isbn' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    isbn = product_locators.get("isbn")
    assert isbn is not None
    assert isbn["attribute"] is None
    assert isbn["by"] is None
    assert isbn["selector"] is None
    assert isbn["if_list"] == "first"
    assert isbn["use_mouse"] is False
    assert isbn["mandatory"] is True
    assert isbn["timeout"] == 0
    assert isbn["timeout_for_event"] == "presence_of_element_located"
    assert isbn["event"] is None


# Test case for the 'upc' locator
def test_upc_locator(product_locators):
    """
     Checks the correctness of the 'upc' locator configuration.
       Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    upc = product_locators.get("upc")
    assert upc is not None
    assert upc["attribute"] is None
    assert upc["by"] is None
    assert upc["selector"] is None
    assert upc["if_list"] == "first"
    assert upc["use_mouse"] is False
    assert upc["mandatory"] is True
    assert upc["timeout"] == 0
    assert upc["timeout_for_event"] == "presence_of_element_located"
    assert upc["event"] is None

# Test case for the 'mpn' locator
def test_mpn_locator(product_locators):
    """
     Checks the correctness of the 'mpn' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    mpn = product_locators.get("mpn")
    assert mpn is not None
    assert mpn["attribute"] is None
    assert mpn["by"] is None
    assert mpn["selector"] is None
    assert mpn["if_list"] == "first"
    assert mpn["use_mouse"] is False
    assert mpn["mandatory"] is True
    assert mpn["timeout"] == 0
    assert mpn["timeout_for_event"] == "presence_of_element_located"
    assert mpn["event"] is None

# Test case for the 'cache_is_pack' locator
def test_cache_is_pack_locator(product_locators):
    """
    Checks the correctness of the 'cache_is_pack' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    cache_is_pack = product_locators.get("cache_is_pack")
    assert cache_is_pack is not None
    assert cache_is_pack["attribute"] is None
    assert cache_is_pack["by"] is None
    assert cache_is_pack["selector"] is None
    assert cache_is_pack["if_list"] == "first"
    assert cache_is_pack["use_mouse"] is False
    assert cache_is_pack["mandatory"] is True
    assert cache_is_pack["timeout"] == 0
    assert cache_is_pack["timeout_for_event"] == "presence_of_element_located"
    assert cache_is_pack["event"] is None


# Test case for the 'cache_has_attachments' locator
def test_cache_has_attachments_locator(product_locators):
    """
    Checks the correctness of the 'cache_has_attachments' locator configuration.
     Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    cache_has_attachments = product_locators.get("cache_has_attachments")
    assert cache_has_attachments is not None
    assert cache_has_attachments["attribute"] is None
    assert cache_has_attachments["by"] is None
    assert cache_has_attachments["selector"] is None
    assert cache_has_attachments["if_list"] == "first"
    assert cache_has_attachments["use_mouse"] is False
    assert cache_has_attachments["mandatory"] is True
    assert cache_has_attachments["timeout"] == 0
    assert cache_has_attachments["timeout_for_event"] == "presence_of_element_located"
    assert cache_has_attachments["event"] is None

# Test case for the 'is_virtual' locator
def test_is_virtual_locator(product_locators):
    """
    Checks the correctness of the 'is_virtual' locator configuration.
      Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    is_virtual = product_locators.get("is_virtual")
    assert is_virtual is not None
    assert is_virtual["attribute"] is None
    assert is_virtual["by"] is None
    assert is_virtual["selector"] is None
    assert is_virtual["if_list"] == "first"
    assert is_virtual["use_mouse"] is False
    assert is_virtual["mandatory"] is True
    assert is_virtual["timeout"] == 0
    assert is_virtual["timeout_for_event"] == "presence_of_element_located"
    assert is_virtual["event"] is None


# Test case for the 'state' locator
def test_state_locator(product_locators):
    """
    Checks the correctness of the 'state' locator configuration.
    Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    state = product_locators.get("state")
    assert state is not None
    assert state["attribute"] is None
    assert state["by"] is None
    assert state["selector"] is None
    assert state["if_list"] == "first"
    assert state["use_mouse"] is False
    assert state["mandatory"] is True
    assert state["timeout"] == 0
    assert state["timeout_for_event"] == "presence_of_element_located"
    assert state["event"] is None


# Test case for the 'additional_delivery_times' locator
def test_additional_delivery_times_locator(product_locators):
    """
    Checks the correctness of the 'additional_delivery_times' locator configuration.
    Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    additional_delivery_times = product_locators.get("additional_delivery_times")
    assert additional_delivery_times is not None
    assert additional_delivery_times["attribute"] is None
    assert additional_delivery_times["by"] is None
    assert additional_delivery_times["selector"] is None
    assert additional_delivery_times["if_list"] == "first"
    assert additional_delivery_times["use_mouse"] is False
    assert additional_delivery_times["mandatory"] is True
    assert additional_delivery_times["timeout"] == 0
    assert additional_delivery_times["timeout_for_event"] == "presence_of_element_located"
    assert additional_delivery_times["event"] is None


# Test case for the 'delivery_in_stock' locator
def test_delivery_in_stock_locator(product_locators):
     """
    Checks the correctness of the 'delivery_in_stock' locator configuration.
    Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
     delivery_in_stock = product_locators.get("delivery_in_stock")
     assert delivery_in_stock is not None
     assert delivery_in_stock["attribute"] is None
     assert delivery_in_stock["by"] is None
     assert delivery_in_stock["selector"] is None
     assert delivery_in_stock["if_list"] == "first"
     assert delivery_in_stock["use_mouse"] is False
     assert delivery_in_stock["mandatory"] is True
     assert delivery_in_stock["timeout"] == 0
     assert delivery_in_stock["timeout_for_event"] == "presence_of_element_located"
     assert delivery_in_stock["event"] is None


# Test case for the 'delivery_out_stock' locator
def test_delivery_out_stock_locator(product_locators):
    """
     Checks the correctness of the 'delivery_out_stock' locator configuration.
    Verifies its 'by', 'selector', 'if_list', 'use_mouse', 'timeout',
    'timeout_for_event', 'event' and 'mandatory' properties.
    """
    delivery_out_stock = product_locators.get("delivery_out_stock")
    assert delivery_out_stock is not None
    assert delivery_out_stock["attribute"] is None
    assert delivery_out_stock["by"] is None
    assert delivery_out_stock["selector"] is None
    assert delivery_out_stock["if_list"] == "first"
    assert delivery_out_stock["use_mouse"]