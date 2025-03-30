## Анализ кода модуля `gpt_traigner`

**Качество кода:**
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Четкая структура классов и функций.
    - Использование аннотаций типов.
    - Логирование ошибок.
- **Минусы**:
    - Не везде есть документация к функциям и классам.
    - Используются двойные кавычки вместо одинарных в некоторых местах.
    - Отсутствует обработка исключений при работе с файлами.
    - Не все переменные аннотированы типами.
    - Дублирование платформ в комментариях.
    - Не используется `j_loads` для загрузки `chat.json`.

**Рекомендации по улучшению:**

1.  **Форматирование и стиль кода**:
    *   Заменить двойные кавычки на одинарные во всем коде.
    *   Добавить пробелы вокруг операторов присваивания: `x = 5` вместо `x=5`.

2.  **Документация**:
    *   Добавить документацию ко всем классам и методам, используя формат, указанный в инструкции.
    *   Удалить дублирующуюся информацию в комментариях (например, повторяющиеся строки о платформах).
    *   Комментарии должны быть более конкретными и описывать, что именно делает код, а не просто повторять его.

3.  **Использование `j_loads`**:
    *   Использовать `j_loads` для загрузки `chat.json` вместо стандартного `open` и `json.load`.

4.  **Обработка исключений**:
    *   Добавить обработку исключений при работе с файлами, чтобы избежать неожиданных сбоев.

5.  **Аннотации типов**:
    *   Добавить аннотации типов для всех переменных, где это возможно.

6.  **Логирование**:
    *   Убедиться, что все ошибки логируются с использованием `logger.error` и включают `exc_info=True` для вывода traceback.

7.  **Улучшение комментариев**:
    *   Избегать общих фраз вроде "Get the HTML content". Вместо этого писать конкретно, что извлекается и для чего.
    *   Удалить `# <- counter`.
    *   Удалить `#! .pyenv/bin/python3`.

**Оптимизированный код:**

```python
## \file /src/suppliers/chat_gpt/gpt_traigner.py
# -*- coding: utf-8 -*-

"""
Модуль для работы с GPT тренером
=================================================

Модуль содержит класс :class:`GPT_Traigner`, который используется для ...

Пример использования
----------------------

>>> trainer = GPT_Traigner()
>>> trainer.dump_downloaded_conversations()
"""

import re
import argparse
import asyncio
from pathlib import Path
from itertools import zip_longest
from typing import Optional

import pandas as pd
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

locator = j_loads(gs.path.src / 'suppliers' / 'chat_gpt' / 'locators' / 'chat.json')


class GPT_Traigner:
    """
    Класс для обучения GPT моделей на основе скачанных данных.
    """
    driver = Driver(Chrome)

    def __init__(self) -> None:
        """
        Инициализирует экземпляр класса GPT_Traigner.
        """
        self.gs = GptGs()

    def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: Optional[str] = 'positive') -> str:
        """
        Определяет метку настроения для пары реплик в диалоге.

        Args:
            conversation_pair (dict[str, str]): Пара реплик (пользователь, ассистент).
            sentiment (str, optional): Предопределенное настроение. По умолчанию 'positive'.

        Returns:
            str: Метка настроения ('positive' или 'negative').
        """
        if sentiment:
            return 'positive'
        else:
            return 'negative'

    def save_conversations_to_jsonl(self, data: list[dict], output_file: str) -> None:
        """
        Сохраняет список диалогов в формате JSONL файл.

        Args:
            data (list[dict]): Список диалогов, где каждый диалог представлен словарем.
            output_file (str): Путь к файлу для сохранения данных.
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in data:
                    f.write(j_dumps(clean_string(item)) + '\n')
        except Exception as ex:
            logger.error(f'Error while saving conversations to {output_file}', ex, exc_info=True)

    def dump_downloaded_conversations(self) -> None:
        """
        Извлекает диалоги из HTML-файлов, сохраняет их в CSV и JSONL файлы.
        """
        conversation_directory = Path(gs.path.google_drive / 'chat_gpt' / 'conversation')
        html_files = conversation_directory.glob('*.html')

        all_data = []
        counter: int = 0

        for local_file_path in html_files:
            # Get the HTML content
            file_uri = local_file_path.resolve().as_uri()
            self.driver.get_url(file_uri)

            user_elements = self.driver.execute_locator(locator['user'])
            assistant_elements = self.driver.execute_locator(locator['assistant'])

            user_content = [element.text for element in user_elements] if isinstance(user_elements, list) else [user_elements.text] if user_elements else None
            assistant_content = [element.text for element in assistant_elements] if isinstance(assistant_elements, list) else [assistant_elements.text] if assistant_elements else None

            if not user_content and not assistant_content:
                logger.error(f'Данные отсутствуют в файле: {local_file_path}')
                continue

            for user_text, assistant_text in zip_longest(user_content, assistant_content):
                if user_text and assistant_text:
                    data = {
                        'role': ['user', 'assistant'],
                        'content': [clean_string(user_text), clean_string(assistant_text)],
                        'sentiment': ['neutral', 'neutral']
                    }
                    all_data.append(pd.DataFrame(data))
                    print(f'{counter} - {local_file_path}')
                    counter += 1

        if all_data:
            all_data_df = pd.concat(all_data, ignore_index=True)

            # Save all accumulated results to a single CSV file
            csv_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
            try:
                all_data_df.to_csv(csv_file_path, index=False, encoding='utf-8')
            except Exception as ex:
                logger.error(f'Error while saving data to CSV file: {csv_file_path}', ex, exc_info=True)

            # Save all accumulated results to a single JSONL file
            jsonl_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
            try:
                all_data_df.to_json(jsonl_file_path, orient='records', lines=True, force_ascii=False)
            except Exception as ex:
                logger.error(f'Error while saving data to JSONL file: {jsonl_file_path}', ex, exc_info=True)

            # Save raw conversations to a single line without formatting
            raw_conversations = ' '.join(all_data_df['content'].dropna().tolist())
            raw_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
            try:
                with open(raw_file_path, 'w', encoding='utf-8') as raw_file:
                    raw_file.write(raw_conversations)
            except Exception as ex:
                logger.error(f'Error while saving raw conversations to file: {raw_file_path}', ex, exc_info=True)


traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()
model = Model()
model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))