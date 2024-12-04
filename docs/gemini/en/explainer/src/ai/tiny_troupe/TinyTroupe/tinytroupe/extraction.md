# Code Explanation: tinytroupe/extraction.py

## <input code>

```python
"""
Simulations produce a lot of data, and it is often useful to extract these data in a structured way. For instance, you might wish to:
  - Extract the main points from an agent's interactions history, so that you can consult them later in a concise form.
  - Generate synthetic data from a simulation, so that you can use it for training machine learning models or testing software.
  - Simply turn some of the data into a more machine-readable format, such as JSON or CSV, so that you can analyze it more easily.

This module provides various utilities to help you extract data from TinyTroupe elements, such as agents and worlds. It also provides a 
mechanism to reduce the extracted data to a more concise form, and to export artifacts from TinyTroupe elements. Incidentaly, it showcases 
one of the many ways in which agent simulations differ from AI assistants, as the latter are not designed to be introspected in this way.
"""

import os
import json
import chevron
import logging
import pandas as pd
import pypandoc
import markdown 
from typing import Union, List
import logging
logger = logging.getLogger("tinytroupe")

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry

from tinytroupe import openai_utils
import tinytroupe.utils as utils
```

## <algorithm>

```mermaid
graph TD
    A[ResultsExtractor] --> B{extract_results_from_agent};
    B --> C[Render Template];
    C --> D{Get Interaction History};
    D --> E{Compose Extraction Request};
    E --> F[Send Message to OpenAI];
    F --> G{Extract JSON};
    G --> H[Cache Result];
    H --> I[Return Result];
    
    J[ResultsExtractor] --> K{extract_results_from_world};
    K --> L[Render Template];
    L --> M{Get Interaction History};
    M --> N{Compose Extraction Request};
    N --> O[Send Message to OpenAI];
    O --> P{Extract JSON};
    P --> Q[Cache Result];
    Q --> R[Return Result];

    S[ArtifactExporter] --> T{Export};
    T --> U[Compose File Path];
    U --> V[Handle Target Format];
    V --> W{Export Artifact};


    Note right of I: Agent Extraction Results
    Note right of R: World Extraction Results
    Note right of W: Exported Artifact File
```

## <mermaid>

```mermaid
graph LR
    subgraph TinyTroupe Extraction
        ResultsExtractor --> extract_results_from_agent
        extract_results_from_agent --> Send_message_to_OpenAI
        Send_message_to_OpenAI --> Extract_json
        Extract_json --> Cache_result
        Cache_result --> Return_result
        ResultsExtractor --> extract_results_from_world
        extract_results_from_world --> Send_message_to_OpenAI
        Send_message_to_OpenAI --> Extract_json
        Extract_json --> Cache_result
        Cache_result --> Return_result
        ArtifactExporter --> Export
        Export --> Compose_file_path
        Compose_file_path --> Handle_target_format
        Handle_target_format --> Export_artifact
    end
    
    Send_message_to_OpenAI --> openai_utils.client()
    Extract_json --> tinytroupe.utils.extract_json
    Return_result -.-> ResultsExtractor
    Export_artifact --> os.path.join(base_output_folder, subfolder)

    TinyPerson --> TinyPerson.pretty_current_interactions
    TinyWorld --> TinyWorld.pretty_current_interactions
    
    
    classDef system fill:#ccf,stroke:#333,stroke-width:2px
    classDef agent fill:#ccf,stroke:#333,stroke-width:2px
    classDef world fill:#ccf,stroke:#333,stroke-width:2px


```

## <explanation>

**Imports:**

- `os`, `json`, `chevron`, `logging`, `pandas`, `pypandoc`, `markdown`, `typing`: Standard Python libraries for file operations, JSON handling, templating, logging, data manipulation, and type hinting.
- `logging`: Used for logging messages during execution. `logger = logging.getLogger("tinytroupe")` creates a logger specifically for the `tinytroupe` module.
- `pypandoc`: Used for converting between different document formats, crucial for exporting data to DOCX format.
- `markdown`: Used for converting markdown to HTML.  Essential for a proper DOCX conversion because pypandoc doesn't have a direct Markdown to DOCX conversion path.
- `tinytroupe.agent`, `tinytroupe.environment`, `tinytroupe.factory`, `tinytroupe.utils`: These are internal modules of the `tinytroupe` project.  They likely define classes and functions related to agents, environments, factories, and utility functions.
- `openai_utils`: Likely a custom module for interacting with OpenAI APIs.
- `tinytroupe.utils`:  Provides utility functions used within `tinytroupe`.

