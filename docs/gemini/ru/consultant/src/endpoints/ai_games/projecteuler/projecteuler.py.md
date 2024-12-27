# Анализ кода модуля `projecteuler.py`

**Качество кода**
8/10
-  Плюсы
    -  Код использует асинхронность для выполнения IO-операций, что способствует повышению производительности.
    -  Используются `Path` для работы с файловой системой, что делает код более читаемым и надежным.
    -  Применение `j_loads_ns` для загрузки конфигурации.
    -  Разделение логики на классы и методы, что способствует лучшему структурированию кода.
-  Минусы
    -  Не хватает документации в формате RST для функций, методов, класса и модуля.
    -  Используется `time.sleep()` для пауз, что может блокировать основной поток и замедлять выполнение, лучше использовать `asyncio.sleep()`.
    -  В коде присутствуют `...` как точки остановки, что является недопустимым в финальном коде.
    -  Использование f-строк в формировании путей к файлам может быть улучшено для лучшей читаемости.
    -  Не используются `logger` для логирования ошибок и отладки.
    -  В методах `save_problem` и `save_problem_solve` не используется `async` и не используется запись асинхронно, что блокирует основной поток.

**Рекомендации по улучшению**

1.  **Документация**: Добавить документацию в формате RST для модуля, класса и методов.
2.  **Импорты**: Добавить недостающие импорты, например `from src.logger.logger import logger`.
3.  **Обработка ошибок**: Использовать `logger.error` для обработки ошибок и избегать общих `try-except`.
4.  **Асинхронность**: Использовать `asyncio.sleep()` вместо `time.sleep()`.
5.  **Удаление точек остановки**: Убрать все `...` и реализовать логику.
6.  **Форматирование**: Улучшить форматирование f-строк для путей к файлам.
7.  **Асинхронные операции с файлами**: Использовать асинхронные операции для чтения и записи файлов, где это применимо.
8.  **Переменные**: Переименовать переменные `q` и `response` на более описательные названия.

**Оптимизированный код**

