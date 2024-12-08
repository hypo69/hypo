rst
How to use the TinyStory class
========================================================================================

Description
-------------------------
This class (`TinyStory`) is designed to generate stories from interactions within a TinyTroupe simulation. It can take an environment or an agent as input to build the context for the story.  The class utilizes OpenAI's API through `openai_utils` and helper functions in `tinytroupe.utils` to generate stories, allowing for custom purposes, requirements, and word counts. It handles constructing the story, including details from provided environments or agents, and can be used to create or continue a story.

Execution steps
-------------------------
1. **Initialization:** Instantiate a `TinyStory` object.  Provide either an `environment` or an `agent` (but not both), along with other optional parameters like `purpose`, `context`, numbers of interactions to include (`first_n`, `last_n`), and whether to include information about omitted interactions (`include_omission_info`). Raise exceptions if no environment or agent is provided, or if both are provided.

2. **Starting the Story:** Call the `start_story()` method to generate the initial story content.  Specify `requirements` for the story's focus and desired length (in words). Optionally, set `include_plot_twist` to include a potential plot twist.

3. **Continuing the Story:** Call the `continue_story()` method to generate a continuation of the story. Same parameters as `start_story` apply.

4. **Accessing the Generated Story:** Access the generated story content by checking the `current_story` attribute of the `TinyStory` object.


Usage example
-------------------------
.. code-block:: python

    from tinytroupe.story import TinyStory
    from tinytroupe.agent import TinyPerson  # Assuming you have a TinyPerson object
    from tinytroupe.environment import TinyWorld # Assuming you have a TinyWorld object

    # Example using an agent:
    agent = TinyPerson()
    story = TinyStory(agent=agent, purpose="A story about an agent's journey.")
    story.start_story(requirements="Describe the agent's initial actions.", number_of_words=50)
    print(story.current_story)
    story.continue_story(requirements="Elaborate on the agent's adventures.", number_of_words=100)
    print(story.current_story)


    # Example using an environment:
    world = TinyWorld()
    story = TinyStory(environment=world, purpose="A story about the world's events.")
    story.start_story(requirements="Describe the world's starting conditions.", number_of_words=50)
    print(story.current_story)
    story.continue_story(requirements="Tell the story of the significant events.", number_of_words=100)
    print(story.current_story)