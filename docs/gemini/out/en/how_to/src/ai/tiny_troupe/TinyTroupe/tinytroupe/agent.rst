rst
How to use the TinyTroupe agent module
========================================================================================

Description
-------------------------
This module defines the `TinyPerson` class, a core component for representing simulated people within the TinyTroupe system.  It handles agent interaction, memory management (both episodic and semantic), and cognitive updates.  Crucially, TinyTroupe agents are designed to model human-like behavior, including idiosyncrasies and emotions, contrasting with agents intended for pure task completion. The module also includes utility functions for configuration, memory management, and agent interaction, along with example implementations of `TinyMentalFaculty` subclasses (e.g., `RecallFaculty`, `FilesAndWebGroundingFaculty`) that provide specific cognitive abilities.


Execution steps
-------------------------
1. **Import the necessary modules:** The code imports various Python modules, including `os`, `csv`, `json`, `ast`, `textwrap`, `datetime`, `chevron`, `logging`, `rich`, `copy`, and custom modules from the `tinytroupe` package.  These imports provide the required functionalities for file handling, JSON processing, text formatting, logging, display output, memory management, and agent-environment interaction.

2. **Define default parameter values:** The module initializes default parameter values for parameters like the embedding model and maximum content display length from a configuration file. These values can be customized as per the application's needs.

3. **Configure LLaMa-Index:** This step configures the embedding model for use with LLaMa-Index, a large language model index library.  The code sets the `Settings.embed_model` to an `OpenAIEmbedding` instance, specifying the embedding model.

4. **Define the `TinyPerson` class:** The `TinyPerson` class encapsulates the behavior of a simulated person. The class is designed to be `JsonSerializableRegistry`, enabling easy serialization and deserialization of agent states.

5. **Implement Agent Initialization:** The `__init__` method of the `TinyPerson` class takes arguments defining the agent's name, episodic memory, semantic memory, and mental faculties (if any).  Important initialization steps are delegated to the `_post_init` method.

6. **Configure agent state:** In the `_post_init` method, default values for agent state attributes (e.g., current messages, actions buffer, accessible agents, configuration dictionary) are set up.   The code sets up a default configuration, including attributes like `name`, `age`, `occupation`, `routines`, `personality_traits`, `current_location`, and others. Critical elements are parsed using a Mustache template (`tinyperson.mustache`).

7. **Initialization of prompts and messages:** The agent's initial system message, derived from the template, is rendered, along with messages retrieved from memory (`episodic_memory`).  A "reset prompt" function clears and reinitializes these messages.

8. **Agent configuration management:** The `define`, `define_several`, `define_relationships`, and `clear_relationships` methods manage the agent's attributes, enabling dynamic updates and modifications to the agent's configuration.

9. **Agent interactions (`act`, `listen`, `see`, etc.):** Methods like `act`, `listen`, `socialize`, `see`, `think`, and `internalize_goal` are provided to allow interaction with the environment, through the exchange of stimuli, thought, and actions.  These interactions are managed transactionally (`@transactional`).

10. **Interaction and action storage:** Actions performed by the agent are stored in a buffer (`_actions_buffer`). The agent produces responses (`_produce_message`), storing messages in memory. Communication displays are handled to show the interactions.

11. **State Updates (`_update_cognitive_state`):** This method updates agent attributes based on interactions with the environment, including cognitive states (goals, attention, emotions), datetime, context, and location.

12. **Display and Handling Communication:** The `_display_communication` method handles how communications are displayed (interactively or within an environment).


Usage example
-------------------------
.. code-block:: python

    from tinytroupe.agent import TinyPerson

    # Create a new agent
    agent = TinyPerson(name="Agent1")

    # Add a document to the semantic memory.
    agent.read_documents_from_folder("./documents")

    # Perform an action (e.g., asking a question)
    agent.listen_and_act("What is the capital of France?")

    # Print the agent's response.
    print(agent.pp_current_interactions())

    # Save agent configuration to a file
    agent.save_spec("./agent1.json")

    # Load an existing agent
    loaded_agent = TinyPerson.load_spec("./agent1.json")