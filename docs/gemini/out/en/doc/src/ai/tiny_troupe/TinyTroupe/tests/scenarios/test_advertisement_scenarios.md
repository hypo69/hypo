# test_advertisement_scenarios.py

## Overview

This module contains test functions for evaluating advertisement scenarios using TinyTroupe agents.  It tests scenarios involving advertisement evaluation, ad creation through focus groups, and consumer profiling.  The tests utilize the TinyTroupe agent framework and data extraction mechanisms.  The module also includes test setups and assertions to validate the expected output.

## Functions

### `test_ad_evaluation_scenario`

**Description**: This function tests the evaluation of multiple advertisements by TinyTroupe agents.  It presents a set of advertisements related to European travel packages and asks agents to select the most convincing one, providing justification.

**Parameters**:
- `setup`: (object): A setup object containing necessary resources and configurations for the test.

**Returns**:
- None: The function performs assertion checks and prints the choices of the agents.

**Raises**:
- `AssertionError`: Raised if any assertion related to the results from the agent evaluation fails, e.g., the agent didn't provide an ad_id, an invalid ad_id, or if the expected number of choices wasn't received.

### `test_ad_creation_scenario`

**Description**: This function simulates a focus group discussion to gather ideas for advertising an apartment for rent. It uses the `focus_group_world` environment to represent the focus group and extracts propositions for the advertisement from the conversation.

**Parameters**:
- `setup`: (object): A setup object containing necessary resources and configurations for the test.
- `focus_group_world`: (object): An instance of the focus group environment, providing simulated participants and interactions.

**Returns**:
- None: The function performs assertion checks on the extracted advertisement proposals from the focus group.

**Raises**:
- `AssertionError`: Raised if the extracted advertisement propositions from the focus group do not meet the expected criteria.

### `test_consumer_profiling_scenario`

**Description**: This function tests the consumer profiling feature of TinyTroupe. It simulates the interview of a set of consumers (represented as agents) to gather their preferences regarding bottled gazpacho. It gathers responses from a large number of consumers and saves the results in a cache file.

**Parameters**:
- `setup`: (object): A setup object containing necessary resources and configurations for the test.

**Returns**:
- None: The function performs assertions to ensure the checkpoint file was created and that the expected number of consumers were interviewed.

**Raises**:
- `AssertionError`: Raised if the consumer profiling process doesn't create the expected cache file, or the expected number of consumers are not interviewed.


## Classes

### N/A

This module does not define any custom classes.


## Modules Imported

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


## Global Variables


### N/A

This module does not define any global variables


```