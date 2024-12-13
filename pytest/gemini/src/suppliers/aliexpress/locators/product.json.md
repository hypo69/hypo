```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def product_locators():
    """Provides the product locator data from the JSON file."""
    with open('hypotez/src/suppliers/aliexpress/locators/product.json', 'r') as f:
        return json.load(f)

# Test for the 'close_banner' locator
def test_close_banner_locator(product_locators):
    """Tests the 'close_banner' locator configuration."""
    close_banner = product_locators.get("close_banner")
    assert close_banner is not None
    assert close_banner["attribute"] is None
    assert close_banner["by"] == "XPATH"
    assert close_banner["selector"] == "//button[@id = 'closeXButton']"
    assert close_banner["if_list"] == "first"
    assert close_banner["use_mouse"] is False
    assert close_banner["mandatory"] is False
    assert close_banner["timeout"] == 0
    assert close_banner["timeout_for_event"] == "presence_of_element_located"
    assert close_banner["event"] == "click()"
    assert close_banner["locator_description"] == "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"

# Test for the 'id' locator
def test_id_locator(product_locators):
    """Tests the 'id' locator configuration."""
    id_locator = product_locators.get("id")
    assert id_locator is not None
    assert id_locator["attribute"] is None
    assert id_locator["by"] is None
    assert id_locator["selector"] is None
    assert id_locator["if_list"] == "first"
    assert id_locator["use_mouse"] is False
    assert id_locator["mandatory"] is False
    assert id_locator["timeout"] == 0
    assert id_locator["timeout_for_event"] == "presence_of_element_located"
    assert id_locator["event"] is None
    assert id_locator["locator_description"] == "id"

# Test for the 'id_manufacturer' locator
def test_id_manufacturer_locator(product_locators):
    """Tests the 'id_manufacturer' locator configuration."""
    id_manufacturer = product_locators.get("id_manufacturer")
    assert id_manufacturer is not None
    assert id_manufacturer["attribute"] == 11290
    assert id_manufacturer["by"] == "VALUE"
    assert id_manufacturer["selector"] is None
    assert id_manufacturer["if_list"] == "first"
    assert id_manufacturer["use_mouse"] is False
    assert id_manufacturer["mandatory"] is True
    assert id_manufacturer["timeout"] == 0
    assert id_manufacturer["timeout_for_event"] == "presence_of_element_located"
    assert id_manufacturer["event"] is None
    assert id_manufacturer["locator_description"] == "id_manufacturer"

# Test for the 'id_supplier' locator
def test_id_supplier_locator(product_locators):
    """Tests the 'id_supplier' locator configuration."""
    id_supplier = product_locators.get("id_supplier")
    assert id_supplier is not None
    assert id_supplier["attribute"] == 11267
    assert id_supplier["by"] == "VALUE"
    assert id_supplier["selector"] is None
    assert id_supplier["if_list"] == "first"
    assert id_supplier["use_mouse"] is False
    assert id_supplier["mandatory"] is True
    assert id_supplier["timeout"] == 0
    assert id_supplier["timeout_for_event"] == "presence_of_element_located"
    assert id_supplier["event"] is None
    assert id_supplier["locator_description"] == "id_supplier"


# Test for the 'condition' locator
def test_condition_locator(product_locators):
    """Tests the 'condition' locator configuration."""
    condition = product_locators.get("condition")
    assert condition is not None
    assert condition["attribute"] == "new"
    assert condition["by"] == "VALUE"
    assert condition["selector"] is None
    assert condition["if_list"] == "first"
    assert condition["use_mouse"] is False
    assert condition["mandatory"] is True
    assert condition["timeout"] == 0
    assert condition["timeout_for_event"] == "presence_of_element_located"
    assert condition["event"] is None
    assert condition["locator_description"] == "condition"

# Test for the 'default_image_url' locator
def test_default_image_url_locator(product_locators):
    """Tests the 'default_image_url' locator configuration."""
    default_image_url = product_locators.get("default_image_url")
    assert default_image_url is not None
    assert default_image_url["attribute"] == "src"
    assert default_image_url["by"] == "XPATH"
    assert default_image_url["selector"] == "//img[contains(@class, 'zoomImg')]"
    assert default_image_url["if_list"] == "first"
    assert default_image_url["use_mouse"] is False
    assert default_image_url["mandatory"] is False
    assert default_image_url["timeout"] == 0
    assert default_image_url["timeout_for_event"] == "presence_of_element_located"
    assert default_image_url["event"] is None
    assert default_image_url["locator_description"] == "default_image_url"


# Test for the 'product_reference_and_volume_and_price_for_100' locator
def test_product_reference_locator(product_locators):
    """Tests the 'product_reference_and_volume_and_price_for_100' locator configuration."""
    product_reference = product_locators.get("product_reference_and_volume_and_price_for_100")
    assert product_reference is not None
    assert product_reference["attribute"] is None
    assert product_reference["by"] == "XPATH"
    assert product_reference["selector"] == "//div[@data-widget_type='shortcode.default']"
    assert product_reference["if_list"] == "first"
    assert product_reference["use_mouse"] is False
    assert product_reference["mandatory"] is True
    assert product_reference["timeout"] == 0
    assert product_reference["timeout_for_event"] == "presence_of_element_located"
    assert product_reference["event"] is None
    assert product_reference["locator_description"] == "На сайте кривой HTML, поэтому одним локатором вытескиваю 3 значения, а потом делаю парсинг. Приходит список из четырех объектов: объем, цена за 100 гр, артикул, пустой div"

# Test for the 'additional_images_urls' locator
def test_additional_images_urls_locator(product_locators):
    """Tests the 'additional_images_urls' locator configuration."""
    additional_images_urls = product_locators.get("additional_images_urls")
    assert additional_images_urls is not None
    assert additional_images_urls["attribute"] == "src"
    assert additional_images_urls["by"] == "XPATH"
    assert additional_images_urls["selector"] == "//ol[contains(@class, 'flex-control-thumbs')]//img"
    assert additional_images_urls["if_list"] == "first"
    assert additional_images_urls["use_mouse"] is False
    assert additional_images_urls["mandatory"] is False
    assert additional_images_urls["timeout"] == 0
    assert additional_images_urls["timeout_for_event"] == "presence_of_element_located"
    assert additional_images_urls["event"] is None

def test_out_of_stock_locator(product_locators):
    """Tests the 'out_of_stock' locator configuration."""
    out_of_stock = product_locators.get("out_of_stock")
    assert out_of_stock is not None
    assert out_of_stock["attribute"] is None
    assert out_of_stock["by"] == "XPATH"
    assert out_of_stock["selector"] == "//p[contains(@class, 'out-of-stock')]"
    assert out_of_stock["if_list"] == "first"
    assert out_of_stock["use_mouse"] is False
    assert out_of_stock["mandatory"] is True
    assert out_of_stock["timeout"] == 0
    assert out_of_stock["timeout_for_event"] == "presence_of_element_located"
    assert out_of_stock["event"] is None
    assert out_of_stock["locator_description"] == "out_of_stock"

def test_delivery_in_stock_locator(product_locators):
    """Tests the 'delivery_in_stock' locator configuration."""
    delivery_in_stock = product_locators.get("delivery_in_stock")
    assert delivery_in_stock is not None
    assert delivery_in_stock["attribute"] == "Israel Post"
    assert delivery_in_stock["by"] == "VALUE"
    assert delivery_in_stock["selector"] is None
    assert delivery_in_stock["if_list"] == "first"
    assert delivery_in_stock["use_mouse"] is False
    assert delivery_in_stock["mandatory"] is False
    assert delivery_in_stock["timeout"] == 0
    assert delivery_in_stock["timeout_for_event"] == "presence_of_element_located"
    assert delivery_in_stock["event"] is None
    assert delivery_in_stock["locator_description"] == "delivery_in_stock (Israel Post)"


def test_on_sale_locator(product_locators):
    """Tests the 'on_sale' locator configuration."""
    on_sale = product_locators.get("on_sale")
    assert on_sale is not None
    assert on_sale["attribute"] == 0
    assert on_sale["by"] == "VALUE"
    assert on_sale["selector"] is None
    assert on_sale["if_list"] == "first"
    assert on_sale["use_mouse"] is False
    assert on_sale["mandatory"] is False
    assert on_sale["timeout"] == 0
    assert on_sale["timeout_for_event"] == "presence_of_element_located"
    assert on_sale["event"] is None
    assert on_sale["locator_description"] == "on_sale"

def test_online_only_locator(product_locators):
    """Tests the 'online_only' locator configuration."""
    online_only = product_locators.get("online_only")
    assert online_only is not None
    assert online_only["attribute"] == 1
    assert online_only["by"] == "VALUE"
    assert online_only["selector"] is None
    assert online_only["if_list"] == "first"
    assert online_only["use_mouse"] is False
    assert online_only["mandatory"] is False
    assert online_only["timeout"] == 0
    assert online_only["timeout_for_event"] == "presence_of_element_located"
    assert online_only["event"] is None
    assert online_only["locator_description"] == "online_only"

def test_minimal_quantity_locator(product_locators):
    """Tests the 'minimal_quantity' locator configuration."""
    minimal_quantity = product_locators.get("minimal_quantity")
    assert minimal_quantity is not None
    assert minimal_quantity["attribute"] == 1
    assert minimal_quantity["by"] == "VALUE"
    assert minimal_quantity["selector"] is None
    assert minimal_quantity["if_list"] == "first"
    assert minimal_quantity["use_mouse"] is False
    assert minimal_quantity["mandatory"] is False
    assert minimal_quantity["timeout"] == 0
    assert minimal_quantity["timeout_for_event"] == "presence_of_element_located"
    assert minimal_quantity["event"] is None
    assert minimal_quantity["locator_description"] == "minimal_quantity"

def test_price_locator(product_locators):
    """Tests the 'price' locator configuration."""
    price = product_locators.get("price")
    assert price is not None
    assert price["attribute"] == "innerText"
    assert price["by"] == "XPATH"
    assert price["selector"] == "//p[@class='price']"
    assert price["if_list"] == "first"
    assert price["use_mouse"] is False
    assert price["mandatory"] is True
    assert price["timeout"] == 0
    assert price["timeout_for_event"] == "presence_of_element_located"
    assert price["event"] is None
    assert price["locator_description"] == "price"

def test_additional_shipping_cost_locator(product_locators):
    """Tests the 'additional_shipping_cost' locator configuration."""
    additional_shipping_cost = product_locators.get("additional_shipping_cost")
    assert additional_shipping_cost is not None
    assert additional_shipping_cost["attribute"] == 30
    assert additional_shipping_cost["by"] == "VALUE"
    assert additional_shipping_cost["selector"] is None
    assert additional_shipping_cost["if_list"] == "first"
    assert additional_shipping_cost["use_mouse"] is False
    assert additional_shipping_cost["mandatory"] is True
    assert additional_shipping_cost["timeout"] == 0
    assert additional_shipping_cost["timeout_for_event"] == "presence_of_element_located"
    assert additional_shipping_cost["event"] is None
    assert additional_shipping_cost["locator_description"] == "Стоимость отправки. 30 шек. by: VALUE означает, что я беру значение из attribute"

def test_affiliate_short_link_locator(product_locators):
    """Tests the 'affiliate_short_link' locator configuration."""
    affiliate_short_link = product_locators.get("affiliate_short_link")
    assert affiliate_short_link is not None
    assert affiliate_short_link["attribute"] == "$_(driver.current_url)_$"
    assert affiliate_short_link["by"] == "VALUE"
    assert affiliate_short_link["selector"] is None
    assert affiliate_short_link["if_list"] == "first"
    assert affiliate_short_link["use_mouse"] is False
    assert affiliate_short_link["mandatory"] is True
    assert affiliate_short_link["timeout"] == 0
    assert affiliate_short_link["timeout_for_event"] == "presence_of_element_located"
    assert affiliate_short_link["event"] is None
    assert affiliate_short_link["locator_description"] == "Исполняю формулу и отдаю результат через `value`"

def test_name_locator(product_locators):
    """Tests the 'name' locator configuration."""
    name = product_locators.get("name")
    assert name is not None
    assert name["attribute"] == "innerText"
    assert name["by"] == "XPATH"
    assert name["selector"] == "//h1[contains(@class,'product_title')]"
    assert name["if_list"] == "first"
    assert name["use_mouse"] is False
    assert name["mandatory"] is True
    assert name["timeout"] == 0
    assert name["timeout_for_event"] == "presence_of_element_located"
    assert name["event"] is None
    assert name["locator_description"] == "name"

def test_description_locator(product_locators):
    """Tests the 'description' locator configuration."""
    description = product_locators.get("description")
    assert description is not None
    assert description["attribute"] == [None, None]
    assert description["by"] == ["XPATH", "XPATH"]
    assert description["selector"] == ["//a[contains(@href, '#tab-description')]", "//div[@id = 'tab-description']//p"]
    assert description["if_list"] == "first"
    assert description["use_mouse"] == [False, False]
    assert description["mandatory"] == [True, True]
    assert description["timeout"] == 0
    assert description["timeout_for_event"] == "presence_of_element_located"
    assert description["event"] == ["click()", None]
    assert description["locator_description"] == ["Нажимаю на таб для отркытия поля description", "читаю данные из div"]

def test_ingredients_locator(product_locators):
    """Tests the 'ingredients' locator configuration."""
    ingredients = product_locators.get("ingredients")
    assert ingredients is not None
    assert ingredients["attribute"] == [None, None]
    assert ingredients["by"] == ["XPATH", "XPATH"]
    assert ingredients["selector"] == ["//a[contains(@href, 'מרכיבים')]", "//div[contains(@id ,'מרכיבים')]"]
    assert ingredients["if_list"] == "first"
    assert ingredients["use_mouse"] == [False, False]
    assert ingredients["mandatory"] == [True, True]
    assert ingredients["timeout"] == 0
    assert ingredients["timeout_for_event"] == "presence_of_element_located"
    assert ingredients["event"] == ["click()", None]
    assert ingredients["locator_description"] == "ingredients"

def test_how_to_use_locator(product_locators):
    """Tests the 'how_to_use' locator configuration."""
    how_to_use = product_locators.get("how_to_use")
    assert how_to_use is not None
    assert how_to_use["attribute"] == [None, None]
    assert how_to_use["by"] == ["XPATH", "XPATH"]
    assert how_to_use["selector"] == ["//a[contains(@href, 'אופן-השימוש')]", "//div[contains(@id ,'אופן-השימוש')]//p"]
    assert how_to_use["if_list"] == "first"
    assert how_to_use["use_mouse"] == [False, False]
    assert how_to_use["mandatory"] == [True, True]
    assert how_to_use["timeout"] == 0
    assert how_to_use["timeout_for_event"] == "presence_of_element_located"
    assert how_to_use["event"] == ["click()", None]
    assert how_to_use["locator_description"] == "how_to_use"


def test_specification_locator(product_locators):
    """Tests the 'specification' locator configuration."""
    specification = product_locators.get("specification")
    assert specification is not None
    assert specification["attribute"] == "innerText"
    assert specification["by"] == "XPATH"
    assert specification["selector"] == "//div[contains(@class, 'product-params')]//li"
    assert specification["if_list"] == "all"
    assert specification["use_mouse"] is False
    assert specification["mandatory"] is True
    assert specification["timeout"] == 0
    assert specification["timeout_for_event"] == "presence_of_element_located"
    assert specification["event"] is None
    assert specification["locator_description"] == "Технические характеристики. "

def test_visibility_locator(product_locators):
    """Tests the 'visibility' locator configuration."""
    visibility = product_locators.get("visibility")
    assert visibility is not None
    assert visibility["attribute"] == "both"
    assert visibility["by"] == "VALUE"
    assert visibility["selector"] is None
    assert visibility["if_list"] == "first"
    assert visibility["use_mouse"] is False
    assert visibility["mandatory"] is True
    assert visibility["timeout"] == 0
    assert visibility["timeout_for_event"] == "presence_of_element_located"
    assert visibility["event"] is None
    assert visibility["locator_description"] == "visibility"

def test_brand_locator(product_locators):
    """Tests the 'brand' locator configuration."""
    brand = product_locators.get("Brand")
    assert brand is not None
    assert brand["attribute"] == "hb"
    assert brand["by"] == "VALUE"
    assert brand["selector"] is None
    assert brand["if_list"] == "first"
    assert brand["use_mouse"] is False
    assert brand["mandatory"] is True
    assert brand["timeout"] == 0
    assert brand["timeout_for_event"] == "presence_of_element_located"
    assert brand["event"] is None
    assert brand["locator_description"] == "@deprecated Brand -  Поле используется при ручном импорте csv"

def test_condition_locator_2(product_locators):
    """Tests the 'Condition' locator configuration."""
    condition = product_locators.get("Condition")
    assert condition is not None
    assert condition["attribute"] == "new"
    assert condition["by"] == "VALUE"
    assert condition["selector"] is None
    assert condition["if_list"] == "first"
    assert condition["use_mouse"] is False
    assert condition["mandatory"] is True
    assert condition["timeout"] == 0
    assert condition["timeout_for_event"] == "presence_of_element_located"
    assert condition["event"] is None


def test_virtual_product_locator(product_locators):
        """Tests the 'Virtual product (0 = No, 1 = Yes)' locator configuration."""
        virtual_product = product_locators.get("Virtual product (0 = No, 1 = Yes)")
        assert virtual_product is not None
        assert virtual_product["attribute"] == 0
        assert virtual_product["by"] == "VALUE"
        assert virtual_product["selector"] is None
        assert virtual_product["if_list"] == "first"
        assert virtual_product["use_mouse"] is False
        assert virtual_product["mandatory"] is True
        assert virtual_product["timeout"] == 0
        assert virtual_product["timeout_for_event"] == "presence_of_element_located"
        assert virtual_product["event"] is None

# Test for mandatory fields
def test_mandatory_fields(product_locators):
    """Test to ensure that all mandatory fields are correctly marked."""
    mandatory_count = 0
    for locator_name, locator_data in product_locators.items():
        if locator_data.get("mandatory", False) is True:
             mandatory_count += 1
    assert mandatory_count > 0, "No mandatory fields were found, which is unusual"

# Test for 'available_for_order' locator
def test_available_for_order_locator(product_locators):
    """Tests the 'available_for_order' locator configuration."""
    available_for_order = product_locators.get("available_for_order")
    assert available_for_order is not None
    assert available_for_order["attribute"] is None
    assert available_for_order["by"] == "XPATH"
    assert available_for_order["selector"] == "//p[contains(@class, 'out-of-stock')]"
    assert available_for_order["if_list"] == "first"
    assert available_for_order["use_mouse"] is False
    assert available_for_order["mandatory"] is False
    assert available_for_order["timeout"] == 0
    assert available_for_order["timeout_for_event"] == "presence_of_element_located"
    assert available_for_order["event"] is None
    assert available_for_order["locator_description"] == "available_for_order - Если вернулся не пустой локатор - флаг выставляется в 1, иначе 0. Текст на сайте עזל ממלאי"

def test_show_price_locator(product_locators):
    """Tests the 'show_price' locator configuration."""
    show_price = product_locators.get("show_price")
    assert show_price is not None
    assert show_price["attribute"] == 1
    assert show_price["by"] == "VALUE"
    assert show_price["selector"] is None
    assert show_price["if_list"] == "first"
    assert show_price["use_mouse"] is False
    assert show_price["mandatory"] is False
    assert show_price["timeout"] == 0
    assert show_price["timeout_for_event"] == "presence_of_element_located"
    assert show_price["event"] is None
    assert show_price["locator_description"] == "show_price"
```