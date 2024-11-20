## \file hypotez/src/endpoints/hypo69/code_assistant/assistant.py
# -*- coding: utf-8 -*- 
#! venv/Scripts/python.exe
#! venv/bin/python
"""Модуль для работы ассистента программиста в проекте src.endpoints.hypo69.code_assistant

Этот модуль содержит класс `CodeAssistant`, который используется для работы с различными моделями ИИ, такими как Google Gemini и OpenAI,
для выполнения задач по обработке кода.

Пример использования:
    assistant = CodeAssistant()
    assistant.process_files(start_file=2)
"""

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
    """Класс обучения ассистента программиста.

    Этот класс позволяет инициализировать ассистента для выполнения задач в области разработки кода, используя различные модели ИИ,
    такие как Google Gemini и OpenAI. Он загружает настройки, файлы и обрабатывает их с использованием заданных инструкций.

    Пример:
        assistant = CodeAssistant()
        assistant.process_files(from_file=2)

    Атрибуты:
        role (str): Роль для выполнения задачи. Например, "code_checker".
        lang (str): Язык выполнения. Например, "en" или "ru".
        model (List[str]): Список моделей для инициализации. По умолчанию "gemini".
        start_dirs (List[Path]): Список стартовых директорий для обработки файлов.
        gemini_generation_config (dict): Конфигурация генерации для модели Gemini.
        gemini_model_name (str): Название модели Gemini.
        openai_model_name (str): Название модели OpenAI.
        openai_assistant_id (str): ID ассистента OpenAI.
        exclude_file_patterns (List[str]): Список паттернов для исключения файлов.
        exclude_dirs (List[str]): Список директорий для исключения.
        exclude_files (List[str]): Список файлов для исключения.
        base_path (Path): Корневая директория для скрипта.
        base_output_directory (Path): Базовая директория для сохранения результатов по ролям.
        translations (SimpleNamespace): Переводы для ролей и языков.
        config (SimpleNamespace): Настройки для конфигурации ассистента.
    """
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
    base_path: Path = Field(default=gs.path.endpoints / 'hypo69' / 'code_assistant', description="Корневая директория скрипта")
    base_output_directory: Path = Field(default=gs.path.root / 'docs' / 'ai', description="Базовая директория для сохранения результатов по ролям")

    translations: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(), description="Переводы для ролей")
    config: SimpleNamespace = Field(default_factory=lambda: j_loads_ns(gs.path.endpoints / 'hypo69' / 'code_assistant' / 'code_assistant.json'), description="Настройки")

    system_instruction_file: Path | str = Field(default="instructions", description="Инструкции перед отправкой кода в модель")

    class Config:
        arbitrary_types_allowed = True

    def signal_handler(self, sig, frame):
        """Обработчик сигнала завершения работы программы через CTRL+C.

        Этот метод завершает выполнение программы, когда пользователь нажимает CTRL+C.

        Пример:
            signal.signal(signal.SIGINT, assistant.signal_handler)
        """
        logger.info("\nПрограмма завершена пользователем.")
        sys.exit(0)

    def __init__(self):
        """Выполняет инициализацию после создания объекта.

        В этой функции инициализируются все необходимые параметры и модели, а также загружаются настройки.

        Пример:
            assistant = CodeAssistant()
        """
        super().__init__()
        pprint('CodeAssistant инициализирован', text_color='gray', bg_color='white')
        self._payload()

    def _payload(self) -> bool:
        """Загружает настройки и инициализирует модели.

        Эта функция загружает параметры из файла конфигурации и командной строки, затем инициализирует модели.

        Пример:
            assistant._payload()
        """
        try:
            # Получаем аргументы командной строки
            cli_args = self.parse_args()

            # Устанавливаем параметры: сначала значения из файла, затем перезаписываем аргументами из командной строки
            self.role = cli_args['role'] if cli_args.get('role') else self.config.get('role', 'code_checker')
            self.lang = cli_args['lang'] if cli_args.get('lang') else self.config.get('lang', 'ru')
            self.model = cli_args['model'] if cli_args.get('model') else self.config.get('model', ['gemini'])
            self.start_dirs = cli_args['start_dirs'] if cli_args.get('start_dirs') else \
                [Path(gs.path.root) / d for d in self.config.get('start_dirs', [])]

            # Загрузка остальных параметров из файла настроек
            self.gemini_generation_config = self.config.get('gemini_generation_config', {})
            self.gemini_model_name = self.config.get('gemini_model_name', 'gemini-1.5-flash-8b')
            self.openai_model_name = self.config.get('openai_model_name', 'gpt-4o-mini')
            self.openai_assistant_id = self.config.get('openai_assistant_id', '')
            self.exclude_file_patterns = self.config.get('exclude_file_patterns', [])
            self.exclude_dirs = self.config.get('exclude_dirs', [])
            self.exclude_files = self.config.get('exclude_files', [])
            self.base_output_directory = Path(self.config.get('base_output_directory', str(self.base_output_directory)))
            self.base_path = Path(self.config.get('base_path', str(self.base_path)))

        except Exception as ex:
            logger.error('Ошибка инициализации', ex)
            return False

        return self.initialize_models()

    @property
    def system_instruction(self) -> str | bool:
        """Чтение инструкции из файла.

        Эта функция пытается загрузить инструкцию из заранее заданного файла для модели. Если файл не найден или возникла ошибка,
        возвращается `False`.

        Пример:
            system_instruction = assistant.system_instruction
        """
        try:
            system_instruction: str = Path(gs.path.src / 'ai' / 'prompts' / 'developer' / f'{self.role}_{self.lang}.md').read_text(encoding='UTF-8')
            return system_instruction
        except Exception as ex:
            logger.error(f"Ошибка чтения инструкции", ex)
            return False

    @property
    def code_instruction(self) -> str | bool:
        """Чтение инструкции для кода.

        Эта функция пытается загрузить инструкцию для кода из файла. Если файл не найден или возникла ошибка, возвращается `False`.

        Пример:
            code_instruction = assistant.code_instruction
        """
        try:
            code_instruction = Path(self.base_path / 'instructions' / f'instruction_{self.role}_{self.lang}.md').read_text(encoding='UTF-8')
            return code_instruction
        except Exception as ex:
            logger.error(f"Ошибка чтения инструкции для кода", ex)
            return False

    def initialize_models(self):
        """Инициализация моделей на основе роли и языка.

        Эта функция инициализирует модели на основе роли и языка, используя параметры, переданные в конструктор.

        Пример:
            assistant.initialize_models()
        """
        try:
            if 'gemini' in self.model:
                self.gemini_model = GoogleGenerativeAI(config=self.gemini_generation_config)
            if 'openai' in self.model:
                self.openai_model = OpenAIModel(model_name=self.openai_model_name, assistant_id=self.openai_assistant_id)
            return True
        except Exception as ex:
            logger.error('Ошибка при инициализации моделей', ex)
            return False
