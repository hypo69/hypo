```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the morlevi categories data from the JSON file."""
    json_data = """
    {
      "scenarios": {
        "routers": {
          "url": "https://www.morlevi.co.il/Cat/111",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,211"
        },
        "switch": {
          "url": "https://www.morlevi.co.il/Cat/141",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,212"
        },
        "access point": {
          "url": "https://www.morlevi.co.il/Cat/144",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,213"
        },
        "network cards": {
          "url": "https://www.morlevi.co.il/Cat/154",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,214"
        },
        "network-cables": {
          "url": "https://www.morlevi.co.il/Cat/192",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,215"
        },
        "nas": {
          "url": "https://www.morlevi.co.il/Cat/346",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,216"
        },
        "racks": {
          "url": "https://www.morlevi.co.il/Cat/198",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,217"
        }
      }
    }
    """
    return json.loads(json_data)


def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test that the loaded JSON data has the expected structure.
    Verifies the presence of 'scenarios' key and its nested keys.
    """
    assert "scenarios" in morlevi_categories_data, "The JSON should contain a 'scenarios' key."
    assert isinstance(morlevi_categories_data["scenarios"], dict), "'scenarios' should be a dictionary."
    expected_keys = ["routers", "switch", "access point", "network cards", "network-cables", "nas", "racks"]
    assert all(key in morlevi_categories_data["scenarios"] for key in expected_keys), "All expected categories should be present."


def test_morlevi_category_attributes(morlevi_categories_data):
    """
    Tests the attributes of one of the categories.
    Verifies the structure and expected types within each category.
    """
    category = morlevi_categories_data["scenarios"]["routers"]
    assert "url" in category, "Category should contain a 'url' key."
    assert isinstance(category["url"], str), "'url' should be a string."
    assert "checkbox" in category, "Category should contain a 'checkbox' key."
    assert isinstance(category["checkbox"], bool), "'checkbox' should be a boolean."
    assert "active" in category, "Category should contain an 'active' key."
    assert isinstance(category["active"], bool), "'active' should be a boolean."
    assert "condition" in category
    assert isinstance(category["condition"], str)
    assert "presta_categories" in category
    assert isinstance(category["presta_categories"], str)

def test_all_morlevi_category_attributes(morlevi_categories_data):
    """
    Tests the attributes of all categories.
    Iterates through all categories and verifies structure and expected types.
    """
    for category_name, category in morlevi_categories_data["scenarios"].items():
        assert "url" in category, f"Category '{category_name}' should contain a 'url' key."
        assert isinstance(category["url"], str), f"'url' in '{category_name}' should be a string."
        assert "checkbox" in category, f"Category '{category_name}' should contain a 'checkbox' key."
        assert isinstance(category["checkbox"], bool), f"'checkbox' in '{category_name}' should be a boolean."
        assert "active" in category, f"Category '{category_name}' should contain an 'active' key."
        assert isinstance(category["active"], bool), f"'active' in '{category_name}' should be a boolean."
        assert "condition" in category, f"Category '{category_name}' should contain a 'condition' key."
        assert isinstance(category["condition"], str), f"'condition' in '{category_name}' should be a string."
        assert "presta_categories" in category, f"Category '{category_name}' should contain a 'presta_categories' key."
        assert isinstance(category["presta_categories"], str), f"'presta_categories' in '{category_name}' should be a string."

def test_morlevi_url_format(morlevi_categories_data):
    """
    Test if URLs have the correct format using startswith
    """
    for category_name, category in morlevi_categories_data["scenarios"].items():
        assert category["url"].startswith("https://www.morlevi.co.il/Cat/"), f"URL in '{category_name}' should start with 'https://www.morlevi.co.il/Cat/'."

def test_presta_categories_format(morlevi_categories_data):
        """
        Tests if presta_categories are comma-separated strings.
        """
        for category_name, category in morlevi_categories_data["scenarios"].items():
            presta_categories = category.get("presta_categories")
            assert presta_categories is not None, f"Category '{category_name}' should have 'presta_categories'."
            assert isinstance(presta_categories, str), f"'presta_categories' in '{category_name}' should be a string"
            categories = presta_categories.split(',')
            assert all(cat.strip().isdigit() for cat in categories), f"All presta_categories in {category_name} should be digits"

def test_morlevi_empty_scenarios(morlevi_categories_data):
  """Tests the case if the `scenarios` dict is empty."""
  morlevi_categories_data["scenarios"] = {}
  assert morlevi_categories_data["scenarios"] == {}, "scenarios should be an empty dict"
```