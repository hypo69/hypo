```python
import pytest
from typing import List

from hypotez.src.ai.openai.model.event_handler import EventHandler
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta, ToolCallType
from openai.types.beta.threads.runs.code_interpreter import CodeInterpreterOutput


# Fixture for creating test data
@pytest.fixture
def example_text():
    return Text(content="initial text")


@pytest.fixture
def example_text_delta():
    return TextDelta(value="updated text")


@pytest.fixture
def example_tool_call():
    return ToolCall(type=ToolCallType.code_interpreter, id="123")


@pytest.fixture
def example_code_interpreter_output():
    return CodeInterpreterOutput(type="logs", logs="some logs")


@pytest.fixture
def example_tool_call_delta():
    code_interpreter = {"input": "some input", "outputs": [
        {"type": "logs", "logs": "some logs"}
    ]}
    return ToolCallDelta(type="code_interpreter", code_interpreter=code_interpreter)



def test_on_text_created(capsys, example_text):
    """Tests the on_text_created method."""
    handler = EventHandler()
    handler.on_text_created(example_text)
    captured = capsys.readouterr()
    assert captured.out == "assistant > "


def test_on_text_delta(capsys, example_text_delta, example_text):
    """Tests the on_text_delta method."""
    handler = EventHandler()
    handler.on_text_delta(example_text_delta, example_text)
    captured = capsys.readouterr()
    assert captured.out == "updated text"


def test_on_tool_call_created(capsys, example_tool_call):
    """Tests the on_tool_call_created method."""
    handler = EventHandler()
    handler.on_tool_call_created(example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == "assistant > code_interpreter\n"


def test_on_tool_call_delta_no_code_interpreter(capsys, example_tool_call_delta):
    """Tests on_tool_call_delta with no code interpreter."""
    handler = EventHandler()
    handler.on_tool_call_delta(example_tool_call_delta, example_tool_call)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_on_tool_call_delta_with_code_interpreter(capsys, example_tool_call_delta, example_code_interpreter_output):
    """Tests on_tool_call_delta with code interpreter and output."""
    handler = EventHandler()
    example_tool_call_delta_outputs = [example_code_interpreter_output]
    example_tool_call_delta = ToolCallDelta(type="code_interpreter", code_interpreter={
        "input": "some input",
        "outputs": example_tool_call_delta_outputs
    })
    handler.on_tool_call_delta(example_tool_call_delta, example_tool_call)
    captured = capsys.readouterr()
    expected_output = "some input\n\noutput >\n\nsome logs\n"
    assert captured.out == expected_output


def test_on_tool_call_delta_empty_output(capsys, example_tool_call_delta):
    """Test for empty output in the code interpreter."""
    handler = EventHandler()
    example_tool_call_delta_outputs = []
    example_tool_call_delta = ToolCallDelta(type="code_interpreter", code_interpreter={
        "input": "some input",
        "outputs": example_tool_call_delta_outputs
    })
    handler.on_tool_call_delta(example_tool_call_delta, example_tool_call)
    captured = capsys.readouterr()
    expected_output = "some input\n\noutput >\n"
    assert captured.out == expected_output

```