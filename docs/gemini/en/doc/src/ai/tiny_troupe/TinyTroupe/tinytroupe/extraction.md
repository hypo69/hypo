# tinytroupe.extraction

## Overview

This module provides utilities for extracting data from TinyTroupe elements (agents and worlds). It supports extracting key points from interaction histories, generating synthetic data, and converting data into machine-readable formats like JSON or CSV.  It also includes a mechanism for reducing extracted data to a more concise form and exporting artifacts.

## Classes

### `ResultsExtractor`

**Description**: This class provides methods for extracting results from `TinyPerson` and `TinyWorld` instances. It uses OpenAI's API for data extraction and caches the results for later use.

**Methods**

#### `extract_results_from_agent`

**Description**: Extracts results from a `TinyPerson` instance.

**Parameters**:
- `tinyperson` (TinyPerson): The `TinyPerson` instance to extract results from.
- `extraction_objective` (str): The objective of the extraction (e.g., "The main points present in the agent's interactions history.").
- `situation` (str): The situation context for the extraction.
- `fields` (list, optional): A list of fields to extract.  If `None`, the extractor decides the fields to use. Defaults to `None`.
- `fields_hints` (dict, optional): Hints for the fields to extract. Defaults to `None`.
- `verbose` (bool, optional): Whether to print debug messages. Defaults to `False`.

**Returns**:
- `dict | None`: The extraction results as a dictionary, or `None` if no results are returned.

**Raises**:
- `Exception`: If there's an issue with the OpenAI API call or result.



#### `extract_results_from_world`

**Description**: Extracts results from a `TinyWorld` instance.

**Parameters**:
- `tinyworld` (TinyWorld): The `TinyWorld` instance to extract results from.
- `extraction_objective` (str): The objective of the extraction.
- `situation` (str): The situation context.
- `fields` (list, optional): The fields to extract. Defaults to `None`.
- `fields_hints` (dict, optional): Hints for fields. Defaults to `None`.
- `verbose` (bool, optional): Whether to print debug messages. Defaults to `False`.

**Returns**:
- `dict | None`: The extraction results or `None` if no results are returned.

**Raises**:
- `Exception`: If there's a problem with the OpenAI call or result.

#### `save_as_json`

**Description**: Saves the last extraction results to a JSON file.

**Parameters**:
- `filename` (str): The name of the output JSON file.
- `verbose` (bool, optional): Whether to print debug messages. Defaults to `False`.

**Raises**:
- `Exception`: If there is an error with saving the file.


### `ResultsReducer`

**Description**:  This class provides methods for reducing extracted data.

**Methods**

#### `add_reduction_rule`

**Description**: Adds a reduction rule to the reducer.

**Parameters**:
- `trigger` (str): The trigger for the rule (e.g., "greeting").
- `func` (callable): The reduction function to apply.

**Raises**:
- `Exception`: If a rule for the given trigger already exists.


#### `reduce_agent`

**Description**: Reduces the data from an agent's interactions.

**Parameters**:
- `agent` (TinyPerson): The agent to reduce data from.

**Returns**:
- `list`: A list of reduced data.

#### `reduce_agent_to_dataframe`

**Description**: Reduces an agent's data to a Pandas DataFrame.

**Parameters**:
- `agent` (TinyPerson): The agent to reduce data from.
- `column_names` (list, optional): The column names for the DataFrame. Defaults to `None`.

**Returns**:
- `pd.DataFrame`: The reduced data as a DataFrame.


### `ArtifactExporter`

**Description**: This class exports artifacts from TinyTroupe elements.

**Methods**

#### `export`

**Description**: Exports the specified artifact data to a file.

**Parameters**:
- `artifact_name` (str): The name of the artifact.
- `artifact_data` (Union[dict, str]): The data to export.
- `content_type` (str): The type of the content (e.g., "interaction_history").
- `content_format` (str, optional): The format of the content (e.g., "md", "csv"). Defaults to `None`.
- `target_format` (str): The format to export the artifact to (e.g., "json", "txt", "docx").
- `verbose` (bool, optional): Whether to print debug messages. Defaults to `False`.

**Raises**:
- `ValueError`: If the `target_format` is unsupported or `artifact_data` is not a string or dictionary.


#### `_export_as_txt`
#### `_export_as_json`
#### `_export_as_docx`

**Description**: Internal methods for exporting to different formats (txt, json, docx).

### `Normalizer`

**Description**: Normalizes textual elements.

**Methods**


#### `__init__`
**Parameters**:
- `elements` (list): Elements to normalize.
- `n` (int): Number of normalized elements to output.
- `verbose` (bool, optional):  Whether to print debug messages.


#### `normalize`

**Description**: Normalizes the specified element or list of elements.

**Parameters**:
- `element_or_elements` (Union[str, List[str]]): Element or list of elements to normalize.


**Returns**:
- `str | List[str]`:  Normalized element or list of elements.

**Raises**:
- `ValueError`: If the input is not a string or a list.

## Functions


```
```