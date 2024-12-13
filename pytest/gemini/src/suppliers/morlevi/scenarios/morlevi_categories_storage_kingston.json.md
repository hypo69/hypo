```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_kingston_data():
    """Loads the morlevi kingston data from the json file."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_storage_kingston.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def test_kingston_nvme_gen4_512gb(morlevi_kingston_data):
    """Test the data for 'KINGSTON NVME GEN4 512GB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON NVME GEN4 512GB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD NVME GEN4 512GB"

def test_kingston_nvme_gen4_1tb(morlevi_kingston_data):
    """Test the data for 'KINGSTON NVME GEN4 1TB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON NVME GEN4 1TB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=829&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD NVME GEN4 1TB"

def test_kingston_nvme_gen4_2tb(morlevi_kingston_data):
    """Test the data for 'KINGSTON NVME GEN4 2TB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON NVME GEN4 2TB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/314?p_315=22&p_175=831&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD NVME GEN4 2TB"

def test_kingston_sata_3_256gb(morlevi_kingston_data):
    """Test the data for 'KINGSTON SATA 3 256GB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON SATA 3 256GB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=823&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD SATA 3 256GB"

def test_kingston_sata_3_512gb(morlevi_kingston_data):
        """Test the data for 'KINGSTON SATA 3 512GB'."""
        scenario = morlevi_kingston_data['scenarios']['KINGSTON SATA 3 512GB']
        assert scenario['brand'] == 'KINGSTON'
        assert scenario['name'] == "internal_ssd_sata_3_2tb"
        assert scenario['url'] == "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword="
        assert scenario['checkbox'] == False
        assert scenario['active'] == True
        assert scenario['condition'] == 'new'
        assert scenario['presta_categories']['template']['kingston'] == "SSD SATA 3 512GB"

def test_kingston_sata_3_1tb(morlevi_kingston_data):
        """Test the data for 'KINGSTON SATA 3 1TB'."""
        scenario = morlevi_kingston_data['scenarios']['KINGSTON SATA 3 1TB']
        assert scenario['brand'] == 'KINGSTON'
        assert scenario['name'] == "internal_ssd_sata_3_4tb"
        assert scenario['url'] == "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=829&sort=datafloat2%2Cprice&keyword="
        assert scenario['checkbox'] == False
        assert scenario['active'] == True
        assert scenario['condition'] == 'new'
        assert scenario['presta_categories']['template']['kingston'] == "SSD SATA 3 1TB"

def test_kingston_sata_3_2tb(morlevi_kingston_data):
    """Test the data for 'KINGSTON SATA 3 2TB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON SATA 3 2TB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=831&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD SATA 3 2TB"

def test_kingston_sata_3_4tb(morlevi_kingston_data):
    """Test the data for 'KINGSTON SATA 3 4TB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON SATA 3 4TB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/50?p_315=22&p_175=3576&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD SATA 3 4TB"

def test_kingston_ssd_nvme_pcie_256gb(morlevi_kingston_data):
    """Test the data for 'KINGSTON SSD NVME PCIE 256GB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON SSD NVME PCIE 256GB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/51?p_315=22&p_175=823&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD NVME PCIE 256GB"

def test_kingston_ssd_nvme_pcie_512gb(morlevi_kingston_data):
    """Test the data for 'KINGSTON SSD NVME PCIE 512GB'."""
    scenario = morlevi_kingston_data['scenarios']['KINGSTON SSD NVME PCIE 512GB']
    assert scenario['brand'] == 'KINGSTON'
    assert scenario['name'] == "internal_ssd_m2sata_256"
    assert scenario['url'] == "https://www.morlevi.co.il/Cat/51?p_315=22&p_175=826&sort=datafloat2%2Cprice&keyword="
    assert scenario['checkbox'] == False
    assert scenario['active'] == True
    assert scenario['condition'] == 'new'
    assert scenario['presta_categories']['template']['kingston'] == "SSD NVME PCIE 512GB"

def test_invalid_key(morlevi_kingston_data):
        """Test for non-existent key."""
        with pytest.raises(KeyError):
            _ = morlevi_kingston_data['scenarios']['NON_EXISTENT_KEY']
```