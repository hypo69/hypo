```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Provides the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "Apple Watch SE": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/2085..245..29185..28724",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          },
          "price_rule": 1,
          "combinations": {
            "size:select": "40 mm",
            "color:color": "black",
            "reseller:select": "Autorized Reseller",
            "importer:select": "Official Importer",
            "warranty:select": "1 year"
          }
        },
        "Apple Watch Series 7": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/245..2085..29150..29229",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
             "3403": "GOOGLE"
          },
          "price_rule": 1,
          "combinations": {
            "size:select": "40 mm",
            "color:color": "black",
            "reseller:select": "Autorized Reseller",
            "importer:select": "Official Importer",
            "warranty:select": "1 year"
          }
        },
        "Apple Watch Series 6": {
          "brand": "APPLE",
          "url": "https://ksp.co.il/web/cat/2085..245..16121",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          },
          "price_rule": 1,
          "combinations": {
            "size:select": "40 mm",
            "color:color:": "black",
            "reseller:select": "Autorized Reseller",
            "importer:select": "Official Importer",
            "warranty:select": "1 year"
          }
        }
      }
    }
    """
    return json.loads(json_data)

# Test for the structure of the JSON data
def test_ksp_categories_structure(ksp_categories_data):
    """
    Verifies the structure of the loaded JSON data.
    Checks if the data has a 'scenarios' key,
    and if 'scenarios' is a dictionary.
    """
    assert "scenarios" in ksp_categories_data
    assert isinstance(ksp_categories_data["scenarios"], dict)

# Test case for correct brand for "Apple Watch SE"
def test_apple_watch_se_brand(ksp_categories_data):
    """
     Test case for correct brand for "Apple Watch SE"
    """
    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["brand"] == "APPLE"

# Test case for correct url for "Apple Watch SE"
def test_apple_watch_se_url(ksp_categories_data):
    """
     Test case for correct url for "Apple Watch SE"
    """
    expected_url = "https://ksp.co.il/web/cat/2085..245..29185..28724"
    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["url"] == expected_url


# Test case for "Apple Watch SE" active status
def test_apple_watch_se_active(ksp_categories_data):
    """
    Test case for "Apple Watch SE" active status
    """
    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["active"] is True

# Test case for "Apple Watch SE" checkbox status
def test_apple_watch_se_checkbox(ksp_categories_data):
     """
     Test case for "Apple Watch SE" checkbox status
    """
     assert ksp_categories_data["scenarios"]["Apple Watch SE"]["checkbox"] is False

# Test case for correct presta_categories for "Apple Watch SE"
def test_apple_watch_se_presta_categories(ksp_categories_data):
    """
    Test case for correct presta_categories for "Apple Watch SE"
    """
    expected_presta_categories = {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
             "3403": "GOOGLE"
        }

    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["presta_categories"] == expected_presta_categories

# Test case for "Apple Watch SE" price_rule
def test_apple_watch_se_price_rule(ksp_categories_data):
    """
    Test case for "Apple Watch SE" price_rule
    """
    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["price_rule"] == 1


# Test case for correct combinations for "Apple Watch SE"
def test_apple_watch_se_combinations(ksp_categories_data):
    """
    Test case for correct combinations for "Apple Watch SE"
    """
    expected_combinations = {
        "size:select": "40 mm",
        "color:color": "black",
        "reseller:select": "Autorized Reseller",
        "importer:select": "Official Importer",
        "warranty:select": "1 year"
    }
    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["combinations"] == expected_combinations



# Test case for correct brand for "Apple Watch Series 7"
def test_apple_watch_series_7_brand(ksp_categories_data):
    """
    Test case for correct brand for "Apple Watch Series 7"
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["brand"] == "APPLE"

# Test case for correct url for "Apple Watch Series 7"
def test_apple_watch_series_7_url(ksp_categories_data):
    """
    Test case for correct url for "Apple Watch Series 7"
    """
    expected_url = "https://ksp.co.il/web/cat/245..2085..29150..29229"
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["url"] == expected_url

# Test case for "Apple Watch Series 7" active status
def test_apple_watch_series_7_active(ksp_categories_data):
    """
     Test case for "Apple Watch Series 7" active status
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["active"] is True

# Test case for "Apple Watch Series 7" checkbox status
def test_apple_watch_series_7_checkbox(ksp_categories_data):
    """
     Test case for "Apple Watch Series 7" checkbox status
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["checkbox"] is False


# Test case for correct presta_categories for "Apple Watch Series 7"
def test_apple_watch_series_7_presta_categories(ksp_categories_data):
    """
    Test case for correct presta_categories for "Apple Watch Series 7"
    """
    expected_presta_categories = {
             "3405": "GOOGLE PIXEL PRO",
             "3198": "CONSUMER ELECTRONICS",
             "3202": "computer,smartphone,gaming console,smart device",
             "6471": "Smartphones",
              "3403": "GOOGLE"
        }
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["presta_categories"] == expected_presta_categories

# Test case for "Apple Watch Series 7" price_rule
def test_apple_watch_series_7_price_rule(ksp_categories_data):
    """
    Test case for "Apple Watch Series 7" price_rule
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["price_rule"] == 1

# Test case for correct combinations for "Apple Watch Series 7"
def test_apple_watch_series_7_combinations(ksp_categories_data):
    """
    Test case for correct combinations for "Apple Watch Series 7"
    """
    expected_combinations = {
        "size:select": "40 mm",
        "color:color": "black",
        "reseller:select": "Autorized Reseller",
        "importer:select": "Official Importer",
        "warranty:select": "1 year"
    }
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["combinations"] == expected_combinations

# Test case for correct brand for "Apple Watch Series 6"
def test_apple_watch_series_6_brand(ksp_categories_data):
    """
    Test case for correct brand for "Apple Watch Series 6"
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["brand"] == "APPLE"

# Test case for correct url for "Apple Watch Series 6"
def test_apple_watch_series_6_url(ksp_categories_data):
    """
    Test case for correct url for "Apple Watch Series 6"
    """
    expected_url = "https://ksp.co.il/web/cat/2085..245..16121"
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["url"] == expected_url

# Test case for "Apple Watch Series 6" active status
def test_apple_watch_series_6_active(ksp_categories_data):
    """
    Test case for "Apple Watch Series 6" active status
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["active"] is True


# Test case for "Apple Watch Series 6" checkbox status
def test_apple_watch_series_6_checkbox(ksp_categories_data):
    """
    Test case for "Apple Watch Series 6" checkbox status
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["checkbox"] is False

# Test case for correct presta_categories for "Apple Watch Series 6"
def test_apple_watch_series_6_presta_categories(ksp_categories_data):
    """
    Test case for correct presta_categories for "Apple Watch Series 6"
    """
    expected_presta_categories = {
          "3405": "GOOGLE PIXEL PRO",
           "3198": "CONSUMER ELECTRONICS",
           "3202": "computer,smartphone,gaming console,smart device",
           "6471": "Smartphones",
          "3403": "GOOGLE"
        }
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["presta_categories"] == expected_presta_categories

# Test case for "Apple Watch Series 6" price_rule
def test_apple_watch_series_6_price_rule(ksp_categories_data):
    """
    Test case for "Apple Watch Series 6" price_rule
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["price_rule"] == 1

# Test case for correct combinations for "Apple Watch Series 6"
def test_apple_watch_series_6_combinations(ksp_categories_data):
    """
    Test case for correct combinations for "Apple Watch Series 6"
    """
    expected_combinations = {
        "size:select": "40 mm",
        "color:color:": "black",
        "reseller:select": "Autorized Reseller",
        "importer:select": "Official Importer",
        "warranty:select": "1 year"
    }
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["combinations"] == expected_combinations

#Test case for the condition
def test_apple_watch_condition(ksp_categories_data):
    """
    Test case for the condition
    """
    assert ksp_categories_data["scenarios"]["Apple Watch Series 6"]["condition"] == "new"
    assert ksp_categories_data["scenarios"]["Apple Watch Series 7"]["condition"] == "new"
    assert ksp_categories_data["scenarios"]["Apple Watch SE"]["condition"] == "new"
```