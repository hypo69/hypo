```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def grandadvance_categories_data():
    """Provides the JSON data as a dictionary."""
    json_data = """
    {
      "MOTHERBOARD socket 1200": {
        "brand": "MSI",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=785&manId=69",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "56,57,59"
      },
      "MOTHERBOARD socket 1151": {
        "brand": "MSI",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=733&manId=69",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "56,57,60"
      },
      "MOTHERBOARD socket 2066": {
        "brand": "MSI",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=766&manId=69",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "56,57,62"
      },
      "MOTHERBOARD socket AM4": {
        "brand": "MSI",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=758&manId=69",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "56,57,58"
      },
      "MOTHERBOARD socket TR4": {
        "brand": "MSI",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=758&manId=69",
        "checkbox": false,
        "active": true, "condition":"new","presta_categories": "56,57,58"
      }
    }
    """
    return json.loads(json_data)


def test_motherboard_socket_1200_data(grandadvance_categories_data):
    """Checks the data for 'MOTHERBOARD socket 1200'."""
    data = grandadvance_categories_data["MOTHERBOARD socket 1200"]
    assert data["brand"] == "MSI"
    assert data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=785&manId=69"
    assert data["checkbox"] == False
    assert data["active"] == True
    assert data["condition"] == "new"
    assert data["presta_categories"] == "56,57,59"

def test_motherboard_socket_1151_data(grandadvance_categories_data):
    """Checks the data for 'MOTHERBOARD socket 1151'."""
    data = grandadvance_categories_data["MOTHERBOARD socket 1151"]
    assert data["brand"] == "MSI"
    assert data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=733&manId=69"
    assert data["checkbox"] == False
    assert data["active"] == True
    assert data["condition"] == "new"
    assert data["presta_categories"] == "56,57,60"


def test_motherboard_socket_2066_data(grandadvance_categories_data):
    """Checks the data for 'MOTHERBOARD socket 2066'."""
    data = grandadvance_categories_data["MOTHERBOARD socket 2066"]
    assert data["brand"] == "MSI"
    assert data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=766&manId=69"
    assert data["checkbox"] == False
    assert data["active"] == True
    assert data["condition"] == "new"
    assert data["presta_categories"] == "56,57,62"


def test_motherboard_socket_am4_data(grandadvance_categories_data):
    """Checks the data for 'MOTHERBOARD socket AM4'."""
    data = grandadvance_categories_data["MOTHERBOARD socket AM4"]
    assert data["brand"] == "MSI"
    assert data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=758&manId=69"
    assert data["checkbox"] == False
    assert data["active"] == True
    assert data["condition"] == "new"
    assert data["presta_categories"] == "56,57,58"

def test_motherboard_socket_tr4_data(grandadvance_categories_data):
    """Checks the data for 'MOTHERBOARD socket TR4'."""
    data = grandadvance_categories_data["MOTHERBOARD socket TR4"]
    assert data["brand"] == "MSI"
    assert data["url"] == "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=758&manId=69"
    assert data["checkbox"] == False
    assert data["active"] == True
    assert data["condition"] == "new"
    assert data["presta_categories"] == "56,57,58"


def test_all_motherboard_have_msi_brand(grandadvance_categories_data):
    """Checks if all motherboards have the 'MSI' brand."""
    for motherboard in grandadvance_categories_data.values():
        assert motherboard["brand"] == "MSI"


def test_all_motherboard_are_active(grandadvance_categories_data):
    """Checks if all motherboards are marked as active."""
    for motherboard in grandadvance_categories_data.values():
        assert motherboard["active"] == True

def test_all_motherboard_are_new(grandadvance_categories_data):
    """Checks if all motherboards are marked as new."""
    for motherboard in grandadvance_categories_data.values():
        assert motherboard["condition"] == "new"


def test_all_motherboard_have_checkbox_false(grandadvance_categories_data):
        """Checks if all motherboards have checkbox set to False."""
        for motherboard in grandadvance_categories_data.values():
            assert motherboard["checkbox"] == False

def test_presta_categories_is_string(grandadvance_categories_data):
    """Checks that presta_categories is a string for all motherboards."""
    for motherboard in grandadvance_categories_data.values():
      assert isinstance(motherboard["presta_categories"], str)
```