# src.suppliers

## Overview

This module defines the `Supplier` class and related functionality for extracting data from various suppliers. Each supplier has specific methods for retrieving information, which extend the base `Supplier` class and are integrated through the `supplier.related_functions` interface.  Supplier-specific methods reside in directories named `<supplier_prefix>`, e.g., `amazon`, `aliexpress`, `morlevi`.  `<supplier_prefix>` is determined during the creation of a new supplier in the system and typically based on an abbreviation of the supplier's name or website.

## Relationships: Supplier, Driver, Product

![Supplier-Warehouse-Client](supplier-warehouse-client.png)


## Classes

### `Supplier`

**Description**:  Base class for all suppliers. Provides a common interface for interacting with different data sources.


## Functions

(No functions defined in the provided snippet)


## Variables

### `MODE`

**Description**:  A string variable used to identify the current operation mode (e.g., 'dev', 'prod').


```python
MODE = 'dev'
```