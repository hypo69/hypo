```python
import pytest
import json
from unittest.mock import MagicMock, patch

from tinytroupe.tools import TinyTool, TinyCalendar, TinyWordProcessor
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher
import tinytroupe.utils as utils


# --- Fixtures ---
@pytest.fixture
def mock_agent():
    """Provides a mock agent object for testing."""
    agent = MagicMock()
    agent.name = "Test Agent"
    return agent

@pytest.fixture
def mock_exporter():
    """Provides a mock artifact exporter."""
    exporter = MagicMock(spec=ArtifactExporter)
    return exporter

@pytest.fixture
def mock_enricher():
    """Provides a mock enricher."""
    enricher = MagicMock(spec=TinyEnricher)
    return enricher

# --- Tests for TinyTool Class ---

def test_tinytool_initialization():
    """Test the initialization of a TinyTool object."""
    tool = TinyTool(name="Test Tool", description="A test tool", owner="Test Owner", real_world_side_effects=True)
    assert tool.name == "Test Tool"
    assert tool.description == "A test tool"
    assert tool.owner == "Test Owner"
    assert tool.real_world_side_effects is True
    assert tool.exporter is None
    assert tool.enricher is None

def test_tinytool_process_action_not_implemented(mock_agent):
    """Test that _process_action raises NotImplementedError."""
    tool = TinyTool(name="Test Tool", description="A test tool")
    with pytest.raises(NotImplementedError):
        tool._process_action(mock_agent, {})

def test_tinytool_protect_real_world_no_side_effects(caplog):
    """Test _protect_real_world does not log warning when real_world_side_effects is false."""
    tool = TinyTool(name="Test Tool", description="A test tool", real_world_side_effects=False)
    tool._protect_real_world()
    assert "REAL-WORLD SIDE EFFECTS" not in caplog.text

def test_tinytool_protect_real_world_with_side_effects(caplog):
    """Test _protect_real_world logs warning when real_world_side_effects is true."""
    tool = TinyTool(name="Test Tool", description="A test tool", real_world_side_effects=True)
    tool._protect_real_world()
    assert f"Tool {tool.name} has REAL-WORLD SIDE EFFECTS" in caplog.text

def test_tinytool_enforce_ownership_owned(mock_agent):
    """Test _enforce_ownership passes when agent owns the tool."""
    owner = MagicMock()
    owner.name = "Test Agent"
    tool = TinyTool(name="Test Tool", description="A test tool", owner=owner)
    tool._enforce_ownership(mock_agent) # Should not raise an exception
    
def test_tinytool_enforce_ownership_not_owned(mock_agent):
    """Test _enforce_ownership raises ValueError when agent does not own the tool."""
    owner = MagicMock()
    owner.name = "Another Agent"
    tool = TinyTool(name="Test Tool", description="A test tool", owner=owner)
    with pytest.raises(ValueError, match=f"Agent {mock_agent.name} does not own tool {tool.name}, which is owned by {owner.name}."):
         tool._enforce_ownership(mock_agent)

def test_tinytool_enforce_ownership_no_owner(mock_agent):
    """Test _enforce_ownership passes when the tool has no owner."""
    tool = TinyTool(name="Test Tool", description="A test tool", owner=None)
    tool._enforce_ownership(mock_agent)  # Should not raise an exception


def test_tinytool_set_owner():
    """Test setting a tool's owner."""
    tool = TinyTool(name="Test Tool", description="A test tool")
    owner = MagicMock()
    tool.set_owner(owner)
    assert tool.owner == owner
    
def test_tinytool_actions_definitions_prompt_not_implemented():
    """Test that actions_definitions_prompt raises NotImplementedError."""
    tool = TinyTool(name="Test Tool", description="A test tool")
    with pytest.raises(NotImplementedError):
        tool.actions_definitions_prompt()

def test_tinytool_actions_constraints_prompt_not_implemented():
    """Test that actions_constraints_prompt raises NotImplementedError."""
    tool = TinyTool(name="Test Tool", description="A test tool")
    with pytest.raises(NotImplementedError):
        tool.actions_constraints_prompt()

def test_tinytool_process_action_calls_protection_and_ownership(mock_agent):
    """Test that process_action calls the protection and ownership checks."""
    tool = TinyTool(name="Test Tool", description="A test tool")
    tool._protect_real_world = MagicMock()
    tool._enforce_ownership = MagicMock()
    tool._process_action = MagicMock()

    action = {"type": "TEST_ACTION", "content": "test content"}

    tool.process_action(mock_agent, action)
    tool._protect_real_world.assert_called_once()
    tool._enforce_ownership.assert_called_once_with(mock_agent)
    tool._process_action.assert_called_once_with(mock_agent, action)

# --- Tests for TinyCalendar Class ---
def test_tinycalendar_initialization():
    """Test the initialization of a TinyCalendar object."""
    calendar = TinyCalendar(owner="Test Owner")
    assert calendar.name == "calendar"
    assert calendar.description == "A basic calendar tool that allows agents to keep track meetings and appointments."
    assert calendar.owner == "Test Owner"
    assert calendar.real_world_side_effects is False
    assert calendar.calendar == {}


def test_tinycalendar_add_event():
    """Test adding events to the calendar."""
    calendar = TinyCalendar()
    calendar.add_event(date="2024-01-01", title="Meeting", description="Team meeting", owner="Test Agent")
    assert "2024-01-01" in calendar.calendar
    assert len(calendar.calendar["2024-01-01"]) == 1
    event = calendar.calendar["2024-01-01"][0]
    assert event["title"] == "Meeting"
    assert event["description"] == "Team meeting"
    assert event["owner"] == "Test Agent"

def test_tinycalendar_find_events_not_implemented():
    """Test that find_events is not yet implemented."""
    calendar = TinyCalendar()
    with pytest.raises(NotImplementedError):
        calendar.find_events(year=2024, month=1, day=1)

def test_tinycalendar_process_action_create_event_valid_content(mock_agent):
    """Test the processing of a CREATE_EVENT action with valid content."""
    calendar = TinyCalendar()
    action = {"type": "CREATE_EVENT", "content": json.dumps({"title": "Test Event", "description": "Test Description", "mandatory_attendees": ["agent1", "agent2"]})}
    
    result = calendar._process_action(mock_agent, action)

    assert result is True
    assert "title" in calendar.calendar
    assert "description" in calendar.calendar["title"][0]
    assert calendar.calendar["title"][0]["title"] == "Test Event"
    assert calendar.calendar["title"][0]["description"] == "Test Description"
    assert calendar.calendar["title"][0]["mandatory_attendees"] == ["agent1", "agent2"]

def test_tinycalendar_process_action_create_event_invalid_content(mock_agent):
    """Test the processing of a CREATE_EVENT action with invalid content."""
    calendar = TinyCalendar()
    action = {"type": "CREATE_EVENT", "content": json.dumps({"invalid_key": "value"})}
    with pytest.raises(ValueError, match="Invalid fields found in the input: {'invalid_key'}"):
            calendar._process_action(mock_agent, action)

def test_tinycalendar_process_action_not_create_event(mock_agent):
    """Test that processing a non-CREATE_EVENT action returns False."""
    calendar = TinyCalendar()
    action = {"type": "OTHER_ACTION", "content": "test content"}
    assert calendar._process_action(mock_agent, action) is False


def test_tinycalendar_actions_definitions_prompt():
    """Test the actions_definitions_prompt for TinyCalendar."""
    calendar = TinyCalendar()
    prompt = calendar.actions_definitions_prompt()
    assert "CREATE_EVENT" in prompt
    assert "title" in prompt
    assert "description" in prompt
    assert "mandatory_attendees" in prompt
    assert "optional_attendees" in prompt
    assert "start_time" in prompt
    assert "end_time" in prompt

def test_tinycalendar_actions_constraints_prompt():
    """Test the actions_constraints_prompt for TinyCalendar."""
    calendar = TinyCalendar()
    prompt = calendar.actions_constraints_prompt()
    assert prompt == ""

# --- Tests for TinyWordProcessor Class ---
def test_tinywordprocessor_initialization(mock_exporter, mock_enricher):
    """Test the initialization of a TinyWordProcessor object."""
    word_processor = TinyWordProcessor(owner="Test Owner", exporter=mock_exporter, enricher=mock_enricher)
    assert word_processor.name == "wordprocessor"
    assert word_processor.description == "A basic word processor tool that allows agents to write documents."
    assert word_processor.owner == "Test Owner"
    assert word_processor.real_world_side_effects is False
    assert word_processor.exporter == mock_exporter
    assert word_processor.enricher == mock_enricher

def test_tinywordprocessor_write_document_no_enricher_no_exporter(caplog):
    """Test writing a document without an enricher or exporter."""
    word_processor = TinyWordProcessor()
    word_processor.write_document(title="Test Document", content="Test content", author="Test Author")
    assert "Writing document with title Test Document and content: Test content" in caplog.text

def test_tinywordprocessor_write_document_with_enricher(mock_enricher, mock_exporter):
    """Test writing a document with an enricher."""
    mock_enricher.enrich_content.return_value = "Enriched content"
    word_processor = TinyWordProcessor(enricher=mock_enricher, exporter=mock_exporter)
    word_processor.write_document(title="Test Document", content="Test content", author="Test Author")
    mock_enricher.enrich_content.assert_called_once()
    mock_exporter.export.assert_called()
    assert mock_exporter.call_count == 3 # for each format: md, docx, json

def test_tinywordprocessor_write_document_with_exporter(mock_exporter):
    """Test writing a document with an exporter."""
    word_processor = TinyWordProcessor(exporter=mock_exporter)
    word_processor.write_document(title="Test Document", content="Test content", author="Test Author")
    mock_exporter.export.assert_called()
    assert mock_exporter.call_count == 3 # for each format: md, docx, json


def test_tinywordprocessor_process_action_write_document_valid_content_string(mock_agent, mock_exporter):
    """Test processing WRITE_DOCUMENT action with valid JSON string content."""
    word_processor = TinyWordProcessor(exporter=mock_exporter)
    action = {"type": "WRITE_DOCUMENT", "content": json.dumps({"title": "Test Doc", "content": "Test Content", "author": "Test Agent"})}
    result = word_processor._process_action(mock_agent, action)

    assert result is True
    mock_exporter.export.assert_called()

def test_tinywordprocessor_process_action_write_document_valid_content_dict(mock_agent, mock_exporter):
    """Test processing WRITE_DOCUMENT action with valid dictionary content."""
    word_processor = TinyWordProcessor(exporter=mock_exporter)
    action = {"type": "WRITE_DOCUMENT", "content": {"title": "Test Doc", "content": "Test Content", "author": "Test Agent"}}
    result = word_processor._process_action(mock_agent, action)
    assert result is True
    mock_exporter.export.assert_called()

def test_tinywordprocessor_process_action_write_document_invalid_content(mock_agent):
    """Test processing WRITE_DOCUMENT action with invalid content."""
    word_processor = TinyWordProcessor()
    action = {"type": "WRITE_DOCUMENT", "content": json.dumps({"invalid_key": "value"})}
    with pytest.raises(ValueError, match="Invalid fields found in the input: {'invalid_key'}"):
        word_processor._process_action(mock_agent, action)
    
def test_tinywordprocessor_process_action_not_write_document(mock_agent):
    """Test processing a non-WRITE_DOCUMENT action."""
    word_processor = TinyWordProcessor()
    action = {"type": "OTHER_ACTION", "content": "test content"}
    assert word_processor._process_action(mock_agent, action) is False

def test_tinywordprocessor_process_action_json_decode_error(mock_agent, caplog):
    """Test processing action with invalid json content."""
    word_processor = TinyWordProcessor()
    action = {"type": "WRITE_DOCUMENT", "content": "invalid json"}
    result = word_processor._process_action(mock_agent, action)
    assert result is False
    assert "Error parsing JSON content" in caplog.text

def test_tinywordprocessor_actions_definitions_prompt():
    """Test the actions_definitions_prompt for TinyWordProcessor."""
    word_processor = TinyWordProcessor()
    prompt = word_processor.actions_definitions_prompt()
    assert "WRITE_DOCUMENT" in prompt
    assert "title" in prompt
    assert "content" in prompt
    assert "author" in prompt

def test_tinywordprocessor_actions_constraints_prompt():
    """Test the actions_constraints_prompt for TinyWordProcessor."""
    word_processor = TinyWordProcessor()
    prompt = word_processor.actions_constraints_prompt()
    assert "WRITE_DOCUMENT" in prompt
    assert "all the content at once" in prompt
    assert "long and detailed" in prompt
    assert "specific owners" in prompt
```