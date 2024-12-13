```python
import pytest
import os
import json
import random

import logging
logger = logging.getLogger("tinytroupe")

import sys
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('../')

from testing_utils import *
from tinytroupe.extraction import ArtifactExporter, Normalizer
from tinytroupe import utils

@pytest.fixture
def exporter():
    """Provides an ArtifactExporter instance for tests."""
    return ArtifactExporter(base_output_folder="./test_exports")

def test_export_json(exporter):
    """
    Test exporting artifact data as JSON.
    
    Verifies that the JSON file is created correctly and contains the expected data.
    """
    # Define the artifact data
    artifact_data = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }
    
    # Export the artifact data as JSON
    exporter.export("test_artifact", artifact_data, content_type="record", target_format="json")
    
    # Check if the JSON file was exported correctly
    assert os.path.exists("./test_exports/record/test_artifact.json"), "The JSON file should have been exported."

    # Check if the JSON data is correct
    with open("./test_exports/record/test_artifact.json", "r") as f:
        exported_data = json.load(f)
        assert exported_data == artifact_data, "The exported JSON data should match the original data."

def test_export_text(exporter):
    """
    Test exporting artifact data as plain text.

    Verifies that the text file is created correctly and contains the expected text.
    """
    # Define the artifact data
    artifact_data = "This is a sample text."
    
    # Export the artifact data as text
    exporter.export("test_artifact", artifact_data, content_type="text", target_format="txt")
    
    # Check if the text file was exported correctly
    assert os.path.exists("./test_exports/text/test_artifact.txt"), "The text file should have been exported."

    # Check if the text data is correct
    with open("./test_exports/text/test_artifact.txt", "r") as f:
        exported_data = f.read()
        assert exported_data == artifact_data, "The exported text data should match the original data."

def test_export_docx(exporter):
    """
    Test exporting artifact data as a docx file from markdown content.

    Verifies that the docx file is created correctly and contains the original text
    without markdown formatting.
    """
    # Define the artifact data with markdown formatting
    artifact_data = """
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """
    
    # Export the artifact data as a docx file
    exporter.export("test_artifact", artifact_data, content_type="Document", content_format="markdown", target_format="docx")
    
    # Check if the docx file was exported correctly
    assert os.path.exists("./test_exports/Document/test_artifact.docx"), "The docx file should have been exported."

    # Check if the docx data contains the unformatted text
    from docx import Document
    doc = Document("./test_exports/Document/test_artifact.docx")
    exported_data = ""
    for para in doc.paragraphs:
        exported_data += para.text

    assert "This is a sample markdown text" in exported_data, "The exported docx data should contain some of the original content."
    assert "#" not in exported_data, "The exported docx data should not contain Markdown."

def test_normalizer_initialization():
    """
    Test the initialization of the Normalizer class.
    
    Verifies that the normalized_elements are created with the correct length.
    """
    concepts = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    normalizer = Normalizer(concepts, n=10, verbose=True)
    assert len(normalizer.normalized_elements) == 10, "The number of normalized elements should match the given n."
    assert len(normalizer.normalizing_map.keys()) == 0, "The normalizing map should be empty initially."


def test_normalizer_normalize():
    """
    Test the normalize method of the Normalizer class.
    
    Verifies that the normalized concepts are generated correctly and the internal cache updates as expected.
    """
    # Define the concepts to be normalized
    concepts = [
    'Antique Book Collection', 'Medical Research', 'Electrical safety', 'Reading', 'Technology',
    'Entrepreneurship', 'Multimedia Teaching Tools', 'Photography', 'Smart home technology',
    'Gardening', 'Travel', 'Outdoors', 'Hiking', 'Yoga', 'Finance', 'Health and wellness',
    'Sustainable Living', 'Barista Skills', 'Oral health education', 'Patient care',
    'Professional Development', 'Project safety', 'Coffee', 'Literature', 'Continuous learning',
    'Model trains', 'Education', 'Mental and Physical Balance', 'Kayaking', 'Social Justice',
    'National Park Exploration', 'Outdoor activities', 'Dental technology',
    'Teaching electrical skills', 'Volunteering', 'Cooking', 'Industry trends',
    'Energy-efficient systems', 'Mentoring', 'Empathetic communication', 'Medical Technology',
    'Historical Research', 'Public Speaking', 'Museum Volunteering', 'Conflict Resolution'
    ]
    
    normalizer = Normalizer(concepts, n=10, verbose=True)
    random_concepts_buckets = [random.sample(concepts, 15) for _ in range(5)]

    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())
        normalized_concept = normalizer.normalize(bucket)
        assert normalized_concept is not None, "The normalized concept should not be None."

        next_cache_size = len(normalizer.normalizing_map.keys())

        assert len(normalized_concept) == len(bucket), "The normalized concept should have the same length as the input concept."

        for element in bucket:
            assert element in normalizer.normalizing_map.keys(), f"{element} should be in the normalizing map keys."
        
        assert next_cache_size > 0, "The cache size should be greater than 0 after normalizing a new concept."
        assert next_cache_size >= init_cache_size, "The cache size should not decrease after normalizing a new concept."

def test_export_invalid_content_type(exporter):
    """
    Test the exporter's behavior with an invalid content_type.
    
    Verifies that the correct exception is raised when an invalid content_type is provided.
    """
    with pytest.raises(ValueError, match="Invalid content_type"):
        exporter.export("test_artifact", "test_data", content_type="invalid_type", target_format="json")


def test_export_invalid_target_format(exporter):
     """
    Test the exporter's behavior with an invalid target_format.
    
    Verifies that the correct exception is raised when an invalid target_format is provided.
    """
     with pytest.raises(ValueError, match="Invalid target_format"):
         exporter.export("test_artifact", "test_data", content_type="text", target_format="invalid_format")


def test_normalizer_empty_concepts():
    """
    Test Normalizer with an empty list of concepts.
    
    Verifies that it correctly initializes without errors and that normalize returns empty lists.
    """
    normalizer = Normalizer([], n=5, verbose=True)
    assert len(normalizer.normalized_elements) == 5, "Should initialize with n normalized elements even if the input is empty"
    normalized = normalizer.normalize(["A", "B"])
    assert len(normalized) == 2, "Normalize should return lists with the same size of the inputs"
    assert all(x is None for x in normalized), "Should return empty lists for an empty concepts list."
    assert len(normalizer.normalizing_map.keys()) == 2, "The normalizing map should contain the values"
    
def test_normalizer_none_concepts():
    """
    Test Normalizer with None concepts.

    Verifies that a TypeError is raised when None is passed as the concepts parameter.
    """
    with pytest.raises(TypeError, match="None type is not iterable"):
        Normalizer(None, n=5, verbose=True)
```