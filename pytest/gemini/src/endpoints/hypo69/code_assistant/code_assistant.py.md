```python
import pytest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch, mock_open, MagicMock
import asyncio
import json

from src.endpoints.hypo69.code_assistant.assistant import CodeAssistant
from src.utils.jjson import j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src import gs


# Mocking dependencies and fixtures
@pytest.fixture
def mock_gs_path(tmp_path):
    """Mocks gs.path for testing"""
    gs.path = SimpleNamespace(
        src=tmp_path / "src",
        endpoints=tmp_path / "src" / "endpoints",
    )
    return gs.path


@pytest.fixture
def mock_config_file(mock_gs_path):
    """Creates a mock config file for testing."""
    config_data = {
        "exclude_file_patterns": [r"test_.*\.py$"],
        "include_files": ["*.py"],
        "exclude_dirs": ["venv", "__pycache__"],
        "exclude_files": ["test_file.py"],
        "output_directory": {
            "code_checker": "gemini/code_checker/<lang>",
            "doc_writer_md": "gemini/doc_writer_md/<lang>",
            "doc_writer_rst": "gemini/doc_writer_rst/<lang>",
            "doc_writer_html": "gemini/doc_writer_html/<lang>",
            "code_explainer_md": "gemini/code_explainer_md/<lang>",
            "code_explainer_html": "gemini/code_explainer_html/<lang>",
            "pytest": "gemini/pytest/<lang>",
        },
        "remove_prefixes": ["```md", "```rst", "```html", "```python", "```"],
    }
    config_path = mock_gs_path.endpoints / "hypo69" / "code_assistant" / "code_assistant.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config_data, f)
    return config_path


@pytest.fixture
def mock_translations_file(mock_gs_path):
    """Creates a mock translations file for testing."""
    translations_data = {
        "roles": {
            "doc_writer_md": {
                "ru": "Ваша специализация - создание документации в формате `MD`",
                "en": "Your specialization is documentation creation in the `MD` format",
            },
            "code_checker": {
                "ru": "Ваша специализация - проверка кода",
                "en": "Your specialization is code checking",
            },
             "pytest": {
                "ru": "Ваша специализация - написание тестов",
                "en": "Your specialization is writing tests",
            },
        },
        "file_location_translated": {
            "ru": "Путь к файлу:",
            "en": "Path to file:",
        },
    }

    translations_path = (
        mock_gs_path.endpoints
        / "hypo69"
        / "code_assistant"
        / "translations"
        / "translations.json"
    )
    translations_path.parent.mkdir(parents=True, exist_ok=True)
    with open(translations_path, "w") as f:
        json.dump(translations_data, f)
    return translations_path


@pytest.fixture
def mock_gemini_model():
    """Mocks GoogleGenerativeAI class for testing."""
    with patch("src.endpoints.hypo69.code_assistant.assistant.GoogleGenerativeAI") as MockGemini:
        mock_instance = MockGemini.return_value
        mock_instance.ask = asyncio.Future()
        mock_instance.ask.set_result("response from gemini")
        mock_instance.upload_file = MagicMock(return_value=SimpleNamespace(url='test_url'))
        yield mock_instance


@pytest.fixture
def mock_openai_model():
    """Mocks OpenAIModel class for testing."""
    with patch("src.endpoints.hypo69.code_assistant.assistant.OpenAIModel") as MockOpenAI:
        mock_instance = MockOpenAI.return_value
        mock_instance.ask = asyncio.Future()
        mock_instance.ask.set_result("response from openai")
        yield mock_instance


@pytest.fixture
def code_assistant(mock_config_file, mock_translations_file, mock_gemini_model, mock_openai_model):
    """Creates an instance of CodeAssistant with mocked dependencies."""
    return CodeAssistant(role="code_checker", lang="ru", model=["gemini", "openai"])


@pytest.fixture
def test_file(mock_gs_path):
    """Creates a mock file for testing."""
    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path, "w") as f:
        f.write("test code")
    return test_file_path

# Test cases
def test_code_assistant_initialization(code_assistant):
    """Test successful initialization of CodeAssistant."""
    assert code_assistant.role == "code_checker"
    assert code_assistant.lang == "ru"
    assert isinstance(code_assistant.gemini_model, GoogleGenerativeAI)
    assert isinstance(code_assistant.openai_model, OpenAIModel)

@patch("argparse.ArgumentParser.parse_args", return_value=SimpleNamespace(role="test_role", lang="test_lang", model=["test_model"], start_dirs=["test_dir"], start_file_number=5))
def test_parse_args(mock_argparse):
    """Test parsing command-line arguments."""
    args = CodeAssistant.parse_args()
    assert args["role"] == "test_role"
    assert args["lang"] == "test_lang"
    assert args["model"] == ["test_model"]
    assert args["start_dirs"] == ["test_dir"]
    assert args["start_file_number"] == 5

