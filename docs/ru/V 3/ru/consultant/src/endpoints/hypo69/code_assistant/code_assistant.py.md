## Анализ кода модуля `code_assistant`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Хорошая структурированность кода.
  - Использование аннотаций типов.
  - Наличие документации к большинству методов и классов.
  - Использование `logger` для логирования.
- **Минусы**:
  - Не везде используется `logger.error` с `exc_info=True` для полноценного логирования ошибок.
  - Смешанный стиль кавычек (и одинарные, и двойные).
  - Есть участки кода с `...`, требующие доработки.
  - Некоторые участки кода требуют более подробных комментариев.

**Рекомендации по улучшению**:

1.  **Приведение к единому стилю кавычек**:
    - Заменить все двойные кавычки на одинарные, чтобы соответствовать стандарту.

2.  **Более полное логирование ошибок**:
    - В блоках `except` использовать `logger.error(..., exc_info=True)` для вывода полной трассировки ошибок.

3.  **Документирование и завершение кода с `...`**:
    - Заменить `...` на полноценную реализацию или добавить заглушку с комментарием о необходимости доработки.

4.  **Улучшение комментариев**:
    - Добавить больше контекста в комментариях, особенно там, где используются общие слова вроде "получение" или "отправка".
    - Уточнить, какие данные "проверяются", "извлекаются" или "выполняются".

5.  **Использование `j_loads` и `j_loads_ns`**:
    - Убедиться, что все JSON-файлы загружаются с использованием `j_loads` или `j_loads_ns` из `src.utils.jjson`.

6.  **Улучшение обработки исключений в `_initialize_models`**:
    - Добавить конкретный тип исключения в `except` блок для более точной обработки ошибок.

7. **Заменить  `str(content_request)` на `json.dumps(content_request)`**
    -  В методе `_create_request` необходимо преобразовывать словарь `content_request` в JSON-строку с использованием `json.dumps(content_request)`, чтобы обеспечить корректный формат запроса.

**Оптимизированный код**:

