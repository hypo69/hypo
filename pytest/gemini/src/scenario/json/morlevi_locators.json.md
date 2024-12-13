```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_locators_data():
    """Loads the morlevi_locators.json data."""
    with open("hypotez/src/scenario/json/morlevi_locators.json", "r") as f:
        return json.load(f)

# Test cases for 'infinity_scroll'
def test_infinity_scroll_valid(morlevi_locators_data):
    """Checks if 'infinity_scroll' key exists and is a boolean."""
    assert "infinity_scroll" in morlevi_locators_data
    assert isinstance(morlevi_locators_data["infinity_scroll"], bool)

# Test cases for 'checkboxes_for_categories'
def test_checkboxes_for_categories_valid(morlevi_locators_data):
    """Checks if 'checkboxes_for_categories' key exists and is a boolean."""
    assert "checkboxes_for_categories" in morlevi_locators_data
    assert isinstance(morlevi_locators_data["checkboxes_for_categories"], bool)

# Test cases for 'pagination'
def test_pagination_ul_valid(morlevi_locators_data):
    """Checks the structure and values of pagination.ul."""
    pagination_ul = morlevi_locators_data.get("pagination", {}).get("ul")
    assert pagination_ul is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in pagination_ul
    assert "attribute" in pagination_ul
    assert "by" in pagination_ul
    assert "selector" in pagination_ul
    assert "timeout" in pagination_ul
    assert "timeout_for_event" in pagination_ul
    assert "event" in pagination_ul
    assert pagination_ul["by"] == "XPATH"
    assert pagination_ul["selector"] == "//ul[@class='pagination']"
    assert isinstance(pagination_ul["timeout"], int)
    assert pagination_ul["timeout_for_event"] == "presence_of_element_located"
    assert pagination_ul["event"] == "click()"

def test_pagination_a_valid(morlevi_locators_data):
    """Checks the structure and values of pagination.a."""
    pagination_a = morlevi_locators_data.get("pagination", {}).get("a")
    assert pagination_a is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in pagination_a
    assert "attribute" in pagination_a
    assert "by" in pagination_a
    assert "selector" in pagination_a
    assert "timeout" in pagination_a
    assert "timeout_for_event" in pagination_a
    assert "event" in pagination_a
    assert pagination_a["by"] == "XPATH"
    assert pagination_a["selector"] == "//ul[@class='pagination']//a[@class='page-link']"
    assert isinstance(pagination_a["timeout"], int)
    assert pagination_a["timeout_for_event"] == "presence_of_element_located"
    assert pagination_a["event"] == "click()"


# Test cases for 'close_pop_up_locator'
def test_close_pop_up_locator_valid(morlevi_locators_data):
    """Checks the structure and values of close_pop_up_locator."""
    close_pop_up = morlevi_locators_data.get("close_pop_up_locator")
    assert close_pop_up is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in close_pop_up
    assert "attribute" in close_pop_up
    assert "by" in close_pop_up
    assert "selector" in close_pop_up
    assert "timeout" in close_pop_up
    assert "timeout_for_event" in close_pop_up
    assert "event" in close_pop_up
    assert close_pop_up["by"] == "XPATH"
    assert close_pop_up["selector"] == "//div[@class='modal-dialog']//button[@class='close']"
    assert isinstance(close_pop_up["timeout"], int)
    assert close_pop_up["timeout_for_event"] == "presence_of_element_located"
    assert close_pop_up["event"] == "click()"


# Test cases for 'store'
def test_store_categories_valid(morlevi_locators_data):
    """Checks the structure and values of store.store categories."""
    store_categories = morlevi_locators_data.get("store", {}).get("store categories")
    assert store_categories is not None
    assert "description" in store_categories
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in store_categories
    assert "attribute" in store_categories
    assert "by" in store_categories
    assert "selector" in store_categories
    assert "logic for action[AND|OR|XOR|VALUE|null]" in store_categories
    assert "timeout" in store_categories
    assert "timeout_for_event" in store_categories
    assert "event" in store_categories
    assert store_categories["description"] == "Список катагероий магазина"
    assert store_categories["attribute"] == {"innerText": "href"}
    assert store_categories["by"] == "XPATH"
    assert store_categories["selector"] == "//li[@class='group-item']//a"
    assert store_categories["event"] is None
    assert isinstance(store_categories["timeout"], int)
    assert store_categories["timeout_for_event"] == "presence_of_element_located"



# Test cases for 'product'
def test_product_link_to_product_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.link_to_product_locator."""
    link_locator = morlevi_locators_data.get("product", {}).get("link_to_product_locator")
    assert link_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in link_locator
    assert "attribute" in link_locator
    assert "by" in link_locator
    assert "selector" in link_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in link_locator
    assert "timeout" in link_locator
    assert "timeout_for_event" in link_locator
    assert "event" in link_locator
    assert link_locator["attribute"] == "href"
    assert link_locator["by"] == "XPATH"
    assert link_locator["selector"] == "//div[@class = 'product-thumb']/a"
    assert link_locator["event"] is None
    assert isinstance(link_locator["timeout"], int)
    assert link_locator["timeout_for_event"] == "presence_of_element_located"

def test_product_stock_available_valid(morlevi_locators_data):
     """Checks the structure and values of product.stock_available."""
     stock_available = morlevi_locators_data.get("product", {}).get("stock available")
     assert stock_available is not None
     assert "logic for attribue[AND|OR|XOR|VALUE|null]" in stock_available
     assert "attribute" in stock_available
     assert "by" in stock_available
     assert "selector" in stock_available
     assert "logic for action[AND|OR|XOR|VALUE|null]" in stock_available
     assert "timeout" in stock_available
     assert "timeout_for_event" in stock_available
     assert "event" in stock_available
     assert stock_available["attribute"] == "innerText"
     assert stock_available["by"] == "XPATH"
     assert stock_available["selector"] == "//div[conatins(@class , 'stockMsg')]"
     assert stock_available["event"] is None
     assert isinstance(stock_available["timeout"], int)
     assert stock_available["timeout_for_event"] == "presence_of_element_located"


def test_product_product_name_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.product_name_locator."""
    name_locator = morlevi_locators_data.get("product", {}).get("product_name_locator")
    assert name_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in name_locator
    assert "attribute" in name_locator
    assert "by" in name_locator
    assert "selector" in name_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in name_locator
    assert "timeout" in name_locator
    assert "timeout_for_event" in name_locator
    assert "event" in name_locator
    assert name_locator["attribute"] == "innerHTML"
    assert name_locator["by"] == "css selector"
    assert name_locator["selector"] == "h1.d-inline-block"
    assert name_locator["event"] is None
    assert isinstance(name_locator["timeout"], int)
    assert name_locator["timeout_for_event"] == "presence_of_element_located"


def test_product_summary_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.summary_locator."""
    summary_locator = morlevi_locators_data.get("product", {}).get("summary_locator")
    assert summary_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in summary_locator
    assert "attribute" in summary_locator
    assert "by" in summary_locator
    assert "selector" in summary_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in summary_locator
    assert "timeout" in summary_locator
    assert "timeout_for_event" in summary_locator
    assert "event" in summary_locator
    assert summary_locator["attribute"] == "innerHTML"
    assert summary_locator["by"] == "css selector"
    assert summary_locator["selector"] == "h1.d-inline-block"
    assert summary_locator["event"] is None
    assert isinstance(summary_locator["timeout"], int)
    assert summary_locator["timeout_for_event"] == "presence_of_element_located"

def test_product_description_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.description_locator."""
    description_locator = morlevi_locators_data.get("product", {}).get("description_locator")
    assert description_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in description_locator
    assert "attribute" in description_locator
    assert "by" in description_locator
    assert "selector" in description_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in description_locator
    assert "timeout" in description_locator
    assert "timeout_for_event" in description_locator
    assert "event" in description_locator
    assert description_locator["attribute"] == "innerHTML"
    assert description_locator["by"] == "css selector"
    assert description_locator["selector"] == ".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5"
    assert description_locator["event"] is None
    assert isinstance(description_locator["timeout"], int)
    assert description_locator["timeout_for_event"] == "presence_of_element_located"


def test_product_price_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.price_locator."""
    price_locator = morlevi_locators_data.get("product", {}).get("price_locator")
    assert price_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in price_locator
    assert "attribute" in price_locator
    assert "by" in price_locator
    assert "selector" in price_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in price_locator
    assert "timeout" in price_locator
    assert "timeout_for_event" in price_locator
    assert "event" in price_locator
    assert price_locator["attribute"] == "innerHTML"
    assert price_locator["by"] == "ID"
    assert price_locator["selector"] == "basicPrice"
    assert price_locator["event"] is None
    assert isinstance(price_locator["timeout"], int)
    assert price_locator["timeout_for_event"] == "presence_of_element_located"

def test_product_brand_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.brand_locator."""
    brand_locator = morlevi_locators_data.get("product", {}).get("brand_locator")
    assert brand_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in brand_locator
    assert "attribute" in brand_locator
    assert "by" in brand_locator
    assert "selector" in brand_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in brand_locator
    assert "timeout" in brand_locator
    assert "timeout_for_event" in brand_locator
    assert "event" in brand_locator
    assert brand_locator["attribute"] == "innerHTML"
    assert brand_locator["by"] == "css selector"
    assert brand_locator["selector"] == "text*='éöøï'"
    assert brand_locator["event"] is None
    assert isinstance(brand_locator["timeout"], int)
    assert brand_locator["timeout_for_event"] == "presence_of_element_located"


def test_product_sku_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.sku_locator."""
    sku_locator = morlevi_locators_data.get("product", {}).get("sku_locator")
    assert sku_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in sku_locator
    assert "attribute" in sku_locator
    assert "by" in sku_locator
    assert "selector" in sku_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in sku_locator
    assert "timeout" in sku_locator
    assert "timeout_for_event" in sku_locator
    assert "event" in sku_locator
    assert sku_locator["attribute"] == "innerText"
    assert sku_locator["by"] == "XPATH"
    assert sku_locator["selector"] == "//div[contains(@class,'main-details')]//span[contains(@class,'sku-copy')]"
    assert sku_locator["event"] is None
    assert isinstance(sku_locator["timeout"], int)
    assert sku_locator["timeout_for_event"] == "presence_of_element_located"

def test_product_brand_sku_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.brand_sku_locator."""
    brand_sku_locator = morlevi_locators_data.get("product", {}).get("brand_sku_locator")
    assert brand_sku_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in brand_sku_locator
    assert "attribute" in brand_sku_locator
    assert "by" in brand_sku_locator
    assert "selector" in brand_sku_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in brand_sku_locator
    assert "timeout" in brand_sku_locator
    assert "timeout_for_event" in brand_sku_locator
    assert "event" in brand_sku_locator
    assert brand_sku_locator["attribute"] == "innerHTML"
    assert brand_sku_locator["by"] == "css selector"
    assert brand_sku_locator["selector"] == "span.sku-copy"
    assert brand_sku_locator["event"] is None
    assert isinstance(brand_sku_locator["timeout"], int)
    assert brand_sku_locator["timeout_for_event"] == "presence_of_element_located"

def test_product_main_image_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.main_image_locator."""
    main_image_locator = morlevi_locators_data.get("product", {}).get("main_image_locator")
    assert main_image_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in main_image_locator
    assert "attribute" in main_image_locator
    assert "by" in main_image_locator
    assert "selector" in main_image_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in main_image_locator
    assert "timeout" in main_image_locator
    assert "timeout_for_event" in main_image_locator
    assert "event" in main_image_locator
    assert main_image_locator["attribute"] == "href"
    assert main_image_locator["by"] == "ID"
    assert main_image_locator["selector"] == "mainpic"
    assert main_image_locator["event"] is None
    assert isinstance(main_image_locator["timeout"], int)
    assert main_image_locator["timeout_for_event"] == "presence_of_element_located"

def test_product_li_locator_valid(morlevi_locators_data):
    """Checks the structure and values of product.li_locator."""
    li_locator = morlevi_locators_data.get("product", {}).get("li_locator")
    assert li_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in li_locator
    assert "attribute" in li_locator
    assert "by" in li_locator
    assert "selector" in li_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in li_locator
    assert "timeout" in li_locator
    assert "timeout_for_event" in li_locator
    assert "event" in li_locator
    assert li_locator["attribute"] == "innerHTML"
    assert li_locator["by"] == "tag name"
    assert li_locator["selector"] == "li"
    assert li_locator["event"] is None
    assert isinstance(li_locator["timeout"], int)
    assert li_locator["timeout_for_event"] == "presence_of_element_located"


# Test cases for 'laptop_description_fields_selectors'
def test_laptop_description_fields_selectors_screen_valid(morlevi_locators_data):
    """Checks the structure and values of laptop_description_fields_selectors.screen."""
    screen_locator = morlevi_locators_data.get("laptop_description_fields_selectors", {}).get("screen")
    assert screen_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in screen_locator
    assert "attribute" in screen_locator
    assert "by" in screen_locator
    assert "selector" in screen_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in screen_locator
    assert "timeout" in screen_locator
    assert "timeout_for_event" in screen_locator
    assert "event" in screen_locator
    assert screen_locator["attribute"] == "innerHTML"
    assert screen_locator["by"] == "css selector"
    assert screen_locator["selector"] == "text*='âåãì îñê'"
    assert screen_locator["event"] is None
    assert isinstance(screen_locator["timeout"], int)
    assert screen_locator["timeout_for_event"] == "presence_of_element_located"


def test_laptop_description_fields_selectors_CPUTYPE_valid(morlevi_locators_data):
    """Checks the structure and values of laptop_description_fields_selectors.CPUTYPE."""
    cputype_locator = morlevi_locators_data.get("laptop_description_fields_selectors", {}).get("CPUTYPE")
    assert cputype_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in cputype_locator
    assert "attribute" in cputype_locator
    assert "by" in cputype_locator
    assert "selector" in cputype_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in cputype_locator
    assert "timeout" in cputype_locator
    assert "timeout_for_event" in cputype_locator
    assert "event" in cputype_locator
    assert cputype_locator["attribute"] == "innerHTML"
    assert cputype_locator["by"] == "css selector"
    assert cputype_locator["selector"] == "text*='CPUTYPE'"
    assert cputype_locator["event"] is None
    assert isinstance(cputype_locator["timeout"], int)
    assert cputype_locator["timeout_for_event"] == "presence_of_element_located"


def test_laptop_description_fields_selectors_cpu_valid(morlevi_locators_data):
    """Checks the structure and values of laptop_description_fields_selectors.cpu."""
    cpu_locator = morlevi_locators_data.get("laptop_description_fields_selectors", {}).get("cpu")
    assert cpu_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in cpu_locator
    assert "attribute" in cpu_locator
    assert "by" in cpu_locator
    assert "selector" in cpu_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in cpu_locator
    assert "timeout" in cpu_locator
    assert "timeout_for_event" in cpu_locator
    assert "event" in cpu_locator
    assert cpu_locator["attribute"] == "innerHTML"
    assert cpu_locator["by"] == "css selector"
    assert cpu_locator["selector"] == "text='îòáã'"
    assert cpu_locator["event"] is None
    assert isinstance(cpu_locator["timeout"], int)
    assert cpu_locator["timeout_for_event"] == "presence_of_element_located"

# Test case for stock_locator
def test_stock_locator_valid(morlevi_locators_data):
    """Checks the structure and values of stock_locator."""
    stock_locator = morlevi_locators_data.get("stock_locator")
    assert stock_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in stock_locator
    assert "attribute" in stock_locator
    assert "by" in stock_locator
    assert "selector" in stock_locator
    assert "logic for action[AND|OR|XOR|VALUE|null]" in stock_locator
    assert "timeout" in stock_locator
    assert "timeout_for_event" in stock_locator
    assert "event" in stock_locator
    assert stock_locator["attribute"] == "innerHTML"
    assert stock_locator["by"] == "css selector"
    assert stock_locator["selector"] == ".stockMsg"
    assert stock_locator["event"] is None
    assert isinstance(stock_locator["timeout"], int)
    assert stock_locator["timeout_for_event"] == "presence_of_element_located"

# Test cases for 'login'
def test_login_open_login_dialog_locator_valid(morlevi_locators_data):
    """Checks the structure and values of login.open_login_dialog_locator."""
    open_login_locator = morlevi_locators_data.get("login", {}).get("open_login_dialog_locator")
    assert open_login_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in open_login_locator
    assert "attribute" in open_login_locator
    assert "by" in open_login_locator
    assert "selector" in open_login_locator
    assert "timeout" in open_login_locator
    assert "timeout_for_event" in open_login_locator
    assert "event" in open_login_locator
    assert open_login_locator["by"] == "XPATH"
    assert open_login_locator["selector"] == "//a[contains(@data-modal,'User')]"
    assert isinstance(open_login_locator["timeout"], int)
    assert open_login_locator["timeout_for_event"] == "presence_of_element_located"
    assert open_login_locator["event"] == "click()"

def test_login_email_valid(morlevi_locators_data):
    """Checks if login email exists and is a string."""
    login_email = morlevi_locators_data.get("login", {}).get("email")
    assert login_email is not None
    assert isinstance(login_email, str)

def test_login_email_locator_valid(morlevi_locators_data):
    """Checks the structure and values of login.email_locator."""
    email_locator = morlevi_locators_data.get("login", {}).get("email_locator")
    assert email_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in email_locator
    assert "attribute" in email_locator
    assert "by" in email_locator
    assert "selector" in email_locator
    assert "timeout" in email_locator
    assert "timeout_for_event" in email_locator
    assert "event" in email_locator
    assert email_locator["by"] == "ID"
    assert email_locator["selector"] == "Email"
    assert isinstance(email_locator["timeout"], int)
    assert email_locator["timeout_for_event"] == "presence_of_element_located"
    assert email_locator["event"] == "send_keys('sales@aluf.co.il')"

def test_login_password_valid(morlevi_locators_data):
    """Checks if login password exists and is a string."""
    login_password = morlevi_locators_data.get("login", {}).get("password")
    assert login_password is not None
    assert isinstance(login_password, str)

def test_login_password_locator_valid(morlevi_locators_data):
    """Checks the structure and values of login.password_locator."""
    password_locator = morlevi_locators_data.get("login", {}).get("password_locator")
    assert password_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in password_locator
    assert "attribute" in password_locator
    assert "by" in password_locator
    assert "selector" in password_locator
    assert "timeout" in password_locator
    assert "timeout_for_event" in password_locator
    assert "event" in password_locator
    assert password_locator["by"] == "ID"
    assert password_locator["selector"] == "Password"
    assert isinstance(password_locator["timeout"], int)
    assert password_locator["timeout_for_event"] == "presence_of_element_located"
    assert password_locator["event"] == "send_keys('9643766')"

def test_login_loginbutton_locator_valid(morlevi_locators_data):
    """Checks the structure and values of login.loginbutton_locator."""
    loginbutton_locator = morlevi_locators_data.get("login", {}).get("loginbutton_locator")
    assert loginbutton_locator is not None
    assert "logic for attribue[AND|OR|XOR|VALUE|null]" in loginbutton_locator
    assert "attribute" in loginbutton_locator
    assert "by" in loginbutton_locator
    assert "selector" in loginbutton_locator
    assert "timeout" in loginbutton_locator
    assert "timeout_for_event" in loginbutton_locator
    assert "event" in loginbutton_locator
    assert loginbutton_locator["by"] == "css selector"
    assert loginbutton_locator["selector"] == ".btn.btn-primary.btn-lg.w-50.float-left.mr-2"
    assert isinstance(loginbutton_locator["timeout"], int)
    assert loginbutton_locator["timeout_for_event"] == "presence_of_element_located"
    assert loginbutton_locator["event"] == "click()"
```