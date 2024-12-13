```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def hair_treatment_data():
    """Loads the hair treatment data from the JSON file."""
    # Since the prompt does not provide the file reading part, we simulate that
    json_content = """
    {
      "scenarios": {
        "complementary-products": {
    
          "url": "https://hbdeadsea.co.il/product-category/hair-treatment/complementary-products/",
          "name": "מוצרי טיפוח משלימים",
          "condition": "new",
          "presta_categories": {
            "default_category": {
              "11111": "presta_category"
            },
            "additional_categories": [
              ""
            ]
          }
        },
    
        "url": "https://hbdeadsea.co.il/product-category/hair-treatment/",
        "name": "טיפוח השיער",
        "condition": [
          "new"
        ],
        "presta_categories": {
          "default_category": {
            "11111": "presta_category"
          },
          "additional_categories": [
            ""
          ]
        },
        "shampoo-conditioner": {
    
          "url": "https://hbdeadsea.co.il/product-category/hair-treatment/shampoo-conditioner/",
          "name": "שמפו ומרכך",
          "condition": "new",
          "presta_categories": {
            "default_category": {
              "11111": "presta_category"
            },
            "additional_categories": [
              ""
            ]
          }
        },
        "cratin-series": {
    
          "url": "https://hbdeadsea.co.il/product-category/hair-treatment/cratin-series/",
          "name": "סדרת קרטין",
          "condition": "new",
          "presta_categories": {
            "default_category": 11111,
            "additional_categories": [
              ""
            ]
          }
        },
        "hair-masks": {
    
          "url": "https://hbdeadsea.co.il/product-category/hair-treatment/hair-masks/",
          "name": "מסכות לשיער",
          "condition": "new",
          "presta_categories": {
            "default_category": 11111,
            "additional_categories": [
              ""
            ]
          }
        }
      }
    }
    """
    return json.loads(json_content)



def test_complementary_products_scenario(hair_treatment_data):
    """Test the 'complementary-products' scenario."""
    scenario = hair_treatment_data["scenarios"].get("complementary-products")
    assert scenario is not None
    assert scenario["url"] == "https://hbdeadsea.co.il/product-category/hair-treatment/complementary-products/"
    assert scenario["name"] == "מוצרי טיפוח משלימים"
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["default_category"] == {"11111": "presta_category"}
    assert scenario["presta_categories"]["additional_categories"] == [""]

def test_main_hair_treatment_scenario(hair_treatment_data):
    """Test the main 'hair-treatment' scenario."""
    scenario = hair_treatment_data["scenarios"].get("url")
    assert scenario is not None
    assert scenario == "https://hbdeadsea.co.il/product-category/hair-treatment/"
    
    scenario = hair_treatment_data["scenarios"].get("name")
    assert scenario == "טיפוח השיער"

    scenario = hair_treatment_data["scenarios"].get("condition")
    assert scenario ==  ["new"]


    scenario = hair_treatment_data["scenarios"].get("presta_categories")
    assert scenario["default_category"] == {"11111": "presta_category"}
    assert scenario["additional_categories"] == [""]


def test_shampoo_conditioner_scenario(hair_treatment_data):
    """Test the 'shampoo-conditioner' scenario."""
    scenario = hair_treatment_data["scenarios"].get("shampoo-conditioner")
    assert scenario is not None
    assert scenario["url"] == "https://hbdeadsea.co.il/product-category/hair-treatment/shampoo-conditioner/"
    assert scenario["name"] == "שמפו ומרכך"
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["default_category"] == {"11111": "presta_category"}
    assert scenario["presta_categories"]["additional_categories"] == [""]

def test_cratin_series_scenario(hair_treatment_data):
    """Test the 'cratin-series' scenario."""
    scenario = hair_treatment_data["scenarios"].get("cratin-series")
    assert scenario is not None
    assert scenario["url"] == "https://hbdeadsea.co.il/product-category/hair-treatment/cratin-series/"
    assert scenario["name"] == "סדרת קרטין"
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["default_category"] == 11111
    assert scenario["presta_categories"]["additional_categories"] == [""]

def test_hair_masks_scenario(hair_treatment_data):
    """Test the 'hair-masks' scenario."""
    scenario = hair_treatment_data["scenarios"].get("hair-masks")
    assert scenario is not None
    assert scenario["url"] == "https://hbdeadsea.co.il/product-category/hair-treatment/hair-masks/"
    assert scenario["name"] == "מסכות לשיער"
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"]["default_category"] == 11111
    assert scenario["presta_categories"]["additional_categories"] == [""]

def test_missing_scenario(hair_treatment_data):
    """Test for a scenario that does not exist in the data."""
    scenario = hair_treatment_data["scenarios"].get("non-existent-scenario")
    assert scenario is None

def test_empty_data():
    """Test with empty data, ensuring no errors are raised."""
    empty_data = {"scenarios": {}}
    assert empty_data["scenarios"] == {}

def test_invalid_json_structure():
    """Test with a malformed JSON to ensure it handles it properly (e.g. via exception)."""
    with pytest.raises(json.JSONDecodeError):
        json.loads("{'scenarios':")
```