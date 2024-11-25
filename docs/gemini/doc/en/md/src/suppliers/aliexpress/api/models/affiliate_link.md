# AffiliateLink Model

## Overview

This module defines the `AffiliateLink` class, representing an affiliate link on AliExpress.  It holds information about the promotion link and its source value.

## Table of Contents

* [AffiliateLink](#affiliate-link)

## Classes

### `AffiliateLink`

**Description**: This class represents an affiliate link on AliExpress, containing the promotion link and its source value.

**Attributes**:

- `promotion_link` (str): The actual promotional link.
- `source_value` (str): The source value associated with the link.


```python
class AffiliateLink:
    promotion_link: str
    source_value: str
```