```python
import pytest
import os
import copy
from tinytroupe.agent import TinyPerson, default, RecallFaculty, FilesAndWebGroundingFaculty, TinyToolUse, EpisodicMemory, SemanticMemory
from rich.console import Console

# Create a temporary directory for test files (if needed)
TEST_DIR = "test_tiny_troupe_files"
os.makedirs(TEST_DIR, exist_ok=True)

@pytest.fixture
def test_agent():
    """Creates a TinyPerson agent for testing."""
    return TinyPerson(name="test_agent")

@pytest.fixture
def test_agent_with_faculty():
    """Creates a TinyPerson agent with a recall faculty for testing."""
    agent = TinyPerson(name="test_agent_faculty")
    agent.add_mental_faculties([RecallFaculty()])
    return agent

@pytest.fixture
def test_agent_with_file_faculty():
    """Creates a TinyPerson agent with file grounding faculty for testing."""
    agent = TinyPerson(name="test_agent_files")
    agent.add_mental_faculties([FilesAndWebGroundingFaculty()])

    # Create a dummy text file for testing
    test_file_path = os.path.join(TEST_DIR, "test_document.txt")
    with open(test_file_path, "w") as f:
        f.write("This is a test document.")

    agent.read_documents_from_folder(TEST_DIR)
    return agent


def test_tiny_person_creation(test_agent):
    """Tests if a TinyPerson object can be created."""
    assert isinstance(test_agent, TinyPerson)
    assert test_agent.name == "test_agent"

def test_tiny_person_define(test_agent):
    """Tests the define method for adding a value to configuration."""
    test_agent.define("age", 30)
    assert test_agent.get("age") == 30
    
def test_tiny_person_define_error(test_agent):
    """Tests invalid input to define method (non-string)."""
    with pytest.raises(Exception) as e: # Ensure the right exception is raised.
        test_agent.define("age", 30.5, group="invalid_group") #Should fail because we are passing a non-string to the value parameter
    assert "Cannot add a definition to an attribute that is not a string or list" in str(e.tracebacks[0].value)
    
def test_tiny_person_define_several(test_agent):
    """Tests define_several for adding multiple values to a group."""
    records = [{"occupation": "Engineer"}, {"occupation": "Teacher"}]
    test_agent.define_several("occupation_description", records)
    assert test_agent._configuration["occupation_description"] == records
    
def test_tiny_person_define_relationships(test_agent):
    """Tests define_relationships for adding agent relationships."""
    other_agent_name = "other_agent"
    test_agent.define_relationships([{"Name": other_agent_name, "Description": "Friend"}])
    assert other_agent_name in test_agent._configuration['relationships']

def test_tiny_person_add_mental_faculty(test_agent):
    """Test adding a mental faculty to the agent."""
    agent = test_agent
    agent.add_mental_faculty(RecallFaculty())
    assert isinstance(agent._mental_faculties[0], RecallFaculty)

def test_tiny_person_add_mental_faculty_duplicate(test_agent):
    """Test adding a duplicate mental faculty."""
    agent = test_agent
    agent.add_mental_faculty(RecallFaculty())
    with pytest.raises(Exception) as e:
        agent.add_mental_faculty(RecallFaculty())
    assert "The mental faculty" in str(e.value)

def test_recall_faculty_process_action(test_agent_with_faculty):
    """Test processing an action with a recall faculty."""
    test_agent_with_faculty.add_mental_faculties([RecallFaculty()])
    action = {"type": "RECALL", "content": "memory_query"}
    success = test_agent_with_faculty._mental_faculties[0].process_action(test_agent_with_faculty, action)
    assert success == True

def test_file_grounding_faculty_process_action(test_agent_with_file_faculty):
    """Test processing CONSULT action with file grounding faculty."""
    action = {"type": "CONSULT", "content": "test_document.txt"}
    success = test_agent_with_file_faculty._mental_faculties[0].process_action(test_agent_with_file_faculty, action)
    assert success is True


# Clean up the temporary directory after tests
def pytest_sessionfinish(session, exitstatus):
    if os.path.exists(TEST_DIR):
        import shutil
        shutil.rmtree(TEST_DIR)


```