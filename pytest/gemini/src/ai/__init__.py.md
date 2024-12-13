```python
import pytest

from src.ai import GoogleGenerativeAI, OpenAIModel, MODE


def test_module_mode():
    """
    Test that the module-level MODE variable is set correctly.
    """
    assert MODE == 'dev', "The MODE variable should be set to 'dev' by default"


def test_google_generative_ai_import():
    """
    Test that the GoogleGenerativeAI class is imported successfully.
    """
    assert GoogleGenerativeAI is not None, "GoogleGenerativeAI class should be imported."


def test_openai_model_import():
    """
    Test that the OpenAIModel class is imported successfully.
    """
    assert OpenAIModel is not None, "OpenAIModel class should be imported."
```