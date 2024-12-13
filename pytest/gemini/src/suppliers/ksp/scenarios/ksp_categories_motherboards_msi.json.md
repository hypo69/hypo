```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_msi_motherboards_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
        "scenarios": {
        
            "MSI Intel-1200 H510": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..23877",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1200 H510" }
            },
            "price_rule": 1
            },
            "MSI Intel-1200 B460": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..12539..13374",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1200 B460" }
            },
            "price_rule": 1
            },
            "MSI Intel-1200 B560": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..12539..23315",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1200 B560" }
            },
            "price_rule": 1
            },
            "MSI Intel-1200 Z590": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..12539..21824",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1200 Z590" }
            },
            "price_rule": 1
            },
            "MSI Intel-1700 Z690": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..29757..29759",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1700 Z690" }
            },
            "price_rule": 1
            },
            "MSI Intel-1700 B660": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..29757..31871",
            "checkbox": false,
            "active": true,
             "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1700 B660" }
            },
            "price_rule": 1
            },
            "MSI Intel-1700 H670": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..29757..31871",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1700 H670" }
            },
            "price_rule": 1
            },
            "MSI Intel-1700 H610": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..52..29757..32570",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
                "template": { "msi": "INTEL 1700 H610" }
            },
            "price_rule": 1
            },
            "MSI AMD AM4 B550": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..202..3951..13789",
            "checkbox": false,
            "active": true,
             "condition":"new",
            "presta_categories": {
                "template": { "msi": "AMD AM4 B550" }
            },
            "price_rule": 1
            },
            "MSI AMD AM4 A520": {
            "brand": "MSI",
            "url": "https://ksp.co.il/web/cat/47..3..202..3951..14715",
            "checkbox": false,
            "active": true,
             "condition":"new",
            "presta_categories": {
                "template": { "msi": "AMD AM4 A520" }
            },
            "price_rule": 1
            }
        }
    }
    """
    return json.loads(json_data)


def test_ksp_msi_motherboards_data_loaded(ksp_msi_motherboards_data):
    """Verify that the JSON data is loaded correctly and is a dictionary."""
    assert isinstance(ksp_msi_motherboards_data, dict)


def test_ksp_msi_motherboards_has_scenarios(ksp_msi_motherboards_data):
    """Verify that the JSON data has a 'scenarios' key."""
    assert "scenarios" in ksp_msi_motherboards_data


def test_ksp_msi_motherboards_scenarios_is_dict(ksp_msi_motherboards_data):
     """Verify that the 'scenarios' value is a dictionary."""
     assert isinstance(ksp_msi_motherboards_data["scenarios"], dict)


def test_ksp_msi_motherboards_scenarios_not_empty(ksp_msi_motherboards_data):
    """Verify that the 'scenarios' dictionary is not empty."""
    assert ksp_msi_motherboards_data["scenarios"]


def test_ksp_msi_motherboards_scenario_has_correct_keys(ksp_msi_motherboards_data):
    """Verify that each scenario has the correct keys."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data
        assert "price_rule" in scenario_data


def test_ksp_msi_motherboards_scenario_brand_is_string(ksp_msi_motherboards_data):
     """Verify that the 'brand' is a string in every scenario."""
     for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str)


def test_ksp_msi_motherboards_scenario_url_is_string(ksp_msi_motherboards_data):
    """Verify that the 'url' is a string in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
         assert isinstance(scenario_data["url"], str)


def test_ksp_msi_motherboards_scenario_checkbox_is_boolean(ksp_msi_motherboards_data):
    """Verify that the 'checkbox' is a boolean in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool)


def test_ksp_msi_motherboards_scenario_active_is_boolean(ksp_msi_motherboards_data):
    """Verify that the 'active' is a boolean in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool)

def test_ksp_msi_motherboards_scenario_condition_is_string(ksp_msi_motherboards_data):
    """Verify that the 'condition' is a string in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str)

def test_ksp_msi_motherboards_scenario_presta_categories_is_dict(ksp_msi_motherboards_data):
    """Verify that 'presta_categories' is a dictionary in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], dict)


def test_ksp_msi_motherboards_scenario_presta_categories_template_is_dict(ksp_msi_motherboards_data):
    """Verify that 'presta_categories' has 'template' key which is a dictionary in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
       assert  isinstance(scenario_data["presta_categories"]["template"],dict)
def test_ksp_msi_motherboards_scenario_price_rule_is_int(ksp_msi_motherboards_data):
    """Verify that 'price_rule' is an integer in every scenario."""
    for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
        assert isinstance(scenario_data["price_rule"], int)


def test_ksp_msi_motherboards_scenario_price_rule_positive(ksp_msi_motherboards_data):
     """Verify that 'price_rule' is positive in every scenario."""
     for scenario_name, scenario_data in ksp_msi_motherboards_data["scenarios"].items():
         assert scenario_data["price_rule"] > 0
```