```python
## \file /src/endpoints/hypo69/code_assistant/code_assistant.py
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

.. module:: src.endpoints.hypo69.code_assistant.code_assistant
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
import os
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace
import signal
import time
import re
import fnmatch
import json # Import json

import header
from header import __root__
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.path import get_relative_path
from src.logger.logger import logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary
from src import USE_ENV

class Config:
    """
    Конфигурационный класс для хранения общих параметров и настроек.
    """
    ...
    base_path:Path = __root__ / 'src' / 'endpoints' / 'hypo69' / 'code_assistant'
    config: SimpleNamespace = j_loads_ns(base_path / 'code_assistant.json')
    role: str = 'doc_writer_md'
    lang: str = 'ru'
    system_instruction:str = ''

    gemini:SimpleNamespace = SimpleNamespace(**{
        'model_name': os.getenv('GEMINI_MODEL') if USE_ENV else config.gemini_model_name or None,
        'api_key': os.getenv('GEMINI_API_KEY') if USE_ENV else gs.credentials.gemini.onela or None,
        'response_mime_type': 'text/plain',
    })

class CodeAssistant:
    """
    Класс для работы ассистента программиста с моделями ИИ.

    Args:
        role (Optional[str]): Роль для выполнения задачи. Defaults to 'doc_writer_md'.
        lang (Optional[str]): Язык выполнения. Defaults to 'en'.
        models_list (Optional[list[str,str] | str]): Список моделей для инициализации. Defaults to ["gemini"].
        system_instruction (Optional[str | Path]): Инструкция для системы. Можно отправить текст или путь к файлу. Defaults to None.
        **kwards: Дополнительные аргументы для инициализации моделей.
    """

    role: str
    lang: str
    base_path:Path = __root__ / 'src' / 'endpoints' / 'hypo69' / 'code_assistant'
    config: SimpleNamespace = j_loads_ns(base_path / 'code_assistant.json')
    gemini_model: GoogleGenerativeAI
    openai_model: OpenAIModel


    def __init__(self,
                 role:Optional[str] = 'doc_writer_md',
                 lang: Optional[str] = 'en',
                 models_list: Optional[list[str,str] | str] = ['gemini'],
                 system_instruction:Optional[str | Path] = None,
                 **kwards):
        """
        Инициализация ассистента с заданными параметрами.

        Args:
            role (Optional[str]): Роль для выполнения задачи. Defaults to 'doc_writer_md'.
            lang (Optional[str]): Язык выполнения. Defaults to 'en'.
            models_list (Optional[list[str,str] | str]): Список моделей для инициализации. Defaults to ['gemini'].
            system_instruction (Optional[str | Path]): Инструкция для системы. Можно отправить текст или путь к файлу. Defaults to None.
            **kwards: Дополнительные аргументы для инициализации моделей.
        """
        Config.role = role
        Config.lang = lang

        if system_instruction:
            if isinstance(system_instruction, str):
                Config.system_instruction = system_instruction

            elif isinstance(system_instruction, Path):
                try:
                    Config.system_instruction = Path(system_instruction).read_text(encoding='UTF-8')
                except Exception as ex:
                    logger.error(f'Ошибка чтения инструкции из файла {system_instruction}', ex, exc_info=True)
                    ... # TODO: Обработать ошибку чтения файла с инструкцией
            else:
                logger.error(f'Ошибка формата инструкции\\n {print(system_instruction)}\\n system_instruction type {type(system_instruction)}', None, exc_info=True)
                ... # TODO: Обработать неверный формат инструкции
        else:
            Config.system_instruction = Path(gs.path.src / 'ai' / 'prompts' / 'developer' / f'CODE_RULES.{lang}.MD').read_text(encoding='UTF-8')

        self._initialize_models( list( models_list ), **kwards)

    def _initialize_models(self, models_list:list, **kwards) -> bool:
        """
        Инициализация моделей на основе заданных параметров.

        Args:
            models_list (list[str]): Список моделей для инициализации.
            **kwards: Дополнительные аргументы для инициализации моделей.

        Returns:
            bool: Успешность инициализации моделей.

        Raises:
            Exception: Если произошла ошибка при инициализации моделей.
        """

        if 'gemini' in models_list:
            # Определение значений по умолчанию

            default_response_mime_type = 'text/plain'

            try:

                # Фильтрация kwards для удаления известных аргументов
                filtered_kwargs = {
                    k: v for k, v in kwards.items()
                    if k not in ('model_name', 'api_key', 'generation_config', 'system_instruction')
                }

                # Создание экземпляра модели Gemini
                self.gemini_model = GoogleGenerativeAI(
                    model_name = kwards.get('model_name', Config.gemini.model_name),   # Значение из kwards имеет приоритет,
                    api_key = kwards.get('api_key', Config.gemini.api_key),
                    system_instruction = kwards.get('system_instruction', Config.system_instruction),
                    generation_config = kwards.get('generation_config', {'response_mime_type': default_response_mime_type}),
                    **filtered_kwargs,
                )
                ... # TODO: Добавить логику постобработки после инициализации модели Gemini
                return True
            except Exception as ex:
                logger.error('Ошибка при инициализации Gemini:', ex, exc_info=True)
                return False

    @property
    def code_instruction(self) -> str | bool:
        """Чтение инструкции для кода."""
        try:
            return Path(
                gs.path.endpoints
                / 'hypo69'
                / 'code_assistant'
                / 'instructions'
                / f'instruction_{Config.role}_{Config.lang}.md'
            ).read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error('Error reading instruction file', ex, exc_info=True)
            ... # TODO: Добавить обработку ошибки чтения файла инструкций
            return ''

    @property
    def translations(self) -> SimpleNamespace:
        """Загрузка переводов для ролей и языков."""
        return j_loads_ns(
            gs.path.endpoints
            / 'hypo69'
            / 'code_assistant'
            / 'translations'
            / 'translations.json'
        )

    def send_file(self, file_path: Path) -> bool:
        """
        Отправка файла в модель.

        Args:
            file_path (Path): Абсолютный путь к файлу, который нужно отправить.
            file_name (Optional[str]): Имя файла для отправки. Если не указано и 'src' отсутствует, используется имя файла без изменений.

        Returns:
            bool: Успешность выполнения операции.
        """
        try:
            #Отправка файла в модель
            response = self.gemini_model.upload_file(file_path)

            if response:
                if hasattr(response, 'url'):
                    return response.url

            return
        except Exception as ex:
            logger.error('Ошибка при отправке файла: ', ex, exc_info=True)
            ... # TODO: Добавить обработку ошибки отправки файла
            return


    async def process_files(self, start_dirs:str|Path|list[str,str]|list[Path,Path] = None, start_file_number: Optional[int] = 1 ) -> bool:\n        """компиляция, отправка запроса и сохранение результата.\n       \n        """
        if not start_dirs:
           start_dirs = self.config.start_dirs
        if not start_dirs:
            logger.error("Ошибка иницаилизации стартовой директории")
            ...
            return 
        start_dirs = start_dirs if isinstance(start_dirs,list) else [start_dirs]\n        for process_driectory in start_dirs:\n            logger.info(f"Start {process_driectory=}")\n
            for i, (file_path, content) in enumerate(self._yield_files_content(process_driectory)):\n                if not any((file_path, content)):    # <- ошибка чтения файла\n                    continue\n                if i < start_file_number: # <- старт с номера файла\n                    continue\n                if file_path and content:\n                    # send_file(file_path) # <- отправить в модель файл\n                    content_request = self._create_request(file_path, content)\n                    response = await self.gemini_model.ask_async(content_request)\n

                    if response:\n                        response:str = self._remove_outer_quotes(response)\n                        if not await self._save_response(file_path, response, "gemini"):\n                            logger.error(f"Файл {file_path} \\n НЕ сохранился")\n                            ...\n                            continue\n                        logger.debug(f"Processed file number: {i + 1}", None, False)\n                        ...\n                    else:\n                        logger.error("Ошибка ответа модели", None, False)\n                        ...\n                        continue\n

                await asyncio.sleep(20) # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (change timeout)\n

    def _create_request(self, file_path: str, content: str) -> str:\n        """Создание запроса с учетом роли и языка."""\n        content_request = content\n        try:\n            roles_translations:SimpleNamespace = getattr(self.translations.roles, Config.role, \'doc_writer_md\')\n            role_description_translated:str = getattr(roles_translations, Config.lang, \'Your specialization is documentation creation in the `MD` format\')\n            file_location_translated:str = getattr(self.translations.file_location_translated, Config.lang, \'Path to file: \')\n
            content_request: dict = {\n                "role": f"{role_description_translated}",\n                "output_language": Config.lang,\n                f"{file_location_translated}": get_relative_path(file_path, "hypotez"),\n                "instruction": self.code_instruction or \'\',\n                "input_code": f"```{content}```",\n            }\n        except Exception as ex:\n            logger.error(f"Ошибка в составлении запроса ", ex, False)\n            ...\n            return content\n

        return json.dumps(content_request)\n

    def _yield_files_content(\n        self,\n        process_driectory: str| Path,\n    ) -> Iterator[tuple[Path, str]]:\n        """\n        Генерирует пути файлов и их содержимое по указанным шаблонам.\n

        Args:\n            process_driectory (Path | str): Абсолютный путь к стартовой директории\n
        Returns:\n            bool: Iterator\n

        """\n

        process_driectory:Path = process_driectory if isinstance(process_driectory, Path) else Path(process_driectory)\n        # Компиляция паттернов исключаемых файлов\n        try:\n            exclude_file_patterns = [\n                re.compile(pattern) for pattern in self.config.exclude_file_patterns\n            ]\n

        except Exception as ex:\n            logger.error(f"Не удалось скомпилировать регулярки из списка:/n{self.config.exclude_file_patterns=}\\n ",ex, exc_info=True)\n            ...\n        include_file_patterns = self.config.include_files\n

        # Итерация по всем файлам в директории\n        for file_path in process_driectory.rglob("*"):\n            # Проверка на соответствие шаблонам включения\n            if not any(\n                fnmatch.fnmatch(file_path.name, pattern)\n                for pattern in include_file_patterns\n            ): \n                continue\n

            # Прверка исключенных директорий\n            if any(\n                exclude_dir in file_path.parts\n                for exclude_dir in self.config.exclude_dirs\n            ):\n               continue\n

            # Проверка исключенных файлов по паттерну\n            if any(\n                exclude.match(str(file_path.name)) for exclude in exclude_file_patterns\n            ): \n                continue\n

            # Проверка конкретных исключенных файлов\n            if str(file_path.name) in self.config.exclude_files:\n                continue\n

            # Чтение содержимого файла\n            try:\n                content = file_path.read_text(encoding="utf-8")\n                yield file_path, content\n                # make_summary( docs_dir = start_dir.parent / \'docs\' )  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG  (create `summary.md`)\n            except Exception as ex:\n                logger.error(f"Ошибка при чтении файла {file_path}",ex, exc_info=True)\n                ...\n                yield None, None\n

            ...\n

    async def _save_response(self, file_path: Path, response: str, model_name: str) -> bool:\n        """Сохранение ответа модели в файл с добавлением суффикса.\n
        Метод сохраняет ответ модели в файл, добавляя к текущему расширению файла\n        дополнительный суффикс, определяемый ролью. \n        Args:\n            file_path (Path): Исходный путь к файлу, в который будет записан ответ.\n            response (str): Ответ модели, который необходимо сохранить.\n            model_name (str): Имя модели, использованной для генерации ответа.\n

        Raises:\n            OSError: Если не удаётся создать директорию или записать в файл.\n        """\n        try:\n

            # Получаем директорию для вывода в зависимости от роли\n            output_directory = getattr(self.config.output_directory, Config.role)\n

            # Формируем целевую директорию с учётом подстановки параметров <model> и <lang>\n            target_dir = (\n                f\'docs/{output_directory}\'\n                .replace(\'<model>\', model_name)\n                .replace(\'<lang>\', Config.lang)\n            )\n

            # Заменяем часть пути на целевую директорию\n            file_path = str(file_path).replace(\'src\', target_dir)\n

            # Определяем суффикс для добавления в зависимости от роли\n            suffix_map = {\n                'code_checker': '.md',\n                'doc_writer_md': '.md',\n                'doc_writer_rst': '.rst',\n                'doc_writer_html': '.html',\n                'code_explainer_md': '.md',\n                'code_explainer_html': '.html',\n                'pytest': '.md',\n            }\n            suffix = suffix_map.get(Config.role, '.md')  # По умолчанию используется .md\n

            export_path = Path(file_path)\n            if export_path.suffix == '.md' and suffix == '.md':\n              export_path = Path(f"{file_path}")\n            else:\n                export_path = Path(f"{file_path}{suffix}")\n

            export_path.parent.mkdir(parents=True, exist_ok=True)\n            export_path.write_text(response, encoding='utf-8')\n            logger.success(f"{export_path.name}")\n            return True\n

        except Exception as ex:\n            logger.critical(f'Ошибка сохранения файла: {export_path=}', ex, exc_info=True)\n            #sys.exit(0)\n            return False\n

    def _remove_outer_quotes(self, response: str) -> str:\n            """\n            Удаляет внешние кавычки в начале и в конце строки, если они присутствуют.\n

            :param response: Ответ модели, который необходимо обработать.\n            :type response: str\n            :return: Очищенный контент как строка.\n            :rtype: str\n

            :example:\n                Если строка '```md some content ```' будет передана в функцию,\n                результат будет ' some content '.\n

            """\n            try:\n                response = response.strip()\n            except Exception as ex:\n                logger.error("Exception in `remove_outer_quotes()`", ex, exc_info=True)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG\n                ...\n                return ''\n

            # Если строка начинается с '```python' или '```mermaid', возвращаем её без изменений. Это годный код\n            if response.startswith(('```python', '```mermaid')):\n                return response\n

            # Удаление маркера для известных форматов, если строка обрамлена в \'```\'\n            config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json')\n            for prefix in config.remove_prefixes:\n                # Сравнение с префиксом без учёта регистра\n                if response.lower().startswith(prefix.lower()):\n                    return response.removeprefix(prefix).removesuffix("```").strip()\n

            # Возврат строки без изменений, если условия не выполнены\n            return response\n

    def run(self, start_file_number: int = 1):\n        """Запуск процесса обработки файлов."""\n        signal.signal(\n            signal.SIGINT, self._signal_handler\n        )  # Обработка прерывания (Ctrl+C)\n        self.process_files(start_file_number)\n

    def _signal_handler(self, signal, frame):\n        """Обработка прерывания выполнения."""\n        logger.debug("Процесс был прерван", text_color="red")\n        sys.exit(0)\n

