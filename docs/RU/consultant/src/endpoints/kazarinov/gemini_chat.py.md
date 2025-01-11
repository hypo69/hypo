# Анализ кода модуля `gemini_chat.py`

**Качество кода**
7
-  Плюсы
    -  Используется  `logger` для логирования.
    -  Присутствуют docstring для классов и функций.
    -  Код разбит на логические блоки.
    -  Используются `recursively_read_text_files` для чтения файлов.
    -  Есть примеры использования `pprint` для вывода данных.
-  Минусы
    -  Не все функции документированы в формате RST.
    -  Не везде используются одинарные кавычки в коде Python.
    -  В некоторых местах  используется `print` вместо `logger`.
    -  Используются магические значения (`chunk_size = 500000`).
    -  Отсутствует обработка ошибок в некоторых функциях.
    -  Используется `time.sleep` в цикле, что замедляет выполнение программы.

**Рекомендации по улучшению**

1.  **Форматирование кода**:
    -   Использовать только одинарные кавычки `'` для строк в коде Python, двойные кавычки `"` использовать только для операций вывода (например, `print`, `input`, `logger`).
2.  **Документация**:
    -   Добавить документацию в формате RST для всех функций и методов, включая аргументы и возвращаемые значения.
    -   Использовать `sphinx` формат для docstring.
3.  **Логирование**:
    -   Заменить `print` на `logger` для вывода информации, включая ошибки.
    -   Улучшить информативность логов, добавив контекст.
4.  **Обработка ошибок**:
    -   Добавить обработку исключений с использованием `try-except` и логированием ошибок с помощью `logger.error`.
    -   Избегать использования `...` в коде.
5.  **Конфигурация**:
    -   Вынести магические значения (например, `chunk_size`) в константы или настройки.
6.  **Оптимизация**:
    -   Избегать использования `time.sleep` в циклах.
7.  **Структура кода**:
    -   Разделить код на более мелкие, переиспользуемые функции.
    -   Улучшить читаемость кода, добавив пустые строки для разделения логических блоков.
8. **Импорты**
    - Проверить и добавить отсутствующие импорты в код.
    - Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с моделью Google Gemini для проекта Kazarinov.
=========================================================================================

Этот модуль содержит класс :class:`KazarinovAI`, который используется для работы с Google Gemini,
для выполнения задач по обработке и генерации текста.

Пример использования
--------------------

Пример использования класса `KazarinovAI`:

.. code-block:: python

    k = KazarinovAI(system_instruction='some instruction')
    k.train()
    k.dialog()
