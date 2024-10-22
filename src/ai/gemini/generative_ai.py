# -*- coding: utf-8 -*-
"""Google generative AI integration."""
import time
import json
from pathlib import Path
from datetime import datetime
import base64
import google.generativeai as genai
from src.logger import logger
from src import gs
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """Class to interact with Google Generative AI models."""

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, 
                 api_key: str, 
                 model_name: str = "gemini-1.5-flash-8b",
                 system_instruction: str = None, 
                 history_file: Path = None, 
                 generation_config: dict = {"response_mime_type": "text/plain"}):
        """Initialize GoogleGenerativeAI with the model and API key.

        Args:
            api_key (str): API key for Google Generative AI.
            model_name (str, optional): Name of the model to use. Defaults to "gemini-1.5-flash-8b".
            system_instruction (str, optional): Instruction for system role.
            history_file (Path, optional): Path to the history file.
            generation_config (dict, optional): Configuration for the generation.
                Defaults to {"response_mime_type": "text/plain"}.
        """
        if model_name not in self.MODELS:
            raise ValueError(f"Invalid model name. Choose from {', '.join(self.MODELS)}")

        self.dialogue_log_path = gs.path.google_drive / 'AI' / f"gemini_{gs.now}.json"
        self.dialogue_txt_path = gs.path.google_drive / 'AI' / 'history'/ f"gemini_{gs.now}.txt"
        self.history_dir = gs.path.google_drive / 'AI' / 'history'
        self.history_txt_file = self.history_dir / history_file if history_file else self.history_dir / f'{gs.now}.txt' 
        self.history_json_file = self.history_dir / history_file if history_file else self.history_dir / f'{gs.now}.json'
        self.system_instruction = system_instruction

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name,
            generation_config=generation_config,
            system_instruction=system_instruction
        )


    def _save_dialogue(self, dialogue: list):
        """Save dialogue to both txt and json files with size management.

        Args:
            dialogue (list): Dialogue content to save.
        """
        # Сохранение в txt-файл
        existing_content = read_text_file(self.history_txt_file)
        new_content = f"{existing_content}\n{str(dialogue)}"

        if len(new_content) > 100_000:
            timestamp:str = gs.now
            saved_file_name =  f"{gs.now}_{self.history_txt_file.name}"
            new_txt_file_path:Path = self.history_txt_file.parent / saved_file_name
            save_text_file(existing_content, new_txt_file_path, mode='w')
            new_content += str(dialogue)

        save_text_file(new_content, self.history_txt_file, mode='w')

        # # Сохранение в json-файл
        # try:
        #     if self.history_json_file.exists():
        #         with self.history_json_file.open('r') as f:
        #             existing_data = json.load(f)
        #     else:
        #         existing_data = []

        #     existing_data.append(dialogue)

        #     if len(json.dumps(existing_data)) > 100_000:
        #         new_json_file_path = self.history_json_file.parent / f"{timestamp}_{self.history_json_file.name}"
        #         with new_json_file_path.open('w') as f:
        #             json.dump(existing_data, f, ensure_ascii=False, indent=2)
        #         existing_data = [dialogue]

        #     with self.history_json_file.open('w') as f:
        #         json.dump(existing_data, f, ensure_ascii=False, indent=2)

        # except Exception as ex:
        #     logger.error(f"Error saving dialogue to JSON: {ex}")


    def ask(self, 
        q: str,
        history_file:str = None,
        attempts: int = 3) -> str | None:
        """Send a prompt to the model and get the response.

        Args:
            q (str): The prompt to send.
            attempts (int, optional): Number of retry attempts.

        Returns:
            str | None: The model's response.
        """
        self.history_file = self.history_dir / history_file if history_file else self.history_txt_file
        try:
            history = read_text_file(self.history_file)
            complete_prompt = f"{history}\n* question *\n{q}\n* answer **\n"

            messages = [
                {"role": "system", "content": self.system_instruction},  # Добавлено system_instruction
                {"role": "user", "content": q}
            ]

            response = self.model.generate_content(
                str(complete_prompt), 
            )

            if not response:
                logger.debug("No response from the model.")
                return 

            #pprint(response.text)
            messages.append({"role":"assiatant","content":response.text})
            self._save_dialogue([messages])

            return response.text

        except Exception as ex:
            logger.error("Error during request", ex)
            if attempts > 0:
                time.sleep(15)
                return self.ask(q, attempts=attempts - 1)
            return 

    def describe_image(self, image_path: Path) -> str | None:
        """Generate a description of an image.

        Args:
            image_path (Path): Path to the image file.

        Returns:
            str | None: Description of the image.
        """
        try:
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')

            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            logger.error(f"Error describing image: {ex}")
            return None

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
