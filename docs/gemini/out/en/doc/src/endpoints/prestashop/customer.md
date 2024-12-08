# PrestaShop Customer Endpoint

## Overview

This module provides a class for interacting with customer data within the PrestaShop API. It facilitates adding, deleting, updating, and retrieving customer details.


## Table of Contents

* [PrestaCustomer](#presta-customer)
    * [__init__](#init)
    * [add_customer_PrestaShop](#add_customer_prestashop)
    * [delete_customer_PrestaShop](#delete_customer_prestashop)
    * [update_customer_PrestaShop](#update_customer_prestashop)
    * [get_customer_details_PrestaShop](#get_customer_details_prestashop)


## Classes

### `PrestaCustomer`

**Description**: This class extends the `PrestaShop` class, providing specialized methods for managing customer data.

**Methods**

#### `__init__`

**Description**: Initializes a `PrestaCustomer` object.

**Parameters**

- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing 'api_domain' and 'api_key' for authentication. Defaults to None.
- `api_domain` (Optional[str], optional): The API domain. Defaults to None.
- `api_key` (Optional[str], optional): The API key. Defaults to None.

**Raises**

- `ValueError`: If both `api_domain` and `api_key` are not provided.


## Functions

(No functions are present in the provided code snippet)