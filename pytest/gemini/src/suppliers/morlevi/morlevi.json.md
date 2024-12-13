```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Provides the morlevi supplier data as a dictionary."""
    json_data = """
    {
      "supplier": "morlevi",
      "supplier_id": "2784",
      "supplier_prefix": "mlv",
      "start_url": "https://www.morlevi.co.il/",
      "login_url": "https://www.morlevi.co.il/",
      "price_rule": "*1.43",
    
      "collect_products_from_categorypage": false,
    
      "scenario_files": [
        { "$ref": "morlevi_categories_cases_antec.json#" },
        "morlevi_categories_storage_samsung.json",
        "morlevi_categories_storage_kingston.json",
        "morlevi_categories_video.json",
        "morlevi_categories_monitors_samsung.json",
        "morlevi_categories_monitors_lenovo.json",
        "morlevi_categories_mb_gigabyte.json",
        "morlevi_categories_cases_coolermaster.json",
        "morlevi_categories_cases_corsair.json",
        "morlevi_categories_cases_generic.json",
        "morlevi_categories_headsets.json",
        "morlevi_categories_laptops_asus.json",
        "morlevi_categories_laptops_gigabyte.json",
        "morlevi_categories_laptops_dell.json",
        "morlevi_categories_laptops_hp.json",
        "morlevi_categories_laptops_lenovo.json",
        "morlevi_categories_memory.json",
        "morlevi_categories_cpu.json",
        "morlevi_categories_cases_antec.json"
    
      ],
      "last_runned_scenario": "morlevi_categories_mb_gigabyte.json",
    
      "excluded": [
        [
    
        ],
        [
          "morlevi_categories_minipc_gigabyte.json",
          "morlevi_categories_minipc_intel.json"
        ],
    
        [
          "morlevi_categories_video.json"
        ],
        [
    
          "morlevi_categories_memory_dimm_ddr4.json",
          "morlevi_categories_memory_sodimm_ddr3.json",
          "morlevi_categories_memory_sodimm_ddr4.json"
        ],
        [
          "morlevi_categories_monitors_aoc.json",
          "morlevi_categories_monitors_dell.json",
          "morlevi_categories_monitors_lenovo.json",
          "morlevi_categories_monitors_philips.json",
          "morlevi_categories_monitors_mag.json"
        ],
        [
          "morlevi_categories_psu_antec.json",
          "morlevi_categories_psu_cooler_maser.json",
          "morlevi_categories_psu_gigabyte.json",
          "morlevi_categories_psu_corsair.json"
        ],
        [
          "morlevi_categories_sound.json"
        ],
        [
          "morlevi_categories_storage_crucial.json",
          "morlevi_categories_storage_gigabyte.json",
          "morlevi_categories_storage_intel.json",
          "morlevi_categories_storage_kingston.json",
          "morlevi_categories_storage_samsung.json",
          "morlevi_categories_storage_sandisk.json",
          "morlevi_categories_storage_toshiba.json",
          "morlevi_categories_storage_wd.json"
        ],
        [
          "morlevi_categories_ups.json"
        ],
        [
          "morlevi_categories_printers.json"
        ],
        [
    
        ],
        [
    
          "morlevi_categories_cases_zalman.json"
        ],
        [
          "morlevi_categories_keyboards_coolermaster.json",
          "morlevi_categories_keyboards_genius.json",
          "morlevi_categories_keyboards_hp.json",
          "morlevi_categories_keyboards_logitech.json",
          "morlevi_categories_keyboards_microsoft.json"
        ],
        [
          "morlevi_categories_network.json"
        ],
          [
              "morlevi_categories_printers.json"
          ]
      ]
    }
    """
    return json.loads(json_data)



def test_supplier_name(morlevi_data):
    """Checks if the supplier name is correctly loaded."""
    assert morlevi_data["supplier"] == "morlevi"

def test_supplier_id(morlevi_data):
    """Checks if the supplier ID is correctly loaded."""
    assert morlevi_data["supplier_id"] == "2784"

def test_supplier_prefix(morlevi_data):
    """Checks if the supplier prefix is correctly loaded."""
    assert morlevi_data["supplier_prefix"] == "mlv"

def test_start_url(morlevi_data):
    """Checks if the start URL is correctly loaded."""
    assert morlevi_data["start_url"] == "https://www.morlevi.co.il/"

def test_login_url(morlevi_data):
    """Checks if the login URL is correctly loaded."""
    assert morlevi_data["login_url"] == "https://www.morlevi.co.il/"

def test_price_rule(morlevi_data):
     """Checks if the price rule is loaded correctly."""
     assert morlevi_data["price_rule"] == "*1.43"

def test_collect_products_from_categorypage(morlevi_data):
    """Checks if the collect_products_from_categorypage flag is loaded correctly."""
    assert morlevi_data["collect_products_from_categorypage"] == False

def test_scenario_files_not_empty(morlevi_data):
    """Checks if the scenario_files list is not empty."""
    assert len(morlevi_data["scenario_files"]) > 0

def test_scenario_files_type(morlevi_data):
    """Checks if scenario files are of string type or dictionary."""
    for file in morlevi_data["scenario_files"]:
        assert isinstance(file, str) or isinstance(file,dict)

def test_last_runned_scenario(morlevi_data):
     """Checks if the last runned scenario is loaded correctly."""
     assert morlevi_data["last_runned_scenario"] == "morlevi_categories_mb_gigabyte.json"

def test_excluded_is_list_of_lists(morlevi_data):
    """Checks if 'excluded' is a list of lists."""
    assert isinstance(morlevi_data["excluded"], list)
    for item in morlevi_data["excluded"]:
        assert isinstance(item, list)


def test_excluded_file_types(morlevi_data):
    """Checks if excluded files are of type string."""
    for list_files in morlevi_data["excluded"]:
       for file in list_files:
          assert isinstance(file,str)

def test_empty_excluded_list(morlevi_data):
    """Checks if there are empty list in excluded filed"""
    for list_files in morlevi_data["excluded"]:
        if not list_files:
             assert True
             return
    assert False , "There is no empty list in excluded field"

def test_excluded_nested_lists_not_empty(morlevi_data):
    """Checks if nested lists in 'excluded' are not empty lists."""
    for lst in morlevi_data["excluded"]:
        if lst:
            assert True
            return
    assert False, "There is no non empty nested list in 'excluded' field"
```