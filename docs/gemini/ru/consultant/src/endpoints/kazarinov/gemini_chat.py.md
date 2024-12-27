# Анализ кода модуля `gemini_chat.py`

**Качество кода**
8
- Плюсы
    - Код структурирован и разбит на классы и функции, что облегчает понимание и поддержку.
    - Используются логирование и вывод отладочной информации.
    - Есть docstring для класса и основных методов.
    - Применяется кастомная библиотека `src`.

- Минусы
    - Не все docstring соответствуют стандарту RST.
    - Некоторые комментарии не соответствуют формату reStructuredText.
    - Есть избыточные и незадействованные переменные.
    - Не везде используется логирование ошибок.
    - Не все импорты используются, требуется их проверка.
    - Не используются константы для значений по умолчанию, что усложняет понимание и поддержку кода.
    - Не все методы класса документированы в формате reStructuredText.

**Рекомендации по улучшению**

1.  **Формат документации**: Привести все docstring и комментарии к формату reStructuredText (RST).
2.  **Импорты**: Проверить и добавить недостающие импорты, удалить неиспользуемые.
3.  **Логирование**: Добавить логирование ошибок в блоках `try-except`, где это требуется.
4.  **Константы**: Определить константы для значений по умолчанию, таких как `response_mime_type`.
5.  **Комментарии**: Уточнить комментарии, где это необходимо.
6.  **Переменные**: Удалить неиспользуемые переменные и привести имена переменных в соответствие со стандартами.
7.  **Обработка данных**: Использовать `j_loads` и `j_dumps` из `src.utils.jjson` вместо стандартных `json.load` и `json.dumps`.
8.  **Общая структура**: Добавить документацию для каждого метода и класса.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Gemini API для проекта Kazarinov
===========================================================

Этот модуль содержит класс :class:`KazarinovAI`, который используется для обучения моделей и генерации диалогов
с использованием Google Gemini API.

Основные возможности:
    - Загрузка системных инструкций и обучающих данных.
    - Разделение обучающих данных на части для обработки.
    - Генерация ответов на основе входных вопросов.
    - Поддержка диалогового режима.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.kazarinov.gemini_chat import KazarinovAI

    system_instruction = "You are a helpful assistant."
    kazarinov_ai = KazarinovAI(system_instruction=system_instruction)
    kazarinov_ai.train()
    response = kazarinov_ai.ask("What is your name?")
    print(response)
