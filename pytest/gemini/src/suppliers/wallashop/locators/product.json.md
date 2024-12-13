```python
import pytest
import json

# Fixture to load the product locator data from the JSON file
@pytest.fixture
def product_locators():
    """Provides the product locators data loaded from the JSON file."""
    with open('hypotez/src/suppliers/wallashop/locators/product.json', 'r') as f:
        return json.load(f)


def test_product_locators_id_exists(product_locators):
    """Check that the 'id' locator exists and has the mandatory fields."""
    assert "id" in product_locators
    assert "attribute" in product_locators["id"]
    assert "by" in product_locators["id"]
    assert "selector" in product_locators["id"]
    assert "if_list" in product_locators["id"]
    assert "use_mouse" in product_locators["id"]
    assert "mandatory" in product_locators["id"]
    assert "timeout" in product_locators["id"]
    assert "timeout_for_event" in product_locators["id"]
    assert "event" in product_locators["id"]

def test_product_locators_id_supplier_exists(product_locators):
    """Check that the 'id_supplier' locator exists and has the mandatory fields."""
    assert "id_supplier" in product_locators
    assert "attribute" in product_locators["id_supplier"]
    assert "by" in product_locators["id_supplier"]
    assert "selector" in product_locators["id_supplier"]
    assert "if_list" in product_locators["id_supplier"]
    assert "use_mouse" in product_locators["id_supplier"]
    assert "mandatory" in product_locators["id_supplier"]
    assert "timeout" in product_locators["id_supplier"]
    assert "timeout_for_event" in product_locators["id_supplier"]
    assert "event" in product_locators["id_supplier"]

def test_product_locators_id_supplier_attribute_value(product_locators):
     """Check that 'id_supplier' attribute is 2777."""
     assert product_locators["id_supplier"]["attribute"] == 2777


def test_product_locators_id_supplier_by_value(product_locators):
    """Check that 'id_supplier' by is VALUE."""
    assert product_locators["id_supplier"]["by"] == "VALUE"

def test_product_locators_mandatory_fields_are_true(product_locators):
    """Check that all mandatory fields are set to True."""
    for locator_key, locator_data in product_locators.items():
        if isinstance(locator_data, dict):
             assert locator_data.get("mandatory", False) is True


def test_product_locators_all_keys_exist(product_locators):
     """Check if all the expected keys are present in the locators."""
     expected_keys = [
        "id", "id_manufacturer", "id_supplier", "id_category_default", "new",
        "cache_default_attribute", "id_default_image", "id_default_combination",
        "id_tax", "position_in_category", "type", "id_shop_default", "reference",
        "supplier_reference", "location", "width", "height", "depth", "weight",
        "quantity_discount", "ean13", "isbn", "upc", "mpn", "cache_is_pack",
        "cache_has_attachments", "is_virtual", "state", "additional_delivery_times",
        "delivery_in_stock", "delivery_out_stock", "product_type", "on_sale",
        "online_only", "ecotax", "minimal_quantity", "low_stock_threshold",
        "low_stock_alert", "price", "wholesale_price", "unity", "unit_price_ratio",
        "additional_shipping_cost", "customizable", "text_fields", "uploadable_files",
        "active", "redirect_type", "id_type_redirected", "available_for_order",
        "available_date", "show_condition", "condition", "show_price", "indexed",
        "visibility", "advanced_stock_management", "date_add", "date_upd",
        "pack_stock_type", "meta_description", "meta_keywords", "meta_title",
        "link_rewrite", "name", "description", "description_short", "specification",
        "affiliate_short_link", "affiliate_text", "affiliate_summary",
        "affiliate_summary_2", "available_now", "available_later", "associations",
        "ASIN", "Active (0/1)", "Name*", "Categories (x,y,z...)",
        "Price tax excluded", "Price tax included", "Tax rule ID", "Cost price",
        "On sale (0/1)", "Discount amount", "Discount percent",
        "Discount from (yyyy-mm-dd)", "Discount to (yyyy-mm-dd)", "reference #",
        "Supplier reference #", "Supplier", "Brand", "EAN13", "UPC", "MPN",
        "Ecotax", "Width", "Height", "Depth", "Weight",
        "Delivery time of in-stock products:",
        "Delivery time of out-of-stock products with allowed orders:", "Quantity",
        "Minimal quantity", "Low stock level",
        "Send me an email when the quantity is under this level", "Visibility",
        "Additional shipping cost", "Unit for base price", "Base price", "Summary",
        "Description", "Tags (x,y,z...)", "Meta title", "Meta keywords",
        "Meta description", "Rewritten URL", "Label when in stock",
        "Label when backorder allowed", "Available for order (0 = No, 1 = Yes)",
        "Product availability date", "Product creation date",
        "Show price (0 = No, 1 = Yes)", "Screenshot", "additional_images_urls",
        "additional_images_alts", "Delete existing images (0 = No, 1 = Yes)",
        "Feature (Name:Value:Position:Customized)",
        "Available online only (0 = No, 1 = Yes)", "Condition",
        "Customizable (0 = No, 1 = Yes)", "Uploadable files (0 = No, 1 = Yes)",
        "Text fields (0 = No, 1 = Yes)", "Action when out of stock",
        "Virtual product (0 = No, 1 = Yes)", "File URL",
        "Number of allowed downloads", "Expiration date (yyyy-mm-dd)",
        "Number of days", "ID / Name of shop", "Advanced Stock Management",
        "Depends on stock", "Warehouse", "Accessories (x,y,z...)",
         "affiliate short link", "affiliate text","affiliate summary",
         "affiliate summary 2","Open AI Product Description", "Byer protection",
        "Specification", "Refirbished product description",
        "Additional shipping details"
     ]
     assert all(key in product_locators for key in expected_keys)


def test_product_locators_specification_details(product_locators):
     """Check specific details of the 'specification' locator."""
     assert product_locators["specification"]["attribute"] == ""
     assert product_locators["specification"]["by"] == "XPATH"
     assert product_locators["specification"]["selector"] == ""
     assert product_locators["specification"]["if_list"] == "all"
     assert product_locators["specification"]["use_mouse"] == False
     assert product_locators["specification"]["mandatory"] == True
     assert product_locators["specification"]["timeout"] == 0
     assert product_locators["specification"]["timeout_for_event"] == "presence_of_element_located"
     assert product_locators["specification"]["event"] == None
     assert product_locators["specification"]["locator_description"] == "Технические характеристики. "


def test_product_locators_affiliate_short_link_logic(product_locators):
     """Check the complex structure of 'affiliate short link' locator."""
     affiliate_short_link = product_locators["affiliate short link"]
     assert affiliate_short_link["logic for attribue[AND|OR|XOR|VALUE|null]"] == [None, None]
     assert affiliate_short_link["attribute"] == [None, "value"]
     assert affiliate_short_link["by"] == ["XPATH", "XPATH"]
     assert affiliate_short_link["selector"] == ["//li[contains(@id,\'amzn-ss-text-link\')]", "//textarea[contains(@id,\'amzn-ss-text-shortlink-textarea\')]"]
     assert affiliate_short_link["if_list"] == "first"
     assert affiliate_short_link["use_mouse"] == [False, False]
     assert affiliate_short_link["timeout"] == 0
     assert affiliate_short_link["timeout_for_event"] == "presence_of_element_located"
     assert affiliate_short_link["event"] == ["wait(click(),2,after)", None]
     assert affiliate_short_link["logic for action[AND|OR|XOR|VALUE|null]"] == [None, None]

def test_product_locators_screenshot_event(product_locators):
    """Check that 'Screenshot' locator has the correct event."""
    assert product_locators["Screenshot"]["event"] == "screenshot()"


def test_product_locators_screenshot_selector(product_locators):
    """Check that 'Screenshot' locator has the correct selector."""
    assert product_locators["Screenshot"]["selector"] == "//img[@id='landingImage']|//img[@class='a-dynamic-image']"


def test_product_locators_price_tax_excluded_selector(product_locators):
    """Check that 'Price tax excluded' locator has the correct selector."""
    assert product_locators["Price tax excluded"]["selector"] == "//div[contains(@id,'corePrice')]//span[@class ='a-price-whole'][1]"


def test_product_locators_name_star_selector(product_locators):
    """Check that 'Name*' locator has the correct selector."""
    assert product_locators["Name*"]["selector"] == "//span[@id='productTitle']"


def test_product_locators_brand_selector(product_locators):
    """Check that 'Brand' locator has the correct selector."""
    assert product_locators["Brand"]["selector"] == "//span[contains(text(), 'Brand')]/parent::td/following-sibling::td/span[contains(@class, 'po-break-word')]"

def test_product_locators_summary_selector(product_locators):
    """Check that 'Summary' locator has the correct selector."""
    assert product_locators["Summary"]["selector"] == "//div[contains(@data-a-expander-name , 'product_overview')]//table"

def test_product_locators_description_selector(product_locators):
    """Check that 'Description' locator has the correct selector."""
    assert product_locators["Description"]["selector"] == "//div[@id='productDescription']"

```