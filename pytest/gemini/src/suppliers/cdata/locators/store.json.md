```python
import pytest
import json

# Assuming the file is read and its content is loaded into a dictionary for testing purposes
# Placeholder for the actual content
STORE_JSON_CONTENT = {
    "store": {
        "home": {
            "page_title": "//title",
            "cookie_button": "//div[@id='cookies-agree']" ,
            "logo": "//div[@class='logo']//img"
          },
        "products":{
           "item_list":"//div[contains(@class,'products-list')]/div[@class='item']",
           "item_title":"./div[@class='item-title']",
           "item_price":"./div[@class='item-price']"
         },
        "product_page": {
          "title": "//h1[@class='product-title']",
          "description":"//div[@class='product-description']",
          "price":"//span[@class='product-price']",
          "add_to_cart_button":"//button[@id='add-to-cart']"
         },
        "cart_page": {
           "item_list":"//div[@class='cart-items']/div[@class='cart-item']",
           "item_title":"./div[@class='cart-item-title']",
           "item_price":"./div[@class='cart-item-price']",
           "total_price":"//span[@class='cart-total-price']",
           "checkout_button":"//button[@id='checkout']"
          }
        }
}

@pytest.fixture
def store_locators():
    """Provides the loaded store locators dictionary."""
    return STORE_JSON_CONTENT.get("store",{})


# Tests for the 'home' locators
def test_home_page_title_locator(store_locators):
    """Checks if the page title locator is present and correct."""
    assert "home" in store_locators, "Home locators are missing"
    assert "page_title" in store_locators["home"], "page_title locator is missing"
    assert store_locators["home"]["page_title"] == "//title", "Incorrect page_title locator"

def test_home_cookie_button_locator(store_locators):
    """Checks if the cookie button locator is present and correct."""
    assert "home" in store_locators, "Home locators are missing"
    assert "cookie_button" in store_locators["home"], "cookie_button locator is missing"
    assert store_locators["home"]["cookie_button"] == "//div[@id='cookies-agree']", "Incorrect cookie_button locator"
    
def test_home_logo_locator(store_locators):
     """Checks if the logo locator is present and correct."""
     assert "home" in store_locators, "Home locators are missing"
     assert "logo" in store_locators["home"], "logo locator is missing"
     assert store_locators["home"]["logo"] == "//div[@class='logo']//img", "Incorrect logo locator"
     

# Tests for the 'products' locators
def test_products_item_list_locator(store_locators):
     """Checks if the item list locator is present and correct."""
     assert "products" in store_locators, "Products locators are missing"
     assert "item_list" in store_locators["products"], "item_list locator is missing"
     assert store_locators["products"]["item_list"] == "//div[contains(@class,'products-list')]/div[@class='item']", "Incorrect item_list locator"
    
def test_products_item_title_locator(store_locators):
     """Checks if the item title locator is present and correct."""
     assert "products" in store_locators, "Products locators are missing"
     assert "item_title" in store_locators["products"], "item_title locator is missing"
     assert store_locators["products"]["item_title"] == "./div[@class='item-title']", "Incorrect item_title locator"
    
def test_products_item_price_locator(store_locators):
     """Checks if the item price locator is present and correct."""
     assert "products" in store_locators, "Products locators are missing"
     assert "item_price" in store_locators["products"], "item_price locator is missing"
     assert store_locators["products"]["item_price"] == "./div[@class='item-price']", "Incorrect item_price locator"
     
# Tests for the 'product_page' locators
def test_product_page_title_locator(store_locators):
    """Checks if the product page title locator is present and correct."""
    assert "product_page" in store_locators, "product_page locators are missing"
    assert "title" in store_locators["product_page"], "title locator is missing"
    assert store_locators["product_page"]["title"] == "//h1[@class='product-title']", "Incorrect title locator"
    
def test_product_page_description_locator(store_locators):
    """Checks if the product page description locator is present and correct."""
    assert "product_page" in store_locators, "product_page locators are missing"
    assert "description" in store_locators["product_page"], "description locator is missing"
    assert store_locators["product_page"]["description"] == "//div[@class='product-description']", "Incorrect description locator"

def test_product_page_price_locator(store_locators):
    """Checks if the product page price locator is present and correct."""
    assert "product_page" in store_locators, "product_page locators are missing"
    assert "price" in store_locators["product_page"], "price locator is missing"
    assert store_locators["product_page"]["price"] == "//span[@class='product-price']", "Incorrect price locator"

def test_product_page_add_to_cart_button_locator(store_locators):
    """Checks if the product page add to cart button locator is present and correct."""
    assert "product_page" in store_locators, "product_page locators are missing"
    assert "add_to_cart_button" in store_locators["product_page"], "add_to_cart_button locator is missing"
    assert store_locators["product_page"]["add_to_cart_button"] == "//button[@id='add-to-cart']", "Incorrect add_to_cart_button locator"

# Tests for the 'cart_page' locators
def test_cart_page_item_list_locator(store_locators):
    """Checks if the cart page item list locator is present and correct."""
    assert "cart_page" in store_locators, "cart_page locators are missing"
    assert "item_list" in store_locators["cart_page"], "item_list locator is missing"
    assert store_locators["cart_page"]["item_list"] == "//div[@class='cart-items']/div[@class='cart-item']", "Incorrect item_list locator"
    
def test_cart_page_item_title_locator(store_locators):
    """Checks if the cart page item title locator is present and correct."""
    assert "cart_page" in store_locators, "cart_page locators are missing"
    assert "item_title" in store_locators["cart_page"], "item_title locator is missing"
    assert store_locators["cart_page"]["item_title"] == "./div[@class='cart-item-title']", "Incorrect item_title locator"
    
def test_cart_page_item_price_locator(store_locators):
    """Checks if the cart page item price locator is present and correct."""
    assert "cart_page" in store_locators, "cart_page locators are missing"
    assert "item_price" in store_locators["cart_page"], "item_price locator is missing"
    assert store_locators["cart_page"]["item_price"] == "./div[@class='cart-item-price']", "Incorrect item_price locator"
   
def test_cart_page_total_price_locator(store_locators):
    """Checks if the cart page total price locator is present and correct."""
    assert "cart_page" in store_locators, "cart_page locators are missing"
    assert "total_price" in store_locators["cart_page"], "total_price locator is missing"
    assert store_locators["cart_page"]["total_price"] == "//span[@class='cart-total-price']", "Incorrect total_price locator"
    
def test_cart_page_checkout_button_locator(store_locators):
    """Checks if the cart page checkout button locator is present and correct."""
    assert "cart_page" in store_locators, "cart_page locators are missing"
    assert "checkout_button" in store_locators["cart_page"], "checkout_button locator is missing"
    assert store_locators["cart_page"]["checkout_button"] == "//button[@id='checkout']", "Incorrect checkout_button locator"

def test_invalid_store_data():
     """Check if not exist store key."""
     invalid_store_data = {}
     assert invalid_store_data.get("store",{}) == {}, "Return empty dict if store not exist"
```