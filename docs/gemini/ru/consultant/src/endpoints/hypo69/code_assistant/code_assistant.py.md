### Анализ кода модуля `assistant`

**Качество кода:**

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код разбит на логические блоки, что облегчает его понимание и поддержку.
    - Используются асинхронные операции, что позволяет эффективно обрабатывать ввод-вывод.
    - Присутствует обработка ошибок через `try-except` блоки, хотя местами можно улучшить логирование.
    - Код использует `logger` для вывода информации о процессе, что помогает в отладке.
    - Имеется разделение на функции и методы, что способствует модульности кода.
    - Присутствует документация в виде docstrings, хоть и не везде в формате RST.
- **Минусы**:
    - Не всегда используется одинарный формат кавычек для строк, что противоречит инструкции.
    - Используются стандартные `json.load`, вместо `j_loads`.
    - Не все функции имеют **RST** документацию.
    - Избыточное использование `...` как маркеров, которые не несут смысловой нагрузки.
    - В некоторых местах логирование ошибок не использует `logger.error`.
    - Не все методы класса имеют docstring.
    -  Импорт `logger` не стандартизирован (`from src.logger import logger`  и `from src.logger.logger import logger`).

**Рекомендации по улучшению:**

1.  **Унификация кавычек**: Заменить двойные кавычки на одинарные в коде (кроме `print`, `input`, `logger`).
2.  **Использование `j_loads`**: Заменить стандартные `json.load` на `j_loads` или `j_loads_ns`.
3.  **Унификация импорта `logger`**: Использовать `from src.logger.logger import logger`.
4.  **Улучшение документации**:
    - Добавить **RST** документацию для всех функций, методов и классов.
    - Добавить примеры использования в документацию, где это уместно.
5.  **Обработка ошибок**:
    - Избегать чрезмерного использования `try-except` без необходимости.
    -  Использовать `logger.error` для записи ошибок с исключением.
6.  **Улучшение читаемости**:
    - Убрать маркеры `...` там, где это не нужно.
7.  **Рефакторинг**:
    - Выровнять названия функций, переменных и импортов.
    - Пересмотреть методы `_remove_outer_quotes`, `_save_response` и `_signal_handler`, так как они дублируются.
8.  **Улучшение  `_create_request`**: Сделать формирование запроса более читаемым и понятным.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов
=========================================================================================

:class:`CodeAssistant`, читает файлы кода, отдает код в модели, модель обрабатывет код и возвращает его в класс, класс сохраняет результат
в директории `docs/gemini` В зависимости от роли файлы сохраняются в

Пример использования
--------------------

Пример использования класса `CodeAssistant`:
# задайте роль исполнителя, язык

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()

.. module:: src.endpoints.hypo69.code_assistant
    :platform: Windows, Unix
    :synopsis: Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов

