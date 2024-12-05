# test_extraction.py

## Overview

This module contains unit tests for the `ArtifactExporter` and `Normalizer` classes in the `tinytroupe` package.  It verifies the functionality of exporting artifacts in different formats (JSON, text, docx) and normalizing a list of concepts.

## TOC

- [test_export_json](#test-export-json)
- [test_export_text](#test-export-text)
- [test_export_docx](#test-export-docx)
- [test_normalizer](#test-normalizer)

## Fixtures

### `exporter`

**Description**: A fixture that returns an instance of `ArtifactExporter` with a temporary output folder for testing.

**Returns**:
- `ArtifactExporter`: An instance of the `ArtifactExporter` class.


## Functions

### `test_export_json`

**Description**: Tests the `export` method of `ArtifactExporter` for JSON format.  Verifies that the correct JSON file is created with the expected data.

**Parameters**:
- `exporter` (`ArtifactExporter`): An instance of the `ArtifactExporter` class, provided by the `exporter` fixture.


**Raises**:
- `AssertionError`: If the JSON file is not created or the content of the exported JSON file does not match the expected data.


### `test_export_text`

**Description**: Tests the `export` method of `ArtifactExporter` for text format.  Verifies that the correct text file is created with the expected data.


**Parameters**:
- `exporter` (`ArtifactExporter`): An instance of the `ArtifactExporter` class, provided by the `exporter` fixture.

**Raises**:
- `AssertionError`: If the text file is not created or the content of the exported text file does not match the expected data.


### `test_export_docx`

**Description**: Tests the `export` method of `ArtifactExporter` for docx format, specifically handling markdown formatting preservation.  Checks that the resulting docx file contains the expected content in a formatted manner and does not include the original markdown syntax.

**Parameters**:
- `exporter` (`ArtifactExporter`): An instance of the `ArtifactExporter` class, provided by the `exporter` fixture.

**Raises**:
- `AssertionError`: If the docx file is not created, or the expected content is not found in the exported docx, or the original markdown formatting is present in the output.
- `ImportError`: If the `docx` module is not installed.


### `test_normalizer`

**Description**: Tests the `normalize` method of the `Normalizer` class.  Validates that the correct number of normalized elements is returned and that the normalizing map is populated.  Emphasizes consistent length between input and output concepts.

**Parameters**:
- `None`: This function does not take any parameters directly.
   It uses a `Normalizer` object created within the test function itself.

**Raises**:
- `AssertionError`: If the number of normalized elements is incorrect, the length of the normalized concept is not the same as the input length, or if an element from the normalized concepts isn't found in the normalizing map keys.
- `TypeError`: If any unexpected data type is encountered.

```