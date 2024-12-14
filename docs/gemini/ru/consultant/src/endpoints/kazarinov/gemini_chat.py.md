# Анализ кода модуля `gemini_chat.py`

**Качество кода**
**8**
-  Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что способствует его читаемости и повторному использованию.
    - Используются логирование и цветной вывод, что улучшает отслеживание и восприятие информации.
    -  Применяются асинхронные операции, что повышает производительность.
-  Минусы
    -  Не все комментарии оформлены в стиле reStructuredText (RST).
    -  В некоторых местах используются избыточные блоки `try-except`, которые можно заменить на логирование ошибок.
    -  В коде присутствуют неиспользуемые закомментированные участки кода, которые стоит удалить.
    -  Не все функции и переменные имеют docstring.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Необходимо переписать все комментарии и docstring в формате RST.
    -   Добавить подробные описания для всех функций, методов и классов.
2.  **Импорты:**
    -   Проверить и добавить все отсутствующие импорты.
3.  **Обработка ошибок:**
    -   Избегать избыточного использования `try-except` блоков, заменяя их на логирование ошибок с помощью `logger.error`.
4.  **Рефакторинг:**
    -   Удалить все закомментированные блоки кода, которые не используются.
    -   Привести имена переменных и функций в соответствие с ранее обработанными файлами.
5.  **Логирование:**
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
6.  **Структура кода:**
    -   Разбить длинные функции на более мелкие для повышения читаемости.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для взаимодействия с Google Gemini API в рамках проекта Kazarinov.
=======================================================================

Этот модуль предоставляет класс `KazarinovAI`, который упрощает взаимодействие
с Google Gemini API для обучения моделей и ведения диалогов.

Пример использования:
--------------------

.. code-block:: python

    k = KazarinovAI(system_instruction='You are a helpful assistant.')
    k.train()
    k.dialog()
"""
MODE = 'dev'
import time
import random
from typing import Optional, Any
from pathlib import Path
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files, read_text_file
from src.utils.jjson import j_dumps
from src.utils.printer import pprint, input_colored, GREEN
from src.logger.logger import logger
import json  # добавление отсутствующего импорта


class KazarinovAI:
    """
    Класс для управления обучением и ведением диалогов с использованием Google Gemini API.

    :param system_instruction: Инструкция для модели. По умолчанию None.
    :type system_instruction: str, optional
    :param generation_config: Конфигурация для генерации контента. По умолчанию {"response_mime_type": "text/plain"}.
    :type generation_config: dict | list[dict], optional
    """

    api_key = gs.credentials.gemini.kazarinov
    base_path = gs.path.google_drive / 'kazarinov'
    system_instruction_list: list = recursively_read_text_files(base_path, ['*.txt', '*.md'])
    history_file = f'{gs.now}.txt'

    gemini_1: GoogleGenerativeAI
    gemini_2: GoogleGenerativeAI
    timestamp = gs.now

    def __init__(self,
                 system_instruction: Optional[str] = None,
                 generation_config: dict | list[dict] = {"response_mime_type": "text/plain"}):
        """
        Инициализирует класс KazarinovAI.

        :param system_instruction: Инструкция для модели. По умолчанию None.
        :type system_instruction: str, optional
        :param generation_config: Конфигурация для генерации контента. По умолчанию {"response_mime_type": "text/plain"}.
        :type generation_config: dict | list[dict], optional
        """
        # Инициализация первого экземпляра модели Google Generative AI (gemini_1).
        # Использует переданный API ключ, системные инструкции и файл истории.
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={"response_mime_type": "text/plain"},
            history_file=f'{gs.now}.txt'
        )
        # Инициализация второго экземпляра модели (gemini_2).
        # Идентична gemini_1, но с отдельным файлом истории.
        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={"response_mime_type": "text/plain"},
            history_file=f'{gs.now}.txt'
        )

    def train(self):
        """
        Обучает модель, используя текстовые данные из файлов, разбивая их на части.
        """
        chunk_size = 500000
        all_chunks = []
        train_data_list: list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data',
                                                             ['*.*'], as_list=True)

        current_chunk = ""

        for line in train_data_list:
            while len(current_chunk) + len(line) > chunk_size:
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)
                line = line[space_left:]
                current_chunk = ""
            current_chunk += line

        if current_chunk:
            all_chunks.append(current_chunk)

        for idx, chunk in enumerate(all_chunks):
            pprint(f"{chunk=}\n{len(chunk)}", text_color='light_blue')
            response = self.gemini_1.ask(q=chunk)
            pprint(response, text_color='yellow')
            time.sleep(5)

    def question_answer(self):
        """
        Задает вопросы и выводит ответы модели.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)

        for q in questions:
            pprint(self.gemini_1.ask(q))

    def dialog(self):
        """
        Запускает диалог с моделью, используя случайные вопросы из разных языков.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'], as_list=True)

        random.shuffle(questions)

        for q in questions:
            pprint(f'Q:> {q}', text_color='yellow')
            pprint(' ', text_color='green')
            a = self.gemini_1.ask(q)
            pprint(f'A:> {a}', text_color='cyan')
            pprint('------------------------------------', text_color='green')
            time.sleep(5)
            ...

    def ask(self, q: str, no_log: bool = False, with_pretrain: bool = True) -> str:
        """
        Отправляет вопрос модели.

        :param q: Задаваемый вопрос.
        :type q: str
        :param no_log: Отключает логирование запроса и ответа, по умолчанию False
        :type no_log: bool, optional
        :param with_pretrain: Указывает, нужно ли использовать предварительное обучение, по умолчанию True
        :type with_pretrain: bool, optional
        :return: Ответ модели.
        :rtype: str
        """
        return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \\n Question: {q}",
                                 no_log=no_log, with_pretrain=False)


def chat():
    """
    Запускает сессию чата с ИИ-ассистентом Kazarinov.

    Читает системные инструкции и обрабатывает пользовательский ввод, пока пользователь не решит выйти.
    Использует класс Kazarinov для обработки запросов пользователя и предоставления ответов.
    """
    questions_list: list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q',
                                                        ['*.*'])

    print(f"""
    Чтобы завершить чат, напишите `--q`
    Чтобы загрузить вопрос из базы вопросов напишите `--next`""")

    k = KazarinovAI()  # Инициализация KazarinovAI
    logger.info(k.ask("Привет, представься"))
    while True:

        q = input_colored(">>>> ", GREEN)
        if q.lower() == 'exit':
            print("Чат завершен.")
            break

        if q.lower() == '--next' or q.lower() == '--нехт':
            q_list: list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            q = q_list[random.randint(0, len(q_list) - 1)]
            print(f"{q=}")
            response = k.ask(f"{q}", no_log=True, with_pretrain=False)
            logger.info(response)
            continue

        response = k.ask(q, no_log=False, with_pretrain=False)
        logger.info(response)


if __name__ == "__main__":
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
    # k.dialog()

```