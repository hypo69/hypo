```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_asus_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "Asus Zenfone 8": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/573..1358..24585",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "asus": "ZENFONE 8" }
          }
        },
        "Asus Zenfone 9": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/573..1358..40840",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "asus": "ZENFONE 9" }
          }
        },
        "Asus ROG Phone 6": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/573..1358..40085",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "asus": "ROGFONE 6" }
          }
        },
        "ROGFONE 6 PRO": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/573..1358..43737",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "asus": "ROGFONE 6 PRO" }
          }
        },
        "ROGFONE 6 PRO BATMAN EDITION": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/573..1358..43370",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "asus": "ROGFONE 6 PRO BATMAN EDITION" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_ksp_asus_data_loaded(ksp_asus_data):
    """
    Checks if the data is loaded correctly and is not empty.
    """
    assert ksp_asus_data is not None
    assert "scenarios" in ksp_asus_data
    assert len(ksp_asus_data["scenarios"]) > 0


def test_ksp_asus_scenario_zenfone8_data(ksp_asus_data):
    """
    Tests the specific data for "Asus Zenfone 8" scenario.
    Checks for correct brand, URL, checkbox, active status, condition and presta_categories.
    """
    zenfone8_data = ksp_asus_data["scenarios"]["Asus Zenfone 8"]
    assert zenfone8_data["brand"] == "ASUS"
    assert zenfone8_data["url"] == "https://ksp.co.il/web/cat/573..1358..24585"
    assert zenfone8_data["checkbox"] == False
    assert zenfone8_data["active"] == True
    assert zenfone8_data["condition"] == "new"
    assert zenfone8_data["presta_categories"]["template"]["asus"] == "ZENFONE 8"

def test_ksp_asus_scenario_zenfone9_data(ksp_asus_data):
    """
    Tests the specific data for "Asus Zenfone 9" scenario.
     Checks for correct brand, URL, checkbox, active status, condition and presta_categories.
    """
    zenfone9_data = ksp_asus_data["scenarios"]["Asus Zenfone 9"]
    assert zenfone9_data["brand"] == "ASUS"
    assert zenfone9_data["url"] == "https://ksp.co.il/web/cat/573..1358..40840"
    assert zenfone9_data["checkbox"] == False
    assert zenfone9_data["active"] == True
    assert zenfone9_data["condition"] == "new"
    assert zenfone9_data["presta_categories"]["template"]["asus"] == "ZENFONE 9"

def test_ksp_asus_scenario_rogphone6_data(ksp_asus_data):
    """
    Tests the specific data for "Asus ROG Phone 6" scenario.
    Checks for correct brand, URL, checkbox, active status, condition and presta_categories.
    """
    rogphone6_data = ksp_asus_data["scenarios"]["Asus ROG Phone 6"]
    assert rogphone6_data["brand"] == "ASUS"
    assert rogphone6_data["url"] == "https://ksp.co.il/web/cat/573..1358..40085"
    assert rogphone6_data["checkbox"] == False
    assert rogphone6_data["active"] == True
    assert rogphone6_data["condition"] == "new"
    assert rogphone6_data["presta_categories"]["template"]["asus"] == "ROGFONE 6"

def test_ksp_asus_scenario_rogphone6pro_data(ksp_asus_data):
    """
    Tests the specific data for "ROGFONE 6 PRO" scenario.
    Checks for correct brand, URL, checkbox, active status, condition and presta_categories.
    """
    rogphone6pro_data = ksp_asus_data["scenarios"]["ROGFONE 6 PRO"]
    assert rogphone6pro_data["brand"] == "ASUS"
    assert rogphone6pro_data["url"] == "https://ksp.co.il/web/cat/573..1358..43737"
    assert rogphone6pro_data["checkbox"] == False
    assert rogphone6pro_data["active"] == True
    assert rogphone6pro_data["condition"] == "new"
    assert rogphone6pro_data["presta_categories"]["template"]["asus"] == "ROGFONE 6 PRO"


def test_ksp_asus_scenario_rogphone6pro_batman_data(ksp_asus_data):
    """
    Tests the specific data for "ROGFONE 6 PRO BATMAN EDITION" scenario.
    Checks for correct brand, URL, checkbox, active status, condition and presta_categories.
    """
    rogphone6pro_batman_data = ksp_asus_data["scenarios"]["ROGFONE 6 PRO BATMAN EDITION"]
    assert rogphone6pro_batman_data["brand"] == "ASUS"
    assert rogphone6pro_batman_data["url"] == "https://ksp.co.il/web/cat/573..1358..43370"
    assert rogphone6pro_batman_data["checkbox"] == False
    assert rogphone6pro_batman_data["active"] == True
    assert rogphone6pro_batman_data["condition"] == "new"
    assert rogphone6pro_batman_data["presta_categories"]["template"]["asus"] == "ROGFONE 6 PRO BATMAN EDITION"

def test_ksp_asus_scenario_missing_key(ksp_asus_data):
    """
        Test for a scenario with a missing key within one of the scenarios
    """
    with pytest.raises(KeyError):
         _ = ksp_asus_data["scenarios"]["Asus Zenfone 8"]["missing_key"]

def test_ksp_asus_empty_scenarios():
    """
    Tests for empty scenarios object
    """
    empty_data = {"scenarios": {}}
    assert len(empty_data["scenarios"]) == 0
```