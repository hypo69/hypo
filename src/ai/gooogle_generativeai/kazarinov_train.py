## \file ../src/ai/openai/model/_experiments/kazarinov.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Module that handles model training for Aliexpress using GoogleGenerativeAI with logging of the dialog into JSON files """

from math import log
import header
import time
import json
import random
from pathlib import Path
from src import gs
from src.ai import OpenAIModel, GoogleGenerativeAI
from src.utils.file import get_filenames, recursive_get_filenames, read_text_file
from src.utils.jjson import j_loads, j_dumps
from src.utils import pprint
from src.logger import logger

# Base paths for system instructions and training files
base_path = gs.path.data / 'kazarinov' / 'prompts' 
system_instruction_path = base_path / 'system_instruction.txt'
system_instruction: str = read_text_file(system_instruction_path)

# Retrieve filenames for training data
train_files = get_filenames(base_path / 'questions_answers')
if not train_files:
    logger.error(f"Нет файлов тренировок")
    ...


class Kazarinov:
    """"""
    ...
    gemini_1 = GoogleGenerativeAI(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
    gemini_2 = GoogleGenerativeAI(system_instruction=system_instruction, generation_config={"response_mime_type": "text/plain"})
    timestamp = gs.now

    def __init__(self):
        """"""
        ...

    def train(self, train_files:list | str):
        """"""
        ...
        train_files = train_files if isinstance(train_files, list) else [train_files]
        random.shuffle(train_files)

        for train_file in train_files:
            # Wait before processing the next file

            prompt = read_text_file(base_path / 'questions_answers' / train_file)

            # Log the initial prompt before the first response
            #logger.info(f"Training File: {train_file}")

            # First response from Gemini 1
            response_1 = self.gemini_1.ask(prompt, f"""
                assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                Prompt: Не давай развернутый ответ. Только Задай вопрос ассистенту на IT тему в одну строку
                Не давай ответ. |Только задай вопрос
                """)
            #response_1 = self.gemini_1.ask(prompt, "assistant asst_w5cM3yqOX1pDJARO2hzNMVZr")
            logger.info(f"Gemini 1 Response: {response_1}")

            # Second response from Gemini 2 based on Gemini 1's response
            response_2 = self.gemini_2.ask(response_1, fr"""
                                        assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                                        дай ответ на вопрос. 
                                         должан быть строка 
                                        `<a href='https://wa.me/97254422'> Whatsapp </a>  <a href="mailto:sergey@mymaster.co.il">или почта</a>`
                                        .""")
            logger.debug(f"Gemini 2 Response: {response_2}", None, False)
            answer = response_2


            # Prepare data for saving to JSON
            dialog_data = {
                "file": train_file,
                "prompt": prompt,
                "response_1": response_1,
                "response_2": response_2
            }

            j_dumps(Path(base_path / 'train' / f'{self.timestamp}_dialog.json'))

    def question_answer(self, train_files:list | str):
        """"""
        ...
        train_files = train_files if isinstance(train_files, list) else [train_files]

        for train_file in train_files:
            # Wait before processing the next file
            logger.warning(f" ------ лимит :( ")
            questions = read_text_file(base_path / 'q'/ train_file, as_list = True)
            for q in questions:
                ...

    def dialog(self):
        """"""
        ...
        base_path: Path = gs.path.data / 'kazarinov' / 'prompts' / 'q'  

        questions:list = read_text_file(base_path / 'ru.md'  , as_list = True)  + read_text_file(base_path / 'he.md'  , as_list = True) + \
            read_text_file(base_path / 'ru2.md'  , as_list = True)  + read_text_file(base_path / 'he2.md'  , as_list = True)  + \
            read_text_file(base_path / 'en1.md'  , as_list = True)  + read_text_file(base_path / 'en2.md'  , as_list = True)

        random.shuffle(questions)
        for q in questions:
            logger.info(q)
            response_1 = self.gemini_1.ask(q, system_instruction = f"""
                    assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                    Prompt:```at the end of each answer you add a line: '<a href='https://wa.me/972544229497'> Whatsapp </a>  <a href="mailto:sergey@mymaster.co.il">или почта</a>`' ```""")
            logger.debug(response_1, None, False)

    def ask(self, prompt):
        return self.gemini_1.ask(prompt)



if __name__ == "__main__":
    """"""
    ...
    kazarinov = Kazarinov()
    train_files = get_filenames(gs.path.data / 'kazarinov' / 'prompts' / 'questions_answers')
    kazarinov.train(train_files)
    kazarinov.dialog()