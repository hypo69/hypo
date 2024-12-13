```python
import pytest
import os

# Since the input is a README.MD file describing a module structure,
# we will test the existence of the files described in the README.

# Define a fixture for the base directory of the AI modules
@pytest.fixture
def ai_base_dir():
    """Provides the base directory where AI submodules should reside."""
    # Assuming the README.MD is located in 'hypotez/src/ai'
    # and the test is being run from the root of the project
    base_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'ai')
    return base_dir

def test_ai_module_directory_exists(ai_base_dir):
    """Checks if the base 'ai' directory exists."""
    assert os.path.isdir(ai_base_dir), f"Base 'ai' directory not found: {ai_base_dir}"

def test_anthropic_module_exists(ai_base_dir):
    """Checks if the anthropic module directory exists."""
    anthropic_dir = os.path.join(ai_base_dir, 'anthropic')
    assert os.path.isdir(anthropic_dir), f"Anthropic module directory not found: {anthropic_dir}"

def test_dialogflow_module_exists(ai_base_dir):
    """Checks if the dialogflow module directory exists."""
    dialogflow_dir = os.path.join(ai_base_dir, 'dialogflow')
    assert os.path.isdir(dialogflow_dir), f"Dialogflow module directory not found: {dialogflow_dir}"

def test_gemini_module_exists(ai_base_dir):
    """Checks if the gemini module directory exists."""
    gemini_dir = os.path.join(ai_base_dir, 'gemini')
    assert os.path.isdir(gemini_dir), f"Gemini module directory not found: {gemini_dir}"

def test_helicone_module_exists(ai_base_dir):
    """Checks if the helicone module directory exists."""
    helicone_dir = os.path.join(ai_base_dir, 'helicone')
    assert os.path.isdir(helicone_dir), f"Helicone module directory not found: {helicone_dir}"

def test_llama_module_exists(ai_base_dir):
    """Checks if the llama module directory exists."""
    llama_dir = os.path.join(ai_base_dir, 'llama')
    assert os.path.isdir(llama_dir), f"Llama module directory not found: {llama_dir}"

def test_myai_module_exists(ai_base_dir):
    """Checks if the myai module directory exists."""
    myai_dir = os.path.join(ai_base_dir, 'myai')
    assert os.path.isdir(myai_dir), f"MyAI module directory not found: {myai_dir}"

def test_openai_module_exists(ai_base_dir):
    """Checks if the openai module directory exists."""
    openai_dir = os.path.join(ai_base_dir, 'openai')
    assert os.path.isdir(openai_dir), f"OpenAI module directory not found: {openai_dir}"

def test_tiny_troupe_module_exists(ai_base_dir):
    """Checks if the tiny_troupe module directory exists."""
    tiny_troupe_dir = os.path.join(ai_base_dir, 'tiny_troupe')
    assert os.path.isdir(tiny_troupe_dir), f"Tiny Troupe module directory not found: {tiny_troupe_dir}"

def test_revai_module_exists(ai_base_dir):
    """Checks if the revai module directory exists."""
    revai_dir = os.path.join(ai_base_dir, 'revai')
    assert os.path.isdir(revai_dir), f"RevAI module directory not found: {revai_dir}"

def test_prompts_directory_exists(ai_base_dir):
    """Checks if the prompts directory exists."""
    prompts_dir = os.path.join(ai_base_dir, 'prompts')
    assert os.path.isdir(prompts_dir), f"'prompts' directory not found: {prompts_dir}"
```