def test_system_instruction_valid_file(code_assistant, mock_gs_path):
    """Test successful reading of system instructions."""
    instruction_path = mock_gs_path.src / "ai" / "prompts" / "developer" / "code_checker_ru.md"
    instruction_path.parent.mkdir(parents=True, exist_ok=True)
    with open(instruction_path, "w", encoding="UTF-8") as f:
        f.write("system instruction")
    
    assert code_assistant.system_instruction == "system instruction"

def test_system_instruction_file_not_found(code_assistant, mock_gs_path, caplog):
    """Test handling when the system instruction file is not found."""
    instruction_path = mock_gs_path.src / "ai" / "prompts" / "developer" / "code_checker_ru.md"
    assert not instruction_path.exists()
    assert not code_assistant.system_instruction
    assert "Error reading instruction file" in caplog.text

def test_code_instruction_valid_file(code_assistant, mock_gs_path):
    """Test successful reading of code instructions."""
    instruction_path = (
        mock_gs_path.endpoints
        / "hypo69"
        / "code_assistant"
        / "instructions"
        / "instruction_code_checker_ru.md"
    )
    instruction_path.parent.mkdir(parents=True, exist_ok=True)
    with open(instruction_path, "w", encoding="UTF-8") as f:
        f.write("code instruction")
    assert code_assistant.code_instruction == "code instruction"

def test_code_instruction_file_not_found(code_assistant, mock_gs_path, caplog):
    """Test handling when code instruction file is not found."""
    instruction_path = (
        mock_gs_path.endpoints
        / "hypo69"
        / "code_assistant"
        / "instructions"
        / "instruction_code_checker_ru.md"
    )
    assert not instruction_path.exists()
    assert code_assistant.code_instruction == ''
    assert "Error reading instruction file" in caplog.text

def test_translations_loading(code_assistant):
    """Test loading translations."""
    assert isinstance(code_assistant.translations, SimpleNamespace)
    assert hasattr(code_assistant.translations, "roles")
    assert hasattr(code_assistant.translations, "file_location_translated")

def test_create_request(code_assistant, mock_gs_path):
    """Test creation of a request."""
    test_file_path = mock_gs_path.src / "test_file.py"
    content = "test code"
    request = code_assistant._create_request(str(test_file_path), content)
    assert "role" in request
    assert "output_language" in request
    assert "Path to file:" in request
    assert "instruction" in request
    assert "input_code" in request
    assert "Your specialization is code checking" in request
    assert "en" not in request
    assert "ru" not in request

    code_assistant.lang = "en"
    request = code_assistant._create_request(str(test_file_path), content)
    assert "Your specialization is code checking" not in request
    assert "Your specialization is code checking" not in request
    assert "Your specialization is code checking" not in request
    assert "Your specialization is code checking" not in request

def test_create_request_exception(code_assistant, mock_gs_path, caplog):
    """Test create request when an exception occurs."""
    code_assistant.translations = SimpleNamespace(roles=SimpleNamespace())
    file_path = "test_file.py"
    content = "test code"
    request = code_assistant._create_request(file_path, content)
    assert request == content
    assert "Ошибка в составлении запроса" in caplog.text

@pytest.mark.asyncio
async def test_process_files_success(code_assistant, mock_gemini_model, test_file, mock_gs_path):
    """Test successful processing of a file."""
    await code_assistant.process_files()
    mock_gemini_model.ask.assert_called()
    assert "test code" in str(mock_gemini_model.ask.call_args)
    
    expected_export_path = mock_gs_path.src / "docs" / "gemini" / "code_checker" / "ru" / "test_file.py.md"
    assert expected_export_path.exists()

@pytest.mark.asyncio
async def test_process_files_skip_file(code_assistant, mock_gemini_model, mock_gs_path):
    """Test skipping a file because it's excluded."""
    init_file_path = mock_gs_path.src / "__init__.py"
    init_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(init_file_path, "w") as f:
        f.write("test code")
    
    header_file_path = mock_gs_path.src / "header.py"
    header_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(header_file_path, "w") as f:
        f.write("test code")

    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path, "w") as f:
        f.write("test code")

    await code_assistant.process_files()
    assert mock_gemini_model.ask.call_count == 1
    mock_gemini_model.upload_file.assert_called()
    assert mock_gemini_model.upload_file.call_count == 1


