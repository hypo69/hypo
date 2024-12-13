```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def facial_scenarios_data():
    """Loads the facial scenarios JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "serums": {
          "url": "https://hbdeadsea.co.il/product-category/facial/serums/",
          "name": "סרומים לפנים",
          "condition": "new",
          "presta_categories": {
            "default_category": 11254,
            "additional_categories": [
              11268
            ]
          }
        },
        "face-masks": {
          "url": "https://hbdeadsea.co.il/product-category/facial/face-masks/#",
          "name": "מסכות פנים",
          "condition": "new",
          "presta_categories": {
            "default_category": 11255,
            "additional_categories": [
              11268
            ]
          }
        },
        "facial-cleaning-products": {
            "url": "https://hbdeadsea.co.il/product-category/facial/facial-cleaning-products/",
            "name": "מוצרי ניקוי פנים",
            "condition": "new",
            "presta_categories": {
              "default_category": 11256,
              "additional_categories": [
                11268
              ]
            }
        },
        "mineral-peptide": {
          "url": "https://hbdeadsea.co.il/product-category/facial/mineral-peptide/",
          "name": "סדרת מינרל פפטיד",
          "condition": "new",
          "presta_categories": {
            "default_category": 11258,
            "additional_categories": [
              11268
            ]
          }
        },
        "multi-active-series": {
          "url": "https://hbdeadsea.co.il/product-category/facial/multi-active-series/",
          "name": "סדרת מולטי אקטיב חומצה היאלורונית",
          "condition": "new",
          "presta_categories": {
            "default_category": 11257,
            "additional_categories": [
              11268
            ]
          }
        },
        "moisture-face": {
          "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face/",
          "name": "לחויות לפנים",
          "condition": "new",
          "presta_categories": {
            "default_category": 11329,
            "additional_categories": [
              11268
            ]
          }
        }
      }
    }
    """
    return json.loads(json_data)


def test_facial_scenarios_structure(facial_scenarios_data):
    """
    Test that the 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in facial_scenarios_data
    assert isinstance(facial_scenarios_data["scenarios"], dict)

def test_facial_scenario_keys(facial_scenarios_data):
    """
    Test that each scenario has the required keys: 'url', 'name', 'condition', 'presta_categories'.
    """
    for scenario_name, scenario_data in facial_scenarios_data["scenarios"].items():
      if scenario_data is not None: # Skip cases where scenario is null 
        assert "url" in scenario_data
        assert "name" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data
def test_presta_categories_structure(facial_scenarios_data):
    """
    Test that 'presta_categories' has 'default_category' and 'additional_categories' keys.
    """
    for scenario_name, scenario_data in facial_scenarios_data["scenarios"].items():
        if scenario_data is not None:  # Skip cases where scenario is null
          presta_categories = scenario_data.get("presta_categories")
          assert isinstance(presta_categories, dict)
          assert "default_category" in presta_categories
          assert "additional_categories" in presta_categories

def test_presta_categories_types(facial_scenarios_data):
    """
    Test that 'default_category' is an integer and 'additional_categories' is a list of integers.
    """
    for scenario_name, scenario_data in facial_scenarios_data["scenarios"].items():
        if scenario_data is not None:  # Skip cases where scenario is null
          presta_categories = scenario_data.get("presta_categories")
          assert isinstance(presta_categories["default_category"], int)
          assert isinstance(presta_categories["additional_categories"], list)
          for item in presta_categories["additional_categories"]:
            assert isinstance(item, int)

def test_url_type(facial_scenarios_data):
    """
    Test that the 'url' is a string.
    """
    for scenario_name, scenario_data in facial_scenarios_data["scenarios"].items():
        if scenario_data is not None:  # Skip cases where scenario is null
          assert isinstance(scenario_data["url"], str)

def test_name_type(facial_scenarios_data):
    """
    Test that 'name' is a string.
    """
    for scenario_name, scenario_data in facial_scenarios_data["scenarios"].items():
        if scenario_data is not None:  # Skip cases where scenario is null
           assert isinstance(scenario_data["name"], str)
           
def test_condition_type(facial_scenarios_data):
    """
    Test that 'condition' is a string.
    """
    for scenario_name, scenario_data in facial_scenarios_data["scenarios"].items():
        if scenario_data is not None:  # Skip cases where scenario is null
           assert isinstance(scenario_data["condition"], str)

def test_facial_cleaning_products_null_scenario(facial_scenarios_data):
    """
    Test that 'facial-cleaning-products' can be null.
    """
    assert facial_scenarios_data["scenarios"]["facial-cleaning-products"] is None


```