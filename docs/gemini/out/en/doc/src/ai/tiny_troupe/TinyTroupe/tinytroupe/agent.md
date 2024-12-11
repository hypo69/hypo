# tinytroupe.agent

## Overview

This module provides the core classes and functions for TinyTroupe agents. Agents are simulated entities capable of interacting with other agents and the environment by receiving stimuli and producing actions.  They have cognitive states, including memory (episodic and semantic), mental faculties, and more human-like characteristics like emotions and goals compared to agents designed solely for productivity tools. The design draws inspiration from cognitive psychology.  Crucial methods include `listen`, `act`, and various methods for managing internal states and interacting with the environment.


## Table of Contents

* [TinyPerson](#tiny-person)
* [Mental Faculties](#mental-faculties)
* [Memory Mechanisms](#memory-mechanisms)


## TinyPerson

### `TinyPerson`

**Description**: This class represents a simulated person within the TinyTroupe universe.  It encapsulates the agent's cognitive state, memory, and interactions with the environment.

**Parameters**:

* `name` (str): The name of the TinyPerson.  Required.
* `episodic_memory` (EpisodicMemory, optional): The memory implementation for storing recent interactions. Defaults to `EpisodicMemory()`.
* `semantic_memory` (SemanticMemory, optional): The memory implementation for storing general knowledge. Defaults to `SemanticMemory()`.
* `mental_faculties` (list, optional): A list of mental faculties to add to the agent. Defaults to `None`.


**Methods**:

* [`__init__(self, name: str=None, episodic_memory=None, semantic_memory=None, mental_faculties: list=None)`](#tiny-person-init): Creates a new TinyPerson instance.
* [`_post_init(self, **kwargs)`](#tiny-person-post-init): Called after the `__init__` method, handling default values and agent regiStartion.
* [`generate_agent_prompt(self)`](#tiny-person-generate-agent-prompt): Generates the prompt string for the agent based on its configuration.
* [`reset_prompt(self)`](#tiny-person-reset-prompt): Resets the internal prompt messages for the agent.
* [`get(self, key)`](#tiny-person-get): Retrieves the value associated with a key in the agent's configuration.
* [`define(self, key, value, group=None)`](#tiny-person-define): Defines a new value in the agent's configuration.
* [`define_several(self, group, records)`](#tiny-person-define-several): Defines multiple values for a specified group.
* [`define_relationships(self, relationships, replace=True)`](#tiny-person-define-relationships): Defines or updates the agent's relationships with other agents.
* [`clear_relationships(self)`](#tiny-person-clear-relationships): Clears the list of relationships.
* [`related_to(self, other_agent, description, symmetric_description=None)`](#tiny-person-related-to): Defines a relationship between this agent and another agent.
* [`add_mental_faculties(self, mental_faculties)`](#tiny-person-add-mental-faculties): Adds a list of mental faculties to the agent.
* [`add_mental_faculty(self, faculty)`](#tiny-person-add-mental-faculty): Adds a single mental faculty to the agent.
* [`act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`](#tiny-person-act): Performs actions in the environment.
* [`listen(self, speech, source: AgentOrWorld=None, max_content_length=default["max_content_display_length"])`](#tiny-person-listen): Processes incoming speech from other agents.
* [`socialize(self, social_description, source: AgentOrWorld=None, max_content_length=default["max_content_display_length"])`](#tiny-person-socialize): Processes social stimuli.
* [`see(self, visual_description, source: AgentOrWorld=None, max_content_length=default["max_content_display_length"])`](#tiny-person-see): Processes visual stimuli.
* [`think(self, thought, max_content_length=default["max_content_display_length"])`](#tiny-person-think): Processes internal thoughts.
* [`internalize_goal(self, goal, max_content_length=default["max_content_display_length"])`](#tiny-person-internalize-goal): Internalizes a goal.
* [`_observe(self, stimulus, max_content_length=default["max_content_display_length"])`](#tiny-person-_observe): Handles observation of various stimuli.
* [`listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"])`](#tiny-person-listen-and-act): Combines `listen` and `act`.
* [`see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`](#tiny-person-see-and-act): Combines `see` and `act`.
* [`think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"])`](#tiny-person-think-and-act): Combines `think` and `act`.
* [`read_documents_from_folder(self, documents_path:str)`](#tiny-person-read-documents-from-folder): Reads documents from a folder and adds them to the semantic memory.
* [`read_documents_from_web(self, web_urls:list)`](#tiny-person-read-documents-from-web): Reads documents from web URLs and adds them to the semantic memory.
* [`move_to(self, location, context=[])`](#tiny-person-move-to): Moves to a new location and updates the context.
* [`change_context(self, context: list)`](#tiny-person-change-context): Changes the context.
* [`make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.")`](#tiny-person-make-agent-accessible): Makes another agent accessible to this agent.
* [`make_agent_inaccessible(self, agent: Self)`](#tiny-person-make-agent-inaccessible): Makes an agent inaccessible.
* [`make_all_agents_inaccessible(self)`](#tiny-person-make-all-agents-inaccessible): Makes all agents inaccessible.
* [`_produce_message(self)`](#tiny-person-_produce-message): Sends messages to the OpenAI API.
* [`_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`](#tiny-person-_update-cognitive-state): Updates the agent's cognitive state.
* [`_display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`](#tiny-person-_display-communication): Displays communication.
* [`_push_and_display_latest_communication(self, rendering)`](#tiny-person-_push-and-display-latest-communication): Pushes communication to the buffer and displays.
* [`pop_and_display_latest_communications(self)`](#tiny-person-pop-and-display-latest-communications): Pops and displays latest communications from the buffer.
* [`clear_communications_buffer(self)`](#tiny-person-clear-communications-buffer): Clears the communications buffer.
* [`pop_latest_actions(self) -> list`](#tiny-person-pop-latest-actions): Returns the latest actions performed by this agent.
* [`pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`](#tiny-person-pop-actions-and-get-contents-for): Returns the contents of actions of a given type.
* [`__repr__(self)`](#tiny-person-repr): Returns a string representation of the agent.
* [`minibio(self)`](#tiny-person-minibio): Returns a mini-biography of the agent.
* [`pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`](#tiny-person-pp-current-interactions): Pretty prints the current interactions (uses `rich`).
* [`pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`](#tiny-person-pretty-current-interactions): Returns a string with pretty printed interactions (uses `rich`).
* [`_pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> list`](#tiny-person-_pretty-stimuli): Formats stimuli for display.
* [`_pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str`](#tiny-person-_pretty-action): Formats actions for display.
* [`_pretty_timestamp(self, role, timestamp)`](#tiny-person-_pretty-timestamp): Formats timestamps for display.
* [`iso_datetime(self) -> str`](#tiny-person-iso-datetime): Returns the environment's current datetime in ISO format, or `None` if not available.
* [`save_spec(self, path, include_mental_faculties=True, include_memory=False)`](#tiny-person-save-spec): Saves the agent's specification to a JSON file.
* [`load_spec(self, path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`](#tiny-person-load-spec): Loads a TinyPerson from a JSON file.
* [`encode_complete_state(self) -> dict`](#tiny-person-encode-complete-state): Encodes the complete agent state for serialization.
* [`decode_complete_state(self, state: dict) -> Self`](#tiny-person-decode-complete-state): Decodes a serialized agent state into a new TinyPerson instance.
* [`create_new_agent_from_current_spec(self, new_name:str) -> Self`](#tiny-person-create-new-agent-from-current-spec): Creates a new agent from the current one's spec with a unique name.
* [`add_agent(self, agent)`](#tiny-person-add-agent): Adds an agent to the global list of agents.
* [`has_agent(self, agent_name: str)`](#tiny-person-has-agent): Checks if an agent is registered.
* [`set_simulation_for_free_agents(self, simulation)`](#tiny-person-set-simulation-for-free-agents): Sets the simulation for free agents.
* [`get_agent_by_name(self, name)`](#tiny-person-get-agent-by-name): Gets an agent by name.
* [`clear_agents()`](#tiny-person-clear-agents): Clears the global list of agents.


### `TinyPerson.__init__`
```python
def __init__(self, name: str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties: list=None):
    """
    Creates a TinyPerson.

    Args:
        name (str): The name of the TinyPerson. Either this or spec_path must be specified.
        episodic_memory (EpisodicMemory, optional): The memory implementation to use. Defaults to EpisodicMemory().
        semantic_memory (SemanticMemory, optional): The memory implementation to use. Defaults to SemanticMemory().
        mental_faculties (list, optional): A list of mental faculties to add to the agent. Defaults to None.
    """
```

(and other methods similarly documented)

## Mental Faculties

### `TinyMentalFaculty`

**Description**: This is the base class for all mental faculties. Mental faculties represent the cognitive abilities of an agent.

(and other mental faculty classes similarly documented, with examples of the prompt return type methods)

## Memory Mechanisms

### `TinyMemory`

**Description**: Base class for different types of memory (episodic and semantic).

(and other memory classes similarly documented)


```