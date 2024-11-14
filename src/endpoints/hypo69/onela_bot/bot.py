import re
from pathlib import Path
import time
import argparse
from typing import Iterator
import signal
import sys

from __init__ import gs
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.utils.file import yield_files_content, read_text_file
from src.logger import logger

# Глобальная переменная для роли
role: str = None

gemini_generation_config: dict = {"response_mime_type": "text/plain"}
gemini_model_name: str = "gemini-1.5-flash-8b"
gemini_model: GoogleGenerativeAI

openai_model_name = 'gpt-4o-mini'
openai_assistant_id = gs.credentials.openai.assistant_id.code_assistant


def parse_args() -> None:
    """Парсинг аргументов командной строки для задания роли."""
    global role
    parser = argparse.ArgumentParser(description="Запуск onela_bot с указанием роли")
    parser.add_argument("--role", type=str, required=True, help="Укажите роль (например, code_checker)")
    try:
        args = parser.parse_args()
        role = args.role
    except Exception as ex:
        role = 'code_checker'
    print(f'{role=}')


def signal_handler(sig, frame):
    """Обработчик сигнала для завершения работы программы через CTRL+C."""
    print("\nПрограмма завершена пользователем.")
    sys.exit(0)


def main() -> None:
    """ Main function to process files and interact with the model. """
    global gemini_model, openai_model, role

    role = role if role else 'doc_creator'

    if role == 'code_checker':
        comment_for_model_about_piece_of_code = 'code_checker.md'
        system_instruction: str = 'improve_code.md'
        #model = gemini_model  # Use Gemini model for code checking
    elif role == 'doc_creator':
        comment_for_model_about_piece_of_code = 'doc_creator.md'
        system_instruction: str = 'create_documentation.md'
        #model = openai_model  # Use OpenAI model for documentation creation

    # Read the comment for model input from a markdown file
    comment_for_model_about_piece_of_code = read_text_file(
        gs.path.src / 'endpoints' / 'hypo69' / 'onela_bot' / 'instructions' / comment_for_model_about_piece_of_code
    )
    system_instruction = read_text_file(gs.path.src / "ai" / "prompts" / "developer" / system_instruction)

    gemini_model = GoogleGenerativeAI(
        api_key=gs.credentials.gemini.onela,
        model_name=gemini_model_name,
        system_instruction=system_instruction,
        generation_config=gemini_generation_config,
    )
    ...
    # openai_model = OpenAIModel(
    #     system_instruction=system_instruction,
    #     model_name=openai_model_name,
    #     assistant_id=openai_assistant_id
    # )
    ...


    # Process each file based on the specified patterns
    for file_path, content in yield_files_content(
        gs.path.src, ['*.py', 'README.MD']
    ):
        # Construct the input content for the model
        content = (
            f"{comment_for_model_about_piece_of_code}\n"
            f"Расположение файла в проекте: `{file_path}`.\n"
            f"Роль выполнения: `{role}`.\n"
            "Код:\n\n"
            f"```{content}```\n"
        )

        gemini_response = gemini_model.ask(content)
        if gemini_response:
            save_response(file_path = file_path, response = gemini_response, from_model = 'gemini')
        else:
            timeout:int = 3600
            print(f'pause at: {gs.now}\ntimeout: {timeout/60=} min')
            time.sleep(timeout)
            ... # <- add logic for failed response

        # openai_response = openai_model.ask(content)
        # if openai_response:
        #     save_response(file_path = file_path, response = openai_response, from_model = 'openai')
        # else:
        #     ... # <- add logic for failed response

        time.sleep(120) # <- Optional sleep to prevent API rate limits or throttling


def save_response(file_path: Path, response: str, from_model:str) -> None:
    """ Save the model's response to a markdown file with updated path based on role. """
    global role

    # Словарь, ассоциирующий роли с директориями
    role_directories = {
        'doc_creator': f'docs/raw_rst_from_{from_model}',
        'code_checker': f'consultant/{from_model}',
    }

    # Проверка наличия роли в словаре
    if role not in role_directories:
        logger.error(f"Неизвестная роль: {role}. Файл не будет сохранен.")
        return

    # Получаем директорию, соответствующую роли
    role_directory = role_directories[role]

    # Формируем новый путь с учетом роли
    export_file_path = file_path.parts
    new_parts = []

    for part in export_file_path:
        if part == 'src':
            new_parts.append(role_directory)
        else:
            new_parts.append(part)

    # Сформировать новый путь с замененной частью
    export_file_path = Path(*new_parts)

    # Изменить суффикс файла на .md
    export_file_path = export_file_path.with_suffix(".md")

    # Убедиться, что директория существует
    export_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Сохранить ответ в новый файл
    export_file_path.write_text(response, encoding="utf-8")
    print(f"Response saved to: {export_file_path}")


def yield_files_content(
    src_path: Path, patterns: list[str]
) -> Iterator[tuple[Path, str]]:
    """ Yield file content based on patterns from the source directory, excluding certain patterns and directories. """
    # Регулярные выражения для исключаемых файлов и директорий
    exclude_file_patterns = [
        re.compile(r'.*\(.*\).*'),  # Файлы и директории, содержащие круглые скобки
        re.compile(r'___+.*'),      # Файлы или директории, начинающиеся с трех и более подчеркиваний
    ]

    # Список служебных директорий, которые необходимо исключить
    exclude_dirs = {'.ipynb_checkpoints', '_experiments', '__pycache__', '.git', '.venv'}

    # Словарь с путями к целевым директориям, где будут сохраняться файлы
    role_directories = {
        'doc_creator': 'docs/openai/raw_rst_from_ai',
        'code_checker': 'consultant/gemini',
    }

    # Получаем директорию, соответствующую роли
    target_directory = role_directories.get(role, None)

    if target_directory is None:
        logger.error(f"Неизвестная роль: {role}. Пропускаем обработку файлов.")
        return

    for pattern in patterns:
        for file_path in src_path.rglob(pattern):
            # Пропустить файлы, которые находятся в исключаемых директориях
            if any(exclude_dir in file_path.parts for exclude_dir in exclude_dirs):
                continue

            # Пропустить файлы, соответствующие исключаемым паттернам
            if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                continue

            # Формируем путь, куда будет сохранен обработанный файл
            export_file_path = file_path.parts
            new_parts = []

            for part in export_file_path:
                if part == 'src':
                    new_parts.append(target_directory)
                else:
                    new_parts.append(part)

            export_file_path = Path(*new_parts).with_suffix(".md")

            # Пропускать файлы, если они уже существуют в целевой папке
            if export_file_path.exists():
                print(f"Файл уже обработан и существует: {export_file_path}. Пропускаем.")
                continue

            # Чтение содержимого файла
            content = file_path.read_text(encoding="utf-8")
            yield file_path, content


if __name__ == "__main__":
    print("Starting training ...")
    signal.signal(signal.SIGINT, signal_handler)  #  обработчик сигнала (`CTRL+C` etc)
    try:
        parse_args()  # Парсим аргументы командной строки
    except Exception as ex:
        #При запуске из IDE
        role = 'doc_creator'
    while True:
        main()
