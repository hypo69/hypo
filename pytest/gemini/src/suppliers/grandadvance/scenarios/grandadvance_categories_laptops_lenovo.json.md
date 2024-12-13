```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_categories_data():
    """Provides the laptop categories data from the JSON file."""
    file_path = "hypotez/src/suppliers/grandadvance/scenarios/grandadvance_categories_laptops_lenovo.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test case for verifying the structure of each laptop category
def test_laptop_category_structure(laptop_categories_data):
    """
    Test case to ensure each laptop category has the correct structure:
    - 'brand' key exists and is not empty.
    - 'url' key exists and is a valid URL format.
    - 'checkbox' key exists and contains 'cpu' and 'screensize' keys.
    - 'active' key exists and is a boolean.
     - 'condition' key exists and is string.
      - 'presta_categories' key exists and is string.
    """
    for category_name, category_data in laptop_categories_data.items():
        assert "brand" in category_data, f"Category '{category_name}' is missing 'brand' key."
        assert category_data["brand"], f"Category '{category_name}' has an empty 'brand'."
        
        assert "url" in category_data, f"Category '{category_name}' is missing 'url' key."
        assert category_data["url"].startswith("https://"), f"Category '{category_name}' URL is not valid."

        assert "checkbox" in category_data, f"Category '{category_name}' is missing 'checkbox' key."
        assert "cpu" in category_data["checkbox"], f"Category '{category_name}' is missing 'cpu' key in checkbox."
        assert "screensize" in category_data["checkbox"], f"Category '{category_name}' is missing 'screensize' key in checkbox."
        
        assert "active" in category_data, f"Category '{category_name}' is missing 'active' key."
        assert isinstance(category_data["active"], bool), f"Category '{category_name}' 'active' is not a boolean."

        assert "condition" in category_data, f"Category '{category_name}' is missing 'condition' key."
        assert isinstance(category_data["condition"], str), f"Category '{category_name}' 'condition' is not a string."


        assert "presta_categories" in category_data, f"Category '{category_name}' is missing 'presta_categories' key."
        assert isinstance(category_data["presta_categories"], str), f"Category '{category_name}' 'presta_categories' is not a string."


# Test case for verifying the CPU checkbox structure
def test_cpu_checkbox_structure(laptop_categories_data):
    """
    Test case to verify the structure of the 'cpu' checkbox within each laptop category.
    - 'class' key exists and is a string.
    - 'by' key exists and is a string.
    - 'value' key exists and is a list.
    """
    for category_name, category_data in laptop_categories_data.items():
        cpu_data = category_data["checkbox"]["cpu"]
        assert "class" in cpu_data, f"Category '{category_name}' CPU is missing 'class' key."
        assert isinstance(cpu_data["class"], str), f"Category '{category_name}' CPU 'class' is not a string."
        
        assert "by" in cpu_data, f"Category '{category_name}' CPU is missing 'by' key."
        assert isinstance(cpu_data["by"], str), f"Category '{category_name}' CPU 'by' is not a string."
        
        assert "value" in cpu_data, f"Category '{category_name}' CPU is missing 'value' key."
        assert isinstance(cpu_data["value"], list), f"Category '{category_name}' CPU 'value' is not a list."
        assert len(cpu_data["value"]) > 0, f"Category '{category_name}' CPU 'value' list is empty."


# Test case for verifying the screensize checkbox structure
def test_screensize_checkbox_structure(laptop_categories_data):
    """
    Test case to verify the structure of the 'screensize' checkbox within each laptop category.
    - 'class' key exists and is a string.
    - 'by' key exists and is a string.
    - 'value' key exists and is a list.
    """
    for category_name, category_data in laptop_categories_data.items():
        screensize_data = category_data["checkbox"]["screensize"]
        assert "class" in screensize_data, f"Category '{category_name}' screensize is missing 'class' key."
        assert isinstance(screensize_data["class"], str), f"Category '{category_name}' screensize 'class' is not a string."
        
        assert "by" in screensize_data, f"Category '{category_name}' screensize is missing 'by' key."
        assert isinstance(screensize_data["by"], str), f"Category '{category_name}' screensize 'by' is not a string."
        
        assert "value" in screensize_data, f"Category '{category_name}' screensize is missing 'value' key."
        assert isinstance(screensize_data["value"], list), f"Category '{category_name}' screensize 'value' is not a list."
        assert len(screensize_data["value"]) > 0, f"Category '{category_name}' screensize 'value' list is empty."

# Test case to check if all categories have unique names
def test_unique_category_names(laptop_categories_data):
    """
    Test case to verify that all category names are unique within the JSON data.
    """
    category_names = list(laptop_categories_data.keys())
    assert len(category_names) == len(set(category_names)), "Category names are not unique."

# Test case to check if all presta_categories are strings and contain comma separated numbers

def test_presta_categories_format(laptop_categories_data):
    """
    Test case to verify that all 'presta_categories' values are strings
    and contain comma-separated numbers.
    """
    for category_name, category_data in laptop_categories_data.items():
        presta_categories = category_data.get("presta_categories")
        assert isinstance(presta_categories, str), f"Category '{category_name}' 'presta_categories' is not a string."

        categories_list = presta_categories.split(',')
        for cat in categories_list:
            assert cat.isdigit(), f"Category '{category_name}' 'presta_categories' contains non-digit values: {cat}."
```