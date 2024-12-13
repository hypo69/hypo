```python
import pytest
import json
import os
import tempfile
from unittest.mock import patch, mock_open

from tinytroupe.control import Simulation, Transaction, transactional, reset, begin, end, checkpoint, current_simulation, CacheOutOfSync, ExecutionCached, SkipTransaction
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyFactory
import tinytroupe.utils as utils

# Fixture definitions
@pytest.fixture
def simulation():
    """Provides a clean Simulation instance for each test."""
    sim = Simulation()
    reset()
    return sim

@pytest.fixture
def person():
    """Provides a TinyPerson instance."""
    return TinyPerson(name="test_person")

@pytest.fixture
def world():
    """Provides a TinyWorld instance."""
    return TinyWorld(name="test_world")

@pytest.fixture
def factory():
     """Provides a TinyFactory instance."""
     return TinyFactory(name="test_factory")
    
@pytest.fixture
def mock_cache_file():
    """Mocks file I/O for cache operations."""
    mock = mock_open()
    with patch('tinytroupe.control.open', mock):
        yield mock


def test_simulation_init():
    """Tests the initialization of the Simulation class."""
    sim = Simulation(id="test_sim")
    assert sim.id == "test_sim"
    assert sim.agents == []
    assert sim.name_to_agent == {}
    assert sim.environments == []
    assert sim.name_to_environment == {}
    assert sim.status == Simulation.STATUS_STOPPED
    assert sim.cache_path == "./tinytroupe-cache-test_sim.json"
    assert sim.auto_checkpoint is False
    assert sim.has_unsaved_cache_changes is False
    assert sim._under_transaction is False
    assert sim.cached_trace == []
    assert sim.execution_trace == []

def test_simulation_begin(simulation, mock_cache_file):
    """Tests the begin method of the Simulation class."""
    simulation.begin(cache_path="test_cache.json", auto_checkpoint=True)
    assert simulation.status == Simulation.STATUS_STARTED
    assert simulation.cache_path == "test_cache.json"
    assert simulation.auto_checkpoint is True
    assert utils._fresh_id_counter == 0
    mock_cache_file.assert_called_with("test_cache.json", "r")
    
    with pytest.raises(ValueError, match="Simulation is already started."):
        simulation.begin()

def test_simulation_begin_no_cache_path(simulation):
    """Tests the begin method with default cache path."""
    simulation.begin()
    assert simulation.cache_path == "./tinytroupe-cache-default.json"

def test_simulation_end(simulation):
    """Tests the end method of the Simulation class."""
    simulation.begin()
    simulation.end()
    assert simulation.status == Simulation.STATUS_STOPPED

    with pytest.raises(ValueError, match="Simulation is already stopped."):
        simulation.end()

def test_simulation_checkpoint(simulation, mock_cache_file):
    """Tests the checkpoint method of the Simulation class."""
    simulation.has_unsaved_cache_changes = True
    simulation.checkpoint()
    mock_cache_file.assert_called()
    
    simulation.has_unsaved_cache_changes = False
    simulation.checkpoint()
    mock_cache_file.assert_called_once()  # Ensure it's not called again

def test_simulation_add_agent(simulation, person):
    """Tests the add_agent method of the Simulation class."""
    simulation.add_agent(person)
    assert person in simulation.agents
    assert simulation.name_to_agent[person.name] == person
    assert person.simulation_id == simulation.id
    
    with pytest.raises(ValueError, match=f"Agent names must be unique, but '{person.name}' is already defined."):
            simulation.add_agent(person)


def test_simulation_add_environment(simulation, world):
    """Tests the add_environment method of the Simulation class."""
    simulation.add_environment(world)
    assert world in simulation.environments
    assert simulation.name_to_environment[world.name] == world
    assert world.simulation_id == simulation.id

    with pytest.raises(ValueError, match=f"Environment names must be unique, but '{world.name}' is already defined."):
        simulation.add_environment(world)

def test_simulation_add_factory(simulation, factory):
    """Tests the add_factory method of the Simulation class."""
    simulation.add_factory(factory)
    assert factory in simulation.factories
    assert simulation.name_to_factory[factory.name] == factory
    assert factory.simulation_id == simulation.id

    with pytest.raises(ValueError, match=f"Factory names must be unique, but '{factory.name}' is already defined."):
        simulation.add_factory(factory)

def test_simulation_execution_trace_position(simulation):
    """Tests the _execution_trace_position method of the Simulation class."""
    assert simulation._execution_trace_position() == -1
    simulation.execution_trace.append((None, "event1", "output1", {"state": 1}))
    assert simulation._execution_trace_position() == 0
    simulation.execution_trace.append((None, "event2", "output2", {"state": 2}))
    assert simulation._execution_trace_position() == 1

def test_simulation_function_call_hash(simulation):
    """Tests the _function_call_hash method of the Simulation class."""
    hash1 = simulation._function_call_hash("test_func", 1, a="test")
    hash2 = simulation._function_call_hash("test_func", 1, a="test")
    hash3 = simulation._function_call_hash("test_func", 2, a="test")
    assert hash1 == hash2
    assert hash1 != hash3

def test_simulation_skip_execution_with_cache(simulation):
     """Tests the _skip_execution_with_cache method of the Simulation class."""
     simulation.cached_trace.append((None, "event1", "output1", {"state": 1}))
     simulation._skip_execution_with_cache()
     assert len(simulation.execution_trace) == 1
     assert simulation.execution_trace[0] == simulation.cached_trace[0]
     
     with pytest.raises(AssertionError, match="There's no cached state at the current execution position."):
          simulation._skip_execution_with_cache()

def test_simulation_is_transaction_event_cached(simulation):
     """Tests the _is_transaction_event_cached method of the Simulation class."""
     # Test case 1: No cached trace
     assert simulation._is_transaction_event_cached("event1") == False
     
     # Test case 2: Cached trace but no match
     simulation.cached_trace.append((None, "event2", "output1", {"state": 1}))
     assert simulation._is_transaction_event_cached("event1") == False
     
     # Test case 3: Cached trace with a match
     simulation.cached_trace[0] = (None, "event1", "output1", {"state": 1})
     assert simulation._is_transaction_event_cached("event1") == True
     
     # Test case 4: Execution trace position is invalid
     simulation.execution_trace.append((None, "event1", "output1", {"state": 1}))
     simulation._drop_cached_trace_suffix() # To reset execution trace
     with pytest.raises(ValueError, match="Execution trace position is invalid, must be >= -1, but is "):
          simulation._is_transaction_event_cached("event1")


def test_simulation_drop_cached_trace_suffix(simulation):
    """Tests the _drop_cached_trace_suffix method of the Simulation class."""
    simulation.cached_trace = [(None, "event1", "output1", {"state": 1}), (None, "event2", "output2", {"state": 2})]
    simulation.execution_trace = [(None, "event1", "output1", {"state": 1})]
    simulation._drop_cached_trace_suffix()
    assert len(simulation.cached_trace) == 1
    assert simulation.cached_trace == [(None, "event1", "output1", {"state": 1})]


def test_simulation_add_to_execution_trace(simulation):
    """Tests the _add_to_execution_trace method of the Simulation class."""
    state = {"agents": [], "environments": []}
    simulation._add_to_execution_trace(state, "event1", "output1")
    assert len(simulation.execution_trace) == 1
    assert simulation.execution_trace[0][1] == "event1"
    assert simulation.execution_trace[0][2] == "output1"
    assert simulation.execution_trace[0][3] == state


def test_simulation_add_to_cache_trace(simulation):
    """Tests the _add_to_cache_trace method of the Simulation class."""
    state = {"agents": [], "environments": []}
    simulation._add_to_cache_trace(state, "event1", "output1")
    assert len(simulation.cached_trace) == 1
    assert simulation.cached_trace[0][1] == "event1"
    assert simulation.cached_trace[0][2] == "output1"
    assert simulation.cached_trace[0][3] == state
    assert simulation.has_unsaved_cache_changes is True


def test_simulation_load_cache_file(simulation, mock_cache_file):
    """Tests the _load_cache_file method of the Simulation class."""
    mock_cache_file.return_value.__enter__.return_value.read.return_value = json.dumps([
        (None, "event1", "output1", {"state": 1})
    ])
    simulation._load_cache_file("test_cache.json")
    assert len(simulation.cached_trace) == 1
    mock_cache_file.assert_called_with("test_cache.json", "r")

    mock_cache_file.side_effect = FileNotFoundError
    simulation._load_cache_file("non_existent_file.json")
    assert simulation.cached_trace == []
    
def test_simulation_save_cache_file(simulation, mock_cache_file):
    """Tests the _save_cache_file method of the Simulation class."""
    simulation.cached_trace = [(None, "event1", "output1", {"state": 1})]
    simulation.has_unsaved_cache_changes = True
    simulation._save_cache_file("test_cache.json")
    mock_cache_file.assert_called()
    assert simulation.has_unsaved_cache_changes is False


def test_simulation_begin_transaction(simulation):
    """Tests the begin_transaction method of the Simulation class."""
    simulation.begin_transaction()
    assert simulation._under_transaction is True


def test_simulation_end_transaction(simulation):
    """Tests the end_transaction method of the Simulation class."""
    simulation._under_transaction = True
    simulation.end_transaction()
    assert simulation._under_transaction is False


def test_simulation_is_under_transaction(simulation):
    """Tests the is_under_transaction method of the Simulation class."""
    assert simulation.is_under_transaction() is False
    simulation._under_transaction = True
    assert simulation.is_under_transaction() is True


def test_simulation_clear_communications_buffers(simulation, person, world):
    """Tests the _clear_communications_buffers method of the Simulation class."""
    simulation.add_agent(person)
    simulation.add_environment(world)
    person.communication_buffer.append("test")
    world.communication_buffer.append("test")
    simulation._clear_communications_buffers()
    assert person.communication_buffer == []
    assert world.communication_buffer == []


def test_simulation_encode_simulation_state(simulation, person, world, factory):
    """Tests the _encode_simulation_state method of the Simulation class."""
    simulation.add_agent(person)
    simulation.add_environment(world)
    simulation.add_factory(factory)
    state = simulation._encode_simulation_state()
    assert "agents" in state
    assert "environments" in state
    assert "factories" in state
    assert len(state["agents"]) == 1
    assert len(state["environments"]) == 1
    assert len(state["factories"]) == 1
    assert "name" in state["agents"][0]
    assert "name" in state["environments"][0]
    assert "name" in state["factories"][0]

def test_simulation_decode_simulation_state(simulation, person, world, factory):
     """Tests the _decode_simulation_state method of the Simulation class."""
     simulation.add_agent(person)
     simulation.add_environment(world)
     simulation.add_factory(factory)
     
     state = simulation._encode_simulation_state()
     
     # Clear the internal state
     person.x = 10
     world.x = 10
     factory.x = 10

     simulation._decode_simulation_state(state)
     
     assert person.x == 0
     assert world.x == 0
     assert factory.x == 0

def test_simulation_decode_simulation_state_raises_valueerror_on_missing_environment(simulation, person, world, factory):
    """Tests that the  _decode_simulation_state method raises a ValueError when the decoded environment is not in the simulation."""
    simulation.add_agent(person)
    simulation.add_factory(factory)

    state = simulation._encode_simulation_state()
    state["environments"] = [{"name":"non_existent_env", "x":0}]

    with pytest.raises(ValueError, match=f"Environment non_existent_env is not in the simulation, thus cannot be decoded there."):
        simulation._decode_simulation_state(state)

def test_simulation_decode_simulation_state_raises_valueerror_on_missing_agent(simulation, person, world, factory):
    """Tests that the  _decode_simulation_state method raises a ValueError when the decoded agent is not in the simulation."""
    simulation.add_environment(world)
    simulation.add_factory(factory)

    state = simulation._encode_simulation_state()
    state["agents"] = [{"name":"non_existent_agent", "x":0}]

    with pytest.raises(ValueError, match=f"Agent non_existent_agent is not in the simulation, thus cannot be decoded there."):
        simulation._decode_simulation_state(state)

def test_transaction_init(simulation, person, world, factory):
    """Tests the initialization of the Transaction class."""
    # Test case 1: Object is a TinyPerson
    transaction1 = Transaction(person, simulation, person.do_something)
    assert transaction1.obj_under_transaction == person
    assert transaction1.simulation == simulation
    assert transaction1.function_name == "do_something"
    assert transaction1.function == person.do_something
    assert person in simulation.agents
    assert person.simulation_id == simulation.id
    
    # Test case 2: Object is a TinyWorld
    transaction2 = Transaction(world, simulation, world.do_something)
    assert transaction2.obj_under_transaction == world
    assert transaction2.simulation == simulation
    assert transaction2.function_name == "do_something"
    assert transaction2.function == world.do_something
    assert world in simulation.environments
    assert world.simulation_id == simulation.id

    # Test case 3: Object is a TinyFactory
    transaction3 = Transaction(factory, simulation, factory.do_something)
    assert transaction3.obj_under_transaction == factory
    assert transaction3.simulation == simulation
    assert transaction3.function_name == "do_something"
    assert transaction3.function == factory.do_something
    assert factory in simulation.factories
    assert factory.simulation_id == simulation.id

    # Test case 4: Simulation is None
    transaction4 = Transaction(person, None, person.do_something)
    assert transaction4.simulation is None

    # Test case 5: Object is already captured by a different simulation
    sim2 = Simulation("sim2")
    person.simulation_id = sim2.id
    with pytest.raises(ValueError, match=f"Object {person} is already captured by a different simulation (id={sim2.id}),"):
        Transaction(person, simulation, person.do_something)

    # Test case 6: Object is not a TinyPerson or TinyWorld
    with pytest.raises(ValueError, match=f"Object test is not a TinyPerson or TinyWorld instance, and cannot be captured by the simulation."):
        Transaction("test", simulation, lambda x: x)

def test_transaction_execute_no_simulation(simulation, person):
    """Tests the execute method of the Transaction class when simulation is not started."""
    transaction = Transaction(person, None, person.do_something, 1)
    result = transaction.execute()
    assert result == 2

def test_transaction_execute_simulation_not_started(simulation, person):
    """Tests the execute method of the Transaction class when the simulation is not started."""
    transaction = Transaction(person, simulation, person.do_something, 1)
    result = transaction.execute()
    assert result == 2

def test_transaction_execute_cached(simulation, person):
     """Tests the execute method of the Transaction class when the transaction is cached."""
     simulation.begin()
     
     # Execute and cache a transaction
     transaction = Transaction(person, simulation, person.do_something, 1)
     transaction.execute()
     
     # Reset the person's internal state to check if it is restored correctly from the cache
     person.x = 10
     
     # Execute it again, but should fetch the result from the cache
     result = transaction.execute()
     
     assert len(simulation.execution_trace) == 2
     assert len(simulation.cached_trace) == 1 + 1
     assert result == 2
     assert person.x == 0 # check the internal state has been restored from the cache

def test_transaction_execute_not_cached(simulation, person):
    """Tests the execute method of the Transaction class when the transaction is not cached."""
    simulation.begin()
    transaction = Transaction(person, simulation, person.do_something, 1)
    result = transaction.execute()
    assert result == 2
    assert len(simulation.execution_trace) == 1
    assert len(simulation.cached_trace) == 1

def test_transaction_execute_reentrant_transaction(simulation, person):
     """Tests the execute method of the Transaction class when the transaction is reentrant (called inside another transaction)."""
     simulation.begin()
     
     def reentrant_func(self, a):
         transaction = Transaction(self, simulation, self.do_something, 1)
         transaction.execute()
         return self.do_something(a)

     # Execute and cache a top-level transaction
     transaction1 = Transaction(person, simulation, reentrant_func, 1)
     result = transaction1.execute()

     assert len(simulation.execution_trace) == 1
     assert len(simulation.cached_trace) == 1
     assert result == 2

def test_transaction_execute_auto_checkpoint(simulation, person, mock_cache_file):
    """Tests the execute method of the Transaction class with auto_checkpoint."""
    simulation.begin(auto_checkpoint=True)
    transaction = Transaction(person, simulation, person.do_something, 1)
    transaction.execute()
    mock_cache_file.assert_called()

def test_transaction_execute_simulation_status_invalid(simulation, person):
    """Tests the execute method of the Transaction class when the simulation status is invalid."""
    simulation.status = "invalid"
    transaction = Transaction(person, simulation, person.do_something, 1)
    with pytest.raises(ValueError, match="Simulation status is invalid at this point: invalid"):
        transaction.execute()

def test_transaction_encode_function_output_none(simulation, person):
    """Tests the _encode_function_output method when the output is None."""
    transaction = Transaction(person, simulation, lambda: None)
    output = transaction._encode_function_output(None)
    assert output is None

def test_transaction_encode_function_output_tiny_person(simulation, person):
    """Tests the _encode_function_output method when the output is a TinyPerson."""
    transaction = Transaction(person, simulation, lambda: person)
    output = transaction._encode_function_output(person)
    assert output == {"type": "TinyPersonRef", "name": person.name}

def test_transaction_encode_function_output_tiny_world(simulation, world):
    """Tests the _encode_function_output method when the output is a TinyWorld."""
    transaction = Transaction(world, simulation, lambda: world)
    output = transaction._encode_function_output(world)
    assert output == {"type": "TinyWorldRef", "name": world.name}

def test_transaction_encode_function_output_tiny_factory(simulation, factory):
    """Tests the _encode_function_output method when the output is a TinyFactory."""
    transaction = Transaction(factory, simulation, lambda: factory)
    output = transaction._encode_function_output(factory)
    assert output == {"type": "TinyFactoryRef", "name": factory.name}
    
def test_transaction_encode_function_output_json_types(simulation, person):
    """Tests the _encode_function_output method when the output is a JSON-supported type."""
    transaction = Transaction(person, simulation, lambda: 1)
    assert transaction._encode_function_output(1) == {"type": "JSON", "value": 1}
    assert transaction._encode_function_output(1.2) == {"type": "JSON", "value": 1.2}
    assert transaction._encode_function_output("test") == {"type": "JSON", "value": "test"}
    assert transaction._encode_function_output(True) == {"type": "JSON", "value": True}
    assert transaction._encode_function_output([1, 2]) == {"type": "JSON", "value": [1, 2]}
    assert transaction._encode_function_output({"a": 1}) == {"type": "JSON", "value": {"a": 1}}
    assert transaction._encode_function_output((1, 2)) == {"type": "JSON", "value": (1, 2)}


def test_transaction_encode_function_output_unsupported_type(simulation, person):
    """Tests the _encode_function_output method when the output is an unsupported type."""
    transaction = Transaction(person, simulation, lambda: object())
    with pytest.raises(ValueError, match="Unsupported output type: <class 'object'>"):
        transaction._encode_function_output(object())


def test_transaction_decode_function_output_none(simulation, person):
    """Tests the _decode_function_output method when the output is None."""
    transaction = Transaction(person, simulation, lambda: None)
    output = transaction._decode_function_output(None)
    assert output is None

def test_transaction_decode_function_output_tiny_person(simulation, person):
    """Tests the _decode_function_output method when the output is a TinyPerson reference."""
    simulation.add_agent(person)
    transaction = Transaction(person, simulation, lambda: person)
    encoded_output = {"type": "TinyPersonRef", "name": person.name}
    output = transaction._decode_function_output(encoded_output)
    assert output == person

def test_transaction_decode_function_output_tiny_world(simulation, world):
    """Tests the _decode_function_output method when the output is a TinyWorld reference."""
    simulation.add_environment(world)
    transaction = Transaction(world, simulation, lambda: world)
    encoded_output = {"type": "TinyWorldRef", "name": world.name}
    output = transaction._decode_function_output(encoded_output)
    assert output == world

def test_transaction_decode_function_output_tiny_factory(simulation, factory):
    """Tests the _decode_function_output method when the output is a TinyFactory reference."""
    simulation.add_factory(factory)
    transaction = Transaction(factory, simulation, lambda: factory)
    encoded_output = {"type": "TinyFactoryRef", "name": factory.name}
    output = transaction._decode_function_output(encoded_output)
    assert output == factory

def test_transaction_decode_function_output_json_types(simulation, person):
    """Tests the _decode_function_output method when the output is a JSON-supported type."""
    transaction = Transaction(person, simulation, lambda: 1)
    assert transaction._decode_function_output({"type": "JSON", "value": 1}) == 1
    assert transaction._decode_function_output({"type": "JSON", "value": 1.2}) == 1.2
    assert transaction._decode_function_output({"type": "JSON", "value": "test"}) == "test"
    assert transaction._decode_function_output({"type": "JSON", "value": True}) == True
    assert transaction._decode_function_output({"type": "JSON", "value": [1, 2]}) == [1, 2]
    assert transaction._decode_function_output({"type": "JSON", "value": {"a": 1}}) == {"a": 1}
    assert transaction._decode_function_output({"type": "JSON", "value": (1, 2)}) == (1, 2)


def test_transaction_decode_function_output_unsupported_type(simulation, person):
    """Tests the _decode_function_output method when the output is an unsupported type."""
    transaction = Transaction(person, simulation, lambda: object())
    with pytest.raises(ValueError, match="Unsupported output type: unknown"):
         transaction._decode_function_output({"type": "unknown"})


def test_transactional_decorator(simulation, person):
    """Tests the transactional decorator."""
    @transactional
    def test_func(self, a):
        return self.do_something(a)
    
    simulation.begin()
    result = test_func(person, 1)
    assert result == 2
    assert len(simulation.execution_trace) == 1
    assert len(simulation.cached_trace) == 1
    
def test_reset():
     """Tests the reset function."""
     global _current_simulations, _current_simulation_id
     begin("test_cache", "test_sim")
     assert _current_simulations["test_sim"] is not None
     assert _current_simulation_id == "test_sim"
     
     reset()
     assert _current_simulations["default"] is None
     assert _current_simulation_id is None


def test_simulation_convenience_functions(simulation):
    """Tests the convenience functions for simulation control."""
    
    # Test begin
    begin(id="test_sim")
    assert current_simulation() is not None
    assert current_simulation().id == "test_sim"
    
    # Test begin when already started
    with pytest.raises(ValueError, match=f"Simulation is already started under id test_sim. Currently only one simulation can be started at a time."):
        begin(id="another_sim")
    
    # Test checkpoint
    checkpoint(id="test_sim")
    assert current_simulation().has_unsaved_cache_changes == False
    
    # Test end
    end(id="test_sim")
    assert current_simulation() is None
    

def test_current_simulation_none():
     """Tests current_simulation when no simulation has been started."""
     assert current_simulation() is None

def test_exception_classes():
     """Tests exception classes."""
     with pytest.raises(SkipTransaction):
          raise SkipTransaction()
     with pytest.raises(CacheOutOfSync):
          raise CacheOutOfSync()
     with pytest.raises(ExecutionCached):
          raise ExecutionCached()
```