```python
import pytest
from unittest.mock import MagicMock
from hypotez.src.ai.openai.model.event_handler import EventHandler
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta

# Fixture definitions, if needed
@pytest.fixture
def mock_text():
    """Provides a mock Text object."""
    return MagicMock(spec=Text)

@pytest.fixture
def mock_text_delta():
    """Provides a mock TextDelta object."""
    return MagicMock(spec=TextDelta)

@pytest.fixture
def mock_tool_call():
    """Provides a mock ToolCall object."""
    return MagicMock(spec=ToolCall)

@pytest.fixture
def mock_tool_call_delta():
    """Provides a mock ToolCallDelta object."""
    return MagicMock(spec=ToolCallDelta)

@pytest.fixture
def event_handler():
    """Provides an instance of the EventHandler class."""
    return EventHandler()

# Tests for EventHandler class
def test_on_text_created(event_handler, mock_text, capsys):
    """Checks correct behavior of on_text_created method."""
    event_handler.on_text_created(mock_text)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > "

def test_on_text_delta(event_handler, mock_text_delta, mock_text, capsys):
    """Checks correct behavior of on_text_delta method with a delta value."""
    mock_text_delta.value = "Hello"
    event_handler.on_text_delta(mock_text_delta, mock_text)
    captured = capsys.readouterr()
    assert captured.out == "Hello"

def test_on_text_delta_empty_delta(event_handler, mock_text_delta, mock_text, capsys):
    """Checks correct behavior of on_text_delta method with an empty delta value."""
    mock_text_delta.value = ""
    event_handler.on_text_delta(mock_text_delta, mock_text)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_on_tool_call_created(event_handler, mock_tool_call, capsys):
    """Checks correct behavior of on_tool_call_created method."""
    mock_tool_call.type = "code_interpreter"
    event_handler.on_tool_call_created(mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > code_interpreter\n"
    
def test_on_tool_call_delta_code_interpreter_input(event_handler, mock_tool_call_delta, mock_tool_call, capsys):
    """Checks correct handling of code_interpreter input in on_tool_call_delta."""
    mock_tool_call_delta.type = "code_interpreter"
    mock_tool_call_delta.code_interpreter = MagicMock()
    mock_tool_call_delta.code_interpreter.input = "print('hello')"
    mock_tool_call_delta.code_interpreter.outputs = None  # Simulate no outputs
    event_handler.on_tool_call_delta(mock_tool_call_delta, mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "print('hello')"


def test_on_tool_call_delta_code_interpreter_output_logs(event_handler, mock_tool_call_delta, mock_tool_call, capsys):
    """Checks correct handling of code_interpreter logs output in on_tool_call_delta."""
    mock_tool_call_delta.type = "code_interpreter"
    mock_tool_call_delta.code_interpreter = MagicMock()
    mock_tool_call_delta.code_interpreter.input = None
    mock_tool_call_delta.code_interpreter.outputs = [MagicMock(type="logs", logs="output logs")]
    event_handler.on_tool_call_delta(mock_tool_call_delta, mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "\n\noutput >\n\noutput logs"


def test_on_tool_call_delta_code_interpreter_no_input_no_output(event_handler, mock_tool_call_delta, mock_tool_call, capsys):
    """Checks behavior when code_interpreter has no input and no outputs."""
    mock_tool_call_delta.type = "code_interpreter"
    mock_tool_call_delta.code_interpreter = MagicMock()
    mock_tool_call_delta.code_interpreter.input = None
    mock_tool_call_delta.code_interpreter.outputs = []
    event_handler.on_tool_call_delta(mock_tool_call_delta, mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_on_tool_call_delta_code_interpreter_with_input_and_logs_output(event_handler, mock_tool_call_delta, mock_tool_call, capsys):
    """Checks behavior when code_interpreter has input and logs output."""
    mock_tool_call_delta.type = "code_interpreter"
    mock_tool_call_delta.code_interpreter = MagicMock()
    mock_tool_call_delta.code_interpreter.input = "test_input"
    mock_tool_call_delta.code_interpreter.outputs = [MagicMock(type="logs", logs="test_logs")]
    event_handler.on_tool_call_delta(mock_tool_call_delta, mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "test_input\n\noutput >\n\ntest_logs"


def test_on_tool_call_delta_not_code_interpreter(event_handler, mock_tool_call_delta, mock_tool_call, capsys):
    """Checks that on_tool_call_delta does nothing for non-code_interpreter tool types."""
    mock_tool_call_delta.type = "retrieval"  # or any other tool type
    mock_tool_call_delta.code_interpreter = MagicMock()
    mock_tool_call_delta.code_interpreter.input = "test"
    mock_tool_call_delta.code_interpreter.outputs = [MagicMock(type="logs", logs="test")]
    event_handler.on_tool_call_delta(mock_tool_call_delta, mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_on_tool_call_delta_no_code_interpreter_object(event_handler, mock_tool_call_delta, mock_tool_call, capsys):
    """Checks behavior when there's no code_interpreter object in the delta."""
    mock_tool_call_delta.type = "code_interpreter"
    mock_tool_call_delta.code_interpreter = None
    event_handler.on_tool_call_delta(mock_tool_call_delta, mock_tool_call)
    captured = capsys.readouterr()
    assert captured.out == ""
```