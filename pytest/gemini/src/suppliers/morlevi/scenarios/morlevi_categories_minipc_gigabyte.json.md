```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Provides test data loaded from the JSON file."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_minipc_gigabyte.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test case for GIGABYTE MINIPC I3 8-9th GEN
def test_gigabyte_minipc_i3_8_9th_gen(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC I3 8-9th GEN' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC I3 8-9th GEN')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=1895&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,160"

# Test case for GIGABYTE MINIPC I3 10th GEN
def test_gigabyte_minipc_i3_10th_gen(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC I3 10th GEN' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC I3 10th GEN')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3447&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,160"

# Test case for GIGABYTE MINIPC I5 8-9th (invalid URL)
def test_gigabyte_minipc_i5_8_9th_invalid_url(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC I5 8-9th' scenario, specifically the invalid URL."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC I5 8-9th')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "--------------------------GIGABYTE MINIPC I5 8-9th-------------------------"
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,161"
    
# Test case for GIGABYTE MINIPC I5 10th
def test_gigabyte_minipc_i5_10th(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC I5 10th' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC I5 10th')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3500&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,161"

# Test case for GIGABYTE MINIPC I7
def test_gigabyte_minipc_i7(morlevi_data):
    """Checks the data for 'GIGABYTE  MINIPC I7' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE  MINIPC I7')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3501&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,162"

# Test case for GIGABYTE MINIPC I9 (invalid URL)
def test_gigabyte_minipc_i9_invalid_url(morlevi_data):
    """Checks the data for 'GIGABYTE  MINIPC I9' scenario, specifically the invalid URL."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE  MINIPC I9')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "-------------GIGABYTE  MINIPC I9---------------- "
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,530"
    
# Test case for GIGABYTE MINIPC AMD (invalid URL)
def test_gigabyte_minipc_amd_invalid_url(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC AMD' scenario, specifically the invalid URL."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC AMD')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "-------------GIGABYTE MINIPC AMD---------------- "
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,531"

# Test case for GIGABYTE MINIPC Celeron
def test_gigabyte_minipc_celeron(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC Celeron' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC Celeron')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3371&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,532"

# Test case for GIGABYTE MINIPC Celeron 2
def test_gigabyte_minipc_celeron_2(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC Celeron 2' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC Celeron 2')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3133&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,532"

# Test case for GIGABYTE MINIPC Pentium
def test_gigabyte_minipc_pentium(morlevi_data):
    """Checks the data for 'GIGABYTE MINIPC Pentium' scenario."""
    scenario = morlevi_data['scenarios'].get('GIGABYTE MINIPC Pentium')
    assert scenario is not None
    assert scenario['brand'] == "GIGABYTE"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3133&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == "new"
    assert scenario['presta_categories'] == "159,532"

# Test case to check if 'scenarios' key exists
def test_scenarios_key_exists(morlevi_data):
    """Checks if the 'scenarios' key exists in the JSON data."""
    assert 'scenarios' in morlevi_data

# Test case for missing scenario
def test_missing_scenario(morlevi_data):
    """Checks if accessing a non-existent scenario returns None."""
    scenario = morlevi_data['scenarios'].get('NON_EXISTENT_SCENARIO')
    assert scenario is None
```