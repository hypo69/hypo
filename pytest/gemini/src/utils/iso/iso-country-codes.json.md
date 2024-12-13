```python
import pytest
import json

# Define a fixture to load the JSON data
@pytest.fixture
def iso_country_data():
    """Loads the iso-country-codes.json data."""
    with open("hypotez/src/utils/iso/iso-country-codes.json", "r") as f:
        data = json.load(f)
    return data

# Test cases for the JSON data structure
def test_iso_country_data_is_list(iso_country_data):
    """Checks if the loaded data is a list."""
    assert isinstance(iso_country_data, list), "The loaded data should be a list."

def test_iso_country_data_list_not_empty(iso_country_data):
      """Checks if the list of countries is not empty."""
      assert len(iso_country_data) > 0, "The list of countries should not be empty."


def test_iso_country_data_list_element_is_dict(iso_country_data):
    """Checks if each element in the list is a dictionary."""
    for item in iso_country_data:
        assert isinstance(item, dict), "Each item in the list should be a dictionary."

def test_iso_country_data_keys_present(iso_country_data):
    """Checks if all required keys are present in each dictionary."""
    required_keys = [
        "name",
        "alpha-2",
        "alpha-3",
        "country-code",
        "iso_3166-2",
        "region",
        "sub-region",
        "intermediate-region",
        "region-code",
        "sub-region-code",
        "intermediate-region-code",
    ]
    for country in iso_country_data:
        for key in required_keys:
            assert key in country, f"Key '{key}' missing in country: {country.get('name', 'unknown')}"

def test_iso_country_data_country_codes_are_string(iso_country_data):
    """Checks if country codes are strings."""
    for country in iso_country_data:
       assert isinstance(country["country-code"], str), f"Country code should be a string in : {country.get('name', 'unknown')}"

def test_iso_country_data_region_codes_are_string(iso_country_data):
      """Checks if the region codes are strings."""
      for country in iso_country_data:
          assert isinstance(country["region-code"], str), f"Region code should be a string in : {country.get('name', 'unknown')}"

def test_iso_country_data_subregion_codes_are_string(iso_country_data):
    """Checks if sub-region codes are strings."""
    for country in iso_country_data:
        assert isinstance(country["sub-region-code"], str), f"Sub-region code should be a string in : {country.get('name', 'unknown')}"


def test_iso_country_data_intermediate_region_codes_are_string(iso_country_data):
    """Checks if intermediate region codes are strings."""
    for country in iso_country_data:
        assert isinstance(country["intermediate-region-code"], str), f"Intermediate region code should be a string in : {country.get('name', 'unknown')}"


def test_iso_country_data_alpha2_codes_are_string(iso_country_data):
    """Checks if alpha-2 codes are strings."""
    for country in iso_country_data:
        assert isinstance(country["alpha-2"], str), f"Alpha-2 code should be a string in : {country.get('name', 'unknown')}"


def test_iso_country_data_alpha3_codes_are_string(iso_country_data):
    """Checks if alpha-3 codes are strings."""
    for country in iso_country_data:
       assert isinstance(country["alpha-3"], str), f"Alpha-3 code should be a string in : {country.get('name', 'unknown')}"


def test_iso_country_data_iso_3166_2_codes_are_string(iso_country_data):
    """Checks if iso-3166-2 codes are strings."""
    for country in iso_country_data:
       assert isinstance(country["iso_3166-2"], str), f"ISO 3166-2 code should be a string in : {country.get('name', 'unknown')}"


def test_iso_country_data_region_are_string(iso_country_data):
      """Checks if the region are strings."""
      for country in iso_country_data:
          assert isinstance(country["region"], str), f"region should be a string in : {country.get('name', 'unknown')}"

def test_iso_country_data_sub_region_are_string(iso_country_data):
      """Checks if the sub region are strings."""
      for country in iso_country_data:
          assert isinstance(country["sub-region"], str), f"sub region should be a string in : {country.get('name', 'unknown')}"

def test_iso_country_data_intermediate_region_are_string(iso_country_data):
      """Checks if the intermediate region are strings."""
      for country in iso_country_data:
          assert isinstance(country["intermediate-region"], str), f"intermediate region should be a string in : {country.get('name', 'unknown')}"

def test_iso_country_data_name_are_string(iso_country_data):
      """Checks if the name are strings."""
      for country in iso_country_data:
          assert isinstance(country["name"], str), f"name should be a string in : {country.get('name', 'unknown')}"


def test_iso_country_data_alpha2_codes_are_uppercase(iso_country_data):
    """Checks if alpha-2 codes are uppercase."""
    for country in iso_country_data:
      assert country["alpha-2"].isupper(), f"Alpha-2 code should be uppercase in : {country.get('name', 'unknown')}"

def test_iso_country_data_alpha3_codes_are_uppercase(iso_country_data):
      """Checks if alpha-3 codes are uppercase."""
      for country in iso_country_data:
          assert country["alpha-3"].isupper(), f"Alpha-3 code should be uppercase in : {country.get('name', 'unknown')}"


def test_iso_country_data_iso_3166_2_codes_start_with_iso(iso_country_data):
    """Checks if iso-3166-2 codes start with ISO 3166-2:"""
    for country in iso_country_data:
        assert country["iso_3166-2"].startswith("ISO 3166-2:"), f"ISO 3166-2 code should start with 'ISO 3166-2:' in : {country.get('name', 'unknown')}"

def test_iso_country_data_iso_3166_2_codes_end_with_alpha2_code(iso_country_data):
    """Checks if iso-3166-2 codes end with the alpha-2 code"""
    for country in iso_country_data:
        assert country["iso_3166-2"].endswith(country["alpha-2"]), f"ISO 3166-2 code should end with alpha-2 code in: {country.get('name','unknown')}"

def test_iso_country_data_no_empty_names(iso_country_data):
      """Checks if there are no empty country names."""
      for country in iso_country_data:
          assert country["name"].strip() != "", f"Country name should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_alpha2(iso_country_data):
    """Checks if there are no empty alpha-2 codes."""
    for country in iso_country_data:
        assert country["alpha-2"].strip() != "", f"Alpha-2 code should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_alpha3(iso_country_data):
    """Checks if there are no empty alpha-3 codes."""
    for country in iso_country_data:
        assert country["alpha-3"].strip() != "", f"Alpha-3 code should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_country_codes(iso_country_data):
    """Checks if there are no empty country codes."""
    for country in iso_country_data:
        assert country["country-code"].strip() != "", f"Country code should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_iso_3166_2_codes(iso_country_data):
    """Checks if there are no empty iso_3166-2 codes."""
    for country in iso_country_data:
        assert country["iso_3166-2"].strip() != "", f"ISO 3166-2 code should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_regions(iso_country_data):
    """Checks if there are no empty region."""
    for country in iso_country_data:
        assert country["region"].strip() != "", f"region should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_sub_regions(iso_country_data):
    """Checks if there are no empty sub-region."""
    for country in iso_country_data:
        assert country["sub-region"].strip() != "", f"sub-region should not be empty in : {country.get('name', 'unknown')}"


def test_iso_country_data_no_empty_region_code(iso_country_data):
    """Checks if there are no empty region codes."""
    for country in iso_country_data:
        assert country["region-code"].strip() != "", f"region-code should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_no_empty_sub_region_code(iso_country_data):
    """Checks if there are no empty sub region codes."""
    for country in iso_country_data:
        assert country["sub-region-code"].strip() != "", f"sub-region-code should not be empty in : {country.get('name', 'unknown')}"

def test_iso_country_data_country_code_is_unique(iso_country_data):
    """Checks if country-code are unique"""
    country_codes = [country["country-code"] for country in iso_country_data]
    assert len(country_codes) == len(set(country_codes)), "Country codes are not unique."


def test_iso_country_data_alpha_2_is_unique(iso_country_data):
    """Checks if alpha-2 codes are unique"""
    alpha_2_codes = [country["alpha-2"] for country in iso_country_data]
    assert len(alpha_2_codes) == len(set(alpha_2_codes)), "Alpha-2 codes are not unique."

def test_iso_country_data_alpha_3_is_unique(iso_country_data):
      """Checks if alpha-3 codes are unique"""
      alpha_3_codes = [country["alpha-3"] for country in iso_country_data]
      assert len(alpha_3_codes) == len(set(alpha_3_codes)), "Alpha-3 codes are not unique."
```