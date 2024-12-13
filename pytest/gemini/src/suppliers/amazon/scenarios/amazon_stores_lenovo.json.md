```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_store_data():
    """Loads the JSON data for the Amazon store."""
    json_data = """
{
  "store": {
    "store_id": "2C6395BA-C701-4025-9D7E-BAE1BD647EEE",
    "supplier_id": 4534,
    "get store banners": true,
    "description": "LENOVO Official store",
    "about": " ",
    "url": "https://www.amazon.com/-/he/stores/LENOVO/page/2C6395BA-C701-4025-9D7E-BAE1BD647EEE",
    "shop categories page": "",
    "shop categories json file": "",

    "scenarios": {
      "ZenBook": {
        "url": "https://www.amazon.com/stores/page/D844B8DB-D9D3-42D4-8FC2-F2DE0800864B?ingress=2&visitId=7527aa1d-ac4c-46e5-8bec-04f6ae5a2068&ref_=ast_bln",
        "active": true,
        "condition":"new","presta_categories": {
          "6484": "ZENBOOK",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "4167": "Zenbook"
        },
        "checkbox": false,
        "price_rule": 1
      },
      "ROG Gaming": {
        "url": "https://www.amazon.com/stores/page/9FE6FA16-F70F-4905-88E3-63344313BFA9?ingress=2&visitId=132d6aa6-3d21-4d52-8cfa-ef1bf1458a64",
        "active": true,
        "condition":"new","presta_categories": {
          "6484": "ZENBOOK",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "4167": "Zenbook"
        },
        "checkbox": false,
        "price_rule": 1
      },
      "TUF Gaming": {
        "url": "https://www.amazon.com/stores/page/9FE6FA16-F70F-4905-88E3-63344313BFA9?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln",
        "active": true,
        "condition":"new","presta_categories": {
          "6486": "TUF",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "4169": "TUF"
        },
        "checkbox": false,
        "price_rule": 1
      },
      "VIVOBook": {
        "url": "https://www.amazon.com/stores/page/FAEE9EC0-F27B-49D0-90F3-F77A3C09FDB9?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln",
        "active": true,
        "condition":"new","presta_categories": {
          "6486": "VIVOBook",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "4169": "TUF"
        },
        "checkbox": false,
        "price_rule": 1
      },
      "ChromeBook": {
        "url": "https://www.amazon.com/stores/page/FAEE9EC0-F27B-49D0-90F3-F77A3C09FDB9?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln",
        "active": true,
        "condition":"new","presta_categories": {
          "6591": "ChromeBook",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "6589": "ChromeBook"
        },
        "checkbox": false,
        "price_rule": 1
      },
      "Asus ProArt Studiobook": {
        "url": "https://www.amazon.com/stores/page/EE8FF8CD-CC10-4DDF-9F0A-CE4E0E79018C?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln",
        "active": true,
        "condition":"new","presta_categories": {
          "6485": "Asus ProArt Studiobook",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "4168": "ProArt Studiobook"
        },
        "checkbox": false,
        "price_rule": 1
      },

      "Asus ProArt Desktops": {
        "url": "https://www.amazon.com/PD500TC-PH778/dp/B09TLH1B4M?ref_=ast_sto_dp&th=1",
        "active": true,
        "condition":"new","presta_categories": {
          "6485": "Asus ProArt Studiobook",
          "3198": "CONSUMER ELECTRONICS",
          "3202": "computer, gaming console, devices",
          "3225": "notebooks",
          "6482": "Asus",
          "2258": "ASUS",
          "2287": "Laptops",
          "4168": "ProArt Studiobook"
        },
        "checkbox": false,
        "price_rule": 1
      }
    }

  }
}
    """
    return json.loads(json_data)

# Test for the store_id
def test_store_id(amazon_store_data):
    """Verify the store_id is correct."""
    assert amazon_store_data["store"]["store_id"] == "2C6395BA-C701-4025-9D7E-BAE1BD647EEE"

# Test for the supplier_id
def test_supplier_id(amazon_store_data):
    """Verify the supplier_id is correct."""
    assert amazon_store_data["store"]["supplier_id"] == 4534

# Test for 'get store banners'
def test_get_store_banners(amazon_store_data):
     """Verify that 'get store banners' is set to true"""
     assert amazon_store_data["store"]["get store banners"] == True

# Test for store description
def test_store_description(amazon_store_data):
    """Verify the store description is correct."""
    assert amazon_store_data["store"]["description"] == "LENOVO Official store"

# Test for store url
def test_store_url(amazon_store_data):
    """Verify the store URL is correct."""
    assert amazon_store_data["store"]["url"] == "https://www.amazon.com/-/he/stores/LENOVO/page/2C6395BA-C701-4025-9D7E-BAE1BD647EEE"

# Test scenarios
def test_scenarios_exist(amazon_store_data):
    """Verify that the scenarios are present"""
    assert "scenarios" in amazon_store_data["store"]

def test_zenbook_scenario(amazon_store_data):
    """Verify the ZenBook scenario details."""
    zenbook = amazon_store_data["store"]["scenarios"]["ZenBook"]
    assert zenbook["url"] == "https://www.amazon.com/stores/page/D844B8DB-D9D3-42D4-8FC2-F2DE0800864B?ingress=2&visitId=7527aa1d-ac4c-46e5-8bec-04f6ae5a2068&ref_=ast_bln"
    assert zenbook["active"] is True
    assert zenbook["condition"] == "new"
    assert zenbook["presta_categories"]["6484"] == "ZENBOOK"
    assert zenbook["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
    assert zenbook["presta_categories"]["3202"] == "computer, gaming console, devices"
    assert zenbook["presta_categories"]["3225"] == "notebooks"
    assert zenbook["presta_categories"]["6482"] == "Asus"
    assert zenbook["presta_categories"]["2258"] == "ASUS"
    assert zenbook["presta_categories"]["2287"] == "Laptops"
    assert zenbook["presta_categories"]["4167"] == "Zenbook"
    assert zenbook["checkbox"] is False
    assert zenbook["price_rule"] == 1

def test_rog_gaming_scenario(amazon_store_data):
    """Verify the ROG Gaming scenario details."""
    rog_gaming = amazon_store_data["store"]["scenarios"]["ROG Gaming"]
    assert rog_gaming["url"] == "https://www.amazon.com/stores/page/9FE6FA16-F70F-4905-88E3-63344313BFA9?ingress=2&visitId=132d6aa6-3d21-4d52-8cfa-ef1bf1458a64"
    assert rog_gaming["active"] is True
    assert rog_gaming["condition"] == "new"
    assert rog_gaming["presta_categories"]["6484"] == "ZENBOOK"
    assert rog_gaming["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
    assert rog_gaming["presta_categories"]["3202"] == "computer, gaming console, devices"
    assert rog_gaming["presta_categories"]["3225"] == "notebooks"
    assert rog_gaming["presta_categories"]["6482"] == "Asus"
    assert rog_gaming["presta_categories"]["2258"] == "ASUS"
    assert rog_gaming["presta_categories"]["2287"] == "Laptops"
    assert rog_gaming["presta_categories"]["4167"] == "Zenbook"
    assert rog_gaming["checkbox"] is False
    assert rog_gaming["price_rule"] == 1

def test_tuf_gaming_scenario(amazon_store_data):
    """Verify the TUF Gaming scenario details."""
    tuf_gaming = amazon_store_data["store"]["scenarios"]["TUF Gaming"]
    assert tuf_gaming["url"] == "https://www.amazon.com/stores/page/9FE6FA16-F70F-4905-88E3-63344313BFA9?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln"
    assert tuf_gaming["active"] is True
    assert tuf_gaming["condition"] == "new"
    assert tuf_gaming["presta_categories"]["6486"] == "TUF"
    assert tuf_gaming["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
    assert tuf_gaming["presta_categories"]["3202"] == "computer, gaming console, devices"
    assert tuf_gaming["presta_categories"]["3225"] == "notebooks"
    assert tuf_gaming["presta_categories"]["6482"] == "Asus"
    assert tuf_gaming["presta_categories"]["2258"] == "ASUS"
    assert tuf_gaming["presta_categories"]["2287"] == "Laptops"
    assert tuf_gaming["presta_categories"]["4169"] == "TUF"
    assert tuf_gaming["checkbox"] is False
    assert tuf_gaming["price_rule"] == 1

def test_vivobook_scenario(amazon_store_data):
    """Verify the VIVOBook scenario details."""
    vivobook = amazon_store_data["store"]["scenarios"]["VIVOBook"]
    assert vivobook["url"] == "https://www.amazon.com/stores/page/FAEE9EC0-F27B-49D0-90F3-F77A3C09FDB9?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln"
    assert vivobook["active"] is True
    assert vivobook["condition"] == "new"
    assert vivobook["presta_categories"]["6486"] == "VIVOBook"
    assert vivobook["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
    assert vivobook["presta_categories"]["3202"] == "computer, gaming console, devices"
    assert vivobook["presta_categories"]["3225"] == "notebooks"
    assert vivobook["presta_categories"]["6482"] == "Asus"
    assert vivobook["presta_categories"]["2258"] == "ASUS"
    assert vivobook["presta_categories"]["2287"] == "Laptops"
    assert vivobook["presta_categories"]["4169"] == "TUF" # Note that this is TUF, not VIVOBook as it is in the JSON.
    assert vivobook["checkbox"] is False
    assert vivobook["price_rule"] == 1

def test_chromebook_scenario(amazon_store_data):
    """Verify the ChromeBook scenario details."""
    chromebook = amazon_store_data["store"]["scenarios"]["ChromeBook"]
    assert chromebook["url"] == "https://www.amazon.com/stores/page/FAEE9EC0-F27B-49D0-90F3-F77A3C09FDB9?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln"
    assert chromebook["active"] is True
    assert chromebook["condition"] == "new"
    assert chromebook["presta_categories"]["6591"] == "ChromeBook"
    assert chromebook["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
    assert chromebook["presta_categories"]["3202"] == "computer, gaming console, devices"
    assert chromebook["presta_categories"]["3225"] == "notebooks"
    assert chromebook["presta_categories"]["6482"] == "Asus"
    assert chromebook["presta_categories"]["2258"] == "ASUS"
    assert chromebook["presta_categories"]["2287"] == "Laptops"
    assert chromebook["presta_categories"]["6589"] == "ChromeBook"
    assert chromebook["checkbox"] is False
    assert chromebook["price_rule"] == 1

def test_proart_studiobook_scenario(amazon_store_data):
    """Verify the Asus ProArt Studiobook scenario details."""
    proart_studiobook = amazon_store_data["store"]["scenarios"]["Asus ProArt Studiobook"]
    assert proart_studiobook["url"] == "https://www.amazon.com/stores/page/EE8FF8CD-CC10-4DDF-9F0A-CE4E0E79018C?ingress=2&visitId=8825a742-bc7f-46ee-afa8-9e505b95c2aa&ref_=ast_bln"
    assert proart_studiobook["active"] is True
    assert proart_studiobook["condition"] == "new"
    assert proart_studiobook["presta_categories"]["6485"] == "Asus ProArt Studiobook"
    assert proart_studiobook["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
    assert proart_studiobook["presta_categories"]["3202"] == "computer, gaming console, devices"
    assert proart_studiobook["presta_categories"]["3225"] == "notebooks"
    assert proart_studiobook["presta_categories"]["6482"] == "Asus"
    assert proart_studiobook["presta_categories"]["2258"] == "ASUS"
    assert proart_studiobook["presta_categories"]["2287"] == "Laptops"
    assert proart_studiobook["presta_categories"]["4168"] == "ProArt Studiobook"
    assert proart_studiobook["checkbox"] is False
    assert proart_studiobook["price_rule"] == 1

def test_proart_desktops_scenario(amazon_store_data):
        """Verify the Asus ProArt Desktops scenario details."""
        proart_desktops = amazon_store_data["store"]["scenarios"]["Asus ProArt Desktops"]
        assert proart_desktops["url"] == "https://www.amazon.com/PD500TC-PH778/dp/B09TLH1B4M?ref_=ast_sto_dp&th=1"
        assert proart_desktops["active"] is True
        assert proart_desktops["condition"] == "new"
        assert proart_desktops["presta_categories"]["6485"] == "Asus ProArt Studiobook"
        assert proart_desktops["presta_categories"]["3198"] == "CONSUMER ELECTRONICS"
        assert proart_desktops["presta_categories"]["3202"] == "computer, gaming console, devices"
        assert proart_desktops["presta_categories"]["3225"] == "notebooks"
        assert proart_desktops["presta_categories"]["6482"] == "Asus"
        assert proart_desktops["presta_categories"]["2258"] == "ASUS"
        assert proart_desktops["presta_categories"]["2287"] == "Laptops"
        assert proart_desktops["presta_categories"]["4168"] == "ProArt Studiobook"
        assert proart_desktops["checkbox"] is False
        assert proart_desktops["price_rule"] == 1
```