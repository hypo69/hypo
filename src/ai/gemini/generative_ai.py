## \file hypotez/src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.ai.gemini """
"""Google generative AI integration."""

import time
import json
from pathlib import Path
from datetime import datetime
import base64
from dataclasses import dataclass, field
from typing import Optional, List, Dict
import google.generativeai as genai
from src.logger import logger
from src import gs
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

@dataclass
class GoogleGenerativeAI:
    """Class to interact with Google Generative AI models."""

    api_key: str
    model_name: str = "gemini-1.5-flash-8b"
    system_instruction: Optional[str] = None
    history_file: Optional[Path] = None
    generation_config: Dict = field(default_factory=lambda: {"response_mime_type": "text/plain"})

    MODELS: List[str] = field(default_factory=lambda: [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ])
    mode: str = 'debug'

    dialogue_log_path: Path = field(init=False)
    dialogue_txt_path: Path = field(init=False)
    history_dir: Path = field(init=False)
    history_txt_file: Path = field(init=False)
    history_json_file: Path = field(init=False)

    def __post_init__(self):
        """Initialize paths and configure the model."""
        if self.model_name not in self.MODELS:
            raise ValueError(f"Invalid model name. Choose from {', '.join(self.MODELS)}")

        self.dialogue_log_path = gs.path.google_drive / 'AI' / f"gemini_{gs.now}.json"
        self.dialogue_txt_path = gs.path.google_drive / 'AI' / 'history' / f"gemini_{gs.now}.txt"
        self.history_dir = gs.path.google_drive / 'AI' / 'history'

        self.history_txt_file = self.history_dir / self.history_file if self.history_file else self.history_dir / f'{gs.now}.txt'
        self.history_json_file = self.history_dir / self.history_file if self.history_file else self.history_dir / f'{gs.now}.json'

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            self.model_name,
            generation_config=self.generation_config,
            system_instruction=self.system_instruction
        )

    def _save_dialogue(self, dialogue: list):
        """Save dialogue to both txt and json files with size management.

        Args:
            dialogue (list): Dialogue content to save.
        """
        existing_content = read_text_file(self.history_txt_file)
        new_content = f"{existing_content}\n{str(dialogue)}"

        if len(new_content) > 100_000:
            saved_file_name = f"{gs.now}_{self.history_txt_file.name}"
            new_txt_file_path: Path = self.history_txt_file.parent / saved_file_name
            save_text_file(existing_content, new_txt_file_path, mode='w')
            new_content += str(dialogue)

        save_text_file(new_content, self.history_txt_file, mode='w')

    def ask(self, q: str, history_file: str = None, attempts: int = 3) -> Optional[str]:
        """Send a prompt to the model and get the response.

        Args:
            q (str): The prompt to send.
            history_file (str, optional): History file to use. Defaults to None.
            attempts (int, optional): Number of retry attempts. Defaults to 3.

        Returns:
            Optional[str]: The model's response or None if an error occurs.
        """
      
        self.history_file = self.history_dir / history_file if history_file else self.history_txt_file

        try:
            history = read_text_file(self.history_file)
            complete_prompt = f"{history}\n* question *\n{q}\n* answer **\n"

            if gs.mode == 'debug':
                pprint(f"INPUT > {q}", text_color='light_blue')
                pprint(f"HISTORY FILE: > {self.history_file}", text_color='light_green')
                pprint(f"PROMPT: > {complete_prompt}", text_color='green')

            messages = [
                {"role": "system", "content": self.system_instruction},
                {"role": "user", "content": q}
            ]

            response = self.model.generate_content(str(complete_prompt))

            if not response:
                logger.debug("No response from the model.")
                return

            if gs.mode == 'debug':
                pprint(f"RESPONSE: > {response}", text_color='cyan')

            messages.append({"role": "assistant", "content": response.text})
            self._save_dialogue([messages])

            return response.text

        except Exception as ex:
            logger.error("Error during request", ex)
            if attempts > 0:
                time.sleep(15)
                return self.ask(q, attempts=attempts - 1)
            return

    def describe_image(self, image_path: Path) -> Optional[str]:
        """Generate a description of an image.

        Args:
            image_path (Path): Path to the image file.

        Returns:
            Optional[str]: Description of the image or None if an error occurs.
        """
        try:
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')

            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            logger.error(f"Error describing image: {ex}")
            return

def chat():
    """Run the interactive chat session."""
    logger.debug("Hello, I am the AI assistant of Sergey Kazarinov. Ask your questions.")
    print("Type 'exit' to end the chat.\n")

    system_instruction = input("Enter system instruction (or press Enter to skip): ")
    ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction=system_instruction or None)

    while True:
        user_input = input("> Question: ")
        if user_input.lower() == 'exit':
            print("Chat ended.")
            break

        response = ai.ask(q=user_input)
        print(f">> Response:\n{response}\n")

if __name__ == "__main__":
    chat()
