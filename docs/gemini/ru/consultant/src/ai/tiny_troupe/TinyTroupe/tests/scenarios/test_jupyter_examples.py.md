# Анализ кода модуля `test_jupyter_examples.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используются параметризованные тесты pytest для перебора всех ноутбуков.
    - Есть обработка ошибок при выполнении ноутбуков.
    - Сохраняется копия исполненного ноутбука.
- Минусы
    - Не используются константы для magic strings (`.ipynb`, `.executed.local.ipynb`).
    - Нет документации в формате RST для функций.
    - Не используется `from src.logger import logger` для логирования.
    - Пути к файлам заданы строками, лучше использовать `pathlib.Path`.
    - Есть несколько `sys.path.insert(0, ...)` что может запутать при отладке

**Рекомендации по улучшению**
1. Добавить описание модуля в начале файла.
2. Добавить документацию в формате RST для функций `get_notebooks` и `test_notebook_execution`.
3. Использовать `pathlib.Path` для работы с путями.
4. Использовать константы для расширений файлов (`.ipynb`, `.executed.local.ipynb`).
5. Использовать `from src.logger.logger import logger` для логирования ошибок.
6. Избегать избыточного использования `try-except`, перенаправляя ошибки в `logger.error`.
7. Переименовать `NOTEBOOK_FOLDER` в `NOTEBOOKS_DIR` для единообразия.
8. Заменить `sys.path.insert(0, ...)` на `PYTHONPATH`
9. Убрать `print` заменив на `logger.info` и `logger.error`

**Оптимизированный код**
```python
"""
Модуль для тестирования Jupyter Notebooks.
=========================================================================================

Этот модуль содержит функции для автоматического выполнения Jupyter Notebooks
и проверки на наличие ошибок.

Пример использования
--------------------

Запуск тестов:

.. code-block:: bash

    pytest tests/scenarios/test_jupyter_examples.py
"""
import os
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
# from src.logger import logger  # перенесено в начало
from src.logger.logger import logger  # импорт logger
import sys
# sys.path.insert(0, '../../tinytroupe/') # ensures that the package is imported from the parent directory, not the Python installation #TODO перенести в PYTHONPATH
# sys.path.insert(0, '../../') # ensures that the package is imported from the parent directory, not the Python installation #TODO перенести в PYTHONPATH
# sys.path.insert(0, '../') # ensures that the package is imported from the parent directory, not the Python installation #TODO перенести в PYTHONPATH

# Set the folder containing the notebooks
NOTEBOOKS_DIR = Path("../examples/")  # Update this path
NOTEBOOK_EXTENSION = ".ipynb" # константа для расширения файлов
EXECUTED_NOTEBOOK_EXTENSION = ".executed.local.ipynb" # константа для расширения исполненных файлов

# Set a timeout for long-running notebooks
TIMEOUT = 600

KERNEL_NAME = "python3" # "py310"


def get_notebooks(folder: Path) -> list[str]:
    """
    Получает список всех Jupyter notebook файлов из указанной папки.

    Args:
        folder (Path): Путь к папке с ноутбуками.

    Returns:
        list[str]: Список путей к файлам ноутбуков.
    """
    return [
        str(folder / f)
        for f in os.listdir(folder)
        if f.endswith(NOTEBOOK_EXTENSION) and not ".executed." in f and not ".local." in f
    ]


@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOKS_DIR))
def test_notebook_execution(notebook_path: str):
    """
    Исполняет Jupyter notebook и проверяет, что не возникает исключений.

    Args:
        notebook_path (str): Путь к файлу ноутбука.
    """
    notebook_path = Path(notebook_path)
    try:
        with open(notebook_path, "r", encoding="utf-8") as nb_file:
            notebook = nbformat.read(nb_file, as_version=4)
            logger.info(f"Executing notebook: {notebook_path} with kernel: {KERNEL_NAME}")
            ep = ExecutePreprocessor(timeout=TIMEOUT, kernel_name=KERNEL_NAME)
            ep.preprocess(notebook, {'metadata': {'path': str(NOTEBOOKS_DIR)}})
            logger.info(f"Notebook {notebook_path} executed successfully.")
    except Exception as e:
        logger.error(f"Notebook {notebook_path} raised an exception: {e}")
        pytest.fail(f"Notebook {notebook_path} raised an exception: {e}")
    finally:
        # save a copy of the executed notebook
        output_path = notebook_path.with_suffix(EXECUTED_NOTEBOOK_EXTENSION)
        with open(output_path, "w", encoding="utf-8") as out_file:
            nbformat.write(notebook, out_file)
        logger.info(f"Executed notebook saved as: {output_path}")
```