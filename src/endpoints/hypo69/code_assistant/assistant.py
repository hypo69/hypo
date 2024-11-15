## \file hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*- 
"""Класс обучения ассистента программиста."""
import re
import sys
import time
import signal
import json
import argparse
from pathlib import Path
from typing import Iterator, List, Optional
from pydantic import BaseModel, Field

from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.file import read_text_file
from src.logger import logger


class CodeAssistant(BaseModel):
    """Класс обучения ассистента программиста."""

    role: str = Field(description="Роль для выполнения задачи")
    lang: str = Field(description="Язык выполнения")
    model: List[str] = Field(description="Список моделей для инициализации")
    start_dirs: List[Path] = Field(default_factory=list, description="Список стартовых директорий для обработки")

    gemini_generation_config: dict = Field(description="Конфигурация генерации для модели Gemini")
    gemini_model_name: str = Field(description="Название модели Gemini")
    gemini_model: Optional[GoogleGenerativeAI] = None

    openai_model_name: str = Field(description="Название модели OpenAI")
    openai_assistant_id: str = Field(description="ID ассистента OpenAI")
    openai_model: Optional[OpenAIModel] = None

    exclude_file_patterns: List[str] = Field(description="Список паттернов для исключения файлов")
    exclude_dirs: List[str] = Field(description="Список директорий для исключения")
    exclude_files: List[str] = Field(description="Список файлов для исключения")
    role_directories: dict = Field(description="Директории для сохранения результатов по ролям")

    class Config:
        arbitrary_types_allowed = True

    def signal_handler(self, sig, frame):
        """Обработчик сигнала завершения работы программы через CTRL+C."""
        logger.info("\nПрограмма завершена пользователем.")
        sys.exit(0)

    def initialize_models(self):
        """Инициализация моделей на основе роли и языка."""
        system_instruction_file = f"{self.role}_{self.lang}.md"
        system_instruction = read_text_file(Path('src/ai/prompts/developer') / system_instruction_file)

        # Инициализация модели Gemini
        if 'gemini' in self.model:
            self.gemini_model = GoogleGenerativeAI(
                api_key=gs.credentials.gemini.onela,
                model_name=self.gemini_model_name,
                system_instruction=system_instruction,
                generation_config=self.gemini_generation_config
            )

        # Инициализация модели OpenAI
        if 'openai' in self.model:
            self.openai_model = OpenAIModel(
                system_instruction=system_instruction,
                model_name=self.openai_model_name,
                assistant_id=self.openai_assistant_id
            )

    def process_files(self):
        """Обработка файлов и взаимодействие с моделями."""
        for file_path, content in self.yield_files_content(self.start_dirs, ['*.py', 'README.MD']):
            content_request = (
                f"Роль выполнения: `{self.role}`.\nКод:\n\n```{content}```\n"
            )

            if self.gemini_model:
                gemini_response = self.gemini_model.ask(content_request)
                if gemini_response:
                    self.save_response(file_path, gemini_response, 'gemini')

            if self.openai_model:
                openai_response = self.openai_model.ask(content_request)
                if openai_response:
                    self.save_response(file_path, openai_response, 'openai')

            time.sleep(120)

    def yield_files_content(self, start_dirs: List[Path], patterns: List[str]) -> Iterator[tuple[Path, str]]:
        """Итерация по файлам, соответствующим паттернам, и их содержимому."""
        exclude_file_patterns = [re.compile(pattern) for pattern in self.exclude_file_patterns]

        for start_dir in start_dirs:
            for pattern in patterns:
                for file_path in start_dir.rglob(pattern):
                    if any(exclude_dir in file_path.parts for exclude_dir in self.exclude_dirs):
                        continue
                    if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                        continue
                    if file_path.name in self.exclude_files:
                        continue

                    content = file_path.read_text(encoding="utf-8")
                    yield file_path, content

    def save_response(self, file_path: Path, response: str, model_name: str):
        """Сохранение ответа модели в файл."""
        target_dir_template = self.role_directories.get(self.role)
        target_dir = target_dir_template.replace("<model>", model_name).replace("<lang>", self.lang)
        export_path = Path(target_dir) / file_path.name
        export_path.parent.mkdir(parents=True, exist_ok=True)
        export_path.write_text(response, encoding="utf-8")
        logger.info(f"Ответ модели сохранен в: {export_path}")

    def parse_args(self):
        """Обработка аргументов командной строки."""
        parser = argparse.ArgumentParser(description="Code Assistant: обучение модели на основе кода.")
        parser.add_argument('--settings', type=Path, help='Путь к JSON файлу настроек')
        args = parser.parse_args()

        if args.settings:
            with open(args.settings, "r") as file:
                settings = json.load(file)
                self.role = settings.get("role", "doc_creator")
                self.lang = settings.get("lang", "EN")
                self.model = settings.get("model", ["gemini"])
                self.start_dirs = [Path(d) for d in settings.get("start_dirs", [])]
                self.gemini_generation_config = settings.get("gemini_generation_config", {})
                self.gemini_model_name = settings.get("gemini_model_name", "gemini-1.5-flash-8b")
                self.openai_model_name = settings.get("openai_model_name", "gpt-4o-mini")
                self.openai_assistant_id = settings.get("openai_assistant_id", "")
                self.exclude_file_patterns = settings.get("exclude_file_patterns", [])
                self.exclude_dirs = settings.get("exclude_dirs", [])
                self.exclude_files = settings.get("exclude_files", [])
                self.role_directories = settings.get("role_directories", {})

if __name__ == "__main__":
    """
    Пример запуска:
    1. Запуск с готовыми настройками:
        python assistant.py --settings settings.json

    2. Запуск с указанием роли 'doc_creator', языка 'ru', моделей 'gemini' и 'openai', а также стартовых директорий:
        python assistant.py --role doc_creator --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2

    3. Запуск с указанием роли 'code_checker', языка 'en' и только модели 'gemini', а также стартовой директории:
        python assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir

    4. Запуск с указанием роли 'doc_creator', языка 'en' и только модели 'openai':
        python assistant.py --role doc_creator --lang en --models openai
    """
    print("Starting Code Assistant...")

    # # Пример 1: Вызов с настройками из JSON
    # # Убедитесь, что в вашей директории есть файл 'settings.json' с нужными параметрами
    # assistant = CodeAssistant()
    # assistant.parse_args()
    # assistant.initialize_models()
    # assistant.process_files()

    # # Пример 2: Вызов с явным указанием роли и настроек
    # # Можно закомментировать или раскомментировать в зависимости от того, какие параметры нужно использовать
    # """
    # assistant = CodeAssistant(role='doc_creator', lang='ru', model=['gemini', 'openai'], start_dirs=[Path('/path/to/dir1'), Path('/path/to/dir2')])
    # assistant.initialize_models()
    # assistant.process_files()
    # """
    
    # """
    # assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'], start_dirs=[Path('/path/to/dir')])
    # assistant.initialize_models()
    # assistant.process_files()
    # """

    # """
    # assistant = CodeAssistant(role='doc_creator', lang='en', model=['openai'])
    # assistant.initialize_models()
    # assistant.process_files()
    # """
