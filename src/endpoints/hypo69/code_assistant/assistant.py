## \file hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.hypo69.code_assistant """
import re
import sys
import time
import signal
import argparse
from pathlib import Path
from typing import Iterator, List
from pydantic import BaseModel, Field

from __init__ import gs
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.file import read_text_file
from src.logger import logger

class CodeAssistant(BaseModel):
    """Класс CodeAssistant для обработки файлов и взаимодействия с моделями."""

    role: str = Field(default="doc_creator", description="Роль для выполнения задачи")
    lang: str = Field(default="EN", description="Язык выполнения")
    models: List[str] = Field(default=["gemini"], description="Список моделей для инициализации: ['gemini', 'openai']")

    gemini_generation_config: dict = Field(
        default_factory=lambda: {"response_mime_type": "text/plain"},
        description="Конфигурация генерации для модели Gemini"
    )
    gemini_model_name: str = "gemini-1.5-flash-8b"
    gemini_model: GoogleGenerativeAI | None = None

    openai_model_name: str = "gpt-4o-mini"
    openai_assistant_id: str = gs.credentials.openai.assistant_id.code_assistant
    openai_model: OpenAIModel | None = None

    class Config:
        """Конфигурация модели Pydantic."""
        arbitrary_types_allowed = True  # Разрешить произвольные типы

    def signal_handler(self, sig, frame):
        """Обработчик сигнала для завершения работы программы через CTRL+C."""
        logger.info("\nПрограмма завершена пользователем.")
        sys.exit(0)

