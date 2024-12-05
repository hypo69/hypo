rst
How to initialize a Gemini model with a system instruction
=========================================================================================

Description
-------------------------
This code snippet defines the `__init__` method for the Gemini model.  It allows the initialization of a Gemini model instance with an optional `system_instruction`.  This instruction, passed to the model at initialization, remains constant throughout the instance's lifetime.  It's crucial for maintaining consistency in the model's behavior.

Execution steps
-------------------------
1. **Initialization with `system_instruction`:** The `__init__` method accepts a `system_instruction` parameter.  If provided, it stores the `system_instruction` value for the model instance.
2. **Setting other model parameters:**  The method also accepts other parameters like `api_key`, `model_name`, and `generation_config`, necessary for model initialization.  These parameters allow users to customize the model's configuration and connect to the API.
3. **Storing the instruction:** The provided `system_instruction` is stored internally within the model object to ensure it's consistently used by the model.
4. **Handling potential errors (not shown):** Internal error handling might be present to manage cases where the `system_instruction` is not in the correct format or missing necessary details, but this is not visible in the code snippet.

Usage example
-------------------------
.. code-block:: python

    from typing import Optional, Dict
    # ... (import necessary libraries, other class definitions, etc.)

    # Initialize the Gemini model with a system instruction
    gemini_model = Gemini(
        api_key="YOUR_API_KEY",
        system_instruction="Respond in a concise and informative manner."
    )

    # Now the 'gemini_model' object can be used with the system instruction.
    # Example usage:
    response = gemini_model.generate_text("...")