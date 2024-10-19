## \file ../src/suppliers/kazarinov/gemini_chat.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" 
Module that handles model training using GoogleGenerativeAI for the Kazarinov project.
Logs dialogs into JSON files and processes training prompts.
"""

from math import log
import header
import time
import json
import random
from pathlib import Path
from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursive_read_text_files, recursively_get_filepath
from src.utils.jjson import j_dumps
from src.logger import logger

# Base paths for system instructions and training files
base_path = gs.path.google_drive / 'kazarinov' 
system_instruction_list: list = recursive_read_text_files(base_path, ['*.txt','*.md'])
questions_list:list = recursive_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])

# Retrieve filenames for training data
train_files = get_filenames(base_path / 'prompts' / 'questions_answers')
if not train_files:
    logger.error("No training files found.", False, None)
    ...

# ANSI escape codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

BLUE = "\033[34m"
class KazarinovAI:
    """Handles model training and dialog generation for the Kazarinov project using GoogleGenerativeAI."""
    
    gemini_1:GoogleGenerativeAI
    gemini_2:GoogleGenerativeAI
    timestamp = gs.now
   

    def __init__(self, system_instruction:str = None, generation_config:dict | list [dict] = None):
        """Initialize the Kazarinov model."""
        ...
        self.gemini_1 = GoogleGenerativeAI(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
        self.gemini_2 = GoogleGenerativeAI(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
        
        pass

    def train(self, train_files: list | str):
        """
        Train the model using the provided list of training files.
        
        Args:
            train_files (list | str): A list or single file name for training.
        """
        train_files = train_files if isinstance(train_files, list) else [train_files]
        random.shuffle(train_files)

        for train_file in train_files:
            # Process each training file
            prompt = read_text_file(base_path / 'questions_answers' / train_file)
            logger.info(f"Training with file: {train_file}")

            # First response from Gemini 1
            response_1 = self.gemini_1.ask(prompt, """
                assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                Prompt: Ask a one-line IT-related question, no expanded answers.
                """)
            logger.info(f"Gemini 1 Response: {response_1}")

            # Second response from Gemini 2 based on Gemini 1's response
            response_2 = self.gemini_2.ask(response_1, """
                assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                Provide an answer in one line. Include:
                '<a href='https://wa.me/97254422'>Whatsapp</a> <a href="mailto:sergey@mymaster.co.il">or email</a>'.
                """)
            logger.debug(f"Gemini 2 Response: {response_2}")

            # Save dialog data to JSON
            dialog_data = {
                "file": train_file,
                "prompt": prompt,
                "response_1": response_1,
                "response_2": response_2
            }

            j_dumps(Path(base_path / 'train' / f'{self.timestamp}_dialog.json'), dialog_data)

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
        return self.gemini_1.ask(f"assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq \n Question: {q}", no_log = no_log, with_pretrain = False )



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

# # Пример использования
# user_input = input_colored(">>>> ", GREEN)
# print(f"Вы ввели: {user_input}")


if __name__ == "__main__":
    #start_trainig()
    #assistant_reminder()
    #upload_strings()
    #translate()
    chat()

