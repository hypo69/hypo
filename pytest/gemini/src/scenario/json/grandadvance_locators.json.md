```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Loads the JSON data from the file."""
    with open("hypotez/src/scenario/json/grandadvance_locators.json", 'r') as f:
        data = json.load(f)
    return data

# Test for category locators
def test_category_pages_listing_locator(json_data):
    """Checks the structure and values of the pages_listing_locator."""
    locator = json_data['category']['pages_listing_locator']
    assert isinstance(locator, dict), "pages_listing_locator should be a dict"
    assert locator['attribute'] == 'href', "attribute should be 'href'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == 'a.glyphicon-triangle-right', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

# Test for product block locators
def test_product_product_block_locator(json_data):
    """Checks the structure and values of the product_block_locator."""
    locator = json_data['product']['product_block_locator']
    assert isinstance(locator, dict), "product_block_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == 'div.prod', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

def test_product_link_to_product_locator(json_data):
    """Checks the structure and values of the link_to_product_locator."""
    locator = json_data['product']['link_to_product_locator']
    assert isinstance(locator, dict), "link_to_product_locator should be a dict"
    assert locator['attribute'] == 'href', "attribute should be 'href'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.name a', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"


# Test for product fields locators
def test_product_fields_brand_locator(json_data):
    """Checks the structure and values of the brand_locator."""
    locator = json_data['product_fields_locators']['brand_locator']
    assert isinstance(locator, dict), "brand_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.brands', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"


def test_product_fields_brand_sku_locator(json_data):
     """Checks the structure and values of the brand_sku_locator."""
     locator = json_data['product_fields_locators']['brand_sku_locator']
     assert isinstance(locator, dict), "brand_sku_locator should be a dict"
     assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
     assert locator['by'] == 'XPATH', "by should be 'XPATH'"
     assert locator['selector'] == "//*[@id=\'aspnetForm\']/center/div[1]/div/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/b", "selector does not match"
     assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

def test_product_fields_summary_locator(json_data):
    """Checks the structure and values of the summary_locator."""
    locator = json_data['product_fields_locators']['summary_locator']
    assert isinstance(locator, dict), "summary_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.pp_pp_ttcc', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

def test_product_fields_description_locator(json_data):
    """Checks the structure and values of the description_locator."""
    locator = json_data['product_fields_locators']['description_locator']
    assert isinstance(locator, dict), "description_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.pp_ttc', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"


def test_product_fields_images_locator(json_data):
    """Checks the structure and values of the images_locator."""
    locator = json_data['product_fields_locators']['images_locator']
    assert isinstance(locator, dict), "images_locator should be a dict"
    assert locator['attribute'] == 'href', "attribute should be 'href'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == 'td.pp_dp a', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

def test_product_fields_price_locator(json_data):
    """Checks the structure and values of the price_locator."""
    locator = json_data['product_fields_locators']['price_locator']
    assert isinstance(locator, dict), "price_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.pp_sp.rc', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"


def test_product_fields_sku_locator(json_data):
    """Checks the structure and values of the sku_locator."""
    locator = json_data['product_fields_locators']['sku_locator']
    assert isinstance(locator, dict), "sku_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.lPartNumber', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

def test_product_fields_product_name_locator(json_data):
    """Checks the structure and values of the product_name_locator."""
    locator = json_data['product_fields_locators']['product_name_locator']
    assert isinstance(locator, dict), "product_name_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.pp_n', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

# Test for stock locators
def test_stock_locator(json_data):
    """Checks the structure and values of the stock_locator."""
    locator = json_data['stock_locator']
    assert isinstance(locator, dict), "stock_locator should be a dict"
    assert locator['attribute'] == 'innerHTML', "attribute should be 'innerHTML'"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == '.t_b.a_r', "selector does not match"
    assert locator['logic for attribue[AND|OR|XOR|VALUE|null]'] is None, "Logic should be null"

def test_not_in_stock_values(json_data):
    """Checks the values of the 'not in stock' list."""
    not_in_stock = json_data['not in stock']
    assert isinstance(not_in_stock, list), "'not in stock' should be a list"
    assert len(not_in_stock) == 2, "There should be 2 values in the list"
    assert "color:red" in not_in_stock, "color:red should be in the list"
    assert "color:#d19b00" in not_in_stock, "color:#d19b00 should be in the list"


# Test for login locators
def test_login_open_login_dialog_locator(json_data):
    """Checks the structure and values of the open_login_dialog_locator."""
    locator = json_data['login']['open_login_dialog_locator']
    assert isinstance(locator, dict), "open_login_dialog_locator should be a dict"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == 'div.col-md-12.login button', "selector does not match"

def test_login_email_values(json_data):
    """Checks email value and its locator."""
    login_data = json_data['login']
    assert isinstance(login_data['email'], str), "email should be a string"
    assert login_data['email'] == 'sales@aluf.co.il', "email does not match"
    locator = login_data['email_selector']
    assert isinstance(locator, dict), "email_selector should be a dict"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == 'input.mp_ltb.tbEmail', "selector does not match"

def test_login_password_values(json_data):
     """Checks password value and its locator."""
     login_data = json_data['login']
     assert isinstance(login_data['password'], str), "password should be a string"
     assert login_data['password'] == '0ee33', "password does not match"
     locator = login_data['password_locator']
     assert isinstance(locator, dict), "password_locator should be a dict"
     assert locator['by'] == 'css selector', "by should be 'css selector'"
     assert locator['selector'] == '.mp_ltb.tbPassword', "selector does not match"

def test_login_loginbutton_locator(json_data):
    """Checks the structure and values of the loginbutton_locator."""
    locator = json_data['login']['loginbutton_locator']
    assert isinstance(locator, dict), "loginbutton_locator should be a dict"
    assert locator['by'] == 'css selector', "by should be 'css selector'"
    assert locator['selector'] == 'div.ui-dialog-buttonpane button', "selector does not match"

# Test for other values
def test_infinity_scroll_value(json_data):
    """Checks the value of infinity_scroll."""
    assert isinstance(json_data['infinity_scroll'], bool), "infinity_scroll should be a boolean"
    assert json_data['infinity_scroll'] is False, "infinity_scroll should be False"

def test_checkboxes_for_categories_value(json_data):
    """Checks the value of checkboxes_for_categories."""
    assert isinstance(json_data['checkboxes_for_categories'], bool), "checkboxes_for_categories should be a boolean"
    assert json_data['checkboxes_for_categories'] is True, "checkboxes_for_categories should be True"
```