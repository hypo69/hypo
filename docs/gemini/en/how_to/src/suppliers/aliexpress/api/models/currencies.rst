rst
How to use the currencies.py code block
========================================================================================

Description
-------------------------
This Python code defines a `Currency` class with various constant strings representing different currency codes.  It provides a way to refer to these currencies using named constants rather than string literals, making the code more readable and maintainable.

Execution steps
-------------------------
1. The code defines a class named `Currency`.
2. Within the `Currency` class, several constant variables (`USD`, `GBP`, `CAD`, etc.) are assigned string values representing different currency codes.
3. The code is meant for use in a project where currency codes are frequently used. By using named constants, you avoid typos and make your code easier to understand and update.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.currencies import Currency

    # Accessing currency codes
    print(Currency.USD)  # Output: USD
    print(Currency.EUR)  # Output: EUR
    
    # Example of using in a larger program
    product_price = 100.0
    product_currency = Currency.USD
    print(f"Product price: {product_price} {product_currency}")