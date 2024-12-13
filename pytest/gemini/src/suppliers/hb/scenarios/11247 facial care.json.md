```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def facial_care_data():
    """Provides the facial care data from the JSON file."""
    json_data = """
    {
      "scenarios": {
        "moisture-face": {
          "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face//",
          "condition": "new",
          "presta_categories": {
            "default_category": 11253,
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        },
        "serums": {
          "url": "https://hbdeadsea.co.il/product-category/facial/serums/",
          "condition": "new",
          "presta_categories": {
            "default_category": 11254,
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        },
        "face-masks": {
          "url": "https://hbdeadsea.co.il/product-category/facial/face-masks/#",
          "condition": "new",
          "presta_categories": {
            "default_category": 11255,
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        },
        "facial-cleaning-products": {
          "url": "https://hbdeadsea.co.il/product-category/facial/facial-cleaning-products/",
          "condition": "new",
          "presta_categories": {
            "default_category": 11256,
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        },
        "multi-active-series": {
          "url": "https://hbdeadsea.co.il/product-category/facial/multi-active-series/",
          "condition": "new",
          "presta_categories": {
            "default_category": 11257,
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        },
        "mineral-peptide": {
          "url": "https://hbdeadsea.co.il/product-category/facial/mineral-peptide/",
          "condition": "new",
          "presta_categories": {
            "default_category": 11258,
            "additional_categories": [ "" ]
          },
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)

def test_facial_care_data_structure(facial_care_data):
    """Checks if the data has the correct top-level structure."""
    assert "scenarios" in facial_care_data
    assert isinstance(facial_care_data["scenarios"], dict)

def test_scenario_keys(facial_care_data):
    """Checks if all scenarios have the correct keys."""
    for scenario in facial_care_data["scenarios"].values():
        assert "url" in scenario
        assert "condition" in scenario
        assert "presta_categories" in scenario
        assert "price_rule" in scenario

def test_scenario_url_format(facial_care_data):
    """Checks that the URLs are strings and start with https"""
    for scenario in facial_care_data["scenarios"].values():
        assert isinstance(scenario["url"], str)
        assert scenario["url"].startswith("https://")


def test_scenario_condition_type(facial_care_data):
    """Checks that the condition is a string"""
    for scenario in facial_care_data["scenarios"].values():
        assert isinstance(scenario["condition"], str)

def test_scenario_presta_categories_structure(facial_care_data):
    """Checks the structure of presta_categories."""
    for scenario in facial_care_data["scenarios"].values():
      assert isinstance(scenario["presta_categories"], dict)
      assert "default_category" in scenario["presta_categories"]
      assert "additional_categories" in scenario["presta_categories"]
      assert isinstance(scenario["presta_categories"]["additional_categories"], list)


def test_scenario_default_category_type(facial_care_data):
    """Checks if the default category is an int"""
    for scenario in facial_care_data["scenarios"].values():
        assert isinstance(scenario["presta_categories"]["default_category"], int)
        

def test_scenario_price_rule_type(facial_care_data):
    """Checks if the price rule is an int"""
    for scenario in facial_care_data["scenarios"].values():
        assert isinstance(scenario["price_rule"], int)

def test_scenario_additional_categories_type(facial_care_data):
     """Checks if additional categories is a list of strings"""
     for scenario in facial_care_data["scenarios"].values():
        for category in scenario["presta_categories"]["additional_categories"]:
            assert isinstance(category, str)


def test_empty_additional_categories(facial_care_data):
    """Checks if additional categories can be empty"""
    for scenario in facial_care_data["scenarios"].values():
       assert scenario["presta_categories"]["additional_categories"] == [""]


def test_all_scenarios_present(facial_care_data):
    """Checks if all the expected scenarios are present."""
    expected_scenarios = {
        "moisture-face",
        "serums",
        "face-masks",
        "facial-cleaning-products",
        "multi-active-series",
        "mineral-peptide"
    }
    assert set(facial_care_data["scenarios"].keys()) == expected_scenarios
```