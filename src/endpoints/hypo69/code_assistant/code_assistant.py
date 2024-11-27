## \file hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.hypo69.code_assistant 
    :platform: Windows, Unix
    :synopsis: Модуль для работы ассистента программиста
"""

MODE = "dev"


"""
Модуль для работы ассистента программиста
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
"""

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
from src.utils.printer import pprint
from src.utils.path import get_relative_path
from src.logger import logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary 


class CodeAssistant:
    """ 
    .. :class:`CodeAssistant`
        :synopsis: Класс для работы ассистента программиста с моделями ИИ
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
        """Инициализация ассистента с заданными параметрами."""
        self.role = kwargs.get("role", "doc_writer_rst")
        self.lang = "en" if self.role == "pytest" else kwargs.get("lang", "EN")
        self.model = kwargs.get("model", ["gemini"])
        self.start_dirs = kwargs.get("start_dirs", [".."])
        self.base_path = gs.path.endpoints / "hypo69" / "code_assistant"
        self.config = j_loads_ns(self.base_path / "code_assistant.json")
        self.gemini_model = None
        self.openai_model = None
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs):
        """Инициализация моделей на основе заданных параметров."""
        if "gemini" in self.model:
            self.gemini_model = GoogleGenerativeAI(
                model_name="gemini-1.5-flash-8b",
                api_key=gs.credentials.gemini.onela,
                **kwargs,
            )
        if "openai" in self.model:
            self.openai_model = OpenAIModel(
                model_name="gpt-4o-mini",
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwargs,
            )

    @staticmethod
    def parse_args():
        """Разбор аргументов командной строки."""
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
        """Чтение инструкции из файла."""
        try:
            return Path(
                gs.path.src
                / "ai"
                / "prompts"
                / "developer"
                / f"{self.role}_{self.lang}.md"
            ).read_text(encoding="UTF-8")
        except Exception as ex:
            logger.error(f"Error reading instruction file", ex)
            return False

    @property
    def code_instruction(self) -> str | bool:
        """Чтение инструкции для кода."""
        try:
            return Path(
                self.base_path
                / "instructions"
                / f"instruction_{self.role}_{self.lang}.md"
            ).read_text(encoding="UTF-8")
        except Exception as ex:
            logger.error(f"Error reading instruction file", ex)
            ...
            return False

    @property
    def translations(self) -> SimpleNamespace:
        """Загрузка переводов для ролей и языков."""
        return j_loads_ns(
            gs.path.endpoints
            / "hypo69"
            / "code_assistant"
            / "translations"
            / "translations.json"
        )

    def process_files(self, start_file_number: Optional[int] = 1):
        """компиляция, отправка запроса и сохранение результата."""
        for i, (file_path, content) in enumerate(self._yield_files_content()):
            if not any((file_path, content)):    # <- ошибка чтения файла
                continue
            if i < start_file_number:
                continue
            if file_path and content:
                content_request = self._create_request(file_path, content)

                if self.gemini_model:
                    response = self.gemini_model.ask(str(content_request))
                    # response = True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (comment out the line above)
                    if response:
                        ... # comment for debug / uncomment for prod
                        # pprint(f"RAW response:\n{response}") # посмотреть на ответ
                        response = self._remove_outer_quotes(response) # <- ~~~~~~~~~~~~~~~~~~ DEBUG (comment line to skip remove_outer_quotes)
                        # pprint(f"CLEAR response:\n{response}")  # посмотреть на очищенный ответ
                        self._save_response(file_path, response, "gemini") # <- ~~~~~~~~~~~~~~~~~~ DEBUG (comment line to skip saving)
                        ...
                    else:
                        logger.error("Ошибка ответа модели")
                        return
                        ...

            pprint(f"Processed file number: {i + 1}", text_color="yellow")
           

            time.sleep(
                20   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (change timeout)
            )  

    def _create_request(self, file_path: str, content: str) -> str:
        """Создание запроса с учетом роли и языка."""
        content_request = content
        try:
            roles_translations:SimpleNamespace = getattr(self.translations.roles, self.role)
            role_description_translated:str = getattr(roles_translations, self.lang)
            file_location_translated:str = getattr(self.translations.file_location_translated, self.lang)
            
            content_request: dict = {
                "role": f"{role_description_translated}",
                "output_language": self.lang,
                f"{file_location_translated}": get_relative_path(file_path, "hypotez"),
                "instruction": self.code_instruction,
                "input_code": f"```{content}```",
            }
        except Exception as ex:
            logger.error(f"Ошибка в составлении запроса ", ex)
            ...
        return content_request

    def _yield_files_content(
        self,
        start_dirs: List[Path] = [gs.path.src],
    ) -> Iterator[tuple[Path, str]]:
        """
        Генерирует пути файлов и их содержимое по указанным шаблонам.

        :param start_dirs: Список директорий для обхода.
        :return: Итератор кортежей из пути файла и его содержимого.
        """
        # Компилируем паттерны исключаемых файлов
        try:
            exclude_file_patterns = [
                re.compile(pattern) for pattern in self.config.exclude_file_patterns
            ]
        except Exception as ex:
            logger.error(f"Не удалось скомпилировать регулярки из списка:/n{self.config.exclude_file_patterns=}\n ",ex)
            ...
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
                    # pprint(
                    #     f"Пропускаю файл в исключенной директории: {file_path}",
                    #     text_color="cyan",
                    # )
                    continue

                # Проверяем исключенные файлы по паттерну
                if any(
                    exclude.match(str(file_path)) for exclude in exclude_file_patterns
                ):
                    # pprint(
                    #     f"Пропускаю файл по паттерну исключения: {file_path}",
                    #     text_color="cyan",
                    # )
                    continue

                # Проверяем конкретные исключенные файлы
                if str(file_path) in self.config.exclude_files:
                    # pprint(
                    #     f"Пропускаю исключенный файл: {file_path}", text_color="cyan"
                    # )
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
   

    def _save_response(self, file_path: Path, response: str, model_name: str) -> None:
        """Сохранение ответа модели в файл.

        Этот метод сохраняет ответ модели в файл в формате, определяемом ролью
        объекта. Путь к файлу строится с учётом настроек конфигурации и параметров 
        модели. Файл сохраняется в соответствующей директории с правильным расширением.

        Args:
            file_path (Path): Исходный путь к файлу, в который будет записан ответ.
            response (str): Ответ модели, который необходимо сохранить.
            model_name (str): Имя модели, использованной для генерации ответа.

        Raises:
            OSError: Если не удаётся создать директорию или записать в файл.
        """
    
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
    

        # Формируем новый путь с нужным расширением в зависимости от роли
        export_path = Path(file_path).with_suffix(
            {
                f'code_checker': '.md',  # для роли "code_checker" будет использоваться .md
                f'doc_writer_md': '.md',  # для роли "doc_writer_md" будет использоваться .md
                f'doc_writer_rst': '.rst',  # для роли "doc_writer_rst" будет использоваться .rst
                f'doc_writer_html': '.html',  # для роли "doc_writer_html" будет использоваться .html
                f'code_explainer_md': '.md',  # для роли "code_explainer_md" будет использоваться .md
                f'code_explainer_html': '.html',  # для роли "code_explainer_html" будет использоваться .html
            }.get(self.role, '.rst')  # Если роль не соответствует ни одной из вышеуказанных, по умолчанию используется .rst
        )

        # Создаём родительскую директорию, если она ещё не существует
        export_path.parent.mkdir(parents=True, exist_ok=True)

        # Записываем ответ в файл с указанной кодировкой UTF-8
        export_path.write_text(response, encoding='utf-8')

        # Выводим сообщение о успешном сохранении файла
        pprint(f'Ответ модели сохранен в: {export_path}', text_color='green')

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
            logger.error("Exception in `remove_outer_quotes()`", ex)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG
            ...
            return ''

        # Если строка начинается с '```python' или '```mermaid', возвращаем её без изменений
        if response.startswith(('```python', '```mermaid')):
            return response

        # Удаляем маркер для известных форматов, если строка обрамлена в '```'
        config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json')
        for prefix in config.known_prefixes:
            # Сравниваем с префиксом без учёта регистра
            if response.lower().startswith(prefix.lower()):
                return response.removeprefix(prefix).removesuffix("```").strip()

        # Возвращаем строку без изменений, если условия не выполнены
        return response

    
    def run(self, start_file_number: int = 1):
        """Запуск процесса обработки файлов."""
        signal.signal(
            signal.SIGINT, self._signal_handler
        )  # Обработка прерывания (Ctrl+C)
        self.process_files(start_file_number)

    def _signal_handler(self, signal, frame):
        """Обработка прерывания выполнения."""
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
                logger.debug(f"Start role: {role}, lang: {lang}", None, False)

                assistant_direct = CodeAssistant(
                    role=role,
                    lang=lang,
                    model=["gemini"],
                    # start_dirs = [Path('suppliers'), Path('webdriver')],
                    start_dirs=[".."],
                )
                assistant_direct.process_files(start_file_number=1)

                # Обновление конфигурации для учёта изменений во время выполнения
                config: SimpleNamespace = j_loads_ns(config_path)
                args = config.argparse
