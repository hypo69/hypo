```python
import pytest
import json

# Fixture to load the product locator data from the JSON file
@pytest.fixture
def product_locators():
    """Loads the product locators from the JSON file."""
    with open("hypotez/src/suppliers/morlevi/locators/product.json", "r") as f:
        return json.load(f)

# Test cases for "close_pop_up" locator
def test_close_pop_up_valid_data(product_locators):
    """Checks the 'close_pop_up' locator with valid data."""
    locator = product_locators.get("close_pop_up")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//button[@class='close']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] == True
    assert locator["locator_description"] == "Кнопка закрытия попап окна"

def test_close_pop_up_missing_key(product_locators):
    """Checks for the absence of a key in 'close_pop_up'."""
    locator = product_locators.get("close_pop_up")
    assert "invalid_key" not in locator


# Test cases for "id" locator
def test_id_valid_data(product_locators):
    """Checks the 'id' locator with valid data."""
    locator = product_locators.get("id")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "id_manufacturer" locator
def test_id_manufacturer_valid_data(product_locators):
    """Checks the 'id_manufacturer' locator with valid data."""
    locator = product_locators.get("id_manufacturer")
    assert locator is not None
    assert locator["attribute"] == "innerText"
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[@class = 'ltr sku-copy']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    assert locator["locator_description"] == "SKU morlevi"

# Test cases for "id_supplier" locator
def test_id_supplier_valid_data(product_locators):
    """Checks the 'id_supplier' locator with valid data."""
    locator = product_locators.get("id_supplier")
    assert locator is not None
    assert locator["attribute"] == 2784
    assert locator["by"] == "VALUE"
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    assert locator["locator_description"] == "SKU morlevi"

# Test cases for "id_product" locator
def test_id_product_valid_data(product_locators):
    """Checks the 'id_product' locator with valid data."""
    locator = product_locators.get("id_product")
    assert locator is not None
    assert locator["attribute"] == "innerText"
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[@class = 'ltr sku-copy']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    assert locator["locator_description"] == "SKU morlevi"


# Test cases for "id_category_default" locator
def test_id_category_default_valid_data(product_locators):
    """Checks the 'id_category_default' locator with valid data."""
    locator = product_locators.get("id_category_default")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "new" locator
def test_new_valid_data(product_locators):
    """Checks the 'new' locator with valid data."""
    locator = product_locators.get("new")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "cache_default_attribute" locator
def test_cache_default_attribute_valid_data(product_locators):
    """Checks the 'cache_default_attribute' locator with valid data."""
    locator = product_locators.get("cache_default_attribute")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "id_default_image" locator
def test_id_default_image_valid_data(product_locators):
    """Checks the 'id_default_image' locator with valid data."""
    locator = product_locators.get("id_default_image")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "default_image_url" locator
def test_default_image_url_valid_data(product_locators):
    """Checks the 'default_image_url' locator with valid data."""
    locator = product_locators.get("default_image_url")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//a[@id = 'mainpic']//img"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "screenshot()"
    assert locator["mandatory"] == True
    assert locator["locator_description"] == "Внимание! в морлеви картинка получается через screenshot и возвращается как png (`bytes`)"


# Test cases for "id_default_combination" locator
def test_id_default_combination_valid_data(product_locators):
    """Checks the 'id_default_combination' locator with valid data."""
    locator = product_locators.get("id_default_combination")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "id_tax" locator
def test_id_tax_valid_data(product_locators):
    """Checks the 'id_tax' locator with valid data."""
    locator = product_locators.get("id_tax")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "position_in_category" locator
def test_position_in_category_valid_data(product_locators):
    """Checks the 'position_in_category' locator with valid data."""
    locator = product_locators.get("position_in_category")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "type" locator
def test_type_valid_data(product_locators):
    """Checks the 'type' locator with valid data."""
    locator = product_locators.get("type")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "id_shop_default" locator
def test_id_shop_default_valid_data(product_locators):
    """Checks the 'id_shop_default' locator with valid data."""
    locator = product_locators.get("id_shop_default")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "reference" locator
def test_reference_valid_data(product_locators):
    """Checks the 'reference' locator with valid data."""
    locator = product_locators.get("reference")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "supplier_reference" locator
def test_supplier_reference_valid_data(product_locators):
    """Checks the 'supplier_reference' locator with valid data."""
    locator = product_locators.get("supplier_reference")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "location" locator
def test_location_valid_data(product_locators):
    """Checks the 'location' locator with valid data."""
    locator = product_locators.get("location")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "width" locator
def test_width_valid_data(product_locators):
    """Checks the 'width' locator with valid data."""
    locator = product_locators.get("width")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "height" locator
def test_height_valid_data(product_locators):
    """Checks the 'height' locator with valid data."""
    locator = product_locators.get("height")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "depth" locator
def test_depth_valid_data(product_locators):
    """Checks the 'depth' locator with valid data."""
    locator = product_locators.get("depth")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "weight" locator
def test_weight_valid_data(product_locators):
    """Checks the 'weight' locator with valid data."""
    locator = product_locators.get("weight")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "quantity_discount" locator
def test_quantity_discount_valid_data(product_locators):
    """Checks the 'quantity_discount' locator with valid data."""
    locator = product_locators.get("quantity_discount")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "ean13" locator
def test_ean13_valid_data(product_locators):
    """Checks the 'ean13' locator with valid data."""
    locator = product_locators.get("ean13")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "isbn" locator
def test_isbn_valid_data(product_locators):
    """Checks the 'isbn' locator with valid data."""
    locator = product_locators.get("isbn")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "upc" locator
def test_upc_valid_data(product_locators):
    """Checks the 'upc' locator with valid data."""
    locator = product_locators.get("upc")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "mpn" locator
def test_mpn_valid_data(product_locators):
    """Checks the 'mpn' locator with valid data."""
    locator = product_locators.get("mpn")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "cache_is_pack" locator
def test_cache_is_pack_valid_data(product_locators):
    """Checks the 'cache_is_pack' locator with valid data."""
    locator = product_locators.get("cache_is_pack")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "cache_has_attachments" locator
def test_cache_has_attachments_valid_data(product_locators):
    """Checks the 'cache_has_attachments' locator with valid data."""
    locator = product_locators.get("cache_has_attachments")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "is_virtual" locator
def test_is_virtual_valid_data(product_locators):
    """Checks the 'is_virtual' locator with valid data."""
    locator = product_locators.get("is_virtual")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "state" locator
def test_state_valid_data(product_locators):
    """Checks the 'state' locator with valid data."""
    locator = product_locators.get("state")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "additional_delivery_times" locator
def test_additional_delivery_times_valid_data(product_locators):
    """Checks the 'additional_delivery_times' locator with valid data."""
    locator = product_locators.get("additional_delivery_times")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "delivery_in_stock" locator
def test_delivery_in_stock_valid_data(product_locators):
    """Checks the 'delivery_in_stock' locator with valid data."""
    locator = product_locators.get("delivery_in_stock")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "delivery_out_stock" locator
def test_delivery_out_stock_valid_data(product_locators):
    """Checks the 'delivery_out_stock' locator with valid data."""
    locator = product_locators.get("delivery_out_stock")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "product_type" locator
def test_product_type_valid_data(product_locators):
    """Checks the 'product_type' locator with valid data."""
    locator = product_locators.get("product_type")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "on_sale" locator
def test_on_sale_valid_data(product_locators):
    """Checks the 'on_sale' locator with valid data."""
    locator = product_locators.get("on_sale")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "online_only" locator
def test_online_only_valid_data(product_locators):
    """Checks the 'online_only' locator with valid data."""
    locator = product_locators.get("online_only")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "ecotax" locator
def test_ecotax_valid_data(product_locators):
    """Checks the 'ecotax' locator with valid data."""
    locator = product_locators.get("ecotax")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "minimal_quantity" locator
def test_minimal_quantity_valid_data(product_locators):
    """Checks the 'minimal_quantity' locator with valid data."""
    locator = product_locators.get("minimal_quantity")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "low_stock_threshold" locator
def test_low_stock_threshold_valid_data(product_locators):
    """Checks the 'low_stock_threshold' locator with valid data."""
    locator = product_locators.get("low_stock_threshold")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
# Test cases for "low_stock_alert" locator
def test_low_stock_alert_valid_data(product_locators):
    """Checks the 'low_stock_alert' locator with valid data."""
    locator = product_locators.get("low_stock_alert")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "price" locator
def test_price_valid_data(product_locators):
    """Checks the 'price' locator with valid data."""
    locator = product_locators.get("price")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "wholesale_price" locator
def test_wholesale_price_valid_data(product_locators):
    """Checks the 'wholesale_price' locator with valid data."""
    locator = product_locators.get("wholesale_price")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "unity" locator
def test_unity_valid_data(product_locators):
    """Checks the 'unity' locator with valid data."""
    locator = product_locators.get("unity")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "unit_price_ratio" locator
def test_unit_price_ratio_valid_data(product_locators):
    """Checks the 'unit_price_ratio' locator with valid data."""
    locator = product_locators.get("unit_price_ratio")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "additional_shipping_cost" locator
def test_additional_shipping_cost_valid_data(product_locators):
    """Checks the 'additional_shipping_cost' locator with valid data."""
    locator = product_locators.get("additional_shipping_cost")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Test cases for "customizable" locator
def test_customizable_valid_data(product_locators):
    """Checks the 'customizable' locator with valid data."""
    locator = product_locators.get("customizable")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == False
    assert locator["mandatory"] == True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Test cases for "text_fields" locator
def test_text_fields_valid_data(product_locators):
    """Checks the 'text_fields' locator with valid data."""
    locator = product_locators.get("text_fields")
    assert locator is not None
    assert locator["attribute"] is None
    assert locator["by"] is None
    assert locator["selector"] is None
    assert locator["if_