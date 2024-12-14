# Анализ кода модуля `assistant.py`

**Качество кода:** 7/10
- **Плюсы:**
    - Код структурирован в классы и функции, что способствует его пониманию и поддержке.
    - Используются асинхронные операции, что позволяет эффективно обрабатывать файловые операции и запросы к API.
    - Присутствует обработка ошибок, хотя местами она требует улучшения.
    - Код использует кастомные `j_loads`, `j_loads_ns` для работы с JSON, что соответствует требованиям.
    - Используется `logger` для логирования, что полезно для отладки.
- **Минусы:**
    - Не все функции и классы имеют docstring в формате reStructuredText (RST).
    - В некоторых местах используются стандартные блоки `try-except`, которые можно заменить на `logger.error`.
    - Есть дублирование кода, особенно в части обработки ошибок.
    - Некоторые комментарии не соответствуют стилю RST.
    - В некоторых местах используется многоточие `...` для обозначения точек остановки, что не всегда наглядно.
    - Не хватает проверки на наличие атрибутов у объекта `response` перед обращением.

**Рекомендации по улучшению:**

1. **Документация:**
   - Добавить docstring в формате RST для всех классов, методов и функций.
   - Обновить комментарии в коде, чтобы они соответствовали стилю RST.
   - Использовать конкретные формулировки в комментариях.
2. **Обработка ошибок:**
   - Заменить избыточные блоки `try-except` на использование `logger.error`.
   - Проверять наличие атрибутов у объектов, прежде чем обращаться к ним.
3. **Рефакторинг:**
   - Вынести повторяющийся код в отдельные функции или методы.
   - Упростить логику обработки путей и имен файлов.
   - Улучшить читаемость кода, особенно в сложных участках.
4. **Улучшения:**
   - Проверять response на наличие атрибутов перед обращением
   - Избегать использования `sys.exit(0)` в блоках `except`, вместо этого возвращать `False` или использовать логирование ошибок.
   - Рассмотреть возможность использования enum для ролей, языков и моделей, чтобы избежать опечаток.

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов
=========================================================================================

:class:`CodeAssistant`, читает файлы кода, отдает код в модели, модель обрабатывает код и возвращает его в класс, класс сохраняет результат
в директории `docs/gemini`. В зависимости от роли файлы сохраняются в разные поддиректории.

Пример использования
--------------------

Пример использования класса `CodeAssistant`:

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

MODE = "dev"

