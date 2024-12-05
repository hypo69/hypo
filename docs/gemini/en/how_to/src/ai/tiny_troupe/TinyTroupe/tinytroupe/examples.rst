rst
How to use this code block
=========================================================================================

Description
-------------------------
This code defines functions to create instances of `TinyPerson` objects, each representing a different person with various attributes like age, occupation, routine, and personality traits.  The code demonstrates how to use the `define()`, `define_several()` methods of the `TinyPerson` class to populate these attributes with detailed descriptions and data.  These examples can be modified to create custom agents with specific characteristics.


Execution steps
-------------------------
1. **Import the `TinyPerson` class:** The code starts by importing the `TinyPerson` class from the `tinytroupe.agent` module.

2. **Define functions for creating specific TinyPerson instances:**  Functions like `create_oscar_the_architect()`, `create_lisa_the_data_scientist()`, `create_marcos_the_physician()` and `create_lila_the_linguist()` are created. Each function is responsible for creating and configuring a `TinyPerson` object.

3. **Initialize a `TinyPerson` object:** Inside each function, a `TinyPerson` object is instantiated with a name (e.g., "Oscar").

4. **Define individual attributes:** The `define()` method is used to set attributes like "age," "nationality," "occupation," and "routine" for the person.

5. **Define multiple attributes at once:** The `define_several()` method is used to define multiple related attributes (e.g., "personality_traits," "professional_interests," etc.) in a concise way. Each attribute is stored as a dictionary, allowing for structured data.

6. **Define detailed descriptions:** The code provides comprehensive descriptions for various attributes using multiline strings for detailed information, especially for "occupation_description."


Usage example
-------------------------
.. code-block:: python

    from tinytroupe.agent import TinyPerson
    from hypotez.src.ai.tiny_troupe.TinyTroupe.tinytroupe.examples import create_oscar_the_architect

    # Create an Oscar object
    oscar = create_oscar_the_architect()

    # Access and print specific attributes
    print(oscar.get("age"))
    print(oscar.get("occupation"))
    print(oscar.get("occupation_description"))
    print(oscar.get_several("personality_traits"))