.. header.py:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```
"""
import asyncio
import argparse
import sys
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace
import signal
import time
import re
import fnmatch

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.path import get_relative_path
from src.logger.logger import logger # fix:  Импорт logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary


class CodeAssistant:
    """
    Класс для работы ассистента программиста с моделями ИИ.

    :param role: Роль ассистента (например, 'doc_writer_md', 'code_checker').
    :type role: str, optional
    :param lang: Язык для обработки (например, 'ru', 'en').
    :type lang: str, optional
    :param models: Список моделей для использования (например, ['gemini'], ['openai']).
    :type models: list[str], optional
    :param kwargs: Дополнительные параметры для инициализации моделей.
    :type kwargs: dict, optional

    Пример:
        >>> assistant = CodeAssistant(role='code_checker', lang='ru', models=['gemini'])
        >>> assistant.process_files()
    """

    role: str
    lang: str
    config: SimpleNamespace
    gemini_model: GoogleGenerativeAI
    openai_model: OpenAIModel

    def __init__(self, role: Optional[str] = 'doc_writer_md', lang: Optional[str] = 'en', models: Optional[list[str, str] | str] = ['gemini'], **kwargs):
        """
        Инициализация ассистента с заданными параметрами.
        """
        self.config: SimpleNamespace = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json') # fix:  j_loads_ns
        self.role: str = role
        self.lang: str = lang
        self.models_list: list = kwargs.get('model', ['gemini']) # fix:  использование одинарных кавычек
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs):
        """
        Инициализация моделей на основе заданных параметров.
        """
        system_instruction = Path(gs.path.src / 'ai' / 'prompts' / 'developer' / 'CODE_RULES.MD').read_text(encoding='UTF-8') # fix:  использование одинарных кавычек
        if 'gemini' in self.models_list:
            self.gemini_model = GoogleGenerativeAI(
                model_name=self.config.gemini_model_name,
                api_key=gs.credentials.gemini.onela,
                system_instruction=system_instruction,
                **kwargs,
            )
        if 'openai' in self.models_list:
            self.openai_model = OpenAIModel(
                model_name='gpt-4o-mini',
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwargs,
            )

    @property
    def system_instruction(self) -> str | bool:
        """
        Чтение инструкции из файла.

        :return: Инструкция в виде строки или False в случае ошибки.
        :rtype: str | bool
        """
        try:
            return Path(
                gs.path.src
                / 'ai'
                / 'prompts'
                / 'developer'
                / f'CODE_RULES.{self.lang}.md'
            ).read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error(f'Error reading instruction file {ex}') # fix:  использование f-string
            return False

    @property
    def code_instruction(self) -> str | bool:
        """
        Чтение инструкции для кода.

        :return: Инструкция в виде строки или False в случае ошибки.
        :rtype: str | bool
        """
        try:
            return Path(
                gs.path.endpoints
                / 'hypo69'
                / 'code_assistant'
                / 'instructions'
                / f'instruction_{self.role}_{self.lang}.md'
            ).read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error(f'Error reading instruction file {ex}') # fix:  использование f-string
            return ''

    @property
    def translations(self) -> SimpleNamespace:
        """
        Загрузка переводов для ролей и языков.

        :return: Переводы в виде объекта SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(
            gs.path.endpoints
            / 'hypo69'
            / 'code_assistant'
            / 'translations'
            / 'translations.json'
        )

    def send_file(self, file_path: Path) -> str | None:
        """
        Отправка файла в модель.

        :param file_path: Абсолютный путь к файлу, который нужно отправить.
        :type file_path: Path
        :return: URL файла, если отправка прошла успешно, None в противном случае.
        :rtype: str | None
        """
        try:
            # Отправка файла в модель
            response = self.gemini_model.upload_file(file_path) # fix: убрали `...`

            if response:
                if hasattr(response, 'url'):
                    return response.url

            return None
        except Exception as ex:
            logger.error(f'Ошибка при отправке файла: {ex}') # fix:  использование f-string
            return None

    async def process_files(self, start_dirs: str | Path | list[str, str] | list[Path, Path] = None, start_file_number: Optional[int] = 1) -> bool:
        """
        Компиляция, отправка запроса и сохранение результата.

        :param start_dirs: Список директорий для обработки или путь к директории.
        :type start_dirs: str|Path|list[str,str]|list[Path,Path], optional
        :param start_file_number: Номер файла, с которого начинать обработку.
        :type start_file_number: int, optional
        :return: True, если обработка завершена успешно, False в противном случае.
        :rtype: bool
        """
        if not start_dirs:
            start_dirs = self.config.start_dirs
        if not start_dirs:
            logger.error('Ошибка иницаилизации стартовой директории') # fix:  использование logger.error()
            return False
        start_dirs = start_dirs if isinstance(start_dirs, list) else [start_dirs] # fix:  использование одинарных кавычек

        for process_driectory in start_dirs:
            logger.info(f'Start {process_driectory=}') # fix:  использование f-string

            for i, (file_path, content) in enumerate(self._yield_files_content(process_driectory)):
                if not any((file_path, content)):  # <- ошибка чтения файла
                    continue
                if i < start_file_number:  # <- старт с номера файла
                    continue
                if file_path and content:
                    content_request = self._create_request(file_path, content)
                    response = await self.gemini_model.ask(content_request)

                    if response:
                        response = self._remove_outer_quotes(response)

                        if not await self._save_response(file_path, response, 'gemini'): # fix:  использование одинарных кавычек
                            logger.error(f'Файл {file_path} \\n НЕ сохранился') # fix:  использование f-string
                            continue
                        logger.debug(f'Processed file number: {i + 1}', None, False) # fix:  использование f-string
                    else:
                        logger.error('Ошибка ответа модели') # fix:  использование logger.error()
                        continue
                await asyncio.sleep(20)  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (change timeout)
        return True

    def _create_request(self, file_path: str, content: str) -> str:
        """
        Создание запроса с учетом роли и языка.

        :param file_path: Путь к файлу.
        :type file_path: str
        :param content: Содержимое файла.
        :type content: str
        :return: Запрос в виде строки.
        :rtype: str
        """
        try:
            roles_translations: SimpleNamespace = getattr(self.translations.roles, self.role, 'doc_writer_md')
            role_description_translated: str = getattr(roles_translations, self.lang, 'Your specialization is documentation creation in the `MD` format')
            file_location_translated: str = getattr(self.translations.file_location_translated, self.lang, 'Path to file: ')

            content_request: dict = {
                'role': f'{role_description_translated}', # fix:  использование f-string
                'output_language': self.lang,
                f'{file_location_translated}': get_relative_path(file_path, 'hypotez'), # fix:  использование f-string
                'instruction': self.code_instruction or '',
                'input_code': f'```{content}```', # fix:  использование f-string
            }
            return str(content_request)
        except Exception as ex:
            logger.error(f'Ошибка в составлении запроса: {ex}') # fix:  использование f-string
            return content

    def _yield_files_content(
        self,
        process_driectory: str | Path,
    ) -> Iterator[tuple[Path, str]]:
        """
        Генерирует пути файлов и их содержимое по указанным шаблонам.

        :param process_driectory: Абсолютный путь к стартовой директории
        :type process_driectory: Path | str
        :return: Итератор, выдающий кортежи (путь_к_файлу, содержимое_файла).
        :rtype: Iterator[tuple[Path, str]]
        """
        process_driectory: Path = process_driectory if isinstance(process_driectory, Path) else Path(process_driectory)

        try:
            exclude_file_patterns = [
                re.compile(pattern) for pattern in self.config.exclude_file_patterns
            ]

        except Exception as ex:
            logger.error(f'Не удалось скомпилировать регулярки из списка:/n{self.config.exclude_file_patterns=}\\n {ex}') # fix:  использование f-string
        include_file_patterns = self.config.include_files

        for file_path in process_driectory.rglob('*'):
            if not any(
                fnmatch.fnmatch(file_path.name, pattern)
                for pattern in include_file_patterns
            ):
                continue

            if any(
                exclude_dir in file_path.parts
                for exclude_dir in self.config.exclude_dirs
            ):
                continue
            if any(
                exclude.match(str(file_path)) for exclude in exclude_file_patterns
            ):
                continue
            if str(file_path) in self.config.exclude_files:
                continue
            try:
                content = file_path.read_text(encoding='utf-8') # fix:  использование одинарных кавычек
                yield file_path, content
            except Exception as ex:
                logger.error(f'Ошибка при чтении файла {file_path} {ex}') # fix:  использование f-string
                yield None, None

    def _remove_outer_quotes(self, response: str) -> str:
        """
        Удаляет внешние кавычки в начале и в конце строки, если они присутствуют.

        :param response: Ответ модели, который необходимо обработать.
        :type response: str
        :return: Очищенный контент как строка.
        :rtype: str

        :example:
            Если строка '```md some content ```' будет передана в функцию,
            результат будет ' some content '.
        """
        try:
            response = response.strip()
        except Exception as ex:
            logger.error(f'Exception in `remove_outer_quotes()` {ex}') # fix:  использование f-string
            return ''
        if response.startswith(('```python', '```mermaid')):
            return response

        config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json') # fix:  j_loads_ns
        for prefix in config.remove_prefixes:
            if response.lower().startswith(prefix.lower()):
                return response.removeprefix(prefix).removesuffix('```').strip() # fix:  использование одинарных кавычек
        return response

    async def _save_response(self, file_path: Path, response: str, model_name: str) -> bool:
        """
        Сохранение ответа модели в файл с добавлением суффикса.

        :param file_path: Исходный путь к файлу, в который будет записан ответ.
        :type file_path: Path
        :param response: Ответ модели, который необходимо сохранить.
        :type response: str
        :param model_name: Имя модели, использованной для генерации ответа.
        :type model_name: str
        :return: True, если файл успешно сохранён, иначе False.
        :rtype: bool
        """
        try:
            output_directory = getattr(self.config.output_directory, self.role) # fix:  использование одинарных кавычек

            target_dir = (
                f'docs/{output_directory}'
                .replace('<model>', model_name)
                .replace('<lang>', self.lang)
            )
            file_path = str(file_path).replace('src', target_dir) # fix:  использование одинарных кавычек

            suffix_map = {
                'code_checker': '.md',
                'doc_writer_md': '.md',
                'doc_writer_rst': '.rst',
                'doc_writer_html': '.html',
                'code_explainer_md': '.md',
                'code_explainer_html': '.html',
                'pytest': '.md',
            }
            suffix = suffix_map.get(self.role, '.md') # fix:  использование одинарных кавычек

            export_path = Path(file_path)
            if export_path.suffix == '.md' and suffix == '.md': # fix:  использование одинарных кавычек
                export_path = Path(f'{file_path}')
            else:
                export_path = Path(f'{file_path}{suffix}') # fix:  использование одинарных кавычек

            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_text(response, encoding='utf-8') # fix:  использование одинарных кавычек
            logger.success(f'{export_path.name}') # fix:  использование f-string
            return True
        except Exception as ex:
            logger.critical(f'Ошибка сохранения файла: {export_path=} {ex}', exc_info=True) # fix:  использование f-string
            return False

    def run(self, start_file_number: int = 1):
        """
        Запуск процесса обработки файлов.

        :param start_file_number: Номер файла, с которого начинать обработку.
        :type start_file_number: int, optional
        """
        signal.signal(
            signal.SIGINT, self._signal_handler
        )  # Обработка прерывания (Ctrl+C)
        asyncio.run(self.process_files(start_file_number=start_file_number)) # fix:  вызов асинхронной функции

    def _signal_handler(self, signal, frame):
        """
        Обработка прерывания выполнения.
        """
        logger.debug('Процесс был прерван', text_color='red') # fix:  использование одинарных кавычек
        sys.exit(0)

