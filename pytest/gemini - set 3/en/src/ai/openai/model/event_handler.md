```python
import pytest
from typing import List
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta, ToolCallType
from openai.types.beta.threads.runs.outputs import OutputType, CodeInterpreterOutput

from hypotez.src.ai.openai.model.event_handler import EventHandler


# Fixture for creating test data
@pytest.fixture
def example_text_delta() -> TextDelta:
    return TextDelta(value="Test text")


@pytest.fixture
def example_tool_call() -> ToolCall:
    return ToolCall(type=ToolCallType.function_call)


@pytest.fixture
def example_tool_call_delta() -> ToolCallDelta:
    return ToolCallDelta(
        type="code_interpreter", code_interpreter=CodeInterpreterOutput(input="test input", outputs=[])
    )


@pytest.fixture
def example_code_interpreter_output() -> List[CodeInterpreterOutput]:
    return [
        CodeInterpreterOutput(
            type=OutputType.logs, logs="Some log message from the code interpreter"
        )
    ]




# Test on_text_created
def test_on_text_created(capsys):
    """Test the on_text_created method."""
    event_handler = EventHandler()
    text = Text(role="assistant", content="Hello")
    event_handler.on_text_created(text)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > Hello\n"


# Test on_text_delta
def test_on_text_delta(capsys, example_text_delta):
    """Test the on_text_delta method."""
    event_handler = EventHandler()
    snapshot = Text(role="assistant", content="")
    event_handler.on_text_delta(example_text_delta, snapshot)
    captured = capsys.readouterr()
    assert captured.out == "Test text"



# Test on_tool_call_created
def test_on_tool_call_created(capsys, example_tool_call):
    """Test the on_tool_call_created method."""
    event_handler = EventHandler()
    event_handler.on_tool_call_created(example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > function_call\n"


# Test on_tool_call_delta with valid code interpreter input
def test_on_tool_call_delta_code_interpreter_input(capsys, example_tool_call_delta):
    """Test on_tool_call_delta with valid code interpreter input."""
    event_handler = EventHandler()
    snapshot = ToolCall(type="code_interpreter")
    event_handler.on_tool_call_delta(example_tool_call_delta, snapshot)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > code_interpreter\ntest input\n\noutput >\n\n"



# Test on_tool_call_delta with valid code interpreter output
def test_on_tool_call_delta_code_interpreter_output(capsys, example_tool_call_delta, example_code_interpreter_output):
    """Test on_tool_call_delta with valid code interpreter output."""
    example_tool_call_delta.code_interpreter.outputs = example_code_interpreter_output
    event_handler = EventHandler()
    snapshot = ToolCall(type="code_interpreter")
    event_handler.on_tool_call_delta(example_tool_call_delta, snapshot)
    captured = capsys.readouterr()
    expected_output = "\nassistant > code_interpreter\n\noutput >\n\nSome log message from the code interpreter\n"
    assert captured.out == expected_output

# Test on_tool_call_delta with empty code interpreter output
def test_on_tool_call_delta_empty_code_interpreter_output(capsys, example_tool_call_delta):
    """Test on_tool_call_delta with empty code interpreter output."""
    event_handler = EventHandler()
    snapshot = ToolCall(type="code_interpreter")
    event_handler.on_tool_call_delta(example_tool_call_delta, snapshot)
    captured = capsys.readouterr()
    assert captured.out == "\nassistant > code_interpreter\ntest input\n\noutput >\n\n"


```