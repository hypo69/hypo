```python
import pytest
import argparse
import json
from pathlib import Path
from unittest.mock import patch
from hypotez.src.endpoints.hypo69.code_assistant.main import parse_args, main, CodeAssistant  # Replace with your actual import

# Fixture for a sample settings file
@pytest.fixture
def sample_settings_file(tmp_path):
    settings = {
        "role": "doc_writer",
        "lang": "en",
        "model": ["openai"],
        "start_dirs": ["/path/to/test/dir"],
    }
    settings_file = tmp_path / "settings.json"
    with open(settings_file, "w") as f:
        json.dump(settings, f)
    return str(settings_file)

# Fixture for mocking CodeAssistant initialization and processing
@pytest.fixture
def mock_code_assistant():
    with patch('hypotez.src.endpoints.hypo69.code_assistant.main.CodeAssistant') as MockAssistant:  # Correctly patch the CodeAssistant import in main
        mock_instance = MockAssistant.return_value
        mock_instance.initialize_models.return_value = None
        mock_instance.process_files.return_value = None
        yield MockAssistant

def test_parse_args_no_args():
    """
    Tests the parse_args function with no command-line arguments.
    It should return a dictionary with default values for optional arguments.
    """
    with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace()):
        args = parse_args()
        assert isinstance(args, dict)
        assert args.get('role') is None
        assert args.get('lang') == 'en'
        assert args.get('models') is None
        assert args.get('start_dirs') is None

def test_parse_args_with_settings(sample_settings_file):
    """
    Tests the parse_args function when a settings file is specified.
    The settings file path should be correctly parsed.
    """
    with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(settings=sample_settings_file)):
          args = parse_args()
          assert args['settings'] == sample_settings_file
          assert args.get('role') is None


def test_parse_args_with_all_args():
    """
    Tests the parse_args function with all command-line arguments specified.
    All arguments should be parsed and stored correctly.
    """
    with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        role='code_checker',
        lang='ru',
        models=['gemini', 'openai'],
        start_dirs=['dir1', 'dir2'],
        settings=None
    )):
        args = parse_args()
        assert args['role'] == 'code_checker'
        assert args['lang'] == 'ru'
        assert args['models'] == ['gemini', 'openai']
        assert args['start_dirs'] == ['dir1', 'dir2']

def test_parse_args_invalid_role():
    """
    Tests that the argument parser raises a SystemExit exception when an invalid role is specified.
    """
    with pytest.raises(SystemExit):
          with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(role='invalid_role')):
              parse_args()

def test_parse_args_invalid_lang():
    """
    Tests that the argument parser raises a SystemExit exception when an invalid language is specified.
    """
    with pytest.raises(SystemExit):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(lang='invalid_lang')):
            parse_args()

def test_parse_args_invalid_model():
    """
     Tests that the argument parser raises a SystemExit exception when an invalid model is specified.
    """
    with pytest.raises(SystemExit):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(models=['invalid_model'])):
           parse_args()
            

def test_main_with_settings_file(sample_settings_file, mock_code_assistant, capsys):
    """
    Tests the main function when a valid settings file is specified.
    It checks if the CodeAssistant is initialized with settings from the file.
    """
    with patch('hypotez.src.endpoints.hypo69.code_assistant.main.parse_args', return_value={'settings': sample_settings_file}):
        main()
        mock_code_assistant.assert_called_once()
        mock_code_assistant.return_value.initialize_models.assert_called_once()
        mock_code_assistant.return_value.process_files.assert_called_once()
        captured = capsys.readouterr()
        assert "Starting Code Assistant..." in captured.out

def test_main_with_nonexistent_settings_file(tmp_path, capsys, mock_code_assistant):
    """
    Tests the main function with a non-existent settings file.
    It should print an error message and not initialize the CodeAssistant.
    """
    nonexistent_file = str(tmp_path / "nonexistent.json")
    with patch('hypotez.src.endpoints.hypo69.code_assistant.main.parse_args', return_value={'settings': nonexistent_file}):
            main()
            captured = capsys.readouterr()
            assert f'Файл настроек "{nonexistent_file}" не найден.' in captured.out
            mock_code_assistant.assert_not_called()


def test_main_with_command_line_args(mock_code_assistant, capsys):
    """
    Tests the main function with command-line arguments.
    It should initialize the CodeAssistant with the provided command-line arguments.
    """
    with patch('hypotez.src.endpoints.hypo69.code_assistant.main.parse_args', return_value={
        'role': 'code_analyzer',
        'lang': 'ru',
        'models': ['gemini'],
        'start_dirs': ['dir1', 'dir2'],
    }):
        main()
        mock_code_assistant.assert_called_once()
        mock_code_assistant.assert_called_with(role='code_analyzer', lang='ru', model=['gemini'], start_dirs=[Path('dir1'), Path('dir2')])
        mock_code_assistant.return_value.initialize_models.assert_called_once()
        mock_code_assistant.return_value.process_files.assert_called_once()
        captured = capsys.readouterr()
        assert "Starting Code Assistant..." in captured.out

def test_main_with_default_args(mock_code_assistant, capsys):
    """
    Tests the main function when no settings or command-line arguments are provided.
     It checks if the CodeAssistant is initialized with default parameters.
    """
    with patch('hypotez.src.endpoints.hypo69.code_assistant.main.parse_args', return_value={}):
            main()
            mock_code_assistant.assert_called_once()
            mock_code_assistant.assert_called_with(role=None, lang='en', model=['gemini'], start_dirs=[])
            mock_code_assistant.return_value.initialize_models.assert_called_once()
            mock_code_assistant.return_value.process_files.assert_called_once()
            captured = capsys.readouterr()
            assert "Starting Code Assistant..." in captured.out

def test_main_with_empty_start_dirs(mock_code_assistant, capsys):
    """
    Tests the main function with command-line arguments with an empty start_dirs list.
    It should initialize the CodeAssistant with an empty start_dirs.
    """
    with patch('hypotez.src.endpoints.hypo69.code_assistant.main.parse_args', return_value={
        'role': 'code_analyzer',
        'lang': 'en',
        'models': ['gemini'],
        'start_dirs': [],
    }):
            main()
            mock_code_assistant.assert_called_once()
            mock_code_assistant.assert_called_with(role='code_analyzer', lang='en', model=['gemini'], start_dirs=[])
            mock_code_assistant.return_value.initialize_models.assert_called_once()
            mock_code_assistant.return_value.process_files.assert_called_once()
            captured = capsys.readouterr()
            assert "Starting Code Assistant..." in captured.out
```