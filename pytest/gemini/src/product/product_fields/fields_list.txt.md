```python
import pytest

# Fixture definitions, if needed
@pytest.fixture
def product_fields():
    """Provides a list of product fields for testing."""
    return [
        "additional_delivery_times",
        "additional_shipping_cost",
        "advanced_stock_management",
        "affiliate_short_link",
        "affiliate_summary",
        "affiliate_summary_2",
        "affiliate_text",
        "affiliate_image_large",
        "affiliate_image_medium",
        "affiliate_image_small",
        "associations",
        "available_date",
        "available_for_order",
        "available_later",
        "available_now",
        "cache_default_attribute",
        "cache_has_attachments",
        "cache_is_pack",
        "condition",
        "customizable",
        "date_add",
        "date_upd",
        "delivery_in_stock",
        "delivery_out_stock",
        "depth",
        "description",
        "description_short",
        "ean13",
        "ecotax",
        "height",
        "how_to_use",
        "specification",
        "id_category_default",
        "id_default_combination",
        "id_default_image",
        "locale",
        "id_manufacturer",
        "id_product",
        "id_shop_default",
        "id_shop",
        "id_supplier",
        "id_tax",
        "id_type_redirected",
        "indexed",
        "ingredients",
        "is_virtual",
        "isbn",
        "link_rewrite",
        "location",
        "low_stock_alert",
        "low_stock_threshold",
        "meta_description",
        "meta_keywords",
        "meta_title",
        "minimal_quantity",
        "mpn",
        "name",
        "online_only",
        "on_sale",
        "out_of_stock",
        "pack_stock_type",
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
        "width",
        "local_image_path",
        "local_video_path"
    ]


# Test that all fields are in the list
def test_all_fields_present(product_fields):
    """Checks if all expected product fields are present in the list"""
    expected_fields = [
        "additional_delivery_times",
        "additional_shipping_cost",
        "advanced_stock_management",
        "affiliate_short_link",
        "affiliate_summary",
        "affiliate_summary_2",
        "affiliate_text",
        "affiliate_image_large",
        "affiliate_image_medium",
        "affiliate_image_small",
        "associations",
        "available_date",
        "available_for_order",
        "available_later",
        "available_now",
        "cache_default_attribute",
        "cache_has_attachments",
        "cache_is_pack",
        "condition",
        "customizable",
        "date_add",
        "date_upd",
        "delivery_in_stock",
        "delivery_out_stock",
        "depth",
        "description",
        "description_short",
        "ean13",
        "ecotax",
        "height",
        "how_to_use",
        "specification",
        "id_category_default",
        "id_default_combination",
        "id_default_image",
        "locale",
        "id_manufacturer",
        "id_product",
        "id_shop_default",
        "id_shop",
        "id_supplier",
        "id_tax",
        "id_type_redirected",
        "indexed",
        "ingredients",
        "is_virtual",
        "isbn",
        "link_rewrite",
        "location",
        "low_stock_alert",
        "low_stock_threshold",
        "meta_description",
        "meta_keywords",
        "meta_title",
        "minimal_quantity",
        "mpn",
        "name",
        "online_only",
        "on_sale",
        "out_of_stock",
        "pack_stock_type",
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
        "width",
        "local_image_path",
        "local_video_path"
    ]
    assert set(product_fields) == set(expected_fields), "Not all expected fields are present"

def test_field_is_string(product_fields):
    """Checks that all fields are string types."""
    for field in product_fields:
        assert isinstance(field, str), f"Field '{field}' is not a string."

def test_field_is_not_empty(product_fields):
    """Checks that all fields are not empty strings."""
    for field in product_fields:
      assert field != "", f"Field '{field}' is empty"

def test_field_is_not_whitespace(product_fields):
    """Checks that all fields are not made entirely of whitespace."""
    for field in product_fields:
      assert not field.isspace(), f"Field '{field}' contains only whitespace"

def test_field_is_lowercase(product_fields):
    """Checks if all fields are in lowercase."""
    for field in product_fields:
      assert field.islower(), f"Field '{field}' is not lowercase"


def test_field_has_no_leading_or_trailing_space(product_fields):
    """Checks if all fields do not have leading or trailing spaces."""
    for field in product_fields:
        assert field.strip() == field, f"Field '{field}' has leading or trailing space(s)."

def test_field_has_no_special_characters(product_fields):
     """Checks that all fields contains only alphanumeric chars, and underscores."""
     for field in product_fields:
         assert all(c.isalnum() or c == '_' for c in field), f"Field '{field}' has invalid characters."

def test_field_has_no_duplicated_underscores(product_fields):
    """Checks that there are no duplicated underscores in the fields."""
    for field in product_fields:
        assert "__" not in field, f"Field '{field}' contains duplicated underscores."

def test_field_does_not_start_or_end_with_underscore(product_fields):
    """Checks that all fields do not start or end with underscore."""
    for field in product_fields:
        assert not field.startswith('_') , f"Field '{field}' starts with an underscore."
        assert not field.endswith('_'), f"Field '{field}' ends with an underscore."
```