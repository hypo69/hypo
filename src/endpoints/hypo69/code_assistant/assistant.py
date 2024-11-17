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
from src.logger import logger

# Устанавливаем глобальную константу MODE


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
    basePath: Path = Field(default = gs.path.src / 'endpoints' / 'hypo69' / 'code_assistant', description="Корневая директория скрипта")
    base_output_directory: Path = Field(default = gs.path.root / 'docs' / 'ai', description="Базовая директория для сохранения результатов по ролям")

    translations: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(), description="Переводы для ролей")
    settings: SimpleNamespace = Field(default_factory=lambda: j_loads_ns(gs.path.src / 'endpoints' / 'hypo69' / 'code_assistant' / 'settings.json'), description="Настройки")

    class Config:
        arbitrary_types_allowed = True

    def signal_handler(self, sig, frame):
        """Обработчик сигнала завершения работы программы через CTRL+C."""
        logger.info("\nПрограмма завершена пользователем.")
        sys.exit(0)


    def __init__(self):
        """Выполняет инициализацию после создания объекта."""
        super().__init__()
        print("init")
        if not self._payload():
            return

    def _payload(self) -> bool:
        """Загружает настройки и инициализирует модели."""
        try:
            self.exclude_dirs = self.settings.exclude_file_patterns
            self.exclude_files = self.settings.exclude_files
            self.exclude_file_patterns = self.settings.exclude_file_patterns
        except Exception as ex:
            logger.error(f"Ошибка инициализации", ex)
            return False
        return self.initialize_models()


    def initialize_models(self) -> bool:
        """Инициализация моделей на основе роли и языка."""
        try:
            system_instruction_file = f'instruction_{self.role}_{self.lang}.md'
            system_instruction = read_text_file(self.basePath / 'instructions' / system_instruction_file)
        except Exception as ex:
            logger.error(f"Error reading instruction file:\n{system_instruction_file=}")
            return False

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
        content_request = f"""Твоя специализация: `{role_description}`.\nИнструкция для: Код:\n\n```{content}```\n"""
        return content_request

    def process_files(self):
        """Обработка файлов и взаимодействие с моделями."""
        self.translations = self.load_translations()
        for i, (file_path, content) in enumerate(self.yield_files_content( )):
            content_request = self.create_request(content, self.translations)

            if self.gemini_model:
                gemini_response = self.gemini_model.ask(content_request)
                if gemini_response:
                    print("save...")
                    self.save_response(file_path, gemini_response, 'gemini')

            # if self.openai_model:
            #     openai_response = self.openai_model.ask(content_request)
            #     if openai_response:
            #         self.save_response(file_path, openai_response, 'openai')

            logger.info(f'Processed file number: {i + 1}', None, False)
            time.sleep(120)

    def yield_files_content(self, start_dirs: List[Path] = [gs.path.src], patterns: List[str] = ['*.py', 'README.MD', 'INTRO.MD', 'README.RU.MD', 'INTRO.RU.MD']) -> Iterator[tuple[Path, str]]:
        """Итерация по файлам, соответствующим паттернам, и их содержимому."""
        exclude_file_patterns = [re.compile(pattern) for pattern in self.exclude_file_patterns]
        for start_dir in start_dirs:
            for pattern in patterns:
                for file_path in start_dir.rglob(pattern):
                    if any(exclude_dir in file_path.parts for exclude_dir in self.exclude_dirs):
                        logger.info(f"Пропускаю {file_path=}", None, False)
                        continue
                    if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                        logger.info(f"Пропускаю {file_path =}", None, False)
                        continue
                    if str(file_path) in self.exclude_files:
                        logger.info(f"Пропускаю {file_path=}", None, False)
                        continue

                    content = file_path.read_text(encoding="utf-8")
                    yield file_path, content

    def save_response(self, file_path: Path, response: str, model_name: str):
        """Сохранение ответа модели в файл."""
        output_directory: str = getattr(self.settings.output_directory, self.role)
        target_dir = self.base_output_directory / output_directory.replace("<model>", model_name).replace("<lang>", self.lang)
    
        # Изменение суффикса файла на .md
        export_path = Path(target_dir) / file_path.with_suffix('.md').name
    
        export_path.parent.mkdir(parents=True, exist_ok=True)
        export_path.write_text(response, encoding="utf-8")
        logger.info(f"Ответ модели сохранен в: {export_path}", None, False)


    def parse_args(self):
        """Обработка аргументов командной строки."""
        parser = argparse.ArgumentParser(description="Code Assistant: обучение модели на основе кода.")
        parser.add_argument('--settings', type=Path, help='Путь к JSON файлу настроек')
        parser.add_argument('--role', type=str, help='Роль для выполнения задачи')
        parser.add_argument('--lang', type=str, help='Язык выполнения')
        parser.add_argument('--models', type=str, nargs='+', help='Список моделей для инициализации')
        parser.add_argument('--start_dirs', type=Path, nargs='+', help='Список стартовых директорий')
        args = parser.parse_args()

        if args.settings:
            settings = j_loads(args.settings)  # Используем j_loads для загрузки настроек
            self.role = settings.get("role", "doc_creator")
            self.lang = settings.get("lang", "EN")
            self.model = settings.get("model", ["gemini"])
            self.start_dirs = [Path(gs.path.root) / d for d in settings.get("start_dirs", [])]
            self.gemini_generation_config = settings.get("gemini_generation_config", {})
            self.gemini_model_name = settings.get("gemini_model_name", "gemini-1.5-flash-8b")
            self.openai_model_name = settings.get("openai_model_name", "gpt-4o-mini")
            self.openai_assistant_id = settings.get("openai_assistant_id", "")
            self.exclude_file_patterns = settings.get("exclude_file_patterns", [])
            self.exclude_dirs = settings.get("exclude_dirs", [])
            self.exclude_files = settings.get("exclude_files", [])
            self.base_output_directory = Path(settings.get("base_output_directory", str(self.base_output_directory)))
            self.basePath = Path(settings.get("basePath", str(self.basePath)))

        self._payload()

    def run(self):
        """Запуск ассистента для обработки файлов."""
        signal.signal(signal.SIGINT, self.signal_handler)
        self.parse_args()
        self.process_files()


    def parse_args(self):
        """Обработка аргументов командной строки."""
        parser = argparse.ArgumentParser(description="Code Assistant: обучение модели на основе кода.")
        parser.add_argument('--settings', type=Path, help='Путь к JSON файлу настроек')
        parser.add_argument('--role', type=str, help='Роль для выполнения задачи')
        parser.add_argument('--lang', type=str, help='Язык выполнения')
        parser.add_argument('--models', type=str, nargs='+', help='Список моделей для инициализации')
        parser.add_argument('--start_dirs', type=Path, nargs='+', help='Список стартовых директорий')
        args = parser.parse_args()

        if args.settings:
            settings = j_loads(args.settings)  # Используем j_loads для загрузки настроек
            self.role = settings.get("role", "doc_creator")
            self.lang = settings.get("lang", "EN")
            self.model = settings.get("model", ["gemini"])
            self.start_dirs = [Path(gs.path.root) / d for d in settings.get("start_dirs", [])]
            self.gemini_generation_config = settings.get("gemini_generation_config", {})
            self.gemini_model_name = settings.get("gemini_model_name", "gemini-1.5-flash-8b")
            self.openai_model_name = settings.get("openai_model_name", "gpt-4o-mini")
            self.openai_assistant_id = settings.get("openai_assistant_id", "")
            self.exclude_file_patterns = settings.get("exclude_file_patterns", [])
            self.exclude_dirs = settings.get("exclude_dirs", [])
            self.exclude_files = settings.get("exclude_files", [])
            self.role_directories = settings.get("role_directories", {})

        # Устанавливаем аргументы командной строки
        if args.role:
            self.role = args.role
        if args.lang:
            self.lang = args.lang
        if args.models:
            self.model = args.models
        if args.start_dirs:
            self.start_dirs = args.start_dirs

if __name__ == "__main__":
    assistant = CodeAssistant()
    assistant.parse_args()
    #assistant.signal_handler(signal.SIGINT, None)
    assistant.initialize_models()
    assistant.process_files()
