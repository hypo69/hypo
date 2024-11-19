## \file hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.endpoints.hypo69.code_assistant """
MODE = 'development'
import re
import sys
import time
import signal
import json
import argparse
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace
from pydantic import BaseModel, Field

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.file import read_text_file, save_text_file
from src.utils.printer import pprint
from src.logger import logger

class CodeAssistant(BaseModel):
    """Класс обучения ассистента программиста."""

    role: str = Field(default="doc_creator", description="Роль для выполнения задачи")
    lang: str = Field(default="EN", description="Язык выполнения")
    model: List[str] = Field(default_factory=lambda: ["gemini"], description="Список моделей для инициализации")
    start_dirs: List[Path] = Field(default_factory=list, description="Список стартовых директорий для обработки")
    gemini_generation_config: dict = Field(default_factory=dict, description="Конфигурация генерации для модели Gemini")
    gemini_model_name: str = Field(default="gemini-1.5-flash-8b", description="Название модели Gemini")
    gemini_model: Optional[GoogleGenerativeAI] = None

    openai_model_name: str = Field(default="gpt-4o-mini", description="Название модели OpenAI")
    openai_assistant_id: str = Field(default="", description="ID ассистента OpenAI")
    openai_model: Optional[OpenAIModel] = None

    exclude_file_patterns: List[str] = Field(default_factory=list, description="Список паттернов для исключения файлов")
    exclude_dirs: List[str] = Field(default_factory=list, description="Список директорий для исключения")
    exclude_files: List[str] = Field(default_factory=list, description="Список файлов для исключения")
    base_path: Path = Field(default = gs.path.src / 'endpoints' / 'hypo69' / 'code_assistant', description="Корневая директория скрипта")
    base_output_directory: Path = Field(default = gs.path.root / 'docs' / 'ai', description="Базовая директория для сохранения результатов по ролям")

    translations: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(), description="Переводы для ролей")
    settings: SimpleNamespace = Field(default_factory=lambda: j_loads_ns(gs.path.src / 'endpoints' / 'hypo69' / 'code_assistant' / 'settings.json'), description="Настройки")

    system_instruction_file: Path| str = Field(default="instructions", description="Инструкции перед отправлок кода в модель")
    class Config:
        arbitrary_types_allowed = True

    def signal_handler(self, sig, frame):
        """Обработчик сигнала завершения работы программы через CTRL+C."""
        logger.info("\nПрограмма завершена пользователем.")
        sys.exit(0)


    def __init__(self):
        """Выполняет инициализацию после создания объекта."""
        super().__init__()
        pprint('CodeAssistant инициализирован',text_color='gray',bg_color='white')
        self._payload()


    def _payload(self) -> bool:
        """Загружает настройки и инициализирует модели."""
        try:
            # Загружаем настройки из файла `settings.json`
            settings_path = Path('settings.json')
            settings = j_loads(settings_path) 


            # Получаем аргументы командной строки
            cli_args = self.parse_args()

            # Устанавливаем параметры: сначала значения из файла, затем перезаписываем аргументами из командной строки
            self.role = cli_args['role'] if cli_args.get('role') else settings.get('role', 'code_checker')
            self.lang = cli_args['lang'] if cli_args.get('lang') else settings.get('lang', 'ru')
            self.model = cli_args['model'] if cli_args.get('model') else settings.get('model', ['gemini'])
            self.start_dirs = cli_args['start_dirs'] if cli_args.get('start_dirs') else \
                [Path(gs.path.root) / d for d in settings.get('start_dirs', [])]

            # Загрузка остальных параметров из файла настроек
            self.gemini_generation_config = settings.get('gemini_generation_config', {})
            self.gemini_model_name = settings.get('gemini_model_name', 'gemini-1.5-flash-8b')
            self.openai_model_name = settings.get('openai_model_name', 'gpt-4o-mini')
            self.openai_assistant_id = settings.get('openai_assistant_id', '')
            self.exclude_file_patterns = settings.get('exclude_file_patterns', [])
            self.exclude_dirs = settings.get('exclude_dirs', [])
            self.exclude_files = settings.get('exclude_files', [])
            self.base_output_directory = Path(settings.get('base_output_directory', str(self.base_output_directory)))
            self.base_path = Path(settings.get('base_path', str(self.base_path)))

        except Exception as ex:
            logger.error('Ошибка инициализации', ex)
            return False

        return self.initialize_models()

    @property
    def system_instruction(self) -> str | bool:
        """ """
        try:
            system_instruction_file = Path(gs.path.src / 'ai' / 'prompts' / 'developer' / f'{self.role}_{self.lang}.md')
            system_instruction = read_text_file(system_instruction_file)
            #pprint(f'{system_instruction=}')
            return system_instruction
        except Exception as ex:
            logger.error(f"Error reading instruction file:\n{system_instruction_file=}")
            return False    

    @property
    def code_instruction(self) -> str | bool:
        """ """
        try:
            code_instruction_file = Path(self.base_path / 'instructions' / f'instruction_{self.role}_{self.lang}.md')
            code_instruction = read_text_file( code_instruction_file)
            #pprint(f'{code_instruction=}')
            return code_instruction
        except Exception as ex:
            logger.error(f"Error reading instruction file:\n{code_instruction_file=}")
            return False

    def initialize_models(self) -> bool:
        """Инициализация моделей на основе роли и языка."""
        system_instruction = self.system_instruction

        try:
            if 'gemini' in self.model:
                self.gemini_model = GoogleGenerativeAI(
                    api_key=gs.credentials.gemini.onela,
                    model_name=self.gemini_model_name,
                    system_instruction=system_instruction,
                    generation_config=self.gemini_generation_config
                )

            if 'openai' in self.model:
                self.openai_model = OpenAIModel(
                    system_instruction=system_instruction,
                    model_name=self.openai_model_name,
                    assistant_id=self.openai_assistant_id
                )
        except Exception as ex:
            logger.error(f"Ошибка инициализации модели", ex)
            return False
        return True

    def load_translations(self, file_path: Path = gs.path.src / 'endpoints' / 'hypo69' / 'code_assistant' / 'translations' / 'translations.json'):
        """Загрузка переводов для ролей и языков."""
        return j_loads_ns(file_path)

    def create_request(self, content: str, translations: SimpleNamespace):
        """Создание запроса с учетом роли и языка."""
        roles_translations: SimpleNamespace = getattr(translations.roles, self.role)
        role_description: str = getattr(roles_translations, self.lang)
        code_instruction = self.code_instruction
        content_request = f"""Твоя специализация: `{role_description}`.\nИнструкция  для кода: ```{code_instruction}```\n Код:\n\n```{content}```\n"""
        return content_request


    def process_files(self):
        """Обрабатывает файлы и взаимодействует с моделью Gemini."""
        # Загружаем переводы
        self.translations = self.load_translations()
        for i, (file_path, content) in enumerate(self.yield_files_content()):
            # Проверяем, что файл и его содержимое не пустые
            if not (file_path and content):
                continue

            # Создаем запрос для модели на основе содержимого файла и переводов
            content_request = self.create_request(content, self.translations)

            # Отправляем запрос в модель Gemini, если она активна
            if self.gemini_model:
                gemini_response = self.gemini_model.ask(content_request)
                if gemini_response:
                    
                    self.save_response(file_path, gemini_response, 'gemini')

            # Логируем номер обработанного файла
            pprint(f'Processed file number: {i + 1}', text_color='yellow')
            time.sleep(120)  # Пауза между запросами для избежания перегрузки

    def yield_files_content(
        self,
        start_dirs: List[Path] = [gs.path.src],
        patterns: List[str] = ['*.py', 'README.MD', 'INTRO.MD', 'README.RU.MD', 'INTRO.RU.MD', 'README.EN.MD', 'INTRO.EN.MD']
    ) -> Iterator[tuple[Path, str]]:
        """Генерирует пути файлов и их содержимое по указанным шаблонам.

        Args:
            start_dirs (List[Path]): Список начальных директорий для поиска файлов.
            patterns (List[str]): Список шаблонов для поиска файлов.

        Yields:
            Iterator[tuple[Path, str]]: Путь к файлу и его содержимое.
        """
        # Компилируем регулярные выражения для паттернов исключаемых файлов
        exclude_file_patterns = [re.compile(pattern) for pattern in self.exclude_file_patterns]
        for start_dir in start_dirs:
            for pattern in patterns:
                # Ищем файлы по шаблонам
                for file_path in start_dir.rglob(pattern):
                    # Проверка исключаемых директорий
                    if any(exclude_dir in file_path.parts for exclude_dir in self.exclude_dirs):
                        pprint(f'Пропускаю файл в исключенной директории: {file_path}', text_color='cyan')
                        continue
                    # Проверка на соответствие паттернам исключаемых файлов
                    if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                        pprint(f'Пропускаю файл по паттерну исключения: {file_path}', text_color='cyan')
                        continue
                    # Проверка на наличие файла в списке исключаемых файлов
                    if str(file_path) in self.exclude_files:
                        pprint(f'Пропускаю исключенный файл: {file_path}', text_color='cyan')
                        continue
                    try:
                        # Читаем содержимое файла
                        content = file_path.read_text(encoding='utf-8')
                        yield file_path, content
                    except Exception as ex:
                        pprint(f'Ошибка при чтении файла: {ex}', text_color='red', bg_color='light_grey' )
                        yield None, None

    def save_response(self, file_path: Path, response: str, model_name: str):
        """Сохранение ответа модели в файл."""
        output_directory: str = getattr(self.settings.output_directory, self.role)  
        print(f'{file_path=}')
        target_dir = 'docs/' + output_directory.replace("<model>", model_name).replace("<lang>", self.lang)
        print(f'{target_dir=}')
        # Изменение суффикса файла на .md
        file_path = str(file_path).replace('src', target_dir)  # Convert Path to string for replace
        export_path = Path(file_path).with_suffix('.md')  # Convert back to Path and change suffix
        print(f'{export_path=}')
        export_path.parent.mkdir(parents=True, exist_ok=True)
        export_path.write_text(response, encoding="utf-8")
        pprint(f"Ответ модели сохранен в: {export_path}", text_color='green')

    def parse_args(self):
        """Обработка аргументов командной строки."""
        parser = argparse.ArgumentParser(description='Code Assistant: обучение модели на основе кода.')
        parser.add_argument('--role', type=str, help='Роль для выполнения задачи')
        parser.add_argument('--lang', type=str, help='Язык выполнения')
        parser.add_argument('--models', type=str, nargs='+', help='Список моделей для инициализации')
        parser.add_argument('--start_dirs', type=Path, nargs='+', help='Список стартовых директорий')
        args = parser.parse_args()
        
        # Создаем словарь с аргументами командной строки
        cli_args = {
            'role': args.role,
            'lang': args.lang,
            'model': args.models,
            'start_dirs': args.start_dirs
        }
        pprint(f'{cli_args=}')
        return cli_args

    def run(self):
        """Запуск ассистента для обработки файлов."""
        signal.signal(signal.SIGINT, self.signal_handler)
    
        # Выполняем _payload после парсинга аргументов
        if not self._payload():
            logger.error('Ошибка при инициализации _payload()')
            return
    
        # Запускаем обработку файлов
        self.process_files()

if __name__ == '__main__':
    assistant = CodeAssistant()
    assistant.parse_args()
    assistant.run()