def main():
    """
    Основная функция для запуска.
    """
    args = parse_args()
    assistant = CodeAssistant(**args)
    assistant.run(start_file_number=args['start_file_number']) # fix:  использование одинарных кавычек

def parse_args():
    """
    Разбор аргументов командной строки.

    :return: Словарь с аргументами командной строки.
    :rtype: dict
    """
    parser = argparse.ArgumentParser(description='Ассистент для программистов') # fix:  использование одинарных кавычек
    parser.add_argument(
        '--role',
        type=str,
        default='code_checker',
        help='Роль для выполнения задачи', # fix:  использование одинарных кавычек
    )
    parser.add_argument('--lang', type=str, default='ru', help='Язык выполнения') # fix:  использование одинарных кавычек
    parser.add_argument(
        '--model',
        nargs='+',
        type=str,
        default=['gemini'],
        help='Список моделей для инициализации', # fix:  использование одинарных кавычек
    )
    parser.add_argument(
        '--start-dirs',
        nargs='+',
        type=str,
        default=[],
        help='Список директорий для обработки', # fix:  использование одинарных кавычек
    )
    parser.add_argument(
        '--start-file-number',
        type=int,
        default=1,
        help='С какого файла делать обработку. Полезно при сбоях', # fix:  использование одинарных кавычек
    )
    return vars(parser.parse_args())

if __name__ == '__main__':
    """
    Код запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.
    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки во время работы программы.
    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.
    """
    config_path: Path = (
        gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json' # fix:  использование одинарных кавычек
    )

    while True:
        config: SimpleNamespace = j_loads_ns(config_path)  # Загрузка конфигурации # fix:  j_loads_ns
        for lang in config.languages:
            for role in config.roles:
                logger.debug(f'Start role: {role}, lang: {lang}', None, False) # fix:  использование f-string
                assistant_direct = CodeAssistant(
                    role=role,
                    lang=lang,
                    model=['gemini'], # fix:  использование одинарных кавычек
                )
                assistant_direct.run(start_file_number=1)  # fix:  убрали async
                config: SimpleNamespace = j_loads_ns(config_path) # fix:  j_loads_ns