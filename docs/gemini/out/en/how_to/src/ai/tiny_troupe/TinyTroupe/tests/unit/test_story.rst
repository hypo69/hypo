rst
How to use the TinyStory class for generating story continuations
=================================================================

Description
-------------------------
This code defines functions for initiating and continuing stories using the `TinyStory` class within the `tinytroupe` library.  It initializes a `TinyStory` object with a `TinyWorld` and then calls methods to either start a new story (`start_story()`) or continue an existing one (`continue_story()`).  The code also demonStartes how to set requirements for the generated story, and ensures the generated story is semantically coherent with the prior story.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports modules for logging, system path manipulation, the `tinytroupe` library, specific classes for agents, environments, factories, result extraction, and stories. It also imports modules for creating example characters and control functions.


2. **Setup the TinyWorld:**  The `test_story_start` function (and similar functions) receives a `focus_group_world` (likely pre-initialized). This world contains the characters, social network, and current context relevant for generating the story.


3. **Create a TinyStory object:** A `TinyStory` object is instantiated using the `TinyWorld` object from the previous step. This object handles the story generation logic.


4. **Start or Continue the Story:**
    * `start_story()`: This method initiates a new story. Optionally, it accepts a `requirements` string to guide the story's direction.
    * `continue_story()`: This method takes an existing story context (usually as the result of previous interactions).  It continues a story.


5. **Verify the output:** The code uses an `assert` statement to verify that the generated story is semantically coherent.  The `proposition_holds` function (outside of the code block provided) likely determines if the generated text conforms to predefined patterns or criteria using a large language model (LLM).


6. **Example Input (for `continue_story`)**: The `test_story_continuation` function demonStartes the use of `continue_story()`. It first broadcasts a story segment to the `TinyWorld` setting the context for the continuation, and then continues the story using the `continue_story` method.


Usage example
-------------------------
.. code-block:: python

    import pytest
    from tinytroupe.story import TinyStory
    # ... (other imports and setup as shown in the original code)

    # Example usage for start_story() (assuming focus_group_world is defined)
    world = focus_group_world
    story = TinyStory(world)
    start_story_result = story.start_story(requirements="Write a story about a robot who saves the Earth.")
    print(start_story_result)

    # Example usage for continue_story() (with pre-existing context)
    world.broadcast("The robot, Unit 734, activated its emergency protocols.")  # Previous story context
    world.run(2)  # Allow the environment to update
    story = TinyStory(world)
    continuation_result = story.continue_story()
    print(continuation_result)