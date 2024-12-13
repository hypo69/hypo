```python
import pytest
import os
import json
from unittest.mock import MagicMock, patch
import pandas as pd
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.extraction import ResultsExtractor, ResultsReducer, ArtifactExporter, Normalizer
from tinytroupe import utils

# Fixtures

@pytest.fixture
def mock_openai_utils():
    with patch('tinytroupe.extraction.openai_utils') as mock:
      mock.client.return_value.send_message.return_value = {"content": '{"key": "value"}'}
      yield mock

@pytest.fixture
def example_tinyperson():
    person = TinyPerson("TestPerson")
    person.episodic_memory.add({"role": "user", "content": {"stimuli": [{"type": "test_stimulus", "content": "test_content", "source": "test_source"}]},"simulation_timestamp":0 })
    person.episodic_memory.add({"role": "assistant", "content": {"action": {"type": "test_action", "content": "test_action_content", "target": "test_target"}}, "simulation_timestamp": 1})
    return person

@pytest.fixture
def example_tinyworld():
    world = TinyWorld("TestWorld")
    person1 = TinyPerson("Person1")
    person2 = TinyPerson("Person2")
    world.add_agent(person1)
    world.add_agent(person2)
    person1.episodic_memory.add({"role": "user", "content": {"stimuli": [{"type": "test_stimulus", "content": "test_content", "source": "test_source"}]},"simulation_timestamp":0 })
    person1.episodic_memory.add({"role": "assistant", "content": {"action": {"type": "test_action", "content": "test_action_content", "target": "test_target"}}, "simulation_timestamp": 1})

    person2.episodic_memory.add({"role": "user", "content": {"stimuli": [{"type": "test_stimulus", "content": "test_content", "source": "test_source"}]},"simulation_timestamp":0 })
    person2.episodic_memory.add({"role": "assistant", "content": {"action": {"type": "test_action", "content": "test_action_content", "target": "test_target"}}, "simulation_timestamp": 1})


    return world

@pytest.fixture
def example_artifact_exporter():
    return ArtifactExporter("test_output_folder")

@pytest.fixture
def example_normalizer():
    return Normalizer(["element1", "element2"], 2)



# Tests for ResultsExtractor
def test_results_extractor_init():
    """Tests if the ResultsExtractor is initialized correctly."""
    extractor = ResultsExtractor()
    assert extractor.agent_extraction == {}
    assert extractor.world_extraction == {}
    assert os.path.exists(extractor._extraction_prompt_template_path)


def test_extract_results_from_agent(mock_openai_utils, example_tinyperson):
    """Tests extracting results from a TinyPerson instance."""
    extractor = ResultsExtractor()
    result = extractor.extract_results_from_agent(example_tinyperson, extraction_objective="Test Objective", situation="Test Situation", fields=["field1"], fields_hints={"field1": "hint1"}, verbose=True)
    assert result == {"key": "value"}
    assert extractor.agent_extraction["TestPerson"] == {"key": "value"}
    mock_openai_utils.client.return_value.send_message.assert_called()

def test_extract_results_from_agent_no_fields(mock_openai_utils, example_tinyperson):
    """Tests extracting results from a TinyPerson instance with no fields specified."""
    extractor = ResultsExtractor()
    result = extractor.extract_results_from_agent(example_tinyperson, extraction_objective="Test Objective", situation="Test Situation", verbose=True)
    assert result == {"key": "value"}
    assert extractor.agent_extraction["TestPerson"] == {"key": "value"}
    mock_openai_utils.client.return_value.send_message.assert_called()


def test_extract_results_from_agent_no_result(mock_openai_utils, example_tinyperson):
    """Tests extracting results from a TinyPerson instance when the LLM does not return any results."""
    mock_openai_utils.client.return_value.send_message.return_value = None
    extractor = ResultsExtractor()
    result = extractor.extract_results_from_agent(example_tinyperson, extraction_objective="Test Objective", situation="Test Situation")
    assert result == None
    assert extractor.agent_extraction["TestPerson"] == None
    mock_openai_utils.client.return_value.send_message.assert_called()


def test_extract_results_from_world(mock_openai_utils, example_tinyworld):
    """Tests extracting results from a TinyWorld instance."""
    extractor = ResultsExtractor()
    result = extractor.extract_results_from_world(example_tinyworld, extraction_objective="Test Objective", situation="Test Situation", fields=["field1"], fields_hints={"field1": "hint1"}, verbose=True)
    assert result == {"key": "value"}
    assert extractor.world_extraction["TestWorld"] == {"key": "value"}
    mock_openai_utils.client.return_value.send_message.assert_called()

def test_extract_results_from_world_no_fields(mock_openai_utils, example_tinyworld):
    """Tests extracting results from a TinyWorld instance with no fields specified."""
    extractor = ResultsExtractor()
    result = extractor.extract_results_from_world(example_tinyworld, extraction_objective="Test Objective", situation="Test Situation", verbose=True)
    assert result == {"key": "value"}
    assert extractor.world_extraction["TestWorld"] == {"key": "value"}
    mock_openai_utils.client.return_value.send_message.assert_called()

def test_extract_results_from_world_no_result(mock_openai_utils, example_tinyworld):
    """Tests extracting results from a TinyWorld instance when the LLM does not return any results."""
    mock_openai_utils.client.return_value.send_message.return_value = None
    extractor = ResultsExtractor()
    result = extractor.extract_results_from_world(example_tinyworld, extraction_objective="Test Objective", situation="Test Situation")
    assert result == None
    assert extractor.world_extraction["TestWorld"] == None
    mock_openai_utils.client.return_value.send_message.assert_called()


def test_save_as_json(tmp_path):
    """Tests saving the last extraction results as JSON."""
    extractor = ResultsExtractor()
    extractor.agent_extraction = {"agent1": {"key1": "value1"}}
    extractor.world_extraction = {"world1": {"key2": "value2"}}
    file_path = tmp_path / "test.json"
    extractor.save_as_json(str(file_path), verbose=True)
    with open(file_path, "r") as f:
        data = json.load(f)
    assert data == {"agent_extractions": {"agent1": {"key1": "value1"}}, "world_extraction": {"world1": {"key2": "value2"}}}

# Tests for ResultsReducer
def test_results_reducer_init():
    """Tests if the ResultsReducer is initialized correctly."""
    reducer = ResultsReducer()
    assert reducer.results == {}
    assert reducer.rules == {}

def test_add_reduction_rule():
    """Tests adding a reduction rule."""
    reducer = ResultsReducer()
    mock_func = MagicMock()
    reducer.add_reduction_rule("test_trigger", mock_func)
    assert "test_trigger" in reducer.rules
    assert reducer.rules["test_trigger"] == mock_func

def test_add_existing_reduction_rule():
    """Tests adding a reduction rule with a trigger that already exists."""
    reducer = ResultsReducer()
    mock_func = MagicMock()
    reducer.add_reduction_rule("test_trigger", mock_func)
    with pytest.raises(Exception, match="Rule for test_trigger already exists."):
         reducer.add_reduction_rule("test_trigger", mock_func)


def test_reduce_agent(example_tinyperson):
    """Tests reducing an agent's interactions using reduction rules."""
    reducer = ResultsReducer()
    mock_func = MagicMock(return_value={"reduced": True})
    reducer.add_reduction_rule("test_stimulus", mock_func)
    reducer.add_reduction_rule("test_action", mock_func)
    reduction = reducer.reduce_agent(example_tinyperson)
    assert len(reduction) == 2
    assert reduction[0] == {"reduced": True}
    assert reduction[1] == {"reduced": True}
    assert mock_func.call_count == 2 # this ensures that the rule was called for both `stimulus` and `action`

def test_reduce_agent_system_message(example_tinyperson):
    """Tests that system messages are skipped during reduction"""
    reducer = ResultsReducer()
    mock_func = MagicMock(return_value={"reduced": True})
    reducer.add_reduction_rule("test_stimulus", mock_func)
    reducer.add_reduction_rule("test_action", mock_func)
    example_tinyperson.episodic_memory.add({"role": "system", "content": "test_system_message", "simulation_timestamp": 2})
    reduction = reducer.reduce_agent(example_tinyperson)
    assert len(reduction) == 2
    assert mock_func.call_count == 2 # this ensures that the rule was called only for stimulus and action, and not for the system message

def test_reduce_agent_no_reduction_rule(example_tinyperson):
    """Tests reducing an agent when there is no rule matching the stimulus / action type."""
    reducer = ResultsReducer()
    reduction = reducer.reduce_agent(example_tinyperson)
    assert len(reduction) == 0

def test_reduce_agent_to_dataframe(example_tinyperson):
    """Tests reducing an agent's interactions to a pandas DataFrame."""
    reducer = ResultsReducer()
    mock_func = MagicMock(return_value={"test_col": "test_val"})
    reducer.add_reduction_rule("test_stimulus", mock_func)
    reducer.add_reduction_rule("test_action", mock_func)
    df = reducer.reduce_agent_to_dataframe(example_tinyperson, column_names=["test_col"])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert df["test_col"][0] == "test_val"
    assert df["test_col"][1] == "test_val"

def test_reduce_agent_to_dataframe_no_column_names(example_tinyperson):
    """Tests reducing an agent's interactions to a pandas DataFrame when no column names are specified."""
    reducer = ResultsReducer()
    mock_func = MagicMock(return_value={"test_col": "test_val"})
    reducer.add_reduction_rule("test_stimulus", mock_func)
    reducer.add_reduction_rule("test_action", mock_func)
    df = reducer.reduce_agent_to_dataframe(example_tinyperson)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert df.iloc[0,0] == "test_val"
    assert df.iloc[1,0] == "test_val"

# Tests for ArtifactExporter
def test_artifact_exporter_init():
    """Tests if the ArtifactExporter is initialized correctly."""
    exporter = ArtifactExporter("test_output_folder")
    assert exporter.base_output_folder == "test_output_folder"

def test_export_string_as_txt(example_artifact_exporter, tmp_path):
    """Tests exporting a string artifact as a txt file."""
    artifact_name = "test_artifact"
    artifact_data = "test_content"
    content_type = "test_type"
    example_artifact_exporter.export(artifact_name, artifact_data, content_type, target_format="txt")
    file_path = tmp_path / "test_output_folder" / content_type / f"{artifact_name}.txt"
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        assert f.read() == artifact_data

def test_export_string_as_md(example_artifact_exporter, tmp_path):
    """Tests exporting a string artifact as a markdown file."""
    artifact_name = "test_artifact"
    artifact_data = "test_content"
    content_type = "test_type"
    example_artifact_exporter.export(artifact_name, artifact_data, content_type, target_format="md")
    file_path = tmp_path / "test_output_folder" / content_type / f"{artifact_name}.md"
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        assert f.read() == artifact_data

def test_export_dict_as_json(example_artifact_exporter, tmp_path):
    """Tests exporting a dict artifact as a json file."""
    artifact_name = "test_artifact"
    artifact_data = {"key": "value"}
    content_type = "test_type"
    example_artifact_exporter.export(artifact_name, artifact_data, content_type, target_format="json")
    file_path = tmp_path / "test_output_folder" / content_type / f"{artifact_name}.json"
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        assert json.load(f) == artifact_data

def test_export_string_as_docx(example_artifact_exporter, tmp_path):
    """Tests exporting a string artifact as a docx file."""
    artifact_name = "test_artifact"
    artifact_data = "# test_content"
    content_type = "test_type"
    example_artifact_exporter.export(artifact_name, artifact_data, content_type, content_format="md", target_format="docx")
    file_path = tmp_path / "test_output_folder" / content_type / f"{artifact_name}.docx"
    assert os.path.exists(file_path)

def test_export_dict_as_docx(example_artifact_exporter, tmp_path):
     """Tests exporting a dict artifact as a docx file."""
     artifact_name = "test_artifact"
     artifact_data = {"content": "# test_content"}
     content_type = "test_type"
     example_artifact_exporter.export(artifact_name, artifact_data, content_type, content_format="md", target_format="docx")
     file_path = tmp_path / "test_output_folder" / content_type / f"{artifact_name}.docx"
     assert os.path.exists(file_path)

def test_export_unsupported_format(example_artifact_exporter):
    """Tests exporting with an unsupported target format."""
    artifact_name = "test_artifact"
    artifact_data = "test_content"
    content_type = "test_type"
    with pytest.raises(ValueError, match="Unsupported target format: pdf."):
        example_artifact_exporter.export(artifact_name, artifact_data, content_type, target_format="pdf")

def test_export_invalid_artifact_data(example_artifact_exporter):
    """Tests exporting an invalid artifact data type."""
    artifact_name = "test_artifact"
    artifact_data = 123
    content_type = "test_type"
    with pytest.raises(ValueError, match="The artifact data must be either a string or a dictionary."):
         example_artifact_exporter.export(artifact_name, artifact_data, content_type)
    
def test_export_invalid_docx_content_format(example_artifact_exporter):
    """Tests exporting to docx with invalid content format."""
    artifact_name = "test_artifact"
    artifact_data = "test_content"
    content_type = "test_type"
    with pytest.raises(ValueError, match="The original format cannot be csv to export to DOCX."):
        example_artifact_exporter.export(artifact_name, artifact_data, content_type, content_format="csv", target_format="docx")

def test_compose_filepath_with_target_format(example_artifact_exporter):
     """Tests composing the file path with a target format."""
     artifact_data = "test_content"
     artifact_name = "test_artifact"
     content_type = "test_type"
     file_path = example_artifact_exporter._compose_filepath(artifact_data, artifact_name, content_type, target_format="json")
     assert file_path == os.path.join("test_output_folder", content_type, "test_artifact.json")

def test_compose_filepath_no_target_format_string(example_artifact_exporter):
    """Tests composing the file path with no target format for string artifact."""
    artifact_data = "test_content"
    artifact_name = "test_artifact"
    content_type = "test_type"
    file_path = example_artifact_exporter._compose_filepath(artifact_data, artifact_name, content_type)
    assert file_path == os.path.join("test_output_folder", content_type, "test_artifact.txt")

def test_compose_filepath_no_target_format_dict(example_artifact_exporter):
    """Tests composing the file path with no target format for a dict artifact (this should not happen)."""
    artifact_data = {"key": "value"}
    artifact_name = "test_artifact"
    content_type = "test_type"
    file_path = example_artifact_exporter._compose_filepath(artifact_data, artifact_name, content_type, target_format="json")
    assert file_path == os.path.join("test_output_folder", content_type, "test_artifact.json")

def test_compose_filepath_no_content_type(example_artifact_exporter):
     """Tests composing the file path with no content type."""
     artifact_data = "test_content"
     artifact_name = "test_artifact"
     file_path = example_artifact_exporter._compose_filepath(artifact_data, artifact_name, None, target_format="txt")
     assert file_path == os.path.join("test_output_folder", "", "test_artifact.txt")

def test_compose_filepath_invalid_artifact_name(example_artifact_exporter):
     """Tests composing the file path with invalid artifact names."""
     artifact_data = "test_content"
     artifact_name = "test/artifact:name?*"
     content_type = "test_type"
     file_path = example_artifact_exporter._compose_filepath(artifact_data, artifact_name, content_type, target_format="txt")
     assert file_path == os.path.join("test_output_folder", content_type, "test-artifact-name--.txt")


# Tests for Normalizer
def test_normalizer_init(mock_openai_utils):
    """Tests if the Normalizer is initialized correctly."""
    normalizer = Normalizer(["element1", "element2"], 2, verbose=True)
    assert normalizer.elements == ["element1", "element2"]
    assert normalizer.n == 2
    assert normalizer.normalized_elements == {"key": "value"}
    assert normalizer.normalizing_map == {}
    mock_openai_utils.client.return_value.send_message.assert_called()

def test_normalizer_init_non_unique_elements(mock_openai_utils):
    """Tests if the Normalizer is initialized with non unique elements, and that those are filtered out."""
    normalizer = Normalizer(["element1", "element1", "element2"], 2, verbose=True)
    assert normalizer.elements == ["element1", "element2"]
    assert normalizer.n == 2
    assert normalizer.normalized_elements == {"key": "value"}
    assert normalizer.normalizing_map == {}
    mock_openai_utils.client.return_value.send_message.assert_called()

def test_normalize_single_element(mock_openai_utils, example_normalizer):
    """Tests normalizing a single element."""
    mock_openai_utils.client.return_value.send_message.return_value = {"content": '["normalized_element1"]'}
    normalized_element = example_normalizer.normalize("element1")
    assert normalized_element == ["normalized_element1"]
    assert example_normalizer.normalizing_map["element1"] == "normalized_element1"
    mock_openai_utils.client.return_value.send_message.assert_called()

def test_normalize_multiple_elements(mock_openai_utils, example_normalizer):
    """Tests normalizing multiple elements."""
    mock_openai_utils.client.return_value.send_message.return_value = {"content": '["normalized_element1", "normalized_element2"]'}
    normalized_elements = example_normalizer.normalize(["element1", "element2"])
    assert normalized_elements == ["normalized_element1", "normalized_element2"]
    assert example_normalizer.normalizing_map["element1"] == "normalized_element1"
    assert example_normalizer.normalizing_map["element2"] == "normalized_element2"
    mock_openai_utils.client.return_value.send_message.assert_called()


def test_normalize_already_normalized_elements(mock_openai_utils, example_normalizer):
    """Tests normalizing elements that have already been normalized (using cache)."""
    mock_openai_utils.client.return_value.send_message.return_value = {"content": '["normalized_element1", "normalized_element2"]'}
    example_normalizer.normalize(["element1", "element2"]) # first call to trigger the mapping and caching
    mock_openai_utils.client.return_value.send_message.assert_called_once() # test that there was one call
    mock_openai_utils.client.reset_mock() # reset the mock to check that no new call occurs
    normalized_elements = example_normalizer.normalize(["element1", "element2"])
    assert normalized_elements == ["normalized_element1", "normalized_element2"]
    assert example_normalizer.normalizing_map["element1"] == "normalized_element1"
    assert example_normalizer.normalizing_map["element2"] == "normalized_element2"
    mock_openai_utils.client.return_value.send_message.assert_not_called()


def test_normalize_mixed_elements(mock_openai_utils, example_normalizer):
    """Tests normalizing a mix of new and already normalized elements."""
    mock_openai_utils.client.return_value.send_message.return_value = {"content": '["normalized_element2", "normalized_element3"]'}
    example_normalizer.normalize("element1") # pre-normalize element 1
    normalized_elements = example_normalizer.normalize(["element1", "element2", "element3"])
    assert normalized_elements == ["normalized_element1", "normalized_element2", "normalized_element3"]
    assert example_normalizer.normalizing_map["element1"] == "normalized_element1"
    assert example_normalizer.normalizing_map["element2"] == "normalized_element2"
    assert example_normalizer.normalizing_map["element3"] == "normalized_element3"
    mock_openai_utils.client.return_value.send_message.assert_called_once()

def test_normalize_invalid_input_type(example_normalizer):
    """Tests normalizing with an invalid input type."""
    with pytest.raises(ValueError, match="The element_or_elements must be either a string or a list."):
        example_normalizer.normalize(123)

def test_normalize_invalid_LLM_output(mock_openai_utils, example_normalizer):
    """Tests normalizing when the LLM does not return a list."""
    mock_openai_utils.client.return_value.send_message.return_value = {"content": '{"normalized_element": "test"}'}
    with pytest.raises(AssertionError, match="The normalized element must be a list."):
      example_normalizer.normalize("element1")

def test_normalize_invalid_LLM_output_length(mock_openai_utils, example_normalizer):
    """Tests normalizing when the LLM returns a list of a wrong length."""
    mock_openai_utils.client.return_value.send_message.return_value = {"content": '["normalized_element1"]'}
    with pytest.raises(AssertionError, match="The number of normalized elements must be equal to the number of elements to normalize."):
      example_normalizer.normalize(["element1", "element2"])
```