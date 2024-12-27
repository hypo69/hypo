# Анализ кода модуля `gpt_traigner.py`

**Качество кода**
8
-  Плюсы
    - Код структурирован в классе `GPT_Traigner`, что способствует логической организации функциональности.
    - Используются `logger` для логирования ошибок и отладки.
    - Применяются `j_dumps` и `j_loads_ns` для обработки JSON, что соответствует требованиям.
    - Код читаемый с использованием осмысленных имен переменных.
    - Применяется `pathlib.Path` для работы с путями, что является хорошей практикой.

-  Минусы
    - Отсутствуют docstring для класса и методов.
    - Есть неиспользуемые импорты `re` и `argparse`.
    - Комментарии в начале файла не соответствуют RST стандарту.
    - Есть лишние пустые строки.
    - Не все переменные используются, что может привести к путанице.
    - Отсутствует обработка ошибок в некоторых частях кода, например, при чтении файлов.
    - Код не следует стандарту PEP8.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring для класса `GPT_Traigner` и всех его методов с использованием RST.
2.  **Импорты**: Убрать неиспользуемые импорты `re`, `argparse`.
3.  **Комментарии**: Привести комментарии в начале файла в соответствие с RST.
4.  **Обработка ошибок**: Добавить обработку ошибок при чтении файлов и при вызове `execute_locator`.
5.  **Форматирование**: Следовать стандарту PEP8.
6.  **Логирование**: Использовать `logger.debug` для отладочной информации, `logger.info` для важных сообщений и `logger.error` для ошибок.
7.  **Переменные**: Удалить неиспользуемые переменные.
8.  **Стиль кода**: Сделать код более консистентным и читаемым.
9.  **Использовать `j_loads`**: В коде не используются функции `j_loads`. Рассмотреть использование этой функции, если необходимо.
10. **Типизация**: Добавить аннотации типов для функций и переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для обучения моделей GPT на основе данных диалогов.
===========================================================

Этот модуль содержит класс :class:`GPT_Traigner`, который используется для сбора,
обработки и сохранения диалогов, полученных из HTML-файлов.
Диалоги могут быть сохранены в формате CSV, JSONL и TXT.

Пример использования
--------------------

.. code-block:: python

    traigner = GPT_Traigner()
    traigner.dump_downloaded_conversations()
    model = Model()
    model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))
"""

import asyncio
from pathlib import Path
from itertools import zip_longest
from typing import List, Dict, Any

import pandas as pd
from aioconsole import ainput

import header  # FIXME:  Непонятно зачем, можно удалить
from src import gs
from src.logger.logger import logger
from src.suppliers.chat_gpt import GptGs
from src.webdriver.driver import Driver, Chrome
from src.ai.openai.model import Model
from src.utils.jjson import j_dumps, j_loads_ns, clean_string
from src.utils.printer import pprint


locator = j_loads_ns(gs.path.src / 'suppliers' / 'chat_gpt' / 'locators' / 'chat.json')


class GPT_Traigner:
    """
    Класс для сбора и обработки диалогов с веб-страниц.

    :ivar driver: Драйвер для управления браузером.
    :vartype driver: src.webdriver.driver.Driver
    :ivar gs: Объект для доступа к глобальным настройкам.
    :vartype gs: src.suppliers.chat_gpt.GptGs
    """
    driver = Driver(Chrome)
    
    def __init__(self) -> None:
        """Инициализирует экземпляр класса GPT_Traigner."""
        self.gs = GptGs()

    def determine_sentiment(self, conversation_pair: Dict[str, str], sentiment: str = 'positive') -> str:
        """
        Определяет тональность диалога (всегда возвращает 'positive').
        
        :param conversation_pair: Пара диалога.
        :type conversation_pair: Dict[str, str]
        :param sentiment: Тональность (по умолчанию 'positive').
        :type sentiment: str
        :return: Всегда возвращает 'positive'.
        :rtype: str
        """
        if sentiment:
            return "positive"
        else:
            return "negative"

    def save_conversations_to_jsonl(self, data: List[Dict], output_file: str) -> None:
        """
        Сохраняет диалоги в файл JSONL.

        :param data: Список словарей с данными диалогов.
        :type data: List[Dict]
        :param output_file: Путь к файлу для сохранения.
        :type output_file: str
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in data:
                    f.write(j_dumps(clean_string(item)) + "\\n")
        except Exception as ex:
            logger.error(f"Ошибка сохранения в JSONL файл: {output_file}", exc_info=ex)
            ...

    def dump_downloaded_conversations(self) -> None:
        """
        Извлекает диалоги из HTML-файлов, сохраняет в CSV, JSONL и TXT файлы.
        """
        conversation_directory = Path(gs.path.google_drive / 'chat_gpt' / 'conversation')
        html_files = conversation_directory.glob("*.html")

        all_data = []
        counter: int = 0

        for local_file_path in html_files:
            try:
                file_uri = local_file_path.resolve().as_uri()
                self.driver.get_url(file_uri)

                user_elements = self.driver.execute_locator(locator.user)
                assistant_elements = self.driver.execute_locator(locator.assistant)

                user_content = [element.text for element in user_elements] if isinstance(user_elements, list) else [user_elements.text] if user_elements  else None
                assistant_content = [element.text for element in assistant_elements] if isinstance(assistant_elements, list) else [assistant_elements.text] if assistant_elements  else None
                
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
                        logger.debug(f'{counter} - {local_file_path}')
                        counter += 1
            except Exception as ex:
                logger.error(f"Ошибка обработки файла: {local_file_path}", exc_info=ex)
                ...
                continue


        if all_data:
            all_data_df = pd.concat(all_data, ignore_index=True)

            csv_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
            try:
                all_data_df.to_csv(csv_file_path, index=False, encoding='utf-8')
                logger.info(f"Сохранено в CSV: {csv_file_path}")
            except Exception as ex:
               logger.error(f"Ошибка сохранения в CSV файл: {csv_file_path}", exc_info=ex)
               ...


            jsonl_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
            try:
                all_data_df.to_json(jsonl_file_path, orient='records', lines=True, force_ascii=False)
                logger.info(f"Сохранено в JSONL: {jsonl_file_path}")
            except Exception as ex:
                logger.error(f"Ошибка сохранения в JSONL файл: {jsonl_file_path}", exc_info=ex)
                ...
          
            raw_conversations = ' '.join(all_data_df['content'].dropna().tolist())
            raw_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
            try:
                with open(raw_file_path, 'w', encoding='utf-8') as raw_file:
                  raw_file.write(raw_conversations)
                logger.info(f"Сохранены raw данные в: {raw_file_path}")
            except Exception as ex:
                 logger.error(f"Ошибка сохранения raw данных в файл: {raw_file_path}", exc_info=ex)
                 ...



traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()
model = Model()
model.stream_w(data_file_path=Path(gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'))
```