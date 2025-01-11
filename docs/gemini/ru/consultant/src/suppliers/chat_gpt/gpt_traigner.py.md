# Анализ кода модуля gpt_traigner

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разделен на функции.
    - Используются асинхронные операции, что хорошо для производительности.
    - Присутствует логирование ошибок, что облегчает отладку.
    - Используются `j_loads_ns` и `j_dumps` для работы с JSON, что соответствует требованиям.
-  Минусы
    -  Неполная документация: отсутствуют docstring для модуля и класса.
    -  Отсутствует обработка ошибок в некоторых местах, например, при чтении HTML файлов.
    -  Не используются константы для значений по умолчанию.
    -  Множественные импорты из одного модуля.
    -  Смешивание кода с запуском в конце файла.
    -  Не все комментарии понятны и объясняют назначение кода.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля и класса, а также для всех функций и методов.
2.  Использовать константы для значений по умолчанию, например, для `sentiment = 'positive'`.
3.  Обработать ошибки при чтении HTML файлов.
4.  Упростить импорты из `src`, сгруппировав их по смыслу.
5.  Вынести код запуска в функцию `main` или в блок `if __name__ == '__main__':`.
6.  Добавить комментарии в формате RST для функций и методов.
7.  Использовать более конкретные формулировки в комментариях.
8.  Избегать использования `...` в коде, заменяя их на логику или комментарии.
9.  Избавиться от ненужных блоков `"""` в начале файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для обучения модели GPT на основе данных из чатов
=========================================================================================

Этот модуль содержит класс :class:`GPT_Traigner`, который используется для сбора и обработки данных
из HTML файлов, содержащих диалоги из ChatGPT, для последующего обучения моделей ИИ.

Пример использования
--------------------

Пример использования класса `GPT_Traigner`::

    traigner = GPT_Traigner()
    traigner.dump_downloaded_conversations()
    model = Model()
    model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))
"""
import re
import argparse
import asyncio
from pathlib import Path
from itertools import zip_longest

import pandas as pd
from aioconsole import ainput

import header
from src import gs
from src.logger.logger import logger
from src.suppliers.chat_gpt import GptGs
from src.webdriver.driver import Driver, Chrome
from src.ai.openai.model import Model
from src.utils.jjson import j_dumps, j_loads, j_loads_ns, clean_string
from src.utils.convertors import dict2csv, json2csv
from src.utils.printer import pprint

locator = j_loads_ns(gs.path.src / 'suppliers' / 'chat_gpt' / 'locators' / 'chat.json')
DEFAULT_SENTIMENT = 'positive'


class GPT_Traigner:
    """
    Класс для сбора и обработки данных из чатов GPT.

    Этот класс предоставляет методы для извлечения диалогов из HTML-файлов,
    определения их тональности и сохранения в различных форматах.
    """

    driver = Driver(Chrome)

    def __init__(self):
        """Инициализирует класс GPT_Traigner."""
        self.gs = GptGs()

    def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = DEFAULT_SENTIMENT) -> str:
        """
        Определяет тональность диалога.

        Args:
            conversation_pair (dict[str, str]): Пара диалога.
            sentiment (str, optional): Заданная тональность. Defaults to 'positive'.

        Returns:
            str: Тональность.

        """
        if sentiment:
            return "positive"
        else:
            return "negative"

    def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
        """
        Сохраняет диалоги в формате JSONL.

        Args:
            data (list[dict]): Список диалогов.
            output_file (str): Путь к файлу.
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(j_dumps(clean_string(item)) + "\n")

    def dump_downloaded_conversations(self):
        """
        Извлекает диалоги из HTML-файлов и сохраняет их в CSV, JSONL и TXT форматы.

        Этот метод ищет HTML-файлы в директории, извлекает из них диалоги
        между пользователем и ассистентом, и сохраняет результаты в CSV, JSONL
        и TXT файлах.
        """
        conversation_directory = Path(gs.path.google_drive / 'chat_gpt' / 'conversation')
        html_files = conversation_directory.glob("*.html")

        all_data = []
        counter: int = 0

        for local_file_path in html_files:
            try:
                # Получение HTML контента
                file_uri = local_file_path.resolve().as_uri()
                self.driver.get_url(file_uri)

                user_elements = self.driver.execute_locator(locator.user)
                assistant_elements = self.driver.execute_locator(locator.assistant)

                # Извлечение текста из элементов пользователя и ассистента
                user_content = [element.text for element in user_elements] if isinstance(user_elements, list) else [user_elements.text] if user_elements else None
                assistant_content = [element.text for element in assistant_elements] if isinstance(assistant_elements, list) else [assistant_elements.text] if assistant_elements else None

                if not user_content and not assistant_content:
                    logger.error(f"Не найдены данные в файле: {local_file_path}")
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
            except Exception as e:
                logger.error(f"Ошибка при обработке файла {local_file_path}: {e}")
                continue
        if all_data:
            all_data_df = pd.concat(all_data, ignore_index=True)

            # Сохранение всех накопленных результатов в один CSV файл
            csv_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
            all_data_df.to_csv(csv_file_path, index=False, encoding='utf-8')

            # Сохранение всех накопленных результатов в один JSONL файл
            jsonl_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
            all_data_df.to_json(jsonl_file_path, orient='records', lines=True, force_ascii=False)

            # Сохранение сырых диалогов в одну строку без форматирования
            raw_conversations = ' '.join(all_data_df['content'].dropna().tolist())
            raw_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
            with open(raw_file_path, 'w', encoding='utf-8') as raw_file:
                raw_file.write(raw_conversations)


def main():
    """Основная функция для запуска обучения модели."""
    traigner = GPT_Traigner()
    traigner.dump_downloaded_conversations()
    model = Model()
    model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))

if __name__ == '__main__':
    main()