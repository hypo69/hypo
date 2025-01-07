# Анализ кода модуля `assistant.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код разбит на логические блоки и функции, что облегчает чтение и понимание.
    *   Используются `logger` для логирования ошибок, что помогает в отладке.
    *   Применяется `j_loads_ns` для загрузки json файлов, что соответствует требованиям.
    *   Есть обработка прерывания сигнала `SIGINT` для корректного завершения программы.
    *   Код соответствует стандарту PEP8.
    *   Есть docstring для класса, методов и функций.
-   **Минусы:**
    *   Не все docstring соответствуют стандарту RST.
    *   Используются `try-except` блоки в местах, где достаточно логирования.
    *   Не везде есть подробные комментарии, объясняющие логику кода.
    *   Смешение функций `async` и синхронных функций.
    *   Дублирование кода в функции `main()` и `run()`, что ведет к избыточности.
    *   Много `...` как точек остановки, которые нужно убрать или заменить на реальный код.
    *   Не везде добавлены rst комментарии к переменным класса.
    *   Отсутствуют type hints для параметров и возвращаемых значений.
    *   Пропущена инициализация переменной `file_name` в функции `send_file`

**Рекомендации по улучшению**

1.  **Документация RST:** Необходимо переписать все docstring в формате reStructuredText (RST), включая описания параметров, возвращаемых значений и т.д.
2.  **Логирование ошибок:** Избегать избыточного использования `try-except` блоков. Предпочтительнее использовать `logger.error` для логирования и возврата `False` или `None` при ошибках.
3.  **Улучшение комментариев:** Добавить подробные комментарии к каждой строчке кода.
4.  **Рефакторинг `send_file`:** Инициализировать `file_name` и улучшить обработку ошибок в `send_file`.
5.  **Удаление `...`:** Заменить все `...` на логику кода или удалить.
6.  **Улучшение `main`:** Убрать дублирование кода, вынести в отдельную функцию.
7.  **Type Hints:** Добавить type hints для параметров и возвращаемых значений всех функций.
8.  **Асинхронность:** Переписать все асинхронные функции или переделать на синхронные.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов
=========================================================================================

