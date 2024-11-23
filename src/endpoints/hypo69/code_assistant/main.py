## \file hypotez/src/endpoints/hypo69/code_assistant/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.hypo69.code_assistant 
	:platform: Windows, Unix
	:synopsis:





Примеры запуска:
1. Запуск с готовыми настройками:
    python main.py --settings settings.json

2. Запуск с указанием роли 'doc_writer', языка 'ru', моделей 'gemini' и 'openai', а также стартовых директорий:
    python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2

3. Запуск с указанием роли 'code_checker', языка 'en' и только модели 'gemini', а также стартовой директории:
    python main.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir

4. Запуск с указанием роли 'doc_writer', языка 'en' и только модели 'openai':
    python main.py --role doc_writer --lang en --models openai
"""
MODE = 'dev'

import argparse
import json
from pathlib import Path
from .assistant import CodeAssistant


def parse_args() -> dict:
    """Парсинг аргументов командной строки.

    Returns:
        dict: Словарь с параметрами запуска.
    """
    parser = argparse.ArgumentParser(description='Code Assistant CLI')

    parser.add_argument(
        '--settings',
        type=str,
        help='Путь к файлу настроек JSON.',
    )
    parser.add_argument(
        '--role',
        type=str,
        choices=['code_checker', 'code_analyzer', 'doc_writer', 'tests_creator'],
        help='Выбор роли ассистента.',
    )
    parser.add_argument(
        '--lang',
        type=str,
        choices=['ru', 'en'],
        default='en',
        help='Выбор языка.',
    )
    parser.add_argument(
        '--models',
        type=str,
        nargs='+',
        choices=['gemini', 'openai'],
        help='Список моделей для использования.',
    )
    parser.add_argument(
        '--start_dirs',
        type=str,
        nargs='+',
        help='Список стартовых директорий.',
    )

    return vars(parser.parse_args())


def main():
    """Главная функция запуска CodeAssistant с параметрами из командной строки или файла настроек."""
    print('Starting Code Assistant...')

    args = parse_args()

    # Если указан файл настроек, загружаем параметры из него
    if args.get('settings'):
        settings_path = Path(args['settings'])
        if settings_path.exists():
            with open(settings_path, 'r', encoding='utf-8') as file:
                settings = json.load(file)
            assistant = CodeAssistant(**settings)
        else:
            print(f'Файл настроек "{settings_path}" не найден.')
            return
    else:
        # Создаем экземпляр ассистента с параметрами из командной строки
        role = args.get('role')
        lang = args.get('lang', 'en')
        models = args.get('models', ['gemini'])
        start_dirs = [Path(d) for d in args.get('start_dirs', [])]

        assistant = CodeAssistant(role=role, lang=lang, model=models, start_dirs=start_dirs)

    # Инициализация и запуск обработки
    assistant.initialize_models()
    assistant.process_files()


if __name__ == '__main__':
    main()
    
