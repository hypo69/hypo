rst
How to use the PrestaSupplier class
========================================================================================

Description
-------------------------
This code defines a `PrestaSupplier` class, inheriting from the `PrestaShop` class.  It handles interactions with PrestaShop suppliers.  Crucially, the `__init__` method validates that both `api_domain` and `api_key` are provided, either directly or through a `credentials` object.

Execution steps
-------------------------
1. **Import necessary modules:** Imports modules like `SimpleNamespace`, `Optional`, `header`, `gs`, `logger`, `j_loads_ns`, `PrestaShop`, ensuring they are available for use within this class and its methods.

2. **Define the `PrestaSupplier` class:** This class inherits from `PrestaShop`, suggesting a common base for interacting with PrestaShop APIs.

3. **`__init__` method:** This method initializes the `PrestaSupplier` object.
   - It accepts optional arguments `credentials`, `api_domain`, and `api_key`.
   - If `credentials` is provided, it extracts `api_domain` and `api_key` from it, handling potential missing values gracefully.
   - It validates that both `api_domain` and `api_key` are provided.  If not, it raises a `ValueError`, preventing an improperly configured object from being created.
   - Finally, it calls the `__init__` method of the parent class `PrestaShop`, passing the validated `api_domain` and `api_key`.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier
    from types import SimpleNamespace
    
    # Example credentials using SimpleNamespace
    credentials = SimpleNamespace(api_domain="your-api-domain.com", api_key="your-api-key")

    try:
        supplier = PrestaSupplier(credentials=credentials)
        # Now you can use the 'supplier' object to make calls
        # to the PrestaShop API related to suppliers.
        # Example:
        # response = supplier.get_supplier_list() 
        # print(response)
    except ValueError as e:
        print(f"Error creating PrestaSupplier: {e}")