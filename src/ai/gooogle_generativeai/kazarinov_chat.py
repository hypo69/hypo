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
from src.utils.file import get_filenames, read_text_file
from src.utils.jjson import j_dumps
from src.logger import logger

# Base paths for system instructions and training files
base_path = gs.path.data / 'kazarinov' / 'prompts'
system_instruction_path = base_path / 'system_instruction.txt'
system_instruction: str = read_text_file(system_instruction_path)

# Retrieve filenames for training data
train_files = get_filenames(base_path / 'questions_answers')
if not train_files:
    logger.error("No training files found.")
    ...

class Kazarinov:
    """Handles model training and dialog generation for the Kazarinov project using GoogleGenerativeAI."""
    
    gemini_1 = GoogleGenerativeAI(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
    gemini_2 = GoogleGenerativeAI(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
    timestamp = gs.now

    def __init__(self):
        """Initialize the Kazarinov model."""
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

    def ask(self, prompt) -> bool:
        """Спрашиваю у машины """
        return self.gemini_1.ask(prompt)



def start_trainig():
    kazarinov = Kazarinov()
    train_files = get_filenames(gs.path.data / 'kazarinov' / 'prompts' / 'questions_answers')
    kazarinov.train(train_files)
    kazarinov.dialog()


def chat():
    logger.debug("Привет, я ИИ ассистент компьюрного мастера Сергея Казаринова. Задавайте вопросы", None, False)
    print("Чтобы завершить чат, напишите 'exit'.\n")
    
    # Инициализация модели с системной инструкцией, если нужно
    system_instruction = input("Введите системную инструкцию (или нажмите Enter, чтобы пропустить): @TODO: - сделать возможность чтения из .txt")
    ...
    ai = Kazarinov()

    while True:
        # Получаем вопрос от пользователя
        user_input = input("> вопрос\n> ")
        
        if user_input.lower() == 'exit':
            print("Чат завершен.")
            break
        
        # Отправляем запрос модели и получаем ответ
        response = ai.ask(prompt=user_input)
        
        # Выводим ответ
        print(f">> ответ\n>> {response}\n")


if __name__ == "__main__":
    #start_trainig()
    chat()

