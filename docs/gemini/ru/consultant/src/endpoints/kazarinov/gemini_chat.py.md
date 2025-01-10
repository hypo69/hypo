# Анализ кода модуля `gemini_chat.py`

**Качество кода**
   -  Соответствие требованиям: 7/10
   -  Плюсы:
        - Код структурирован в класс `KazarinovAI`, что обеспечивает модульность.
        - Используются функции `recursively_read_text_files`, `j_dumps`, `pprint`, `logger` из `src`.
        - Присутствует обработка больших объемов данных через разбиение на чанки при обучении.
        - Есть функция для диалога с пользователем.
        - Добавлены docstring для классов и методов.

   -  Минусы:
        - Не все комментарии соответствуют стандарту RST.
        - Не везде используется `logger.error` для обработки исключений.
        - Есть избыточное использование `try-except`, которое можно заменить на `logger.error`.
        - Не все переменные и функции имеют описательные имена.
        -  Использование `time.sleep(5)` может быть заменено на асинхронную задержку или убрано в будующем.
        - В коде есть `...` как точки остановки, которые нужно убрать в релизной версии.
        -  Не стандартизированы выводы в консоль `print` и `logger.info`.
        -  Код в `chat` не должен быть частью модуля а выполнятся в отдельном скрипте.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавьте docstring для модуля в начале файла.
    -   Дополните docstring для всех функций и методов, включая описание параметров и возвращаемых значений.
    -   Используйте RST формат для docstring.
    -   Уберите `.. module::` и `.. platform::` это устаревшее оформление.
    -   Вместо  `# <- Q` используйте ` # Q:`
    -   Вместо `# <- A` используйте  ` # A:`
2.  **Логирование**:
    -   Замените `print` на `logger.info` для более стандартизированного вывода в консоль.
    -   Используйте `logger.error` для записи ошибок вместо `try-except` и `print` исключений.
3.  **Структура кода**:
    -   Вынесите инициализацию `KazarinovAI` в `if __name__ == "__main__":`.
    -   Удалите избыточный код `dialog_data` и `header` в методе `train()`.
    -   Упростите логику в методе `train()`.
    -  Удалить магические числа, такие как `5`.
4.  **Комментарии**:
    -   Улучшите комментарии, чтобы они более точно описывали логику кода.
    -   Уберите комментарии, которые не несут смысловой нагрузки.
5.  **Именование**:
    -   Переименуйте переменные `q`  и `a` на `question` и `answer`.
6. **Обработка ошибок**:
    -   Используйте `logger.error` для обработки ошибок в функции `ask`.
7.  **Код**:
    -   Разделение логики на более мелкие функции для улучшения читаемости.
    -   Удалите `...`
    -   Удалите `chat` функцию из модуля.
    -   Изменить тип возвращаемого значения функции `ask` на `str`
    -   Удалить `no_log`, `with_pretrain` у `ask` они не используются в вызываемом коде.
8. **Общее**:
    -   Не используйте задержки `time.sleep()` в основном коде.
    -   Добавить проверку на пустой список при чтении файлов.
    -   Использовать `j_loads_ns` вместо `json.load`.

