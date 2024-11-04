# `dicst2ns_ns2dict` Module

## `dict2ns()`

The `dict2ns` function recursively converts dictionaries to `SimpleNamespace` objects. It can handle nested dictionaries and lists of dictionaries, converting all of them into `SimpleNamespace` objects.

### How the function works:

1. **Dictionary Handling**: Converts dictionary keys and values to `SimpleNamespace` objects.
2. **List Handling**: Converts lists of dictionaries to lists of `SimpleNamespace` objects.
3. **Non-Dict Data**: Returns other data types unchanged.

### Args:
- **data (dict | list | any)**: The data to convert. This can be a dictionary, a list of dictionaries, or any other data type.

### Returns:
- **SimpleNamespace | list | any**: Converted data as a `SimpleNamespace` object, list of `SimpleNamespace` objects, or the original data if it is not a dictionary or list.

### Example:

```python
>>> from types import SimpleNamespace
>>> data = {
...     'name': 'Alice',
...     'age': 30,
...     'address': {
...         'street': '123 Main St',
...         'city': 'Wonderland'
...     }
... }
>>> ns_obj = dict2ns(data)
>>> print(ns_obj)
namespace(name='Alice', age=30, address=namespace(street='123 Main St', city='Wonderland'))
```

## `ns2dict()`

The `ns2dict` function recursively converts `SimpleNamespace` objects back into dictionaries. It can handle nested `SimpleNamespace` objects and lists of `SimpleNamespace` objects, converting all of them into dictionaries.

### How the function works:

1. **SimpleNamespace Handling**: Converts `SimpleNamespace` objects to dictionaries by iterating through their attributes.
2. **List Handling**: Converts lists of `SimpleNamespace` objects to lists of dictionaries.
3. **Non-SimpleNamespace Data**: Returns other data types unchanged.

### Args:
- **data (Any)**: The data to convert. This can be a `SimpleNamespace` object, a list of `SimpleNamespace` objects, or any other data type.

### Returns:
- **Union[Dict[str, Any], List[Any]]**: Converted data as a dictionary or a list of dictionaries, or the original data if it is not a `SimpleNamespace` object or list.

### Example:

```python
>>> from types import SimpleNamespace
>>> ns_obj = SimpleNamespace(
...     name="Alice",
...     age=30,
...     address=SimpleNamespace(
...         street="123 Main St",
...         city="Wonderland"
...     )
... )
>>> data_dict = ns2dict(ns_obj)
>>> print(data_dict)
{'name': 'Alice', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Wonderland'}}
```
