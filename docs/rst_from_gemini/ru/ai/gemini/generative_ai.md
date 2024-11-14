```python
## \file hypotez/src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai.gemini """
"""Google generative AI integration."""

import time
import json
from pathlib import Path
from datetime import datetime
import base64
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
import google.generativeai as genai
from src.logger import logger
from __init__ import gs
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()


class GoogleGenerativeAI(BaseModel):
    """Class to interact with Google Generative AI models.  Manages model calls and dialogue history.
    """
    model_config = {
        "arbitrary_types_allowed": True
    }

    MODELS: List[str] = Field(default_factory=lambda: [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ])

    api_key: str = Field(..., description="Your Google Generative AI API key.")  # Required
    model_name: str = Field(default="gemini-1.5-flash-8b")
    generation_config: Dict[str, Any] = Field(default_factory=lambda: {"response_mime_type": "text/plain"})
    mode: str = Field(default='debug')
    
    dialogue_log_path: Path = Field(default=gs.path.google_drive / 'AI' / 'log', description="Path to store dialogue logs.")
    dialogue_txt_path: Path = Field(default=None, description="Path to store dialogue logs (dynamically generated).")
    history_dir: Path = Field(default=gs.path.google_drive / 'AI' / 'history', description="Directory to store dialogue history.")
    history_txt_file: Path = Field(default=None, description="Path to store dialogue history (dynamically generated).")
    history_json_file: Path = Field(default=None, description="Path to store dialogue history as JSON (dynamically generated).")
    model: Optional[genai.GenerativeModel] = None
    system_instruction: Optional[str] = Field(default=None, description="System instructions for the model.")


    @validator('dialogue_txt_path', pre=True)  #pre-validation, before __init__
    def _validate_dialogue_path(cls, value, values):
        if value is None:
          return gs.path.google_drive / 'AI' / 'log' / f"gemini_{gs.now}.txt"
        return value
    
    @validator('history_txt_file', pre=True)
    def _validate_history_txt_file(cls, value, values):
        if value is None:
            return values['history_dir'] / f"gemini_{gs.now}.txt"
        return value
        
    @validator('history_json_file', pre=True)
    def _validate_history_json_file(cls, value, values):
        if value is None:
            return values['history_dir'] / f"gemini_{gs.now}.json"
        return value


    def __init__(self, api_key: str, **kwargs):
        """Initialize the GoogleGenerativeAI model with required API key and other settings."""
        # Crucial: api_key validation here
        if not api_key:
          raise ValueError("API key cannot be empty.")
        super().__init__(api_key=api_key, **kwargs)
        genai.configure(api_key=api_key)  # Configure immediately

    # ... (rest of the class remains the same)


def chat():
    """Run the interactive chat session."""
    # ... (rest of the chat function remains the same)
    try:
        ai = GoogleGenerativeAI(api_key="your_api_key", **kwargs)
    except ValueError as e:
        print(f"Error creating AI instance: {e}")
        return


if __name__ == "__main__":
    chat()
```

**Key Improvements and Explanations:**

* **`api_key` Validation:** Added a crucial check in the `__init__` method to ensure that the `api_key` is not empty.  This prevents a runtime error.  If the key is missing, a `ValueError` is raised immediately.
* **`@validator` Decorators:**  Instead of relying on `__post_init__`, which can be a bit tricky, these decorators ensure the dynamic path generation is performed correctly *before* the object is fully initialized.  This is better, more maintainable, and more pythonic.
* **Clearer Docstrings:**  Improved docstrings to be more descriptive, especially for crucial parameters like `api_key` and the different paths.
* **Type Hinting and Annotations:**  Used explicit type hinting (`Optional[str]`, `List[str]`, `Dict[str, Any]`). This increases code clarity and maintainability.
* **Error Handling:** Wrapped the `chat` function in a `try...except` block to catch and report `ValueError` during AI instantiation. This helps prevent crashes due to missing or bad API keys.
* **Default Values:**  Added default values for `dialogue_txt_path`, `history_txt_file`, `history_json_file`  in the `Field` definition. This makes the class more robust.


**How to Use:**

1.  **Replace `"your_api_key"`** with your actual Google Generative AI API key.
2.  **Install the necessary packages:**
    ```bash
    pip install google-generative-ai pydantic
    ```
3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

This improved version is much more robust, readable, and maintainable. It prevents common errors and provides better clarity on how the code functions. Remember to install the required packages before running.


**Important Considerations:**

* **Error Handling:**  While the `try-except` block is a good start, consider logging errors more specifically (e.g., if the Generative AI API returns an error response).
* **Security:** Never hardcode your API key directly in your code; use environment variables or configuration files to store sensitive information.
* **Robustness:** Add more comprehensive error handling within the `ask` and `describe_image` methods to catch potential issues with the Google Generative AI API, network problems, etc.