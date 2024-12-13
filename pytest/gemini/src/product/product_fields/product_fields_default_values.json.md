```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def default_values_data():
    """Loads the default values JSON data."""
    with open("hypotez/src/product/product_fields/product_fields_default_values.json", "r") as f:
        return json.load(f)

def test_default_values_data_is_dict(default_values_data):
    """Checks if the loaded JSON data is a dictionary."""
    assert isinstance(default_values_data, dict), "The loaded JSON data should be a dictionary."


def test_default_values_has_required_keys(default_values_data):
    """Checks if required keys are present in default values dictionary."""
    required_keys = [
        "available_now",
        "available_later",
        "affiliate_short_link",
        "affiliate_text",
        "affiliate_summary",
        "affiliate_summary_2",
        "affiliate_image_large",
        "affiliate_image_medium",
        "affiliate_image_small",
        "active",
        "additional_delivery_times",
        "additional_shipping_cost",
        "advanced_stock_management",
        "associations",
        "available_date",
        "available_for_order",
        "cache_default_attribute",
        "cache_has_attachments",
        "cache_is_pack",
        "condition",
        "customizable",
        "date_add",
        "date_upd",
        "default_image_url",
        "images_urls",
        "delivery_additional_message",
        "delivery_in_stock",
        "delivery_out_stock",
        "depth",
        "description",
        "description_short",
        "ean13",
        "ecotax",
        "height",
        "id_category_default",
        "id_default_combination",
        "id_default_image",
        "id_lang",
        "id_manufacturer",
        "id_product",
        "id_shop",
        "id_shop_default",
        "id_supplier",
        "id_tax",
        "id_type_redirected",
        "indexed",
        "is_virtual",
        "isbn",
        "locale",
        "location",
        "low_stock_alert",
        "low_stock_threshold",
        "meta_description",
        "meta_keywords",
        "meta_title",
        "link_rewrite",
        "name",
        "ingredients",
        "how_to_use",
        "specification",
        "minimal_quantity",
        "mpn",
        "on_sale",
        "online_only",
        "out_of_stock",
        "pack_stock_type",
        "position_in_category",
        "price",
         "product_type",
        "quantity_discount",
        "redirect_type",
        "reference",
        "show_condition",
        "show_price",
        "state",
        "supplier_reference",
        "text_fields",
        "unit_price_ratio",
        "unity",
        "upc",
        "uploadable_files",
        "visibility",
        "volume",
        "weight",
        "wholesale_price",
        "width"
    ]
    for key in required_keys:
        assert key in default_values_data, f"Missing key: {key} in the default values data."

def test_default_values_active_is_int_one(default_values_data):
    """Checks if 'active' has the default value 1."""
    assert default_values_data["active"] == 1, "The 'active' field should default to 1."

def test_default_values_advanced_stock_management_is_string_zero(default_values_data):
    """Checks if 'advanced_stock_management' has the default value '0'."""
    assert default_values_data["advanced_stock_management"] == "0", "The 'advanced_stock_management' field should default to '0'."

def test_default_values_associations_is_dict(default_values_data):
    """Checks if 'associations' is a dictionary"""
    assert isinstance(default_values_data["associations"], dict), "The 'associations' should be a dictionary."

def test_default_values_associations_has_required_keys(default_values_data):
     """Checks if required keys are present in default values dictionary."""
     required_keys = [
        "categories",
        "images",
        "combinations",
        "product_option_values",
        "product_features",
        "tags",
        "stock_availables",
        "attachments",
        "accessories",
        "product_bundle"
     ]
     for key in required_keys:
          assert key in default_values_data["associations"], f"Missing key: {key} in the associations data."

def test_default_values_associations_categories_is_dict(default_values_data):
     """Checks if categories is a dictionary"""
     assert isinstance(default_values_data["associations"]["categories"], dict), "The 'categories' should be a dictionary."

def test_default_values_associations_categories_has_category_key(default_values_data):
     """Checks if category is present in categories"""
     assert "category" in default_values_data["associations"]["categories"], "Missing 'category' key in 'categories' data."

def test_default_values_associations_categories_category_is_list(default_values_data):
     """Checks if category value is a list"""
     assert isinstance(default_values_data["associations"]["categories"]["category"], list), "The 'category' should be a list."

def test_default_values_associations_categories_category_has_one_element(default_values_data):
      """Checks if category list has one element"""
      assert len(default_values_data["associations"]["categories"]["category"]) == 1, "The 'category' should be a list of one element."

def test_default_values_associations_categories_category_has_id_key(default_values_data):
      """Checks if id key is present in the category dictionary"""
      assert "id" in default_values_data["associations"]["categories"]["category"][0], "Missing 'id' key in the 'category' dictionary."

def test_default_values_associations_images_is_dict(default_values_data):
     """Checks if images is a dictionary"""
     assert isinstance(default_values_data["associations"]["images"], dict), "The 'images' should be a dictionary."

def test_default_values_associations_images_has_image_key(default_values_data):
     """Checks if image key is present in images"""
     assert "image" in default_values_data["associations"]["images"], "Missing 'image' key in 'images' data."

def test_default_values_associations_images_image_is_list(default_values_data):
      """Checks if image value is a list"""
      assert isinstance(default_values_data["associations"]["images"]["image"], list), "The 'image' should be a list."

def test_default_values_associations_images_image_has_one_element(default_values_data):
      """Checks if image list has one element"""
      assert len(default_values_data["associations"]["images"]["image"]) == 1, "The 'image' list should have one element."

def test_default_values_associations_images_image_has_id_key(default_values_data):
      """Checks if id key is present in image dictionary"""
      assert "id" in default_values_data["associations"]["images"]["image"][0], "Missing 'id' key in the 'image' dictionary."

def test_default_values_associations_combinations_is_dict(default_values_data):
     """Checks if combinations is a dictionary"""
     assert isinstance(default_values_data["associations"]["combinations"], dict), "The 'combinations' should be a dictionary."

def test_default_values_associations_combinations_has_combination_key(default_values_data):
     """Checks if combination key is present in combinations"""
     assert "combination" in default_values_data["associations"]["combinations"], "Missing 'combination' key in 'combinations' data."

def test_default_values_associations_combinations_combination_is_dict(default_values_data):
      """Checks if combination value is a dict"""
      assert isinstance(default_values_data["associations"]["combinations"]["combination"], dict), "The 'combination' should be a dict."

def test_default_values_associations_combinations_combination_has_id_key(default_values_data):
      """Checks if id key is present in combination dictionary"""
      assert "id" in default_values_data["associations"]["combinations"]["combination"], "Missing 'id' key in the 'combination' dictionary."

def test_default_values_associations_product_option_values_is_dict(default_values_data):
     """Checks if product_option_values is a dictionary"""
     assert isinstance(default_values_data["associations"]["product_option_values"], dict), "The 'product_option_values' should be a dictionary."

def test_default_values_associations_product_option_values_has_product_option_value_key(default_values_data):
     """Checks if product_option_value is present in product_option_values"""
     assert "product_option_value" in default_values_data["associations"]["product_option_values"], "Missing 'product_option_value' key in 'product_option_values' data."

def test_default_values_associations_product_option_values_product_option_value_is_dict(default_values_data):
      """Checks if product_option_value value is a dict"""
      assert isinstance(default_values_data["associations"]["product_option_values"]["product_option_value"], dict), "The 'product_option_value' should be a dict."

def test_default_values_associations_product_option_values_product_option_value_has_id_key(default_values_data):
      """Checks if id key is present in product_option_value dictionary"""
      assert "id" in default_values_data["associations"]["product_option_values"]["product_option_value"], "Missing 'id' key in the 'product_option_value' dictionary."

def test_default_values_associations_product_features_is_dict(default_values_data):
     """Checks if product_features is a dictionary"""
     assert isinstance(default_values_data["associations"]["product_features"], dict), "The 'product_features' should be a dictionary."

def test_default_values_associations_product_features_has_product_feature_key(default_values_data):
     """Checks if product_feature is present in product_features"""
     assert "product_feature" in default_values_data["associations"]["product_features"], "Missing 'product_feature' key in 'product_features' data."

def test_default_values_associations_product_features_product_feature_is_dict(default_values_data):
      """Checks if product_feature value is a dict"""
      assert isinstance(default_values_data["associations"]["product_features"]["product_feature"], dict), "The 'product_feature' should be a dict."

def test_default_values_associations_product_features_product_feature_has_id_keys(default_values_data):
      """Checks if id and id_feature_value keys are present in product_feature dictionary"""
      assert "id" in default_values_data["associations"]["product_features"]["product_feature"], "Missing 'id' key in the 'product_feature' dictionary."
      assert "id_feature_value" in default_values_data["associations"]["product_features"]["product_feature"], "Missing 'id_feature_value' key in the 'product_feature' dictionary."

def test_default_values_associations_tags_is_dict(default_values_data):
     """Checks if tags is a dictionary"""
     assert isinstance(default_values_data["associations"]["tags"], dict), "The 'tags' should be a dictionary."

def test_default_values_associations_tags_has_tag_key(default_values_data):
     """Checks if tag is present in tags"""
     assert "tag" in default_values_data["associations"]["tags"], "Missing 'tag' key in 'tags' data."

def test_default_values_associations_tags_tag_is_dict(default_values_data):
      """Checks if tag value is a dict"""
      assert isinstance(default_values_data["associations"]["tags"]["tag"], dict), "The 'tag' should be a dict."

def test_default_values_associations_tags_tag_has_id_key(default_values_data):
      """Checks if id key is present in tag dictionary"""
      assert "id" in default_values_data["associations"]["tags"]["tag"], "Missing 'id' key in the 'tag' dictionary."

def test_default_values_associations_stock_availables_is_dict(default_values_data):
     """Checks if stock_availables is a dictionary"""
     assert isinstance(default_values_data["associations"]["stock_availables"], dict), "The 'stock_availables' should be a dictionary."

def test_default_values_associations_stock_availables_has_stock_available_key(default_values_data):
     """Checks if stock_available is present in stock_availables"""
     assert "stock_available" in default_values_data["associations"]["stock_availables"], "Missing 'stock_available' key in 'stock_availables' data."

def test_default_values_associations_stock_availables_stock_available_is_list(default_values_data):
      """Checks if stock_available value is a list"""
      assert isinstance(default_values_data["associations"]["stock_availables"]["stock_available"], list), "The 'stock_available' should be a list."

def test_default_values_associations_stock_availables_stock_available_has_one_element(default_values_data):
      """Checks if stock_available list has one element"""
      assert len(default_values_data["associations"]["stock_availables"]["stock_available"]) == 1, "The 'stock_available' list should have one element."

def test_default_values_associations_stock_availables_stock_available_has_id_keys(default_values_data):
      """Checks if id and id_product_attribute keys are present in stock_available dictionary"""
      assert "id" in default_values_data["associations"]["stock_availables"]["stock_available"][0], "Missing 'id' key in the 'stock_available' dictionary."
      assert "id_product_attribute" in default_values_data["associations"]["stock_availables"]["stock_available"][0], "Missing 'id_product_attribute' key in the 'stock_available' dictionary."


def test_default_values_associations_attachments_is_dict(default_values_data):
     """Checks if attachments is a dictionary"""
     assert isinstance(default_values_data["associations"]["attachments"], dict), "The 'attachments' should be a dictionary."

def test_default_values_associations_attachments_has_attachment_key(default_values_data):
     """Checks if attachment is present in attachments"""
     assert "attachment" in default_values_data["associations"]["attachments"], "Missing 'attachment' key in 'attachments' data."

def test_default_values_associations_attachments_attachment_is_dict(default_values_data):
      """Checks if attachment value is a dict"""
      assert isinstance(default_values_data["associations"]["attachments"]["attachment"], dict), "The 'attachment' should be a dict."

def test_default_values_associations_attachments_attachment_has_id_key(default_values_data):
      """Checks if id key is present in attachment dictionary"""
      assert "id" in default_values_data["associations"]["attachments"]["attachment"], "Missing 'id' key in the 'attachment' dictionary."

def test_default_values_associations_accessories_is_dict(default_values_data):
     """Checks if accessories is a dictionary"""
     assert isinstance(default_values_data["associations"]["accessories"], dict), "The 'accessories' should be a dictionary."

def test_default_values_associations_accessories_has_product_key(default_values_data):
     """Checks if product is present in accessories"""
     assert "product" in default_values_data["associations"]["accessories"], "Missing 'product' key in 'accessories' data."

def test_default_values_associations_accessories_product_is_dict(default_values_data):
      """Checks if product value is a dict"""
      assert isinstance(default_values_data["associations"]["accessories"]["product"], dict), "The 'product' should be a dict."

def test_default_values_associations_accessories_product_has_id_key(default_values_data):
      """Checks if id key is present in product dictionary"""
      assert "id" in default_values_data["associations"]["accessories"]["product"], "Missing 'id' key in the 'product' dictionary."

def test_default_values_associations_product_bundle_is_dict(default_values_data):
     """Checks if product_bundle is a dictionary"""
     assert isinstance(default_values_data["associations"]["product_bundle"], dict), "The 'product_bundle' should be a dictionary."

def test_default_values_associations_product_bundle_has_product_key(default_values_data):
     """Checks if product is present in product_bundle"""
     assert "product" in default_values_data["associations"]["product_bundle"], "Missing 'product' key in 'product_bundle' data."

def test_default_values_associations_product_bundle_product_is_dict(default_values_data):
      """Checks if product value is a dict"""
      assert isinstance(default_values_data["associations"]["product_bundle"]["product"], dict), "The 'product' should be a dict."

def test_default_values_associations_product_bundle_product_has_id_keys(default_values_data):
      """Checks if id and id_product_attribute keys are present in product dictionary"""
      assert "id" in default_values_data["associations"]["product_bundle"]["product"], "Missing 'id' key in the 'product' dictionary."
      assert "id_product_attribute" in default_values_data["associations"]["product_bundle"]["product"], "Missing 'id_product_attribute' key in the 'product' dictionary."
      assert "quantity" in default_values_data["associations"]["product_bundle"]["product"], "Missing 'quantity' key in the 'product' dictionary."

def test_default_values_available_for_order_is_int_one(default_values_data):
     """Checks if available_for_order has default value of 1"""
     assert default_values_data["available_for_order"] == 1, "The 'available_for_order' field should default to 1."

def test_default_values_condition_is_new(default_values_data):
     """Checks if condition has default value of new"""
     assert default_values_data["condition"] == "new", "The 'condition' field should default to 'new'."

def test_default_values_id_category_default_is_int_2(default_values_data):
     """Checks if id_category_default has default value of 2"""
     assert default_values_data["id_category_default"] == 2, "The 'id_category_default' field should default to 2."

def test_default_values_id_lang_is_int_1(default_values_data):
     """Checks if id_lang has default value of 1"""
     assert default_values_data["id_lang"] == 1, "The 'id_lang' field should default to 1."

def test_default_values_id_shop_is_int_1(default_values_data):
     """Checks if id_shop has default value of 1"""
     assert default_values_data["id_shop"] == 1, "The 'id_shop' field should default to 1."

def test_default_values_id_shop_default_is_int_1(default_values_data):
     """Checks if id_shop_default has default value of 1"""
     assert default_values_data["id_shop_default"] == 1, "The 'id_shop_default' field should default to 1."

def test_default_values_id_tax_is_int_13(default_values_data):
     """Checks if id_tax has default value of 13"""
     assert default_values_data["id_tax"] == 13, "The 'id_tax' field should default to 13."

def test_default_values_is_virtual_is_int_0(default_values_data):
     """Checks if is_virtual has default value of 0"""
     assert default_values_data["is_virtual"] == 0, "The 'is_virtual' field should default to 0."

def test_default_values_minimal_quantity_is_int_1(default_values_data):
     """Checks if minimal_quantity has default value of 1"""
     assert default_values_data["minimal_quantity"] == 1, "The 'minimal_quantity' field should default to 1."

def test_default_values_on_sale_is_int_1(default_values_data):
     """Checks if on_sale has default value of 1"""
     assert default_values_data["on_sale"] == 1, "The 'on_sale' field should default to 1."

def test_default_values_online_only_is_int_0(default_values_data):
     """Checks if online_only has default value of 0"""
     assert default_values_data["online_only"] == 0, "The 'online_only' field should default to 0."

def test_default_values_product_type_is_standard(default_values_data):
    """Checks if product_type has default value of standard"""
    assert default_values_data["product_type"] == "standard", "The 'product_type' field should default to 'standard'."

def test_default_values_show_condition_is_int_1(default_values_data):
     """Checks if show_condition has default value of 1"""
     assert default_values_data["show_condition"] == 1, "The 'show_condition' field should default to 1."

def test_default_values_show_price_is_int_1(default_values_data):
     """Checks if show_price has default value of 1"""
     assert default_values_data["show_price"] == 1, "The 'show_price' field should default to 1."

def test_default_values_state_is_int_1(default_values_data):
     """Checks if state has default value of 1"""
     assert default_values_data["state"] == 1, "The 'state' field should default to 1."

def test_default_values_visibility_is_int_1(default_values_data):
     """Checks if visibility has default value of 1"""
     assert default_values_data["visibility"] == 1, "The 'visibility' field should default to 1."
```