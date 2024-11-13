## \file hypotez/src/endpoints/hypo69/onela_bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.hypo69 """

""" Отсылатель кода в модель gemini
https://stackoverflow.com/questions/78382534/googlegenerativeaierror-error-embedding-contentmodels-embeddings-001-is-not-fo
"""
...
from pathlib import Path
import time

import header
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import yield_files_content, read_text_file

system_instruction:str = read_text_file(gs.path.src / 'ai' / 'prompts' / 'developer' / 'improve_code.md') 
generation_config: dict = {"response_mime_type": "text/plain"}
model_name: str = "gemini-1.5-flash-8b"
model:GoogleGenerativeAI = GoogleGenerativeAI(api_key = gs.credentials.gemini.onela, 
                                              model_name = model_name,
                                              system_instruction = system_instruction,
                                              generation_config = generation_config,
                                              )

def main():
    """"""
    ...
    global model
    for file_path, content in yield_files_content(gs.path.src ,['*.py','*.txt','*.md','*.json','*.dot']):
        content:str = f"""
            Я предоставлю тебе код на Python, включая его расположение в проекте. Проанализируй код с учетом этого расположения и дай оценку. Обрати внимание на следующие аспекты:
** Запоминай каждый полученный файл **
** Собери общую логику из файлов, которые я тебе передаю.**
** Проверь код на:  **
- Правильность и эффективность кода.
- Читаемость и стиль кодирования.
- Наличие комментариев и документации в формате Sphinx.
- Возможные ошибки или области для улучшения.
** Если есть возможность расставить комментарии без нарушения работы логики - расставь комментарии в формате Sphinx **
** Верни исправленный код **

Расположение файла в проекте: `{file_path}`. 
Вот мой код:

```{content}```
                """
        response = model.ask(content)
        print(response)
        time.sleep(20)

if __name__ == '__main__':
    print(f"Starting trainig ...")
    main()