class CodeAssistant:
    """
    Класс для работы ассистента программиста с моделями ИИ.

    :param role: Роль ассистента (например, 'code_checker', 'doc_writer_rst').
    :type role: str
    :param lang: Язык, на котором будет работать ассистент (например, 'ru', 'en').
    :type lang: str
    :param model: Список моделей, которые будут использоваться (например, ['gemini'], ['openai']).
    :type model: list[str]
    :param start_dirs: Список директорий, с которых начнется поиск файлов для обработки.
    :type start_dirs: list[str]
    """
    role: str
    lang: str
    start_dirs: Path | str | list[Path] | list[str]
    base_path: Path
    config: SimpleNamespace
    gemini_model: Optional[GoogleGenerativeAI]
    openai_model: Optional[OpenAIModel]
    start_file_number: int

    def __init__(self, **kwargs):
        """
        Инициализация ассистента с заданными параметрами.

        :param kwargs: Параметры для инициализации ассистента.
        :type kwargs: dict
        """
        self.role:str = kwargs.get("role", "doc_writer_rst")
        self.lang:str = "en" if self.role == "pytest" else kwargs.get("lang", "ru")
        self.models_list:list = kwargs.get("model", ["gemini"])
        self.start_dirs:list = kwargs.get("start_dirs", [".."])
        self.base_path = gs.path.endpoints / "hypo69" / "code_assistant"
        self.config = j_loads_ns(self.base_path / "code_assistant.json")
        self.gemini_model: Optional[GoogleGenerativeAI] = None
        self.openai_model: Optional[OpenAIModel] = None
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs):
        """
        Инициализация моделей на основе заданных параметров.

        :param kwargs: Параметры для инициализации моделей.
        :type kwargs: dict
        """
        if "gemini" in self.models_list:
            try:
                self.gemini_model = GoogleGenerativeAI(
                    model_name=self.config.gemini_model_name,
                    api_key=gs.credentials.gemini.onela,
                    **kwargs,
                )
            except Exception as ex:
                 logger.error(f"Ошибка инициализации Gemini: {ex}")
        if "openai" in self.models_list:
            try:
                self.openai_model = OpenAIModel(
                    model_name="gpt-4o-mini",
                    assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                    **kwargs,
                )
            except Exception as ex:
                logger.error(f"Ошибка инициализации OpenAI: {ex}")

    @staticmethod
    def parse_args() -> dict:
        """
        Разбор аргументов командной строки.

        :return: Словарь аргументов.
        :rtype: dict
        """
        parser = argparse.ArgumentParser(description="Ассистент для программистов")
        parser.add_argument(
            "--role",
            type=str,
            default="code_checker",
            help="Роль для выполнения задачи",
        )
        parser.add_argument("--lang", type=str, default="ru", help="Язык выполнения")
        parser.add_argument(
            "--model",
            nargs="+",
            type=str,
            default=["gemini"],
            help="Список моделей для инициализации",
        )
        parser.add_argument(
            "--start-dirs",
            nargs="+",
            type=str,
            default=[],
            help="Список директорий для обработки",
        )
        parser.add_argument(
            "--start-file-number",
            type=int,
            default=1,
            help="С какого файла делать обработку. Полезно при сбоях",
        )
        return vars(parser.parse_args())

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
                / "ai"
                / "prompts"
                / "developer"
                / f"{self.role}_{self.lang}.md"
            ).read_text(encoding="UTF-8")
        except Exception as ex:
            logger.error(f"Ошибка при чтении файла инструкции: {ex}")
            return False

    @property
    def code_instruction(self) -> str | bool:
        """
        Чтение инструкции для кода.

        :return: Инструкция для кода в виде строки или '' в случае ошибки.
        :rtype: str | bool
        """
        try:
            return Path(
                self.base_path
                / "instructions"
                / f"instruction_{self.role}_{self.lang}.md"
            ).read_text(encoding="UTF-8")
        except Exception as ex:
            logger.error(f"Ошибка при чтении файла инструкции для кода: {ex}")
            return ''

    @property
    def translations(self) -> SimpleNamespace:
        """
        Загрузка переводов для ролей и языков.

        :return: Переводы в виде SimpleNamespace.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(
            gs.path.endpoints
            / "hypo69"
            / "code_assistant"
            / "translations"
            / "translations.json"
        )

    async def process_files(self, start_file_number: Optional[int] = 1):
        """
        Компилирует, отправляет запрос и сохраняет результат.

        :param start_file_number: Номер файла, с которого начать обработку.
        :type start_file_number: Optional[int]
        """
        async def send_file(file_path: Path) -> str | bool:
             """
             Отправляет файл в модель.

             :param file_path: Абсолютный путь к файлу, который нужно отправить.
             :type file_path: Path
             :return: URL ответа или False в случае ошибки.
             :rtype: str | bool
             """
             file_name = None
             try:
                 if file_path.name in  ('__init__.py','header.py'):
                     logger.info(f'Пропускаю файл: {file_path}')
                     return False
                 if not file_name:
                     if 'src' in file_path.parts:
                         index = file_path.parts.index('src')
                         relative_path = Path(*file_path.parts[index:])
                         file_name = 'src--' + '--'.join(relative_path.parts[1:-1]) + '--' + relative_path.stem
                     else:
                         file_name = file_path.stem
                 if self.gemini_model:
                     response = self.gemini_model.upload_file(file_path)
                     if response:
                         pprint(response, text_color='light_gray')
                         if hasattr(response, 'url'):
                             return response.url
                     return False
                 else:
                     logger.error('Модель Gemini не инициализирована')
                     return False
             except Exception as ex:
                 logger.error(f'Ошибка при отправке файла: {ex}')
                 return False
        for i, (file_path, content) in enumerate(self._yield_files_content()):
            if not any((file_path, content)):
                continue
            if i < start_file_number:
                continue
            if file_path and content:
                content_request = self._create_request(file_path, content)
                if self.gemini_model:
                    response = await self.gemini_model.ask(content_request)
                    if response:
                        response = self._remove_outer_quotes(response)
                        if not await self._save_response(file_path, response, "gemini"):
                            logger.error(f"Файл {file_path} не сохранился")
                            continue
                        pprint(f"Обработан файл номер: {i + 1}", text_color="yellow")
                    else:
                        logger.error("Ошибка ответа модели")
                        continue
                else:
                    logger.error("Модель Gemini не инициализирована")
                    continue

            await asyncio.sleep(20)

    def _create_request(self, file_path: str, content: str) -> str:
        """
        Создание запроса с учетом роли и языка.

        :param file_path: Путь к файлу.
        :type file_path: str
        :param content: Содержимое файла.
        :type content: str
        :return: Строка запроса.
        :rtype: str
        """
        content_request = content
        try:
            roles_translations:SimpleNamespace = getattr(self.translations.roles, self.role, 'doc_writer_md')
            role_description_translated:str = getattr(roles_translations, self.lang, 'Your specialization is documentation creation in the `MD` format')
            file_location_translated:str = getattr(self.translations.file_location_translated, self.lang, 'Path to file: ')
            content_request: dict = {
                "role": f"{role_description_translated}",
                "output_language": self.lang,
                f"{file_location_translated}": get_relative_path(file_path, "hypotez"),
                "instruction": self.code_instruction or '',
                "input_code": f"```{content}```",
            }
        except Exception as ex:
            logger.error(f"Ошибка в составлении запроса: {ex}")
            return content

        return str(content_request)

    def _yield_files_content(
        self,
        start_dirs: List[Path] = [gs.path.src],
    ) -> Iterator[tuple[Optional[Path], Optional[str]]]:
        """
        Генерирует пути файлов и их содержимое по указанным шаблонам.

        :param start_dirs: Список директорий для обхода.
        :type start_dirs: List[Path]
        :return: Итератор кортежей из пути файла и его содержимого.
        :rtype: Iterator[tuple[Optional[Path], Optional[str]]]
        """
        try:
            exclude_file_patterns = [
                re.compile(pattern) for pattern in self.config.exclude_file_patterns
            ]
        except Exception as ex:
            logger.error(f"Не удалось скомпилировать регулярки: {self.config.exclude_file_patterns=}, {ex=}")
            return
        include_file_patterns = self.config.include_files
        for start_dir in start_dirs:
            for file_path in start_dir.rglob("*"):
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
                    content = file_path.read_text(encoding="utf-8")
                    yield file_path, content
                except Exception as ex:
                    logger.error(f"Ошибка при чтении файла: {ex}, {file_path=}")
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
        :return: True, если файл сохранен успешно, False в противном случае.
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
            export_path = Path(f"{file_path}{suffix}")
            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_text(response, encoding='utf-8')
            pprint(f'Ответ модели сохранен в: {export_path}', text_color='green')
            return True
        except Exception as ex:
            logger.critical(f'Ошибка сохранения файла: {export_path=}, {ex=}')
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
            logger.error(f"Ошибка в `remove_outer_quotes()`: {ex}")
            return ''
        if response.startswith(('```python', '```mermaid')):
            return response
        config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json')
        for prefix in config.remove_prefixes:
            if response.lower().startswith(prefix.lower()):
                return response.removeprefix(prefix).removesuffix("```").strip()
        return response

    def run(self, start_file_number: int = 1):
        """
        Запуск процесса обработки файлов.

        :param start_file_number: Номер файла, с которого начать обработку.
        :type start_file_number: int
        """
        signal.signal(
            signal.SIGINT, self._signal_handler
        )
        asyncio.run(self.process_files(start_file_number))

    def _signal_handler(self, signal, frame):
         """
         Обработка прерывания выполнения.

         :param signal: Сигнал прерывания.
         :type signal: int
         :param frame: Текущий кадр стека.
         :type frame: Any
         """
         pprint("Процесс был прерван", text_color="red")
         sys.exit(0)

def main():
    """Основная функция для запуска."""
    args = CodeAssistant.parse_args()
    assistant = CodeAssistant(**args)
    assistant.run(start_file_number=args["start_file_number"])


if __name__ == "__main__":
    """
    Код запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.
    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки во время работы программы.
    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.
    """
    config_path: Path = (
        gs.path.endpoints / "hypo69" / "code_assistant" / "code_assistant.json"
    )
    while True:
        config: SimpleNamespace = j_loads_ns(config_path)
        args = config.argparse
        for lang in args.languages:
            for role in args.roles:
                logger.debug(f"Start role: {role}, lang: {lang}", None, False)
                assistant_direct = CodeAssistant(
                    role=role,
                    lang=lang,
                    model=["gemini"],
                    start_dirs=[".."],
                )
                asyncio.run(assistant_direct.process_files(start_file_number=1))
                config: SimpleNamespace = j_loads_ns(config_path)
                args = config.argparse
```