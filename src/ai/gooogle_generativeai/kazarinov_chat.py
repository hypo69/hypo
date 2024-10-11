## \file ../src/ai/openai/model/_experiments/kazarinov.py
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
from src.ai import OpenAIModel, GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursive_read_text_files
from src.utils.jjson import j_dumps
from src.logger import logger

# Base paths for system instructions and training files
base_path = gs.path.data / 'kazarinov' / 'prompts'
system_instruction_path = base_path / 'chat_system_instruction.txt'
system_instruction: str = read_text_file(system_instruction_path)

#system_instruction_path_advertisement_strings = base_path / 'system_instruction_path_advertisement_strings.txt'
#system_instruction: str = read_text_file(system_instruction_path_advertisement_strings)

# Retrieve filenames for training data
train_files = get_filenames(base_path / 'questions_answers')
if not train_files:
    logger.error("No training files found.")
    ...

class Kazarinov:
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
                Prompt: Add a line at the end of each answer: '<a href='https://wa.me/972544229497'> Whatsapp </a> 
                <a href="mailto:sergey@mymaster.co.il">or email</a>'.
                """)
            logger.debug(response_1)

    def ask(self, q, system_instruction:str = None) -> bool:
        """Спрашиваю у машины """
        return self.gemini_1.ask(f"assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq {q}", system_instruction)



def start_trainig():
    """Берет информацию и прогоняет через машину. 
    Один сет уже прогнан. Пока не готовторой сет нет смысла запуакть по второму разу
    """
    ...
    return True # <- см объснение в комментарии к функции
    kazarinov = Kazarinov()
    train_files = get_filenames(gs.path.data / 'kazarinov' / 'prompts' / 'questions_answers')
    kazarinov.train(train_files)
    kazarinov.dialog()

def upload_strings():
    """ Беру информацию из файлов рекламых сообщений
    для дообучения модели рекламе """
    ...
    base_path = gs.path.data / 'kazarinov' / 'prompts'
    system_instruction_path = base_path / 'chat_system_instruction.txt'
    system_instruction: str = read_text_file(system_instruction_path)


    k = Kazarinov(system_instruction = system_instruction, generation_config={"response_mime_type": "text/plain"})
    #adverstisement_strings_list:list = recursive_read_text_files(gs.path.data / 'kazarinov' / 'campaigns', ['description.txt'])
    adverstisement_strings_list:list = recursive_read_text_files(gs.path.data / 'kazarinov' /  'prompts', ['*.txt','*.md'])
    response = k.ask(adverstisement_strings_list)
    print(response)
    ...

def assistant_reminder():
    """Processes reminders in batches and sends them to the Kazarinov assistant."""
    ...
    base_path = gs.path.data / 'kazarinov' / 'prompts'
    system_instruction_path = base_path / 'system_instruction.txt'
    system_instruction: str = read_text_file(system_instruction_path)

    k = Kazarinov(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})

    # Read reminders strings list from .txt and .md files
    reminders_strings_list: list = recursive_read_text_files(gs.path.data / 'AI', ['*.txt', '*.md'])
    logger.info(f"{len(reminders_strings_list)=}")

    # Send reminders in batches of 100
    batch_size = 20
    # for i in range(0, len(reminders_strings_list), batch_size):
    #     batch = reminders_strings_list[i:i + batch_size]  # Get the current batch
    #     print(batch)
    #     response = k.ask(q=batch, system_instruction=system_instruction)
    #     logger.info(f"{batch=} sended")

    # # Read reminders strings list from all file types
    # reminders_strings_list: list = recursive_read_text_files(gs.path.data / 'AI', ['*.*'])
    # logger.info(f"{len(reminders_strings_list)=}")

    # Send reminders in batches of ...
    for i in range(0, len(reminders_strings_list), batch_size):
        batch = reminders_strings_list[i:i + batch_size]  # Get the current batch
        print(batch)
        response = k.ask(q=batch, system_instruction=system_instruction)
        logger.info(f"{batch=} sended")

    #print(response)

def chat():
    """ Чат с gemini """
    ...

    base_path = gs.path.data / 'kazarinov' / 'prompts'
    system_instruction_path = base_path / 'chat_system_instruction.txt'
    system_instruction: str = read_text_file(system_instruction_path)

    print("Чтобы завершить чат, напишите 'exit'.\n")
    
    # Инициализация модели с системной инструкцией, если нужно
    #system_instruction = input("Введите системную инструкцию (или нажмите Enter, чтобы пропустить): @TODO: - сделать возможность чтения из .txt")
    logger.debug("Привет, я ИИ ассистент компьюрного мастера Сергея Казаринова. Задавайте вопросы", None, False)
    ...
    ai = Kazarinov(system_instruction  = system_instruction, generation_config = {'response_mime_type': 'text/plain'})

    while True:
        # Получаем вопрос от пользователя
        #user_input = input(">>>> ")
        user_input = input_colored(">>>> ", GREEN)
        if user_input.lower() == 'exit':
            print("Чат завершен.")
            break
        
        # Отправляем запрос модели и получаем ответ
        response = ai.ask(q = user_input, system_instruction=system_instruction)
        
        # Выводим ответ
        logger.warning(response, None, False)

# ANSI escape codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def input_colored(prompt: str, color: str) -> str:
    """Prompts the user for input with colored text."""
    return input(f"{color}{prompt}{RESET}")

# # Пример использования
# user_input = input_colored(">>>> ", GREEN)
# print(f"Вы ввели: {user_input}")

if __name__ == "__main__":
    #start_trainig()
    assistant_reminder()
    #upload_strings()
    chat()

