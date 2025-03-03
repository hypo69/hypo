## \file /src/endpoints/hypo69/code_assistant/code_translator.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Модуль переводов кода
=========================================================================================

:class:`CodeAssistant`, читает файлы кода, отдает код в модели, модель обрабатывет код и возвращает его в класс, класс сохраняет результат
в директории `docs/gemini` В зависимости от роли файлы сохраняются в 

Пример использования
--------------------

Пример использования класса `CodeAssistant`:
# задайте роль исполнителя, язык 

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()

.. module:: src.endpoints.hypo69.code_assistant 
    :platform: Windows, Unix
    :synopsis: Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов

.. header.py:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```
"""
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.endpoints.hypo69.code_assistant.code_assistant import CodeAssistant
from src.utils.path import get_relative_path
from src.logger.logger import logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary 

class CodeTranslator(CodeAssistant):
    """Переводчик кода. Наследует CodeAssistant"""

    role:str = 'code_translator'

    def __init__(self, role:str, models:Optional[list] = ['gemini']):
        """"""
        super().__init__(role=self.role)