**Classes:**

- `ResultsExtractor`:  Responsible for extracting results from TinyPerson and TinyWorld instances using OpenAI prompts.
    - `__init__`: Initializes the class with a path to a template for OpenAI prompts. Also initializes empty dictionaries for caching results.
    - `extract_results_from_agent`, `extract_results_from_world`: These methods take elements (`TinyPerson`, `TinyWorld`) and an extraction objective, situation, optional fields and hints, and verbose flag.  They compose OpenAI prompts using `chevron` templates, send requests, process the OpenAI responses (using `extract_json` helper function from `tinytroupe.utils`), and cache the results.  They handle different scenarios for agent and world data, adjusting the prompt accordingly.
    - `save_as_json`: Saves the cached extraction results to a JSON file.

- `ResultsReducer`: Reduces agent data based on predefined reduction rules.
    - `__init__`: Initializes the class with an empty dictionary to store the results and another to store rules.
    - `add_reduction_rule`: Adds a reduction rule based on a trigger (e.g., stimulus type) and a function to process that trigger.
    - `reduce_agent`: Iterates over the agent's episodic memory, applying reduction rules to stimulus and action messages as needed. Critically, handles `system` messages, and correctly refers to the `source_agent` and `target_agent` context.
    - `reduce_agent_to_dataframe`: Converts the reduced agent data into a Pandas DataFrame.


- `ArtifactExporter`: Exports artifacts (e.g., simulation data).  Inherits from `JsonSerializableRegistry`.
    - `__init__`: Initializes with a base output folder.
    - `export`: Exports the specified data (`artifact_data`) to a file with specific format (e.g., `json`, `txt`, `docx`). The function handles `content` formatting and name cleaning, preventing common file system issues (e.g. invalid character).
    - `_export_as_json`, `_export_as_txt`, `_export_as_docx`: Internal methods for exporting data in different formats. This is extremely useful for flexibility in dealing with various output formats.  Specifically, the DOCX export utilizes `pypandoc` to convert the content (e.g., markdown or plain text) to DOCX format through an HTML intermediate step.
    - `_compose_filepath`: Constructs the complete file path, handling different content types, extensions, and intermediate directories.  

- `Normalizer`: Normalizes passages, concepts, and other textual elements using OpenAI.
    - `__init__`: Initializes with elements to normalize, `n` (number of normalized elements) and `verbose` flag. Caches the normalization mappings using `self.normalizing_map` and stores the results.
    - `normalize`: Normalizes element(s) using OpenAI prompts. This method efficiently uses a cache (`self.normalizing_map`) to avoid redundant normalization requests for the same element.  Handles both single strings and lists of strings to normalize.


**Functions:**

- Various utility functions (`utils`) exist to support data extraction, template rendering, and file operations (e.g., `dedent`, `extract_json`). This is important for modularity and maintainability.

**Variables:**

- `_extraction_prompt_template_path`, `agent_extraction`, `world_extraction`: Internal variables, crucial for handling prompt generation and caching of data.
- `self.rules`: Holds reduction rules in `ResultsReducer`.
- `self.base_output_folder`: Specifies the root directory for storing exported artifacts in `ArtifactExporter`.

**Potential Errors and Improvements:**

- Error handling in `ArtifactExporter` could be improved. Checking for the correct format and the existence of the `content` key in the dictionary when exporting should be done explicitly.
- Consider adding a mechanism for managing and validating the reduction rules (in `ResultsReducer`) to avoid unexpected behavior. This would include error handling, input validation, and documentation of the types of expected functions (`func` in `add_reduction_rule`) in order to avoid unexpected execution paths.
- The use of `utils.extract_json` is a good choice because it may handle different formats/edge cases of JSON input. However, it would be better to be more explicit with the exception handling in case of non-JSON input.

**Relationships:**

The code heavily relies on other parts of the `tinytroupe` project, specifically classes like `TinyPerson` and `TinyWorld`. The `openai_utils` module is crucial for communication with OpenAI. The `utils` module serves a support function and has likely dependencies of its own.


This comprehensive analysis provides a detailed understanding of the code's functionality, potential issues, and relationships with other parts of the project.