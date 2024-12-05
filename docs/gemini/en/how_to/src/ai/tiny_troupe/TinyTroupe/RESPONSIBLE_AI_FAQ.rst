rst
How to use this TinyTroupe code documentation
========================================================================================

Description
-------------------------
This documentation provides an overview of the TinyTroupe library, an experimental Python library designed for simulating people with specific personalities and goals.  It explains how TinyTroupe utilizes Language Models (LLMs) for realistic simulated behavior, and its intended uses and limitations.

Execution steps
-------------------------
1. **Understanding the Purpose:**  TinyTroupe is a simulation tool, not a direct AI or machine learning model. It leverages external APIs (like GPT-4) to generate simulated agent behavior. The library focuses on creating simulations of human interactions, not on building systems that directly interact with users.

2. **Simulating Personas:**  Define agent characteristics (age, nationality, location, interests, job) to create simulated personas.

3. **Designing Interactions:** Define the conversations or scenarios to simulate. The user provides input to the agents, specifying interactions.

4. **Specifying Environments:** The library allows for the specification of environments in which agents interact.

5. **Extracting Structured Output:** The simulation will produce outputs that can be extracted into structured data formats.  This extracted information is useful for analysis.

6. **Enriching Simulations:** TinyTroupe tools can be used to add realism to simulations.

7. **Understanding Limitations:** TinyTroupe, relying on external LLM capabilities, does not inherently control for potentially malicious or undesirable outputs.  Users need to implement safeguards for their applications using TinyTroupe.

8. **Responsible Use:**  TinyTroupe should not be used for direct user interaction, policy decisions, or anything with real-world consequences without implementation of safeguards against the simulated agent generating malicious or inappropriate output.

9. **Utilizing External Safety Mechanisms:** Leverage external APIs like Azure OpenAI for added safety.

10. **Non-malicious Personas:** Design personas and simulations that do not encourage or result in undesirable output.


Usage example
-------------------------
.. code-block:: python

    # This is a conceptual example, actual usage will depend on specific TinyTroupe implementation.

    from tiny_troupe import TinyWorld, TinyPerson

    # Define personas (example)
    persona1 = {
        "name": "Alice",
        "age": 30,
        "location": "New York",
        "interests": ["reading", "hiking"]
    }

    persona2 = {
        "name": "Bob",
        "age": 25,
        "location": "London",
        "interests": ["coding", "music"]
    }

    # Create TinyPerson objects from the persona data
    alice = TinyPerson(persona1)
    bob = TinyPerson(persona2)

    # Create a TinyWorld object
    world = TinyWorld()
    world.add_person(alice)
    world.add_person(bob)

    # Simulate conversation between Alice and Bob (example)
    conversation = world.simulate_conversation(alice, bob, "Hello!")


    # Extract structured output (example)
    extracted_data = world.extract_data(conversation)
    print(extracted_data)