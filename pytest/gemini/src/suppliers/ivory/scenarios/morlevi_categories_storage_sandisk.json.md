```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data from the file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_sandisk.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['scenarios']


def test_all_scenarios_are_present(morlevi_categories_data):
    """
     Test that checks if all the expected scenarios are present in the loaded JSON data.
     It asserts that the length of the 'morlevi_categories_data' dictionary is equal to 38,
     ensuring that all expected scenarios are loaded. This test does not focus on the data content
     of each scenario, but instead checks if the structure is complete and no scenarios are missing.
    """
    assert len(morlevi_categories_data) == 38

def test_scenario_has_correct_keys(morlevi_categories_data):
    """
        Verifies that each scenario in the loaded JSON data contains the expected keys
        such as 'brand', 'name', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
        It iterates over the scenarios, ensuring that all required keys are present, which validates
        the basic structure of the JSON data. This check is crucial for preventing errors in downstream code
        that depends on these keys being present.
    """
    expected_keys = {"brand", "name", "url", "checkbox", "active", "condition", "presta_categories"}
    for scenario in morlevi_categories_data.values():
        assert set(scenario.keys()) == expected_keys

def test_brand_is_sandisk(morlevi_categories_data):
     """
        Test to ensure that the 'brand' attribute for all scenarios is set to 'SANDISK'.
        It loops through each scenario in the 'morlevi_categories_data' and verifies
        if the 'brand' is indeed 'SANDISK'. It raises an AssertionError if the brand of any scenario
        does not match the expected value. This check ensures that data is consistent
        with the expected structure for the scenarios from this supplier.
     """
     for scenario in morlevi_categories_data.values():
        assert scenario['brand'] == 'SANDISK'


def test_checkbox_is_false(morlevi_categories_data):
    """
        This test verifies that the 'checkbox' attribute for all scenarios is set to 'False'.
        It iterates over the 'morlevi_categories_data' dictionary and asserts that
        the value of the 'checkbox' key is False. This verifies a structural aspect of the data,
        ensuring consistent configuration across all scenarios and that no checkbox is enabled by default.
    """
    for scenario in morlevi_categories_data.values():
        assert scenario['checkbox'] == False

def test_active_is_true(morlevi_categories_data):
    """
        Test to check that the 'active' attribute is set to true for all scenarios.
        The test iterates through each scenario in the 'morlevi_categories_data' and
        asserts that the 'active' attribute equals True, which ensures that all the
        scenarios are correctly marked as active and ready for further processing.
    """
    for scenario in morlevi_categories_data.values():
        assert scenario['active'] == True

def test_condition_is_new(morlevi_categories_data):
    """
        Test to ensure that the 'condition' attribute for all scenarios is set to 'new'.
        It checks each scenario in the 'morlevi_categories_data' and asserts that
        the value of the 'condition' key is equal to the string 'new'. This confirms that the
        products are all set to the correct state according to the data requirements.
    """
    for scenario in morlevi_categories_data.values():
        assert scenario['condition'] == 'new'

def test_presta_categories_is_string(morlevi_categories_data):
     """
        Test to verify that the 'presta_categories' attribute for each scenario is a string.
        It iterates through all the scenarios in 'morlevi_categories_data' and uses the
        isinstance method to ensure that each 'presta_categories' value is of string type.
        This checks the data structure of the 'presta_categories' field, which is important
        as it is required to be a comma separated string that prestashop recognizes.
     """
     for scenario in morlevi_categories_data.values():
        assert isinstance(scenario['presta_categories'], str)


def test_url_not_empty(morlevi_categories_data):
    """
        Test to check that the 'url' attribute for all scenarios is not empty, which helps ensure data integrity.
        It loops over each scenario in 'morlevi_categories_data' and checks if the 'url'
        value exists, is not None, and is not an empty string using a boolean check.
        This ensures that required URLs are available, which is crucial for scenarios
        to link correctly and that they are provided correctly in the json.
    """
    for scenario in morlevi_categories_data.values():
        assert scenario['url']

def test_name_not_empty(morlevi_categories_data):
    """
        This test ensures that the 'name' attribute for every scenario is not empty.
        It iterates through each scenario in 'morlevi_categories_data' and
        verifies that the 'name' value exists, is not None, and is not an empty string using a boolean check.
        This check ensures that each scenario has a meaningful name, which is
        important for identification and processing purposes.
    """
    for scenario in morlevi_categories_data.values():
         assert scenario['name']

def test_url_is_string(morlevi_categories_data):
    """
        This test ensures that the 'url' attribute for each scenario is a string.
        It iterates over all scenarios and checks that the 'url' is of string type using isinstance.
        This verifies the data type of each scenario's 'url' and prevents errors where string operations are assumed.
    """
    for scenario in morlevi_categories_data.values():
        assert isinstance(scenario['url'],str)

def test_name_is_string(morlevi_categories_data):
    """
        Test to verify that the 'name' attribute of each scenario is a string.
        It iterates through all scenarios in 'morlevi_categories_data' and asserts that
        the 'name' attribute is an instance of the string class. This is important for ensuring
        that operations that expect strings can be performed safely on this attribute and that it is stored correctly
    """
    for scenario in morlevi_categories_data.values():
        assert isinstance(scenario['name'],str)
```