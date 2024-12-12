# Анализ кода модуля `assistant.py`

**Качество кода: 7/10**
-  **Плюсы:**
    - Код разбит на логические блоки, что облегчает понимание.
    - Используются классы для организации кода.
    - Присутствует базовая обработка ошибок через `try-except`.
    - Логирование с использованием `src.logger.logger`.
    - Применяются `asyncio` для асинхронных операций.
-  **Минусы:**
    - Не все функции и методы имеют подробную документацию в формате RST.
    - Избыточное использование `try-except` блоков в некоторых местах.
    - Не везде используется `logger.error` для логирования ошибок.
    - Некоторые комментарии не соответствуют стандарту RST.
    - Есть устаревшие комментарии `# <- ~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG`.
    - Используются `...` для обозначения не реализованного кода, что не является хорошей практикой.
    - Есть неиспользуемые переменные.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить подробные docstring в формате RST для всех функций, методов и классов.
    - Переписать комментарии в стиле RST, например, с использованием `:param`, `:return`, `:raises`.

2.  **Обработка ошибок**:
    - Заменить избыточные `try-except` блоки на более целенаправленную обработку с использованием `logger.error`.
    - Убрать `...` и добавить логику обработки ошибок.

3.  **Логирование**:
    - Использовать `logger.debug`, `logger.info`, `logger.warning`, `logger.error` в зависимости от уровня важности события.

4.  **Импорты**:
     - Все импорты должны быть в верхней части файла.
     - Проверить и добавить отсутствующие импорты, если нужно.

5.  **Рефакторинг**:
    - Убрать магические строки и числа, вынести в константы или параметры.
    - Переменные должны соответствовать PEP8.
    - Избавиться от неиспользуемых переменных.

6. **Оформление**:
   - Переписать docstring в reStructuredText
   - Всегда используйте одинарные кавычки (`'`) в Python коде

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов
=========================================================================================

:class:`CodeAssistant`, читает файлы кода, отдает код в модели, модель обрабатывает код и возвращает его в класс, класс сохраняет результат
в директории `docs/gemini`. В зависимости от роли файлы сохраняются в

Пример использования
--------------------

Пример использования класса :class:`CodeAssistant`:
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
from typing import Iterator, List, Optional, Any
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
from src.utils.printer import pprint
from src.utils.path import get_relative_path
from src.logger.logger import logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary

MODE = 'dev'


