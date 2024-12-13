```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "EPIX": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..33807",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Fenix 6": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..9393..13927..9392..13929..13930..9391",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Fenix 7": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..32654..32651..32657",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "HRM": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..33807",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Vivo": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..31651..33932..13858..13860..10115..10116",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Venu": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..10117..15956..15955..25643..24313..31738",
          "checkbox": false,
          "active": true,
           "condition":"new",
            "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Lily": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..25048",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Instinct": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..6109..33962",
          "checkbox": false,
          "active": true,
           "condition":"new",
            "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Swim": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..10118",
          "checkbox": false,
          "active": true,
           "condition":"new",
            "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Enduro": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..21932",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        },
        "Forerunner": {
          "brand": "GARMIN",
          "url": "https://ksp.co.il/web/cat/2085..2160..8336..17956..27545..7820..7821..15741..4104..7822",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "3405": "GOOGLE PIXEL PRO",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "6471": "Smartphones",
            "3403": "GOOGLE"
          }
        }
      }
    }
    """
    return json.loads(json_data)


def test_ksp_data_loads_correctly(ksp_data):
    """Checks if the fixture loads the data and if 'scenarios' key exists."""
    assert "scenarios" in ksp_data
    assert isinstance(ksp_data["scenarios"], dict)

def test_scenario_epix_data(ksp_data):
    """Checks if the 'EPIX' scenario data is correct."""
    epix_data = ksp_data["scenarios"]["EPIX"]
    assert epix_data["brand"] == "GARMIN"
    assert epix_data["url"] == "https://ksp.co.il/web/cat/2085..2160..33807"
    assert epix_data["checkbox"] == False
    assert epix_data["active"] == True
    assert epix_data["condition"] == "new"
    assert epix_data["presta_categories"]["3405"] == "GOOGLE PIXEL PRO"


def test_scenario_fenix6_data(ksp_data):
    """Checks if the 'Fenix 6' scenario data is correct."""
    fenix6_data = ksp_data["scenarios"]["Fenix 6"]
    assert fenix6_data["brand"] == "GARMIN"
    assert fenix6_data["url"] == "https://ksp.co.il/web/cat/2085..2160..9393..13927..9392..13929..13930..9391"
    assert fenix6_data["checkbox"] == False
    assert fenix6_data["active"] == True
    assert fenix6_data["condition"] == "new"
    assert fenix6_data["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"


def test_scenario_fenix7_data(ksp_data):
    """Checks if the 'Fenix 7' scenario data is correct."""
    fenix7_data = ksp_data["scenarios"]["Fenix 7"]
    assert fenix7_data["brand"] == "GARMIN"
    assert fenix7_data["url"] == "https://ksp.co.il/web/cat/2085..2160..32654..32651..32657"
    assert fenix7_data["checkbox"] == False
    assert fenix7_data["active"] == True
    assert fenix7_data["condition"] == "new"
    assert fenix7_data["presta_categories"]["3202"] == "computer,smartphone,gaming console,smart device"


def test_scenario_hrm_data(ksp_data):
    """Checks if the 'HRM' scenario data is correct."""
    hrm_data = ksp_data["scenarios"]["HRM"]
    assert hrm_data["brand"] == "GARMIN"
    assert hrm_data["url"] == "https://ksp.co.il/web/cat/2085..2160..33807"
    assert hrm_data["checkbox"] == False
    assert hrm_data["active"] == True
    assert hrm_data["condition"] == "new"
    assert hrm_data["presta_categories"]["6471"] == "Smartphones"


def test_scenario_vivo_data(ksp_data):
    """Checks if the 'Vivo' scenario data is correct."""
    vivo_data = ksp_data["scenarios"]["Vivo"]
    assert vivo_data["brand"] == "GARMIN"
    assert vivo_data["url"] == "https://ksp.co.il/web/cat/2085..2160..31651..33932..13858..13860..10115..10116"
    assert vivo_data["checkbox"] == False
    assert vivo_data["active"] == True
    assert vivo_data["condition"] == "new"
    assert vivo_data["presta_categories"]["3403"] == "GOOGLE"


def test_scenario_venu_data(ksp_data):
    """Checks if the 'Venu' scenario data is correct."""
    venu_data = ksp_data["scenarios"]["Venu"]
    assert venu_data["brand"] == "GARMIN"
    assert venu_data["url"] == "https://ksp.co.il/web/cat/2085..2160..10117..15956..15955..25643..24313..31738"
    assert venu_data["checkbox"] == False
    assert venu_data["active"] == True
    assert venu_data["condition"] == "new"


def test_scenario_lily_data(ksp_data):
    """Checks if the 'Lily' scenario data is correct."""
    lily_data = ksp_data["scenarios"]["Lily"]
    assert lily_data["brand"] == "GARMIN"
    assert lily_data["url"] == "https://ksp.co.il/web/cat/2085..2160..25048"
    assert lily_data["checkbox"] == False
    assert lily_data["active"] == True
    assert lily_data["condition"] == "new"

def test_scenario_instinct_data(ksp_data):
    """Checks if the 'Instinct' scenario data is correct."""
    instinct_data = ksp_data["scenarios"]["Instinct"]
    assert instinct_data["brand"] == "GARMIN"
    assert instinct_data["url"] == "https://ksp.co.il/web/cat/2085..2160..6109..33962"
    assert instinct_data["checkbox"] == False
    assert instinct_data["active"] == True
    assert instinct_data["condition"] == "new"

def test_scenario_swim_data(ksp_data):
    """Checks if the 'Swim' scenario data is correct."""
    swim_data = ksp_data["scenarios"]["Swim"]
    assert swim_data["brand"] == "GARMIN"
    assert swim_data["url"] == "https://ksp.co.il/web/cat/2085..2160..10118"
    assert swim_data["checkbox"] == False
    assert swim_data["active"] == True
    assert swim_data["condition"] == "new"

def test_scenario_enduro_data(ksp_data):
    """Checks if the 'Enduro' scenario data is correct."""
    enduro_data = ksp_data["scenarios"]["Enduro"]
    assert enduro_data["brand"] == "GARMIN"
    assert enduro_data["url"] == "https://ksp.co.il/web/cat/2085..2160..21932"
    assert enduro_data["checkbox"] == False
    assert enduro_data["active"] == True
    assert enduro_data["condition"] == "new"

def test_scenario_forerunner_data(ksp_data):
    """Checks if the 'Forerunner' scenario data is correct."""
    forerunner_data = ksp_data["scenarios"]["Forerunner"]
    assert forerunner_data["brand"] == "GARMIN"
    assert forerunner_data["url"] == "https://ksp.co.il/web/cat/2085..2160..8336..17956..27545..7820..7821..15741..4104..7822"
    assert forerunner_data["checkbox"] == False
    assert forerunner_data["active"] == True
    assert forerunner_data["condition"] == "new"


def test_all_scenarios_have_expected_keys(ksp_data):
    """Checks if all scenarios have the expected keys."""
    expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        for key in expected_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing key '{key}'"

def test_all_scenarios_brand_is_garmin(ksp_data):
    """Checks if the brand is garmin for all the scenarios"""
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert scenario_data["brand"] == "GARMIN", f"Scenario '{scenario_name}' has wrong brand"

def test_all_scenarios_checkbox_is_false(ksp_data):
    """Checks if the checkbox is false for all the scenarios"""
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' has wrong checkbox value"


def test_all_scenarios_active_is_true(ksp_data):
    """Checks if the active is true for all the scenarios"""
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
         assert scenario_data["active"] == True, f"Scenario '{scenario_name}' has wrong active value"

def test_all_scenarios_condition_is_new(ksp_data):
    """Checks if the condition is new for all the scenarios"""
    for scenario_name, scenario_data in ksp_data["scenarios"].items():
         assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' has wrong condition value"
```