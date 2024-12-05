# test_tinyworld.py

## Overview

This module contains unit tests for the `TinyWorld` class, verifying its functionality regarding agent interactions, broadcasting, and state encoding/decoding.  The tests utilize various agents from `tinytroupe.examples` and assert for expected behaviors within the `TinyWorld` environment.


## Table of Contents

* [test_run](#test_run)
* [test_broadcast](#test_broadcast)
* [test_encode_complete_state](#test_encode_complete_state)
* [test_decode_complete_state](#test_decode_complete_state)


## Functions

### `test_run`

**Description**: This function tests the `run` method of the `TinyWorld` class in both empty and populated scenarios. It checks for proper agent interaction and ensures that agents do not send messages to themselves.

**Parameters**:
- `setup`: (object):  A setup object (likely containing necessary objects for testing).
- `focus_group_world`: (TinyWorld): An instance of the TinyWorld class pre-populated with agents.

**Raises**:
- `AssertionError`: If an agent sends a message to itself, or if the retrieved message content does not match expectations.


### `test_broadcast`

**Description**: This function tests the `broadcast` method, verifying that messages are successfully delivered to agents within the `TinyWorld`.

**Parameters**:
- `setup`: (object): A setup object (likely containing necessary objects for testing).
- `focus_group_world`: (TinyWorld): An instance of the TinyWorld class with agents.

**Raises**:
- `AssertionError`: If an agent does not receive the broadcasted message.


### `test_encode_complete_state`

**Description**: Tests the `encode_complete_state` method of the `TinyWorld` class. It asserts that the encoded state is not `None` and contains the expected keys (`name`, `agents`).

**Parameters**:
- `setup`: (object): A setup object (likely containing necessary objects for testing).
- `focus_group_world`: (TinyWorld): An instance of the `TinyWorld` class with agents.


**Raises**:
- `AssertionError`: If the encoded state is `None` or if the expected keys or values are missing from the encoded state.


### `test_decode_complete_state`

**Description**: Tests the `decode_complete_state` method, ensuring that a decoded `TinyWorld` instance maintains the original state.

**Parameters**:
- `setup`: (object): A setup object (likely containing necessary objects for testing).
- `focus_group_world`: (TinyWorld): An instance of the `TinyWorld` class with agents.

**Raises**:
- `AssertionError`: If the decoded `TinyWorld` object is `None` or if the world's name, or number of agents, differs from the original.