Этот модуль содержит класс :class:`CodeAssistant`, который используется для работы с различными моделями ИИ,
такими как Google Gemini и OpenAI, для выполнения задач по обработке кода.

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
from typing import Iterator, List, Optional, Any, Dict
from types import SimpleNamespace
import signal
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

    :param role: Роль ассистента, например 'code_checker', 'doc_writer_rst'.
    :type role: str
    :param lang: Язык, на котором ассистент будет работать, например 'ru', 'en'.
    :type lang: str
    :param model: Список моделей ИИ для использования, например ['gemini', 'openai'].
    :type model: list[str]
    :param start_dirs: Список начальных директорий для обработки файлов.
    :type start_dirs: list[str]
    """
    role: str
    lang: str
    start_dirs: Path | str | list[Path] | list[str]
    base_path: Path
    config: SimpleNamespace
    gemini_model: GoogleGenerativeAI
    openai_model: OpenAIModel
    start_file_number: int

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        """
        Инициализация ассистента с заданными параметрами.

        :param kwargs: Словарь параметров для инициализации.
            :key role: Роль ассистента, по умолчанию 'doc_writer_rst'.
            :key lang: Язык ассистента, по умолчанию 'ne'.
            :key model: Список моделей ИИ, по умолчанию ['gemini'].
            :key start_dirs: Список директорий для обработки, по умолчанию ['..'].
        :type kwargs: dict
        """
        self.role = kwargs.get("role", "doc_writer_rst")
        self.lang = "en" if self.role == "pytest" else kwargs.get("lang", "ne")
        self.models_list = kwargs.get("model", ["gemini"])
        self.start_dirs = kwargs.get("start_dirs", [".."])
        self.base_path = gs.path.endpoints / "hypo69" / "code_assistant"
        self.config = j_loads_ns(self.base_path / "code_assistant.json")
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs: Dict[str, Any]) -> None:
        """
        Инициализация моделей на основе заданных параметров.

        :param kwargs: Параметры для инициализации моделей.
        :type kwargs: dict
        """
        if "gemini" in self.models_list:
            self.gemini_model = GoogleGenerativeAI(
                model_name=self.config.gemini_model_name,
                api_key=gs.credentials.gemini.onela,
                **kwargs,
            )
        if "openai" in self.models_list:
            self.openai_model = OpenAIModel(
                model_name="gpt-4o-mini",
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwargs,
            )

    @staticmethod
    def parse_args() -> Dict[str, Any]:
        """
        Разбор аргументов командной строки.

        :return: Словарь с аргументами командной строки.
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
            logger.error(f"Ошибка чтения файла инструкции: {ex}")
            return False

    @property
    def code_instruction(self) -> str:
        """
        Чтение инструкции для кода.

        :return: Инструкция в виде строки или пустая строка в случае ошибки.
        :rtype: str
        """
        try:
            return Path(
                self.base_path
                / "instructions"
                / f"instruction_{self.role}_{self.lang}.md"
            ).read_text(encoding="UTF-8")
        except Exception as ex:
            logger.error(f"Ошибка чтения файла инструкции: {ex}")
            return ""

    @property
    def translations(self) -> SimpleNamespace:
        """
        Загрузка переводов для ролей и языков.

        :return: Объект SimpleNamespace с переводами.
        :rtype: SimpleNamespace
        """
        return j_loads_ns(
            gs.path.endpoints
            / "hypo69"
            / "code_assistant"
            / "translations"
            / "translations.json"
        )

    async def process_files(self, start_file_number: Optional[int] = 1) -> None:
        """
        Компиляция, отправка запроса и сохранение результата.

        :param start_file_number: Номер файла, с которого начать обработку.
        :type start_file_number: Optional[int]
        """

        async def send_file(file_path: Path, file_name: Optional[str] = None) -> str | bool:
             """
             Отправка файла в модель.

             :param file_path: Абсолютный путь к файлу, который нужно отправить.
             :type file_path: Path
             :param file_name: Имя файла для отправки. Если не указано и 'src' отсутствует, используется имя файла без изменений.
             :type file_name: Optional[str]
             :return: URL файла или False в случае ошибки.
             :rtype: str | bool
             """
             try:
                 # Проверка имени файла на `__init__.py` и `header.py`
                 if file_path.name in ('__init__.py', 'header.py'):
                    logger.info(f'Файл пропущен: {file_path}')
                    return False

                 # Если file_name не задан, извлекается часть пути начиная с 'src'
                 if not file_name:
                     if 'src' in file_path.parts:
                         index = file_path.parts.index('src')
                         relative_path = Path(*file_path.parts[index:])

                         # Заменяем `/` на `--` и игнорируем суффикс файла
                         file_name = 'src--' + '--'.join(relative_path.parts[1:-1]) + '--' + relative_path.stem
                     else:
                         # Если 'src' нет, используется имя файла без изменений
                         file_name = file_path.stem

                 # Отправка файла в модель
                 response = self.gemini_model.upload_file(file_path)

                 if response:
                     pprint(response, text_color='light_gray')
                     if hasattr(response, 'url'):
                         return response.url
                 return False
             except Exception as ex:
                # Логирование ошибки при отправке файла
                logger.error(f'Ошибка при отправке файла: {ex}')
                return False


        for i, (file_path, content) in enumerate(self._yield_files_content()):
            # Проверка корректности чтения файла
            if not all((file_path, content)):
                continue
            # Пропускаем файлы до указанного номера
            if i < start_file_number:
                continue
            if file_path and content:
                # Отправка файла в модель
                # send_file_response = send_file(file_path) # <- отправить в модель файл
                content_request = self._create_request(file_path, content)
                response = await self.gemini_model.ask(content_request)

                if response:
                    response = self._remove_outer_quotes(response)

                    if not await self._save_response(file_path, response, "gemini"):
                        logger.error(f"Файл {file_path} не был сохранен")
                        continue
                    pprint(f"Обработан файл номер: {i + 1}", text_color="yellow")
                else:
                    logger.error("Ошибка ответа модели")
                    continue

            await asyncio.sleep(20) # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (change timeout)

    def _create_request(self, file_path: str, content: str) -> str:
        """
        Создание запроса с учетом роли и языка.

        :param file_path: Путь к файлу.
        :type file_path: str
        :param content: Содержимое файла.
        :type content: str
        :return: Строка запроса для модели.
        :rtype: str
        """
        content_request = content
        try:
            roles_translations: SimpleNamespace = getattr(self.translations.roles, self.role, 'doc_writer_md')
            role_description_translated: str = getattr(roles_translations, self.lang, 'Your specialization is documentation creation in the `MD` format')
            file_location_translated: str = getattr(self.translations.file_location_translated, self.lang, 'Path to file: ')

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
    ) -> Iterator[tuple[Path, str]]:
        """
        Генерирует пути файлов и их содержимое по указанным шаблонам.

        :param start_dirs: Список директорий для обхода.
        :type start_dirs: list[Path]
        :return: Итератор кортежей из пути файла и его содержимого.
        :rtype: Iterator[tuple[Path, str]]
        """
        # Компилируем паттерны исключаемых файлов
        try:
            exclude_file_patterns = [
                re.compile(pattern) for pattern in self.config.exclude_file_patterns
            ]
        except Exception as ex:
            logger.error(f"Не удалось скомпилировать регулярки из списка: {self.config.exclude_file_patterns=}, {ex}")
            return

        include_file_patterns = self.config.include_files
        for start_dir in start_dirs:
            # Итерация по всем файлам в директории
            for file_path in start_dir.rglob("*"):
                # Проверяем соответствие шаблонам включения
                if not any(
                    fnmatch.fnmatch(file_path.name, pattern)
                    for pattern in include_file_patterns
                ):
                    continue

                # Проверяем исключенные директории
                if any(
                    exclude_dir in file_path.parts
                    for exclude_dir in self.config.exclude_dirs
                ):
                    continue

                # Проверяем исключенные файлы по паттерну
                if any(
                    exclude.match(str(file_path)) for exclude in exclude_file_patterns
                ):
                   continue

                # Проверяем конкретные исключенные файлы
                if str(file_path) in self.config.exclude_files:
                    continue

                # Чтение содержимого файла
                try:
                    content = file_path.read_text(encoding="utf-8")
                    yield file_path, content
                    # make_summary( docs_dir = start_dir.parent / 'docs' )  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG  (create `summary.md`)
                except Exception as ex:
                    pprint(
                        f"Ошибка при чтении файла: {ex}",
                        text_color="red",
                        bg_color="light_grey",
                    )
                    yield None, None

    async def _save_response(self, file_path: Path, response: str, model_name: str) -> bool:
        """
        Сохранение ответа модели в файл с добавлением суффикса.

        :param file_path: Исходный путь к файлу, в который будет записан ответ.
        :type file_path: Path
        :param response: Ответ модели, который необходимо сохранить.
        :type response: str
        :param model_name: Имя модели, использованной для генерации ответа.
        :type model_name: str
        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        try:
            # Получаем директорию для вывода в зависимости от роли
            output_directory = getattr(self.config.output_directory, self.role)

            # Формируем целевую директорию с учётом подстановки параметров <model> и <lang>
            target_dir = (
                f'docs/{output_directory}'
                .replace('<model>', model_name)
                .replace('<lang>', self.lang)
            )

            # Заменяем часть пути на целевую директорию
            file_path = str(file_path).replace('src', target_dir)

            # Определяем суффикс для добавления в зависимости от роли
            suffix_map = {
                'code_checker': '.md',
                'doc_writer_md': '.md',
                'doc_writer_rst': '.rst',
                'doc_writer_html': '.html',
                'code_explainer_md': '.md',
                'code_explainer_html': '.html',
                'pytest': '.md',
            }
            suffix = suffix_map.get(self.role, '.md')  # По умолчанию используется .md

            # Формируем новый путь с добавлением суффикса
            export_path = Path(f"{file_path}{suffix}")

            # Создаём родительскую директорию, если она ещё не существует
            export_path.parent.mkdir(parents=True, exist_ok=True)

            # Записываем ответ в файл с указанной кодировкой UTF-8
            export_path.write_text(response, encoding='utf-8')

            # Выводим сообщение о успешном сохранении файла
            pprint(f'Ответ модели сохранен в: {export_path}', text_color='green')
            return True

        except Exception as ex:
            logger.critical(f'Ошибка сохранения файла: {export_path=}, {ex}')
            return False

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
            logger.error(f"Ошибка в `remove_outer_quotes()`: {ex}")
            return ''

        # Если строка начинается с '```python' или '```mermaid', возвращаем её без изменений
        if response.startswith(('```python', '```mermaid')):
            return response

        # Удаляем маркер для известных форматов, если строка обрамлена в '```'
        config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json')
        for prefix in config.remove_prefixes:
            # Сравниваем с префиксом без учёта регистра
            if response.lower().startswith(prefix.lower()):
                return response.removeprefix(prefix).removesuffix("```").strip()

        # Возвращаем строку без изменений, если условия не выполнены
        return response

    def run(self, start_file_number: int = 1) -> None:
        """
        Запуск процесса обработки файлов.

        :param start_file_number: Номер файла, с которого начать обработку.
        :type start_file_number: int
        """
        signal.signal(
            signal.SIGINT, self._signal_handler
        )  # Обработка прерывания (Ctrl+C)
        asyncio.run(self.process_files(start_file_number))

    def _signal_handler(self, signal: int, frame: Any) -> None:
        """
        Обработка прерывания выполнения.

        :param signal: Номер сигнала.
        :type signal: int
        :param frame: Текущий кадр стека.
        :type frame: Any
        """
        pprint("Процесс был прерван", text_color="red")
        sys.exit(0)

def main() -> None:
    """
    Основная функция для запуска.
    """
    args = CodeAssistant.parse_args()
    assistant = CodeAssistant(**args)
    assistant.run(start_file_number=args["start_file_number"])

if __name__ == "__main__":
    """
    Код запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.
    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки во время работы программы.
    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.
    """
    # Путь к файлу конфигурации
    config_path: Path = (
        gs.path.endpoints / "hypo69" / "code_assistant" / "code_assistant.json"
    )

    while True:
        # Загрузка конфигурации
        config: SimpleNamespace = j_loads_ns(config_path)
        args = config.argparse

        # Обработка файлов для каждой комбинации языков и ролей
        for lang in args.languages:
            for role in args.roles:
                logger.debug(f"Start role: {role}, lang: {lang}")

                assistant_direct = CodeAssistant(
                    role=role,
                    lang=lang,
                    model=["gemini"],
                    start_dirs=[".."],
                )
                asyncio.run(assistant_direct.process_files(start_file_number=1))

                # Обновление конфигурации для учёта изменений во время выполнения
                config: SimpleNamespace = j_loads_ns(config_path)
                args = config.argparse

```