"""
import time
import random
from typing import Optional, Any
from pathlib import Path
from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursively_read_text_files, recursively_get_filepath
from src.utils.jjson import j_dumps, j_loads
from src.utils.printer import pprint, input_colored, GREEN
from src.logger.logger import logger


class KazarinovAI:
    """
    Класс для управления моделью Kazarinov с использованием Google Generative AI.

    :param system_instruction: Инструкция для модели.
    :type system_instruction: str, optional
    :param generation_config: Конфигурация генерации текста.
    :type generation_config: dict | list[dict], optional
    """
    api_key = gs.credentials.gemini.kazarinov
    base_path = gs.path.google_drive / 'kazarinov'
    system_instruction_list: list = recursively_read_text_files(base_path, ['*.txt', '*.md'])
    history_file = f'{gs.now}.txt'
    gemini_1: GoogleGenerativeAI
    gemini_2: GoogleGenerativeAI
    timestamp = gs.now
    CHUNK_SIZE = 500000 # Размер чанка для разделения обучающих данных

    def __init__(self,
                 system_instruction: str = None,
                 generation_config: dict | list[dict] = {'response_mime_type': 'text/plain'}):
        """
        Инициализирует модель Kazarinov AI.

        Args:
            system_instruction (str, optional): Инструкция для модели. Defaults to None.
            generation_config (dict | list[dict], optional): Конфигурация генерации контента.
                Defaults to {"response_mime_type": "text/plain"}.
        """
        # Инициализация экземпляра модели Google Generative AI (gemini_1)
        # Использует переданный API ключ, системные инструкции и файл истории
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={'response_mime_type': 'text/plain'},
            history_file=f'{gs.now}.txt'
        )
        # Инициализация второго экземпляра модели (gemini_2)
        # Идентична gemini_1, но с отдельным файлом истории
        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={'response_mime_type': 'text/plain'},
            history_file=f'{gs.now}.txt'
        )

    def _split_into_chunks(self, text_list: list[str], chunk_size: int) -> list[str]:
        """
        Разбивает список строк на чанки заданного размера.

        Args:
            text_list (list[str]): Список строк для разделения.
            chunk_size (int): Размер чанка.
        Returns:
            list[str]: Список чанков.
        """
        all_chunks = []
        current_chunk = ''
        for line in text_list:
            while len(current_chunk) + len(line) > chunk_size:
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)
                line = line[space_left:]
                current_chunk = ''
            current_chunk += line
        if current_chunk:
            all_chunks.append(current_chunk)
        return all_chunks

    def train(self):
        """
        Обучает модель, отправляя данные порциями заданного размера.
        """
        try:
            train_data_list: list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data',
                                                            ['*.*'], as_list=True)
            all_chunks = self._split_into_chunks(train_data_list, self.CHUNK_SIZE)
            for idx, chunk in enumerate(all_chunks):
                pprint(f'{chunk=}\\n{len(chunk)}', text_color='light_blue')
                response = self.gemini_1.ask(q=chunk)
                pprint(response, text_color='yellow')
                time.sleep(5)
        except Exception as ex:
            logger.error('Ошибка при обучении модели', exc_info=ex)

    def question_answer(self):
        """
        Запускает процесс ответов на вопросы с использованием предоставленных файлов обучения.
        """
        try:
            questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)
            for q in questions:
                pprint(self.gemini_1.ask(q))
        except Exception as ex:
            logger.error('Ошибка при ответе на вопросы', exc_info=ex)

    def dialog(self):
        """
        Запускает диалог на основе предварительно определенных вопросов.
        """
        try:
            questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'],
                                                    as_list=True)
            random.shuffle(questions)
            for q in questions:
                pprint(f'Q:> {q}', text_color='yellow')  # <- Q
                pprint(' ', text_color='green')
                a = self.gemini_1.ask(q)
                pprint(f'A:> {a}', text_color='cyan')  # <- A
                pprint('------------------------------------', text_color='green')
                time.sleep(5)
                ...
        except Exception as ex:
            logger.error('Ошибка во время диалога', exc_info=ex)

    def ask(self, q: str, no_log: bool = False, with_pretrain: bool = True) -> bool:
        """
        Отправляет запрос модели и возвращает ответ.

        Args:
            q (str): Текст вопроса.
            no_log (bool, optional): Флаг для отключения логирования. Defaults to False.
            with_pretrain (bool, optional): Флаг для использования предварительной подготовки. Defaults to True.

        Returns:
            bool: Ответ модели.
        """
        try:
            return self.gemini_1.ask(f'role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \\n Question: {q}',
                                     no_log=no_log, with_pretrain=False)
        except Exception as ex:
             logger.error(f'Ошибка при запросе к модели: {q=}', exc_info = ex)
             return False

def chat():
    """
    Инициирует сессию чата с ассистентом Kazarinov.
    """
    try:
        questions_list: list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q',
                                                        ['*.*'])

        print("""
        Чтобы завершить чат, напишите `--q`
        Чтобы загрузить вопрос из базы вопросов напишите `--next`""")

        k = KazarinovAI(system_instruction='system_instruction') # todo: load sys instraction

        logger.info(k.ask('Привет, представься'))
        while True:
            q = input_colored('>>>> ', GREEN)
            if q.lower() == 'exit':
                print('Чат завершен.')
                break
            if q.lower() == '--next' or q.lower() == '--нехт':
                q_list: list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
                q = q_list[random.randint(0, len(q_list) - 1)]
                print(f'{q=}')
                response = k.ask(f'{q}', no_log=True, with_pretrain=False)
                logger.info(response)
                continue

            response = k.ask(q, no_log=False, with_pretrain=False)
            logger.info(response)
    except Exception as ex:
        logger.error('Ошибка в чате', exc_info=ex)


if __name__ == '__main__':
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
    # k.dialog()
```