## \file hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.hypo69.code_assistant 
    :platform: Windows, Unix
    :synopsis: Модуль для работы ассистента программиста
"""

MODE = 'dev'


"""
Модуль для работы ассистента программиста
=========================================================================================

Этот модуль содержит класс :class:`CodeAssistant`, который используется для работы с различными моделями ИИ, 
такими как Google Gemini и OpenAI, для выполнения задач по обработке кода.

Пример использования
--------------------

Пример использования класса `CodeAssistant`:

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
from src.logger import logger


class CodeAssistant:
    """Класс для работы ассистента программиста с моделями ИИ."""

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
        self.role = kwargs.get('role', 'doc_writer_rst')
        self.lang = 'en' if self.role == 'pytest' else kwargs.get('lang', 'EN')  
        self.model = kwargs.get('model', ['gemini'])
        self.start_dirs = kwargs.get('start_dirs', ['..'])
        self.base_path = gs.path.endpoints / 'hypo69' / 'code_assistant'
        self.config = j_loads_ns(self.base_path / 'code_assistant.json')
        self.gemini_model = None
        self.openai_model = None
        self._initialize_models(**kwargs)

    def _initialize_models(self, **kwargs):
        """Инициализация моделей на основе заданных параметров."""
        if 'gemini' in self.model:
            self.gemini_model = GoogleGenerativeAI(
                model_name='gemini-1.5-flash-8b',
                api_key=gs.credentials.gemini.onela,
                **kwargs
            )
        if 'openai' in self.model:
            self.openai_model = OpenAIModel(
                model_name='gpt-4o-mini',
                assistant_id=gs.credentials.openai.assistant_id.code_assistant,
                **kwargs
            )

    @staticmethod
    def parse_args():
        """Разбор аргументов командной строки."""
        parser = argparse.ArgumentParser(description='Ассистент для программистов')
        parser.add_argument('--role', type=str, default='code_checker', help='Роль для выполнения задачи')
        parser.add_argument('--lang', type=str, default='ru', help='Язык выполнения')
        parser.add_argument('--model', nargs='+', type=str, default=['gemini'], help='Список моделей для инициализации')
        parser.add_argument('--start-dirs', nargs='+', type=str, default=[], help='Список директорий для обработки')
        parser.add_argument('--start-file-number', type=int, default=1, help='С какого файла делать обработку. Полезно при сбоях')
        return vars(parser.parse_args())

    @property
    def system_instruction(self) -> str | bool:
        """Чтение инструкции из файла."""
        try:
            return Path(gs.path.src / 'ai' / 'prompts' / 'developer' / f'{self.role}_{self.lang}.md').read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error(f"Error reading instruction file", ex)
            return False   

    @property
    def code_instruction(self) -> str | bool:
        """Чтение инструкции для кода."""
        try:
            return Path(self.base_path / 'instructions' / f'instruction_{self.role}_{self.lang}.md').read_text(encoding='UTF-8')
        except Exception as ex:
            logger.error(f"Error reading instruction file", ex)
            return False

    @property
    def translations(self) -> SimpleNamespace:
        """Загрузка переводов для ролей и языков."""
        return j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'translations' / 'translations.json')

    def process_files(self, start_file_number: Optional[int] = 1):
        """компиляция, отправка запроса и сохранение результата."""
        for i, (file_path, content) in enumerate(self._yield_files_content()):
            if i < start_file_number:
                continue
            if file_path and content:
                content_request = self._create_request(content)

                if self.gemini_model:
                    response = self.gemini_model.ask(content_request)
                    
                    if response:
                        #pprint(f"RAW response:\n{response}")
                        response = self._remove_outer_quotes(response)
                        #pprint(f"CLEAR response:\n{response}")
                        self._save_response(file_path, response, 'gemini')
                    else:
                        logger.error("Ошибка ответа модели")
                        return
                        ...

            pprint(f'Processed file number: {i + 1}', text_color='yellow')
            time.sleep(30) # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG  
                                                 
    def _create_request(self, content: str) -> str:
        """Создание запроса с учетом роли и языка."""
        roles_translations = getattr(self.translations.roles, self.role)
        role_description = getattr(roles_translations, self.lang)
    
        content_request = (
            f'**{role_description}**\n'
            f'{self.code_instruction}\n'
            f'Input code:\n\n```{content}```\n'
        )
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
        exclude_file_patterns = [re.compile(pattern) for pattern in self.config.exclude_file_patterns]
        include_file_patterns = self.config.include_files
        for start_dir in start_dirs:
            # Итерация по всем файлам в директории
            for file_path in start_dir.rglob('*'):
                # Проверяем соответствие шаблонам включения
                if not any(fnmatch.fnmatch(file_path.name, pattern) for pattern in include_file_patterns):
                    continue

                # Проверяем исключенные директории
                if any(exclude_dir in file_path.parts for exclude_dir in self.config.exclude_dirs):
                    pprint(f'Пропускаю файл в исключенной директории: {file_path}', text_color='cyan')
                    continue

                # Проверяем исключенные файлы по паттерну
                if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                    pprint(f'Пропускаю файл по паттерну исключения: {file_path}', text_color='cyan')
                    continue

                # Проверяем конкретные исключенные файлы
                if str(file_path) in self.config.exclude_files:
                    pprint(f'Пропускаю исключенный файл: {file_path}', text_color='cyan')
                    continue

                # Чтение содержимого файла
                try:
                    content = file_path.read_text(encoding='utf-8')
                    yield file_path, content
                except Exception as ex:
                    pprint(f'Ошибка при чтении файла: {ex}', text_color='red', bg_color='light_grey')
                    yield None, None

    def _save_response(self, file_path: Path, response: str, model_name: str):
        """Сохранение ответа модели в файл."""
        output_directory: str = getattr(self.config.output_directory, self.role)  
        target_dir = 'docs/' + output_directory.replace("<model>", model_name).replace("<lang>", self.lang)
        file_path = str(file_path).replace('src', target_dir)  # Convert Path to string for replace
        export_path = Path(file_path).with_suffix('.md'if role != 'doc_writer_rst' else '.rst')  # Convert back to Path and change suffix
        export_path.parent.mkdir(parents=True, exist_ok=True)
        export_path.write_text(response, encoding="utf-8")
        pprint(f"Ответ модели сохранен в: {export_path}", text_color='green')

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
        response = response.strip()
        # Если строка начинается с '```python', возвращаем её без изменений
        if response.startswith('```python'):
            return response

        # Удаляем маркер для известных форматов, если строка обрамлена в '```'
        known_prefixes = ['```md', '```markdown', '```rst', '```']
        for prefix in known_prefixes:
            if response.startswith(prefix) and response.endswith('```'):
                return response.removeprefix(prefix).removesuffix('```').strip()

        # Возвращаем строку без изменений, если условия не выполнены
        return response



    def run(self, start_file_number: int = 1):
        """Запуск процесса обработки файлов."""
        signal.signal(signal.SIGINT, self._signal_handler)  # Обработка прерывания (Ctrl+C)
        self.process_files(start_file_number)

    def _signal_handler(self, signal, frame):
        """Обработка прерывания выполнения."""
        pprint('Процесс был прерван', text_color='red')
        sys.exit(0)


def main():
    """Основная функция для запуска."""
    args = CodeAssistant.parse_args()

    assistant = CodeAssistant(**args)

    assistant.run(start_file_number=args['start_file_number'])

if __name__ == '__main__':
    #main()
    while True:
        for lang in ['ru','en']:
            for role in ['code_checker','doc_writer_md','pytest','doc_writer_rst','code_explainer']:
                logger.debug(f"Start role: {role}, lang: {lang}", None, False)
                assistant_direct = CodeAssistant(
                    role=role,
                    lang=lang,
                    model=["gemini"],
                    #start_dirs=[Path("suppliers"), Path("webdriver")],
                    start_dirs=[".."],

                )
                assistant_direct.process_files(start_file_number = 1)

