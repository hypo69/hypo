## \file hypotez/src/ai/gemini/version.py
# -*- coding: utf-8 -*-

""" module: src.ai.gemini """
MODE = 'debug'
""" module: src.ai.gemini """
MODE = 'debug'
...
import json
import sys
from pathlib import Path

def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    current_path = Path(__file__).resolve().parent
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            return parent
    return current_path


# Define project root
__root__: Path = get_project_root()

if __root__ not in sys.path:
    sys.path.insert(0, str(__root__))

try:
    settings:dict = None
    with open(__root__ / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)

    __project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
    __version__: str = settings.get("version", '')  if settings  else ''
    __doc__: str = ''
    __details__: str = ''
    __author__: str = settings.get("author", '')  if settings  else ''
    __copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
    __cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

except (FileNotFoundError, json.JSONDecodeError) as ex:
    ...
    print(f"Ошибка", ex)
             