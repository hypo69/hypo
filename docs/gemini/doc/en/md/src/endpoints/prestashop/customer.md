# PrestaShop Customer Endpoint

## Overview

This module provides a class `PrestaCustomer` for interacting with PrestaShop customers. It extends the base `PrestaShop` class, adding methods specifically for customer management.

## Table of Contents

* [Classes](#classes)
    * [PrestaCustomer](#presta-customer)
        * [\_\_init\_\_](#__init__)


## Classes

### `PrestaCustomer`

**Description**:  A class for interacting with PrestaShop customers, extending the `PrestaShop` class.  Provides methods for adding, deleting, updating, and retrieving customer details.


**Methods**

#### `__init__`

**Description**: Initializes the PrestaShop customer client.

**Parameters**:

- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or a `SimpleNamespace` object containing the API domain and key. Defaults to `None`.
- `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): The API key. Defaults to `None`.

**Raises**:

- `ValueError`: If both `api_domain` and `api_key` are not provided.


```python
def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
    """Инициализация клиента PrestaShop.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)
```
```
**Example Usage (Illustrative):**

```python
# Assuming API_DOMAIN and API_KEY are defined elsewhere
prestacustomer = PrestaCustomer(API_DOMAIN, API_KEY)
prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
```

**Note**:  Example usage above and within the docstring assume that the `add_customer_PrestaShop`, `delete_customer_PrestaShop`, `update_customer_PrestaShop`, and `get_customer_details_PrestaShop` methods exist, as these are not implemented in the provided code snippet.  This documentation needs to be updated to reflect the actual functionality of those methods if they are present.