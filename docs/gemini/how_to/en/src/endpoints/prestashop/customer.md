## Usage Guide for `hypotez/src/endpoints/prestashop/customer.py`

This guide describes how to use the `PrestaCustomer` class to interact with PrestaShop customers via its API.

**Class Overview:**

The `PrestaCustomer` class inherits from the `PrestaShop` class and provides methods for managing customers within a PrestaShop store.  It simplifies the process of making API calls for common customer operations.

**Example Usage:**

```python
from hypotez.src.endpoints.prestashop.customer import PrestaCustomer

# Replace with your actual credentials
API_DOMAIN = "your_api_domain"
API_KEY = "your_api_key"

# Initialize the PrestaCustomer object
prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)

# Add a new customer
try:
    result = prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
    print(f"Customer added: {result}")
except Exception as e:
    print(f"Error adding customer: {e}")

# Delete a customer
try:
    result = prestacustomer.delete_customer_PrestaShop(3)  # Replace 3 with the customer ID
    print(f"Customer deleted: {result}")
except Exception as e:
    print(f"Error deleting customer: {e}")

# Update a customer
try:
  result = prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
  print(f"Customer updated: {result}")
except Exception as e:
  print(f"Error updating customer: {e}")
  
# Get customer details
try:
  customer_details = prestacustomer.get_customer_details_PrestaShop(5)
  print(f"Customer details: {customer_details}")
except Exception as e:
  print(f"Error getting customer details: {e}")
```

**Constructor (`__init__`) Details:**

```python
def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
```

*   **`credentials` (Optional):** A dictionary or `SimpleNamespace` object containing `api_domain` and `api_key`.  If provided, this will override any `api_domain` or `api_key` passed separately.
*   **`api_domain` (Optional):** The PrestaShop API domain. **Required.**
*   **`api_key` (Optional):** The PrestaShop API key. **Required.**

**Important Considerations:**

*   **Error Handling:** The example includes `try...except` blocks to handle potential exceptions during API calls.  This is crucial for robust code.  Examine the exception types and messages within the `except` block to understand the specific cause of the error.
*   **Credentials:**  Replace `"your_api_domain"` and `"your_api_key"` with your actual PrestaShop API credentials.
*   **API Endpoints:** The `PrestaCustomer` class likely uses specific PrestaShop API endpoints (not shown) for the `add_customer_PrestaShop`, `delete_customer_PrestaShop`, `update_customer_PrestaShop`, and `get_customer_details_PrestaShop` methods. Consult the PrestaShop API documentation for the correct endpoint structures and parameters.
*   **Authentication:** Ensure proper authentication using your `API_KEY` is set up within the `PrestaShop` base class that `PrestaCustomer` inherits from.

**Before running:**

Make sure you have the necessary dependencies installed (e.g., `requests`, `attr`)

```bash
pip install requests attr
```

This guide provides a basic example.  For more complex use cases, refer to the PrestaShop API documentation for specific details on endpoints, parameter formats, and expected return values.