**Оптимизированный код**
```python
"""
Модуль для работы с моделью Gemini для проекта Kazarinov.
=========================================================================================

Этот модуль содержит класс :class:`KazarinovAI`, который используется для работы с моделью
Google Gemini для обучения и ведения диалогов.

Пример использования
--------------------

Пример использования класса `KazarinovAI`:

.. code-block:: python

    k = KazarinovAI(system_instruction="You are a helpful assistant")
    k.train()
    k.dialog()
"""
import time
import random
from typing import Optional, List, Any
from pathlib import Path

from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files
from src.utils.printer import pprint
from src.logger.logger import logger


class KazarinovAI:
    """
    Класс для управления обучением и диалогами с использованием модели Google Gemini.

    Args:
        system_instruction (str, optional): Инструкция для модели. Defaults to None.
        generation_config (dict, optional): Конфигурация для генерации контента.
            Defaults to {"response_mime_type": "text/plain"}.
    """

    api_key = gs.credentials.gemini.kazarinov
    base_path = gs.path.google_drive / 'kazarinov'
    system_instruction_list: list = recursively_read_text_files(base_path, ['*.txt', '*.md'])
    history_file = f'{gs.now}.txt'
    gemini_1: GoogleGenerativeAI
    gemini_2: GoogleGenerativeAI
    timestamp = gs.now
    SLEEP_TIME = 5 # Задержка перед следующим запросом

    def __init__(self,
                 system_instruction: Optional[str] = None,
                 generation_config: dict = {"response_mime_type": "text/plain"}):
        """
        Инициализирует модель KazarinovAI с двумя экземплярами GoogleGenerativeAI.

        Args:
            system_instruction (str, optional): Инструкция для модели. Defaults to None.
            generation_config (dict, optional): Конфигурация для генерации контента.
                Defaults to {"response_mime_type": "text/plain"}.
        """
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config=generation_config,
            history_file=self.history_file
        )
        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config=generation_config,
            history_file=self.history_file
        )

    def _split_into_chunks(self, text_list: List[str], chunk_size: int) -> List[str]:
         """
         Разбивает список строк на чанки заданного размера.

         Args:
             text_list (list): Список строк для разбиения.
             chunk_size (int): Максимальный размер чанка.
         Returns:
            list[str]: Список чанков.
         """
         all_chunks = []
         current_chunk = ""
         for line in text_list:
            while len(current_chunk) + len(line) > chunk_size:
               space_left = chunk_size - len(current_chunk)
               current_chunk += line[:space_left]
               all_chunks.append(current_chunk)
               line = line[space_left:]
               current_chunk = ""
            current_chunk += line
         if current_chunk:
            all_chunks.append(current_chunk)
         return all_chunks

    def train(self):
        """
        Обучает модель, отправляя данные по частям.
        """
        chunk_size = 500000
        train_data_list: list = recursively_read_text_files(
            gs.path.data / 'kazarinov' / 'prompts' / 'train_data',
            ['*.*'],
            as_list=True
        )
        if not train_data_list:
            logger.error("Список обучающих данных пуст.")
            return

        all_chunks = self._split_into_chunks(train_data_list, chunk_size)
        for idx, chunk in enumerate(all_chunks):
            pprint(f"{chunk=}\n{len(chunk)}", text_color='light_blue')
            response = self.gemini_1.ask(q = chunk)
            pprint(response, text_color='yellow')
            time.sleep(self.SLEEP_TIME)

    def question_answer(self):
         """
         Отвечает на вопросы, используя предоставленные обучающие файлы.
         """
         questions = recursively_read_text_files(
             self.base_path / 'prompts' / 'train_data' / 'q',
             as_list=True
         )
         if not questions:
             logger.error("Список вопросов пуст.")
             return
         for question in questions:
             pprint(self.gemini_1.ask(question))

    def dialog(self):
        """
        Запускает диалог, перемешивая вопросы из разных языков.
        """
        questions = recursively_read_text_files(
            self.base_path / 'prompts' / 'train_data' / 'q',
            patterns=['*.*'],
            as_list=True
        )
        if not questions:
            logger.error("Список вопросов пуст.")
            return
        random.shuffle(questions)
        for question in questions:
            pprint(f'Q:> {question}', text_color='yellow') # Q:
            pprint(' ', text_color='green')
            answer = self.gemini_1.ask(question)
            pprint(f'A:> {answer}', text_color='cyan') # A:
            pprint('------------------------------------', text_color='green')
            time.sleep(self.SLEEP_TIME)

    def ask(self, question: str) -> str:
        """
        Отправляет вопрос модели и возвращает ответ.

        Args:
            question (str): Вопрос для модели.

        Returns:
            str: Ответ модели.
        """
        try:
            return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \\n Question: {question}")
        except Exception as e:
            logger.error(f"Ошибка при выполнении запроса: {e}", exc_info=True)
            return ""

if __name__ == "__main__":
    system_instruction = recursively_read_text_files(
    gs.path.google_drive / 'kazarinov' / 'prompts',
    ['system_instruction.txt'],
    as_list = True
    )
    if system_instruction:
        k = KazarinovAI(system_instruction = system_instruction[0])
        k.train()
        #k.dialog()
    else:
        logger.error("Не удалось загрузить системные инструкции.")