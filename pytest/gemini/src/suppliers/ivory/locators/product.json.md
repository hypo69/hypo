```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def product_locators():
    """Loads the product locator data from the JSON file."""
    file_path = 'hypotez/src/suppliers/ivory/locators/product.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test cases for the structure and basic data of the loaded JSON
def test_product_locators_is_dict(product_locators):
    """Checks if the loaded data is a dictionary."""
    assert isinstance(product_locators, dict), "Loaded data is not a dictionary"

def test_product_locators_not_empty(product_locators):
    """Checks if the loaded dictionary is not empty."""
    assert product_locators, "Loaded data is empty"

# Test cases for each locator's structure and keys
def test_close_pop_up_locator_structure(product_locators):
    """Checks the structure and keys of the 'close_pop_up' locator."""
    locator = product_locators.get("close_pop_up")
    assert locator is not None, "close_pop_up locator not found"
    assert isinstance(locator, dict), "close_pop_up locator is not a dictionary"
    assert 'attribute' in locator, "close_pop_up is missing attribute key"
    assert 'by' in locator, "close_pop_up is missing by key"
    assert 'selector' in locator, "close_pop_up is missing selector key"
    assert 'if_list' in locator, "close_pop_up is missing if_list key"
    assert 'use_mouse' in locator, "close_pop_up is missing use_mouse key"
    assert 'timeout' in locator, "close_pop_up is missing timeout key"
    assert 'timeout_for_event' in locator, "close_pop_up is missing timeout_for_event key"
    assert 'event' in locator, "close_pop_up is missing event key"
    assert 'mandatory' in locator, "close_pop_up is missing mandatory key"
    assert 'locator_description' in locator, "close_pop_up is missing locator_description key"

def test_id_locator_structure(product_locators):
    """Checks the structure and keys of the 'id' locator."""
    locator = product_locators.get("id")
    assert locator is not None, "id locator not found"
    assert isinstance(locator, dict), "id locator is not a dictionary"
    assert 'attribute' in locator, "id is missing attribute key"
    assert 'by' in locator, "id is missing by key"
    assert 'selector' in locator, "id is missing selector key"
    assert 'if_list' in locator, "id is missing if_list key"
    assert 'use_mouse' in locator, "id is missing use_mouse key"
    assert 'mandatory' in locator, "id is missing mandatory key"
    assert 'timeout' in locator, "id is missing timeout key"
    assert 'timeout_for_event' in locator, "id is missing timeout_for_event key"
    assert 'event' in locator, "id is missing event key"

def test_id_manufacturer_locator_structure(product_locators):
    """Checks the structure and keys of the 'id_manufacturer' locator."""
    locator = product_locators.get("id_manufacturer")
    assert locator is not None, "id_manufacturer locator not found"
    assert isinstance(locator, dict), "id_manufacturer locator is not a dictionary"
    assert 'attribute' in locator, "id_manufacturer is missing attribute key"
    assert 'by' in locator, "id_manufacturer is missing by key"
    assert 'selector' in locator, "id_manufacturer is missing selector key"
    assert 'if_list' in locator, "id_manufacturer is missing if_list key"
    assert 'use_mouse' in locator, "id_manufacturer is missing use_mouse key"
    assert 'mandatory' in locator, "id_manufacturer is missing mandatory key"
    assert 'timeout' in locator, "id_manufacturer is missing timeout key"
    assert 'timeout_for_event' in locator, "id_manufacturer is missing timeout_for_event key"
    assert 'event' in locator, "id_manufacturer is missing event key"
    assert 'locator_description' in locator, "id_manufacturer is missing locator_description key"

def test_id_supplier_locator_structure(product_locators):
    """Checks the structure and keys of the 'id_supplier' locator."""
    locator = product_locators.get("id_supplier")
    assert locator is not None, "id_supplier locator not found"
    assert isinstance(locator, dict), "id_supplier locator is not a dictionary"
    assert 'attribute' in locator, "id_supplier is missing attribute key"
    assert 'by' in locator, "id_supplier is missing by key"
    assert 'selector' in locator, "id_supplier is missing selector key"
    assert 'if_list' in locator, "id_supplier is missing if_list key"
    assert 'use_mouse' in locator, "id_supplier is missing use_mouse key"
    assert 'mandatory' in locator, "id_supplier is missing mandatory key"
    assert 'timeout' in locator, "id_supplier is missing timeout key"
    assert 'timeout_for_event' in locator, "id_supplier is missing timeout_for_event key"
    assert 'event' in locator, "id_supplier is missing event key"
    assert 'locator_description' in locator, "id_supplier is missing locator_description key"


def test_id_product_locator_structure(product_locators):
    """Checks the structure and keys of the 'id_product' locator."""
    locator = product_locators.get("id_product")
    assert locator is not None, "id_product locator not found"
    assert isinstance(locator, dict), "id_product locator is not a dictionary"
    assert 'attribute' in locator, "id_product is missing attribute key"
    assert 'by' in locator, "id_product is missing by key"
    assert 'selector' in locator, "id_product is missing selector key"
    assert 'if_list' in locator, "id_product is missing if_list key"
    assert 'use_mouse' in locator, "id_product is missing use_mouse key"
    assert 'mandatory' in locator, "id_product is missing mandatory key"
    assert 'timeout' in locator, "id_product is missing timeout key"
    assert 'timeout_for_event' in locator, "id_product is missing timeout_for_event key"
    assert 'event' in locator, "id_product is missing event key"
    assert 'locator_description' in locator, "id_product is missing locator_description key"

def test_default_image_url_locator_structure(product_locators):
    """Checks the structure and keys of the 'default_image_url' locator."""
    locator = product_locators.get("default_image_url")
    assert locator is not None, "default_image_url locator not found"
    assert isinstance(locator, dict), "default_image_url locator is not a dictionary"
    assert 'attribute' in locator, "default_image_url is missing attribute key"
    assert 'by' in locator, "default_image_url is missing by key"
    assert 'selector' in locator, "default_image_url is missing selector key"
    assert 'if_list' in locator, "default_image_url is missing if_list key"
    assert 'use_mouse' in locator, "default_image_url is missing use_mouse key"
    assert 'timeout' in locator, "default_image_url is missing timeout key"
    assert 'timeout_for_event' in locator, "default_image_url is missing timeout_for_event key"
    assert 'event' in locator, "default_image_url is missing event key"
    assert 'mandatory' in locator, "default_image_url is missing mandatory key"
    assert 'locator_description' in locator, "default_image_url is missing locator_description key"

def test_name_locator_structure(product_locators):
     """Checks the structure and keys of the 'name' locator."""
     locator = product_locators.get("name")
     assert locator is not None, "name locator not found"
     assert isinstance(locator, dict), "name locator is not a dictionary"
     assert 'attribute' in locator, "name is missing attribute key"
     assert 'by' in locator, "name is missing by key"
     assert 'selector' in locator, "name is missing selector key"
     assert 'if_list' in locator, "name is missing if_list key"
     assert 'use_mouse' in locator, "name is missing use_mouse key"
     assert 'timeout' in locator, "name is missing timeout key"
     assert 'timeout_for_event' in locator, "name is missing timeout_for_event key"
     assert 'event' in locator, "name is missing event key"
     assert 'mandatory' in locator, "name is missing mandatory key"
     assert 'locator_description' in locator, "name is missing locator_description key"


def test_description_short_locator_structure(product_locators):
     """Checks the structure and keys of the 'description_short' locator."""
     locator = product_locators.get("description_short")
     assert locator is not None, "description_short locator not found"
     assert isinstance(locator, dict), "description_short locator is not a dictionary"
     assert 'attribute' in locator, "description_short is missing attribute key"
     assert 'by' in locator, "description_short is missing by key"
     assert 'selector' in locator, "description_short is missing selector key"
     assert 'if_list' in locator, "description_short is missing if_list key"
     assert 'use_mouse' in locator, "description_short is missing use_mouse key"
     assert 'timeout' in locator, "description_short is missing timeout key"
     assert 'timeout_for_event' in locator, "description_short is missing timeout_for_event key"
     assert 'event' in locator, "description_short is missing event key"
     assert 'mandatory' in locator, "description_short is missing mandatory key"
     assert 'locator_description' in locator, "description_short is missing locator_description key"

def test_description_locator_structure(product_locators):
    """Checks the structure and keys of the 'description' locator."""
    locator = product_locators.get("description")
    assert locator is not None, "description locator not found"
    assert isinstance(locator, dict), "description locator is not a dictionary"
    assert 'attribute' in locator, "description is missing attribute key"
    assert 'by' in locator, "description is missing by key"
    assert 'selector' in locator, "description is missing selector key"
    assert 'if_list' in locator, "description is missing if_list key"
    assert 'use_mouse' in locator, "description is missing use_mouse key"
    assert 'mandatory' in locator, "description is missing mandatory key"
    assert 'timeout' in locator, "description is missing timeout key"
    assert 'timeout_for_event' in locator, "description is missing timeout_for_event key"
    assert 'event' in locator, "description is missing event key"
    assert 'locator_description' in locator, "description is missing locator_description key"


def test_specification_locator_structure(product_locators):
     """Checks the structure and keys of the 'specification' locator."""
     locator = product_locators.get("specification")
     assert locator is not None, "specification locator not found"
     assert isinstance(locator, dict), "specification locator is not a dictionary"
     assert 'attribute' in locator, "specification is missing attribute key"
     assert 'by' in locator, "specification is missing by key"
     assert 'selector' in locator, "specification is missing selector key"
     assert 'if_list' in locator, "specification is missing if_list key"
     assert 'use_mouse' in locator, "specification is missing use_mouse key"
     assert 'timeout' in locator, "specification is missing timeout key"
     assert 'timeout_for_event' in locator, "specification is missing timeout_for_event key"
     assert 'event' in locator, "specification is missing event key"
     assert 'mandatory' in locator, "specification is missing mandatory key"
     assert 'locator_description' in locator, "specification is missing locator_description key"

def test_ASIN_locator_structure(product_locators):
     """Checks the structure and keys of the 'ASIN' locator."""
     locator = product_locators.get("ASIN")
     assert locator is not None, "ASIN locator not found"
     assert isinstance(locator, dict), "ASIN locator is not a dictionary"
     assert 'attribute' in locator, "ASIN is missing attribute key"
     assert 'by' in locator, "ASIN is missing by key"
     assert 'selector' in locator, "ASIN is missing selector key"
     assert 'if_list' in locator, "ASIN is missing if_list key"
     assert 'use_mouse' in locator, "ASIN is missing use_mouse key"
     assert 'timeout' in locator, "ASIN is missing timeout key"
     assert 'timeout_for_event' in locator, "ASIN is missing timeout_for_event key"
     assert 'event' in locator, "ASIN is missing event key"
     assert 'mandatory' in locator, "ASIN is missing mandatory key"

def test_Name_star_locator_structure(product_locators):
     """Checks the structure and keys of the 'Name*' locator."""
     locator = product_locators.get("Name*")
     assert locator is not None, "Name* locator not found"
     assert isinstance(locator, dict), "Name* locator is not a dictionary"
     assert 'attribute' in locator, "Name* is missing attribute key"
     assert 'by' in locator, "Name* is missing by key"
     assert 'selector' in locator, "Name* is missing selector key"
     assert 'if_list' in locator, "Name* is missing if_list key"
     assert 'use_mouse' in locator, "Name* is missing use_mouse key"
     assert 'timeout' in locator, "Name* is missing timeout key"
     assert 'timeout_for_event' in locator, "Name* is missing timeout_for_event key"
     assert 'event' in locator, "Name* is missing event key"
     assert 'mandatory' in locator, "Name* is missing mandatory key"

def test_Price_tax_excluded_locator_structure(product_locators):
     """Checks the structure and keys of the 'Price tax excluded' locator."""
     locator = product_locators.get("Price tax excluded")
     assert locator is not None, "Price tax excluded locator not found"
     assert isinstance(locator, dict), "Price tax excluded locator is not a dictionary"
     assert 'attribute' in locator, "Price tax excluded is missing attribute key"
     assert 'by' in locator, "Price tax excluded is missing by key"
     assert 'selector' in locator, "Price tax excluded is missing selector key"
     assert 'if_list' in locator, "Price tax excluded is missing if_list key"
     assert 'use_mouse' in locator, "Price tax excluded is missing use_mouse key"
     assert 'timeout' in locator, "Price tax excluded is missing timeout key"
     assert 'timeout_for_event' in locator, "Price tax excluded is missing timeout_for_event key"
     assert 'event' in locator, "Price tax excluded is missing event key"
     assert 'mandatory' in locator, "Price tax excluded is missing mandatory key"

def test_brand_locator_structure(product_locators):
     """Checks the structure and keys of the 'Brand' locator."""
     locator = product_locators.get("Brand")
     assert locator is not None, "Brand locator not found"
     assert isinstance(locator, dict), "Brand locator is not a dictionary"
     assert 'attribute' in locator, "Brand is missing attribute key"
     assert 'by' in locator, "Brand is missing by key"
     assert 'selector' in locator, "Brand is missing selector key"
     assert 'if_list' in locator, "Brand is missing if_list key"
     assert 'use_mouse' in locator, "Brand is missing use_mouse key"
     assert 'timeout' in locator, "Brand is missing timeout key"
     assert 'timeout_for_event' in locator, "Brand is missing timeout_for_event key"
     assert 'event' in locator, "Brand is missing event key"
     assert 'mandatory' in locator, "Brand is missing mandatory key"

def test_summary_locator_structure(product_locators):
     """Checks the structure and keys of the 'Summary' locator."""
     locator = product_locators.get("Summary")
     assert locator is not None, "Summary locator not found"
     assert isinstance(locator, dict), "Summary locator is not a dictionary"
     assert 'attribute' in locator, "Summary is missing attribute key"
     assert 'by' in locator, "Summary is missing by key"
     assert 'selector' in locator, "Summary is missing selector key"
     assert 'if_list' in locator, "Summary is missing if_list key"
     assert 'use_mouse' in locator, "Summary is missing use_mouse key"
     assert 'timeout' in locator, "Summary is missing timeout key"
     assert 'timeout_for_event' in locator, "Summary is missing timeout_for_event key"
     assert 'event' in locator, "Summary is missing event key"
     assert 'mandatory' in locator, "Summary is missing mandatory key"

def test_Description_locator_structure(product_locators):
     """Checks the structure and keys of the 'Description' locator."""
     locator = product_locators.get("Description")
     assert locator is not None, "Description locator not found"
     assert isinstance(locator, dict), "Description locator is not a dictionary"
     assert 'attribute' in locator, "Description is missing attribute key"
     assert 'by' in locator, "Description is missing by key"
     assert 'selector' in locator, "Description is missing selector key"
     assert 'if_list' in locator, "Description is missing if_list key"
     assert 'use_mouse' in locator, "Description is missing use_mouse key"
     assert 'timeout' in locator, "Description is missing timeout key"
     assert 'timeout_for_event' in locator, "Description is missing timeout_for_event key"
     assert 'event' in locator, "Description is missing event key"
     assert 'mandatory' in locator, "Description is missing mandatory key"

def test_Screenshot_locator_structure(product_locators):
    """Checks the structure and keys of the 'Screenshot' locator."""
    locator = product_locators.get("Screenshot")
    assert locator is not None, "Screenshot locator not found"
    assert isinstance(locator, dict), "Screenshot locator is not a dictionary"
    assert 'attribute' in locator, "Screenshot is missing attribute key"
    assert 'by' in locator, "Screenshot is missing by key"
    assert 'selector' in locator, "Screenshot is missing selector key"
    assert 'if_list' in locator, "Screenshot is missing if_list key"
    assert 'use_mouse' in locator, "Screenshot is missing use_mouse key"
    assert 'timeout' in locator, "Screenshot is missing timeout key"
    assert 'timeout_for_event' in locator, "Screenshot is missing timeout_for_event key"
    assert 'event' in locator, "Screenshot is missing event key"
    assert 'mandatory' in locator, "Screenshot is missing mandatory key"
    assert 'logic for action[AND|OR|XOR|VALUE|null]' in locator, "Screenshot is missing logic for action[AND|OR|XOR|VALUE|null] key"

def test_images_urls_locator_structure(product_locators):
     """Checks the structure and keys of the 'images_urls' locator."""
     locator = product_locators.get("images_urls")
     assert locator is not None, "images_urls locator not found"
     assert isinstance(locator, dict), "images_urls locator is not a dictionary"
     assert 'attribute' in locator, "images_urls is missing attribute key"
     assert 'by' in locator, "images_urls is missing by key"
     assert 'selector' in locator, "images_urls is missing selector key"
     assert 'if_list' in locator, "images_urls is missing if_list key"
     assert 'use_mouse' in locator, "images_urls is missing use_mouse key"
     assert 'timeout' in locator, "images_urls is missing timeout key"
     assert 'timeout_for_event' in locator, "images_urls is missing timeout_for_event key"
     assert 'event' in locator, "images_urls is missing event key"
     assert 'mandatory' in locator, "images_urls is missing mandatory key"
     assert 'locator_description' in locator, "images_urls is missing locator_description key"


def test_affiliate_short_link_locator_structure(product_locators):
    """Checks the structure and keys of the 'affiliate short link' locator."""
    locator = product_locators.get("affiliate short link")
    assert locator is not None, "affiliate short link locator not found"
    assert isinstance(locator, dict), "affiliate short link locator is not a dictionary"
    assert 'logic for attribue[AND|OR|XOR|VALUE|null]' in locator, "affiliate short link is missing logic for attribue[AND|OR|XOR|VALUE|null] key"
    assert 'attribute' in locator, "affiliate short link is missing attribute key"
    assert 'by' in locator, "affiliate short link is missing by key"
    assert 'selector' in locator, "affiliate short link is missing selector key"
    assert 'if_list' in locator, "affiliate short link is missing if_list key"
    assert 'use_mouse' in locator, "affiliate short link is missing use_mouse key"
    assert 'timeout' in locator, "affiliate short link is missing timeout key"
    assert 'timeout_for_event' in locator, "affiliate short link is missing timeout_for_event key"
    assert 'event' in locator, "affiliate short link is missing event key"
    assert 'logic for action[AND|OR|XOR|VALUE|null]' in locator, "affiliate short link is missing logic for action[AND|OR|XOR|VALUE|null] key"

# Test case to check all keys are strings
def test_all_locator_keys_are_strings(product_locators):
    """Checks if all keys in the locators dictionary are strings."""
    for key in product_locators:
        assert isinstance(key, str), f"Key '{key}' is not a string"
```