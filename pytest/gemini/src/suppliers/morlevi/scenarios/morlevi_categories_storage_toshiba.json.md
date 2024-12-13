```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the morlevi categories data from the json."""
    json_data = """
    {
      "scenarios": {
        "internal_ssd_sata_3 120-128GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_128",
          "url": "---------------------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "117,118,134"
        },
        "internal_ssd_sata_3 240-256GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_256",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "117,118,135"
        },
        "internal_ssd_sata_3 480-525GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_512",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,118,136"
        },
        "internal_ssd_sata_3 960GB-1TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_1tb",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,118,137"
        },
        "internal_ssd_sata_3 2TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_2tb",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,118,138"
        },
        "internal_ssd_sata_3 4TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_4tb",
          "url": "------------------------TOSHIBA  internal_ssd_sata_3_4tb---------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,118,139"
        },
        "internal_ssd_sata_3 8TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_8tb",
          "url": "------------------------TOSHIBA  internal_ssd_sata_3_8tb---------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,118,140"
        },
        "internal_ssd_msata 240-256GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_msata_240gb",
          "url": "------------------------TOSHIBA  internal_ssd_msata_240gb---------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,163,164"
        },
        "internal_ssd_m2sata 240-256GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_m2sata_256",
          "url": "------------------------TOSHIBA  internal_ssd_m2sata_256---------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,149"
        },
        "internal_ssd_m2sata 480-525GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_m2sata_256",
          "url": "------------------------TOSHIBA internal_ssd_m2sata_256--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,150"
        },
        "internal_ssd_nvmi 240-256GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvme_256",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,119,141"
        },
        "internal_ssd_nvmi 480-525GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvme_512",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,119,142"
        },
        "internal_ssd_nvmi 960GB-1TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvme_1tb",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,119,143"
        },
        "internal_ssd_nvmi 2TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvme_2tb",
          "url": "-------------------------------TOSHIBA--internal_ssd_nvme_2tb--------------=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,119,144"
        },
        "internal_ssd_nvmi_gen4 240-256GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvmi_gen4_256",
          "url": "------------------------TOSHIBA internal_ssd_nvmi_gen4_256---------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,120,141,165"
        },
        "internal_ssd_nvmi_gen4 480-525GB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvmi_gen4_512",
          "url": "------------------------TOSHIBA internal_ssd_nvmi_gen4_512---------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,120,142,168"
        },
        "internal_ssd_nvmi_gen4 960GB-1TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvmi_gen4_1tb",
          "url": "-------------------------------------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,120,143,169"
        },
        "internal_ssd_nvmi_gen4 2TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_nvmi_gen4_2tb",
          "url": "------------------------TOSHIBA internal_ssd_nvmi_gen4_2tb--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,120,144"
        },
        "external_ssd 500GB": {
          "brand": "TOSHIBA",
          "name": "external_ssd_500GB",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,122,549"
        },
        "external_ssd 1TB": {
          "brand": "TOSHIBA",
          "name": "external_ssd-1TB",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,122,550"
        },
        "external_ssd 2TB": {
          "brand": "TOSHIBA",
          "name": "external_ssd_2TB",
          "url": "--------------------------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,122,551"
        },
        "internal_hdd_35 1TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-1tb",
          "url": "https://www.morlevi.co.il/Cat/49?p_315=35&p_177=839&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,177"
        },
        "internal_hdd_35 2TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-2tb",
          "url": "https://www.morlevi.co.il/Cat/49?p_315=35&p_177=840&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,178"
        },
        "internal_hdd_35 3TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-3tb",
          "url": "https://www.morlevi.co.il/Cat/49?p_315=35&p_177=841&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,179"
        },
        "internal_hdd_35 4TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-4tb",
          "url": "https://www.morlevi.co.il/Cat/49?p_315=35&p_177=842&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,180"
        },
        "internal_hdd_35 6TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-6tb",
          "url": "https://www.morlevi.co.il/Cat/49?p_315=35&p_177=843&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,181"
        },
        "internal_hdd_35 8TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-8tb",
          "url": "https://www.morlevi.co.il/Cat/49?p_315=35&p_177=844&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,182"
        },
        "TOSHIBA internal_hdd_35 10TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-10tb",
          "url": "----------------------------TOSHIBA internal_hdd_35 10TB--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,183"
        },
         "internal_hdd_35 18TB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_35-10tb",
          "url": "----------------------------TOSHIBA internal_hdd_35 18TB--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,123,552"
        },
        "internal_hdd_25 500GB": {
          "brand": "TOSHIBA",
          "name": "internal_hdd_25_480",
          "url": "----------------------------TOSHIBA internal_hdd_25 500GB --------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,124,166"
        },
        "internal_hdd_25 1TB": {
          "brand": "TOSHIBA",
          "name": "internal_ssd_sata_3_1tb",
          "url": "----------------------------TOSHIBA internal_hdd_25 1T --------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,124,167"
        },
         "external_hdd_25 1TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_25-1tb",
          "url": "----------------------------TOSHIBA external_hdd_25 1t --------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,125,184"
        },
        "external_hdd_25 2TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_2tb",
          "url": "----------------------------TOSHIBA external_hdd_25 2t --------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,125,185"
        },
        "external_hdd_25 4TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_25_4tb",
          "url": "----------------------------TOSHIBA external_hdd_25 4t --------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,125,186"
        },
        "external_hdd_25 5TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_25-5tb",
          "url": "----------------------------TOSHIBA external_hdd_25 5t --------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,125,187"
        },
        "external_hdd_35 4TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_35-4tb",
          "url": "------------------------TOSHIBA external_hdd_35--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,126,184"
        },
         "external_hdd_35 6TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_35_6tb",
          "url": "------------------------TOSHIBA external_hdd_35--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,126,185"
        },
        "external_hdd_35 8TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_35_8tb",
          "url": "------------------------TOSHIBA external_hdd_35--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,126,186"
        },
        "external_hdd_35 10TB": {
          "brand": "TOSHIBA",
          "name": "external_hdd_35_10tb",
          "url": "------------------------TOSHIBA external_hdd_35--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "117,126,187"
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test if the loaded data has the 'scenarios' key and it's a dictionary.
    """
    assert 'scenarios' in morlevi_categories_data
    assert isinstance(morlevi_categories_data['scenarios'], dict)

def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test if each scenario in the 'scenarios' dictionary has the required keys.
    """
    required_keys = ['brand', 'name', 'url', 'checkbox', 'active','condition', 'presta_categories']
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert all(key in scenario_data for key in required_keys), f"Scenario '{scenario_name}' is missing some of the required keys: {required_keys}"

def test_morlevi_categories_scenario_values_type(morlevi_categories_data):
    """
    Test if each scenario in the 'scenarios' dictionary has the correct types.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['brand'], str), f"Scenario '{scenario_name}' 'brand' is not a string"
        assert isinstance(scenario_data['name'], str), f"Scenario '{scenario_name}' 'name' is not a string"
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' 'url' is not a string"
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean"
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' 'active' is not a boolean"
        assert isinstance(scenario_data['condition'], str), f"Scenario '{scenario_name}' 'condition' is not a string"
        assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' 'presta_categories' is not a string"

def test_morlevi_categories_scenario_presta_categories_format(morlevi_categories_data):
     """
     Test if each 'presta_categories' is a string of comma-separated integers.
     """
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         presta_categories = scenario_data.get('presta_categories', '')
         categories = presta_categories.split(',')
         for category in categories:
             assert category.strip().isdigit(), f"Scenario '{scenario_name}' has invalid 'presta_categories' format: {presta_categories}. Each category must be an integer."

def test_morlevi_categories_active_values(morlevi_categories_data):
    """
    Test if all 'active' values are booleans.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' 'active' is not a boolean."
        # Add check if active is true (optional)
        assert scenario_data['active'] == True, f"Scenario '{scenario_name}' 'active' is not True"

def test_morlevi_categories_checkbox_values(morlevi_categories_data):
     """
     Test if all 'checkbox' values are booleans
     """
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean."
        assert scenario_data['checkbox'] == False, f"Scenario '{scenario_name}' 'checkbox' is not False"

def test_morlevi_categories_scenario_brand_values(morlevi_categories_data):
    """
    Test if each 'brand' is "TOSHIBA".
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert scenario_data['brand'] == "TOSHIBA", f"Scenario '{scenario_name}' brand is not TOSHIBA"

def test_morlevi_categories_scenario_condition_values(morlevi_categories_data):
    """
    Test if each 'condition' is "new".
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert scenario_data['condition'] == "new", f"Scenario '{scenario_name}' condition is not new"

def test_morlevi_categories_scenario_url_not_empty(morlevi_categories_data):
    """
    Test if each 'url' is not an empty string.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
       assert scenario_data['url'] != "", f"Scenario '{scenario_name}' url is empty string"
```