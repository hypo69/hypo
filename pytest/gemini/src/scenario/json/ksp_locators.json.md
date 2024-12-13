```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_locators_data():
    """Loads the ksp_locators.json data."""
    with open("hypotez/src/scenario/json/ksp_locators.json", "r") as file:
        return json.load(file)

# Test cases for the 'languages' section
def test_languages_he_selector(ksp_locators_data):
    """Checks the selector for the 'he' language."""
    assert ksp_locators_data["languages"]["he"]["selector"] == "//li[@data-value='he']"

def test_languages_en_attribute(ksp_locators_data):
    """Checks the attribute for the 'en' language."""
    assert ksp_locators_data["languages"]["en"]["attribute"] is None

def test_languages_ru_event(ksp_locators_data):
    """Checks the event for the 'ru' language."""
    assert ksp_locators_data["languages"]["ru"]["event"] == "sendKeys(Keys.RETURN)"

def test_languages_timeout_default(ksp_locators_data):
    """Checks if default timeout is 0 for languages section"""
    for lang_data in ksp_locators_data["languages"].values():
        assert lang_data["timeout"] == 0
        
# Test cases for the 'infinity_scroll' property
def test_infinity_scroll_value(ksp_locators_data):
    """Checks the value of 'infinity_scroll'."""
    assert ksp_locators_data["infinity_scroll"] is True

# Test cases for the 'checkboxes_for_categories' property
def test_checkboxes_for_categories_value(ksp_locators_data):
    """Checks the value of 'checkboxes_for_categories'."""
    assert ksp_locators_data["checkboxes_for_categories"] is False

# Test cases for 'category' -> 'pages_listing_locator'
def test_category_pages_listing_selector(ksp_locators_data):
    """Checks the selector for 'pages_listing_locator'."""
    assert ksp_locators_data["category"]["pages_listing_locator"]["selector"] == "infinity_scroll"

def test_category_pages_listing_attribute(ksp_locators_data):
    """Checks the attribute for 'pages_listing_locator'."""
    assert ksp_locators_data["category"]["pages_listing_locator"]["attribute"] == "innerHTML"

# Test cases for 'top_banner_locator'
def test_top_banner_locator_selector(ksp_locators_data):
    """Checks the selector for 'top_banner_locator'."""
    assert ksp_locators_data["top_banner_locator"]["selector"] == "//ul[contains(@class , 'slider animated')]//img"

def test_top_banner_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'top_banner_locator'."""
    assert ksp_locators_data["top_banner_locator"]["attribute"] == {"src" : None}

# Test cases for 'product' -> 'link_to_product_locator'
def test_product_link_to_product_selector(ksp_locators_data):
    """Checks the selector for 'link_to_product_locator'."""
    assert ksp_locators_data["product"]["link_to_product_locator"]["selector"] == "//a[contains(@class,'MuiTypography') and contains(@href , 'web/item')]"

def test_product_link_to_product_attribute(ksp_locators_data):
    """Checks the attribute for 'link_to_product_locator'."""
    assert ksp_locators_data["product"]["link_to_product_locator"]["attribute"] == "href"

# Test cases for 'product' -> 'product_block_locator'
def test_product_block_locator_selector(ksp_locators_data):
    """Checks the selector for 'product_block_locator'."""
    assert ksp_locators_data["product"]["product_block_locator"]["selector"] == "//*[@id='product-page-root']"

def test_product_block_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'product_block_locator'."""
    assert ksp_locators_data["product"]["product_block_locator"]["attribute"] == "innerHTML"

# Test cases for 'product' -> 'sku_locator'
def test_product_sku_locator_selector(ksp_locators_data):
    """Checks the selector for 'sku_locator'."""
    assert ksp_locators_data["product"]["sku_locator"]["selector"] == "//*[contains(@data-id, 'product-')]/span"

def test_product_sku_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'sku_locator'."""
    assert ksp_locators_data["product"]["sku_locator"]["attribute"] == "innerText"

# Test cases for 'product' -> 'product_name_locator'
def test_product_name_locator_selector(ksp_locators_data):
    """Checks the selector for 'product_name_locator'."""
    assert ksp_locators_data["product"]["product_name_locator"]["selector"] == "//*[@id='product-page-root']//h1//span"

def test_product_name_locator_attribute(ksp_locators_data):
     """Checks the attribute for 'product_name_locator'."""
     assert ksp_locators_data["product"]["product_name_locator"]["attribute"] == "innerText"

def test_product_name_locator_replaced_by_driver(ksp_locators_data):
     """Checks the  'replaced by driver.title' value for 'product_name_locator'."""
     assert ksp_locators_data["product"]["product_name_locator"]["replaced by driver.title"] is None

# Test cases for 'product' -> 'price_locator'
def test_product_price_locator_selector(ksp_locators_data):
    """Checks the selector for 'price_locator'."""
    assert ksp_locators_data["product"]["price_locator"]["selector"] == "//*[@id='product-page-root']//div[@aria-label]//div[text()]"

def test_product_price_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'price_locator'."""
    assert ksp_locators_data["product"]["price_locator"]["attribute"] == "innerText"

# Test cases for 'product' -> 'product_delivery_locator'
def test_product_delivery_locator_selector(ksp_locators_data):
     """Checks the selector for 'product_delivery_locator'."""
     assert ksp_locators_data["product"]["product_delivery_locator"]["selector"] == "//h2[contains(@aria-label ,'אפשרויות איסוף ומשלו')]//following::ul//li[contains(@aria-label ,'משלוח')]"

def test_product_delivery_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'product_delivery_locator'."""
    assert ksp_locators_data["product"]["product_delivery_locator"]["attribute"] is None

# Test cases for 'product' -> 'main_image_locator'
def test_product_main_image_locator_selector(ksp_locators_data):
    """Checks the selector for 'main_image_locator'."""
    assert ksp_locators_data["product"]["main_image_locator"]["selector"] == "//li[contains(@class ,'slide selected')]//div//img"

def test_product_main_image_locator_event(ksp_locators_data):
    """Checks the event for 'main_image_locator'."""
    assert ksp_locators_data["product"]["main_image_locator"]["event"] == "screenshot()"

# Test cases for 'product' -> 'summary_locator'
def test_product_summary_locator_selector(ksp_locators_data):
    """Checks the selector for 'summary_locator'."""
    assert ksp_locators_data["product"]["summary_locator"]["selector"] == "//p[contains(text(),'תיאור קצר')]//following-sibling::p[1]"

def test_product_summary_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'summary_locator'."""
    assert ksp_locators_data["product"]["summary_locator"]["attribute"] == "innerHTML"

# Test cases for 'product' -> 'description_locator'
def test_product_description_locator_selector(ksp_locators_data):
    """Checks the selector for 'description_locator'."""
    assert ksp_locators_data["product"]["description_locator"]["selector"] == "//div[contains(@id , 'review-section')]"

def test_product_description_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'description_locator'."""
    assert ksp_locators_data["product"]["description_locator"]["attribute"] == "innerText"

# Test cases for 'product' -> 'specification_locator'
def test_product_specification_locator_selector(ksp_locators_data):
    """Checks the selector for 'specification_locator'."""
    assert ksp_locators_data["product"]["specification_locator"]["selector"] == "//div[contains(@id , 'review-section')]"

def test_product_specification_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'specification_locator'."""
    assert ksp_locators_data["product"]["specification_locator"]["attribute"] is None

# Test case for 'customer_reviews_locator'
def test_product_customer_reviews_locator_is_null(ksp_locators_data):
    """Checks that 'customer_reviews_locator' is null."""
    assert ksp_locators_data["product"]["customer_reviews_locator"] is None
    
# Test cases for 'product' -> 'product_attributes_locator'
def test_product_attributes_locator_selector(ksp_locators_data):
    """Checks the selector for 'product_attributes_locator'."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["selector"] == "//*[@id='product-page-root']//div[@aria-label]//following-sibling::div/p[1]"

def test_product_attributes_locator_attribute(ksp_locators_data):
    """Checks the attribute for 'product_attributes_locator'."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["attribute"] == "innerHTML"

# Test cases for 'product' -> 'product_attributes_locator' -> 'color'
def test_product_attributes_color_selector(ksp_locators_data):
    """Checks the selector for 'color' attribute."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["product attribute"]["color"]["selector"] == "//h3[contains(@aria-label , 'בחירת צבע')]/following-sibling::*"

def test_product_attributes_color_attribute(ksp_locators_data):
    """Checks the attribute for 'color' attribute."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["product attribute"]["color"]["attribute"] is None

# Test cases for 'product' -> 'product_attributes_locator' -> 'phone memory'
def test_product_attributes_phone_memory_selector(ksp_locators_data):
    """Checks the selector for 'phone memory' attribute."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["product attribute"]["phone memory"]["selector"] == "//h3[contains(@aria-label , 'בחירת נפח')]/following-sibling::*"

def test_product_attributes_phone_memory_attribute(ksp_locators_data):
    """Checks the attribute for 'phone memory' attribute."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["product attribute"]["phone memory"]["attribute"] is None

# Test cases for 'product' -> 'product_attributes_locator' -> 'delivery'
def test_product_attributes_delivery_selector(ksp_locators_data):
    """Checks the selector for 'delivery' attribute."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["product attribute"]["delivery"]["selector"] == "//h3[contains(@aria-label , 'אפשרויות איסוף ומשלוח')]/following-sibling::*"

def test_product_attributes_delivery_attribute(ksp_locators_data):
    """Checks the attribute for 'delivery' attribute."""
    assert ksp_locators_data["product"]["product_attributes_locator"]["product attribute"]["delivery"]["attribute"] is None
```