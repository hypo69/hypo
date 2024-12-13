```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_monitors_philips-----.json"
    with open(file_path, 'r') as file:
        return json.load(file)

# Test to ensure data is loaded correctly
def test_data_loaded(morlevi_data):
    """Checks if the data fixture loads the JSON data correctly."""
    assert "scenarios" in morlevi_data
    assert isinstance(morlevi_data["scenarios"], dict)
    assert len(morlevi_data["scenarios"]) > 0

# Test for the PHILIPS 22 scenario
def test_philips_22_scenario(morlevi_data):
    """Checks the attributes of the PHILIPS 22 scenario."""
    scenario = morlevi_data["scenarios"].get("PHILIPS 22")
    assert scenario is not None
    assert scenario["brand"] == "PHILIPS"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1805&p_75=289&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "127,128,526"


# Test for the PHILIPS 24-25 scenario
def test_philips_24_25_scenario(morlevi_data):
    """Checks the attributes of the PHILIPS 24-25 scenario."""
    scenario = morlevi_data["scenarios"].get("PHILIPS 24-25")
    assert scenario is not None
    assert scenario["brand"] == "PHILIPS"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1807&p_75=483&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "127,129,526"

# Test for the PHILIPS 27-29 scenario
def test_philips_27_29_scenario(morlevi_data):
    """Checks the attributes of the PHILIPS 27-29 scenario."""
    scenario = morlevi_data["scenarios"].get("PHILIPS 27-29")
    assert scenario is not None
    assert scenario["brand"] == "PHILIPS"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1808&p_75=297&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "127,130,526"


# Test for the PHILIPS 32 scenario
def test_philips_32_scenario(morlevi_data):
    """Checks the attributes of the PHILIPS 32 scenario."""
    scenario = morlevi_data["scenarios"].get("PHILIPS 32")
    assert scenario is not None
    assert scenario["brand"] == "PHILIPS"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_315=26&p_350=1809&p_75=298&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "127,131,526"

# Test for the PHILIPS 34 scenario
def test_philips_34_scenario(morlevi_data):
    """Checks the attributes of the PHILIPS 34 scenario."""
    scenario = morlevi_data["scenarios"].get("PHILIPS 34")
    assert scenario is not None
    assert scenario["brand"] == "PHILIPS"
    assert scenario["url"] == " --------------------------  PHILIPS 34 -----------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "127,132,526"

# Test for the PHILIPS 49 scenario
def test_philips_49_scenario(morlevi_data):
    """Checks the attributes of the PHILIPS 49 scenario."""
    scenario = morlevi_data["scenarios"].get("PHILIPS 49")
    assert scenario is not None
    assert scenario["brand"] == "PHILIPS"
    assert scenario["url"] == "-----------------------------  PHILIPS 49 ---------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "127,133,526"

# Test for non existent scenario
def test_nonexistent_scenario(morlevi_data):
    """Checks if a non-existent scenario returns None."""
    scenario = morlevi_data["scenarios"].get("NonExistentScenario")
    assert scenario is None
```