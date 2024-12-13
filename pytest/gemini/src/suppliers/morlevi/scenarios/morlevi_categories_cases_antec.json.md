```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_cases_antec.json data."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_cases_antec.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def test_store_description(morlevi_categories_data):
    """Checks if the store description is loaded correctly."""
    assert morlevi_categories_data["store"]["description"] == "Antec Computer Cases"

def test_store_brand(morlevi_categories_data):
    """Checks if the store brand is loaded correctly."""
    assert morlevi_categories_data["store"]["brand"] == ["ANTEC"]

def test_store_get_store_banners(morlevi_categories_data):
  """Checks if get_store_banners is set to true"""
  assert morlevi_categories_data["store"]["get store banners"] == True


def test_scenario_antec_mid_tower(morlevi_categories_data):
    """Checks the data of the 'ANTEC MID TOWER' scenario."""
    mid_tower = morlevi_categories_data["scenarios"]["ANTEC MID TOWER"]
    assert mid_tower["brand"] == "ANTEC"
    assert mid_tower["url"] == "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=540&sort=datafloat2%2Cprice&keyword="
    assert mid_tower["checkbox"] == False
    assert mid_tower["active"] == True
    assert mid_tower["condition"] == "new"
    assert mid_tower["presta_categories"]["template"]["antec"] == "MID TOWER"

def test_scenario_antec_full_tower(morlevi_categories_data):
    """Checks the data of the 'ANTEC FULL TOWER' scenario."""
    full_tower = morlevi_categories_data["scenarios"]["ANTEC FULL TOWER"]
    assert full_tower["brand"] == "ANTEC"
    assert full_tower["url"] == "----------------------------ANTEC FULL TOWER--------------------------------"
    assert full_tower["checkbox"] == False
    assert full_tower["active"] == True
    assert full_tower["condition"] == "new"
    assert full_tower["presta_categories"]["template"]["antec"] == "FULL TOWER"

def test_scenario_antec_mini_tower(morlevi_categories_data):
    """Checks the data of the 'ANTEC MINI TOWER' scenario."""
    mini_tower = morlevi_categories_data["scenarios"]["ANTEC MINI TOWER"]
    assert mini_tower["brand"] == "ANTEC"
    assert mini_tower["url"] == "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=542&sort=datafloat2%2Cprice&keyword="
    assert mini_tower["checkbox"] == False
    assert mini_tower["active"] == True
    assert mini_tower["condition"] == "new"
    assert mini_tower["presta_categories"]["template"]["antec"] == "MINI TOWER"


def test_scenario_antec_gaming_mid_tower(morlevi_categories_data):
    """Checks the data of the 'ANTEC gaming MID TOWER' scenario."""
    gaming_mid_tower = morlevi_categories_data["scenarios"]["ANTEC gaming MID TOWER"]
    assert gaming_mid_tower["brand"] == "ANTEC"
    assert gaming_mid_tower["url"] == "https://www.morlevi.co.il/Cat/98?p_315=12&p_124=545&sort=datafloat2%2Cprice&keyword="
    assert gaming_mid_tower["checkbox"] == False
    assert gaming_mid_tower["active"] == True
    assert gaming_mid_tower["condition"] == "new"
    assert gaming_mid_tower["presta_categories"]["template"]["antec"] == "MINI TOWER"


def test_scenario_antec_gaming_full_tower(morlevi_categories_data):
    """Checks the data of the 'ANTEC gaming full tower' scenario."""
    gaming_full_tower = morlevi_categories_data["scenarios"]["ANTEC gaming full tower"]
    assert gaming_full_tower["brand"] == "ANTEC"
    assert gaming_full_tower["url"] == "----------------------------ANTEC gaming full TOWER--------------------------------"
    assert gaming_full_tower["checkbox"] == False
    assert gaming_full_tower["active"] == True
    assert gaming_full_tower["condition"] == "new"
    assert gaming_full_tower["presta_categories"]["template"]["antec"] == "MINI TOWER"

def test_scenario_antec_mini_itx(morlevi_categories_data):
    """Checks the data of the 'ANTEC mini itx' scenario."""
    mini_itx = morlevi_categories_data["scenarios"]["ANTEC mini itx"]
    assert mini_itx["brand"] == "ANTEC"
    assert mini_itx["url"] == "----------------------------ANTEC mini itxR--------------------------------"
    assert mini_itx["checkbox"] == False
    assert mini_itx["active"] == True
    assert mini_itx["condition"] == "new"
    assert mini_itx["presta_categories"]["template"]["antec"] == "MINI ITX"


def test_missing_key(morlevi_categories_data):
    """Tests accessing a non-existent key in the loaded data."""
    with pytest.raises(KeyError):
        _ = morlevi_categories_data["non_existent_key"]


def test_empty_file_load():
    """Test loading an empty json file (edge case)."""
    with open('empty.json', 'w') as f:
        f.write("")
    with pytest.raises(json.JSONDecodeError):
      with open('empty.json', 'r') as f:
        json.load(f)


def test_invalid_json_format():
    """Test loading a file that contains invalid json format"""
    with open('invalid.json', 'w') as f:
        f.write('{"key" : "value",}')
    with pytest.raises(json.JSONDecodeError):
      with open('invalid.json', 'r') as f:
        json.load(f)
```