def initialize_models(self, role: str, lang: str):
    """Инициализация моделей на основе роли и языка."""
    if role == 'code_checker':
        comment_for_model_about_piece_of_code = f'code_checker_{lang}.md'
        system_instruction: str = f'improve_code.md'
        # model = gemini_model  # Используем модель Gemini для проверки кода
    elif role == 'doc_creator':
        comment_for_model_about_piece_of_code = f'doc_creator_{lang}.md'
        system_instruction: str = f'create_documentation.md'
        # model = openai_model  # Используем модель OpenAI для создания документации

    # Чтение инструкций для модели
    comment_for_model_about_piece_of_code = read_text_file(
        gs.path.src / 'endpoints' / 'hypo69' / 'onela_bot' / 'instructions' / comment_for_model_about_piece_of_code
    )
    system_instruction = read_text_file(gs.path.src / "ai" / "prompts" / "developer" / system_instruction)

    gemini_model = GoogleGenerativeAI(
        api_key=gs.credentials.gemini.onela,
        model_name=self.gemini_model_name,
        system_instruction=system_instruction,
        generation_config=self.gemini_generation_config,
    )

    # Для OpenAI модели
    openai_model = OpenAIModel(
        system_instruction=system_instruction,
        model_name=self.openai_model_name,
        assistant_id=self.openai_assistant_id
    )

    return gemini_model, openai_model, comment_for_model_about_piece_of_code

    def initialize_models(self, role: str, lang: str):
        """Инициализация моделей на основе роли и языка."""
        if role == 'code_checker':
            comment_for_model_about_piece_of_code = f'code_checker_{lang}.md'
            system_instruction: str = f'improve_code.md'
            # model = gemini_model  # Используем модель Gemini для проверки кода
        elif role == 'doc_creator':
            comment_for_model_about_piece_of_code = f'doc_creator_{lang}.md'
            system_instruction: str = f'create_documentation.md'
            # model = openai_model  # Используем модель OpenAI для создания документации

        # Чтение инструкций для модели
        comment_for_model_about_piece_of_code = read_text_file(
            gs.path.src / 'endpoints' / 'hypo69' / 'onela_bot' / 'instructions' / comment_for_model_about_piece_of_code
        )
        system_instruction = read_text_file(gs.path.src / "ai" / "prompts" / "developer" / system_instruction)

        gemini_model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.onela,
            model_name=self.gemini_model_name,
            system_instruction=system_instruction,
            generation_config=self.gemini_generation_config,
        )

        # Для OpenAI модели
        openai_model = OpenAIModel(
            system_instruction=system_instruction,
            model_name=self.openai_model_name,
            assistant_id=self.openai_assistant_id
        )

        return gemini_model, openai_model, comment_for_model_about_piece_of_code

    def process_files(self):
        """Основной процесс обработки файлов и взаимодействия с моделями."""
        gemini_model, openai_model, comment_for_model_about_piece_of_code = self.initialize_models(self.role, self.lang)

        for file_path, content in self.yield_files_content(gs.path.src, ['*.py', 'README.MD'], self.role):
            # Конструируем входные данные для модели
            content = (
                f"{comment_for_model_about_piece_of_code}\n"
                f"Расположение файла в проекте: `{file_path}`.\n"
                f"Роль выполнения: `{self.role}`.\n"
                "Код:\n\n"
                f"```{content}```\n"
            )

            # Обработка через Gemini модель
            if gemini_model:
                gemini_response = gemini_model.ask(content)
                if gemini_response:
                    self.save_response(file_path, gemini_response, 'gemini')

            # Обработка через OpenAI модель
            if openai_model:
                openai_response = openai_model.ask(content)
                if openai_response:
                    self.save_response(file_path, openai_response, 'openai')

            time.sleep(120)

        """Инициализация моделей на основе указанных в self.models."""
        if 'gemini' in self.models:
            self.gemini_model = GoogleGenerativeAI(
                api_key=gs.credentials.gemini.onela,
                model_name=self.gemini_model_name,  # Передаем имя модели
                system_instruction="Ваши инструкции для Gemini",  # Убедитесь, что вы передаете правильное значение
                generation_config=self.gemini_generation_config  # Конфигурация для Gemini
            )
            logger.info(f"Модель Gemini {self.gemini_model_name} инициализирована.")

        if 'openai' in self.models:
            self.openai_model = OpenAIModel(
                model_name=self.openai_model_name, 
                assistant_id=self.openai_assistant_id
            )
            logger.info(f"Модель OpenAI {self.openai_model_name} инициализирована.")


    def get_role_directory(self, from_model: str) -> str:
        """Получение директории для роли в зависимости от модели и языка."""
        return {
            'doc_creator': f'docs/rst_from_{from_model}/{self.lang}',
            'code_checker': f'docs/consultant_{from_model}/{self.lang}',
        }.get(self.role, None)

    def save_response(self, file_path: Path, response: str, from_model: str) -> None:
        """Сохранение ответа модели в файл Markdown."""
        role_directory = self.get_role_directory(from_model)
        if not role_directory:
            logger.error(f"Неизвестная роль: {self.role}. Файл не будет сохранен.")
            return

        export_file_path = self.build_export_path(file_path, role_directory)
        export_file_path.parent.mkdir(parents=True, exist_ok=True)
        export_file_path.write_text(response, encoding="utf-8")
        logger.info(f"Response saved to: {export_file_path} at: {gs.now}")

    def build_export_path(self, file_path: Path, role_directory: str) -> Path:
        """Формирование нового пути файла с заменой 'src' на роль."""
        export_file_path = file_path.parts
        new_parts = [
            role_directory if part == 'src' else part
            for part in export_file_path
        ]
        return Path(*new_parts).with_suffix(".md")

    def yield_files_content(self, src_path: Path, patterns: list[str], from_model: str) -> Iterator[tuple[Path, str]]:
        """Итерация по файлам, соответствующим паттернам, и их содержимому."""
        exclude_file_patterns = [
                    re.compile(r'.*\(.*\).*'),
                    re.compile(r'___+.*'),
                    re.compile(r'___+')
                    ]
        exclude_dirs = {'.ipynb_checkpoints', '_experiments', 'db', '__pycache__', '_examples', '.git', '.venv'}
        exclude_files = {'version.py'}

        role_directories = {
            'doc_creator': f'docs/raw_rst_from_{from_model}/{self.lang}',
            'code_checker': f'consultant/{from_model}/{self.lang}',
        }

        target_directory = role_directories.get(self.role, None)
        if not target_directory:
            logger.info(f"Неизвестная роль: {self.role}. Пропускаем обработку файлов.")
            ...
            #return

        for pattern in patterns:
            for file_path in src_path.rglob(pattern):
                if any(exclude_dir in file_path.parts for exclude_dir in exclude_dirs):
                    continue
                if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                    continue
                if file_path.name in exclude_files:
                    logger.info(f"Исключён файл: {file_path}. Пропускаем.")
                    continue

                export_file_path = self.build_export_path(file_path, target_directory)
                if export_file_path.exists():
                    logger.info(f"Файл уже обработан и существует: {export_file_path}. Пропускаем.")
                    continue

                content = file_path.read_text(encoding="utf-8")
                yield file_path, content

    def process_files(self) -> None:
        """Основной процесс обработки файлов и взаимодействия с моделями."""
        self.initialize_models()
        for file_path, content in self.yield_files_content(gs.path.src, ['*.py', 'README.MD'], 'gemini'):
            prompt = (
                f"{self.role}_{self.lang}.md\n"
                f"Расположение файла в проекте: `{file_path}`.\n"
                f"Роль выполнения: `{self.role}`.\nКод:\n\n```{content}```\n"
            )
            if self.gemini_model:
                response = self.gemini_model.ask(prompt)
                if response:
                    self.save_response(file_path, response, 'gemini')
            if self.openai_model:
                response = self.openai_model.ask(prompt)
                if response:
                    self.save_response(file_path, response, 'openai')
            time.sleep(120)

    def run(self):
        """Запуск основного цикла выполнения."""
        signal.signal(signal.SIGINT, self.signal_handler)  # Устанавливаем обработчик сигнала
        self.parse_args()
        while True:
            self.process_files()

    def parse_args(self):
        """Обработка аргументов командной строки с помощью argparse."""
        parser = argparse.ArgumentParser(description="Code Assistant: обработка файлов и взаимодействие с моделями.")
        parser.add_argument('--role', type=str, default='doc_creator', choices=['doc_creator', 'code_checker'], help='Роль для выполнения задачи')
        parser.add_argument('--lang', type=str, default='EN', choices=['en', 'ru'], help='Язык выполнения')
        parser.add_argument('--models', type=str, nargs='+', default=['gemini'], choices=['gemini', 'openai'], help='Список моделей для инициализации')

        args = parser.parse_args()
        self.role = args.role
        self.lang = args.lang
        self.models = args.models

if __name__ == "__main__":
    """
    Пример запуска:

    1. Запуск с указанием роли 'doc_creator', языка 'ru' и моделей 'gemini' и 'openai':
        python assistant.py --role doc_creator --lang ru --models gemini openai

    2. Запуск с указанием роли 'code_checker', языка 'en' и только модели 'gemini':
        python assistant.py --role code_checker --lang en --models gemini

    3. Запуск с указанием роли 'doc_creator', языка 'en' и только модели 'openai':
        python assistant.py --role doc_creator --lang en --models openai
    """
    print("Starting Code Assistant...")
    assistant = CodeAssistant(role='doc_creator', lang='ru', models=['gemini'])
    assistant.run()
