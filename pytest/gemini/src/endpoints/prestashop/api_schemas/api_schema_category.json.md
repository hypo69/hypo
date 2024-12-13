```python
import pytest
import json

# Fixture to load the JSON schema
@pytest.fixture
def category_schema():
    """Loads the category schema from the JSON file."""
    with open('hypotez/src/endpoints/prestashop/api_schemas/api_schema_category.json', 'r') as f:
        return json.load(f)

def test_category_schema_structure(category_schema):
    """
    Tests the basic structure of the category schema. 
    Checks if the main 'category' key exists and has the expected nested structure.
    """
    assert "category" in category_schema, "The 'category' key is missing."
    category = category_schema["category"]
    
    expected_keys = [
        "id", "id_parent", "active", "id_shop_default", "is_root_category", 
        "position", "date_add", "date_upd", "name", "link_rewrite", 
        "description", "meta_title", "meta_description", "meta_keywords", 
        "description_long", "associations"
    ]
    for key in expected_keys:
         assert key in category, f"The '{key}' key is missing in category."


def test_category_language_structure(category_schema):
    """
    Tests the language structure within the category schema.
    Verifies if fields with language variation have the correct 'language' key and 'attrs' structure.
    """
    category = category_schema["category"]

    language_fields = [
        "name", "link_rewrite", "description", 
        "meta_title", "meta_description", "meta_keywords", "description_long"
    ]
    
    for field in language_fields:
      assert "language" in category[field], f"The 'language' key is missing in {field}."
      language_list = category[field]["language"]
      assert isinstance(language_list,list), f"The 'language' in '{field}' is not a list"
      for lang_item in language_list:
         assert "attrs" in lang_item, f"The 'attrs' key is missing in language item of {field}"
         assert "id" in lang_item["attrs"], f"The 'id' key is missing in attrs of language item of {field}"
         assert "value" in lang_item, f"The 'value' key is missing in language item of {field}"


def test_category_associations_structure(category_schema):
    """
    Tests the associations structure within the category schema.
    Verifies if the 'associations' key exists and has the expected nested structure for 'categories' and 'products'.
    """
    category = category_schema["category"]
    assert "associations" in category, "The 'associations' key is missing."
    associations = category["associations"]
    
    assert "categories" in associations, "The 'categories' key is missing in associations."
    assert "category" in associations["categories"], "The 'category' key is missing in categories."
    assert "id" in associations["categories"]["category"], "The 'id' key is missing in associations.categories.category"

    assert "products" in associations, "The 'products' key is missing in associations."
    assert "product" in associations["products"], "The 'product' key is missing in products."
    assert "id" in associations["products"]["product"], "The 'id' key is missing in associations.products.product"

def test_category_schema_empty_values(category_schema):
    """
    Tests the default values of the category schema.
    Verifies if all the values are empty strings ("") by default as defined in schema.
    """
    category = category_schema["category"]

    # List of fields which must be strings
    string_fields = [
        "id", "id_parent", "active", "id_shop_default", "is_root_category", "position", "date_add", "date_upd"
    ]
    for field in string_fields:
        assert category[field] == "", f"The default value of '{field}' is not an empty string."
    
    language_fields = [
        "name", "link_rewrite", "description", 
        "meta_title", "meta_description", "meta_keywords", "description_long"
    ]

    for field in language_fields:
        for lang_item in category[field]["language"]:
           assert lang_item["value"] == "", f"The default value of language item in '{field}' is not an empty string."

    
    assert category["associations"]["categories"]["category"]["id"] == "", "The default value of category id in associations is not empty string"
    assert category["associations"]["products"]["product"]["id"] == "", "The default value of product id in associations is not empty string"

def test_category_schema_language_ids(category_schema):
    """
    Tests the language ids in the category schema.
     Verifies if the language ids have values "1", "2" and "3" as defined in the schema.
    """
    category = category_schema["category"]
    language_fields = [
         "name", "link_rewrite", "description",
         "meta_title", "meta_description", "meta_keywords", "description_long"
     ]

    for field in language_fields:
         lang_ids = [lang_item["attrs"]["id"] for lang_item in category[field]["language"]]
         assert lang_ids == ["1","2","3"], f"The language ids in '{field}' do not match expected values"
```