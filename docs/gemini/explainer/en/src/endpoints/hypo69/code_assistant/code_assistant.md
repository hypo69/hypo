```
## File hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.hypo69.code_assistant
    :platform: Windows, Unix
    :synopsis: Module for code assistant functionality
"""

MODE = "dev"


"""
Module for code assistant functionality
=========================================================================================

This module contains the :class:`CodeAssistant` class, used to interact with various AI models,
such as Google Gemini and OpenAI, for code processing tasks.

Example Usage
--------------------

Example usage of the `CodeAssistant` class:

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
"""

import argparse
import sys
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace
import signal
import time
import re
import fnmatch

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.printer import pprint
from src.utils.path import get_relative_path
from src.logger import logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary


class CodeAssistant:
    """Class for interacting with AI models for code assistance."""

    role: str
    lang: str
    start_dirs: Path | str | list[Path] | list[str]
    base_path: Path
    config: SimpleNamespace
    gemini_model: GoogleGenerativeAI
    openai_model: OpenAIModel
    start_file_number: int

    def __init__(self, **kwargs):
        """Initializes the assistant with given parameters."""
        self.role = kwargs.get("role", "doc_writer_rst")
        self.lang = "en" if self.role == "pytest" else kwargs.get("lang", "EN")
        self.model = kwargs.get("model", ["gemini"])
        self.start_dirs = kwargs.get("start_dirs", [".."])
        self.base_path = gs.path.endpoints / "hypo69" / "code_assistant"
        self.config = j_loads_ns(self.base_path / "code_assistant.json")
        self.gemini_model = None
        self.openai_model = None
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs):
        """Initializes AI models based on parameters."""
        if "gemini" in self.model:
            self.gemini_model = GoogleGenerativeAI(
                model_name="gemini-1.5-flash-8b",
                api_key=gs.credentials.gemini.onela,
                **kwargs,
            )
        if "openai" in self.model:
            self.openai_model = OpenAIModel(
                model_name="gpt-4o-mini",
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwargs,
            )

    # ... (rest of the code)
```

<algorithm>

```mermaid
graph TD
    A[Main Loop] --> B{Load Config};
    B --> C[Process Files];
    C --> D[Get Files];
    D --> E{Iterate Files};
    E -- File Matches -- > F[Create Request];
    F --> G{Gemini Model?};
    G -- Yes --> H[Ask Gemini];
    H --> I[Save Response];
    G -- No --> J[OpenAI Model?];
    J -- Yes --> K[Ask OpenAI];
    K --> L[Save Response];
    J -- No --> M[Skip];
    E -- File Does Not Match -- > N[Skip];
    I --> O[Sleep];
    O --> C;
    L --> O;
    M --> O;
    N --> O;
```

**Example Data Flow:**

*   **A:**  The main script continually loops, loading configurations.
*   **B:** Configuration (e.g., file patterns, models to use) is loaded from `code_assistant.json`.
*   **D:**  `_yield_files_content` retrieves file paths from specified directories.
*   **F:** `_create_request` constructs a request dictionary for the AI model, including file content, instructions, role, language, etc.
*   **H/K:**  If Gemini is available, it's used; otherwise, OpenAI.
*   **I/L:** The response is saved to a file (e.g., `docs/<role>/<model>/<language>/<filename>).
*   **O:** A delay is introduced using `time.sleep` (important for rate limiting or for allowing the model response to be received).
*   **C:** The loop continues processing subsequent files.


</algorithm>

<explanation>

*   **Imports:** The code imports necessary modules from various parts of the project (`src` package).
    *   `argparse`: for command-line argument parsing.
    *   `sys`, `pathlib`, `typing`, `types`, `signal`, `time`, `re`, `fnmatch`: for basic system functions, file system interaction, type hinting, signal handling, time manipulation, regular expression, and filename matching.
    *   `gs`: likely a global settings module.
    *   `jjson`: for JSON handling.
    *   `gemini`, `openai`: modules for interacting with Google Gemini and OpenAI AI models.
    *   `printer`: for formatted printing.
    *   `path`: for path manipulation.
    *   `logger`: for logging.
    *   `make_summary`: Likely a module to generate summaries (relationship to docs generation).


*   **Classes:**
    *   `CodeAssistant`:  This is the main class, responsible for handling the entire code processing pipeline.
        *   `__init__`: Initializes the assistant with parameters, loads configuration, and initializes AI models.
        *   `_initialize_models`: Loads Gemini and OpenAI models if specified.
        *   `parse_args`: Parses command-line arguments.
        *   `process_files`:  Iterates through files, creates requests, sends them to AI models, and saves the responses.
        *   `_create_request`: Builds the request payload for the AI model.
        *   `_yield_files_content`: Yields file paths and content, handling inclusion/exclusion criteria based on patterns and directories.
        *   `_save_response`: Saves the AI model's response to files following specific naming conventions.
        *   `_remove_outer_quotes`: Cleans up response strings, removing surrounding code blocks.
        *   `run`: Starts the processing, adding signal handling for interruption.
        *   `_signal_handler`: Handles the process interruption gracefully.


*   **Functions:** Many helper functions exist for specific tasks (e.g., handling requests, saving responses, extracting data).


*   **Variables:**
    *   `MODE`: a string variable for likely a development/production mode.
    *   `config`: `SimpleNamespace` object holding configuration loaded from `code_assistant.json`.
    *   `role`, `lang`, `model`, `start_dirs`: hold user parameters.

*   **Potential Errors/Improvements:**
    *   **Error Handling**: The code has `try...except` blocks, but error handling could be improved by providing more specific error messages and logging more detailed information.
    *   **Rate Limiting**: The `time.sleep(20)` is a critical issue.  It needs careful review. It may be causing significant delays. Consider proper rate limiting mechanisms from the AI provider's API documentation.
    *   **Robustness:** The code may not handle various edge cases gracefully.  Improve error handling for file reading and missing files.
    *   **Debugging**: `response = True` in `process_files` is a debug line. This should be removed in a production environment.
    *   **Clearer Variable Names**: Variable names can be more expressive and descriptive (e.g., `file_location_translated` -> `translated_file_path`).
    *   **Code Style**: Consider using more consistent naming conventions and coding style to improve readability.
    *   **`make_summary` call:** In the `_yield_files_content` loop, this line is commented out: `make_summary(docs_dir = start_dir.parent / 'docs')`. This suggests a potential integration with a summary generation process, which should be investigated and properly integrated if it needs to be run.



*   **Relationships:**
    *   The code heavily relies on the `src` package, especially modules like `gs` (for credentials and paths), `gemini`, `openai`, `utils.jjson`, `utils.printer`, and `utils.path`.
    *   The code has dependencies to `make_summary` within the same repository.
    *   There is a link with a configuration file (`code_assistant.json`), which controls behavior and settings.
    *   The `translations.json` is used for internationalization, which links to internationalization logic.
    *   The project structure seems to be following a standard file organization to decouple logic, and that makes the relationships of modules more visible and comprehensible.


</explanation>