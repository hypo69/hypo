# PrestaShop Shop Endpoint

## Overview

This module provides a class for interacting with PrestaShop stores. It extends the `PrestaShop` class, offering methods for various shop-related operations.  It handles authentication and basic API interaction.


## Table of Contents

- [PrestaShopShop](#prestashopshop)
    - [__init__](#__init__)


## Classes

### `PrestaShopShop`

**Description**: This class provides methods for interacting with PrestaShop stores. It inherits from the `PrestaShop` class.

**Methods**

#### `__init__`

**Description**: Initializes a PrestaShopShop object.

**Parameters**

- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing `api_domain` and `api_key`.  Defaults to `None`.
- `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): The API key. Defaults to `None`.


**Raises**

- `ValueError`: If both `api_domain` and `api_key` are not provided.  

**Example Usage**

```python
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
shop = PrestaShopShop(credentials=credentials)
```
```python
shop = PrestaShopShop(api_domain='your_api_domain', api_key='your_api_key')
```
```python
# Using SimpleNamespace
from types import SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
shop = PrestaShopShop(credentials=credentials)
```
```python
# Important: Replace placeholders with your actual values.
```
```python


```
```python

```
```python


```
```python


```
```python


```
```python


```

```python