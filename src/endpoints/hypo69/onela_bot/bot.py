## \file hypotez/src/endpoints/hypo69/onela_bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.hypo69 """

""" Отсылатель кода в модель gemini
https://stackoverflow.com/questions/78382534/googlegenerativeaierror-error-embedding-contentmodels-embeddings-001-is-not-fo
"""
...
import re
from pathlib import Path
import time

from __init__ import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import yield_files_content, read_text_file
from src.logger import logger

system_instruction: str = read_text_file(
    gs.path.src / "ai" / "prompts" / "developer" / "improve_code.md"
)
generation_config: dict = {"response_mime_type": "text/plain"}
model_name: str = "gemini-1.5-flash-8b"
model: GoogleGenerativeAI = GoogleGenerativeAI(
    api_key=gs.credentials.gemini.onela,
    model_name=model_name,
    system_instruction=system_instruction,
    generation_config=generation_config,
)

import time
from pathlib import Path
from typing import Iterator


def main() -> None:
    """! Main function to process files and interact with the model.

    This function reads a comment file, iterates over specified files in the source directory,
    and sends the file content to a model for analysis. It then processes the model's response.
    """

    global model

    # Read the comment for model input from a markdown file
    comment_for_model_about_piece_of_code: str = read_text_file(
        gs.path.src / 'endpoints' / 'hypo69' / 'onela_bot' / 'instructions' / 'input_output.md'
    )

    # Process each file based on the specified patterns
    for file_path, content in yield_files_content(
        #gs.path.src, ["*.py", "*.txt", "*.md", "*.json", "*.dot"]
        gs.path.src, ["*.py"]
    ):
        # Construct the input content for the model
        content: str = (
            f"{comment_for_model_about_piece_of_code}\n"
            f"Расположение файла в проекте: `{file_path}`.\n"
            "Код:\n\n"
            f"```{content}```\n"
        )
        try:
            # Get the response from the model
            response = model.ask(content)

            # Save the model's response, changing the file suffix to `.md`
            save_response(file_path, response)
        except Exception as ex:
            logger.error(ex)
            ...
        # Optional sleep to prevent API rate limits or throttling
        time.sleep(20)


def save_response(file_path: Path, response: str) -> None:
    """! Save the model's response to a markdown file with updated path.

    Args:
        file_path (Path): The original file path being processed.
        response (str): The response from the model to be saved.

    This function modifies the original file path's suffix to `.md` and saves the response as a markdown file.
    """
    # Заменить часть пути 'src' на 'gemini_consultatnt'
    export_file_path = file_path.parts
    new_parts = []
    
    for part in export_file_path:
        if part == 'src':
            new_parts.append('gemini_consultant')
        else:
            new_parts.append(part)
    
    # Сформировать новый путь с замененной частью
    export_file_path = Path(*new_parts)
    
    # Убедиться, что директория существует
    export_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Сохранить ответ в новый файл
    export_file_path.write_text(response, encoding="utf-8")
    print(f"Response saved to: {export_file_path}")



def yield_files_content(
    src_path: Path, patterns: list[str]
) -> Iterator[tuple[Path, str]]:
    """! Yield file content based on patterns from the source directory, excluding certain patterns.

    Args:
        src_path (Path): The base directory to search for files.
        patterns (list[str]): List of file patterns to include (e.g., ['*.py', '*.txt']).

    Yields:
        Iterator[tuple[Path, str]]: A tuple of file path and its content as a string.
    """
    # Регулярные выражения для исключаемых файлов
    exclude_patterns = [
        re.compile(r'.*\(.*\).*'),  # Файлы с круглыми скобками
        re.compile(r'___.*\..*'),   # Файлы, начинающиеся с трех подчеркиваний
    ]
    
    for pattern in patterns:
        for file_path in src_path.rglob(pattern):
            # Пропустить файлы, которые соответствуют исключаемым паттернам
            if any(exclude.match(str(file_path)) for exclude in exclude_patterns):
                continue

            # Чтение содержимого файла
            content = file_path.read_text(encoding="utf-8")
            yield file_path, content


if __name__ == "__main__":
    print(f"Starting trainig ...")
    main()
