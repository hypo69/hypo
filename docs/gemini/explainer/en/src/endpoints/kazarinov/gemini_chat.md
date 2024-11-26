## File hypotez/src/endpoints/kazarinov/gemini_chat.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov 
	:platform: Windows, Unix
	:synopsis: Module that handles model training using GoogleGenerativeAI for the Kazarinov project

"""
MODE = 'dev'
import header
import time
import json
import random
from typing import Optional
from pathlib import Path
from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursively_read_text_files, recursively_get_filepath
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger import logger


class KazarinovAI:
    """Handles model training and dialog generation for the Kazarinov project using GoogleGenerativeAI."""

    api_key = gs.credentials.gemini.kazarinov
    # Base paths for system instructions and training files
    base_path = gs.path.google_drive / 'kazarinov'
    system_instruction_list: list = recursively_read_text_files(base_path, ['*.txt', '*.md'])
    #questions_list:list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])
    history_file = f'{gs.now}.txt'

    gemini_1: GoogleGenerativeAI
    gemini_2: GoogleGenerativeAI
    timestamp = gs.now

    def __init__(self, 
                 system_instruction: str = None, 
                 generation_config: dict | list[dict] = {"response_mime_type": "text/plain"}):
        """Initialize the Kazarinov model.

        Args:
            system_instruction (str, optional): Instruction for the model's system role. Defaults to None.
            generation_config (dict | list[dict], optional): Configuration for content generation. 
                Defaults to {"response_mime_type": "text/plain"}.
        """
        # Initialize the first Gemini model instance
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key, 
            system_instruction=system_instruction, 
            generation_config={"response_mime_type": "text/plain"}, 
            history_file=f'{gs.now}.txt'
        )

        # Initialize the second Gemini model instance (gemini_2)
        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key, 
            system_instruction=system_instruction, 
            generation_config={"response_mime_type": "text/plain"}, 
            history_file=f'{gs.now}.txt'
        )


    def train(self):
        """Train the model using training data in chunks."""
        chunk_size = 500000
        all_chunks = []
        train_data_list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data', ['*.*'], as_list=True)

        current_chunk = ""
        for line in train_data_list:
            while len(current_chunk) + len(line) > chunk_size:
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)
                line = line[space_left:]
                current_chunk = ""
            current_chunk += line

        if current_chunk:
            all_chunks.append(current_chunk)

        for idx, chunk in enumerate(all_chunks):
            pprint(f"{chunk=}\n{len(chunk)}", text_color='light_blue')
            response = self.gemini_1.ask(q=chunk)
            pprint(response, text_color='yellow')
            time.sleep(5)


    def question_answer(self):
        """Handles question answering using training data."""
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)
        for q in questions:
            pprint(self.gemini_1.ask(q))


    def dialog(self):
        """Runs a dialog session."""
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'], as_list=True)
        random.shuffle(questions)
        for q in questions:
            pprint(f'Q:> {q}', text_color='yellow')
            pprint(' ', text_color='green')
            a = self.gemini_1.ask(q)
            pprint(f'A:> {a}', text_color='cyan')
            pprint('------------------------------------', text_color='green')
            time.sleep(5)
            # ... (rest of the dialog function)


    def ask(self, q: str, no_log: bool = False, with_pretrain: bool = True) -> bool:
        """Asks the AI a question."""
        return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq **\n Question: {q}", no_log=no_log, with_pretrain=False)


def chat():
    """Initiates a chat session with the KazarinovAI."""
    questions_list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])
    print(f"""
    To exit, type '--q'
    To load a question from the database, type '--next'""")
    k = KazarinovAI(system_instruction=read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt'))
    logger.info(k.ask("Привет, представься"))
    while True:
        q = input_colored(">>>> ", GREEN)
        if q.lower() == 'exit':
            print("Chat ended.")
            break
        if q.lower() == '--next' or q.lower() == '--нехт':
            q_list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            q = q_list[random.randint(0, len(q_list) - 1)]
            response = k.ask(f"{q}", no_log=True, with_pretrain=False)
            logger.info(response)
            continue

        response = k.ask(q, no_log=False, with_pretrain=False)
        logger.info(response)


if __name__ == "__main__":
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
    #k.dialog()
```

```
<algorithm>
(Step-by-step block diagram for KazarinovAI.train method)

[Start] --> [Read Training Data] --> [Chunk Data] --> [Send Chunk to gemini_1] --> [Get Response] --> [pprint Response] --> [Sleep 5 seconds] --> [Loop Back to Chunk Data] --> [End]

[Read Training Data]: Reads training data from files in specified folders,  turning the files into a list of strings.
    Example Input: List of strings representing text from training files.
    Example Output: List of strings, where each string represents a chunk of training data.

[Chunk Data]: Splits the training data into smaller chunks of a maximum size (chunk_size). 
    Example Input: ["line1", "line2", ..., "lineN"]. 
    Example Output: [["line1", "line2"], ["line3", "line4"], ...].

[Send Chunk to gemini_1]: Sends each chunk to the gemini_1 model for processing.
    Example Input: ["line1", "line2"]
    Example Output: Response from the gemini model.

[Get Response]: Receives the response from the gemini model.

[pprint Response]: Formats and prints the response from gemini in a readable way using the pprint function.


(Block diagram for KazarinovAI class initialization)
[Start] --> [Initialize gemini_1] --> [Initialize gemini_2] --> [End]

[Initialize gemini_1]: Initializes a GoogleGenerativeAI instance (gemini_1) with provided API key, system instruction, generation config, and history file.
[Initialize gemini_2]: Initializes a GoogleGenerativeAI instance (gemini_2) with the same configuration as gemini_1.

```

```
<explanation>

- **Imports:**  The script imports various modules needed for its functionality:
    - `header`: Likely contains project-specific header or utility functions.
    - `time`: Provides time-related functions (e.g., `time.sleep`).
    - `json`: For handling JSON data (likely for saving/loading data).
    - `random`: For random operations (e.g., shuffling questions).
    - `typing.Optional`: For type hinting.
    - `pathlib.Path`: For working with file paths.
    - `src.gs`:  Project-specific module containing global settings and resources.
    - `src.ai.openai`: Likely contains functions related to the OpenAI API (if needed).
    - `src.ai.gemini`: Contains classes for interacting with Google Generative AI (Gemini) models.
    - `src.utils.file`: Contains functions for file reading, and potentially other file system operations.
    - `src.utils.jjson`: Functions for handling JSON data.
    - `src.utils.printer`: For formatted printing output (e.g., using colors).
    - `src.logger`: A custom logger to record events.
    
The `src` package structure suggests a modular design for the project.  The imports show a clear dependency relationship between different project modules.

- **Classes:**
    - `KazarinovAI`: This class encapsulates the logic for model training, question answering, and dialog interactions. 
        - `api_key`: Stores the API key for the Gemini model.
        - `base_path`: Specifies the base directory for training data and instructions.
        - `system_instruction_list`: Contains system instructions read from files in the project folder.
        - `gemini_1`, `gemini_2`:  Instances of `GoogleGenerativeAI` for interacting with the Gemini model.
        - `__init__`: Initializes `KazarinovAI` instances, creating Gemini model objects.
        - `train`: Trains the model by feeding chunks of training data to `gemini_1`.  Critically, it handles chunking to avoid overloading the model's input size.  Potentially slow due to the `time.sleep(5)` delay after each model call.
        - `question_answer`: Processes questions from a file.
        - `dialog`: Runs a dialog session based on shuffled questions (interacting with `gemini_1`).
        - `ask`:  A method for interacting with `gemini_1` to pose a question, including the ability to suppress logging (no_log).

- **Functions:**
    - `chat`:  Starts the user interaction loop, handling user input, and calling `KazarinovAI` methods.

- **Variables:** `MODE`, `chunk_size`, `all_chunks`, `current_chunk`, `train_data_list`, `questions`, `q`, `a`, `response` etc. are all crucial variables that contribute to different stages of the training and question-answering processes.

- **Potential Errors/Improvements:**
    - The `time.sleep(5)` within the `train` loop is significant.  It pauses the program for 5 seconds after each call to the Gemini API. This is likely a necessary delay to avoid overwhelming the API or encountering rate limits. However, consider optimizing the training process using more sophisticated batching or asynchronous processing if possible.
    - The `ask` method within the `KazarinovAI` class has an unnecessary and potentially confusing parameter `no_log`.  The usage and effect of this is unclear.  Better variable names and comments might clarify its purpose.
    - The `with_pretrain` parameter should be used consistently across code to help clarify whether the model is making use of previous training.


- **Relationships:**  The code strongly depends on `src` package components, particularly `gs` for accessing credentials, file paths, and utilities. The `GoogleGenerativeAI` class from the `src.ai.gemini` package is crucial for interacting with the Gemini model, demonstrating a clear dependency between the `kazarinov` module and other components within the project.