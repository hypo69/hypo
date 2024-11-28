```python
import pytest
from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta
from hypotez.src.ai.openai.model.event_handler import EventHandler


# Fixture for creating test data
@pytest.fixture
def example_text_delta():
    return TextDelta(value="Hello")


@pytest.fixture
def example_text():
    return Text(content="World")


@pytest.fixture
def example_tool_call():
    return ToolCall(type="code_interpreter")


@pytest.fixture
def example_tool_call_delta():
    return ToolCallDelta(type="code_interpreter", code_interpreter={"input": "print('Hello')"})


@pytest.fixture
def example_code_interpreter_output():
    return [{"type": "logs", "logs": "Output: Hello"}]


# Tests for on_text_created
def test_on_text_created(capsys):
    """Checks correct output for on_text_created."""
    handler = EventHandler()
    text = Text(content="Test Text")
    handler.on_text_created(text)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > "


# Tests for on_text_delta
def test_on_text_delta(capsys, example_text_delta, example_text):
    """Checks correct output for on_text_delta."""
    handler = EventHandler()
    handler.on_text_delta(example_text_delta, example_text)
    captured = capsys.readouterr()
    assert captured.out == "Hello"


# Tests for on_tool_call_created
def test_on_tool_call_created(capsys, example_tool_call):
    """Checks correct output for on_tool_call_created."""
    handler = EventHandler()
    handler.on_tool_call_created(example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > code_interpreter\n"


# Tests for on_tool_call_delta with input
def test_on_tool_call_delta_input(capsys, example_tool_call_delta):
    """Checks correct output for on_tool_call_delta with input."""
    handler = EventHandler()
    handler.on_tool_call_delta(example_tool_call_delta, example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "print('Hello')\n\n"


# Tests for on_tool_call_delta with outputs
def test_on_tool_call_delta_outputs(capsys, example_tool_call_delta, example_code_interpreter_output):
    """Checks correct output for on_tool_call_delta with outputs."""
    delta = example_tool_call_delta
    delta.code_interpreter['outputs'] = example_code_interpreter_output
    handler = EventHandler()
    handler.on_tool_call_delta(delta, example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "\n\noutput >\n\nOutput: Hello\n"

# Test for missing code_interpreter in delta
def test_on_tool_call_delta_no_code_interpreter(capsys, example_tool_call_delta):
  """Checks correct handling when code_interpreter is missing in delta."""
  delta = example_tool_call_delta
  delta.code_interpreter = None
  handler = EventHandler()
  handler.on_tool_call_delta(delta, example_tool_call)
  captured = capsys.readouterr()
  assert captured.out == ""

# Test for missing output in delta
def test_on_tool_call_delta_no_outputs(capsys, example_tool_call_delta):
    """Checks correct handling when outputs are missing in delta."""
    handler = EventHandler()
    handler.on_tool_call_delta(example_tool_call_delta, example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "print('Hello')\n\n"



```