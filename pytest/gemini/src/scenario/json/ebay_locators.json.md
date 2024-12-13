```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ebay_locators():
    """Loads the ebay_locators.json file."""
    with open("hypotez/src/scenario/json/ebay_locators.json", "r") as f:
        return json.load(f)

def test_login_open_login_selector(ebay_locators):
    """Checks the selector for the 'open_login' element is correct."""
    assert ebay_locators["login"]["open_login"]["selector"] == "//a[. = 'Sign in']"

def test_login_open_login_by(ebay_locators):
    """Checks the 'by' method for the 'open_login' element is correct."""
    assert ebay_locators["login"]["open_login"]["by"] == "XPATH"
    
def test_login_open_login_event(ebay_locators):
    """Checks the 'event' method for the 'open_login' element is correct."""
    assert ebay_locators["login"]["open_login"]["event"] == "click()"

def test_login_user_id_selector(ebay_locators):
    """Checks the selector for the 'user_id' element is correct."""
    assert ebay_locators["login"]["user_id"]["selector"] == "//input[@id = 'userid']"
    
def test_login_user_id_event(ebay_locators):
    """Checks the event for the 'user_id' element is correct"""
    assert ebay_locators["login"]["user_id"]["event"] == "send_keys('one.last.bit@gmail.com')"


def test_login_button_continue_login_selector(ebay_locators):
    """Checks the selector for the 'button_continue_login' element is correct."""
    assert ebay_locators["login"]["button_continue_login"]["selector"] == "//button[@id = 'signin-continue-btn']"

def test_login_button_continue_login_event(ebay_locators):
    """Checks the 'event' method for the 'button_continue_login' element is correct."""
    assert ebay_locators["login"]["button_continue_login"]["event"] == "click()"

def test_login_password_selector(ebay_locators):
    """Checks the selector for the 'password' element is correct."""
    assert ebay_locators["login"]["password"]["selector"] == "//input[@id = '...']"

def test_login_password_event(ebay_locators):
    """Checks the event for the 'password' element is correct"""
    assert ebay_locators["login"]["password"]["event"] == "send_keys('bG4I8y_oiOh9')"
    
def test_login_button_login_selector(ebay_locators):
    """Checks the selector for the 'button_login' element is correct."""
    assert ebay_locators["login"]["button_login"]["selector"] == "//button[@id = 'sgnBt']"
    
def test_login_button_login_event(ebay_locators):
    """Checks the 'event' method for the 'button_login' element is correct."""
    assert ebay_locators["login"]["button_login"]["event"] == "click()"

def test_pagination_next_selector(ebay_locators):
    """Checks the selector for the '->' pagination element is correct."""
    assert ebay_locators["pagination"]["->"]["selector"] == "//a[contains(@class,'pagination__next')]"

def test_pagination_next_event(ebay_locators):
    """Checks the 'event' method for the '->' pagination element is correct."""
    assert ebay_locators["pagination"]["->"]["event"] == "click()"

def test_product_product_block_locator_selector(ebay_locators):
    """Checks the selector for the 'product_block_locator' element is correct."""
    assert ebay_locators["product"]["product_block_locator"]["selector"] == "div.boxItem-wrap"

def test_product_product_block_locator_attribute(ebay_locators):
    """Checks the attribute for the 'product_block_locator' element is correct."""
    assert ebay_locators["product"]["product_block_locator"]["attribute"] == "innerHTML"

def test_product_link_to_product_locator_selector(ebay_locators):
    """Checks the selector for the 'link_to_product_locator' element is correct."""
    assert ebay_locators["product"]["link_to_product_locator"]["selector"] == "//div[@id='srp-river-results']//a[@class='s-item__link' and not(@aria-hidden='true')]"

def test_product_link_to_product_locator_attribute(ebay_locators):
    """Checks the attribute for the 'link_to_product_locator' element is correct."""
    assert ebay_locators["product"]["link_to_product_locator"]["attribute"] == "href"


def test_product_product_name_locator_selector(ebay_locators):
    """Checks the selector for the 'product_name_locator' element is correct."""
    assert ebay_locators["product"]["product_name_locator"]["selector"] == "//h1[contains(@class,'mainTitle')]"
    
def test_product_product_name_locator_attribute(ebay_locators):
     """Checks the attribute for the 'product_name_locator' element is correct."""
     assert ebay_locators["product"]["product_name_locator"]["attribute"] == "innerText"

def test_product_brand_locator_selector(ebay_locators):
    """Checks the selector for the 'brand_locator' element is correct."""
    assert ebay_locators["product"]["brand_locator"]["selector"] == ".brands"

def test_product_brand_locator_attribute(ebay_locators):
    """Checks the attribute for the 'brand_locator' element is correct."""
    assert ebay_locators["product"]["brand_locator"]["attribute"] == "innerHTML"

def test_product_sku_locator_selector(ebay_locators):
    """Checks the selector for the 'sku_locator' element is correct."""
    assert ebay_locators["product"]["sku_locator"]["selector"] == "div[class=sku] span[itemprop='sku']"
    
def test_product_sku_locator_attribute(ebay_locators):
    """Checks the attribute for the 'sku_locator' element is correct."""
    assert ebay_locators["product"]["sku_locator"]["attribute"] == "innerHTML"

def test_product_brand_sku_locator_selector(ebay_locators):
    """Checks the selector for the 'brand_sku_locator' element is correct."""
    assert ebay_locators["product"]["brand_sku_locator"]["selector"] == "div[class=sku] span[itemprop='sku']"
    
def test_product_brand_sku_locator_attribute(ebay_locators):
    """Checks the attribute for the 'brand_sku_locator' element is correct."""
    assert ebay_locators["product"]["brand_sku_locator"]["attribute"] == "innerHTML"


def test_product_summary_locator_selector(ebay_locators):
    """Checks the selector for the 'summary_locator' element is correct."""
    assert ebay_locators["product"]["summary_locator"]["selector"] == "//div[@class=product-name]//h1[itemprop()='name']"

def test_product_summary_locator_attribute(ebay_locators):
    """Checks the attribute for the 'summary_locator' element is correct."""
    assert ebay_locators["product"]["summary_locator"]["attribute"] == "innerHTML"

def test_product_description_locator_selector(ebay_locators):
    """Checks the selector for the 'description_locator' element is correct."""
    assert ebay_locators["product"]["description_locator"]["selector"] == "//div[contains(@class, 'x-about-this-item')]"

def test_product_description_locator_attribute(ebay_locators):
    """Checks the attribute for the 'description_locator' element is correct."""
    assert ebay_locators["product"]["description_locator"]["attribute"] == "innerHTML"

def test_product_images_locator_selector(ebay_locators):
    """Checks the selector for the 'images_locator' element is correct."""
    assert ebay_locators["product"]["images_locator"]["selector"] == "//div[contains(@class,'ux-image-carousel-item')]//img"

def test_product_images_locator_attribute(ebay_locators):
    """Checks the attribute for the 'images_locator' element is correct."""
    assert ebay_locators["product"]["images_locator"]["attribute"] == "src"
    
def test_product_main_image_locator_selector(ebay_locators):
    """Checks the selector for the 'main_image_locator' element is correct."""
    assert ebay_locators["product"]["main_image_locator"]["selector"] == "//div[@class='ux-image-carousel-item active image']"

def test_product_main_image_locator_event(ebay_locators):
    """Checks the event for the 'main_image_locator' element is correct."""
    assert ebay_locators["product"]["main_image_locator"]["event"] == "screenshot()"
    

def test_product_price_locator_selector(ebay_locators):
    """Checks the selector for the 'price_locator' element is correct."""
    assert ebay_locators["product"]["price_locator"]["selector"] == "//span[@class = 'x-price-approx__price']"

def test_product_price_locator_attribute(ebay_locators):
    """Checks the attribute for the 'price_locator' element is correct."""
    assert ebay_locators["product"]["price_locator"]["attribute"] == "innerText"
    
def test_product_qty_locator_selector(ebay_locators):
    """Checks the selector for the 'qty_locator' element is correct."""
    assert ebay_locators["product"]["qty_locator"]["selector"] == "//span[@id = 'qtySubTxt']"

def test_product_qty_locator_attribute(ebay_locators):
    """Checks the attribute for the 'qty_locator' element is correct."""
    assert ebay_locators["product"]["qty_locator"]["attribute"] == "innerText"

def test_product_condition_locator_selector(ebay_locators):
    """Checks the selector for the 'condition_locator' element is correct."""
    assert ebay_locators["product"]["condition_locator"]["selector"] == "//div[@class='d-item-condition-text']//following-sibling::span[@class = 'ux-textspans']"
    
def test_product_condition_locator_attribute(ebay_locators):
    """Checks the attribute for the 'condition_locator' element is correct."""
    assert ebay_locators["product"]["condition_locator"]["attribute"] == "innerText"
```