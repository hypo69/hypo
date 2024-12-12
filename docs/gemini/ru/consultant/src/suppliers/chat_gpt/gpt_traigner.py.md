# Анализ кода модуля `gpt_traigner.py`

**Качество кода**
-  Соответствие требованиям по оформлению кода: 7/10
 -  Плюсы
    - Код структурирован и разделен на классы и функции, что облегчает понимание и поддержку.
    - Используются `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Логирование ошибок с помощью `logger.error`.
    - Использование `j_dumps`, `j_loads`, `j_loads_ns` для работы с JSON, как и требовалось.
    - Присутствует обработка HTML контента для извлечения диалогов.
 -  Минусы
    -  Отсутствуют docstring для класса и методов, что затрудняет понимание их назначения и использования.
    -  Не все комментарии соответствуют формату RST.
    -  Используется `pd.DataFrame`, хотя требовалось сохранение в JSONL без pandas.
    -  Некоторые части кода, такие как `...`, остались не обработанными.
    -  Не хватает обработки ошибок при открытии и чтении файлов.
    -  Не все переменные имеют snake_case стиль.
    -  Смешение логики сбора данных и сохранения их в файлы.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstring к классу `GPT_Traigner` и всем его методам в формате RST.
    -   Переписать все комментарии в стиле RST, включая описание параметров и возвращаемых значений.
    -   Добавить описание модуля в начале файла в формате RST.

2.  **Обработка данных:**
    -  Исключить использование `pd.DataFrame` и `pd.concat` при формировании JSONL файлов, как указано в задании.
    -  Реализовать сохранение данных в JSONL файл с использованием `j_dumps` и добавлением новой строки (`\n`).
    -  Обеспечить корректное формирование JSONL файла без использования `orient='records'`.
    -  Удалить избыточное сохранение в `all_conversations.csv`.
    -  Разделить логику сбора данных и сохранения в файл.
    
3.  **Логирование и обработка ошибок:**
    -  Добавить обработку ошибок при работе с файлами, например, с помощью `try-except` и `logger.error`.
    -  Использовать `logger.debug` для отладочной информации.

4.  **Структура кода:**
    -   Избавиться от `...` заменив их на соответствующий код.
    -  Использовать snake_case стиль для имен переменных.
    -  Сделать код более модульным, разделив его на более мелкие функции.
    
5.  **Улучшения:**
    -   Пересмотреть использование `zip_longest` и удостовериться, что данные правильно обрабатываются, когда количество элементов в разных списках не совпадает.
    -   Избегать прямого конкатенирования строк, а использовать форматирование строк `f""`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для обучения модели GPT на основе диалогов.
=========================================================================================

Этот модуль содержит класс :class:`GPT_Traigner`, который используется для сбора и обработки данных
из HTML файлов для обучения моделей ИИ, таких как GPT.
Модуль также отвечает за сохранение обработанных данных в форматах JSONL и TXT.

Пример использования
--------------------

Пример использования класса `GPT_Traigner`:

.. code-block:: python

    traigner = GPT_Traigner()
    traigner.dump_downloaded_conversations()
"""

import re
import argparse
import asyncio
from pathlib import Path
from itertools import zip_longest
# import pandas as pd # Удален pandas, как указано в инструкции
from aioconsole import ainput

import header
from src import gs
from src.logger.logger import logger
from src.suppliers.chat_gpt import GptGs
from src.webdriver.driver import Driver, Chrome, Firefox, Edge
from src.ai.openai.model import Model
from src.utils.jjson import j_dumps, j_loads, j_loads_ns, clean_string
from src.utils.convertors import dict2csv, json2csv
from src.utils.printer import pprint

#: Загрузка локаторов из JSON файла.
locator = j_loads_ns(gs.path.src / 'suppliers' / 'chat_gpt' / 'locators' / 'chat.json')


class GPT_Traigner:
    """
    Класс для сбора и обработки диалогов из HTML файлов для обучения моделей GPT.

    :ivar driver: Экземпляр веб-драйвера для навигации и взаимодействия с веб-страницами.
    :vartype driver: src.webdriver.driver.Driver
    :ivar gs: Экземпляр класса GptGs для доступа к глобальным настройкам.
    :vartype gs: src.suppliers.chat_gpt.GptGs
    """
    driver = Driver(Chrome)
    
    def __init__(self):
        """
        Инициализация экземпляра класса `GPT_Traigner`.
        
        Инициализирует объект :class:`GptGs` для доступа к настройкам.
        """
        self.gs = GptGs()

    def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = 'positive') -> str:
        """
        Определяет метку настроения для пары диалога.

        :param conversation_pair: Пара диалога (словарь с ключами 'user' и 'assistant').
        :type conversation_pair: dict[str, str]
        :param sentiment: Метка настроения (по умолчанию 'positive').
        :type sentiment: str
        :return: Метка настроения ('positive' или 'negative').
        :rtype: str
        """
        if sentiment:
            return 'positive'
        else:
            return 'negative'

    def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
        """
        Сохраняет список пар диалогов в формате JSONL.

        :param data: Список словарей, представляющих пары диалогов.
        :type data: list[dict]
        :param output_file: Путь к файлу для сохранения данных.
        :type output_file: str
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in data:
                    f.write(j_dumps(clean_string(item)) + '\n')
        except Exception as ex:
            logger.error(f'Ошибка при сохранении в JSONL файл: {output_file}', ex)
    
    def _extract_conversation_data(self, local_file_path: Path) -> list[dict] | None:
        """
        Извлекает данные диалогов из HTML-файла.

        :param local_file_path: Путь к HTML-файлу.
        :type local_file_path: pathlib.Path
        :return: Список словарей, представляющих пары диалогов, или None, если данные не найдены.
        :rtype: list[dict] | None
        """
        try:
            file_uri = local_file_path.resolve().as_uri()
            self.driver.get_url(file_uri)
            
            user_elements = self.driver.execute_locator(locator.user)
            assistant_elements = self.driver.execute_locator(locator.assistant)
            
            user_content = [element.text for element in user_elements] if isinstance(user_elements, list) else [user_elements.text] if user_elements  else None
            assistant_content = [element.text for element in assistant_elements] if isinstance(assistant_elements, list) else [assistant_elements.text] if assistant_elements  else None

            if not user_content and not assistant_content:
                logger.error(f"Данные не найдены в файле: {local_file_path}")
                return None

            conversations = []
            for user_text, assistant_text in zip_longest(user_content, assistant_content, fillvalue=''):
                if user_text and assistant_text:
                    data = {
                        'role': ['user', 'assistant'],
                        'content': [clean_string(user_text), clean_string(assistant_text)],
                        'sentiment': ['neutral', 'neutral']
                    }
                    conversations.append(data)
            return conversations
        except Exception as ex:
            logger.error(f"Ошибка при обработке файла {local_file_path}: {ex}")
            return None

    def dump_downloaded_conversations(self):
        """
        Собирает диалоги из HTML-файлов и сохраняет их в JSONL и TXT форматы.

        Обходит все HTML файлы в указанной директории, извлекает из них диалоги
        и сохраняет в файлы `all_conversations.jsonl` и `raw_conversations.txt`.
        """
        conversation_directory = Path(gs.path.google_drive / 'chat_gpt' / 'conversation')
        html_files = conversation_directory.glob('*.html')
        
        all_data = []
        counter = 0

        for local_file_path in html_files:
            conversations = self._extract_conversation_data(local_file_path)
            if conversations:
                all_data.extend(conversations)
                counter += len(conversations)
                logger.debug(f'{counter} - {local_file_path}')
        
        if all_data:
            jsonl_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
            self.save_conversations_to_jsonl(all_data, jsonl_file_path)

            raw_conversations = ' '.join(
                [content for conv in all_data for content in conv.get('content', []) if content]
            )
            raw_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
            try:
                with open(raw_file_path, 'w', encoding='utf-8') as raw_file:
                    raw_file.write(raw_conversations)
            except Exception as ex:
                logger.error(f"Ошибка при сохранении raw conversations в файл: {raw_file_path}", ex)
        
        
traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()

model = Model()
model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'))
```