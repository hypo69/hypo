```python
## file hypotez/src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
"""

MODE = 'dev'
import time
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict
from types import SimpleNamespace
import base64

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from src.logger import logger
from src import gs
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    Этот класс используется для настройки и работы с моделью Google Generative AI, включая отправку запросов,
    получение ответов и сохранение диалогов в текстовых и JSON файлах.

    Атрибуты:
        MODELS (List[str]): Список доступных моделей AI.
        api_key (str): Ключ API для доступа к генеративной модели.
        model_name (str): Название модели для использования.
        generation_config (Dict): Конфигурация для генерации.
        mode (str): Режим работы модели (например, 'debug' или 'production').
        dialogue_log_path (Optional[Path]): Путь для логирования диалогов.
        dialogue_txt_path (Optional[Path]): Путь для сохранения текстовых файлов диалогов.
        history_dir (Path): Директория для хранения истории.
        history_txt_file (Optional[Path]): Путь к файлу для хранения истории в формате текста.
        history_json_file (Optional[Path]): Путь к файлу для хранения истории в формате JSON.
        model (Optional[genai.GenerativeModel]): Объект модели Google Generative AI.
        system_instruction (Optional[str]): Инструкция для системы, которая задает параметры поведения модели.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self,
                 api_key: str,
                 model_name: Optional[str] = None,
                 generation_config: Optional[Dict] = None,
                 system_instruction: Optional[str] = None,
                 **kwargs):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        Этот метод настраивает модель AI, а также определяет пути для логирования и истории.

        Аргументы:
            api_key (str): Ключ API для доступа к генеративной модели.
            model_name (Optional[str], optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
            generation_config (Optional[Dict], optional): Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
            system_instruction (Optional[str], optional): Инструкция для системы. По умолчанию None.
        """

        self.api_key = api_key
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction
        # ... (rest of the class definition)
```

**<algorithm>**

```mermaid
graph TD
    A[User Input (q)] --> B{GoogleGenerativeAI.ask};
    B --> C[Model Generation];
    C --Success--> D[Response (response.text)];
    D --> E[Save Dialogue];
    E --> F[Return Response];
    B --Error--> G[Error Handling];
    G --> H[Error Log];
    H --> F;
```

**Example Data Flow:**

* **User Input (q):** "What's the weather like today?"
* **Model Generation:** The code sends the user input ("What's the weather like today?") to the Google Generative AI model using the `model.generate_content()` method.
* **Response (response.text):** The model returns the generated text (e.g., "The weather is sunny and warm.")
* **Save Dialogue:** The response is saved to both a text file (`history_txt_file`) and a JSON file (`history_json_file`) along with the user input.
* **Return Response:** The generated text is returned to the caller.
* **Error Handling (G):** If there are errors (e.g., network problems, API errors, authentication failures), the code handles them gracefully, logs the error, potentially retries the request, and returns appropriate values.


**<explanation>**

* **Imports:** The code imports necessary modules for various functionalities:
    * `google.generativeai`: For interacting with the Google Generative AI API.
    * `requests`: For making HTTP requests (likely used internally by `google.generativeai`).
    * `pathlib`, `datetime`, `typing`, `base64`: For file paths, timestamps, type hinting, and encoding.
    * `grpc`, `google.api_core.exceptions`: For handling potential errors during API interactions.
    * `google.auth.exceptions`: For handling authentication errors (critical for API access).
    * `src.logger`: For logging messages.
    * `src.gs`: Likely a custom module for Google Cloud Storage, file paths, and likely other file system utilities.
    * `src.utils`: A module for general utility functions.
    * `src.utils.file`, `src.utils.date_time`, `src.utils.jjson`: Modules for file I/O, date/time operations, and JSON handling.  The import structure shows a clear modular organization within the `src` package, which is standard practice for large Python projects.

* **Classes:**
    * `GoogleGenerativeAI`: This class encapsulates the interaction with the Google Generative AI model.  It manages API keys, model selection, generation configuration, and dialogue/history logging.
    * Important attributes: `api_key`, `model_name`, `generation_config`, `system_instruction`, `model`, `dialogue_log_path`, `history_dir`.  The attributes show the necessary information to interact with the API and record interactions.
        * The `__init__` method sets up the configuration. The `__post_init__` method handles the situation when the `api_key` is available later.
    * Methods: `ask`, `describe_image`, `_save_dialogue`, and `config`. `ask` is the core method for interacting with the model.

* **Functions:**
    * `ask`: Takes a question (`q`) and generates a response from the Google Generative AI model.  It handles potential errors (`requests`, `grpc`, authentication) and implements exponential backoff for retrying failed requests, which is crucial for robust API interaction.

    * `describe_image`: Sends an image encoded in base64 to the model for description.
    * `chat`: The main function for starting an interactive chat session with the AI model. It prompts for the user's input.


* **Variables:**
    * `MODELS`: A list of supported model names.
    * `MODE`: A string indicating the operation mode (e.g., 'dev', 'production').
    * `timeout_check`: An instance of `TimeoutCheck` (from `src.utils.date_time`).

* **Potential Errors and Improvements:**

    * **Robust Error Handling:** The `ask` method has extensive error handling, which is a strong design choice for production-ready code.
    * **Exponential Backoff:**  The `ask` method's implementation of exponential backoff is good practice, preventing overwhelming the API.  Explicit timeouts could improve robustness to unexpected issues.
    * **Rate Limiting:**  The code doesn't explicitly handle rate limiting. If the API has rate limits, add logic to respect them.
    * **Authentication:**  The `api_key` is hardcoded. This is insecure. In production, the `api_key` should be fetched from a secure location (e.g., environment variables or a configuration file).


**Relationship with Other Parts of the Project:**

The code interacts with several modules in the `src` package (`logger`, `gs`, `utils`, `utils.file`, `utils.date_time`, `utils.jjson`), demonstrating a clear modular design pattern. The `gs` module (Google Storage) is likely responsible for file system operations. This separation of concerns improves maintainability and code organization.  The `generative_ai.json` file referenced in `config` is likely an external configuration file used for storing any parameters or keys that shouldn't be hardcoded.

The `chat()` function is a CLI interface to the generative AI model, illustrating a typical use case.  The way the `system_instruction` is used suggests that this code might form part of a larger application or framework that allows users to customize the AI assistant's behaviour.