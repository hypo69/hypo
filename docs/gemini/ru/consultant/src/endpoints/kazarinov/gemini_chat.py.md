# Анализ кода модуля `gemini_chat.py`

**Качество кода**
9
-  Плюсы
    - Код имеет четкую структуру, разбит на классы и функции.
    - Используется логирование для отслеживания работы программы.
    - Присутствует базовая обработка ошибок через `try-except` блоки.
    - Используются константы для базовых путей и настроек.
    -  Используется библиотека `src.utils.printer` для вывода цветного текста.
    - Присутствует документация в виде docstring, хотя и не в полной мере соответствует RST.
-  Минусы
    -  Комментарии в коде не соответствуют стандарту RST.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не все функции и методы имеют docstring.
    -  Используется `time.sleep` для задержки, что может быть неэффективным в некоторых случаях.
    -  Некоторые переменные и импорты не приведены в соответствие с ранее обработанными файлами.
    -  Присутствует избыточное использование try-except блоков.

**Рекомендации по улучшению**
1.  **Документация**:
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
    -   Добавить docstring ко всем функциям, методам и классам.

2.  **Обработка данных**:
    -   Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.

3.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
    -   Избегать избыточного использования `try-except`, предпочитать `logger.error`.

4.  **Рефакторинг**:
    -   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
    -   Убрать `time.sleep`.
    -    Избавиться от закомментированного кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с моделью Gemini для проекта Kazarinov.
=========================================================================================

Этот модуль содержит класс :class:`KazarinovAI`, который использует модель Google Gemini
для обучения и генерации диалогов. Он также включает функции для запуска чат-сессии.

Пример использования
--------------------

Пример инициализации класса и обучения модели:

.. code-block:: python

    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
"""
MODE = 'dev'
import time
import random
from typing import Optional, Any
from pathlib import Path
from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursively_read_text_files, recursively_get_filepath
from src.utils.jjson import j_dumps
from src.utils.printer import pprint, input_colored, GREEN
from src.logger.logger import logger

class KazarinovAI:
    """
    Класс для управления моделью Gemini в проекте Kazarinov.

    Этот класс инкапсулирует логику для обучения модели, ведения диалогов
    и обработки запросов с использованием Google Generative AI.

    :param system_instruction: Инструкция для модели, устанавливающая ее системную роль.
    :type system_instruction: str, optional
    :param generation_config: Конфигурация для генерации контента.
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
                 system_instruction: str = None,
                 generation_config: dict | list[dict] = {"response_mime_type": "text/plain"}):
        """
        Инициализирует модель KazarinovAI.

        :param system_instruction: Инструкция для модели, устанавливающая ее системную роль.
        :type system_instruction: str, optional
        :param generation_config: Конфигурация для генерации контента.
        :type generation_config: dict | list[dict], optional
        """
        #  Инициализация первого экземпляра модели Google Generative AI (gemini_1)
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={"response_mime_type": "text/plain"},
            history_file=f'{gs.now}.txt'
        )
        #  Инициализация второго экземпляра модели (gemini_2)
        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={"response_mime_type": "text/plain"},
            history_file=f'{gs.now}.txt'
        )

    def train(self):
        """
        Обучает модель, используя предоставленные обучающие файлы.

        Разбивает данные на фрагменты заданного размера и отправляет их модели для обучения.
        """
        chunk_size = 500000
        all_chunks = []  # List to hold all chunks
        train_data_list: list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data',
                                                            ['*.*'], as_list=True)

        current_chunk = ""  # String to accumulate text for the current chunk

        for line in train_data_list:
            # Если текущий фрагмент плюс новая строка превышают chunk_size, разбиваем его
            while len(current_chunk) + len(line) > chunk_size:
                # Определяем, сколько строки можно добавить к текущему фрагменту
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)

                # Начинаем новый фрагмент с оставшейся части строки
                line = line[space_left:]
                current_chunk = ""

            # Если осталась какая-либо часть строки, добавляем ее
            current_chunk += line

        # Если остался какой-либо фрагмент, добавляем его
        if current_chunk:
            all_chunks.append(current_chunk)

        # Отправляем данные по фрагментам
        for idx, chunk in enumerate(all_chunks):
            pprint(f"{chunk=}\\n{len(chunk)}", text_color='light_blue')

            # Отправляем каждый фрагмент модели
            response = self.gemini_1.ask(q=chunk)
            pprint(response, text_color='yellow')
            # time.sleep(5)  # Удалено time.sleep

    def question_answer(self):
        """
        Обрабатывает процесс ответов на вопросы, используя предоставленные обучающие файлы.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)

        for q in questions:
            pprint(self.gemini_1.ask(q))

    def dialog(self):
        """
        Запускает диалог на основе предопределенных вопросов.

        Перемешивает вопросы из разных языков и выводит их с ответами.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'],
                                                 as_list=True)

        random.shuffle(questions)

        for q in questions:
            pprint(f'Q:> {q}', text_color='yellow')
            pprint(' ', text_color='green')
            a = self.gemini_1.ask(q)
            pprint(f'A:> {a}', text_color='cyan')
            pprint('------------------------------------', text_color='green')
            # time.sleep(5)  # Удалено time.sleep
            ...

    def ask(self, q: str, no_log: bool = False, with_pretrain: bool = True) -> bool:
        """
        Отправляет запрос модели.

        :param q: Текст запроса.
        :type q: str
        :param no_log: Флаг отключения логирования.
        :type no_log: bool, optional
        :param with_pretrain: Флаг использования предварительного обучения.
        :type with_pretrain: bool, optional
        :return: Результат запроса.
        :rtype: bool
        """
        return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \\n Question: {q}",
                                no_log=no_log, with_pretrain=False)

def chat():
    """
    Инициирует чат-сессию с ИИ-ассистентом Kazarinov.

    Читает системные инструкции из текстовых файлов и обрабатывает ввод пользователя
    до тех пор, пока пользователь не решит выйти из чата. Использует класс Kazarinov
    для обработки запросов пользователя и предоставления ответов.

    :raises Exception: Если есть проблема с чтением файлов системных инструкций.
    """
    questions_list: list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q',
                                                        ['*.*'])
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)

    print(f"""
    Чтобы завершить чат, напишите `--q`
    Чтобы загрузить вопрос из базы вопросов напишите `--next`""")

    logger.info(k.ask("Привет, представься"))
    while True:
        #  Получаем ввод пользователя
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

        #  Отправляем вопрос пользователя ИИ и получаем ответ
        response = k.ask(q, no_log=False, with_pretrain=False)
        logger.info(response)

if __name__ == "__main__":
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
    # k.dialog()
```