def parse_args():\n        """Разбор аргументов командной строки."""\n        parser = argparse.ArgumentParser(description="Ассистент для программистов")\n        parser.add_argument(\n            "--role",\n            type=str,\n            default="code_checker",\n            help="Роль для выполнения задачи",\n        )\n        parser.add_argument("--lang", type=str, default="ru", help="Язык выполнения")\n        parser.add_argument(\n            "--model",\n            nargs="+",\n            type=str,\n            default=["gemini"],\n            help="Список моделей для инициализации",\n        )\n        parser.add_argument(\n            "--start-dirs",\n            nargs="+",\n            type=str,\n            default=[],\n            help="Список директорий для обработки",\n        )\n        parser.add_argument(\n            "--start-file-number",\n            type=int,\n            default=1,\n            help="С какого файла делать обработку. Полезно при сбоях",\n        )\n        return vars(parser.parse_args())\n

def main():\n    """\n    Функция запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.\n    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки в файле `code_assistant.json` во время работы программы.\n    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.\n    """\n

    config_path: Path = (\n        gs.path.endpoints / "hypo69" / "code_assistant" / "code_assistant.json"\n    )\n

    while True:\n        # Загрузка конфигурации\n        config: SimpleNamespace = j_loads_ns(config_path)\n

        # Обработка файлов для каждой комбинации языков и ролей\n        for lang in config.languages:\n

            for role in config.roles:\n                logger.debug(f"Start role: {role}, lang: {lang}", None, False)\n

                assistant_direct = CodeAssistant(\n                    role = role,\n                    lang = lang,\n                    models_list = ["gemini"],\n                    #system_instruction = Config.system_instruction,\n

                )\n                asyncio.run( assistant_direct.process_files( start_dirs=config.start_dirs) )\n

                # Обновление конфигурации для учёта изменений во время выполнения\n                config: SimpleNamespace = j_loads_ns(config_path)\n

if __name__ == "__main__":\n     main()\n