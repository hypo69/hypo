```python
import pytest
import json
import os

# Since the input is a markdown file containing a question and answer,
# we will create dummy functions to simulate reading and parsing this content.
# In a real scenario, you'd be testing your actual functions.
# Here, we will create functions to represent possible processing logic.

def load_markdown_file(filepath):
    """Loads the markdown file.
       For the test, we'll just check if the file exists.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    #In a real application this would read and return the content.
    with open(filepath, 'r', encoding="utf-8") as f:
        content = f.read()
    return content

def parse_question_answer(markdown_content):
    """Parses the question and answer from markdown content."""
    try:
        lines = markdown_content.split("\n")
        question_line = next((line for line in lines if line.startswith("**ВОПРОС**")), None)
        answer_line = next((line for line in lines if line.startswith("**ОТВЕТ**")), None)

        if not question_line or not answer_line:
            raise ValueError("Could not find question or answer tags in markdown.")
        
        question = question_line.replace("**ВОПРОС** ", "").strip()
        answer = answer_line.replace("**ОТВЕТ** ", "").strip()

        return {"question": question, "answer": answer}
    
    except (StopIteration, ValueError) as e:
        raise ValueError(f"Failed to parse question and answer: {e}")


@pytest.fixture
def valid_markdown_filepath():
    """Provides a valid markdown filepath for testing."""
    # Create a dummy file
    filepath = "test_questions.md"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("**ВОПРОС** Почему конфигурационные файлы называются по имени модуля (например: `suppliers.json`)?  \nНе лучше ли было их именовать `config.json`?  \n**ОТВЕТ** Имена файлов сделаны для удобства понимания моделями ИИ.\n")
    yield filepath
    os.remove(filepath)


@pytest.fixture
def invalid_markdown_filepath():
     """Provides an invalid markdown filepath for testing."""
     return "nonexistent_file.md"

@pytest.fixture
def malformed_markdown_content():
    """Provides malformed markdown content for testing."""
    return "**SOME_OTHER_TAG** This is not correct"

def test_load_markdown_file_valid_file(valid_markdown_filepath):
    """Checks if the markdown file can be loaded."""
    content = load_markdown_file(valid_markdown_filepath)
    assert isinstance(content, str)
    assert len(content) > 0

def test_load_markdown_file_file_not_found(invalid_markdown_filepath):
    """Checks FileNotFoundError when the markdown file does not exist."""
    with pytest.raises(FileNotFoundError):
        load_markdown_file(invalid_markdown_filepath)

def test_parse_question_answer_valid_content(valid_markdown_filepath):
    """Checks the parsing of valid markdown content."""
    markdown_content = load_markdown_file(valid_markdown_filepath)
    qa = parse_question_answer(markdown_content)
    assert isinstance(qa, dict)
    assert "question" in qa
    assert "answer" in qa
    assert qa["question"] == "Почему конфигурационные файлы называются по имени модуля (например: `suppliers.json`)?  \nНе лучше ли было их именовать `config.json`?"
    assert qa["answer"] == "Имена файлов сделаны для удобства понимания моделями ИИ."

def test_parse_question_answer_no_question_tag(malformed_markdown_content):
    """Checks ValueError if question tag is missing."""
    with pytest.raises(ValueError, match="Failed to parse question and answer: Could not find question or answer tags in markdown."):
       parse_question_answer(malformed_markdown_content)

def test_parse_question_answer_no_answer_tag():
    """Checks ValueError if answer tag is missing."""
    no_answer_markdown = "**ВОПРОС** Where is the answer?"
    with pytest.raises(ValueError, match="Failed to parse question and answer: Could not find question or answer tags in markdown."):
        parse_question_answer(no_answer_markdown)

def test_parse_question_answer_empty_content():
    """Checks ValueError if content is empty."""
    with pytest.raises(ValueError, match="Failed to parse question and answer: Could not find question or answer tags in markdown."):
      parse_question_answer("")

```