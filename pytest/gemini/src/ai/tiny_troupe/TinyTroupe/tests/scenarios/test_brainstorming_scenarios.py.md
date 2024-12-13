```python
import pytest
import logging
import sys

# Add necessary paths to import modules
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('../')

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import ResultsExtractor
from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect, create_marcos_the_physician
from tinytroupe.extraction import default_extractor as extractor
from tinytroupe.control import Simulation
from testing_utils import proposition_holds

logger = logging.getLogger("tinytroupe")


@pytest.fixture
def focus_group_world():
    """Sets up a TinyWorld with a focus group of agents."""
    world = TinyWorld(social_network=TinySocialNetwork())
    lisa = create_lisa_the_data_scientist(world)
    oscar = create_oscar_the_architect(world)
    marcos = create_marcos_the_physician(world)
    return world


def test_brainstorming_scenario(focus_group_world):
    """
    Tests the brainstorming scenario where agents discuss and summarize ideas for a new product.
    
    This test verifies if the agents can brainstorm ideas for a new product, if they can
    summarize the discussion, and finally if the summarized ideas are consistent with the
    objective of the brainstorming.
    """
    world = focus_group_world

    # Initial brainstorming prompt
    world.broadcast("""
             Folks, we need to brainstorm ideas for a new product. Your mission is to discuss potential AI feature ideas
             to add to Microsoft Word. In general, we want features that make you or your industry more productive,
             taking advantage of all the latest AI technologies.

             Please start the discussion now.
             """)
    
    world.run(1)

    # Retrieve the agent "Lisa"
    agent = TinyPerson.get_agent_by_name("Lisa")

    # Prompt Lisa to summarize the discussion
    agent.listen_and_act("Can you please summarize the ideas that the group came up with?")

    # Extract results from Lisa's summary
    extractor = ResultsExtractor()

    results = extractor.extract_results_from_agent(agent, 
                            extraction_objective="Summarize the the ideas that the group came up with, explaining each idea as an item of a list. Describe in details the benefits and drawbacks of each.", 
                            situation="A focus group to brainstorm ideas for a new product.")

    print("Brainstorm Results: ", results)

    # Assertion to check if the summarized results are aligned with the initial objective.
    assert proposition_holds(f"The following contains some ideas for new product features or entirely new products: \'{results}\'"), f"Proposition is false according to the LLM."

def test_brainstorming_empty_world():
    """
    Tests the brainstorming scenario with an empty world.

    Verifies that the test is working correctly when the world has no agents.
    Expects the summarization to be empty, or at least not to contain any specific ideas.
    """

    world = TinyWorld(social_network=TinySocialNetwork())

    world.broadcast("""
            Folks, we need to brainstorm ideas for a new product. Your mission is to discuss potential AI feature ideas
             to add to Microsoft Word. In general, we want features that make you or your industry more productive,
             taking advantage of all the latest AI technologies.

             Please start the discussion now.
             """)
    
    world.run(1)

    # There are no agents in the world, so the return of None is expected.
    agent = TinyPerson.get_agent_by_name("Lisa")
    
    assert agent is None, "Expected to have no agent called Lisa"


def test_brainstorming_no_broadcast(focus_group_world):
    """
    Tests the scenario where no broadcast is made, and the agents are expected not to react
    """

    world = focus_group_world
    
    world.run(1)

    # Retrieve the agent "Lisa"
    agent = TinyPerson.get_agent_by_name("Lisa")

    # Prompt Lisa to summarize the discussion
    agent.listen_and_act("Can you please summarize the ideas that the group came up with?")

    # Extract results from Lisa's summary
    extractor = ResultsExtractor()

    results = extractor.extract_results_from_agent(agent, 
                            extraction_objective="Summarize the the ideas that the group came up with, explaining each idea as an item of a list. Describe in details the benefits and drawbacks of each.", 
                            situation="A focus group to brainstorm ideas for a new product.")

    print("Brainstorm Results: ", results)

    # Assertion to check if the summarized results are aligned with the initial objective.
    assert proposition_holds(f"The following contains some ideas for new product features or entirely new products: \'{results}\'"), f"Proposition is false according to the LLM."

```