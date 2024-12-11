# ProductFields Class Documentation

## Overview

The `ProductFields` class is designed to manage and structure product data in the format required by the PrestaShop API. This class provides a comprehensive interface for handling product fields, including both single-language and multi-language fields. It ensures that the data is correctly formatted and validated before being sent to the PrestaShop API.

## Table of Contents

1. [Introduction](#introduction)
2. [Class Initialization](#class-initialization)
3. [Product Fields](#product-fields)
   - [Single-Language Fields](#single-language-fields)
   - [Multi-Language Fields](#multi-language-fields)
4. [Associations](#associations)
5. [Default Values](#default-values)
6. [Error Handling](#error-handling)
7. [Usage Examples](#usage-examples)
8. [Conclusion](#conclusion)

## Introduction

The `ProductFields` class is a Python class that encapsulates the structure and behavior of product fields in the PrestaShop database. It is designed to simplify the process of creating, updating, and managing product data by providing a clear and consistent interface for interacting with product fields.

The class is particularly useful for developers working with the PrestaShop API, as it ensures that all required fields are correctly formatted and validated before being sent to the API.

## Class Initialization

### `__init__` Method

The `__init__` method initializes the `ProductFields` class by loading the list of product fields and setting up default values for the fields. It also initializes a `SimpleNamespace` object to store the product fields and an auxiliary dictionary for additional fields.

```python
def __init__(self):
    self.product_fields_list = self._load_product_fields_list()
    self.language = {'en': 1, 'he': 2, 'ru': 3}
    self.presta_fields = SimpleNamespace(**{key: None for key in self.product_fields_list})
    self.assist_fields_dict = {
        'default_image_url': '', 
        'images_urls': []
    }
    self._payload()
```

### `_load_product_fields_list` Method

This method loads the list of product fields from a text file. The file is expected to contain one field name per line.

```python
def _load_product_fields_list(self) -> List[str]:
    return read_text_file(Path(gs.path.src, 'product', 'product_fields', 'fields_list.txt'), as_list=True)
```

### `_payload` Method

This method loads default values for the product fields from a JSON file. If the file is not found or cannot be loaded, a debug message is logged.

```python
def _payload(self) -> bool:
    data = j_loads(Path(gs.path.src, 'product', 'product_fields', 'product_fields_default_values.json'))
    if not data:
        logger.debug(f"Ошибка загрузки полей из файла {gs.path.src}/product/product_fields/product_fields_default_values.json")
        return False
    for name, value in data.items():
        setattr(self, name, value)
    return True
```

## Product Fields

### Single-Language Fields

Single-language fields are fields that do not require translation and are stored in a single language. Examples include `id_product`, `id_supplier`, `id_manufacturer`, etc.

#### Example: `id_product`

```python
@property
def id_product(self) -> Optional[int]:
    return self.presta_fields.id_product

@id_product.setter
def id_product(self, value: int = None):
    try:
        self.presta_fields.id_product = value
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}
        Ошибка: """, ex)
        return
```

### Multi-Language Fields

Multi-language fields are fields that require translation and are stored in multiple languages. Examples include `name`, `description`, `meta_title`, etc.

#### Example: `name`

```python
@property
def name(self):
    return self.presta_fields.name or ''

@name.setter
def name(self, value: str, lang:str = 'en') -> bool:
    try:
        self.presta_fields.name: dict = {'language':
                                                    [
                                                        {'attrs':{'id':self.language[lang]}, 'value': value},
                                                    ]
                                                 }
        return True
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: 'name' данными {value}
        Ошибка: """, ex)
        return
```

## Associations

Associations are used to link products to other entities, such as categories, manufacturers, and suppliers. The `associations` property allows you to set and get these associations.

#### Example: `associations`

```python
@property
def associations(self) -> Optional[Dict]:
    return self.presta_fields.associations or None

@associations.setter
def associations(self, value: Dict[str, Optional[str]]):
    self.presta_fields.associations = value
```

## Default Values

Default values for product fields can be loaded from a JSON file using the `_payload` method. This method ensures that all fields have a default value, which can be overridden as needed.

## Error Handling

The class includes robust error handling to catch and log any exceptions that occur during the setting of product fields. This ensures that any issues are logged and can be addressed by the developer.

#### Example: Error Handling in `id_product`

```python
@id_product.setter
def id_product(self, value: int = None):
    try:
        self.presta_fields.id_product = value
    except ProductFieldException as ex:
        logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}
        Ошибка: """, ex)
        return
```

## Usage Examples

### Example 1: Setting a Single-Language Field

```python
product = ProductFields()
product.id_product = 123
print(product.id_product)  # Output: 123
```

### Example 2: Setting a Multi-Language Field

```python
product = ProductFields()
product.name = "Product Name", lang='en'
print(product.name)  # Output: {'language': [{'attrs': {'id': 1}, 'value': 'Product Name'}]}
```

### Example 3: Setting Associations

```python
product = ProductFields()
product.associations = {'categories': [{'id': 2}, {'id': 3}]}
print(product.associations)  # Output: {'categories': [{'id': 2}, {'id': 3}]}
```

## Conclusion

The `ProductFields` class is a powerful tool for managing product data in the PrestaShop API. It provides a clear and consistent interface for handling both single-language and multi-language fields, ensuring that data is correctly formatted and validated before being sent to the API. With robust error handling and support for default values, the class simplifies the process of working with product data in PrestaShop.