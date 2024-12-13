```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the json."""
    json_data =  """
    {
      "scenarios": {
        "routers": {
          
          "url": "https://www.morlevi.co.il/Cat/111",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,211"
        },
        "switch": {
          
          "url": "https://www.morlevi.co.il/Cat/141",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,212"
        },
        "access point": {
          
          "url": "https://www.morlevi.co.il/Cat/144",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,213"
        },
        "network cards": {
          
          "url": "https://www.morlevi.co.il/Cat/154",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,214"
        },
        "network-cables": {
          
          "url": "https://www.morlevi.co.il/Cat/192",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,215"
        },
        "nas": {
          
          "url": "https://www.morlevi.co.il/Cat/346",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,216"
        },
    
        "racks": {
          
          "url": "https://www.morlevi.co.il/Cat/198",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "210,217"
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_categories_data_load(morlevi_categories_data):
    """Tests if the data is loaded correctly from json."""
    assert isinstance(morlevi_categories_data, dict)
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)
    
def test_morlevi_category_router_data(morlevi_categories_data):
    """Tests data for the 'routers' category."""
    router_data = morlevi_categories_data["scenarios"]["routers"]
    assert router_data["url"] == "https://www.morlevi.co.il/Cat/111"
    assert router_data["checkbox"] == False
    assert router_data["active"] == True
    assert router_data["condition"] == "new"
    assert router_data["presta_categories"] == "210,211"

def test_morlevi_category_switch_data(morlevi_categories_data):
    """Tests data for the 'switch' category."""
    switch_data = morlevi_categories_data["scenarios"]["switch"]
    assert switch_data["url"] == "https://www.morlevi.co.il/Cat/141"
    assert switch_data["checkbox"] == False
    assert switch_data["active"] == True
    assert switch_data["condition"] == "new"
    assert switch_data["presta_categories"] == "210,212"

def test_morlevi_category_access_point_data(morlevi_categories_data):
     """Tests data for the 'access point' category."""
     access_point_data = morlevi_categories_data["scenarios"]["access point"]
     assert access_point_data["url"] == "https://www.morlevi.co.il/Cat/144"
     assert access_point_data["checkbox"] == False
     assert access_point_data["active"] == True
     assert access_point_data["condition"] == "new"
     assert access_point_data["presta_categories"] == "210,213"

def test_morlevi_category_network_cards_data(morlevi_categories_data):
    """Tests data for the 'network cards' category."""
    network_cards_data = morlevi_categories_data["scenarios"]["network cards"]
    assert network_cards_data["url"] == "https://www.morlevi.co.il/Cat/154"
    assert network_cards_data["checkbox"] == False
    assert network_cards_data["active"] == True
    assert network_cards_data["condition"] == "new"
    assert network_cards_data["presta_categories"] == "210,214"

def test_morlevi_category_network_cables_data(morlevi_categories_data):
    """Tests data for the 'network-cables' category."""
    network_cables_data = morlevi_categories_data["scenarios"]["network-cables"]
    assert network_cables_data["url"] == "https://www.morlevi.co.il/Cat/192"
    assert network_cables_data["checkbox"] == False
    assert network_cables_data["active"] == True
    assert network_cables_data["condition"] == "new"
    assert network_cables_data["presta_categories"] == "210,215"

def test_morlevi_category_nas_data(morlevi_categories_data):
    """Tests data for the 'nas' category."""
    nas_data = morlevi_categories_data["scenarios"]["nas"]
    assert nas_data["url"] == "https://www.morlevi.co.il/Cat/346"
    assert nas_data["checkbox"] == False
    assert nas_data["active"] == True
    assert nas_data["condition"] == "new"
    assert nas_data["presta_categories"] == "210,216"
    
def test_morlevi_category_racks_data(morlevi_categories_data):
    """Tests data for the 'racks' category."""
    racks_data = morlevi_categories_data["scenarios"]["racks"]
    assert racks_data["url"] == "https://www.morlevi.co.il/Cat/198"
    assert racks_data["checkbox"] == False
    assert racks_data["active"] == True
    assert racks_data["condition"] == "new"
    assert racks_data["presta_categories"] == "210,217"

def test_morlevi_scenarios_keys(morlevi_categories_data):
    """Tests if all keys exist in the 'scenarios' dictionary."""
    expected_keys = ["routers", "switch", "access point", "network cards", "network-cables", "nas", "racks"]
    actual_keys = list(morlevi_categories_data["scenarios"].keys())
    assert sorted(actual_keys) == sorted(expected_keys)


def test_morlevi_category_missing_key(morlevi_categories_data):
    """Tests for the missing key in the category."""
    with pytest.raises(KeyError):
        morlevi_categories_data["scenarios"]["non_existing_key"]

def test_morlevi_invalid_json():
        """Test case to check if the loading function will raise exception when json is invalid."""
        invalid_json = '{"scenarios": { "routers" : "wrong"}}'
        with pytest.raises(TypeError):
            json.loads(invalid_json)
```