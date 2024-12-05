rst
How to use the PrestaCustomer class
========================================================================================

Description
-------------------------
This code defines a `PrestaCustomer` class for interacting with PrestaShop customers.  It inherits from the `PrestaShop` class, providing methods to add, delete, update, and retrieve customer information.  The class is designed to handle authentication and API interaction with PrestaShop.  It also includes error handling.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports modules like `sys`, `os`, `attr`, `pathlib`, `typing`, `header`, `gs`, `logger`, `j_loads`, `PrestaShop`, and `PrestaShopException`.  These are crucial for the class's functionalities, including API interactions, logging, and error management.

2. **Define the PrestaCustomer class:**  This class inherits from the `PrestaShop` class, indicating a relationship and re-usability of common functionality.

3. **Initialize the PrestaCustomer instance:** The `__init__` method takes optional `credentials`, `api_domain`, and `api_key` arguments.  If `credentials` are provided, the class extracts `api_domain` and `api_key` from them.  It validates that both `api_domain` and `api_key` are provided and raises a `ValueError` if not.  Otherwise, it calls the `super().__init__` method to initialize the inherited `PrestaShop` class with the provided credentials.

4. **Define methods for interacting with customers:** The class includes methods like `add_customer_PrestaShop`, `delete_customer_PrestaShop`, `update_customer_PrestaShop`, and `get_customer_details_PrestaShop`.  These methods are responsible for sending API requests to PrestaShop for the respective operations.

5. **Handle potential errors:** The class uses exception handling, specifically raising a `ValueError` if critical parameters (`api_domain`, `api_key`) are missing during initialization.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.customer import PrestaCustomer
    import os

    # Replace with your API credentials.  Store securely!
    API_DOMAIN = os.environ.get('PRESTASHOP_API_DOMAIN')
    API_KEY = os.environ.get('PRESTASHOP_API_KEY')
    
    if not API_DOMAIN or not API_KEY:
        raise ValueError("API credentials not provided or incorrect.  Set PRESTASHOP_API_DOMAIN and PRESTASHOP_API_KEY environment variables.")


    try:
        prestacustomer = PrestaCustomer(api_domain=API_DOMAIN, api_key=API_KEY)
        # Add a customer
        prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
        #Delete a customer (replace 3 with the customer ID)
        prestacustomer.delete_customer_PrestaShop(3)
        # Update a customer (replace 4 and "Updated Customer Name" with the ID and new name)
        prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
        # Get customer details (replace 5 with the customer ID)
        customer_details = prestacustomer.get_customer_details_PrestaShop(5)
        print(customer_details)  # Print the retrieved customer details

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")