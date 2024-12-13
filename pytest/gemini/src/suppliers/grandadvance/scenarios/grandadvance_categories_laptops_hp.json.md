```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def grandadvance_hp_categories():
    """Loads the grandadvance_categories_laptops_hp.json data."""
    file_path = 'hypotez/src/suppliers/grandadvance/scenarios/grandadvance_categories_laptops_hp.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test for the structure of the JSON data
def test_json_data_structure(grandadvance_hp_categories):
    """
    Test if the loaded JSON is a dictionary and each value is also a dictionary
     with required keys.
    """
    assert isinstance(grandadvance_hp_categories, dict), "The root element should be a dictionary."
    for key, value in grandadvance_hp_categories.items():
        assert isinstance(value, dict), f"The value for key '{key}' should be a dictionary."
        assert "brand" in value, f"The key 'brand' is missing in the dictionary for '{key}'."
        assert "url" in value, f"The key 'url' is missing in the dictionary for '{key}'."
        assert "checkbox" in value, f"The key 'checkbox' is missing in the dictionary for '{key}'."
        assert "active" in value, f"The key 'active' is missing in the dictionary for '{key}'."
        assert "condition" in value, f"The key 'condition' is missing in the dictionary for '{key}'."
        assert "presta_categories" in value, f"The key 'presta_categories' is missing in the dictionary for '{key}'."
        assert isinstance(value["checkbox"], dict), f"The value of 'checkbox' for key '{key}' should be a dictionary."
        assert "cpu" in value["checkbox"], f"The key 'cpu' is missing in the 'checkbox' dictionary for '{key}'."
        assert "screensize" in value["checkbox"], f"The key 'screensize' is missing in the 'checkbox' dictionary for '{key}'."
        assert isinstance(value["checkbox"]["cpu"], dict), f"The value of 'cpu' for key '{key}' should be a dictionary."
        assert isinstance(value["checkbox"]["screensize"], dict), f"The value of 'screensize' for key '{key}' should be a dictionary."
        assert "class" in value["checkbox"]["cpu"], f"The key 'class' is missing in the 'cpu' dictionary for '{key}'."
        assert "by" in value["checkbox"]["cpu"], f"The key 'by' is missing in the 'cpu' dictionary for '{key}'."
        assert "value" in value["checkbox"]["cpu"], f"The key 'value' is missing in the 'cpu' dictionary for '{key}'."
        assert "class" in value["checkbox"]["screensize"], f"The key 'class' is missing in the 'screensize' dictionary for '{key}'."
        assert "by" in value["checkbox"]["screensize"], f"The key 'by' is missing in the 'screensize' dictionary for '{key}'."
        assert "value" in value["checkbox"]["screensize"], f"The key 'value' is missing in the 'screensize' dictionary for '{key}'."
        assert isinstance(value["checkbox"]["cpu"]["value"], list), f"The value of 'cpu'->'value' for key '{key}' should be a list."
        assert isinstance(value["checkbox"]["screensize"]["value"], list), f"The value of 'screensize'->'value' for key '{key}' should be a list."



# Test to check brand values
def test_brand_values(grandadvance_hp_categories):
    """Checks if the brand value is 'HP' for all entries."""
    for key, value in grandadvance_hp_categories.items():
        assert value["brand"] == "HP", f"The brand for '{key}' is not 'HP'."

# Test to check that the url is valid
def test_url_values(grandadvance_hp_categories):
    """Checks if the url value is a valid url."""
    for key, value in grandadvance_hp_categories.items():
        assert value["url"].startswith("https://www.grandadvance.co.il/"), f"The url for '{key}' is not a grandadvance url."

# Test to check the 'by' values in checkbox
def test_checkbox_by_values(grandadvance_hp_categories):
    """Checks if the 'by' value in 'checkbox' is 'css selector' for all entries."""
    for key, value in grandadvance_hp_categories.items():
         assert value["checkbox"]["cpu"]["by"] == "css selector", f"The 'by' value for cpu in '{key}' is not 'css selector'."
         assert value["checkbox"]["screensize"]["by"] == "css selector", f"The 'by' value for screensize in '{key}' is not 'css selector'."
        
# Test to check the 'class' values in checkbox
def test_checkbox_class_values(grandadvance_hp_categories):
    """Checks if the 'class' value in 'checkbox' is '.fSel' for all entries."""
    for key, value in grandadvance_hp_categories.items():
         assert value["checkbox"]["cpu"]["class"] == ".fSel", f"The 'class' value for cpu in '{key}' is not '.fSel'."
         assert value["checkbox"]["screensize"]["class"] == ".fSel", f"The 'class' value for screensize in '{key}' is not '.fSel'."


# Test to check for active is always true
def test_active_values(grandadvance_hp_categories):
    """Checks if the active value is True for all entries."""
    for key, value in grandadvance_hp_categories.items():
        assert value["active"] is True, f"The active value for '{key}' is not True."
        
# Test to check if condition is 'new'
def test_condition_values(grandadvance_hp_categories):
    """Checks if the condition value is 'new' for all entries."""
    for key, value in grandadvance_hp_categories.items():
        assert value["condition"] == "new", f"The condition value for '{key}' is not 'new'."

# Test to validate presta_categories 
def test_presta_categories_values(grandadvance_hp_categories):
    """
     Checks if the presta_categories value is a string and contains only digits and commas
     and if it starts with '3'.
    """
    for key, value in grandadvance_hp_categories.items():
      assert isinstance(value["presta_categories"], str), f"The presta_categories for '{key}' is not a string."
      assert all(c.isdigit() or c == ',' for c in value["presta_categories"]), f"The presta_categories for '{key}' contains invalid characters."
      assert value["presta_categories"].startswith('3'), f"The presta_categories for '{key}' does not start with '3'."
```