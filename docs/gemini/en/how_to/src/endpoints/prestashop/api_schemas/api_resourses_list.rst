rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a list named `resource` containing strings.  Each string represents a resource available for API calls within a PrestaShop application.  The list likely serves as a reference for the available endpoints in the API, potentially used for handling requests or validating inputs.

Execution steps
-------------------------
1. The code initializes a variable `MODE` to the string 'dev'. This likely controls settings or behaviors related to the environment (e.g., development or production).
2. The code then assigns a list of strings to the variable `resource`. This list contains numerous resource names, each potentially corresponding to an API endpoint (e.g., 'products', 'categories', 'orders').
3. The list elements are strings representing various resources accessible through PrestaShop's API.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.api_schemas.api_resourses_list import resource

    # Print the list of resources
    print(resource)

    # Check if a specific resource exists
    if 'products' in resource:
        print("The 'products' resource is available.")
    else:
        print("The 'products' resource is not available.")

    # Iterate over the resources and print each one
    for res in resource:
        print(res)