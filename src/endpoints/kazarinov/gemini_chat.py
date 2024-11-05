## \file ./src/endpoints/kazarinov/gemini_chat.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
# /path/to/interpreter/python
""" 
Module that handles model training using GoogleGenerativeAI for the Kazarinov project.
Logs dialogs into JSON files and processes training prompts.
"""

import header
import time
import json
import random
from typing import Optional
from pathlib import Path
from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursive_read_text_files, recursively_get_filepath
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger import logger



class KazarinovAI:
    """Handles model training and dialog generation for the Kazarinov project using GoogleGenerativeAI."""
    
    api_key = gs.credentials.gemini.kazarinov
    # Base paths for system instructions and training files
    base_path = gs.path.google_drive / 'kazarinov' 
    system_instruction_list: list = recursive_read_text_files(base_path, ['*.txt','*.md'])
    #questions_list:list = recursive_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])
    history_file = f'{gs.now}.txt'


    gemini_1:GoogleGenerativeAI
    gemini_2:GoogleGenerativeAI
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
        # Инициализация экземпляра модели Google Generative AI (gemini_1)
        # Использует переданный API ключ, системные инструкции и файл истории
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key, 
            system_instruction=system_instruction, 
            generation_config={"response_mime_type": "text/plain"}, 
            history_file=f'{gs.now}.txt'
        )

        # Инициализация второго экземпляра модели (gemini_2)
        # Идентична gemini_1, но с отдельным файлом истории
        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key, 
            system_instruction=system_instruction, 
            generation_config={"response_mime_type": "text/plain"}, 
            history_file=f'{gs.now}.txt'
        )

        


    def train(self):
        """
        Train the model using the provided list of training files, sending data in chunks of specified size.

        Args:
            train_files (list | str): A list or single file name for training.
        """
        chunk_size = 500000
        all_chunks = []  # List to hold all chunks
        train_data_list: list = recursive_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data', ['*.*'], as_list = True)
    
        current_chunk = ""  # String to accumulate text for the current chunk

        for line in train_data_list:
            # If the current chunk plus the new line exceeds chunk_size, split it
            while len(current_chunk) + len(line) > chunk_size:
                # Determine how much of the line can be added to the current chunk
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)

                # Start a new chunk with the remainder of the line
                line = line[space_left:]
                current_chunk = ""

            # If there's any remaining part of the line, append it
            current_chunk += line

        # If there's any remaining part of the last chunk, append it
        if current_chunk:
            all_chunks.append(current_chunk)

        # Send data in chunks
        for idx, chunk in enumerate(all_chunks):
            #logger.info(f"Sending chunk {idx + 1} of {len(all_chunks)}")
            pprint(f"{chunk=}\n{len(chunk)}", text_color='light_blue')
        
            # Send each chunk to the model
            #header: str = '** role: '
            response = self.gemini_1.ask(q = chunk)

            pprint(response, text_color='yellow')
            time.sleep(5)

            # # Save dialog data in JSON
            # dialog_data = {
            #     "chunk_index": idx + 1,
            #     "prompt_chunk": chunk,
            #     "response": response
            # }
            # j_dumps(Path(base_path / 'train' / f'{self.timestamp}_chunk{idx + 1}.json'), dialog_data)


    def question_answer(self):
        """
        Handles the question-answering process using the provided training files.
        
        Args:
            train_files (list | str): A list or single file name for training questions.
        """
        questions = recursive_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)

        for q in questions:
            pprint(self.gemini_1.ask(q))

    def dialog(self):
        """
        Runs a dialog based on pre-defined questions, shuffling questions from different languages.
        """
        questions = recursive_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'], as_list=True)
        
        random.shuffle(questions)

        for q in questions:
            pprint(f'Q:> {q}', text_color = 'yellow')                    # <- Q
            pprint(' ', text_color = 'green')
            a = self.gemini_1.ask(q)
            pprint(f'A:> {a}', text_color = 'cyan')                      # <- A
            pprint('------------------------------------', text_color = 'green')
            time.sleep(5)
            ...
            

    def ask(self, q:str, no_log:bool=False, with_pretrain:bool = True) -> bool:
        """Спрашиваю у машины """
        return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \n Question: {q}", no_log = no_log, with_pretrain = False )




def chat():
    """Initiates a chat session with the AI assistant, Kazarinov.

    This function reads system instructions from text files and handles user input
    until the user decides to exit the chat. It uses the Kazarinov class to process
    user queries and provide responses.

    Raises:
        Exception: If there is an issue reading system instruction files.
    """
    

    # k = KazarinovAI(system_instruction=system_instruction_list[random.randint(0, len(system_instruction_list) - 1)], 
    #               generation_config={'response_mime_type': 'text/plain'})   
    
    questions_list:list = recursive_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])

    print(f"""
    Чтобы завершить чат, напишите `--q`
    Чтобы загрузить вопрос из базы вопросов напишите `--next`""")
    
    #logger.debug("Привет, я ИИ ассистент компьюрного мастера Сергея Казаринова. Задавайте вопросы", None, False)
    logger.info(k.ask("Привет, представься"))
    while True:
              
        # Get user input
        q = input_colored(">>>> ", GREEN)
        if q.lower() == 'exit':
            print("Чат завершен.")
            break

        if q.lower() == '--next' or q.lower() == '--нехт':
            q_list:list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            q = q_list[random.randint(0, len(q_list) - 1)]
            print(f"{q=}")
            response = k.ask(f"{q}", no_log = True, with_pretrain = False)
            logger.info(response)
            continue
            
       
        
        # Send the user's question to the AI and get a response
        response = k.ask(q, no_log = False, with_pretrain = False)
        logger.info(response)


if __name__ == "__main__":
    system_instruction = read_text_file( gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt' )
    k = KazarinovAI(system_instruction = system_instruction)
    k.train()
    #k.dialog()

