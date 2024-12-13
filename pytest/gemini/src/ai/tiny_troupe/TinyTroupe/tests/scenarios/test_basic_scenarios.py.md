```python
import pytest
import logging
import sys

sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('../')

import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import ResultsExtractor
from tinytroupe.examples import create_lisa_the_data_scientist, create_oscar_the_architect, create_marcos_the_physician
from tinytroupe.extraction import default_extractor as extractor
import tinytroupe.control as control
from tinytroupe.control import Simulation

from testing_utils import *


def test_scenario_1():
    """
    Test the basic simulation scenario:
    - Checks if the simulation starts correctly.
    - Checks if the cached and execution traces are created.
    - Checks if checkpoint saves are triggered correctly
    - Checks agent definition updates.
    """
    control.reset()
    # Check if the default simulation is None before starting
    assert control._current_simulations["default"] is None, "There should be no simulation running at this point."

    # Begin the simulation and check if its status is started
    control.begin()
    assert control._current_simulations["default"].status == Simulation.STATUS_STARTED, "The simulation should be started at this point."

    # Create an agent and define attributes
    agent = create_oscar_the_architect()
    agent.define("age", 19)
    agent.define("nationality", "Brazilian")

    # Check that traces have been created
    assert control._current_simulations["default"].cached_trace is not None, "There should be a cached trace at this point."
    assert control._current_simulations["default"].execution_trace is not None, "There should be an execution trace at this point."

    # Trigger a checkpoint and TODO check file creation
    control.checkpoint()
    # agent listens and acts and updates definition again
    agent.listen_and_act("How are you doing?")
    agent.define("occupation", "Engineer")
    # Trigger another checkpoint and TODO check file creation
    control.checkpoint()
    # End the simulation
    control.end()
```