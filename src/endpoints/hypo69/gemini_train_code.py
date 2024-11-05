## \file ..
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" HERE MUST BE DESCRIPTION OF MODULE 
https://stackoverflow.com/questions/78382534/googlegenerativeaierror-error-embedding-contentmodels-embeddings-001-is-not-fo
"""

from pathlib import Path
import time

import header
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import yield_files_content, read_text_file
system_instruction:str = read_text_file(gs.path.src / 'ai' / 'prompts' / 'developer' / 'improve_code.md')     \

model:GoogleGenerativeAI = GoogleGenerativeAI(api_key = gs.credentials.gemini.onela, system_instruction = system_instruction)

def main():

    for content in yield_files_content(gs.path.src ,['*.py','*.txt','*.md','*.json','*.dot']):
        content:str = f"""
            Я предоставлю тебе код на Python, включая его расположение в проекте. Пожалуйста, проанализируй код с учетом этого расположения и дай оценку. Обрати внимание на следующие аспекты:

                1. Правильность и эффективность кода.
                2. Читаемость и стиль кодирования.
                3. Наличие комментариев и документации в формате Sphinx.
                4. Возможные ошибки или области для улучшения.

                Расположение файла в проекте будет указано в начале кода. Вот мой код:

                ```{content}```
                """
        response = model.ask(content)
        print(response)
        time.sleep(20)

if __name__ == 'main':
    print(f"Starting trainig ...")
    main()
