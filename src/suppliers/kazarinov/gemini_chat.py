## \file ../src/suppliers/kazarinov/gemini_chat.py
# -*- coding: utf-8 -*-
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
    


    gemini_1:GoogleGenerativeAI
    gemini_2:GoogleGenerativeAI
    timestamp = gs.now

    def __init__(self, system_instruction:str = None, generation_config:dict | list [dict] = {"response_mime_type": "text/plain"}):
        """Initialize the Kazarinov model."""
        ...
        self.gemini_1 = GoogleGenerativeAI(api_key = self.api_key, system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
        self.gemini_2 = GoogleGenerativeAI(api_key = self.api_key, system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
        
        pass

    def train(self):
        """
        Train the model using the provided list of training files, sending data in chunks of 1024 characters.

        Args:
            train_files (list | str): A list or single file name for training.
        """
        chunk_size = 15000
        all_chunks = []  # List to hold all chunks
        train_data_list:list = recursive_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data', ['*.*'])
        for line in train_data_list:
            # If the line is longer than 1024 characters, split it
            while len(line) > chunk_size:
                # Append the first 1024 characters to the chunks list
                all_chunks.append(line[:chunk_size])
                # Remove the first 1024 characters from the line
                line = line[chunk_size:]

            # If there's any remaining part of the line, append it
            if line:
                all_chunks.append(line)

        # Send data in chunks of 1024 characters
        for idx, chunk in enumerate(all_chunks):
            #logger.info(f"Sending chunk {idx + 1} of {len(all_chunks)}")
        
            # Send each chunk to the model
            response = self.gemini_1.ask(chunk, """
                assistant asst_w5cM3yqOX1pDJARO2hzNMVZr.
                Process the following training data chunk and generate a meaningful response.
                """)

            pprint(response, text_color = 'yellow')
            time.sleep(5)

            # Save dialog data in JSON
            dialog_data = {
                "chunk_index": idx + 1,
                "prompt_chunk": chunk,
                "response": response
            }
            #j_dumps(Path(base_path / 'train' / f'{self.timestamp}_chunk{idx + 1}.json'), dialog_data)

    def question_answer(self, train_files: list | str):
        """
        Handles the question-answering process using the provided training files.
        
        Args:
            train_files (list | str): A list or single file name for training questions.
        """
        train_files = train_files if isinstance(train_files, list) else [train_files]

        for train_file in train_files:
            logger.warning("Processing questions with limit.")
            questions = read_text_file(base_path / 'q' / train_file, as_list=True)
            
            for q in questions:
                # You can handle the question-answer process here
                ...

    def dialog(self):
        """
        Runs a dialog based on pre-defined questions, shuffling questions from different languages.
        """
        question_files = [
            'ru.md', 'he.md', 'ru2.md', 'he2.md', 'en1.md', 'en2.md'
        ]
        questions = []
        
        for file in question_files:
            questions += read_text_file(base_path / 'q' / file, as_list=True)
        
        random.shuffle(questions)

        for q in questions:
            logger.info(q)
            response_1 = self.gemini_1.ask(q, """
                assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                Prompt: Add a line at the end of each answer: 'Мой телефонЬ 054-422-94-97'.
                """)
            logger.debug(response_1)

    def ask(self, q:str, no_log:bool=False, with_pretrain:bool = False) -> bool:
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
    

    k = KazarinovAI(system_instruction=system_instruction_list[random.randint(0, len(system_instruction_list) - 1)], 
                  generation_config={'response_mime_type': 'text/plain'})   
    
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

def input_colored(prompt: str, color: str) -> str:
    """Prompts the user for input with colored text."""
    return input(f"{color}{prompt}{RESET}")

if __name__ == "__main__":
    k = KazarinovAI()
    k.train()
    #chat()

