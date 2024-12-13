```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def dornet_locators_data():
    """Loads the JSON data from the file."""
    with open('hypotez/src/scenario/json/dornet_locators.json', 'r') as f:
        return json.load(f)

# Test cases for the 'category' locators
def test_category_pages_listing_locator_valid(dornet_locators_data):
    """Checks the validity of 'pages_listing_locator' within 'category'."""
    locator = dornet_locators_data['category']['pages_listing_locator']
    assert locator['attribute'] == 'href'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == 'li.next-page a'
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


# Test cases for the 'product' locators
def test_product_product_block_locator_valid(dornet_locators_data):
    """Checks the validity of 'product_block_locator' within 'product'."""
    locator = dornet_locators_data['product']['product_block_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == 'div.boxItem-wrap'
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None
    

def test_product_link_to_product_locator_valid(dornet_locators_data):
    """Checks the validity of 'link_to_product_locator' within 'product'."""
    locator = dornet_locators_data['product']['link_to_product_locator']
    assert locator['attribute'] == 'href'
    assert locator['by'] == 'XPATH'
    assert locator['selector'] == "//a[@class=\'str-item-card__property-title\']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

# Test cases for the 'product_fields_locators'
def test_product_fields_product_name_locator_valid(dornet_locators_data):
    """Checks the validity of 'product_name_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['product_name_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == "div[class=product-name] h1[itemprop='name']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


def test_product_fields_brand_locator_valid(dornet_locators_data):
    """Checks the validity of 'brand_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['brand_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == ".brands"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_product_fields_sku_locator_valid(dornet_locators_data):
    """Checks the validity of 'sku_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['sku_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == "div[class=sku] span[itemprop='sku']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

def test_product_fields_brand_sku_locator_valid(dornet_locators_data):
    """Checks the validity of 'brand_sku_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['brand_sku_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == "div[class=sku] span[itemprop='sku']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None
    
def test_product_fields_summary_locator_valid(dornet_locators_data):
    """Checks the validity of 'summary_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['summary_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == "div[class=product-name] h1[itemprop='name']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None
    

def test_product_fields_description_locator_valid(dornet_locators_data):
    """Checks the validity of 'description_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['description_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == ".data-table[role='presentation']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


def test_product_fields_images_locator_valid(dornet_locators_data):
    """Checks the validity of 'images_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['images_locator']
    assert locator['attribute'] == 'src'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == ".cloudzoom"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None
    

def test_product_fields_price_locator_valid(dornet_locators_data):
    """Checks the validity of 'price_locator' within 'product_fields_locators'."""
    locator = dornet_locators_data['product_fields_locators']['price_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == "div span[itemprop='price']"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None

# Test cases for the 'stock_locator'
def test_stock_locator_valid(dornet_locators_data):
    """Checks the validity of 'stock_locator'."""
    locator = dornet_locators_data['stock_locator']
    assert locator['attribute'] == 'innerHTML'
    assert locator['by'] == 'css selector'
    assert locator['selector'] == ".value.stock_staus"
    assert locator['timeout'] == 0
    assert locator['timeout_for_event'] == 'presence_of_element_located'
    assert locator['event'] is None
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None
    assert locator['logic for action[AND|OR|XOR|VALUE|null]'] is None


# Test cases for the 'not in stock' list
def test_not_in_stock_list_valid(dornet_locators_data):
    """Checks the validity of 'not in stock' list."""
    not_in_stock_list = dornet_locators_data['not in stock']
    assert isinstance(not_in_stock_list, list)
    assert "color:red" in not_in_stock_list
    assert "color:#d19b00" in not_in_stock_list


def test_dornet_locators_data_structure(dornet_locators_data):
    """Validates the overall structure of the loaded JSON data."""
    assert isinstance(dornet_locators_data, dict)
    assert 'category' in dornet_locators_data
    assert 'product' in dornet_locators_data
    assert 'product_fields_locators' in dornet_locators_data
    assert 'stock_locator' in dornet_locators_data
    assert 'not in stock' in dornet_locators_data
    
    assert isinstance(dornet_locators_data['category'], dict)
    assert isinstance(dornet_locators_data['product'], dict)
    assert isinstance(dornet_locators_data['product_fields_locators'], dict)
    assert isinstance(dornet_locators_data['stock_locator'], dict)
    assert isinstance(dornet_locators_data['not in stock'], list)
```