```python
"""
Модуль для работы с Project Euler.
=========================================================================================

Этот модуль содержит класс :class:`ProjectEuler`, который используется для сбора и решения
задач Project Euler с использованием моделей ИИ.

Пример использования
--------------------

Пример использования класса `ProjectEuler`:

.. code-block:: python

    euler = ProjectEuler(lang='en')
    asyncio.run(euler.collect_problems())
    asyncio.run(euler.solve_probems())
"""
from __future__ import annotations

import asyncio
import time
from pathlib import Path
from types import SimpleNamespace

from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.jjson import j_loads_ns
from src.utils.file import get_filenames
from src.logger.logger import logger  # Добавлен импорт logger


class ProjectEuler:
    """
    Класс для сбора и решения задач Project Euler с использованием моделей ИИ.

    :param lang: Язык, на котором будут формулироваться задачи и решения.
    :type lang: str
    :ivar lang: Язык, на котором будут формулироваться задачи и решения.
    :vartype lang: str
    :ivar alice: Экземпляр GoogleGenerativeAI для получения текста задачи.
    :vartype alice: GoogleGenerativeAI
    :ivar bob: Экземпляр GoogleGenerativeAI для получения решения задачи.
    :vartype bob: GoogleGenerativeAI
    :ivar base_path: Путь к директории с ресурсами Project Euler.
    :vartype base_path: Path
    :ivar alice_instruction: Инструкция для модели ИИ, генерирующей текст задачи.
    :vartype alice_instruction: str
    :ivar bob_instruction: Инструкция для модели ИИ, генерирующей решение задачи.
    :vartype bob_instruction: str
    :ivar config: Конфигурация приложения.
    :vartype config: SimpleNamespace
    """
    lang: str
    alice: GoogleGenerativeAI
    bob: GoogleGenerativeAI
    base_path: Path = gs.path.endpoints / 'ai_games' / 'projecteuler'
    alice_instruction: str
    bob_instruction: str
    config: SimpleNamespace = j_loads_ns(base_path / 'projecteuler.json')

    def __init__(self, lang: str = 'en'):
        """
        Инициализация экземпляра класса ProjectEuler.

        :param lang: Язык, на котором будут формулироваться задачи и решения.
        :type lang: str
        """
        self.lang = lang
        # Код исполняет чтение инструкций для alice из файла
        self.alice_instruction = Path(self.base_path / 'assets' / 'instructions' / f'alice.{self.lang}.md').read_text(encoding='UTF-8')
        # Код исполняет чтение инструкций для bob из файла
        self.bob_instruction = Path(self.base_path / 'assets' / 'instructions' / f'bob.{self.lang}.md').read_text(encoding='UTF-8')
        
        # Код инициализирует модель ИИ для bob
        self.bob = GoogleGenerativeAI(
            model_name=self.config.model_name,
            api_key=gs.credentials.gemini.onela
        )
        # Код инициализирует модель ИИ для alice
        self.alice = GoogleGenerativeAI(
            model_name=self.config.model_name,
            api_key=gs.credentials.gemini.onela
        )

    async def collect_problems(self):
        """
        Асинхронно собирает задачи Project Euler, запрашивая их у модели ИИ.
        """
        
        for i in range(135, 900):
             # Код формирует запрос к ИИ для получения текста задачи
            query = self.alice_instruction.replace('<PROBLEM_NUMBER>', str(i))
            try:
                # Код отправляет запрос к ИИ и получает ответ
                response = await self.alice.ask(query)
                self.save_problem(str(i), response)
                # Код делает паузу
                await asyncio.sleep(25)
            except Exception as e:
               # Код логирует ошибку в случае неудачи
                logger.error(f"Ошибка при сборе задачи № {i}: {e}", exc_info=True)

    async def solve_probems(self):
        """
        Асинхронно решает задачи Project Euler, запрашивая решения у модели ИИ.
        """
        # Код получает список файлов с задачами
        problems_to_solve_files_list = get_filenames(self.base_path / self.lang / 'problems')
        for file_name in problems_to_solve_files_list:
            try:
                # Код извлекает номер задачи из имени файла
                problem_number = int(file_name.split('_')[1].split('.')[0])
                # Код читает текст задачи из файла
                problem_text = Path(self.base_path / self.lang / 'problems' / file_name).read_text(encoding='UTF-8')
                # Код формирует запрос к ИИ для получения решения задачи
                query = self.bob_instruction.replace('<PROBLEM_TO_SOLVE>', problem_text)
                # Код отправляет запрос к ИИ и получает ответ
                response = await self.bob.ask(query)
                self.save_problem_solve(problem_number, response)
                # Код делает паузу
                await asyncio.sleep(25)
            except Exception as e:
                # Код логирует ошибку в случае неудачи
                logger.error(f"Ошибка при решении задачи № {problem_number}: {e}", exc_info=True)

    def save_problem(self, problem_number: str, problem_text: str):
        """
        Сохраняет текст задачи в файл.

        :param problem_number: Номер задачи.
        :type problem_number: str
        :param problem_text: Текст задачи.
        :type problem_text: str
        """
        # Код формирует путь к файлу для сохранения задачи
        output_file = self.base_path / self.lang / 'problems' / f'e_{problem_number}.md'
        # Код создает директорию для файла, если она не существует
        output_file.parent.mkdir(parents=True, exist_ok=True)
        # Код записывает текст задачи в файл
        output_file.write_text(problem_text, encoding='UTF-8')
        print(f'Saved problem No {problem_number}')

    def save_problem_solve(self, problem_number: str, solve_text: str):
        """
        Сохраняет решение задачи в файл.

        :param problem_number: Номер задачи.
        :type problem_number: str
        :param solve_text: Текст решения задачи.
        :type solve_text: str
        """
        # Код формирует путь к файлу для сохранения решения задачи
        output_file = self.base_path / self.lang / 'solves' / f'e_{problem_number}.md'
        # Код создает директорию для файла, если она не существует
        output_file.parent.mkdir(parents=True, exist_ok=True)
        # Код записывает текст решения задачи в файл
        output_file.write_text(solve_text, encoding='UTF-8')
        print(f'Saved sovle No {problem_number}')


if __name__ == '__main__':
    languages_list: list = ['ru', 'he', 'en']
    for lang in languages_list:
        euler = ProjectEuler(lang)
        asyncio.run(euler.collect_problems())
        asyncio.run(euler.solve_probems())
```