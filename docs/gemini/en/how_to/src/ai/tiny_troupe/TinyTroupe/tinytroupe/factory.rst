rst
How to use the TinyFactory class
========================================================================================

Description
-------------------------
This code defines a base class `TinyFactory` and a subclass `TinyPersonFactory` for creating and managing factory instances.  `TinyFactory` provides methods for adding, retrieving, and clearing factory instances.  `TinyPersonFactory` extends this to specifically generate `TinyPerson` instances using OpenAI's LLM. It also includes caching mechanisms to ensure consistent data handling across multiple operations.

Execution steps
-------------------------
1. **Import necessary modules:** The code starts by importing `os`, `json`, `chevron`, `logging`, `copy`, `openai_utils`, `TinyPerson`, `utils`, and `transactional` from various modules.  A logger is also initialized.

2. **Define the TinyFactory class:** This class encapsulates factory logic and contains static methods for managing all created factories.
    * `__init__(self, simulation_id=None)`: Initializes a `TinyFactory` instance, assigning a unique name and an optional `simulation_id`.
    * `__repr__(self)`: Returns a string representation of the `TinyFactory` instance.
    * `add_factory(factory)`: Adds a factory to the global `all_factories` dictionary, checking for name uniqueness.
    * `set_simulation_for_free_factories(simulation)`: Assigns a simulation to factories that don't have one.
    * `clear_factories()`: Clears the global `all_factories` dictionary.
    * `encode_complete_state(self)`: Creates a deep copy of the factory's state attributes to be serialized.  Subclasses should override for custom data.
    * `decode_complete_state(self, state)`: Restores the factory's state from a serialized dictionary. This allows for transactional caching of factory states.


3. **Define the TinyPersonFactory class:** This class inherits from `TinyFactory` and is responsible for generating `TinyPerson` instances using OpenAI's LLM.
    * `__init__(self, context_text, simulation_id=None)`: Initializes a `TinyPersonFactory`, storing context text and initializing lists to track generated `TinyPerson` instances.
    * `generate_person_factories(number_of_factories, generic_context_text)`: Generates a list of `TinyPersonFactory` instances using OpenAI's LLM based on a given context.
    * `generate_person(self, agent_particularities=None, temperature=1.5, attempts=5)`: Generates a `TinyPerson` instance using OpenAI's LLM, incorporating any agent-specific details and handling potential errors during generation.
    * `_aux_model_call(self, messages, temperature)`: An auxiliary method to make model calls, used to integrate the transactional decorator.
    * `_setup_agent(self, agent, configuration)`: Sets up the generated `TinyPerson` agent with its specified configuration.


4. **Transactional decorator (`@transactional`)**: This decorator is used on methods to support transactional caching by saving the state before executing the method and restoring the previous state if an exception occurs.


Usage example
-------------------------
.. code-block:: python

    import logging
    from tinytroupe.factory import TinyPersonFactory

    logging.basicConfig(level=logging.INFO)

    # Example usage of generate_person_factories:
    context_text = "A group of friends are on a camping trip."
    number_of_factories = 3
    factories = TinyPersonFactory.generate_person_factories(number_of_factories, context_text)

    if factories:
        for factory in factories:
            person = factory.generate_person()
            if person:
                print(f"Generated TinyPerson: {person.get('name')}")
            else:
                print("Failed to generate a TinyPerson.")
    else:
        print("Failed to generate TinyPerson factories.")