## \file ../src/ai/gemini/kazarinov_train.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Module that handles model training for Aliexpress using GoogleGenerativeAI with logging of the dialog into JSON files """

from math import log
from optparse import Option
import header
import time
import json
import random
from pathlib import Path
from typing import Optional
from src import gs
from src.ai import OpenAIModel, GoogleGenerativeAI
from src.utils.file import get_filenames, recursive_get_filenames, read_text_file, recursive_read_text_files, save_text_file
from src.utils.jjson import j_loads, j_dumps
from src.utils import pprint
from src.logger import logger

# Base paths for system instructions and training files
base_path = gs.path.data / 'kazarinov' / 'prompts' 
system_instruction_path = base_path / 'system_instruction.txt'
questions_file_path = base_path / 'model' / 'generated_questions'
system_instruction: str = read_text_file(system_instruction_path)

# Retrieve filenames for training data
train_files = get_filenames(base_path / 'questions_answers')
if not train_files:
    logger.error(f"Нет файлов тренировок")
    ...


class Kazarinov:
    """"""
    ...
    gemini_1 = GoogleGenerativeAI(api_key = gs.credentials.gemini.kazarinov, 
                                  system_instruction=system_instruction, 
                                  generation_config={"response_mime_type": "text/plain"})

    gemini_2 = GoogleGenerativeAI(api_key = gs.credentials.gemini.kazarinov,
                                  system_instruction=system_instruction, 
                                  generation_config={"response_mime_type": "text/plain"})
    timestamp = gs.now

    def __init__(self):
        """"""
        ...

    def train(self, train_dir:Optional[Path | str] = None, train_files:Optional[list | str] = None, system_instructions: Optional[str] = None):
        """"""
        ...
        if train_dir:
            train_data_list:list = recursive_read_text_files(train_dir,['*.*'])

        if train_files:
            # train_files = train_files if isinstance(train_files, list) else [train_files]
            # train_files += _train_data_list
            ...
        else:
            train_data = train_data_list


        random.shuffle(train_data_list)
        response:str = None
        for train_data in train_data_list:
            # First response from Gemini 1

            assistant = 'assistant asst_w5cM3yqOX1pDJARO2hzNMVZr '
            response = self.gemini_1.ask(q = assistant + response if response else assistant, 
                                         system_instruction = f"""
                                        assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                                        Prompt: Задай вопрос ассистенту на IT тему 
                                        Не давай ответ. Только задай вопрос
                                        """)
            #response_1 = self.gemini_1.ask(prompt, "assistant asst_w5cM3yqOX1pDJARO2hzNMVZr")
            logger.info(f"Q > : {response}")
            save_text_file(response, self.questions_file_path / f'{self.timestamp}.txt', mode = 'a' )
            
            # Second response from Gemini 2 based on Gemini 1's response
            response = self.gemini_2.ask(q = assistant + response if response else assistant,  
                                         system_instruction = fr"""
                                        assistant asst_w5cM3yqOX1pDJARO2hzNMVZr. 
                                        дай ответ на вопрос.
                                        В конце ответа добавь: `Рад вам помочь! Мастер по ремонту компьютеров Сергей Казаринов. тел: 054-422-94-97
                                        .mode=--plain_text""")
            logger.debug(f"A > : {response}", None, False)
            time.sleep(10)
            


            # # Prepare data for saving to JSON
            # dialog_data = {
            #     "file": train_file,
            #     "prompt": prompt,
            #     "response_1": response_1,
            #     "response_2": response_2
            # }

            # j_dumps(Path(base_path / 'train' / f'{self.timestamp}_dialog.json'))

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

    def ask(self, prompt, system_instruction: Optional[str]):
        return self.gemini_1.ask(prompt,system_instruction)  

    

    def assistant_reminder(self):
        """Processes reminders in batches and sends them to the Kazarinov assistant."""
        ...

        # # Read reminders strings list from .txt and .md files
        # reminders_strings_list: list = recursive_read_text_files(gs.path.data / 'AI', ['*.txt', '*.md'])
        # logger.info(f"{len(reminders_strings_list)=}")

        # # Send reminders in batches of 100
        # batch_size = 1
        # for i in range(0, len(reminders_strings_list), batch_size):
        #     batch = reminders_strings_list[i:i + batch_size]  # Get the current batch
        #     print(batch)
        #     response = k.ask(q=batch, system_instruction=system_instruction)
        #     logger.info(f"{batch=} sended")

        # Read reminders strings list from all file types
        reminders_strings_list: list = recursive_read_text_files(base_path / 'campaigns' , ['*.txt'] )
        if not reminders_strings_list:
            return
    
        logger.info(f"{len(reminders_strings_list)=}")
        #Send reminders in batches of ...
        batch_size = 1
        for i in range(0, len(reminders_strings_list), batch_size):
        
            batch = reminders_strings_list[i:i + batch_size]  # Get the current batch
            print(batch)
            response = k.ask(q=batch, no_log=True)
            logger.info(f"{batch=} sended")

        #print(response)




    def upload_strings(sekf):
        """ Беру информацию из файлов рекламых сообщений
        для дообучения модели рекламе """
        ...

        strings_list:list = recursive_read_text_files(base_path / 'campaigns', ['description.txt'])
        if not  strings_list:
            ...
        else:
            k = Kazarinov(system_instruction = system_instruction_list[random.randint(0, len(system_instruction_list) - 1)], 
                      generation_config={"response_mime_type": "text/plain"})
            for string in strings_list:
                response = k.ask(string,  no_log = True , with_pretrain = True)
                print(response)

        strings_list:list = recursive_read_text_files(base_path /  'prompts', ['*.txt','*.md'])
        if not  strings_list:
            ...
        else:
            for string in strings_list:
                response = k.ask(string,  no_log=True)
                print(response)
            k = Kazarinov(system_instruction = system_instruction_list[random.randint(0, len(system_instruction_list) - 1)], 
                      generation_config={"response_mime_type": "text/plain"})
            for string in strings_list:
                response = k.ask(string,  no_log=True)
                print(response)




if __name__ == "__main__":
    """"""
    ...
    kazarinov = Kazarinov()
    #kazarinov.train(train_dir = gs.path.data / 'AI', system_instructions = None )
    kazarinov.train(train_dir = gs.path.data / 'kazarinov' / 'prompts', system_instructions = None )
    kazarinov.dialog()