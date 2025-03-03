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
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace
import signal
import time
import re
import fnmatch

import header
from header import __root__
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.path import get_relative_path
from src.logger.logger import logger
from src.endpoints.hypo69.code_assistant.make_summary import make_summary 
# from toolbox import 


class CodeAssistant:
    """ 
    .. :class:`CodeAssistant`
        :synopsis: Класс для работы ассистента программиста с моделями ИИ
    """

    role: str
    lang: str
    base_path:Path = __root__ / 'src' / 'endpoints' / 'hypo69' / 'code_assistant'
    config: SimpleNamespace =  = j_loads_ns(base_path / 'code_assistant.json')
    gemini_model: GoogleGenerativeAI
    openai_model: OpenAIModel


    def __init__(self, 
                 role:Optional[str] = 'doc_writer_md', 
                 lang: Optional[str] = 'en', 
                 models: Optional[list[str,str] | str] = ["gemini"],
                 system_instruction:Optional[str] = None,
                 system_instruction_path:Optional[Path | str] = None,
                 **kwards):
        """Инициализация ассистента с заданными параметрами."""
        self.role:str = role 
        self.lang:str = lang
        self.models_list:list = list( models )
        if system_instruction:
                if isinstance(system_instruction, str):
                    kwards['system_instruction'] = system_instruction
                else:
                    logger.error(f"Ошибка формата инструкции\n {system_instruction=}\n system_instruction type {type(system_instruction)}", None, False)
                    ...
        if  system_instruction_path:
            try:
                kwards['system_instruction'] = Path(system_instruction_path).read_text(encoding='UTF-8')
            except Exception as ex:
                logger.error(f"Ошибка чтения инструкции из файла {system_instruction_path=}", ex, False)
                ...

        self._initialize_models(**kwards)

    def _initialize_models(self, **kwards):
        """Инициализация моделей на основе заданных параметров."""
        

        if self.role == 'code_translator':

        else:
            system_instruction = Path(gs.path.src / 'ai' / 'prompts' / 'developer' / 'CODE_RULES.MD').read_text(encoding='UTF-8')

        if "gemini" in self.models_list:
            self.gemini_model = GoogleGenerativeAI(
                model_name=self.config.gemini_model_name,
                api_key=gs.credentials.gemini.onela,
                system_instruction = system_instruction,
                **kwards,
            )
        if "openai" in self.models_list:
            self.openai_model = OpenAIModel(
                model_name="gpt-4o-mini",
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwards,
            )


    @property
    def code_instruction(self) -> str | bool:
        """Чтение инструкции для кода."""
        try:
            return Path(
                gs.path.endpoints 
                / "hypo69" 
                / "code_assistant" 
                / "instructions"
                / f"instruction_{self.role}_{self.lang}.md"
            ).read_text(encoding="UTF-8")
        except Exception as ex:
            logger.error(f"Error reading instruction file", ex, False)
            ...
            return ''

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
                logger.error('Ошибка при отправке файла: ', ex)
                ...
                return 


    async def process_files(self, start_dirs:str|Path|list[str,str]|list[Path,Path] = None, start_file_number: Optional[int] = 1 ) -> bool:
        """компиляция, отправка запроса и сохранение результата.
       
        """
        if not start_dirs:
           start_dirs = self.config.start_dirs
        if not start_dirs:
            logger.error("Ошибка иницаилизации стартовой директории")
            ...
            return 
        start_dirs = start_dirs if isinstance(start_dirs,list) else [start_dirs]
        for process_driectory in start_dirs:
            logger.info(f"Start {process_driectory=}")

            for i, (file_path, content) in enumerate(self._yield_files_content(process_driectory)):
                if not any((file_path, content)):    # <- ошибка чтения файла
                    continue
                if i < start_file_number: # <- старт с номера файла
                    continue
                if file_path and content:
                    # send_file(file_path) # <- отправить в модель файл
                    content_request = self._create_request(file_path, content)
                    response = await self.gemini_model.ask_async(content_request)

                    if response:

                        if not await self._save_response(file_path, response, "gemini"):
                            logger.error(f"Файл {file_path} \n НЕ сохранился")
                            ...
                            continue
                        logger.debug(f"Processed file number: {i + 1}", None, False)
                        ...
                    else:
                        logger.error("Ошибка ответа модели", None, False)
                        ...
                        continue

                await asyncio.sleep(20) # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (change timeout)

    def _create_request(self, file_path: str, content: str) -> str:
        """Создание запроса с учетом роли и языка."""
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
            logger.error(f"Ошибка в составлении запроса ", ex, False)
            ...
            return content

        return str(content_request)

    def _yield_files_content(
        self,
        process_driectory: str| Path,
    ) -> Iterator[tuple[Path, str]]:
        """
        Генерирует пути файлов и их содержимое по указанным шаблонам.

        Args:
            process_driectory (Path | str): Абсолютный путь к стартовой директории
          
        Returns:
            bool: Iterator

        """

        process_driectory:Path = process_driectory if isinstance(process_driectory, Path) else Path(process_driectory)
        # Компиляция паттернов исключаемых файлов
        try:
            exclude_file_patterns = [
                re.compile(pattern) for pattern in self.config.exclude_file_patterns
            ]

        except Exception as ex:
            logger.error(f"Не удалось скомпилировать регулярки из списка:/n{self.config.exclude_file_patterns=}\n ",ex)
            ...
        include_file_patterns = self.config.include_files


        # Итерация по всем файлам в директории
        for file_path in process_driectory.rglob("*"):
            # Проверка на соответствие шаблонам включения
            if not any(
                fnmatch.fnmatch(file_path.name, pattern)
                for pattern in include_file_patterns
            ): 
                continue

            # Прверка исключенных директорий
            if any(
                exclude_dir in file_path.parts
                for exclude_dir in self.config.exclude_dirs
            ):
               continue

            # Проверка исключенных файлов по паттерну
            if any(
                exclude.match(str(file_path)) for exclude in exclude_file_patterns
            ): 
                continue

            # Проверка конкретных исключенных файлов
            if str(file_path) in self.config.exclude_files:
                continue

            # Чтение содержимого файла
            try:
                content = file_path.read_text(encoding="utf-8")
                yield file_path, content
                # make_summary( docs_dir = start_dir.parent / 'docs' )  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG  (create `summary.md`)
            except Exception as ex:
                logger.error(f"Ошибка при чтении файла {file_path}",ex)
                ...
                yield None, None

            ...


     

    async def _save_response(self, file_path: Path, response: str, model_name: str) -> bool:
        """Сохранение ответа модели в файл с добавлением суффикса.

        Метод сохраняет ответ модели в файл, добавляя к текущему расширению файла
        дополнительный суффикс, определяемый ролью. 
        Args:
            file_path (Path): Исходный путь к файлу, в который будет записан ответ.
            response (str): Ответ модели, который необходимо сохранить.
            model_name (str): Имя модели, использованной для генерации ответа.

        Raises:
            OSError: Если не удаётся создать директорию или записать в файл.
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
        
            export_path = Path(file_path)
            if export_path.suffix == '.md' and suffix == '.md':
              export_path = Path(f"{file_path}")
            else:
                export_path = Path(f"{file_path}{suffix}")

            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_text(response, encoding='utf-8')
            logger.success(f"{export_path.name}")
            return True

        except Exception as ex:
            logger.critical(f'Ошибка сохранения файла: {export_path=}', exc_info=ex)
            #sys.exit(0)
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
                logger.error("Exception in `remove_outer_quotes()`", ex)   # <- ~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG
                ...
                return ''

            # Если строка начинается с '```python' или '```mermaid', возвращаем её без изменений
            if response.startswith(('```python', '```mermaid')):
                return response

            # Удаление маркера для известных форматов, если строка обрамлена в '```'
            config = j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json')
            for prefix in config.remove_prefixes:
                # Сравнение с префиксом без учёта регистра
                if response.lower().startswith(prefix.lower()):
                    return response.removeprefix(prefix).removesuffix("```").strip()

            # Возврат строки без изменений, если условия не выполнены
            return response

    
    def run(self, start_file_number: int = 1):
        """Запуск процесса обработки файлов."""
        signal.signal(
            signal.SIGINT, self._signal_handler
        )  # Обработка прерывания (Ctrl+C)
        self.process_files(start_file_number)

    def _signal_handler(self, signal, frame):
        """Обработка прерывания выполнения."""
        logger.debug("Процесс был прерван", text_color="red")
        sys.exit(0)


def main():
    """Основная функция для запуска."""
    args = parse_args()

    assistant = CodeAssistant(**args)

    assistant.run(start_file_number=args["start_file_number"])


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


if __name__ == "__main__":
    """
    Код запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.
    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки во время работы программы.
    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.
    """
    
    ########################################################################################
    #                               Запуск через конфигурацию 
    # 

    config_path: Path = (
        gs.path.endpoints / "hypo69" / "code_assistant" / "code_assistant.json"
    )

    while True:
        # Загрузка конфигурации
        config: SimpleNamespace = j_loads_ns(config_path)
       

        # Обработка файлов для каждой комбинации языков и ролей
        for lang in config.languages:
            for role in config.roles:
                logger.debug(f"Start role: {role}, lang: {lang}", None, False)

                assistant_direct = CodeAssistant(
                    role = role,
                    lang = lang,
                    model = ["gemini"],
                   
                )
                asyncio.run( assistant_direct.process_files( start_dirs=config.start_dirs) )

                # Обновление конфигурации для учёта изменений во время выполнения
                config: SimpleNamespace = j_loads_ns(config_path)