"""
import time
import random
from typing import Optional, Any
from pathlib import Path

from src import gs
from src.ai.openai import OpenAIModel  # TODO: check if used
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files, read_text_file # TODO: check if used get_filenames and recursively_get_filepath
from src.utils.jjson import j_dumps
from src.utils.printer import pprint, input_colored, GREEN
from src.logger.logger import logger


class KazarinovAI:
    """
    Управляет обучением модели и генерацией диалогов для проекта Kazarinov
    с использованием GoogleGenerativeAI.

    :param system_instruction: Инструкция для модели, определяющая её системную роль.
    :type system_instruction: str, optional
    :param generation_config: Конфигурация для генерации контента.
    :type generation_config: dict | list[dict], optional
    """

    _RESPONSE_MIME_TYPE = "text/plain"  # Константа для типа ответа
    api_key = gs.credentials.gemini.kazarinov
    base_path = gs.path.google_drive / 'kazarinov'
    system_instruction_list: list = recursively_read_text_files(base_path, ['*.txt', '*.md'])
    history_file = f'{gs.now}.txt'
    gemini_1: GoogleGenerativeAI
    gemini_2: GoogleGenerativeAI
    timestamp = gs.now

    def __init__(self,
                 system_instruction: str = None,
                 generation_config: dict | list[dict] = None):
        """
        Инициализирует модель Kazarinov.

        :param system_instruction: Инструкция для модели, определяющая её системную роль.
        :type system_instruction: str, optional
        :param generation_config: Конфигурация для генерации контента.
        :type generation_config: dict | list[dict], optional
        """
        if generation_config is None:
            generation_config = {"response_mime_type": self._RESPONSE_MIME_TYPE}

        # Инициализация первого экземпляра модели Google Generative AI (gemini_1)
        # Используется переданный API ключ, системные инструкции и файл истории.
        try:
            self.gemini_1 = GoogleGenerativeAI(
                api_key=self.api_key,
                system_instruction=system_instruction,
                generation_config=generation_config,
                history_file=f'{gs.now}.txt'
            )
        except Exception as e:
            logger.error(f'Ошибка при инициализации gemini_1: {e}')
            raise

        # Инициализация второго экземпляра модели (gemini_2)
        # Идентична gemini_1, но с отдельным файлом истории.
        try:
            self.gemini_2 = GoogleGenerativeAI(
                api_key=self.api_key,
                system_instruction=system_instruction,
                generation_config=generation_config,
                history_file=f'{gs.now}.txt'
            )
        except Exception as e:
            logger.error(f'Ошибка при инициализации gemini_2: {e}')
            raise

    def train(self):
        """
        Обучает модель, используя предоставленный список обучающих файлов,
        отправляя данные частями заданного размера.
        """
        chunk_size = 500000
        all_chunks = []
        train_data_list: list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data',
                                                            ['*.*'], as_list=True)
        current_chunk = ""

        for line in train_data_list:
            # Если текущий чанк плюс новая строка превышают chunk_size, разделяем
            while len(current_chunk) + len(line) > chunk_size:
                # Определяем, сколько строки можно добавить к текущему чанку
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)

                # Начинаем новый чанк с остатка строки
                line = line[space_left:]
                current_chunk = ""

            # Если осталась какая-либо часть строки, добавляем её
            current_chunk += line

        # Если осталась часть последнего чанка, добавляем его
        if current_chunk:
            all_chunks.append(current_chunk)

        # Отправляем данные по частям
        for idx, chunk in enumerate(all_chunks):
            # logger.info(f"Sending chunk {idx + 1} of {len(all_chunks)}")
            pprint(f"{chunk=}\\n{len(chunk)}", text_color='light_blue')

            # Отправляем каждый чанк модели
            try:
                response = self.gemini_1.ask(q=chunk)
                pprint(response, text_color='yellow')
                time.sleep(5)
            except Exception as e:
                logger.error(f'Ошибка при отправке чанка {idx + 1}: {e}')
                continue  # Продолжить обработку других чанков

            # # Сохраняем данные диалога в JSON
            # dialog_data = {
            #     "chunk_index": idx + 1,
            #     "prompt_chunk": chunk,
            #     "response": response
            # }
            # j_dumps(Path(base_path / 'train' / f'{self.timestamp}_chunk{idx + 1}.json'), dialog_data)


    def question_answer(self):
        """
        Обрабатывает процесс вопросов-ответов, используя предоставленные обучающие файлы.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)

        for q in questions:
            try:
               response = self.gemini_1.ask(q)
               pprint(response)
            except Exception as e:
                logger.error(f'Ошибка в процессе question_answer: {e}')
                continue  # Продолжить выполнение со следующим вопросом

    def dialog(self):
        """
        Запускает диалог на основе предварительно заданных вопросов, перемешивая вопросы из разных языков.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'],
                                                as_list=True)

        random.shuffle(questions)

        for q in questions:
            pprint(f'Q:> {q}', text_color='yellow')  # <- Q
            pprint(' ', text_color='green')
            try:
                a = self.gemini_1.ask(q)
                pprint(f'A:> {a}', text_color='cyan')  # <- A
                pprint('------------------------------------', text_color='green')
                time.sleep(5)
            except Exception as e:
                logger.error(f'Ошибка в процессе dialog: {e}')
                continue # Продолжить диалог со следующим вопросом
            ...

    def ask(self, q: str, no_log: bool = False, with_pretrain: bool = True) -> Any:
        """
        Отправляет запрос в модель и возвращает ответ.

        :param q: Запрос для отправки.
        :type q: str
        :param no_log: Флаг, определяющий, нужно ли логировать запрос.
        :type no_log: bool, optional
        :param with_pretrain: Флаг, определяющий, нужно ли использовать предварительное обучение.
        :type with_pretrain: bool, optional
        :return: Ответ от модели.
        :rtype: Any
        """
        try:
            response = self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \\n Question: {q}",
                                         no_log=no_log, with_pretrain=False)
            return response
        except Exception as e:
            logger.error(f'Ошибка в методе ask: {e}')
            return None


def chat():
    """
    Инициирует сеанс чата с AI-ассистентом Kazarinov.

    Эта функция считывает системные инструкции из текстовых файлов и обрабатывает ввод пользователя
    до тех пор, пока пользователь не решит выйти из чата. Она использует класс Kazarinov для обработки
    запросов пользователя и предоставления ответов.

    :raises Exception: Если возникает проблема при чтении файлов системных инструкций.
    """

    # k = KazarinovAI(system_instruction=system_instruction_list[random.randint(0, len(system_instruction_list) - 1)],
    #               generation_config={'response_mime_type': 'text/plain'})

    questions_list: list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q',
                                                        ['*.*'])

    print(f"""
    Чтобы завершить чат, напишите `--q`
    Чтобы загрузить вопрос из базы вопросов напишите `--next`""")

    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')

    k = KazarinovAI(system_instruction=system_instruction)

    logger.info(k.ask("Привет, представься"))

    while True:

        # Получаем ввод пользователя
        q = input_colored(">>>> ", GREEN)
        if q.lower() == 'exit':
            print("Чат завершен.")
            break

        if q.lower() == '--next' or q.lower() == '--нехт':
            q_list: list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            q = q_list[random.randint(0, len(q_list) - 1)]
            print(f"{q=}")
            try:
                response = k.ask(f"{q}", no_log=True, with_pretrain=False)
                logger.info(response)
            except Exception as e:
                logger.error(f'Ошибка в чате при обработке --next: {e}')
            continue

        # Отправляем вопрос пользователя AI и получаем ответ
        try:
            response = k.ask(q, no_log=False, with_pretrain=False)
            logger.info(response)
        except Exception as e:
            logger.error(f'Ошибка в чате при отправке запроса: {e}')


if __name__ == "__main__":
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
    # k.dialog()

```