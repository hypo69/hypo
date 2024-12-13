```python
import pytest
import gradio as gr
from unittest.mock import patch

# Fixture definitions, if needed
@pytest.fixture
def example_name():
    """Provides a sample name for testing the greet function."""
    return "Test User"

# Tests for the greet function
def test_greet_valid_input(example_name):
    """Checks correct greeting with valid name input."""
    from hypotez.src.ai.gradio.gradio import greet
    expected_output = "Hello " + example_name + "!"
    actual_output = greet(example_name)
    assert actual_output == expected_output

def test_greet_empty_input():
    """Checks correct greeting with an empty name input."""
    from hypotez.src.ai.gradio.gradio import greet
    expected_output = "Hello !"
    actual_output = greet("")
    assert actual_output == expected_output

def test_greet_special_characters():
    """Checks correct greeting with special characters input."""
    from hypotez.src.ai.gradio.gradio import greet
    special_name = "!@#$%^"
    expected_output = "Hello " + special_name + "!"
    actual_output = greet(special_name)
    assert actual_output == expected_output

def test_greet_numbers():
    """Checks correct greeting with numeric input."""
    from hypotez.src.ai.gradio.gradio import greet
    numeric_name = "12345"
    expected_output = "Hello " + numeric_name + "!"
    actual_output = greet(numeric_name)
    assert actual_output == expected_output

def test_greet_unicode():
    """Checks correct greeting with unicode input."""
    from hypotez.src.ai.gradio.gradio import greet
    unicode_name = "你好"
    expected_output = "Hello " + unicode_name + "!"
    actual_output = greet(unicode_name)
    assert actual_output == expected_output

@patch("gradio.blocks.Blocks.launch")
def test_gradio_interface_launch(mock_launch):
     """Checks if the gradio interface launches correctly."""
     from hypotez.src.ai.gradio.gradio import demo
     demo.launch()
     mock_launch.assert_called_once()


@patch("gradio.interface.Interface.launch")
def test_gradio_interface_default_parameters(mock_launch):
    """
    Checks if the gradio interface is launched with default parameters if none are specified.
    This includes the default input/output of text box
    """
    from hypotez.src.ai.gradio.gradio import greet
    from hypotez.src.ai.gradio.gradio import gr
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()
    mock_launch.assert_called_once()
```