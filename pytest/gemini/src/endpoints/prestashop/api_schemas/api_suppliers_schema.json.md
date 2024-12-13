```python
import pytest
import json

# Fixture for loading the JSON schema
@pytest.fixture
def api_suppliers_schema_data():
    """Provides test data from the JSON schema."""
    schema_content = """
    {
        "suppliers": {
            "supplier": [
                {
                    "attrs": {
                        "id": "1"
                    },
                    "value": ""
                },
                {
                    "attrs": {
                        "id": "2"
                    },
                    "value": ""
                }
            ]
        }
    }
    """
    return json.loads(schema_content)

# Test case for checking the structure of the schema
def test_api_suppliers_schema_structure(api_suppliers_schema_data):
    """Tests the basic structure of the API suppliers schema."""
    assert "suppliers" in api_suppliers_schema_data, "The 'suppliers' key should exist."
    assert "supplier" in api_suppliers_schema_data["suppliers"], "The 'supplier' key should exist inside 'suppliers'."
    assert isinstance(api_suppliers_schema_data["suppliers"]["supplier"], list), "'supplier' should be a list."
    assert len(api_suppliers_schema_data["suppliers"]["supplier"]) == 2, "There should be 2 supplier entries."

# Test case for checking the contents of each supplier
def test_api_suppliers_schema_supplier_content(api_suppliers_schema_data):
    """Tests the content of each supplier element in the schema."""
    suppliers = api_suppliers_schema_data["suppliers"]["supplier"]

    for supplier in suppliers:
        assert "attrs" in supplier, "Each supplier entry should have an 'attrs' key."
        assert "id" in supplier["attrs"], "Each supplier's attrs should have an 'id' key."
        assert isinstance(supplier["attrs"]["id"], str), "The 'id' should be a string."
        assert "value" in supplier, "Each supplier entry should have a 'value' key."
        assert isinstance(supplier["value"], str), "The 'value' should be a string."
        

# Test case to check supplier ids.
def test_api_suppliers_schema_supplier_ids(api_suppliers_schema_data):
    """Tests if the supplier IDs are correct."""
    suppliers = api_suppliers_schema_data["suppliers"]["supplier"]

    supplier_ids = [supplier["attrs"]["id"] for supplier in suppliers]
    assert "1" in supplier_ids, "Supplier with id '1' should exist"
    assert "2" in supplier_ids, "Supplier with id '2' should exist"

# Test case for empty schema
def test_api_suppliers_schema_empty_suppliers():
    """Tests an empty schema structure."""
    schema_content = '{"suppliers": {"supplier": []}}'
    empty_schema = json.loads(schema_content)

    assert "suppliers" in empty_schema, "The 'suppliers' key should exist."
    assert "supplier" in empty_schema["suppliers"], "The 'supplier' key should exist inside 'suppliers'."
    assert isinstance(empty_schema["suppliers"]["supplier"], list), "'supplier' should be a list."
    assert len(empty_schema["suppliers"]["supplier"]) == 0, "There should be 0 supplier entries."


# Test case with missing suppliers
def test_api_suppliers_schema_missing_suppliers():
    """Test schema with missing 'suppliers' key."""
    schema_content = '{"something_else": {"supplier": []}}'
    missing_suppliers_schema = json.loads(schema_content)

    assert "suppliers" not in missing_suppliers_schema, "The 'suppliers' key should not exist."


# Test case with missing supplier
def test_api_suppliers_schema_missing_supplier():
    """Test schema with missing 'supplier' key."""
    schema_content = '{"suppliers": {"something_else": []}}'
    missing_supplier_schema = json.loads(schema_content)
    
    assert "suppliers" in missing_supplier_schema, "The 'suppliers' key should exist."
    assert "supplier" not in missing_supplier_schema["suppliers"], "The 'supplier' key should not exist."


# Test case with invalid data type for supplier list
def test_api_suppliers_schema_invalid_supplier_type():
    """Test schema with 'supplier' as a string instead of a list."""
    schema_content = '{"suppliers": {"supplier": "invalid_data"}}'
    invalid_supplier_type_schema = json.loads(schema_content)

    assert "suppliers" in invalid_supplier_type_schema, "The 'suppliers' key should exist."
    assert "supplier" in invalid_supplier_type_schema["suppliers"], "The 'supplier' key should exist inside 'suppliers'."
    assert isinstance(invalid_supplier_type_schema["suppliers"]["supplier"], str), "The 'supplier' key should be a string."

# Test case with invalid data type for supplier id
def test_api_suppliers_schema_invalid_supplier_id():
    """Test schema with 'id' as an integer instead of a string."""
    schema_content = """
    {
        "suppliers": {
            "supplier": [
                {
                    "attrs": {
                        "id": 1
                    },
                    "value": ""
                }
                ]
        }
    }
    """
    invalid_supplier_id_schema = json.loads(schema_content)
    suppliers = invalid_supplier_id_schema["suppliers"]["supplier"]
    for supplier in suppliers:
        assert isinstance(supplier["attrs"]["id"], int), "The 'id' should be an integer."

# Test case with missing supplier attrs key
def test_api_suppliers_schema_missing_supplier_attrs():
    """Test schema with missing attrs key."""
    schema_content = """
        {
            "suppliers": {
                "supplier": [
                    {
                        "value": ""
                    }
                    ]
            }
        }
        """
    missing_attrs_schema = json.loads(schema_content)
    suppliers = missing_attrs_schema["suppliers"]["supplier"]
    for supplier in suppliers:
        assert "attrs" not in supplier, "The 'attrs' key should not exist."
```