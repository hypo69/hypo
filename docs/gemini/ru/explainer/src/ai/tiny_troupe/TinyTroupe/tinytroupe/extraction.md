# <input code>

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
```
# <algorithm>

**1. Initialization (ResultsExtractor):**

*   Creates an instance of `ResultsExtractor`.
*   Sets the path to the extraction prompt template.
*   Initializes empty dictionaries `agent_extraction` and `world_extraction` to cache results.

**2. Extract Results from Agent:**

*   Takes `TinyPerson` instance and extraction parameters.
*   Renders the prompt template using `chevron` with provided fields and hints.
*   Retrieves the interaction history from `tinyperson`.
*   Constructs an extraction request prompt, including the objective, situation, and interaction history.
*   Sends the prompt to the OpenAI API via `openai_utils.client().send_message()`.
*   Extracts JSON data from the response using `utils.extract_json()`.
*   Caches the result in `self.agent_extraction`.
*   Returns the extracted result.

**3. Extract Results from World:**

*   Similar to step 2, but for `TinyWorld` instance.
*   Constructs a different prompt that considers interactions from multiple agents within the environment.
*   Caches the result in `self.world_extraction`.


**4. Save as JSON:**

*   Saves the cached results (`agent_extraction`, `world_extraction`) to a JSON file.


**5. Reduction (ResultsReducer):**

*   Initializes `ResultsReducer` and an empty `results` dictionary.  
*   Adds reduction rules using `add_reduction_rule`.
*   Handles `stimulus` and `action` messages:
    *   If a message is of type 'stimulus' or 'action', and a rule exists, applies that rule, extracting data.
    *   Adds the extracted data to the `reduction` list.
*   Creates a DataFrame from the `reduction` list.


**6. Export (ArtifactExporter):**

*   Initializes `ArtifactExporter` with a base output folder.
*   Handles different export formats (txt, json, docx):
    *   Handles potential issues like invalid characters in artifact names.
    *   Uses `_compose_filepath` to generate the correct file path.
    *   Uses appropriate methods (`_export_as_txt`, `_export_as_json`, `_export_as_docx`) to export the artifact data in the selected format.  
*   Handles string and dictionary inputs for `artifact_data`.
*   Handles different content types.


**7. Normalization (Normalizer):**

*   Initializes `Normalizer` with elements, number of desired outputs and verbosity flag.
*   Gets rid of duplicate elements.
*   Constructs initial LLM messages using templates.
*   Sends the messages to the LLM.
*   Extracts the normalized results.

**8. Normalization (continued):**

*   Uses the caching mechanism (`normalizing_map`) to only normalize elements not already normalized.
*   Returns normalized results.


```
# <mermaid>
```mermaid
graph LR
    subgraph Initialization
        A[ResultsExtractor] --> B{agent_extraction};
        A --> C{world_extraction};
        B --> D[extract_results_from_agent];
    end
    subgraph Extraction
        D --> E[openai_utils.client().send_message];
        E --> F[utils.extract_json];
        F --> G[cache result];
        D --> H[extract_results_from_world];
    end
    subgraph Saving
        G --> I[save_as_json];
        I --> J{save to file};
    end
    subgraph Reduction
        K[ResultsReducer] --> L{add_reduction_rule};
        L --> M[reduce_agent];
        M --> N[DataFrame creation];
    end
    subgraph Exporting
        O[ArtifactExporter] --> P{export};
        P --> Q[compose filepath];
        Q --> R{_export_as_txt};
        Q --> S{_export_as_json};
        Q --> T{_export_as_docx};
    end
    subgraph Normalization
        U[Normalizer] --> V{initial LLM message};
        V --> W[process normalized result];
        W --> X[normalize];
    end
    
    A --> D;
    A --> H;
    K --> M;
    O --> P;
    U --> V;
```
# <explanation>

**Imports**:

*   `os`, `json`, `chevron`, `logging`, `pandas`, `pypandoc`, `markdown`, `typing`, `openai_utils`: Standard Python libraries and custom libraries from the `tinytroupe` project.  `pypandoc` and `markdown` are used for document format conversion.
*   `tinytroupe.agent`, `tinytroupe.environment`, `tinytroupe.factory`, `tinytroupe.utils`: Modules from the `tinytroupe` package, likely containing classes and functions related to agents, environments, and utility functions, respectively.
*   `openai_utils`: Likely a module from the project that handles interactions with the OpenAI API.
*   `tinytroupe.utils`: Provides utility functions used throughout the code, such as JSON extraction and prompt template rendering.


**Classes**:

*   **`ResultsExtractor`**: Handles data extraction from agents and worlds, caching results for later use.  It's crucial for organizing simulation data and leveraging the results in further analysis or reporting.   `agent_extraction` and `world_extraction` are dictionaries for caching results; the structure is suitable for quick lookup based on the agent/world name.

*   **`ResultsReducer`**: Reduces the extracted data further using predefined rules.  `rules` dictionary allows flexible and customizable data reduction.   The structure is suitable to process historical data and apply reduction rules.

*   **`ArtifactExporter`**: Responsible for exporting the extracted data into various formats (JSON, text, DOCX).   `base_output_folder` makes it easy to control output locations and avoids hardcoding.  `_export_*` methods provide specific format handling, preventing code duplication.

*   **`Normalizer`**: Normalizes textual elements, likely to improve data consistency and quality for subsequent processing steps, potentially important for semantic analysis.  It demonstrates a proper use of caching with `normalizing_map` for efficiency.

**Functions**:

*   `extract_results_from_agent`, `extract_results_from_world`: These functions send prompts to OpenAI to extract insights from interaction histories.
*   `save_as_json`: Saves extracted results to a JSON file. The method is clear and well-documented.
*   `add_reduction_rule`: Adds rules to the `ResultsReducer` for further data processing. The code handles the possibility of a rule already existing and raises an exception, a vital aspect for correctness.
*   `reduce_agent`: Reduces agent data based on defined rules and events, effectively summarizing information extracted from the data, facilitating the process of analyzing agent activities.  The structure carefully considers both stimulus and action types, with the ability to apply custom functions depending on the specific event.
*   `reduce_agent_to_dataframe`: Creates a pandas DataFrame from the reduced agent data. This step is essential to making the data usable for further analysis.
*   `export`: Exports an artifact in various formats like JSON, text, or DOCX files.  The function is well-structured, considering different types of input data and output formats, allowing for various uses of this module.


**Variables**:

*   `_extraction_prompt_template_path`: Path to the template for constructing prompts to send to the LLM.  This makes the code adaptable to different input structures.
*   `agent_extraction`, `world_extraction`: Dictionaries to cache the extraction results for agents and worlds, respectively. This improves performance by avoiding redundant API calls.
*   `results`: An empty dictionary in the `ResultsReducer` class.  Suitable for storing the results of data reduction.
*   `rules`: A dictionary to store the reduction rules in the `ResultsReducer` class.


**Possible Errors or Improvements**:

*   Error handling in `ResultsReducer.add_reduction_rule`: The function should ideally raise a more informative exception if a rule for the trigger already exists. The current exception message is slightly too generic.


**Relationships with other parts of the project**:

*   The code heavily relies on `tinytroupe.agent`, `tinytroupe.environment`, `tinytroupe.utils`, and `openai_utils`. This clearly indicates that this extraction module is part of a larger TinyTroupe project aimed at agent simulation and interactions.  The relationships to `tinytroupe` classes and functions are crucial for the project's architecture. The `utils` module and `openai_utils` provide important supporting functions to the entire framework.  The use of the OpenAI API suggests a role in data analysis and generation within the broader simulation.