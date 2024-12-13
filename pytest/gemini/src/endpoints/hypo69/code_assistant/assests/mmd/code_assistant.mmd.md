```python
import pytest
from unittest.mock import patch, mock_open
import os
import signal
from src.endpoints.hypo69.code_assistant.code_assistant import CodeAssistant # Assuming this is the correct module path

# Mock the models to avoid actual API calls
class MockGeminiModel:
    def generate_content(self, content):
      if "error" in content:
         raise Exception("Mock Gemini Model Error")
      return f"Gemini response: {content}"

class MockOpenAIModel:
    def generate_content(self, content):
        return f"OpenAI response: {content}"


@pytest.fixture
def mock_config(tmp_path):
    config_data = {
        "gemini": {"api_key": "test_gemini_key"},
        "openai": {"api_key": "test_openai_key", "model": "gpt-3.5-turbo"},
    }
    config_file = tmp_path / "config.yaml"
    import yaml
    with open(config_file, "w") as f:
        yaml.dump(config_data, f)
    return config_file


@pytest.fixture
def mock_code_assistant(mock_config):
   
    # Patch the models to use the mocks
    with patch("src.endpoints.hypo69.code_assistant.code_assistant.GeminiModel",return_value = MockGeminiModel()):
       with patch("src.endpoints.hypo69.code_assistant.code_assistant.OpenAIModel", return_value = MockOpenAIModel()):
         return CodeAssistant(config_file_path = str(mock_config))


def test_code_assistant_initialization(mock_config):
    """Tests if the CodeAssistant class initializes correctly."""
    with patch("src.endpoints.hypo69.code_assistant.code_assistant.GeminiModel",return_value = MockGeminiModel()):
       with patch("src.endpoints.hypo69.code_assistant.code_assistant.OpenAIModel", return_value = MockOpenAIModel()):
           ca = CodeAssistant(config_file_path = str(mock_config))
           assert ca.gemini_model is not None
           assert ca.openai_model is not None
           assert ca.args is not None


def test_parse_args_with_files(mock_code_assistant):
    """Tests if parse_args correctly parses file paths."""
    
    with patch("sys.argv", ["script_name", "--files", "file1.txt", "file2.py"]):
        mock_code_assistant.parse_args()
    
    assert mock_code_assistant.args.files == ["file1.txt", "file2.py"]
    assert mock_code_assistant.args.prompt is None
    assert mock_code_assistant.args.output_file is None


def test_parse_args_with_prompt(mock_code_assistant):
    """Tests if parse_args correctly parses the prompt argument."""
    
    with patch("sys.argv", ["script_name", "--prompt", "Test Prompt"]):
        mock_code_assistant.parse_args()
    
    assert mock_code_assistant.args.prompt == "Test Prompt"
    assert mock_code_assistant.args.files is None
    assert mock_code_assistant.args.output_file is None



def test_parse_args_with_output_file(mock_code_assistant):
    """Tests if parse_args correctly parses the output file path."""
    
    with patch("sys.argv", ["script_name", "--output-file", "output.txt"]):
        mock_code_assistant.parse_args()
    
    assert mock_code_assistant.args.output_file == "output.txt"
    assert mock_code_assistant.args.files is None
    assert mock_code_assistant.args.prompt is None

def test_parse_args_no_arguments(mock_code_assistant):
    """Tests if parse_args works correctly when no arguments are passed."""
    with patch("sys.argv", ["script_name"]):
        mock_code_assistant.parse_args()
    
    assert mock_code_assistant.args.files is None
    assert mock_code_assistant.args.prompt is None
    assert mock_code_assistant.args.output_file is None


def test_yield_files_content_valid_files(mock_code_assistant,tmp_path):
    """Tests if _yield_files_content correctly yields file content."""
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.py"
    file1.write_text("Content of file1")
    file2.write_text("Content of file2")
    
    files = [str(file1), str(file2)]
    
    
    expected = [("file1.txt", "Content of file1"), ("file2.py", "Content of file2")]
    
    actual = list(mock_code_assistant._yield_files_content(files))

    assert actual == expected


def test_yield_files_content_file_not_found(mock_code_assistant,tmp_path):
     """Tests if _yield_files_content handles file not found gracefully."""
     file1 = tmp_path / "file1.txt"
     file1.write_text("Content of file1")
     files = [str(file1), "non_existent_file.txt"]
     
     expected = [("file1.txt", "Content of file1")]
     
     actual = list(mock_code_assistant._yield_files_content(files))
     assert actual == expected


def test_create_request_with_files(mock_code_assistant):
    """Tests if _create_request generates the correct prompt with file content."""
    files_content = [("file1.txt", "Content of file1"), ("file2.py", "Content of file2")]
    prompt_prefix = "Analyze the following code snippets:\n"
    expected_prompt = (
        prompt_prefix +
        "file1.txt:\nContent of file1\n\n" +
        "file2.py:\nContent of file2\n\n"
    )
    
    actual_prompt = mock_code_assistant._create_request(files_content, prompt_prefix)
    
    assert actual_prompt == expected_prompt

def test_create_request_with_prompt(mock_code_assistant):
    """Tests if _create_request generates the correct prompt with user input prompt."""
    prompt = "Test Prompt"
    files_content = [("file1.txt", "Content of file1"), ("file2.py", "Content of file2")]
    expected_prompt = (
        "Test Prompt\nAnalyze the following code snippets:\n"
        "file1.txt:\nContent of file1\n\n"
        "file2.py:\nContent of file2\n\n"
    )
    mock_code_assistant.args = mock_code_assistant.args = type('args', (object,), {'prompt': prompt, 'files': None, 'output_file':None})()
    actual_prompt = mock_code_assistant._create_request(files_content)
    assert actual_prompt == expected_prompt


def test_create_request_no_files(mock_code_assistant):
     """Tests if _create_request generates the correct prompt when no files are provided."""
     prompt = "Test Prompt"
     mock_code_assistant.args = type('args', (object,), {'prompt': prompt, 'files': None, 'output_file':None})()
     expected_prompt = prompt
     actual_prompt = mock_code_assistant._create_request([])
     assert actual_prompt == expected_prompt


def test_remove_outer_quotes_single_quotes(mock_code_assistant):
    """Tests if _remove_outer_quotes removes single outer quotes."""
    text = "'quoted text'"
    expected = "quoted text"
    actual = mock_code_assistant._remove_outer_quotes(text)
    assert actual == expected

def test_remove_outer_quotes_double_quotes(mock_code_assistant):
    """Tests if _remove_outer_quotes removes double outer quotes."""
    text = '"quoted text"'
    expected = "quoted text"
    actual = mock_code_assistant._remove_outer_quotes(text)
    assert actual == expected

def test_remove_outer_quotes_no_quotes(mock_code_assistant):
    """Tests if _remove_outer_quotes does not change text without quotes."""
    text = "text without quotes"
    expected = "text without quotes"
    actual = mock_code_assistant._remove_outer_quotes(text)
    assert actual == expected

def test_remove_outer_quotes_internal_quotes(mock_code_assistant):
    """Tests if _remove_outer_quotes does not affect internal quotes."""
    text = "'text with 'internal' quotes'"
    expected = "text with 'internal' quotes"
    actual = mock_code_assistant._remove_outer_quotes(text)
    assert actual == expected

def test_save_response_to_file(mock_code_assistant, tmp_path):
    """Tests if _save_response saves the response to the specified file."""
    output_file = tmp_path / "output.txt"
    response = "Test Response"
    mock_code_assistant.args = type('args', (object,), {'prompt': None, 'files': None, 'output_file': str(output_file)})()
    mock_code_assistant._save_response(response)
    assert output_file.read_text() == response

def test_save_response_to_stdout(mock_code_assistant,capsys):
     """Tests if _save_response prints to stdout when no output file is provided."""
     response = "Test Response"
     mock_code_assistant.args = type('args', (object,), {'prompt': None, 'files': None, 'output_file': None})()
     mock_code_assistant._save_response(response)
     captured = capsys.readouterr()
     assert response in captured.out


def test_signal_handler(mock_code_assistant):
     """Tests if signal handler correctly handles KeyboardInterrupt."""
     with pytest.raises(SystemExit) as e:
       mock_code_assistant._signal_handler(signal.SIGINT, None)
     assert e.type == SystemExit

def test_process_files_no_files(mock_code_assistant, capsys):
   """Tests processing no files or input prompt."""
   with patch("sys.argv", ["script_name"]):
        mock_code_assistant.parse_args()
   mock_code_assistant.process()
   captured = capsys.readouterr()
   assert "Please provide either --files or --prompt." in captured.out


def test_process_files_with_files_gemini(mock_code_assistant, tmp_path, capsys):
    """Tests the main process flow with valid file inputs."""
    
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.py"
    file1.write_text("Content of file1")
    file2.write_text("Content of file2")
    
    with patch("sys.argv", ["script_name", "--files", str(file1), str(file2)]):
       mock_code_assistant.parse_args()
    
    mock_code_assistant.process()
    captured = capsys.readouterr()
    assert "Gemini response: Analyze the following code snippets:" in captured.out
    assert "Content of file1" in captured.out
    assert "Content of file2" in captured.out
    

def test_process_files_with_files_gemini_error(mock_code_assistant, tmp_path, capsys):
    """Tests the main process flow with valid file inputs."""
    
    file1 = tmp_path / "file1.txt"
    file1.write_text("error content of file1")
    
    with patch("sys.argv", ["script_name", "--files", str(file1)]):
       mock_code_assistant.parse_args()
    
    mock_code_assistant.process()
    captured = capsys.readouterr()
    assert "Error processing file: file1.txt" in captured.out


def test_process_with_prompt_gemini(mock_code_assistant, capsys):
    """Tests the main process flow with a valid prompt."""
    
    with patch("sys.argv", ["script_name", "--prompt", "Test Prompt"]):
       mock_code_assistant.parse_args()
    
    mock_code_assistant.process()
    captured = capsys.readouterr()
    assert "Gemini response: Test Prompt" in captured.out


def test_process_files_with_files_and_prompt_gemini(mock_code_assistant, tmp_path, capsys):
    """Tests the main process flow with valid file inputs."""
    
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.py"
    file1.write_text("Content of file1")
    file2.write_text("Content of file2")
    
    with patch("sys.argv", ["script_name", "--files", str(file1), str(file2), "--prompt", "Test Prompt"]):
       mock_code_assistant.parse_args()
    
    mock_code_assistant.process()
    captured = capsys.readouterr()
    assert "Gemini response: Test Prompt" in captured.out
    assert "Content of file1" in captured.out
    assert "Content of file2" in captured.out

def test_process_with_output_file(mock_code_assistant, tmp_path):
     """Tests if process saves response to the output file correctly."""
     output_file = tmp_path / "output.txt"
     with patch("sys.argv", ["script_name", "--prompt", "Test Prompt", "--output-file", str(output_file)]):
        mock_code_assistant.parse_args()
     mock_code_assistant.process()
     assert "Gemini response: Test Prompt" in output_file.read_text()
```