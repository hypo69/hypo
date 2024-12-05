rst
How to Use the TinyTroupe Library
========================================================================================

Description
-------------------------
The TinyTroupe library is a Python library for simulating people (TinyPeople) with specific personalities, interests, and goals.  It leverages Large Language Models (LLMs) like GPT-4 to generate realistic simulated behavior in simulated environments (TinyWorld). This allows for investigating human interactions and consumer types, with highly customizable personas and controllable conditions.  The focus is on understanding human behavior, not directly supporting it.

Execution steps
-------------------------
1. **Installation:**
   Clone the repository: `git clone https://github.com/microsoft/tinytroupe`
   Navigate to the repository: `cd tinytroupe`
   Install the library from the local repository (not PyPI): `pip install .`

2. **Environment Setup:**
   Ensure you have Python 3.10 or higher.  You should use a Conda environment (recommended).
   Set appropriate environment variables for your chosen LLM API provider (Azure OpenAI or OpenAI):
   - For Azure OpenAI: Set `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` environment variables.
   - For OpenAI: Set `OPENAI_API_KEY` environment variable.
   - **Crucially**, if using Azure OpenAI, enable content filters for safety.  Refer to the Azure OpenAI documentation for details.

3. **Creating a TinyPerson:**
   Use example builders (e.g., `create_lisa_the_data_scientist`) to quickly create pre-defined agents, or use the `TinyPersonFactory` to generate new agents with specific characteristics from text descriptions.

4. **Creating a TinyWorld:**
   Define a simulation environment using `TinyWorld`, specifying the agents (`TinyPerson` objects) within it.  Ensure everyone is accessible for interaction.

5. **Running the Simulation:**
   Execute the desired interactions and actions using methods like `listen`, `see`, `act`, `listen_and_act`, and `make_everyone_accessible()` within the `TinyWorld`.
   Use the `run()` method on the `TinyWorld` object to initiate the simulation for a set number of steps.

6. **Extracting Results:**
   Utilize utilities like `ResultsExtractor` and `ResultsReducer` to automatically extract and analyze the outcomes of the simulation.  This can help to generate insights or reports.

7. **Caching (Optional but Recommended):**
   For performance, employ caching mechanisms for simulation state and LLM API calls.  Start a recording session with `control.begin()`, checkpoint regularly with `control.checkpoint()`, and end with `control.end()`. Consider LLM API caching using `openai_utils.force_api_cache()` or by modifying your config.ini.

8. **Config Customization:**
    Modify the `config.ini` file (in the same directory as your program or notebook) to customize API type, model parameters, and logging levels.


Usage example
-------------------------
.. code-block:: python

    from tinytroupe.examples import create_lisa_the_data_scientist
    from tinytroupe.world import TinyWorld

    # Create two agents
    lisa = create_lisa_the_data_scientist()
    oscar = TinyPerson("Oscar")

    # Define a TinyWorld
    world = TinyWorld("Chat Room", [lisa, oscar])
    world.make_everyone_accessible()

    # Start the conversation
    lisa.listen("Talk to Oscar to know more about him")
    world.run(4)  # Run for 4 steps

    # Extract results (replace with your extraction logic)
    # ... (e.g., using ResultsExtractor) ...