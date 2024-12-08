rst
How to use the ABRandomizer class
========================================================================================

Description
-------------------------
This code defines a class `ABRandomizer` for randomizing and de-randomizing choices between two options (A and B). It also handles cases where certain names should not be randomized.  The class maintains a record of the randomization to allow for de-randomization later. It's useful for A/B testing or similar scenarios where you need to switch between choices in a dataset while keeping track of the original assignment.


Execution steps
-------------------------
1. **Import necessary libraries:** Import `random`, `pandas` (though it's not directly used in `ABRandomizer`), and `TinyPerson` from the `tinytroupe.agent` module.

2. **Create an `ABRandomizer` instance:** Initialize the `ABRandomizer` class, specifying:
   - `real_name_1`: The actual name of option 1 in your data.
   - `real_name_2`: The actual name of option 2 in your data.
   - `blind_name_a`: The name of option 1 presented to the user.
   - `blind_name_b`: The name of option 2 presented to the user.
   - `passtrough_name`: A list of names that should not be randomized (e.g., control groups).
   - `random_seed`: An integer to set the random seed for reproducibility.

3. **Randomize choices:** Call the `randomize` method, providing the index (`i`) of the item and the two choices (`a` and `b`). This method randomly swaps `a` and `b` and stores the result in the `choices` dictionary.

4. **De-randomize choices:** To get back to the original assignments, call the `derandomize` method with the corresponding index (`i`) and choices (`a` and `b`).

5. **De-randomize user choice:** To get the actual option from the user's input `blind_name`, call the `derandomize_name` method with the index (`i`) and the `blind_name`  chosen by the user. This method returns the real name of the option.

6. **Error Handling:** The code includes robust error handling in `derandomize` and `derandomize_name` methods to catch cases where an item's randomization is not found.

Usage example
-------------------------
.. code-block:: python

    import random
    import pandas as pd
    from tinytroupe.agent import TinyPerson

    # Example Usage
    randomizer = ABRandomizer(real_name_1="control", real_name_2="treatment",
                               blind_name_a="A", blind_name_b="B",
                               passtrough_name=["control"], random_seed=42)

    a = "option_A"
    b = "option_B"
    i = 0

    random_a, random_b = randomizer.randomize(i, a, b)
    print(f"Randomized choices for item {i}: {random_a}, {random_b}")


    original_a, original_b = randomizer.derandomize(i, random_a, random_b)
    print(f"Original choices for item {i}: {original_a}, {original_b}")


    user_choice = "A"
    real_choice = randomizer.derandomize_name(i, user_choice)
    print(f"The real choice is: {real_choice}")


    user_choice = "control"
    real_choice = randomizer.derandomize_name(i, user_choice)
    print(f"The real choice is: {real_choice}")