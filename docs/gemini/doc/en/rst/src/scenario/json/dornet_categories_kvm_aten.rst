DORNET Categories KVM ATEN
==========================

This file defines the KVM configuration details for the ATEN KVM system.  It specifies the brand, URL, checkbox status, active status, condition, and PrestaShop category ID.

.. automodule:: hypotez.src.scenario.json.dornet_categories_kvm_aten
    :members:
    :undoc-members:
    :show-inheritance:

KVM Configuration
-----------------

~ KVM Details
^^^
```python
# Placeholder for the actual JSON data
# This is a representation only.  The actual data would be loaded here.
kvm_data = {
    "KVM": {
        "brand": "ATEN",
        "url": "https://www.cable.co.il/items.asp?Cat2Cat1ID=107&Cat2ID=301",
        "checkbox": False,
        "active": True,
        "condition": "new",
        "presta_categories": "536"
    }
}
```
```
```
```python
# Example functions (replace with actual functions if present)

# Function to access KVM brand
def get_kvm_brand() -> str:
    """
    Returns the KVM brand.
    
    Returns:
        str: The KVM brand.
        
    Raises:
        KeyError: If 'KVM' or 'brand' key is missing from the JSON.
    """
    try:
        return kvm_data['KVM']['brand']
    except KeyError as ex:
        raise KeyError(f"Missing key: {ex}")
```