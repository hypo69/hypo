rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block contains test functions for scenarios involving advertisement evaluation and creation, as well as consumer profiling. It utilizes the TinyTroupe framework for agent-based simulations.  The functions demonstrate how to interact with TinyPerson agents to evaluate advertisements, generate advertising ideas for an apartment, and collect consumer opinions about a product.  The code also includes error handling and assertions to validate the results of the simulations.

Execution steps
-------------------------
1. **Import necessary modules:** The code starts by importing essential libraries like `pytest`, `logging`, `sys`, the TinyTroupe modules (`tinytroupe`, `tinytroupe.agent`, `tinytroupe.environment`, `tinytroupe.factory`, `tinytroupe.extraction`, `tinytroupe.examples`, etc.), and the `control` module.
2. **Define advertisement scenarios:** Multiple strings are defined for advertisements (e.g., `travel_ad_1`, `travel_ad_2`) and contain the text of different advertisement examples.
3. **Define evaluation request message:**  A message (`eval_request_msg`) is formed, prompting the agents to evaluate the provided advertisements and select the most convincing one, explaining the rationale.  This message includes multiple advertisements within code blocks.
4. **Set situation and extraction objective:** A descriptive situation (`situation`) is provided for context, and the `extraction_objective` specifies what data the agents should extract.
5. **Create TinyPerson agents:** Agent objects (`create_oscar_the_architect`, `create_lisa_the_data_scientist`) are instantiated and their context is changed to align with the scenario. The agents will "listen and act" in response to the evaluation message.
6. **Evaluate advertisements:** The `listen_and_act` method is used to have the agents evaluate the advertisements and formulate their opinions. The results are extracted using `ResultsExtractor`
7. **Validate agent responses:** Assertions ensure the agents provide valid responses (including the ad id, title, and justification). The extracted choices are appended to a `choices` list.
8. **Create ad creation scenario:** A new scenario (`test_ad_creation_scenario`) is defined to collect opinions from a simulated focus group to create advertisements for an apartment. This includes details about the apartment's characteristics and specifications.
9. **Broadcast information to the focus group:** The situation, apartment description, and advertising task are broadcast to the focus group for discussion.
10. **Run the focus group simulation:** The focus group simulation runs for a set duration (`focus_group.run(2)`).
11. **Extract focus group results:** The simulation results are extracted, and an assertion validates that the results hold the correct information about the advertisement ideas generated.
12. **Consumer profiling scenario:** A scenario (`test_consumer_profiling_scenario`) is setup to collect consumer opinions on bottled gazpacho. This involves generating numerous consumer agents using the `TinyPersonFactory`, presenting a questionnaire, and collecting their responses.  A checkpoint file is created to persist the data.
13. **Persist results:**  The `control.checkpoint()` function is used to save simulation results during the consumer profiling process.


Usage example
-------------------------
.. code-block:: python

    # Example of how to add a new advertisement to the evaluation process.
    new_ad = """Your new advertisement here."""
    eval_request_msg += f"# AD 5\n```\n{new_ad}\n```\n"


    # Example of how to add a new agent to the focus group scenario.
    other_agent = create_another_agent()
    people.append(other_agent)
```