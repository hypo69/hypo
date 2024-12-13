```python
import pytest
import json

# Fixture to load the product schema
@pytest.fixture
def product_schema():
    """Loads the product schema from the JSON file."""
    with open("hypotez/src/endpoints/prestashop/api_schemas/api_schema_product.json", "r") as f:
        return json.load(f)

def test_product_schema_structure(product_schema):
    """
    Test the basic structure of the product schema.
    Checks if the top-level key 'product' exists and is a dictionary.
    """
    assert "product" in product_schema
    assert isinstance(product_schema["product"], dict)

def test_product_id_field(product_schema):
    """
    Test the 'id' field within the product schema.
    Checks if 'id' field exists and is a string, allowing empty string.
    """
    assert "id" in product_schema["product"]
    assert isinstance(product_schema["product"]["id"], str)

def test_product_delivery_in_stock_structure(product_schema):
    """
    Test the structure of the 'delivery_in_stock' field.
    Checks if the 'delivery_in_stock' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "delivery_in_stock" in product_schema["product"]
    assert isinstance(product_schema["product"]["delivery_in_stock"], dict)
    assert "language" in product_schema["product"]["delivery_in_stock"]
    assert isinstance(product_schema["product"]["delivery_in_stock"]["language"], list)
    
    for lang in product_schema["product"]["delivery_in_stock"]["language"]:
      assert "attrs" in lang
      assert "id" in lang["attrs"]
      assert isinstance(lang["attrs"]["id"], str)
      assert "value" in lang
      assert isinstance(lang["value"], str)

def test_product_delivery_out_stock_structure(product_schema):
    """
    Test the structure of the 'delivery_out_stock' field.
    Checks if the 'delivery_out_stock' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "delivery_out_stock" in product_schema["product"]
    assert isinstance(product_schema["product"]["delivery_out_stock"], dict)
    assert "language" in product_schema["product"]["delivery_out_stock"]
    assert isinstance(product_schema["product"]["delivery_out_stock"]["language"], list)
    
    for lang in product_schema["product"]["delivery_out_stock"]["language"]:
      assert "attrs" in lang
      assert "id" in lang["attrs"]
      assert isinstance(lang["attrs"]["id"], str)
      assert "value" in lang
      assert isinstance(lang["value"], str)

def test_product_meta_description_structure(product_schema):
    """
    Test the structure of the 'meta_description' field.
    Checks if the 'meta_description' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "meta_description" in product_schema["product"]
    assert isinstance(product_schema["product"]["meta_description"], dict)
    assert "language" in product_schema["product"]["meta_description"]
    assert isinstance(product_schema["product"]["meta_description"]["language"], list)
    
    for lang in product_schema["product"]["meta_description"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_meta_keywords_structure(product_schema):
    """
    Test the structure of the 'meta_keywords' field.
     Checks if the 'meta_keywords' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "meta_keywords" in product_schema["product"]
    assert isinstance(product_schema["product"]["meta_keywords"], dict)
    assert "language" in product_schema["product"]["meta_keywords"]
    assert isinstance(product_schema["product"]["meta_keywords"]["language"], list)
    
    for lang in product_schema["product"]["meta_keywords"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_meta_title_structure(product_schema):
    """
    Test the structure of the 'meta_title' field.
    Checks if the 'meta_title' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "meta_title" in product_schema["product"]
    assert isinstance(product_schema["product"]["meta_title"], dict)
    assert "language" in product_schema["product"]["meta_title"]
    assert isinstance(product_schema["product"]["meta_title"]["language"], list)
    
    for lang in product_schema["product"]["meta_title"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_link_rewrite_structure(product_schema):
    """
    Test the structure of the 'link_rewrite' field.
     Checks if the 'link_rewrite' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "link_rewrite" in product_schema["product"]
    assert isinstance(product_schema["product"]["link_rewrite"], dict)
    assert "language" in product_schema["product"]["link_rewrite"]
    assert isinstance(product_schema["product"]["link_rewrite"]["language"], list)
    
    for lang in product_schema["product"]["link_rewrite"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_name_structure(product_schema):
    """
    Test the structure of the 'name' field.
    Checks if the 'name' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "name" in product_schema["product"]
    assert isinstance(product_schema["product"]["name"], dict)
    assert "language" in product_schema["product"]["name"]
    assert isinstance(product_schema["product"]["name"]["language"], list)
    
    for lang in product_schema["product"]["name"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_description_structure(product_schema):
    """
    Test the structure of the 'description' field.
     Checks if the 'description' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "description" in product_schema["product"]
    assert isinstance(product_schema["product"]["description"], dict)
    assert "language" in product_schema["product"]["description"]
    assert isinstance(product_schema["product"]["description"]["language"], list)
    
    for lang in product_schema["product"]["description"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_description_short_structure(product_schema):
    """
    Test the structure of the 'description_short' field.
     Checks if the 'description_short' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "description_short" in product_schema["product"]
    assert isinstance(product_schema["product"]["description_short"], dict)
    assert "language" in product_schema["product"]["description_short"]
    assert isinstance(product_schema["product"]["description_short"]["language"], list)
    
    for lang in product_schema["product"]["description_short"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_available_now_structure(product_schema):
    """
    Test the structure of the 'available_now' field.
      Checks if the 'available_now' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "available_now" in product_schema["product"]
    assert isinstance(product_schema["product"]["available_now"], dict)
    assert "language" in product_schema["product"]["available_now"]
    assert isinstance(product_schema["product"]["available_now"]["language"], list)
    
    for lang in product_schema["product"]["available_now"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_available_later_structure(product_schema):
    """
    Test the structure of the 'available_later' field.
     Checks if the 'available_later' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "available_later" in product_schema["product"]
    assert isinstance(product_schema["product"]["available_later"], dict)
    assert "language" in product_schema["product"]["available_later"]
    assert isinstance(product_schema["product"]["available_later"]["language"], list)
    
    for lang in product_schema["product"]["available_later"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_affiliate_short_link_structure(product_schema):
    """
    Test the structure of the 'affiliate_short_link' field.
    Checks if the 'affiliate_short_link' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "affiliate_short_link" in product_schema["product"]
    assert isinstance(product_schema["product"]["affiliate_short_link"], dict)
    assert "language" in product_schema["product"]["affiliate_short_link"]
    assert isinstance(product_schema["product"]["affiliate_short_link"]["language"], list)

    for lang in product_schema["product"]["affiliate_short_link"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_affiliate_text_structure(product_schema):
    """
    Test the structure of the 'affiliate_text' field.
     Checks if the 'affiliate_text' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "affiliate_text" in product_schema["product"]
    assert isinstance(product_schema["product"]["affiliate_text"], dict)
    assert "language" in product_schema["product"]["affiliate_text"]
    assert isinstance(product_schema["product"]["affiliate_text"]["language"], list)
    
    for lang in product_schema["product"]["affiliate_text"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_affiliate_summary_structure(product_schema):
    """
    Test the structure of the 'affiliate_summary' field.
    Checks if the 'affiliate_summary' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
    assert "affiliate_summary" in product_schema["product"]
    assert isinstance(product_schema["product"]["affiliate_summary"], dict)
    assert "language" in product_schema["product"]["affiliate_summary"]
    assert isinstance(product_schema["product"]["affiliate_summary"]["language"], list)

    for lang in product_schema["product"]["affiliate_summary"]["language"]:
        assert "attrs" in lang
        assert "id" in lang["attrs"]
        assert isinstance(lang["attrs"]["id"], str)
        assert "value" in lang
        assert isinstance(lang["value"], str)

def test_product_affiliate_summary_2_structure(product_schema):
     """
     Test the structure of the 'affiliate_summary_2' field.
     Checks if the 'affiliate_summary_2' field exists, is a dictionary,
    and contains a list of languages with correct attributes.
    """
     assert "affiliate_summary_2" in product_schema["product"]
     assert isinstance(product_schema["product"]["affiliate_summary_2"], dict)
     assert "language" in product_schema["product"]["affiliate_summary_2"]
     assert isinstance(product_schema["product"]["affiliate_summary_2"]["language"], list)

     for lang in product_schema["product"]["affiliate_summary_2"]["language"]:
          assert "attrs" in lang
          assert "id" in lang["attrs"]
          assert isinstance(lang["attrs"]["id"], str)
          assert "value" in lang
          assert isinstance(lang["value"], str)
          
def test_product_associations_structure(product_schema):
    """
    Test the structure of the 'associations' field.
    Checks if the 'associations' field exists and contains nested dictionaries.
    """
    assert "associations" in product_schema["product"]
    assert isinstance(product_schema["product"]["associations"], dict)
    assert "categories" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["categories"], dict)
    assert "images" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["images"], dict)
    assert "combinations" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["combinations"], dict)
    assert "product_option_values" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["product_option_values"], dict)
    assert "product_features" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["product_features"], dict)
    assert "tags" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["tags"], dict)
    assert "stock_availables" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["stock_availables"], dict)
    assert "attachments" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["attachments"], dict)
    assert "accessories" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["accessories"], dict)
    assert "product_bundle" in product_schema["product"]["associations"]
    assert isinstance(product_schema["product"]["associations"]["product_bundle"], dict)
          
def test_product_categories_association(product_schema):
    """
    Test the structure of the 'categories' association.
    Checks if 'category' is a list.
    """
    assert "category" in product_schema["product"]["associations"]["categories"]
    assert isinstance(product_schema["product"]["associations"]["categories"]["category"], list)
    
    for cat in product_schema["product"]["associations"]["categories"]["category"]:
        assert "id" in cat
        assert isinstance(cat["id"], str)

def test_product_images_association(product_schema):
     """
     Test the structure of the 'images' association.
     Checks if 'image' is a dictionary with 'id' as a string.
     """
     assert "image" in product_schema["product"]["associations"]["images"]
     assert isinstance(product_schema["product"]["associations"]["images"]["image"], dict)
     assert "id" in product_schema["product"]["associations"]["images"]["image"]
     assert isinstance(product_schema["product"]["associations"]["images"]["image"]["id"], str)

def test_product_combinations_association(product_schema):
    """
    Test the structure of the 'combinations' association.
    Checks if 'combination' is a dictionary with 'id' as a string.
    """
    assert "combination" in product_schema["product"]["associations"]["combinations"]
    assert isinstance(product_schema["product"]["associations"]["combinations"]["combination"], dict)
    assert "id" in product_schema["product"]["associations"]["combinations"]["combination"]
    assert isinstance(product_schema["product"]["associations"]["combinations"]["combination"]["id"], str)
    
def test_product_option_values_association(product_schema):
    """
    Test the structure of the 'product_option_values' association.
     Checks if 'product_option_value' is a dictionary with 'id' as a string.
    """
    assert "product_option_value" in product_schema["product"]["associations"]["product_option_values"]
    assert isinstance(product_schema["product"]["associations"]["product_option_values"]["product_option_value"], dict)
    assert "id" in product_schema["product"]["associations"]["product_option_values"]["product_option_value"]
    assert isinstance(product_schema["product"]["associations"]["product_option_values"]["product_option_value"]["id"], str)
    
def test_product_features_association(product_schema):
    """
    Test the structure of the 'product_features' association.
    Checks if 'product_feature' is a dictionary and has 'id' and 'id_feature_value'.
    """
    assert "product_feature" in product_schema["product"]["associations"]["product_features"]
    assert isinstance(product_schema["product"]["associations"]["product_features"]["product_feature"], dict)
    assert "id" in product_schema["product"]["associations"]["product_features"]["product_feature"]
    assert isinstance(product_schema["product"]["associations"]["product_features"]["product_feature"]["id"], str)
    assert "id_feature_value" in product_schema["product"]["associations"]["product_features"]["product_feature"]
    assert isinstance(product_schema["product"]["associations"]["product_features"]["product_feature"]["id_feature_value"], str)
    
def test_product_tags_association(product_schema):
    """
    Test the structure of the 'tags' association.
    Checks if 'tag' is a dictionary with 'id' as a string.
    """
    assert "tag" in product_schema["product"]["associations"]["tags"]
    assert isinstance(product_schema["product"]["associations"]["tags"]["tag"], dict)
    assert "id" in product_schema["product"]["associations"]["tags"]["tag"]
    assert isinstance(product_schema["product"]["associations"]["tags"]["tag"]["id"], str)

def test_product_stock_availables_association(product_schema):
    """
    Test the structure of the 'stock_availables' association.
    Checks if 'stock_available' is a dictionary and has 'id' and 'id_product_attribute'.
    """
    assert "stock_available" in product_schema["product"]["associations"]["stock_availables"]
    assert isinstance(product_schema["product"]["associations"]["stock_availables"]["stock_available"], dict)
    assert "id" in product_schema["product"]["associations"]["stock_availables"]["stock_available"]
    assert isinstance(product_schema["product"]["associations"]["stock_availables"]["stock_available"]["id"], str)
    assert "id_product_attribute" in product_schema["product"]["associations"]["stock_availables"]["stock_available"]
    assert isinstance(product_schema["product"]["associations"]["stock_availables"]["stock_available"]["id_product_attribute"], str)

def test_product_attachments_association(product_schema):
    """
    Test the structure of the 'attachments' association.
    Checks if 'attachment' is a dictionary with 'id' as a string.
    """
    assert "attachment" in product_schema["product"]["associations"]["attachments"]
    assert isinstance(product_schema["product"]["associations"]["attachments"]["attachment"], dict)
    assert "id" in product_schema["product"]["associations"]["attachments"]["attachment"]
    assert isinstance(product_schema["product"]["associations"]["attachments"]["attachment"]["id"], str)

def test_product_accessories_association(product_schema):
    """
    Test the structure of the 'accessories' association.
    Checks if 'product' is a dictionary with 'id' as a string.
    """
    assert "product" in product_schema["product"]["associations"]["accessories"]
    assert isinstance(product_schema["product"]["associations"]["accessories"]["product"], dict)
    assert "id" in product_schema["product"]["associations"]["accessories"]["product"]
    assert isinstance(product_schema["product"]["associations"]["accessories"]["product"]["id"], str)
    
def test_product_bundle_association(product_schema):
    """
    Test the structure of the 'product_bundle' association.
    Checks if 'product' is a dictionary and has 'id', 'id_product_attribute' and 'quantity'
    """
    assert "product" in product_schema["product"]["associations"]["product_bundle"]
    assert isinstance(product_schema["product"]["associations"]["product_bundle"]["product"], dict)
    assert "id" in product_schema["product"]["associations"]["product_bundle"]["product"]
    assert isinstance(product_schema["product"]["associations"]["product_bundle"]["product"]["id"], str)
    assert "id_product_attribute" in product_schema["product"]["associations"]["product_bundle"]["product"]
    assert isinstance(product_schema["product"]["associations"]["product_bundle"]["product"]["id_product_attribute"], str)
    assert "quantity" in product_schema["product"]["associations"]["product_bundle"]["product"]
    assert isinstance(product_schema["product"]["associations"]["product_bundle"]["product"]["quantity"], str)
```