@pytest.mark.asyncio
async def test_process_files_start_file_number(code_assistant, mock_gemini_model, mock_gs_path):
    """Test skipping files based on start_file_number."""
    
    test_file1_path = mock_gs_path.src / "test_file1.py"
    test_file1_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file1_path, "w") as f:
        f.write("test code 1")
    test_file2_path = mock_gs_path.src / "test_file2.py"
    test_file2_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file2_path, "w") as f:
        f.write("test code 2")

    await code_assistant.process_files(start_file_number=2)
    assert mock_gemini_model.ask.call_count == 1
    assert "test code 2" in str(mock_gemini_model.ask.call_args)

@pytest.mark.asyncio
async def test_process_files_file_missing(code_assistant, mock_gemini_model, mock_gs_path, caplog):
    """Test handling of file read error."""
    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    test_file_path.unlink()
    await code_assistant.process_files()
    assert mock_gemini_model.ask.call_count == 0
    assert "Ошибка при чтении файла" in caplog.text
    assert "None" in caplog.text

@pytest.mark.asyncio
async def test_process_files_gemini_ask_fails(code_assistant, mock_gemini_model, test_file, caplog):
    """Test handling when gemini model ask method fails."""
    mock_gemini_model.ask.set_result(None)
    await code_assistant.process_files()
    assert mock_gemini_model.ask.called
    assert "Ошибка ответа модели" in caplog.text

@pytest.mark.asyncio
async def test_save_response_success(code_assistant, mock_gs_path, caplog):
    """Test successful saving of a response."""
    file_path = mock_gs_path.src / "test_file.py"
    response = "test response"
    result = await code_assistant._save_response(file_path, response, "gemini")
    assert result
    export_path = mock_gs_path.src / "docs" / "gemini" / "code_checker" / "ru" / "test_file.py.md"
    assert export_path.exists()
    with open(export_path, 'r') as f:
        assert f.read() == response
    assert f"Ответ модели сохранен в: {export_path}" in caplog.text

@pytest.mark.asyncio
async def test_save_response_exception(code_assistant, mock_gs_path, caplog):
    """Test handling of an exception during save response."""
    file_path = mock_gs_path.src / "test_file.py"
    response = "test response"
    with patch("pathlib.Path.write_text", side_effect=OSError("Test Error")):
        result = await code_assistant._save_response(file_path, response, "gemini")
        assert not result
        assert "Ошибка сохранения файла" in caplog.text
        assert "Test Error" in caplog.text


def test_remove_outer_quotes_no_quotes(code_assistant):
    """Test no removal of quotes when not present."""
    response = "test content"
    assert code_assistant._remove_outer_quotes(response) == "test content"

def test_remove_outer_quotes_with_quotes(code_assistant):
    """Test removing outer quotes."""
    response = "```test content```"
    assert code_assistant._remove_outer_quotes(response) == "test content"

def test_remove_outer_quotes_markdown_with_quotes(code_assistant):
    """Test removing outer markdown quotes."""
    response = "```md test content```"
    assert code_assistant._remove_outer_quotes(response) == "test content"

def test_remove_outer_quotes_rst_with_quotes(code_assistant):
    """Test removing outer rst quotes."""
    response = "```rst test content```"
    assert code_assistant._remove_outer_quotes(response) == "test content"

def test_remove_outer_quotes_html_with_quotes(code_assistant):
    """Test removing outer html quotes."""
    response = "```html test content```"
    assert code_assistant._remove_outer_quotes(response) == "test content"

def test_remove_outer_quotes_python_with_quotes(code_assistant):
    """Test no removing outer python quotes."""
    response = "```python test content```"
    assert code_assistant._remove_outer_quotes(response) == "```python test content```"

def test_remove_outer_quotes_mermaid_with_quotes(code_assistant):
     """Test no removing outer mermaid quotes."""
     response = "```mermaid test content```"
     assert code_assistant._remove_outer_quotes(response) == "```mermaid test content```"

def test_remove_outer_quotes_exception(code_assistant, caplog):
    """Test handling of exception in remove_outer_quotes method"""
    with patch("str.strip", side_effect=Exception("Test Exception")):
        result = code_assistant._remove_outer_quotes("test string")
        assert result == ''
        assert "Exception in `remove_outer_quotes()`" in caplog.text

def test_yield_files_content_no_files(code_assistant, mock_gs_path):
    """Test file generation with no files."""
    files = list(code_assistant._yield_files_content(start_dirs=[mock_gs_path.src]))
    assert len(files) == 0

def test_yield_files_content_exclude_file_pattern(code_assistant, mock_gs_path):
     """Test file generation excluding files by pattern."""
     test_file_path = mock_gs_path.src / "test_file.py"
     test_file_path.parent.mkdir(parents=True, exist_ok=True)
     with open(test_file_path, "w") as f:
        f.write("test code")
     test_excluded_path = mock_gs_path.src / "test_exclude.py"
     test_excluded_path.parent.mkdir(parents=True, exist_ok=True)
     with open(test_excluded_path, "w") as f:
        f.write("test code")

     files = list(code_assistant._yield_files_content(start_dirs=[mock_gs_path.src]))
     assert len(files) == 1
     assert files[0][0] == test_file_path

