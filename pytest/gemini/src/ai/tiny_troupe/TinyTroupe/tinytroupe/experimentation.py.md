```python
import pytest
import random
from tinytroupe.experimentation import ABRandomizer, Intervention
from tinytroupe.agent import TinyPerson

# Fixture definitions, if needed
@pytest.fixture
def ab_randomizer():
    """Provides a basic ABRandomizer instance for testing."""
    return ABRandomizer()

@pytest.fixture
def sample_agent():
    """Provides a basic TinyPerson instance for testing."""
    return TinyPerson("test_agent")

# Tests for ABRandomizer class
def test_abrandomizer_initialization():
    """Checks if ABRandomizer initializes with correct attributes."""
    randomizer = ABRandomizer(real_name_1="group1", real_name_2="group2", blind_name_a="A", blind_name_b="B", passtrough_name=["passthrough"], random_seed=123)
    assert randomizer.real_name_1 == "group1"
    assert randomizer.real_name_2 == "group2"
    assert randomizer.blind_name_a == "A"
    assert randomizer.blind_name_b == "B"
    assert randomizer.passtrough_name == ["passthrough"]
    assert randomizer.random_seed == 123

def test_abrandomizer_randomize(ab_randomizer):
    """Checks if randomize method correctly switches or not, and stores the choice."""
    a, b = "apple", "banana"
    first_a, first_b = ab_randomizer.randomize(0, a, b)
    assert (first_a == a and first_b == b) or (first_a == b and first_b == a)
    assert 0 in ab_randomizer.choices

    second_a, second_b = ab_randomizer.randomize(1, a,b)
    assert (second_a == a and second_b == b) or (second_a == b and second_b == a)
    assert 1 in ab_randomizer.choices

def test_abrandomizer_derandomize(ab_randomizer):
    """Checks if derandomize method returns the correct order based on previous randomization."""
    a, b = "apple", "banana"
    # randomize, and keep the order
    ab_randomizer.randomize(0, a, b)
    derandomized_a, derandomized_b = ab_randomizer.derandomize(0, a, b)
    if ab_randomizer.choices[0] == (0, 1):
        assert derandomized_a == a
        assert derandomized_b == b
    else:
        assert derandomized_a == b
        assert derandomized_b == a

    # randomize again, this time the order is changed
    ab_randomizer.randomize(1, a, b)
    derandomized_a, derandomized_b = ab_randomizer.derandomize(1, a, b)
    if ab_randomizer.choices[1] == (0, 1):
        assert derandomized_a == a
        assert derandomized_b == b
    else:
        assert derandomized_a == b
        assert derandomized_b == a

def test_abrandomizer_derandomize_no_randomization(ab_randomizer):
    """Checks if derandomize raises an exception if no randomization is found."""
    with pytest.raises(Exception, match="No randomization found for item 0"):
        ab_randomizer.derandomize(0, "apple", "banana")

def test_abrandomizer_derandomize_name(ab_randomizer):
    """Checks if derandomize_name method returns the correct real name based on the blind name."""
    ab_randomizer.randomize(0, "apple", "banana")
    # Assuming randomize kept the order.
    if ab_randomizer.choices[0] == (0, 1):
        assert ab_randomizer.derandomize_name(0, ab_randomizer.blind_name_a) == ab_randomizer.real_name_1
        assert ab_randomizer.derandomize_name(0, ab_randomizer.blind_name_b) == ab_randomizer.real_name_2
    else:
        assert ab_randomizer.derandomize_name(0, ab_randomizer.blind_name_a) == ab_randomizer.real_name_2
        assert ab_randomizer.derandomize_name(0, ab_randomizer.blind_name_b) == ab_randomizer.real_name_1
    
def test_abrandomizer_derandomize_name_passthrough(ab_randomizer):
        """Checks if derandomize_name method returns the same name if it's in the passthrough list"""
        ab_randomizer.passtrough_name = ["passthrough"]
        ab_randomizer.randomize(0, "apple", "banana")
        assert ab_randomizer.derandomize_name(0, "passthrough") == "passthrough"

def test_abrandomizer_derandomize_name_invalid_choice(ab_randomizer):
    """Checks if derandomize_name method raises an exception if the blind name is not recognized."""
    ab_randomizer.randomize(0, "apple", "banana")
    with pytest.raises(Exception, match="Choice \'invalid\' not recognized"):
        ab_randomizer.derandomize_name(0, "invalid")

def test_abrandomizer_derandomize_name_no_randomization(ab_randomizer):
    """Checks if derandomize_name method raises exception if no randomization for item."""
    with pytest.raises(Exception, match="No randomization found for item 0"):
         ab_randomizer.derandomize_name(0, "A")

# Tests for Intervention class
def test_intervention_initialization_single_agent(sample_agent):
    """Checks if Intervention initializes correctly with a single agent."""
    intervention = Intervention(agent=sample_agent)
    assert intervention.agents == [sample_agent]
    assert intervention.environments is None
    assert intervention.text_precondition is None
    assert intervention.precondition_func is None
    assert intervention.effect_func is None

def test_intervention_initialization_single_environment():
    """Checks if Intervention initializes correctly with a single environment."""
    class MockEnvironment:
         pass
    mock_environment = MockEnvironment()

    intervention = Intervention(environment=mock_environment)
    assert intervention.environments == [mock_environment]
    assert intervention.agents is None
    assert intervention.text_precondition is None
    assert intervention.precondition_func is None
    assert intervention.effect_func is None

def test_intervention_initialization_agent_and_agents(sample_agent):
    """Checks if Intervention raises exception if both agent and agents are provided."""
    with pytest.raises(Exception, match="Either \'agent\' or \'agents\' should be provided, not both"):
        Intervention(agent=sample_agent, agents=[sample_agent])

def test_intervention_initialization_environment_and_environments():
    """Checks if Intervention raises exception if both environment and environments are provided."""
    class MockEnvironment:
         pass
    mock_environment = MockEnvironment()
    with pytest.raises(Exception, match="Either \'environment\' or \'environments\' should be provided, not both"):
        Intervention(environment=mock_environment, environments=[mock_environment])

def test_intervention_initialization_no_parameters():
    """Checks if Intervention raises exception if no parameters are provided."""
    with pytest.raises(Exception, match="At least one of the parameters should be provided"):
        Intervention()

def test_intervention_check_precondition_not_implemented():
    """Checks if check_precondition raises NotImplementedError."""
    intervention = Intervention(agent=TinyPerson("test_agent"))
    with pytest.raises(NotImplementedError, match="TO-DO"):
        intervention.check_precondition()

def test_intervention_apply(sample_agent):
    """Checks if apply method correctly calls the effect function."""
    def mock_effect_func(agents, environments):
        mock_effect_func.called = True
        assert agents == [sample_agent]
        assert environments is None
    mock_effect_func.called = False

    intervention = Intervention(agent=sample_agent)
    intervention.set_effect(mock_effect_func)
    intervention.apply()
    assert mock_effect_func.called

def test_intervention_set_textual_precondition():
    """Checks if set_textual_precondition sets the precondition text correctly."""
    intervention = Intervention(agent=TinyPerson("test_agent"))
    text = "This is a text precondition."
    intervention.set_textual_precondition(text)
    assert intervention.text_precondition == text

def test_intervention_set_functional_precondition():
    """Checks if set_functional_precondition sets the precondition function correctly."""
    def mock_func(agent, agents, environment, environments):
        return True

    intervention = Intervention(agent=TinyPerson("test_agent"))
    intervention.set_functional_precondition(mock_func)
    assert intervention.precondition_func == mock_func

def test_intervention_set_effect():
    """Checks if set_effect sets the effect function correctly."""
    def mock_effect_func(agents, environments):
        pass
    
    intervention = Intervention(agent=TinyPerson("test_agent"))
    intervention.set_effect(mock_effect_func)
    assert intervention.effect_func == mock_effect_func
```