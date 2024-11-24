Computer Builder Assistant
=========================

This module provides an assistant for building computers.  It takes a JSON input of components and generates a detailed description of the resulting build in Hebrew and Russian, including build type probabilities.


.. automodule:: hypotez.src.endpoints.kazarinov.instructions.command_instruction_mexiron
    :members:
    :undoc-members:
    :show-inheritance:


Build Generation
---------------

.. autofunction:: hypotez.src.endpoints.kazarinov.instructions.command_instruction_mexiron.build_computer
    :noindex:
    :show-inheritance:
    :special-members:


Example Usage
------------

This example demonstrates how to use the `build_computer` function.


.. code-block:: python
    import json

    input_data = [
        {"product_id": "<leave as is>", "product_title": "<component name>", "product_description": "<description and specs>", "image_local_saved_path": "<leave as is>"},
        {"product_id": "<leave as is>", "product_title": "<component name>", "product_description": "<description and specs>", "image_local_saved_path": "<leave as is>"}
    ]
    input_json = json.dumps(input_data)

    output = build_computer(input_json)

    print(output)

.. note:: Replace placeholders like `<component name>` with actual component data.


.. toctree::
    :maxdepth: 2
    :caption: Modules

    modules/module_name