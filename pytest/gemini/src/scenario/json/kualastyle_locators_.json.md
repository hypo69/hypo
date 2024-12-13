```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def kualastyle_locators():
    """Loads the kualastyle_locators.json data."""
    json_data = """
{
  "infinity_scroll": false,
  "checkboxes_for_categories": false,
  "main menu": {
    "categories parent": {
      
      "attribute": "innerText",
      "by": "XPATH",
      "selector": "//nav[@class,'site-navigation']//li[contains(@class,'navmenu-item-parent')][{x}]//details//summary",
      "if_list":"first","use_mouse": false, "mandatory": true,
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loop",
      
      "variables in selector": "x",
      "formula for locator": "range(1,6)"
    },
    "categories sub menu": {
      
      "attribute": "{'innerText':'href'}",
      "by": "XPATH",
      "selector": "//nav[@class,'site-navigation']//li[contains(@class,'navmenu-item-parent')][{x}]//div[contains(@class,'navmenu-submenu')]//li//a",
      "if_list":"first","use_mouse": false, "mandatory": true,
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
      "logic for action[AND|OR|XOR|VALUE|null]": null

    },
    "a": {
      
      "attribute": null,
      "by": "XPATH",
      "selector": "//ul[@class='pagination']//a[@class='page-link']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
    }
  },

  "store": {
    "store categories dept-1": {
      "description": "Список главных категероий магазина",
      
      "attribute": {
        "innerText": "href"
      },
      "by": "XPATH",
      "selector": "//nav[@class='site-navigation'],//ul[contains(@class,'navmenu-depth-1')]/li",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "store categories dept-2": {
      "description": "Список подкатегероий магазина",
      
      "attribute": {
        "innerText": "href"
      },
      "by": "XPATH",
      "selector": "//nav[@class='site-navigation'],//ul[contains(@class,'navmenu-depth-1')]/li//ul[contains(@class,'navmenu-depth-2')]/li",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "store categories dept-3": {
      "description": "Список подкатегероий магазина",
      
      "attribute": {
        "innerText": "href"
      },
      "by": "XPATH",
      "selector": "//nav[@class='site-navigation'],//ul[contains(@class,'navmenu-depth-1')]/li//ul[contains(@class,'navmenu-depth-2')]/li//ul[contains(@class,'navmenu-depth-3')]/li",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    }
  },

  "product": {
    "link_to_product_locator": {
      
      "attribute": "href",
      "by": "XPATH",
      "selector": "//div[@class = 'product-thumb']/a",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "stock available": {
      
      "attribute": "innerText",
      "by": "XPATH",
      "selector": "//div[conatins(@class , 'stockMsg')]",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },

    "product_name_locator": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "h1.d-inline-block",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "summary_locator": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "h1.d-inline-block",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "description_locator": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": ".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },

    "price_locator": {
      
      "attribute": "innerHTML",
      "by": "ID",
      "selector": "basicPrice",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },

    "brand_locator": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text*='éöøï'",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },

    "sku_locator": {
      
      "attribute": "innerText",
      "by": "XPATH",
      "selector": "//div[contains(@class,'main-details')]//span[contains(@class,'sku-copy')]",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "brand_sku_locator": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "span.sku-copy",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },

    "main_image_locator": {
      
      "attribute": "href",
      "by": "ID",
      "selector": "mainpic",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },

    "li_locator": {
      
      "attribute": "innerHTML",
      "by": "tag name",
      "selector": "li",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    }
  },
  "product_fields_locators": {

  },
  "laptop_description_fields_selectors": {
    "screen": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text*='âåãì îñê'",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "CPUTYPE": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text*='CPUTYPE'",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    },
    "cpu": {
      
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text='îòáã'",
      
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
    }
  },
  "stock_locator": {
    
    "attribute": "innerHTML",
    "by": "css selector",
    "selector": ".stockMsg",
    
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null

  },
  "login": {

    "open_login_dialog_locator": {
      
      "attribute": null,
      "by": "XPATH",
      "selector": "//a[contains(@data-modal,'User')]",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
    },

    "email": "sales@aluf.co.il",
    "email_locator": {
      
      "attribute": null,
      "by": "ID",
      "selector": "Email",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "send_keys('sales@aluf.co.il')"

    },
    "password": "9643766",
    "password_locator": {
      
      "attribute": null,
      "by": "ID",
      "selector": "Password",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "send_keys('9643766')"

    },
    "loginbutton_locator": {
      
      "attribute": null,
      "by": "css selector",
      "selector": ".btn.btn-primary.btn-lg.w-50.float-left.mr-2",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"

    }
  }
}
"""
    return json.loads(json_data)


# Tests for the "main menu" section
def test_main_menu_categories_parent_valid(kualastyle_locators):
    """Checks the 'categories parent' locator with valid data."""
    locator = kualastyle_locators["main menu"]["categories parent"]
    assert locator["attribute"] == "innerText"
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//nav[@class,'site-navigation']//li[contains(@class,'navmenu-item-parent')][{x}]//details//summary"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "loop"
    assert locator["variables in selector"] == "x"
    assert locator["formula for locator"] == "range(1,6)"

def test_main_menu_categories_sub_menu_valid(kualastyle_locators):
    """Checks the 'categories sub menu' locator with valid data."""
    locator = kualastyle_locators["main menu"]["categories sub menu"]
    assert locator["attribute"] == "{'innerText':'href'}"
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//nav[@class,'site-navigation']//li[contains(@class,'navmenu-item-parent')][{x}]//div[contains(@class,'navmenu-submenu')]//li//a"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["mandatory"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["logic for action[AND|OR|XOR|VALUE|null]"] is None

def test_main_menu_a_valid(kualastyle_locators):
    """Checks the 'a' locator within main menu with valid data."""
    locator = kualastyle_locators["main menu"]["a"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//ul[@class='pagination']//a[@class='page-link']"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    

# Tests for the "store" section
def test_store_categories_dept_1_valid(kualastyle_locators):
     """Checks the 'store categories dept-1' locator with valid data."""
     locator = kualastyle_locators["store"]["store categories dept-1"]
     assert locator["description"] == "Список главных категероий магазина"
     assert locator["attribute"] == {"innerText": "href"}
     assert locator["by"] == "XPATH"
     assert locator["selector"] == "//nav[@class='site-navigation'],//ul[contains(@class,'navmenu-depth-1')]/li"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_store_categories_dept_2_valid(kualastyle_locators):
     """Checks the 'store categories dept-2' locator with valid data."""
     locator = kualastyle_locators["store"]["store categories dept-2"]
     assert locator["description"] == "Список подкатегероий магазина"
     assert locator["attribute"] == {"innerText": "href"}
     assert locator["by"] == "XPATH"
     assert locator["selector"] == "//nav[@class='site-navigation'],//ul[contains(@class,'navmenu-depth-1')]/li//ul[contains(@class,'navmenu-depth-2')]/li"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_store_categories_dept_3_valid(kualastyle_locators):
     """Checks the 'store categories dept-3' locator with valid data."""
     locator = kualastyle_locators["store"]["store categories dept-3"]
     assert locator["description"] == "Список подкатегероий магазина"
     assert locator["attribute"] == {"innerText": "href"}
     assert locator["by"] == "XPATH"
     assert locator["selector"] == "//nav[@class='site-navigation'],//ul[contains(@class,'navmenu-depth-1')]/li//ul[contains(@class,'navmenu-depth-2')]/li//ul[contains(@class,'navmenu-depth-3')]/li"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

# Tests for the "product" section
def test_product_link_to_product_locator_valid(kualastyle_locators):
    """Checks the 'link_to_product_locator' with valid data."""
    locator = kualastyle_locators["product"]["link_to_product_locator"]
    assert locator["attribute"] == "href"
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@class = 'product-thumb']/a"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

def test_product_stock_available_valid(kualastyle_locators):
     """Checks the 'stock available' locator within product with valid data."""
     locator = kualastyle_locators["product"]["stock available"]
     assert locator["attribute"] == "innerText"
     assert locator["by"] == "XPATH"
     assert locator["selector"] == "//div[conatins(@class , 'stockMsg')]"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None
     
def test_product_product_name_locator_valid(kualastyle_locators):
    """Checks the 'product_name_locator' with valid data."""
    locator = kualastyle_locators["product"]["product_name_locator"]
    assert locator["attribute"] == "innerHTML"
    assert locator["by"] == "css selector"
    assert locator["selector"] == "h1.d-inline-block"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

def test_product_summary_locator_valid(kualastyle_locators):
    """Checks the 'summary_locator' with valid data."""
    locator = kualastyle_locators["product"]["summary_locator"]
    assert locator["attribute"] == "innerHTML"
    assert locator["by"] == "css selector"
    assert locator["selector"] == "h1.d-inline-block"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    
def test_product_description_locator_valid(kualastyle_locators):
    """Checks the 'description_locator' with valid data."""
    locator = kualastyle_locators["product"]["description_locator"]
    assert locator["attribute"] == "innerHTML"
    assert locator["by"] == "css selector"
    assert locator["selector"] == ".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

def test_product_price_locator_valid(kualastyle_locators):
     """Checks the 'price_locator' with valid data."""
     locator = kualastyle_locators["product"]["price_locator"]
     assert locator["attribute"] == "innerHTML"
     assert locator["by"] == "ID"
     assert locator["selector"] == "basicPrice"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_product_brand_locator_valid(kualastyle_locators):
     """Checks the 'brand_locator' with valid data."""
     locator = kualastyle_locators["product"]["brand_locator"]
     assert locator["attribute"] == "innerHTML"
     assert locator["by"] == "css selector"
     assert locator["selector"] == "text*='éöøï'"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_product_sku_locator_valid(kualastyle_locators):
     """Checks the 'sku_locator' with valid data."""
     locator = kualastyle_locators["product"]["sku_locator"]
     assert locator["attribute"] == "innerText"
     assert locator["by"] == "XPATH"
     assert locator["selector"] == "//div[contains(@class,'main-details')]//span[contains(@class,'sku-copy')]"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_product_brand_sku_locator_valid(kualastyle_locators):
     """Checks the 'brand_sku_locator' with valid data."""
     locator = kualastyle_locators["product"]["brand_sku_locator"]
     assert locator["attribute"] == "innerHTML"
     assert locator["by"] == "css selector"
     assert locator["selector"] == "span.sku-copy"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_product_main_image_locator_valid(kualastyle_locators):
    """Checks the 'main_image_locator' with valid data."""
    locator = kualastyle_locators["product"]["main_image_locator"]
    assert locator["attribute"] == "href"
    assert locator["by"] == "ID"
    assert locator["selector"] == "mainpic"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

def test_product_li_locator_valid(kualastyle_locators):
    """Checks the 'li_locator' with valid data."""
    locator = kualastyle_locators["product"]["li_locator"]
    assert locator["attribute"] == "innerHTML"
    assert locator["by"] == "tag name"
    assert locator["selector"] == "li"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None

# Tests for the "laptop_description_fields_selectors" section
def test_laptop_description_screen_valid(kualastyle_locators):
     """Checks the 'screen' locator within laptop_description_fields_selectors with valid data."""
     locator = kualastyle_locators["laptop_description_fields_selectors"]["screen"]
     assert locator["attribute"] == "innerHTML"
     assert locator["by"] == "css selector"
     assert locator["selector"] == "text*='âåãì îñê'"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_laptop_description_cputype_valid(kualastyle_locators):
     """Checks the 'CPUTYPE' locator within laptop_description_fields_selectors with valid data."""
     locator = kualastyle_locators["laptop_description_fields_selectors"]["CPUTYPE"]
     assert locator["attribute"] == "innerHTML"
     assert locator["by"] == "css selector"
     assert locator["selector"] == "text*='CPUTYPE'"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None

def test_laptop_description_cpu_valid(kualastyle_locators):
     """Checks the 'cpu' locator within laptop_description_fields_selectors with valid data."""
     locator = kualastyle_locators["laptop_description_fields_selectors"]["cpu"]
     assert locator["attribute"] == "innerHTML"
     assert locator["by"] == "css selector"
     assert locator["selector"] == "text='îòáã'"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] is None
     

# Tests for the "stock_locator" section
def test_stock_locator_valid(kualastyle_locators):
    """Checks the 'stock_locator' with valid data."""
    locator = kualastyle_locators["stock_locator"]
    assert locator["attribute"] == "innerHTML"
    assert locator["by"] == "css selector"
    assert locator["selector"] == ".stockMsg"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None


# Tests for the "login" section
def test_login_open_login_dialog_locator_valid(kualastyle_locators):
    """Checks the 'open_login_dialog_locator' with valid data."""
    locator = kualastyle_locators["login"]["open_login_dialog_locator"]
    assert locator["attribute"] is None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//a[contains(@data-modal,'User')]"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"

def test_login_email_locator_valid(kualastyle_locators):
     """Checks the 'email_locator' with valid data."""
     locator = kualastyle_locators["login"]["email_locator"]
     assert locator["attribute"] is None
     assert locator["by"] == "ID"
     assert locator["selector"] == "Email"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] == "send_keys('sales@aluf.co.il')"

def test_login_password_locator_valid(kualastyle_locators):
     """Checks the 'password_locator' with valid data."""
     locator = kualastyle_locators["login"]["password_locator"]
     assert locator["attribute"] is None
     assert locator["by"] == "ID"
     assert locator["selector"] == "Password"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] == "send_keys('9643766')"


def test_login_loginbutton_locator_valid(kualastyle_locators):
     """Checks the 'loginbutton_locator' with valid data."""
     locator = kualastyle_locators["login"]["loginbutton_locator"]
     assert locator["attribute"] is None
     assert locator["by"] == "css selector"
     assert locator["selector"] == ".btn.btn-primary.btn-lg.w-50.float-left.mr-2"
     assert locator["timeout"] == 0
     assert locator["timeout_for_event"] == "presence_of_element_located"
     assert locator["event"] == "click()"
```