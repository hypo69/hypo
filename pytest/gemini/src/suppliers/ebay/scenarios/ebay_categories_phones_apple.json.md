```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ebay_data():
    """Provides the ebay categories data as a dictionary."""
    json_data = """
    {
      "scenarios": {
        "iPhone XS MAX": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520XS%2520Max",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone XS MAX" }
          },
          "product combinations": [ "bundle", "color" ]
        },
        "iPhone XS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520XS",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone XS" }
          },
          "product combinations": [ "bundle", "color" ]
        },
        "iPhone XR": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520XR",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone XR" }
          },
          "product combinations": [ "bundle", "color" ]
        },
        "iPhone X": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520X",
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone X" }
          },
          "product combinations": [ "bundle", "color" ]
        },
        "iPhone SE 2022": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520SE%2520%25283rd%2520Generation%2529",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone SE 2022" }
          }
        },
        "iPhone SE 2020": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520SE%2520%25282nd%2520Generation%2529",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone SE 2020" }
          }
        },
        "iPhone SE": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%2520SE",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone SE 2022" }
          }
        },
        "iPhone 1ST GENERATION": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 1ST GENERATION" }
          }
        },
        "iPhone 11": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 11" }
          }
        },
        "iPhone 11 PRO": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011%2520Pro",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 11 PRO" }
          }
        },
        "iPhone 11 PRO MAX": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252011%2520Pro%2520Max",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 11 PRO MAX" }
          }
        },
        "iPhone 12": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 12" }
          }
        },
        "iPhone 12 MINI": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012%2520mini",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 12 MINI" }
          }
        },
        "iPhone 12 PRO": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012%2520Pro",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 12 PRO" }
          }
        },
        "iPhone 12 PRO MAX": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252012%2520Pro",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 12 PRO MAX" }
          }
        },
        "iPhone 13": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 13" }
          }
        },
        "iPhone 13 MINI": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013%2520mini",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 MINI" }
          }
        },
        "iPhone 13 PRO": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013%2520Pro",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 PRO" }
          }
        },
        "iPhone 13 PRO MAX": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252013%2520Pro%2520Max",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 13 PRO MAX" }
          }
        },
        "iPhone 14": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 14" }
          }
        },
        "iPhone 14 PLUS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014%2520Plus",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 14 PLUS" }
          }
        },
        "iPhone 14 PRO": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014%2520Pro",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 14 PRO" }
          }
        },
        "iPhone 14 PRO MAX": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%252014%2520Pro%2520Max",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 14 PRO MAX" }
          }
        },
          "iPhone 3G": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25203G",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 3G" }
          }
        },
        "iPhone 3GS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25203GS",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 3GS" }
          }
        },
        "iPhone 4": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25204",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 4" }
          }
        },
        "iPhone 4S": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25204s",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 4S" }
          }
        },
        "iPhone 5": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25205",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 5" }
          }
        },
        "iPhone 5C": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25205c",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 5C" }
          }
        },
           "iPhone 5S": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25205s",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 5S" }
          }
        },
        "iPhone 6": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_fsrp=1&LH_FS=1&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&rt=nc&Model=Apple%2520iPhone%25206&_oaa=1&_dcat=9355",
          "checkbox": false,
          "active": true,
          "condition": "new",
           "presta_categories": {
            "template": { "apple": "iPhone 6" }
          }
        },
        "iPhone 6 PLUS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25206%2520Plus",
          "checkbox": false,
          "active": true,
          "condition": "new",
           "presta_categories": {
            "template": { "apple": "iPhone 6 PLUS" }
          }
        },
        "iPhone 6S": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_fsrp=1&LH_FS=1&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&rt=nc&Model=Apple%2520iPhone%25206s&_oaa=1&_dcat=9355",
          "checkbox": false,
          "active": true,
          "condition": "new",
           "presta_categories": {
            "template": { "apple": "iPhone 6S" }
          }
        },
        "iPhone 6S PLUS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_fsrp=1&LH_FS=1&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&rt=nc&Model=Apple%2520iPhone%25206s%2520Plus&_oaa=1&_dcat=9355",
          "checkbox": false,
          "active": true,
          "condition": "new",
           "presta_categories": {
            "template": { "apple": "iPhone 6S PLUS" }
          }
        },
        "iPhone 7": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25207",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 7" }
          }
        },
          "iPhone 7 PLUS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25207%2520Plus",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 7 PLUS" }
          }
        },
        "iPhone 8": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25208",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 8" }
          }
        },
         "iPhone 8 PLUS": {
          "brand": "APPLE",
          "url": "https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&LH_FS=1&rt=nc&_from=R40&LH_TitleDesc=0&_nkw=Iphone&_sacat=0&Network=Unlocked&Model=Apple%2520iPhone%25208%2520Plus",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": { "apple": "iPhone 8 PLUS" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_ebay_data_structure(ebay_data):
    """
    Test if the loaded data is a dictionary and has the 'scenarios' key.
    """
    assert isinstance(ebay_data, dict)
    assert "scenarios" in ebay_data

def test_scenario_keys(ebay_data):
    """
    Test if each scenario has the necessary keys.
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_presta_categories_structure(ebay_data):
    """
    Test if 'presta_categories' has the correct structure.
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)

def test_active_is_boolean(ebay_data):
    """
    Test if the 'active' field is a boolean.
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool)

def test_condition_is_string(ebay_data):
    """
    Test if the 'condition' field is a string.
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str)

def test_brand_is_string(ebay_data):
    """
    Test if the 'brand' field is a string.
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str)

def test_url_is_string(ebay_data):
    """
    Test if the 'url' field is a string.
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)


def test_product_combinations_is_list(ebay_data):
    """
    Test if 'product combinations' is a list when present
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        if "product combinations" in scenario_data:
           assert isinstance(scenario_data["product combinations"], list)

def test_checkbox_is_boolean_when_present(ebay_data):
    """
    Test if 'checkbox' is boolean when present
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        if "checkbox" in scenario_data:
            assert isinstance(scenario_data["checkbox"], bool)

def test_scenario_data_is_dict(ebay_data):
    """
     Test if scenario data is a dictionary
    """
    for scenario_name, scenario_data in ebay_data["scenarios"].items():
        assert isinstance(scenario_data, dict)

def test_empty_scenario_name(ebay_data):
     """
     Test if any scenario name is an empty string
     """
     for scenario_name, _ in ebay_data["scenarios"].items():
        assert scenario_name != ""
```