def test_yield_files_content_exclude_dir(code_assistant, mock_gs_path):
    """Test file generation excluding files by directory."""
    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path, "w") as f:
        f.write("test code")
    exclude_dir = mock_gs_path.src / "venv" / "test_exclude.py"
    exclude_dir.parent.mkdir(parents=True, exist_ok=True)
    with open(exclude_dir, "w") as f:
        f.write("test code")
    files = list(code_assistant._yield_files_content(start_dirs=[mock_gs_path.src]))
    assert len(files) == 1
    assert files[0][0] == test_file_path

def test_yield_files_content_exclude_file(code_assistant, mock_gs_path):
     """Test file generation excluding specific files."""
     test_file_path = mock_gs_path.src / "test_file.py"
     test_file_path.parent.mkdir(parents=True, exist_ok=True)
     with open(test_file_path, "w") as f:
         f.write("test code")
     test_exclude_path = mock_gs_path.src / "test_exclude.py"
     test_exclude_path.parent.mkdir(parents=True, exist_ok=True)
     with open(test_exclude_path, "w") as f:
         f.write("test code")
     code_assistant.config.exclude_files = ["test_exclude.py"]
     files = list(code_assistant._yield_files_content(start_dirs=[mock_gs_path.src]))
     assert len(files) == 1
     assert files[0][0] == test_file_path

def test_yield_files_content_exception(code_assistant, mock_gs_path, caplog):
     """Test handling exception on file read."""
     test_file_path = mock_gs_path.src / "test_file.py"
     test_file_path.parent.mkdir(parents=True, exist_ok=True)
     with patch("pathlib.Path.read_text", side_effect=Exception("Test Exception")):
         files = list(code_assistant._yield_files_content(start_dirs=[mock_gs_path.src]))
         assert len(files) == 1
         assert files[0] == (None, None)
         assert "Ошибка при чтении файла" in caplog.text
         assert "Test Exception" in caplog.text

def test_yield_files_content_include_file(code_assistant, mock_gs_path):
    """Test file generation when including files by pattern."""
    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path, "w") as f:
        f.write("test code")
    test_file_path2 = mock_gs_path.src / "test_file2.txt"
    test_file_path2.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path2, "w") as f:
        f.write("test code")

    files = list(code_assistant._yield_files_content(start_dirs=[mock_gs_path.src]))
    assert len(files) == 1
    assert files[0][0] == test_file_path

def test_signal_handler(code_assistant, capsys):
    """Test signal handler"""
    with pytest.raises(SystemExit) as excinfo:
        code_assistant._signal_handler(None, None)
    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert "Процесс был прерван" in captured.out

def test_run(code_assistant, mock_gs_path, mock_gemini_model):
    """Test run method execution."""
    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path, "w") as f:
        f.write("test code")
    
    with patch.object(code_assistant, 'process_files', return_value=asyncio.Future()):
        code_assistant.run()
        code_assistant.process_files.assert_called_once()

def test_main_integration(mock_gs_path, mock_config_file, mock_translations_file, mock_gemini_model, mock_openai_model):
    """Test the main function for a full integration test."""
    # Create a dummy config
    config_data = {
        "argparse": {
            "languages": ["ru", "en"],
            "roles": ["code_checker", "pytest"],
        },
        "exclude_file_patterns": [r"test_.*\.py$"],
        "include_files": ["*.py"],
        "exclude_dirs": ["venv", "__pycache__"],
        "exclude_files": ["test_file.py"],
        "output_directory": {
            "code_checker": "gemini/code_checker/<lang>",
            "doc_writer_md": "gemini/doc_writer_md/<lang>",
            "doc_writer_rst": "gemini/doc_writer_rst/<lang>",
            "doc_writer_html": "gemini/doc_writer_html/<lang>",
            "code_explainer_md": "gemini/code_explainer_md/<lang>",
            "code_explainer_html": "gemini/code_explainer_html/<lang>",
            "pytest": "gemini/pytest/<lang>",
        },
        "remove_prefixes": ["```md", "```rst", "```html", "```python", "```"],
    }
    config_path = mock_gs_path.endpoints / "hypo69" / "code_assistant" / "code_assistant.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config_data, f)
    
    # Create test file
    test_file_path = mock_gs_path.src / "test_file.py"
    test_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file_path, "w") as f:
        f.write("test code")

    # Mock the asyncio.run
    with patch("asyncio.run") as mock_asyncio_run:
        from src.endpoints.hypo69.code_assistant import assistant
        assistant.main()
        assert mock_asyncio_run.call_count == 4
```