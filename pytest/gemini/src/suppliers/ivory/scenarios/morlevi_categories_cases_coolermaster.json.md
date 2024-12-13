```python
import pytest
import json

# Define a fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides test data loaded from the JSON file."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_cases_coolermaster.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for COOLERMASTER MID TOWER scenario
def test_coolermaster_mid_tower_brand(morlevi_categories_data):
    """Checks if the brand is correct for 'COOLERMASTER MID TOWER'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER MID TOWER']
    assert scenario['brand'] == 'COOLER MASTER'

def test_coolermaster_mid_tower_url(morlevi_categories_data):
      """Checks if the URL is correct for 'COOLERMASTER MID TOWER'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER MID TOWER']
      expected_url = "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=540&sort=datafloat2%2Cprice&keyword="
      assert scenario['url'] == expected_url

def test_coolermaster_mid_tower_checkbox(morlevi_categories_data):
    """Checks if the checkbox is false for 'COOLERMASTER MID TOWER'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER MID TOWER']
    assert scenario['checkbox'] == False

def test_coolermaster_mid_tower_active(morlevi_categories_data):
    """Checks if the scenario is active for 'COOLERMASTER MID TOWER'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER MID TOWER']
    assert scenario['active'] == True

def test_coolermaster_mid_tower_condition(morlevi_categories_data):
     """Checks if the condition is new for 'COOLERMASTER MID TOWER'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER MID TOWER']
     assert scenario['condition'] == "new"

def test_coolermaster_mid_tower_presta_categories(morlevi_categories_data):
    """Checks the presta categories for 'COOLERMASTER MID TOWER'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER MID TOWER']
    assert scenario['presta_categories']['template'] == {"cooler master": "MID TOWER"}

# Test cases for COOLERMASTER full tower scenario
def test_coolermaster_full_tower_brand(morlevi_categories_data):
     """Checks if the brand is correct for 'COOLERMASTER full tower'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER full tower']
     assert scenario['brand'] == 'COOLER MASTER'

def test_coolermaster_full_tower_url(morlevi_categories_data):
      """Checks if the URL is correct for 'COOLERMASTER full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER full tower']
      expected_url = "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=541&sort=datafloat2%2Cprice&keyword="
      assert scenario['url'] == expected_url

def test_coolermaster_full_tower_checkbox(morlevi_categories_data):
     """Checks if the checkbox is false for 'COOLERMASTER full tower'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER full tower']
     assert scenario['checkbox'] == False

def test_coolermaster_full_tower_active(morlevi_categories_data):
      """Checks if the scenario is active for 'COOLERMASTER full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER full tower']
      assert scenario['active'] == True

def test_coolermaster_full_tower_condition(morlevi_categories_data):
      """Checks if the condition is new for 'COOLERMASTER full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER full tower']
      assert scenario['condition'] == "new"

def test_coolermaster_full_tower_presta_categories(morlevi_categories_data):
    """Checks the presta categories for 'COOLERMASTER full tower'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER full tower']
    assert scenario['presta_categories']['template'] == {"cooler master": "FULL TOWER"}

# Test cases for COOLERMASTER mini tower scenario
def test_coolermaster_mini_tower_brand(morlevi_categories_data):
     """Checks if the brand is correct for 'COOLERMASTER mini tower'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini tower']
     assert scenario['brand'] == 'COOLER MASTER'

def test_coolermaster_mini_tower_url(morlevi_categories_data):
      """Checks if the URL is correct for 'COOLERMASTER mini tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini tower']
      expected_url = "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=542&sort=datafloat2%2Cprice&keyword="
      assert scenario['url'] == expected_url

def test_coolermaster_mini_tower_checkbox(morlevi_categories_data):
     """Checks if the checkbox is false for 'COOLERMASTER mini tower'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini tower']
     assert scenario['checkbox'] == False

def test_coolermaster_mini_tower_active(morlevi_categories_data):
      """Checks if the scenario is active for 'COOLERMASTER mini tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini tower']
      assert scenario['active'] == True

def test_coolermaster_mini_tower_condition(morlevi_categories_data):
      """Checks if the condition is new for 'COOLERMASTER mini tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini tower']
      assert scenario['condition'] == "new"

def test_coolermaster_mini_tower_presta_categories(morlevi_categories_data):
    """Checks the presta categories for 'COOLERMASTER mini tower'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini tower']
    assert scenario['presta_categories']['template'] == {"cooler master": "MINI TOWER"}

# Test cases for COOLERMASTER gaming MID TOWER scenario
def test_coolermaster_gaming_mid_tower_brand(morlevi_categories_data):
      """Checks if the brand is correct for 'COOLERMASTER gaming MID TOWER'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming MID TOWER']
      assert scenario['brand'] == 'COOLER MASTER'

def test_coolermaster_gaming_mid_tower_url(morlevi_categories_data):
      """Checks if the URL is correct for 'COOLERMASTER gaming MID TOWER'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming MID TOWER']
      expected_url = "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=545&sort=datafloat2%2Cprice&keyword="
      assert scenario['url'] == expected_url

def test_coolermaster_gaming_mid_tower_checkbox(morlevi_categories_data):
      """Checks if the checkbox is false for 'COOLERMASTER gaming MID TOWER'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming MID TOWER']
      assert scenario['checkbox'] == False

def test_coolermaster_gaming_mid_tower_active(morlevi_categories_data):
      """Checks if the scenario is active for 'COOLERMASTER gaming MID TOWER'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming MID TOWER']
      assert scenario['active'] == True

def test_coolermaster_gaming_mid_tower_condition(morlevi_categories_data):
       """Checks if the condition is new for 'COOLERMASTER gaming MID TOWER'."""
       scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming MID TOWER']
       assert scenario['condition'] == "new"

def test_coolermaster_gaming_mid_tower_presta_categories(morlevi_categories_data):
    """Checks the presta categories for 'COOLERMASTER gaming MID TOWER'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming MID TOWER']
    assert scenario['presta_categories']['template'] == {"cooler master": "GAMING MID TOWER"}

# Test cases for COOLERMASTER gaming full tower scenario
def test_coolermaster_gaming_full_tower_brand(morlevi_categories_data):
      """Checks if the brand is correct for 'COOLERMASTER gaming full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming full tower']
      assert scenario['brand'] == 'COOLER MASTER'

def test_coolermaster_gaming_full_tower_url(morlevi_categories_data):
      """Checks if the URL is correct for 'COOLERMASTER gaming full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming full tower']
      expected_url = "----------------------------COOLER MASTER gaming full TOWER--------------------------------"
      assert scenario['url'] == expected_url

def test_coolermaster_gaming_full_tower_checkbox(morlevi_categories_data):
      """Checks if the checkbox is false for 'COOLERMASTER gaming full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming full tower']
      assert scenario['checkbox'] == False

def test_coolermaster_gaming_full_tower_active(morlevi_categories_data):
      """Checks if the scenario is active for 'COOLERMASTER gaming full tower'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming full tower']
      assert scenario['active'] == True

def test_coolermaster_gaming_full_tower_condition(morlevi_categories_data):
        """Checks if the condition is new for 'COOLERMASTER gaming full tower'."""
        scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming full tower']
        assert scenario['condition'] == "new"

def test_coolermaster_gaming_full_tower_presta_categories(morlevi_categories_data):
    """Checks the presta categories for 'COOLERMASTER gaming full tower'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER gaming full tower']
    assert scenario['presta_categories']['template'] == {"cooler master": "GAMING FULL TOWER"}

# Test cases for COOLERMASTER mini itx scenario
def test_coolermaster_mini_itx_brand(morlevi_categories_data):
     """Checks if the brand is correct for 'COOLERMASTER mini itx'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini itx']
     assert scenario['brand'] == 'COOLER MASTER'

def test_coolermaster_mini_itx_url(morlevi_categories_data):
      """Checks if the URL is correct for 'COOLERMASTER mini itx'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini itx']
      expected_url = "https://www.morlevi.co.il/Cat/285?p_124=3527&sort=datafloat2%2Cprice&keyword="
      assert scenario['url'] == expected_url

def test_coolermaster_mini_itx_checkbox(morlevi_categories_data):
     """Checks if the checkbox is false for 'COOLERMASTER mini itx'."""
     scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini itx']
     assert scenario['checkbox'] == False

def test_coolermaster_mini_itx_active(morlevi_categories_data):
      """Checks if the scenario is active for 'COOLERMASTER mini itx'."""
      scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini itx']
      assert scenario['active'] == True

def test_coolermaster_mini_itx_condition(morlevi_categories_data):
        """Checks if the condition is new for 'COOLERMASTER mini itx'."""
        scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini itx']
        assert scenario['condition'] == "new"

def test_coolermaster_mini_itx_presta_categories(morlevi_categories_data):
    """Checks the presta categories for 'COOLERMASTER mini itx'."""
    scenario = morlevi_categories_data['scenarios']['COOLERMASTER mini itx']
    assert scenario['presta_categories']['template'] == {"cooler master": "MINI ITX"}
```