class CodeAssistant:
    """
    Класс для работы ассистента программиста с моделями ИИ.

    :param role: Роль ассистента (например, 'code_checker', 'doc_writer_rst').
    :type role: str
    :param lang: Язык для обработки (например, 'ru', 'en').
    :type lang: str
    :param model: Список моделей для использования (например, ['gemini', 'openai']).
    :type model: list
    :param start_dirs: Список начальных директорий для обработки.
    :type start_dirs: list[str] | list[Path]
    """

    role: str
    lang: str
    start_dirs: Path | str | list[Path] | list[str]
    base_path: Path
    config: SimpleNamespace
    gemini_model: GoogleGenerativeAI
    openai_model: OpenAIModel
    start_file_number: int

    def __init__(self, **kwargs):
        """
        Инициализирует ассистента с заданными параметрами.

        :param kwargs: Дополнительные параметры для инициализации.
            - `role`: Роль ассистента (по умолчанию 'doc_writer_rst').
            - `lang`: Язык для обработки (по умолчанию 'en' для 'pytest', иначе 'ne').
            - `model`: Список моделей для использования (по умолчанию ['gemini']).
            - `start_dirs`: Список начальных директорий для обработки (по умолчанию ['..']).
        :type kwargs: dict
        """
        self.role: str = kwargs.get('role', 'doc_writer_rst')
        self.lang: str = 'en' if self.role == 'pytest' else kwargs.get('lang', 'ne')
        self.models_list: list = kwargs.get('model', ['gemini'])
        self.start_dirs: list = kwargs.get('start_dirs', ['..'])
        self.base_path = gs.path.endpoints / 'hypo69' / 'code_assistant'
        self.config = j_loads_ns(self.base_path / 'code_assistant.json')
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs):
        """
        Инициализирует модели на основе заданных параметров.

        :param kwargs: Дополнительные параметры для инициализации моделей.
        :type kwargs: dict
        """
        if 'gemini' in self.models_list:
            self.gemini_model = GoogleGenerativeAI(
                model_name=self.config.gemini_model_name,
                api_key=gs.credentials.gemini.onela,
                **kwargs,
            )
        if 'openai' in self.models_list:
            self.openai_model = OpenAIModel(
                model_name='gpt-4o-mini',
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwargs,
            )

    @staticmethod
    def parse_args():
        """
        Разбирает аргументы командной строки.

        :return: Словарь с аргументами.
        :rtype: dict
        """
        parser = argparse.ArgumentParser(description='Ассистент для программистов')
        parser.add_argument(
            '--role',
            type=str,
            default='code_checker',
            help='Роль для выполнения задачи',
        )
        parser.add_argument('--lang', type=str, default='ru', help='Язык выполнения')
        parser.add_argument(
            '--model',
            nargs='+',
            type=str,
            default=['gemini'],
            help='Список моделей для инициализации',
        )
        parser.add_argument(
            '--start-dirs',
            nargs='+',
            type=str,
            default=[],
            help='Список директорий для обработки',
        )
        parser.add_argument(
            '--start-file-number',
            type=int,
            default=1,
            help='С какого файла делать обработку. Полезно при сбоях',
        )
        return vars(parser.parse_args())

    @property
    def system_instruction(self) -> str | bool:
        """
        Читает инструкцию из файла.

        :return: Содержимое файла инструкции или `False` в случае ошибки.
        :rtype: str | bool
        """
        try:
            return Path(
                gs.path.src
                / 'ai'
                / 'prompts'
                / 'developer'
                / f'{self.role}_{self.lang}.md'
            ).read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error(f'Ошибка при чтении файла инструкции: {ex}', exc_info=True)  # Сохраняем информацию об исключении
            return False

    @property
    def code_instruction(self) -> str | bool:
        """
        Читает инструкцию для кода.

        :return: Содержимое файла инструкции или пустая строка в случае ошибки.
        :rtype: str | bool
        """
        try:
            return Path(
                self.base_path
                / 'instructions'
                / f'instruction_{self.role}_{self.lang}.md'
            ).read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error(f'Ошибка при чтении файла инструкции: {ex}', exc_info=True)  # Сохраняем информацию об исключении
            return ''

    @property
    def translations(self) -> SimpleNamespace:
        """
        Загружает переводы для ролей и языков.

        :return: Объект SimpleNamespace с переводами.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(
            gs.path.endpoints
            / 'hypo69'
            / 'code_assistant'
            / 'translations'
            / 'translations.json'
        )

    async def process_files(self, start_file_number: Optional[int] = 1):
        """
        Компилирует, отправляет запрос и сохраняет результат.

        :param start_file_number: Номер файла, с которого начать обработку.
        :type start_file_number: int, optional
        """
        def send_file(file_path: Path) -> bool:
            """
            Отправляет файл в модель.

            :param file_path: Абсолютный путь к файлу, который нужно отправить.
            :type file_path: Path
            :return: `True`, если отправка прошла успешно, `False` в противном случае.
            :rtype: bool
            """
            try:
                if file_path.name in ('__init__.py', 'header.py'):
                    logger.info(f'Пропущен файл: {file_path}')
                    return False

                file_name = None
                if not file_name:
                    if 'src' in file_path.parts:
                        index = file_path.parts.index('src')
                        relative_path = Path(*file_path.parts[index:])
                        file_name = 'src--' + '--'.join(relative_path.parts[1:-1]) + '--' + relative_path.stem
                    else:
                        file_name = file_path.stem

                response = self.gemini_model.upload_file(file_path)

                if response:
                    pprint(response, text_color='light_gray')
                    if hasattr(response, 'url'):
                        return response.url
                return False
            except Exception as ex:
                logger.error(f'Ошибка при отправке файла: {ex}', exc_info=True)  # Сохраняем информацию об исключении
                return False

        for i, (file_path, content) in enumerate(self._yield_files_content()):
            if not all((file_path, content)):
                continue
            if i < start_file_number:
                continue
            if file_path and content:
                # send_file(file_path)  # Отправить в модель файл
                content_request = self._create_request(file_path, content)
                response = await self.gemini_model.ask(content_request)

                if response:
                    response = self._remove_outer_quotes(response)

                    if not await self._save_response(file_path, response, 'gemini'):
                        logger.error(f'Файл {file_path} не был сохранен')
                        continue
                    pprint(f'Обработан файл номер: {i + 1}', text_color='yellow')
                else:
                    logger.error('Ошибка ответа модели', exc_info=True)  # Сохраняем информацию об исключении
                    continue

            await asyncio.sleep(20)

    def _create_request(self, file_path: str, content: str) -> str:
        """
        Создает запрос с учетом роли и языка.

        :param file_path: Путь к файлу.
        :type file_path: str
        :param content: Содержимое файла.
        :type content: str
        :return: Строка запроса.
        :rtype: str
        """
        try:
            roles_translations: SimpleNamespace = getattr(self.translations.roles, self.role, 'doc_writer_md')
            role_description_translated: str = getattr(roles_translations, self.lang, 'Your specialization is documentation creation in the `MD` format')
            file_location_translated: str = getattr(self.translations.file_location_translated, self.lang, 'Path to file: ')

            content_request: dict = {
                'role': f'{role_description_translated}',
                'output_language': self.lang,
                f'{file_location_translated}': get_relative_path(file_path, 'hypotez'),
                'instruction': self.code_instruction or '',
                'input_code': f'```{content}```',
            }
        except Exception as ex:
            logger.error(f'Ошибка в составлении запроса: {ex}', exc_info=True)  # Сохраняем информацию об исключении
            return content
        return str(content_request)

    def _yield_files_content(
        self,
        start_dirs: List[Path] = [gs.path.src],
    ) -> Iterator[tuple[Path, str]]:
        """
        Генерирует пути файлов и их содержимое по указанным шаблонам.

        :param start_dirs: Список директорий для обхода.
        :type start_dirs: list[Path]
        :return: Итератор кортежей из пути файла и его содержимого.
        :rtype: Iterator[tuple[Path, str]]
        """
        try:
            exclude_file_patterns = [
                re.compile(pattern) for pattern in self.config.exclude_file_patterns
            ]
        except Exception as ex:
            logger.error(f'Не удалось скомпилировать регулярки из списка: {self.config.exclude_file_patterns=}, {ex}', exc_info=True)  # Сохраняем информацию об исключении
        include_file_patterns = self.config.include_files
        for start_dir in start_dirs:
            for file_path in start_dir.rglob('*'):
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
                    content = file_path.read_text(encoding='utf-8')
                    yield file_path, content
                    # make_summary( docs_dir = start_dir.parent / 'docs' )  # DEBUG
                except Exception as ex:
                    logger.error(f'Ошибка при чтении файла: {ex}', exc_info=True)
                    yield None, None

    async def _save_response(self, file_path: Path, response: str, model_name: str) -> bool:
        """
        Сохраняет ответ модели в файл с добавлением суффикса.

        :param file_path: Исходный путь к файлу, в который будет записан ответ.
        :type file_path: Path
        :param response: Ответ модели, который необходимо сохранить.
        :type response: str
        :param model_name: Имя модели, использованной для генерации ответа.
        :type model_name: str
        :return: `True`, если сохранение прошло успешно, `False` в противном случае.
        :rtype: bool
        """
        try:
            output_directory = getattr(self.config.output_directory, self.role)

            target_dir = (
                f'docs/{output_directory}'
                .replace('<model>', model_name)
                .replace('<lang>', self.lang)
            )

            file_path = str(file_path).replace('src', target_dir)

            suffix_map = {
                'code_checker': '.md',
                'doc_writer_md': '.md',
                'doc_writer_rst': '.rst',
                'doc_writer_html': '.html',
                'code_explainer_md': '.md',
                'code_explainer_html': '.html',
                'pytest': '.md',
            }
            suffix = suffix_map.get(self.role, '.md')

            export_path = Path(f'{file_path}{suffix}')
            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_text(response, encoding='utf-8')
            pprint(f'Ответ модели сохранен в: {export_path}', text_color='green')
            return True

        except Exception as ex:
            logger.critical(f'Ошибка сохранения файла: {export_path=}, {ex}', exc_info=True)
            return False

    def _remove_outer_quotes(self, response: str) -> str:
        """
        Удаляет внешние кавычки в начале и в конце строки, если они присутствуют.

        :param response: Ответ модели, который необходимо обработать.
        :type response: str
        :return: Очищенный контент как строка.
        :rtype: str
        """
        try:
            response = response.strip()
        except Exception as ex:
            logger.error('Ошибка в `remove_outer_quotes()`', exc_info=True)  # Сохраняем информацию об исключении
            return ''

        if response.startswith(('```python', '```mermaid')):
            return response

        config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json')
        for prefix in config.remove_prefixes:
            if response.lower().startswith(prefix.lower()):
                return response.removeprefix(prefix).removesuffix('```').strip()

        return response

    def run(self, start_file_number: int = 1):
        """
        Запускает процесс обработки файлов.

        :param start_file_number: Номер файла, с которого начать обработку.
        :type start_file_number: int
        """
        signal.signal(
            signal.SIGINT, self._signal_handler
        )
        asyncio.run(self.process_files(start_file_number=start_file_number))

    def _signal_handler(self, signal, frame):
        """
        Обрабатывает прерывание выполнения.
        """
        pprint('Процесс был прерван', text_color='red')
        sys.exit(0)


def main():
    """
    Основная функция для запуска.
    """
    args = CodeAssistant.parse_args()
    assistant = CodeAssistant(**args)
    assistant.run(start_file_number=args['start_file_number'])


if __name__ == '__main__':
    """
    Код запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.
    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки во время работы программы.
    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.
    """
    config_path: Path = (
        gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json'
    )

    while True:
        config: SimpleNamespace = j_loads_ns(config_path)
        args = config.argparse

        for lang in args.languages:
            for role in args.roles:
                logger.debug(f'Запуск role: {role}, lang: {lang}')

                assistant_direct = CodeAssistant(
                    role=role,
                    lang=lang,
                    model=['gemini'],
                    start_dirs=['..'],
                )
                asyncio.run(assistant_direct.process_files(start_file_number=1))

                config: SimpleNamespace = j_loads_ns(config_path)
                args = config.argparse
```