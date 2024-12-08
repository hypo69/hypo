# tinytroupe.enrichment.py

## Overview

This module provides the `TinyEnricher` class for enriching content using a large language model (LLM). It leverages templates for constructing LLM messages and extracts code blocks from the LLM's response.

## Classes

### `TinyEnricher`

**Description**: This class extends `JsonSerializableRegistry` and handles the enrichment of content using an LLM. It manages a context cache for maintaining previous results.

**Methods**:

#### `__init__`

**Description**: Initializes the `TinyEnricher` object.

**Parameters**:

- `use_past_results_in_context` (bool): A boolean flag indicating whether to use past results in the context. Defaults to `False`.

**Returns**:
- None

#### `enrich_content`

**Description**: Enriches the input content using the LLM.

**Parameters**:

- `requirements` (str): The requirements for the content enrichment.
- `content` (str): The content to be enriched.
- `content_type` (str, optional): The type of the content. Defaults to `None`.
- `context_info` (str, optional): Additional context information. Defaults to `""`.
- `context_cache` (list, optional): A list of previous context results. Defaults to `None`.
- `verbose` (bool, optional): A boolean flag to enable verbose output. Defaults to `False`.

**Returns**:
- dict | None: Returns a dictionary containing the enriched content or None if no enrichment was performed.

**Raises**:
- `Exception`: Any exceptions raised during the LLM communication process.

## Functions

(No functions defined in this file, only classes are present)