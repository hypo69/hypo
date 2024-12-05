rst
How to use the `tinytroupe.experimentation.ABRandomizer` class
=========================================================================================

Description
-------------------------
This code defines unit tests for the `ABRandomizer` class, which is part of the `tinytroupe` library.  It validates the `randomize`, `derandomize`, `derandomize_name`, and `passtrough_name` methods of the class by checking if they produce the expected results for different input values. The tests ensure consistent randomization and correct derandomization.  Crucially, the tests employ a loop to run multiple iterations, increasing confidence in the correctness of the randomization logic.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `pytest` framework, system path manipulation tools (`sys`), the `testing_utils` module (assumed to exist elsewhere), and the `ABRandomizer` class from the `tinytroupe.experimentation` module.


2. **Define test functions:** Several test functions (`test_randomize`, `test_derandomize`, `test_derandomize_name`, `test_passtrough_name`, `test_intervention_1`) are defined to test different aspects of the `ABRandomizer` class.


3. **Instantiate `ABRandomizer`:** An instance of `ABRandomizer` is created within each test function.


4. **Call `randomize`:** The `randomize` method is called with input parameters to simulate an experiment.


5. **Check randomization outcomes:** Assertions are made to verify that the output of the `randomize` method matches the expected randomized result.


6. **Call `derandomize`:** The `derandomize` method is called to reverse the randomization.


7. **Validate derandomization:** Assertions check if the `derandomize` method correctly recovers the original options.


8. **Test `derandomize_name`:**  This test function checks that the `derandomize_name` function accurately converts the randomized names to their original names (either 'control' or 'treatment').


9. **Test `passtrough_name`:** This function tests how the `ABRandomizer` handles inputs specified within the `passtrough_name` parameter.


10. **Handle `test_intervention_1` (TODO):**  This test function is marked as a placeholder (`pass`) and requires future implementation.


Usage example
-------------------------
.. code-block:: python

    import sys
    sys.path.append('path/to/tinytroupe')  # Replace with the actual path
    from tinytroupe.experimentation import ABRandomizer

    randomizer = ABRandomizer(passtrough_name=["option3"])
    option_a = "option1"
    option_b = "option2"
    experiment_id = 0

    a, b = randomizer.randomize(experiment_id, option_a, option_b)
    real_name = randomizer.derandomize_name(experiment_id, a)
    
    print(f"Randomized options: {a}, {b}")
    print(f"Original name: {real_name}")