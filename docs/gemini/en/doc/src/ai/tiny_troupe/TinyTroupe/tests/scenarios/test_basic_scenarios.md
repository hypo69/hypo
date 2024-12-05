# test_basic_scenarios.py

## Overview

This module contains unit tests for basic scenarios in the TinyTroupe simulation framework.  It focuses on verifying the initialization, execution, and checkpointing functionalities of the simulation engine.


## Functions

### `test_scenario_1`

**Description**: This function tests a basic scenario involving the creation and interaction of an agent within a simulation. It verifies the simulation status transitions and the existence of cached and execution traces.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- AssertionError: If the simulation status is not as expected or if cached/execution traces are missing.


## Modules Used

- `pytest`
- `logging`
- `sys`
- `tinytroupe`
- `tinytroupe.agent`
- `tinytroupe.environment`
- `tinytroupe.factory`
- `tinytroupe.extraction`
- `tinytroupe.examples`
- `tinytroupe.control`
- `testing_utils`


## Classes Used

- `TinyPerson`
- `TinyWorld`
- `TinySocialNetwork`
- `TinyPersonFactory`
- `ResultsExtractor`


## Notes

- The test relies on functions like `create_oscar_the_architect` which are assumed to be defined in the `tinytroupe.examples` module.  These create agent instances.
- The test verifies the simulation lifecycle (begin, checkpoint, end) as well as agent interactions and the existence of traces (cached and execution).
- Further assertions and logging are suggested for detailed verification of files created during checkpointing (TODO).
- The `testing_utils` module is assumed to contain helper functions for testing.
- The use of `control.reset()` ensures a clean simulation state for each test.
-  The assertions relating to `control._current_simulations["default"]` check that the simulation correctly tracks the default simulation.


## Example Usage

```
pytest tests/scenarios/test_basic_scenarios.py
```