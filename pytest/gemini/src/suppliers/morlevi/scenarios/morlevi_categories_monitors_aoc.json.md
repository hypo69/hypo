```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_aoc_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
        "scenarios": {
            "AOC 22": {
                "brand": "AOC",
                "url": "---------------------------------------AOC 22-------------------------------",
                "checkbox": false,
                "active": true,
                "condition":"new",
                "presta_categories": "127,128,529"
            },
            "AOC 23": {
                "brand": "AOC",
                "url": "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1806&sort=datafloat2%2Cprice&keyword=",
                "checkbox": false,
                "active": true,
                "condition":"new",
                "presta_categories": "127,128,529"
            },
            "AOC 24-25": {
                "brand": "AOC",
                "url": "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1807&sort=datafloat2%2Cprice&keyword=",
                "checkbox": false,
                "active": true,
                 "condition":"new",
                "presta_categories": "127,129,529"
            },
            "AOC 27-29": {
                "brand": "AOC",
                "url": "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1808&sort=datafloat2%2Cprice&keyword=",
                "checkbox": false,
                "active": true,
                 "condition":"new",
                "presta_categories": "127,130,529"
            },
            "AOC 32": {
                "brand": "AOC",
                "url": "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1809&sort=datafloat2%2Cprice&keyword=",
                "checkbox": false,
                "active": true,
                 "condition":"new",
                "presta_categories": "127,131,529"
            },
           "AOC 34": {
                "brand": "AOC",
                "url": " --------------------------  AOC 34 -----------------------------------",
                "checkbox": false,
                "active": true,
                 "condition":"new",
                "presta_categories": "127,132,529"
            },
           "AOC 49": {
                "brand": "AOC",
                "url": "-----------------------------  AOC 49 ---------------------------------",
                "checkbox": false,
                "active": true,
                 "condition":"new",
                 "presta_categories": "127,133,529"
            }
        }
    }
    """
    return json.loads(json_data)

# Test to check if the data is loaded correctly.
def test_morlevi_aoc_data_loaded(morlevi_aoc_data):
    """Check if the fixture loads the JSON data correctly."""
    assert "scenarios" in morlevi_aoc_data
    assert len(morlevi_aoc_data["scenarios"]) == 7

# Test cases for each scenario.
def test_aoc_22_data(morlevi_aoc_data):
    """Checks the data for the 'AOC 22' scenario."""
    aoc_22 = morlevi_aoc_data["scenarios"]["AOC 22"]
    assert aoc_22["brand"] == "AOC"
    assert aoc_22["url"] == "---------------------------------------AOC 22-------------------------------"
    assert aoc_22["checkbox"] == False
    assert aoc_22["active"] == True
    assert aoc_22["condition"] == "new"
    assert aoc_22["presta_categories"] == "127,128,529"

def test_aoc_23_data(morlevi_aoc_data):
    """Checks the data for the 'AOC 23' scenario."""
    aoc_23 = morlevi_aoc_data["scenarios"]["AOC 23"]
    assert aoc_23["brand"] == "AOC"
    assert aoc_23["url"] == "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1806&sort=datafloat2%2Cprice&keyword="
    assert aoc_23["checkbox"] == False
    assert aoc_23["active"] == True
    assert aoc_23["condition"] == "new"
    assert aoc_23["presta_categories"] == "127,128,529"

def test_aoc_24_25_data(morlevi_aoc_data):
     """Checks the data for the 'AOC 24-25' scenario."""
     aoc_24_25 = morlevi_aoc_data["scenarios"]["AOC 24-25"]
     assert aoc_24_25["brand"] == "AOC"
     assert aoc_24_25["url"] == "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1807&sort=datafloat2%2Cprice&keyword="
     assert aoc_24_25["checkbox"] == False
     assert aoc_24_25["active"] == True
     assert aoc_24_25["condition"] == "new"
     assert aoc_24_25["presta_categories"] == "127,129,529"

def test_aoc_27_29_data(morlevi_aoc_data):
     """Checks the data for the 'AOC 27-29' scenario."""
     aoc_27_29 = morlevi_aoc_data["scenarios"]["AOC 27-29"]
     assert aoc_27_29["brand"] == "AOC"
     assert aoc_27_29["url"] == "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1808&sort=datafloat2%2Cprice&keyword="
     assert aoc_27_29["checkbox"] == False
     assert aoc_27_29["active"] == True
     assert aoc_27_29["condition"] == "new"
     assert aoc_27_29["presta_categories"] == "127,130,529"


def test_aoc_32_data(morlevi_aoc_data):
    """Checks the data for the 'AOC 32' scenario."""
    aoc_32 = morlevi_aoc_data["scenarios"]["AOC 32"]
    assert aoc_32["brand"] == "AOC"
    assert aoc_32["url"] == "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1809&sort=datafloat2%2Cprice&keyword="
    assert aoc_32["checkbox"] == False
    assert aoc_32["active"] == True
    assert aoc_32["condition"] == "new"
    assert aoc_32["presta_categories"] == "127,131,529"

def test_aoc_34_data(morlevi_aoc_data):
    """Checks the data for the 'AOC 34' scenario."""
    aoc_34 = morlevi_aoc_data["scenarios"]["AOC 34"]
    assert aoc_34["brand"] == "AOC"
    assert aoc_34["url"] == " --------------------------  AOC 34 -----------------------------------"
    assert aoc_34["checkbox"] == False
    assert aoc_34["active"] == True
    assert aoc_34["condition"] == "new"
    assert aoc_34["presta_categories"] == "127,132,529"

def test_aoc_49_data(morlevi_aoc_data):
    """Checks the data for the 'AOC 49' scenario."""
    aoc_49 = morlevi_aoc_data["scenarios"]["AOC 49"]
    assert aoc_49["brand"] == "AOC"
    assert aoc_49["url"] == "-----------------------------  AOC 49 ---------------------------------"
    assert aoc_49["checkbox"] == False
    assert aoc_49["active"] == True
    assert aoc_49["condition"] == "new"
    assert aoc_49["presta_categories"] == "127,133,529"
```